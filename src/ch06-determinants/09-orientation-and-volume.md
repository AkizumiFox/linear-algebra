# Orientation and Volume

The chapter began in §1 with a picture: the area of a parallelogram, with a sign attached, obeys a few simple rules, and those rules pinned down \( ad - bc \). We have since built the determinant in every size from the same rules. It is time to return to geometry and say precisely what the determinant measures. There are two halves to the answer. Its absolute value measures volume, and its sign measures orientation, the difference between a left hand and a right hand. Both halves need care. "Volume" in \( \nR^7 \) has no meaning until someone defines it, and "orientation" has no meaning at all over \( \nC \).

Throughout this section the field is \( \nR \).

## What should the volume of a parallelepiped be?

For vectors \( \a_1, \dots, \a_n \in \nR^n \), the **parallelepiped** they span is the set
\[
P(\a_1, \dots, \a_n) \coloneqq \{ t_1\a_1 + \dots + t_n\a_n : 0 \le t_i \le 1 \text{ for every } i \}.
\]
For \( n = 2 \) it is the parallelogram with sides \( \a_1, \a_2 \) at the origin, and for \( n = 3 \) a slanted box. For \( n = 1 \) it is the segment from \( 0 \) to \( \a_1 \).

We would like to say "its volume is \( \lvert \det\begin{pmatrix} \a_1 & \cdots & \a_n \end{pmatrix} \rvert \)". But a theorem needs two sides, and one side is missing: we have no definition of the volume of a subset of \( \nR^n \). School geometry supplies one for \( n = 2 \) and \( n = 3 \) through "base times height", and the proper general notion, Lebesgue measure, belongs to a course in measure theory. So we proceed honestly in three steps. We **define** the volume of a parallelepiped by the determinant. We **prove** that this is the only function obeying the rules that any reasonable notion of volume must obey. And we **state**, without proof, that it agrees with Lebesgue measure.

*The volume of a parallelepiped is the size of the determinant of its edge vectors.*

