# Signed Area and Volume

In Chapter 0 a single number, \( ad - bc \), decided whether a \( 2 \times 2 \) matrix is invertible (@thm-two-by-two-inverse). For an \( n \times n \) matrix, Chapter 2 answered the same question by row reduction, which is a procedure, not a number. Is there one number for every square matrix that does the job of \( ad - bc \)? This section does not define it yet. Instead it asks what such a number should **mean**, finds the answer in area and volume, and extracts a short list of rules. From the rules alone, \( ad - bc \) comes out, with no other choice possible.

## Area as a function of two vectors

Take two vectors \( \u, \v \in \nR^2 \) and the parallelogram they span,
\[
  P(\u, \v) = \{ s\u + t\v : 0 \le s \le 1,\ 0 \le t \le 1 \}.
\]
Its corners are \( \0 \), \( \u \), \( \v \) and \( \u + \v \). We want to understand its area as a **function of the two vectors**, without drawing a coordinate grid and counting squares. Four features are visible without any formula.

**Scaling a side scales the area.** Replacing \( \v \) by \( 2\v \) stacks two copies of \( P(\u, \v) \) on top of each other, so the area doubles. Replacing \( \v \) by \( 3\v \) triples it, and replacing \( \v \) by \( \frac12\v \) halves it.

**Shearing does not change the area.** Replace \( \v \) by \( \v + c\u \). The top edge slides along its own line, parallel to the base \( \u \). The base stays the same, and so does the height, so the area stays the same. The picture shows \( c = 1 \): the triangle cut off on the left of \( P(\u, \v) \) reappears, moved by \( \u \), on the right of \( P(\u, \v + \u) \).

\begin{center}
\begin{tikzpicture}[scale=0.9]
  \fill[gray!25] (0,0) -- (1,2) -- (4,2) -- cycle;
  \fill[gray!25] (3,0) -- (7,2) -- (4,2) -- cycle;
  \draw[thick] (0,0) -- (3,0) -- (4,2) -- (1,2) -- cycle;
  \draw[thick, dashed] (3,0) -- (7,2) -- (4,2);
  \draw[very thick, ->] (0,0) -- (3,0) node[below] {$\mathbf{u}$};
  \draw[very thick, ->] (0,0) -- (1,2) node[above left] {$\mathbf{v}$};
  \draw[very thick, ->] (0,0) -- (4,2) node[above] {$\mathbf{v}+\mathbf{u}$};
  \node at (1.6,1.45) {$T$};
  \node at (4.6,1.45) {$T + \mathbf{u}$};
  \draw[<->] (-0.5,0) -- (-0.5,2) node[midway, left] {height};
\end{tikzpicture}
\end{center}

The solid outline is \( P(\u, \v) \) and the dashed one completes \( P(\u, \v + \u) \). Both consist of the unshaded middle triangle plus a shaded triangle, and the two shaded triangles \( T \) and \( T + \u \) are translates of each other.

**Equal sides give area zero.** \( P(\u, \u) \) is a segment, which has no area. More generally, if \( \v \) is a multiple of \( \u \), the parallelogram is flat.

**The unit square has area one.** \( P(\e_1, \e_2) \) is the unit square. This fixes the unit of measurement.

## Why the area needs a sign

The first feature is not quite right as stated. Replacing \( \v \) by \( -\v \) moves the parallelogram to the other side of the line of \( \u \) (the point reflection \( \x \mapsto \u - \x \) carries \( P(\u, \v) \) onto \( P(\u, -\v) \)) and does **not** change its area, so ordinary area satisfies \( \operatorname{area}(\u, c\v) = \lvert c \rvert \operatorname{area}(\u, \v) \), with an absolute value. That absolute value spoils a second, very useful property.

Fix the base \( \u \) and let the second vector vary. The area is base times height, and heights along a fixed direction add up: if \( \v \) reaches height \( 1 \) above the line of \( \u \) and \( \w \) reaches height \( 1.5 \), then \( \v + \w \) reaches height \( 2.5 \). So we expect
\[
  \operatorname{area}(\u, \v + \w) = \operatorname{area}(\u, \v) + \operatorname{area}(\u, \w).
\]
The picture shows it: \( P(\u, \w) \), moved up by \( \v \), sits exactly on top of \( P(\u, \v) \), and the two together have the same base and total height as \( P(\u, \v + \w) \) (dashed).

\begin{center}
\begin{tikzpicture}[scale=1.0]
  \fill[gray!15] (0,0) -- (3,0) -- (4,1) -- (1,1) -- cycle;
  \fill[gray!35] (1,1) -- (4,1) -- (3.5,2.5) -- (0.5,2.5) -- cycle;
  \draw[thick] (0,0) -- (3,0) -- (4,1) -- (1,1) -- cycle;
  \draw[thick] (1,1) -- (4,1) -- (3.5,2.5) -- (0.5,2.5) -- cycle;
  \draw[thick, dashed] (0,0) -- (0.5,2.5) -- (3.5,2.5) -- (3,0);
  \draw[very thick, ->] (0,0) -- (3,0) node[below] {$\mathbf{u}$};
  \draw[very thick, ->] (0,0) -- (1,1) node[below right] {$\mathbf{v}$};
  \draw[very thick, ->] (1,1) -- (0.5,2.5) node[midway, right] {$\mathbf{w}$};
  \node at (2.0,0.45) {$P(\mathbf{u},\mathbf{v})$};
  \node at (2.3,1.75) {$\mathbf{v} + P(\mathbf{u},\mathbf{w})$};
  \draw[<->] (5,0) -- (5,1) node[midway, right] {$1$};
  \draw[<->] (5,1) -- (5,2.5) node[midway, right] {$1.5$};
\end{tikzpicture}
\end{center}

Now take \( \w = -\v \). Then \( \v + \w = \0 \) and the left side is \( \operatorname{area}(\u, \0) = 0 \), while the right side is \( 2 \operatorname{area}(\u, \v) \), which is positive. Additivity fails, because \( -\v \) points **below** the line of \( \u \) and its height should count as negative. The repair is to give area a sign.

*Signed area is ordinary area, counted positive when the second vector lies on the counterclockwise side of the first, and negative when it lies on the clockwise side.*

So \( P(\e_1, \e_2) \) has signed area \( +1 \), because \( \e_2 \) is a quarter turn counterclockwise from \( \e_1 \), and \( P(\e_2, \e_1) \) has signed area \( -1 \). With the sign in place, scaling holds with \( c \) instead of \( \lvert c \rvert \), and heights add with their signs, so additivity holds for all \( \v, \w \).

Write \( D(\u, \v) \) for the signed area. The pictures suggest that \( D \colon \nR^2 \times \nR^2 \to \nR \) obeys the following rules, **for all** \( \u, \v, \w \in \nR^2 \) and **all** \( c \in \nR \):

::: {.enumerate options="label=(R\arabic*)"}
1. **(Scaling)** \( D(c\u, \v) = cD(\u, \v) \) and \( D(\u, c\v) = cD(\u, \v) \).
2. **(Shear)** \( D(\u + c\v, \v) = D(\u, \v) \) and \( D(\u, \v + c\u) = D(\u, \v) \).
3. **(Equal sides)** \( D(\u, \u) = 0 \).
4. **(Normalization)** \( D(\e_1, \e_2) = 1 \).
5. **(Additivity)** \( D(\u + \w, \v) = D(\u, \v) + D(\w, \v) \) and \( D(\u, \v + \w) = D(\u, \v) + D(\u, \w) \).
:::

These are rules read off from pictures, not yet a definition. The question is what they force.

## The rules force \( ad - bc \)

A \( 2 \times 2 \) matrix \( \A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \) has columns \( \u = (a, c) \) and \( \v = (b, d) \), and \( P(\u, \v) \) is the image of the unit square under \( \x \mapsto \A\x \). We now show that the first four rules leave no freedom at all. The method is the column version of elimination: use shears to clear entries until the parallelogram becomes a rectangle.