::: {#def-parallelepiped-volume}
[Volume of a Parallelepiped]

Let \( n \ge 1 \) and \( \a_1, \dots, \a_n \in \nR^n \). The (\( n \)-dimensional) **volume** of the parallelepiped spanned by \( \a_1, \dots, \a_n \) is
\[
\vol(\a_1, \dots, \a_n) \coloneqq \big\lvert \det\begin{pmatrix} \a_1 & \a_2 & \cdots & \a_n \end{pmatrix} \big\rvert \ \ge 0 .
\]
:::

In words: stack the \( n \) edge vectors as the columns of a square matrix, take its determinant, and forget the sign. There must be **exactly \( n \)** vectors in \( \nR^n \), so that the matrix is square.

**Examples.**

- The unit cube \( P(\e_1, \dots, \e_n) \) has volume \( \lvert \det \I_n \rvert = 1 \).
- A box with edges \( d_1\e_1, \dots, d_n\e_n \) has volume \( \lvert \det\diag(d_1, \dots, d_n) \rvert = \lvert d_1 \cdots d_n \rvert \) by @thm-det-triangular: the product of its side lengths, as it should be.
- The parallelepiped spanned by \( (1, 2, 0) \), \( (0, 1, 1) \), \( (1, 0, 3) \) in \( \nR^3 \) has volume
\[
\left\lvert \det\begin{pmatrix} 1 & 0 & 1 \\ 2 & 1 & 0 \\ 0 & 1 & 3 \end{pmatrix} \right\rvert = \lvert 1\cdot(3 - 0) - 0 + 1\cdot(2 - 0) \rvert = 5,
\]
expanding along the first row.
- **Degenerate case.** If \( \a_1, \dots, \a_n \) are linearly dependent, the parallelepiped is flattened into a proper subspace, and its volume is \( 0 \) by @thm-alternating-properties. For \( n = 2 \), \( P((1, 2), (2, 4)) \) is the segment from \( (0, 0) \) to \( (3, 6) \), with area \( \lvert 4 - 4 \rvert = 0 \). This case matters: "volume zero" is the geometric face of "not invertible".

**Non-example by minimal change.** Drop one vector: \( (1, 2, 0) \) and \( (0, 1, 1) \) span a genuine parallelogram in \( \nR^3 \), but the matrix \( \begin{pmatrix} 1 & 0 \\ 2 & 1 \\ 0 & 1 \end{pmatrix} \) is \( 3 \times 2 \) and has no determinant. The clause that fails is **exactly \( n \) vectors in \( \nR^n \)**. The \( 3 \)-dimensional volume of that flat parallelogram would be \( 0 \), and its area needs a different formula (@exr-orientation-and-volume-c1).

**Why this definition.** Reordering the vectors multiplies the determinant by a sign (@thm-alternating-properties), which the absolute value removes, so the volume does not depend on the order in which the edges are listed. The absolute value is also what makes volume non-negative. The sign we threw away is not garbage: it is the orientation, the subject of the second half of this section.

::: {.warning}
**Volume is not linear.** Scaling **one** edge by \( 2 \) doubles the volume, but scaling the whole parallelepiped by \( 2 \) multiplies it by \( 2^n \): \( \vol(2\a_1, \dots, 2\a_n) = \lvert \det(2\A) \rvert = 2^n \vol(\a_1, \dots, \a_n) \), where \( \A \) has columns \( \a_1, \dots, \a_n \). A cube of side \( 2 \) in \( \nR^3 \) has volume \( 8 \), not \( 2 \); this failure persists even with the sign kept, since \( \det \) is linear in each edge separately, not in all edges at once. The absolute value also destroys additivity in a single edge: \( \vol(\a_1 + \b_1, \a_2, \dots) \) is in general not \( \vol(\a_1, \a_2, \dots) + \vol(\b_1, \a_2, \dots) \): with \( \a_1 = \e_1 \), \( \b_1 = -\e_1 \) in \( \nR^2 \) and \( \a_2 = \e_2 \), the left side is \( 0 \) and the right side is \( 2 \).
:::

## Volume is forced by its rules

Why should anyone accept @def-parallelepiped-volume? Because of what any notion of volume of parallelepipeds must satisfy. The pictures in §1 showed three facts about area, and they have obvious \( n \)-dimensional versions: stretching one edge by a factor \( c \) multiplies the volume by \( \lvert c \rvert \); sliding one edge parallel to another (a shear) does not change the volume; and the unit cube has volume \( 1 \). The next theorem says that these three rules alone determine the volume completely. So any definition that obeys them, whether from school geometry or from measure theory, must agree with ours.

::: {#thm-volume-characterization}
[Volume Is Determined by Its Rules]

Let \( n \ge 1 \), and let \( g \) be a function assigning a real number \( g(\a_1, \dots, \a_n) \) to every list of \( n \) vectors in \( \nR^n \). Suppose that for every list, every \( i \ne j \) and every \( c \in \nR \):

::: {.enumerate options="label=(V\arabic*)"}
1. \( g(\a_1, \dots, c\a_i, \dots, \a_n) = \lvert c \rvert\, g(\a_1, \dots, \a_i, \dots, \a_n) \) (only slot \( i \) changes);
2. \( g(\a_1, \dots, \a_i + c\a_j, \dots, \a_n) = g(\a_1, \dots, \a_i, \dots, \a_n) \) (only slot \( i \) changes);
3. \( g(\e_1, \dots, \e_n) = 1 \).
:::

Then \( g(\a_1, \dots, \a_n) = \vol(\a_1, \dots, \a_n) \) for every list. Moreover, \( \vol \) itself satisfies (V1)–(V3).
:::

::: {.idea}
Think of \( g \) as a function of the matrix \( \M \) with columns \( \a_1, \dots, \a_n \). ① If the columns are dependent, shear one column to \( \0 \) and scale by \( 0 \): \( g = 0 \). ② Each elementary column operation changes \( g \) by the factor \( \lvert \det \E \rvert \). Scaling and shearing are (V1) and (V2); a swap is not among the rules, but three shears and a sign change perform it. ③ An invertible \( \M \) is a product of elementary matrices, so peel them off one at a time until only \( \I \) is left.
:::

::: {.proof}
For \( \M \in M_n(\nR) \) with columns \( \a_1, \dots, \a_n \), write \( h(\M) = g(\a_1, \dots, \a_n) \).

**Step 1: dependent columns give \( h(\M) = 0 \).** Suppose the columns are linearly dependent. By @thm-linear-dependence-lemma, some \( \a_i = c_1\a_1 + \dots + c_{i-1}\a_{i-1} \) (for \( i = 1 \), \( \a_1 = \0 \)). Applying (V2) to slot \( i \) with the scalars \( -c_1, \dots, -c_{i-1} \), one at a time, does not change \( g \), and it replaces \( \a_i \) by \( \0 \) while the other slots stay fixed. Then (V1) with \( c = 0 \) gives \( g(\dots, \0, \dots) = g(\dots, 0 \cdot \0, \dots) = 0 \cdot g(\dots, \0, \dots) = 0 \). Hence \( h(\M) = 0 \).

**Step 2: \( h(\M\E) = \lvert \det \E \rvert\, h(\M) \) for every elementary matrix \( \E \).** By @thm-row-op-is-left-multiplication and @thm-transpose-properties, \( \M\E = (\E\tp \M\tp)\tp \), and \( \E\tp \) is the elementary matrix \( \P_{ij} \), \( \D_i(c) \) or \( \I + c\E_{ji} \) when \( \E \) is \( \P_{ij} \), \( \D_i(c) \) or \( \I + c\E_{ij} \). So right multiplication by \( \E \) performs a column operation: swap columns \( i \) and \( j \); multiply column \( i \) by \( c \ne 0 \); or add \( c \) times column \( i \) to column \( j \). The determinants are \( \det \P_{ij} = -1 \), \( \det \D_i(c) = c \) and \( \det(\I + c\E_{ij}) = 1 \) by @thm-det-row-operations.

- For \( \E = \I + c\E_{ij} \), (V2) gives \( h(\M\E) = h(\M) = \lvert 1 \rvert\, h(\M) \).
- For \( \E = \D_i(c) \), (V1) gives \( h(\M\E) = \lvert c \rvert\, h(\M) \).
- For \( \E = \P_{ij} \), watch only slots \( i \) and \( j \), holding \( \x \) and \( \y \). By (V2) three times, \( (\x, \y) \to (\x + \y, \y) \to (\x + \y, -\x) \to (\y, -\x) \) leaves \( g \) unchanged, where the second step subtracts slot \( i \) from slot \( j \) and the third adds slot \( j \) to slot \( i \). By (V1) with \( c = -1 \) on slot \( j \), \( g \) at \( (\y, \x) \) equals \( \lvert -1 \rvert \) times \( g \) at \( (\y, -\x) \). Hence \( h(\M\P_{ij}) = h(\M) = \lvert -1 \rvert\, h(\M) \).

**Step 3: conclusion.** If the columns of \( \M \) are dependent, then \( h(\M) = 0 \) by Step 1 and \( \det \M = 0 \) by @thm-alternating-properties, so \( h(\M) = \lvert \det \M \rvert \). Otherwise \( \M \) is invertible by @thm-invertible-tfae, hence \( \M = \E_1\E_2\cdots \E_k \) is a product of elementary matrices by the same theorem. Applying Step 2 \( k \) times, starting from \( \I \), and then (V3),
\[
h(\M) = h(\I\E_1\cdots \E_k) = \lvert \det \E_1 \rvert \cdots \lvert \det \E_k \rvert\, h(\I) = \lvert \det(\E_1\cdots \E_k) \rvert = \lvert \det \M \rvert,
\]
where the third equality uses @thm-det-multiplicative and \( \lvert xy \rvert = \lvert x \rvert \lvert y \rvert \). This proves \( g = \vol \).

Finally, \( \vol \) satisfies (V1) because the determinant is linear in each column (@thm-leibniz-formula-alternating) and \( \lvert c\,d \rvert = \lvert c \rvert \lvert d \rvert \); (V2) by @thm-alternating-properties; and (V3) because \( \det \I_n = 1 \).
:::

**Agreement with area and volume from school.** For \( n = 2 \), let \( g(\a_1, \a_2) \) be the area of the parallelogram \( P(\a_1, \a_2) \) in the sense of school geometry, base times height. The pictures of §1 are exactly (V1)–(V3) for this \( g \): stretching a side by \( c \) stretches the base or the height by \( \lvert c \rvert \); a shear \( \a_1 \mapsto \a_1 + c\a_2 \) slides the opposite side along a line parallel to the base \( \a_2 \), keeping base and height; and the unit square has area \( 1 \). Hence, by @thm-volume-characterization, school area equals \( \lvert \det\begin{pmatrix} \a_1 & \a_2 \end{pmatrix} \rvert \). For \( n = 3 \) the same argument works with "area of base times height". What the theorem cannot supply is the geometric input itself: it takes the three rules as given.

**Agreement with Lebesgue measure.** In measure theory, every reasonable subset \( S \subseteq \nR^n \) has an \( n \)-dimensional volume, its Lebesgue measure. One can prove that the Lebesgue measure of \( P(\a_1, \dots, \a_n) \) satisfies (V1)–(V3), and hence equals \( \vol(\a_1, \dots, \a_n) \). We state this without proof; nothing in this book depends on it.

::: {.check}
Which of the rules (V1)–(V3) does the function \( g(\a_1, \a_2) = \lvert \det\begin{pmatrix} \a_1 & \a_2 \end{pmatrix} \rvert^2 \) on \( \nR^2 \) break?
:::

::: {.solution}
It satisfies (V2), since shears do not change the determinant, and (V3), since \( 1^2 = 1 \). It breaks (V1): \( g(2\e_1, \e_2) = 4 \), while \( \lvert 2 \rvert\, g(\e_1, \e_2) = 2 \). So the theorem does not apply, and indeed \( g \ne \vol \).
:::

## Linear maps scale volume

Applying a linear map to a parallelepiped gives another parallelepiped: by linearity, \( T\big(\sum t_i\a_i\big) = \sum t_iT\a_i \), so \( T(P(\a_1, \dots, \a_n)) = P(T\a_1, \dots, T\a_n) \). How does the volume change? Multiplicativity answers this in one line, and the answer does not depend on the parallelepiped.

::: {#thm-det-volume-scaling}
[Linear Maps Scale Volume by \( \lvert \det \rvert \)]

Let \( T \in \cL(\nR^n) \) and \( \a_1, \dots, \a_n \in \nR^n \). Then
\[
\vol(T\a_1, \dots, T\a_n) = \lvert \det T \rvert \cdot \vol(\a_1, \dots, \a_n).
\]
In particular, the image of the unit cube under \( T \) has volume \( \lvert \det T \rvert \).
:::

::: {.proof}
Let \( \B \) be the matrix of \( T \) in the standard basis, so \( T\x = \B\x \) for all \( \x \) (@thm-matrix-of-map-coordinates) and \( \det T = \det \B \) (@def-det-operator). Let \( \A = \begin{pmatrix} \a_1 & \cdots & \a_n \end{pmatrix} \). By @thm-three-views-of-product, \( \B\A = \begin{pmatrix} \B\a_1 & \cdots & \B\a_n \end{pmatrix} \). By @thm-det-multiplicative,
\[
\vol(T\a_1, \dots, T\a_n) = \lvert \det(\B\A) \rvert = \lvert \det \B \rvert\,\lvert \det \A \rvert = \lvert \det T \rvert\,\vol(\a_1, \dots, \a_n).
\]
For the unit cube take \( \a_i = \e_i \), with \( \vol(\e_1, \dots, \e_n) = 1 \).
:::

This is the meaning of the determinant of a real operator: **the factor by which it scales every volume**. An operator with \( \det T = 0 \) squashes \( \nR^n \) into a lower-dimensional subspace, where \( n \)-dimensional volume is \( 0 \). In multivariable calculus the same fact, applied to the linear approximation of a smooth map, becomes the Jacobian factor \( \lvert \det \J \rvert \) in the change-of-variables formula for integrals.

::: {#exm-volume-scaling}
[Area of an Image]

Let \( T \colon \nR^2 \to \nR^2 \) be \( T(x, y) = (3x + y,\ x + 2y) \). Find the area of the image of the unit square, and of the image of the parallelogram \( P((1, 1), (-1, 2)) \).
:::

::: {.solution}
The standard matrix is \( \B = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix} \), with \( \det T = 6 - 1 = 5 \). By @thm-det-volume-scaling the image of the unit square, the parallelogram spanned by \( (3, 1) \) and \( (1, 2) \), has area \( 5 \). The parallelogram \( P((1, 1), (-1, 2)) \) has area \( \lvert 2 + 1 \rvert = 3 \), so its image has area \( 5 \cdot 3 = 15 \). Check directly: \( T(1, 1) = (4, 3) \) and \( T(-1, 2) = (-1, 3) \), and \( \lvert \det\begin{pmatrix} 4 & -1 \\ 3 & 3 \end{pmatrix} \rvert = \lvert 12 + 3 \rvert = 15 \).
:::

## Orientation

Now the sign. In \( \nR^2 \), the ordered basis \( (\e_1, \e_2) \) turns **counterclockwise** from its first vector to its second, while \( (\e_2, \e_1) \) turns clockwise. No rotation carries one arrangement to the other: a rotation of the plane keeps counterclockwise turns counterclockwise. The determinant sees the difference: \( \det\begin{pmatrix} \e_1 & \e_2 \end{pmatrix} = 1 > 0 \) and \( \det\begin{pmatrix} \e_2 & \e_1 \end{pmatrix} = -1 < 0 \).

\begin{center}
\begin{tikzpicture}[scale=1.3, arr/.style={->, thick}]
  \draw[arr] (0,0) -- (1.4,0) node[below] {$\mathbf{e}_1$ (first)};
  \draw[arr] (0,0) -- (0,1.4) node[left] {$\mathbf{e}_2$ (second)};
  \draw[->, dashed] (0.7,0) arc (0:90:0.7);
  \node at (0.75,-0.55) {counterclockwise, $\det = 1$};
  \begin{scope}[xshift=4.2cm]
  \draw[arr] (0,0) -- (1.4,0) node[below] {$\mathbf{e}_1$ (second)};
  \draw[arr] (0,0) -- (0,1.4) node[left] {$\mathbf{e}_2$ (first)};
  \draw[->, dashed] (0,0.7) arc (90:0:0.7);
  \node at (0.75,-0.55) {clockwise, $\det = -1$};
  \end{scope}
\end{tikzpicture}
\end{center}

To compare two bases of an arbitrary real space, we compare them with each other rather than with a fixed standard basis, using the change-of-coordinates matrix of Chapter 3.

*Two bases have the same orientation when the matrix converting one into the other has positive determinant.*

::: {#def-orientation}
[Orientation]

Let \( V \) be a vector space **over \( \nR \)** with \( \dim V = n \ge 1 \), and let \( \sB \) and \( \sC \) be **ordered** bases of \( V \). We say \( \sB \) and \( \sC \) have the **same orientation** if
\[
\det \mtx{\id}{\sB}{\sC} > 0,
\]
and **opposite orientations** if \( \det\mtx{\id}{\sB}{\sC} < 0 \).
:::

In words: write each vector of \( \sB \) in coordinates with respect to \( \sC \), put the coordinate columns side by side (@def-change-of-coordinates-matrix), and look at the **sign** of the determinant. Exactly one of the two cases occurs, because \( \mtx{\id}{\sB}{\sC} \) is invertible (@thm-change-of-coordinates (c)), so its determinant is non-zero (@thm-det-nonzero-iff-invertible), and a non-zero real number is either positive or negative. The bases must be **ordered**: reordering a basis can change the answer.

For \( V = \nR^n \) there is a shortcut. If \( \B \) and \( \C \) are the matrices whose columns are the vectors of \( \sB \) and \( \sC \), then \( \mtx{\id}{\sB}{\sE} = \B \) and \( \mtx{\id}{\sC}{\sE} = \C \) for the standard basis \( \sE \). By @thm-change-of-coordinates (b) and (c), \( \mtx{\id}{\sB}{\sC} = \C^{-1}\B \). Since \( \det \C\,\det \C^{-1} = \det \I = 1 \) (@thm-det-multiplicative), \( \det\mtx{\id}{\sB}{\sC} = \det \B / \det \C \). So **\( \sB \) and \( \sC \) have the same orientation if and only if \( \det \B \) and \( \det \C \) have the same sign.**

**Examples.**

- In \( \nR^2 \), \( (\e_1, \e_2) \) and \( (\e_2, \e_1) \) have opposite orientations: \( \det \I_2 = 1 \) and \( \det\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = -1 \).
- In \( \nR^3 \), \( (\e_1, \e_2, \e_3) \) and \( (\e_2, \e_3, \e_1) \) have the **same** orientation. The second matrix is the permutation matrix of a \( 3 \)-cycle, whose sign is \( (-1)^{3-1} = 1 \). A cyclic shift of three vectors is two swaps.
- In \( V = \nR[x]_{\le 1} \), the bases \( \sB = (1, x) \) and \( \sC = (x, 1 + x) \) have \( 1 = -x + (1 + x) \) and \( x = x + 0 \cdot (1 + x) \), so \( \mtx{\id}{\sB}{\sC} = \begin{pmatrix} -1 & 1 \\ 1 & 0 \end{pmatrix} \), with determinant \( -1 \). They have opposite orientations. Orientation makes sense in any real space, with no picture at all.
- **Degenerate case, \( n = 1 \).** Bases of \( \nR \) are single non-zero numbers \( (a) \), and \( \mtx{\id}{(a)}{(b)} = (a/b) \). So \( (a) \) and \( (b) \) have the same orientation exactly when \( a \) and \( b \) have the same sign. The two orientations of a line are its two directions.

**Non-example by minimal change.** In \( \nR^2 \), \( (-\e_1, -\e_2) \) has the same orientation as \( (\e_1, \e_2) \): \( \det(-\I_2) = 1 \), and indeed it is the rotation of \( (\e_1, \e_2) \) by a half-turn. Change only **one** sign, to \( (\e_1, -\e_2) \): the determinant becomes \( -1 \), and the orientation flips. What changed is the sign of the determinant, which is the whole content of the definition. In \( \nR^3 \), by contrast, \( -\I_3 \) has determinant \( -1 \): negating all three vectors reverses orientation.

**Why this definition.** Using the change-of-coordinates matrix, rather than the matrices \( \B \) and \( \C \) above, makes the definition work in every real space, including spaces like \( \nR[x]_{\le 1} \) that have no standard picture. Requiring \( \det > 0 \) rather than \( \det = 1 \) is what gives a coarse, two-valued answer: rescaling a basis vector by a positive number should not change its handedness.

The payoff is that "same orientation" really sorts all bases into two families, as the pictures suggest.

::: {#thm-two-orientations}
[There Are Exactly Two Orientations]

Let \( V \) be a vector space over \( \nR \) with \( \dim V = n \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. "Having the same orientation" is an equivalence relation on the set of ordered bases of \( V \).
2. It has **exactly two** equivalence classes. If \( \sB = (\v_1, \dots, \v_n) \), then \( \sB^- = (-\v_1, \v_2, \dots, \v_n) \) lies in the class not containing \( \sB \).
:::
:::

::: {.idea}
The three axioms are three facts about change-of-coordinates matrices: \( \mtx{\id}{\sB}{\sB} = \I \); the matrix back is the inverse; and matrices compose along a chain \( \sB \to \sC \to \sD \). Determinants turn these into \( 1 > 0 \), \( 1/\text{positive} > 0 \) and \( \text{positive} \cdot \text{positive} > 0 \). For "exactly two", flipping one vector gives a second class, and "negative times negative is positive" shows there is no third.
:::

::: {.proof}
Write \( d(\sB, \sC) = \det\mtx{\id}{\sB}{\sC} \). By @thm-change-of-coordinates (b) and @thm-det-multiplicative, for bases \( \sB, \sC, \sD \),
\[
d(\sB, \sD) = d(\sC, \sD)\, d(\sB, \sC). \tag{$\ast$}
\]

(a) *Reflexive:* \( \mtx{\id}{\sB}{\sB} = \I_n \), so \( d(\sB, \sB) = 1 > 0 \). *Symmetric:* by \( (\ast) \) with \( \sD = \sB \), \( d(\sC, \sB)\,d(\sB, \sC) = d(\sB, \sB) = 1 \), so \( d(\sC, \sB) = 1/d(\sB, \sC) \), which is positive when \( d(\sB, \sC) \) is. *Transitive:* if \( d(\sB, \sC) > 0 \) and \( d(\sC, \sD) > 0 \), then \( d(\sB, \sD) > 0 \) by \( (\ast) \), since a product of positive reals is positive. By @def-equivalence-relation, this is an equivalence relation.

(b) *At least two classes.* \( \sB^- \) is a basis, and \( \mtx{\id}{\sB^-}{\sB} = \diag(-1, 1, \dots, 1) \), because \( -\v_1 = (-1)\v_1 \) and \( \v_j = 1 \cdot \v_j \). Its determinant is \( -1 \) by @thm-det-triangular. So \( d(\sB^-, \sB) < 0 \), and \( \sB^- \) and \( \sB \) lie in different classes.

*At most two classes.* Let \( \sC \) and \( \sD \) be bases, neither of which has the same orientation as \( \sB \). Then \( d(\sC, \sB) < 0 \) and \( d(\sD, \sB) < 0 \), and by symmetry \( d(\sB, \sD) < 0 \) as well. By \( (\ast) \), \( d(\sC, \sD) = d(\sB, \sD)\,d(\sC, \sB) \) is a product of two negative reals, hence positive. So all bases outside the class of \( \sB \) lie in one class, and there are exactly two classes.
:::

Choosing one of the two classes is called **orienting** \( V \); its bases are then called **positively oriented**, and the others **negatively oriented**. On \( \nR^n \) the standard choice is the class of \( (\e_1, \dots, \e_n) \). By the shortcut above, \( (\a_1, \dots, \a_n) \) is positively oriented if and only if \( \det\begin{pmatrix} \a_1 & \cdots & \a_n \end{pmatrix} > 0 \). So the determinant of a real square matrix carries two independent pieces of information: its absolute value is a volume, and its sign is an orientation.

::: {.warning}
**Orientation needs \( \nR \).** The proof used two facts about the reals: every non-zero number is positive or negative, and products and inverses of positive numbers are positive. Over \( \nC \) there is no such splitting. Suppose we tried "\( \sB \) and \( \sC \) have the same orientation if \( d(\sB, \sC) \) has positive real part". In \( \nC^1 \), with \( z = e^{i\pi/3} \), the bases \( (\e_1) \), \( (z\e_1) \), \( (z^2\e_1) \) give \( d((\e_1), (z\e_1)) = z^{-1} \) and \( d((z\e_1), (z^2\e_1)) = z^{-1} \), both with real part \( \frac12 > 0 \), but \( d((\e_1), (z^2\e_1)) = z^{-2} \) has real part \( -\frac12 \): transitivity fails. Over \( \nF_2 \), \( -1 = 1 \), so the second basis \( \sB^- \) of the proof is \( \sB \) itself. The theorem holds verbatim over any field with a compatible order, such as \( \nQ \), but not over \( \nC \) or a finite field.
:::

::: {.check}
Do \( ((1, 2), (3, 4)) \) and \( ((3, 4), (1, 2)) \) have the same orientation? Does \( ((1, 2), (3, 4)) \) have the standard orientation of \( \nR^2 \)?
:::

::: {.solution}
\( \det\begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix} = 4 - 6 = -2 \) and \( \det\begin{pmatrix} 3 & 1 \\ 4 & 2 \end{pmatrix} = 6 - 4 = 2 \). The signs differ, so the two bases have opposite orientations. The first has negative determinant, so it is negatively oriented: it is **not** in the class of \( (\e_1, \e_2) \).
:::

## The right-hand rule

In \( \nR^3 \), the standard orientation is the one described by the right hand: curl the fingers of the right hand from the first basis vector toward the second, and the thumb points along the third. For \( (\e_1, \e_2, \e_3) \) with the usual picture of the axes, this is the familiar arrangement below.

\begin{center}
\begin{tikzpicture}[scale=1.5, arr/.style={->, thick}]
  \draw[arr] (0,0) -- (1.6,0) node[right] {$\mathbf{e}_2$};
  \draw[arr] (0,0) -- (-0.9,-0.75) node[below left] {$\mathbf{e}_1$};
  \draw[arr] (0,0) -- (0,1.6) node[above] {$\mathbf{e}_3 = \mathbf{e}_1 \times \mathbf{e}_2$};
  \draw[->, dashed] (-0.55,-0.46) .. controls (-0.2,-0.75) and (0.5,-0.45) .. (0.7,-0.05);
  \node[font=\small, align=left] at (1.9,-0.7) {fingers curl from $\mathbf{e}_1$ to $\mathbf{e}_2$};
  \node[font=\small, align=left] at (1.25,1.1) {thumb along $\mathbf{e}_3$};
\end{tikzpicture}
\end{center}

The **cross product** of \( \a = (a_1, a_2, a_3) \) and \( \b = (b_1, b_2, b_3) \) in \( \nR^3 \) is
\[
\a \times \b \coloneqq (a_2b_3 - a_3b_2,\ a_3b_1 - a_1b_3,\ a_1b_2 - a_2b_1).
\]
Physics defines it by the right-hand rule. Here is the linear-algebra reason the two descriptions match: \( (\a, \b, \a \times \b) \) is always positively oriented.

Expand \( \det\begin{pmatrix} \a & \b & \a \times \b \end{pmatrix} \) along its third column (@thm-laplace-expansion). The cofactors of that column are \( C_{13} = a_2b_3 - a_3b_2 \), \( C_{23} = -(a_1b_3 - a_3b_1) \) and \( C_{33} = a_1b_2 - a_2b_1 \), which are exactly the three components of \( \a \times \b \). Hence
\[
\det\begin{pmatrix} \a & \b & \a \times \b \end{pmatrix} = (a_2b_3 - a_3b_2)^2 + (a_3b_1 - a_1b_3)^2 + (a_1b_2 - a_2b_1)^2 \ \ge\ 0 .
\]
If \( \a \) and \( \b \) are linearly independent, the \( 3 \times 2 \) matrix \( \begin{pmatrix} \a & \b \end{pmatrix} \) has rank \( 2 \), so one of its \( 2 \times 2 \) minors, which are \( \pm \) the components of \( \a \times \b \), is non-zero (@thm-rank-via-minors). Then the determinant is strictly positive, so \( (\a, \b, \a \times \b) \) is a basis (@thm-det-nonzero-iff-invertible) with the standard orientation. For example, \( \e_1 \times \e_2 = (0, 0, 1) = \e_3 \), matching the picture.

## Orientation-preserving maps

An invertible operator carries each basis to a basis. Does it keep the orientation? The answer is the same for every basis and depends only on the sign of \( \det T \).

::: {#prp-orientation-preserving}
[Determinant Sign and Orientation]

Let \( V \) be a vector space over \( \nR \) with \( \dim V = n \ge 1 \), let \( T \in \cL(V) \) be invertible, and let \( \sB = (\v_1, \dots, \v_n) \) be any basis of \( V \). Then \( T\sB = (T\v_1, \dots, T\v_n) \) is a basis of \( V \), and
\[
\mtx{\id}{T\sB}{\sB} = \mtx{T}{\sB}{\sB}.
\]
Hence \( \sB \) and \( T\sB \) have the same orientation if and only if \( \det T > 0 \), and this does not depend on \( \sB \).
:::

::: {.proof}
Since \( T \) is invertible, it is an isomorphism, so \( T\sB \) is a basis by @thm-isomorphism-preserves-bases. By @def-change-of-coordinates-matrix, column \( j \) of \( \mtx{\id}{T\sB}{\sB} \) is \( \coord{T\v_j}{\sB} \), which is column \( j \) of \( \mtx{T}{\sB}{\sB} \) by @def-matrix-of-linear-map. Hence the two matrices are equal, and by @def-det-operator, \( \det\mtx{\id}{T\sB}{\sB} = \det T \). By @def-orientation and the symmetry in @thm-two-orientations (a), \( \sB \) and \( T\sB \) have the same orientation exactly when \( \det T > 0 \).
:::

An invertible operator with \( \det T > 0 \) is **orientation-preserving**, and one with \( \det T < 0 \) is **orientation-reversing**. Rotations of the plane preserve orientation and reflections reverse it (@exr-orientation-and-volume-c2). In \( \nR^3 \), the map \( \x \mapsto -\x \) reverses orientation, since \( \det(-\I_3) = -1 \): a right hand, pushed through the origin, becomes a left hand.

## Exercises

### A. Check your understanding

:::: {#exr-orientation-and-volume-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the definition of the volume of the parallelepiped spanned by \( \a_1, \dots, \a_n \in \nR^n \), and say what it is when the vectors are dependent.
2. True or false: \( \vol(\a_1 + \b, \a_2, \dots, \a_n) = \vol(\a_1, \dots, \a_n) + \vol(\b, \a_2, \dots, \a_n) \). Justify your answer.
3. Which three rules characterize volume in @thm-volume-characterization?
4. True or false: if \( \det T = -2 \), then \( T \) doubles every volume. Justify your answer.
5. Define "same orientation" for two ordered bases of a real vector space.
6. True or false: for every \( n \ge 1 \), the map \( \x \mapsto -\x \) on \( \nR^n \) reverses orientation. Justify your answer.
:::
::::

::: {.solution}
(a) \( \vol(\a_1, \dots, \a_n) = \lvert \det\begin{pmatrix} \a_1 & \cdots & \a_n \end{pmatrix} \rvert \) (@def-parallelepiped-volume). For dependent vectors it is \( 0 \), by @thm-alternating-properties.

(b) False. With \( n = 2 \), \( \a_1 = \e_1 \), \( \b = -\e_1 \), \( \a_2 = \e_2 \): the left side is \( \vol(\0, \e_2) = 0 \), the right side is \( 1 + 1 = 2 \). The absolute value destroys additivity.

(c) (V1) scaling one vector by \( c \) scales the volume by \( \lvert c \rvert \); (V2) adding a multiple of one vector to another does not change it; (V3) the unit cube has volume \( 1 \).

(d) True. By @thm-det-volume-scaling, \( \vol(T\a_1, \dots, T\a_n) = \lvert -2 \rvert \vol(\a_1, \dots, \a_n) \). The sign only affects orientation.

(e) \( \sB \) and \( \sC \) have the same orientation if \( \det\mtx{\id}{\sB}{\sC} > 0 \) (@def-orientation).

(f) False. \( \det(-\I_n) = (-1)^n \), so by @prp-orientation-preserving the map reverses orientation for odd \( n \) and preserves it for even \( n \). In \( \nR^2 \) it is the rotation by a half-turn.
:::

### B. Practice

:::: {#exr-orientation-and-volume-b1}
[B1: Volume of a parallelepiped]

Find the volume of the parallelepiped in \( \nR^3 \) spanned by \( (2, 1, 0) \), \( (1, 3, 1) \) and \( (0, 1, 1) \). Hence find the volume of its image under the map \( T(x, y, z) = (x + y,\ y + z,\ 2z) \).
::::

::: {.solution}
Expanding along the first row,
\[
\det\begin{pmatrix} 2 & 1 & 0 \\ 1 & 3 & 1 \\ 0 & 1 & 1 \end{pmatrix} = 2(3 - 1) - 1\cdot(1 - 0) + 0 = 3,
\]
so the volume is \( 3 \). The standard matrix of \( T \) is \( \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{pmatrix} \), upper triangular with determinant \( 2 \) (@thm-det-triangular). By @thm-det-volume-scaling the image has volume \( 2 \cdot 3 = 6 \).
:::

:::: {#exr-orientation-and-volume-b2}
[B2: Comparing orientations]

In \( \nR^3 \), let \( \sB = ((1, 1, 0), (0, 1, 1), (1, 0, 1)) \), \( \sC = ((0, 1, 0), (1, 0, 0), (1, 1, 1)) \) and \( \sD = ((1, 0, 1), (1, 1, 0), (0, 1, 1)) \). Determine which pairs have the same orientation, and which are positively oriented. Justify your answer.
::::

::: {.solution}
By the shortcut after @def-orientation, compare signs of the determinants of the matrices with these columns. Expanding along the first row:
\[
\det\begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix} = 1\cdot(1 - 0) - 0 + 1\cdot(1 - 0) = 2, \qquad
\det\begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 0 & 0 & 1 \end{pmatrix} = -1,
\]
the second by expanding along the last row: \( 1 \cdot \det\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = -1 \). The list \( \sD \) is \( \sB \) shifted cyclically, \( (\b_3, \b_1, \b_2) \); moving the last column to the front takes two column swaps, so by @thm-alternating-properties its determinant is \( (-1)^2 \cdot 2 = 2 \). Hence \( \sB \) and \( \sD \) are positively oriented and have the same orientation; \( \sC \) is negatively oriented, opposite to both.
:::

:::: {#exr-orientation-and-volume-b3}
[B3: Areas of images]

Let \( T(x, y) = (2x + y,\ -x + 3y) \) on \( \nR^2 \).

::: {.enumerate options="label=(\alph*)"}
1. Find the area of the image of the unit square under \( T \).
2. Find the area of the image of the parallelogram \( P((1, 0), (1, 2)) \), first by @thm-det-volume-scaling and then directly.
3. Is \( T \) orientation-preserving?
:::
::::

::: {.solution}
(a) The standard matrix \( \begin{pmatrix} 2 & 1 \\ -1 & 3 \end{pmatrix} \) has determinant \( 6 + 1 = 7 \), so the image of the unit square has area \( 7 \).

(b) \( \vol((1, 0), (1, 2)) = \lvert \det\begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix} \rvert = 2 \), so the image has area \( 7 \cdot 2 = 14 \). Directly, \( T(1, 0) = (2, -1) \) and \( T(1, 2) = (4, 5) \), and \( \lvert \det\begin{pmatrix} 2 & 4 \\ -1 & 5 \end{pmatrix} \rvert = \lvert 10 + 4 \rvert = 14 \).

(c) Yes: \( \det T = 7 > 0 \), so by @prp-orientation-preserving \( T \) preserves orientation.
:::

### C. Going deeper

:::: {#exr-orientation-and-volume-c1}
[C1: Area of a triangle in space]

For \( \u, \v \in \nR^3 \), let \( \A = \begin{pmatrix} \u & \v \end{pmatrix} \in M_{3 \times 2}(\nR) \). We **define** the area of the parallelogram \( P(\u, \v) \subseteq \nR^3 \) to be \( \sqrt{\det(\A\tp \A)} \); Chapter 12 justifies this with inner products, where \( \det(\A\tp\A) \) is recognized as a Gram determinant.

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \det(\A\tp \A) \ge 0 \), so the square root exists, and that \( \det(\A\tp \A) = (u_2v_3 - u_3v_2)^2 + (u_3v_1 - u_1v_3)^2 + (u_1v_2 - u_2v_1)^2 \).
2. Show that if \( \u \) and \( \v \) lie in the plane \( z = 0 \), this area equals the area \( \vol((u_1, u_2), (v_1, v_2)) \) of @def-parallelepiped-volume in \( \nR^2 \).
3. Find the area of the triangle with vertices \( (1, 0, 0) \), \( (0, 2, 0) \), \( (0, 0, 3) \).
:::

*Hint: apply @cor-gram-determinant-nonnegative to \( \A\tp \).*
::::

::: {.solution}
(a) \( \A\tp \in M_{2 \times 3}(\nR) \) and \( (\A\tp)\tp = \A \), so by @cor-gram-determinant-nonnegative applied to \( \A\tp \), \( \det(\A\tp \A) = \sum_{|S| = 2} (\det (\A\tp)_{[2],S})^2 \ge 0 \). The \( 2 \times 2 \) minors of \( \A\tp = \begin{pmatrix} u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{pmatrix} \) are \( u_1v_2 - u_2v_1 \), \( u_1v_3 - u_3v_1 \), \( u_2v_3 - u_3v_2 \) for \( S = \{1,2\}, \{1,3\}, \{2,3\} \); squaring removes the signs, giving the stated sum.

(b) If \( u_3 = v_3 = 0 \), two of the three squares vanish, and \( \det(\A\tp \A) = (u_1v_2 - u_2v_1)^2 \). Hence \( \sqrt{\det(\A\tp \A)} = \lvert u_1v_2 - u_2v_1 \rvert = \lvert \det\begin{pmatrix} u_1 & v_1 \\ u_2 & v_2 \end{pmatrix} \rvert \), which is \( \vol((u_1, u_2), (v_1, v_2)) \).

(c) The triangle is half of the parallelogram spanned by \( \u = (0, 2, 0) - (1, 0, 0) = (-1, 2, 0) \) and \( \v = (0, 0, 3) - (1, 0, 0) = (-1, 0, 3) \). By (a), \( \det(\A\tp \A) = (6 - 0)^2 + (0 + 3)^2 + (0 + 2)^2 = 36 + 9 + 4 = 49 \). As a check, \( \A\tp \A = \begin{pmatrix} 5 & 1 \\ 1 & 10 \end{pmatrix} \) has determinant \( 50 - 1 = 49 \). So the parallelogram has area \( 7 \), and the triangle has area \( \frac72 \).
:::

:::: {#exr-orientation-and-volume-c2}
[C2: Rotations and reflections]

For \( \theta \in \nR \), let \( \R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} \) (rotation by \( \theta \)) and \( \S_\theta = \begin{pmatrix} \cos 2\theta & \sin 2\theta \\ \sin 2\theta & -\cos 2\theta \end{pmatrix} \) (reflection in the line through \( 0 \) at angle \( \theta \)).

::: {.enumerate options="label=(\alph*)"}
1. Show that every rotation preserves orientation and area, and every reflection reverses orientation and preserves area.
2. Show that \( \S_\theta \S_\varphi \) is orientation-preserving for all \( \theta, \varphi \). (It is in fact a rotation, but you need not show this.)
3. Prove that no \( \M \in M_2(\nR) \) satisfies \( \M^2 = \S_0 = \diag(1, -1) \). Does the same argument rule out \( \M^2 = -\I_2 \)?
:::
::::

::: {.solution}
(a) \( \det \R_\theta = \cos^2\theta + \sin^2\theta = 1 > 0 \) and \( \det \S_\theta = -\cos^2 2\theta - \sin^2 2\theta = -1 < 0 \). By @prp-orientation-preserving, rotations preserve and reflections reverse orientation. Both have \( \lvert \det \rvert = 1 \), so both preserve area by @thm-det-volume-scaling.

(b) By @thm-det-multiplicative, \( \det(\S_\theta \S_\varphi) = (-1)(-1) = 1 > 0 \).

(c) If \( \M^2 = \S_0 \), then \( (\det \M)^2 = \det \S_0 = -1 \) by @thm-det-multiplicative, impossible for a real number \( \det \M \). The argument says nothing about \( -\I_2 \), since \( \det(-\I_2) = 1 \); and indeed \( \R_{\pi/2}^2 = \R_{\pi/2}\R_{\pi/2} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}^2 = -\I_2 \). An orientation-reversing map can never be the square of a real map, since the square of anything preserves orientation.
:::