::: {#exm-two-by-two-from-rules}
[\( ad - bc \) from the Rules]

Let \( D \colon \nR^2 \times \nR^2 \to \nR \) be **any** function satisfying (R1)–(R4). Show that \( D((a, c), (b, d)) = ad - bc \) for all \( a, b, c, d \in \nR \).
:::

::: {.solution}
Write \( \u = (a, c) \) and \( \v = (b, d) \). Two consequences of (R1) come first. Taking the scalar \( 0 \) in (R1) gives \( D(\u, \0) = D(\u, 0\v) = 0 \cdot D(\u, \v) = 0 \), and likewise \( D(\0, \v) = 0 \). Using (R1) twice and then (R4),
\[
  \begin{aligned}
  D((p, 0), (0, q)) &= D(p\e_1, q\e_2) = pq\,D(\e_1, \e_2) \\
  &= pq \qquad \text{for all } p, q \in \nR.
  \end{aligned} \tag{$\ast$}
\]

*Case 1: \( a \neq 0 \).* By the second shear rule with scalar \( -b/a \),
\[
  D(\u, \v) = D\bigl(\u, \v - \tfrac{b}{a}\u\bigr) = D\bigl(\u, (0, d')\bigr), \qquad \text{where } d' = d - \tfrac{bc}{a}.
\]
If \( d' = 0 \), this is \( D(\u, \0) = 0 = ad' \). If \( d' \neq 0 \), the first shear rule with scalar \( -c/d' \) clears the second entry of \( \u \):
\[
  D\bigl(\u, (0, d')\bigr) = D\bigl(\u - \tfrac{c}{d'}(0, d'), (0, d')\bigr) = D\bigl((a, 0), (0, d')\bigr) = ad'
\]
by \( (\ast) \). In both sub-cases \( D(\u, \v) = ad' = ad - bc \).

*Case 2: \( a = 0 \) and \( b \neq 0 \).* By the first shear rule with scalar \( 1 \), \( D(\u, \v) = D(\u + \v, \v) \), and \( \u + \v = (b, c + d) \) has first entry \( b \neq 0 \). Case 1, applied to the columns \( (b, c + d) \) and \( (b, d) \), gives
\[
  D(\u, \v) = bd - b(c + d) = -bc = ad - bc,
\]
since \( a = 0 \).

*Case 3: \( a = b = 0 \).* If \( c = 0 \), then \( \u = \0 \) and \( D(\u, \v) = 0 \). If \( c \neq 0 \), the second shear rule with scalar \( -d/c \) gives \( D(\u, \v) = D(\u, \v - \tfrac{d}{c}\u) = D(\u, \0) = 0 \). In both sub-cases \( D(\u, \v) = 0 = ad - bc \).

The three cases cover all \( a, b, c, d \), so \( D((a, c), (b, d)) = ad - bc \), as claimed.
:::

So **at most one** function obeys (R1)–(R4). Conversely, \( (a, c), (b, d) \mapsto ad - bc \) obeys all five rules; for instance, for the second shear rule, replacing \( (b, d) \) by \( (b + ta, d + tc) \) gives \( a(d + tc) - (b + ta)c = ad - bc \). The other checks are just as short. Hence **exactly one** function satisfies (R1)–(R4), and it satisfies (R5) as well.

Two things in this computation are worth noticing. First, (R3) was never used. It follows from the others: \( D(\u, \u) = D(\u, \u - \u) = D(\u, \0) = 0 \), by a shear and then scaling by \( 0 \). Second, the argument used only addition, subtraction, multiplication and division by non-zero numbers. So over **any** field \( F \), exactly one function \( F^2 \times F^2 \to F \) satisfies (R1)–(R4), namely \( ad - bc \). The picture needs \( \nR \); the algebra does not.

There is also a shorter route, if we allow additivity. Expanding \( \u = a\e_1 + c\e_2 \) and \( \v = b\e_1 + d\e_2 \) with (R5) and (R1) gives four terms:
\[
  D(\u, \v) = ab\,D(\e_1, \e_1) + ad\,D(\e_1, \e_2) + cb\,D(\e_2, \e_1) + cd\,D(\e_2, \e_2).
\]
The first and last vanish by (R3), \( D(\e_1, \e_2) = 1 \) by (R4), and \( D(\e_2, \e_1) = -1 \) (see the Quick check below). This expansion is the route that generalizes to \( n \) vectors later in the chapter, while the elimination route of @exm-two-by-two-from-rules becomes the practical way to compute.

::: {.check}
Using only (R1) and (R2), show that \( D(\u, \v) = -D(\v, \u) \) for all \( \u, \v \). Deduce \( D(\e_2, \e_1) \).
:::

::: {.solution}
Apply shears and one scaling:
\[
  \begin{aligned}
  D(\u, \v) &\overset{\text{(R2)}}{=} D(\u + \v, \v) \\
  &\overset{\text{(R2)}}{=} D\bigl(\u + \v, \v - (\u + \v)\bigr) = D(\u + \v, -\u) \\
  &\overset{\text{(R2)}}{=} D\bigl((\u + \v) + (-\u), -\u\bigr) = D(\v, -\u) \\
  &\overset{\text{(R1)}}{=} -D(\v, \u).
  \end{aligned}
\]
With \( \u = \e_1 \), \( \v = \e_2 \) and (R4), \( D(\e_2, \e_1) = -D(\e_1, \e_2) = -1 \). This agrees with \( ad - bc = 0 \cdot 0 - 1 \cdot 1 \) for the columns \( (0, 1), (1, 0) \).
:::

Now compare with Chapter 0. By @thm-two-by-two-inverse, \( \A \) is invertible **if and only if** \( ad - bc \neq 0 \). In the language of this section: \( \A \) is invertible exactly when the parallelogram spanned by its columns is **not flat**, that is, when the columns do not lie on a common line through the origin. The number that decides invertibility and the signed area of the image of the unit square are the same number. Drag the images of \( \e_1 \) and \( \e_2 \) below and watch the signed area pass through \( 0 \) exactly when the two columns line up.

::: {.widget src="widgets/linear-map.js" matrix="2,1,1,3" readout="area"}
::: {.print}
\begin{center}
\begin{tikzpicture}[scale=0.9]
    \draw[->] (-0.5,0) -- (3.8,0) node[right] {$x$};
    \draw[->] (0,-0.5) -- (0,4.4) node[above] {$y$};
    \draw[dashed] (0,0) rectangle (1,1);
    \fill[gray!25] (0,0) -- (2,1) -- (3,4) -- (1,3) -- cycle;
    \draw (0,0) -- (2,1) -- (3,4) -- (1,3) -- cycle;
    \draw[very thick, ->] (0,0) -- (2,1) node[right] {$\A\mathbf{e}_1 = (2,1)$};
    \draw[very thick, ->] (0,0) -- (1,3) node[left] {$\A\mathbf{e}_2 = (1,3)$};
\end{tikzpicture}
\end{center}

The unit square (dashed) and its image under \( \A = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} \), a parallelogram of signed area \( 2 \cdot 3 - 1 \cdot 1 = 5 \). The second column lies counterclockwise from the first, so the sign is positive.
:::
:::

## Volume in three dimensions

The same story plays out one dimension up. Three vectors \( \u, \v, \w \in \nR^3 \) span a **parallelepiped**
\[
  P(\u, \v, \w) = \{ r\u + s\v + t\w : 0 \le r, s, t \le 1 \},
\]
a slanted box whose faces are parallelograms.

\begin{center}
\begin{tikzpicture}[x={(1cm,0cm)}, y={(0.55cm,0.4cm)}, z={(0cm,1cm)}, scale=1.1]
  \coordinate (O) at (0,0,0);
  \coordinate (U) at (3,0,0);
  \coordinate (V) at (0.6,2.4,0);
  \coordinate (W) at (0.8,0.3,2);
  \coordinate (UV) at (3.6,2.4,0);
  \coordinate (UW) at (3.8,0.3,2);
  \coordinate (VW) at (1.4,2.7,2);
  \coordinate (UVW) at (4.4,2.7,2);
  \fill[gray!20] (O) -- (U) -- (UV) -- (V) -- cycle;
  \draw[dashed] (O) -- (V) -- (UV);
  \draw[dashed] (V) -- (VW);
  \draw (U) -- (UV);
  \draw (W) -- (UW) -- (UVW) -- (VW) -- cycle;
  \draw (U) -- (UW);
  \draw (UV) -- (UVW);
  \draw[very thick, ->] (O) -- (U) node[below] {$\mathbf{u}$};
  \draw[very thick, ->, dashed] (O) -- (V) node[above left] {$\mathbf{v}$};
  \draw[very thick, ->] (O) -- (W) node[above left] {$\mathbf{w}$};
  \draw[<->] (-0.7,0,0) -- (-0.7,0,2) node[midway, left] {height};
\end{tikzpicture}
\end{center}

Its volume is the area of the base \( P(\u, \v) \) (shaded) times the height of \( \w \) above the plane of the base. Each feature from the plane has a counterpart:

- scaling one edge scales the volume;
- replacing \( \w \) by \( \w + a\u + b\v \) slides the top face within its own plane, so the base and height, hence the volume, are unchanged, and similarly for shears of \( \u \) or \( \v \);
- if two edges are equal, the box is flat and the volume is \( 0 \);
- the unit cube \( P(\e_1, \e_2, \e_3) \) has volume \( 1 \);
- with a sign attached, heights add, so the signed volume is additive in each edge.

The sign in three dimensions records whether \( (\u, \v, \w) \) is arranged like \( (\e_1, \e_2, \e_3) \), the right-hand rule. We make this precise as orientation later in the chapter. For now the point is that the rules are **the same rules**, now for a function \( D(\u, \v, \w) \) of three vectors. The Quick check above also carries over word for word: shearing and scaling two of the arguments while the third stays fixed shows that swapping two arguments changes the sign.

## What we will prove

Here is the goal for the next three sections. Let \( F \) be a field and \( n \ge 1 \).

> There is **exactly one** function \( D \) of \( n \) vectors in \( F^n \) that is linear in each argument separately, is \( 0 \) whenever two arguments are equal, and takes the value \( 1 \) at \( (\e_1, \dots, \e_n) \).

Its value on the columns of a matrix \( \A \) will be the determinant \( \det \A \). The plan follows the shorter route for \( n = 2 \). Expanding every argument in the standard basis gives \( n^n \) terms. The rule for equal arguments kills every term with a repeated basis vector, which leaves one term for each rearrangement \( (\e_{\sigma(1)}, \dots, \e_{\sigma(n)}) \) of the standard basis. Each surviving value is \( \pm 1 \), reached from \( D(\e_1, \dots, \e_n) = 1 \) by swaps, with one sign change per swap. That creates two tasks:

1. Name and study functions of several vectors with these rules. This is the next section, on multilinear alternating forms.
2. Make sure the sign of a rearrangement is well defined, even though it can be reached by different sequences of swaps. This is the section on permutations and sign.

The existence and uniqueness theorem itself comes after both.

::: {.warning}
**Sarrus's rule is a \( 3 \times 3 \) coincidence.** For a \( 3 \times 3 \) matrix, the "diagonals" shortcut (add the three products along the down-right diagonals of the array with its first two columns copied to the right, subtract the three along the up-right diagonals) gives the correct six terms, because there are exactly \( 3! = 6 \) rearrangements. The same picture for \( 4 \times 4 \) gives \( 4 + 4 = 8 \) products, while the expansion above has \( 4! = 24 \) terms. It fails already for the matrix with columns \( \e_2, \e_1, \e_3, \e_4 \): every one of the eight wrapped diagonals passes through a zero entry, so the shortcut returns \( 0 \), but the swap rule gives \( D(\e_2, \e_1, \e_3, \e_4) = -D(\e_1, \e_2, \e_3, \e_4) = -1 \). Never use Sarrus's rule beyond \( 3 \times 3 \), and never use it as a proof tool.
:::

## Exercises

### A. Check your understanding

:::: {#exr-area-and-volume-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the four rules (R1)–(R4) for signed area.
2. True or false: ordinary (unsigned) area satisfies \( \operatorname{area}(\u, \v + \w) = \operatorname{area}(\u, \v) + \operatorname{area}(\u, \w) \) for all \( \u, \v, \w \in \nR^2 \). Justify your answer.
3. Find the signed area of \( P((1, 3), (2, 4)) \). Is \( \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \) invertible?
4. Explain why any \( D \) satisfying (R1) and (R2) has \( D(\u, 5\u) = 0 \).
5. How many terms does the full expansion for \( 4 \times 4 \) matrices have, and how many products does the \( 4 \times 4 \) analogue of Sarrus's rule use?
:::
::::

::: {.solution}
(a) For all \( \u, \v \in \nR^2 \) and \( c \in \nR \): \( D(c\u, \v) = cD(\u, \v) = D(\u, c\v) \); \( D(\u + c\v, \v) = D(\u, \v) = D(\u, \v + c\u) \); \( D(\u, \u) = 0 \); \( D(\e_1, \e_2) = 1 \).

(b) False. Take \( \u = \e_1 \), \( \v = \e_2 \), \( \w = -\e_2 \). The left side is the area of \( P(\e_1, \0) \), which is \( 0 \); the right side is \( 1 + 1 = 2 \).

(c) With \( a = 1 \), \( b = 2 \), \( c = 3 \), \( d = 4 \), the signed area is \( ad - bc = 4 - 6 = -2 \). Since \( -2 \neq 0 \), the matrix is invertible by @thm-two-by-two-inverse.

(d) By the second shear rule with scalar \( -5 \), \( D(\u, 5\u) = D(\u, 5\u - 5\u) = D(\u, \0) \), and \( D(\u, \0) = D(\u, 0 \cdot \u) = 0 \cdot D(\u, \u) = 0 \) by (R1).

(e) The expansion has \( 4! = 24 \) terms, one for each rearrangement of \( \e_1, \dots, \e_4 \). The Sarrus-type diagram has only \( 8 \) products, so it must miss \( 16 \) of them.
:::

### B. Practice

:::: {#exr-area-and-volume-b1}
[B1: Signed Areas from the Rules]

Using only (R1)–(R4), in the manner of @exm-two-by-two-from-rules, compute the following. Then check each answer against \( ad - bc \).

::: {.enumerate options="label=(\alph*)"}
1. \( D((2, 1), (4, 5)) \).
2. \( D((1, 2), (3, 6)) \).
3. \( D((0, 3), (2, 0)) \).
:::
::::

::: {.solution}
(a) By the second shear rule with scalar \( -2 \), \( D((2, 1), (4, 5)) = D((2, 1), (4, 5) - 2(2, 1)) = D((2, 1), (0, 3)) \). By the first shear rule with scalar \( -\tfrac13 \), this equals \( D((2, 1) - \tfrac13(0, 3), (0, 3)) = D((2, 0), (0, 3)) \). By (R1) twice and (R4), \( D(2\e_1, 3\e_2) = 6D(\e_1, \e_2) = 6 \). Check: \( 2 \cdot 5 - 4 \cdot 1 = 6 \).

(b) By the second shear rule with scalar \( -3 \), \( D((1, 2), (3, 6)) = D((1, 2), (0, 0)) \), and \( D(\u, \0) = D(\u, 0 \cdot \u) = 0 \) by (R1). So the value is \( 0 \). Check: \( 1 \cdot 6 - 3 \cdot 2 = 0 \). The columns lie on one line, and the parallelogram is flat.

(c) By (R1) twice, \( D(3\e_2, 2\e_1) = 6D(\e_2, \e_1) \). By the Quick check (which uses only (R1) and (R2)), \( D(\e_2, \e_1) = -D(\e_1, \e_2) = -1 \) by (R4). So the value is \( -6 \). Check: with columns \( (0, 3) \) and \( (2, 0) \), \( a = 0 \), \( b = 2 \), \( c = 3 \), \( d = 0 \), and \( ad - bc = -6 \). The sign is negative because \( (2, 0) \) lies clockwise from \( (0, 3) \).
:::

:::: {#exr-area-and-volume-b2}
[B2: Equal Sides Force the Swap Rule]

Let \( D \colon \nR^2 \times \nR^2 \to \nR \) satisfy (R1), (R3) and (R5), but not necessarily (R2).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( D(\u, \v) = -D(\v, \u) \) for all \( \u, \v \in \nR^2 \).
2. Suppose moreover that (R4) holds. Deduce that \( D((a, c), (b, d)) = ad - bc \).
:::

*Hint: expand \( D(\u + \v, \u + \v) \).*
::::

::: {.solution}
(a) Let \( \u, \v \in \nR^2 \). By (R3), \( D(\u + \v, \u + \v) = 0 \). Expanding with (R5) in the first argument and then in the second,
\[
  0 = D(\u, \u) + D(\u, \v) + D(\v, \u) + D(\v, \v) = D(\u, \v) + D(\v, \u),
\]
where the second equality uses (R3) twice. Hence \( D(\u, \v) = -D(\v, \u) \).

(b) Write \( (a, c) = a\e_1 + c\e_2 \) and \( (b, d) = b\e_1 + d\e_2 \). By (R5) and (R1) in each argument,
\[
  D((a, c), (b, d)) = ab\,D(\e_1, \e_1) + ad\,D(\e_1, \e_2) + cb\,D(\e_2, \e_1) + cd\,D(\e_2, \e_2).
\]
By (R3) the first and last terms are \( 0 \). By (R4), \( D(\e_1, \e_2) = 1 \), and by (a), \( D(\e_2, \e_1) = -1 \). Hence \( D((a, c), (b, d)) = ad - bc \).
:::

### C. Going deeper

:::: {#exr-area-and-volume-c1}
[C1: Area of a Triangle]

Let \( \p, \q, \r \in \nR^2 \).

::: {.enumerate options="label=(\alph*)"}
1. Explain why the triangle with vertices \( \p, \q, \r \) has area \( \tfrac12 \lvert D(\q - \p, \r - \p) \rvert \), where \( D(\u, \v) \) is the signed area.
2. Find the area of the triangle with vertices \( (1, 2) \), \( (4, 3) \), \( (2, 6) \).
3. Hence decide whether the points \( (0, 1) \), \( (2, 4) \), \( (6, 10) \) lie on a line. Justify your answer.
:::
::::

::: {.solution}
(a) Translating by \( -\p \) does not change areas, so the triangle has the same area as the triangle with vertices \( \0 \), \( \u = \q - \p \), \( \v = \r - \p \). That triangle is half of the parallelogram \( P(\u, \v) \): the diagonal from \( \u \) to \( \v \) cuts \( P(\u, \v) \) into the triangle with vertices \( \0, \u, \v \) and the triangle with vertices \( \u + \v, \v, \u \), and the point reflection \( \x \mapsto \u + \v - \x \) maps the first onto the second, so they have equal area. The area of \( P(\u, \v) \) is \( \lvert D(\u, \v) \rvert \), since the signed area differs from the area only by its sign. Hence the triangle has area \( \tfrac12 \lvert D(\q - \p, \r - \p) \rvert \).

(b) Here \( \q - \p = (3, 1) \) and \( \r - \p = (1, 4) \), so \( D = 3 \cdot 4 - 1 \cdot 1 = 11 \) and the area is \( \tfrac{11}{2} \).

(c) With \( \p = (0, 1) \), \( \q - \p = (2, 3) \) and \( \r - \p = (6, 9) \), so \( D = 2 \cdot 9 - 6 \cdot 3 = 0 \) and the "triangle" has area \( 0 \). Indeed \( (6, 9) = 3(2, 3) \), so \( \r - \p \) is a multiple of \( \q - \p \), and all three points lie on the line through \( (0, 1) \) with direction \( (2, 3) \). Yes, they are collinear.
:::

:::: {#exr-area-and-volume-c2}
[C2: The \( 1 \times 1 \) Case]

For \( n = 1 \), the rules ask for a function \( f \colon F \to F \) of one vector in \( F^1 = F \).

::: {.enumerate options="label=(\alph*)"}
1. Explain why the rule "zero whenever two arguments are equal" imposes no condition when \( n = 1 \).
2. Prove that the only function \( f \colon F \to F \) that is linear with \( f(1) = 1 \) is \( f(a) = a \). Hence the determinant of a \( 1 \times 1 \) matrix \( (a) \) must be \( a \).
:::
::::

::: {.solution}
(a) The rule speaks about two **different** positions \( i \neq j \) holding equal vectors. With one argument there is no pair of positions, so the condition is vacuously true (@exm-vacuous-truth).

(b) Let \( f \) be linear with \( f(1) = 1 \), and let \( a \in F \). Since \( a = a \cdot 1 \), homogeneity gives \( f(a) = f(a \cdot 1) = a f(1) = a \). Conversely, \( a \mapsto a \) is linear and sends \( 1 \) to \( 1 \). Hence \( f(a) = a \) is the only such function.
:::
