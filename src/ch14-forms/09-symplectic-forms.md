# Alternating Forms and Darboux Bases

Almost every classification theorem so far in this chapter has carried the same asterisk — the exceptions being the crude invariants of Section 2, rank and the square class of the determinant, which need nothing of the field. Diagonalize a symmetric form: characteristic \( \ne 2 \). Split a form into a symmetric and an alternating half: characteristic \( \ne 2 \). Recover a form from its quadratic form: characteristic \( \ne 2 \). This section has no asterisk. Alternating forms admit a complete classification over **every** field, with no hypothesis on the characteristic at all, and the classification is as clean as a classification gets: one congruence class for each even rank.

Throughout, \( F \) is an arbitrary field, \( V \) is a finite-dimensional vector space over \( F \), and \( \beta \) is an **alternating** bilinear form on \( V \) (@def-alternating-form), meaning \( \beta(\v, \v) = 0 \) for **every** \( \v \in V \). Two facts from Section 3 are used constantly. First, \( \beta \) is then skew-symmetric, \( \beta(\u, \v) = -\beta(\v, \u) \), by @thm-alternating-vs-skew (a) — and that direction needs no hypothesis on \( F \). Second, by @prp-alternating-form-matrix (b) the matrix of \( \beta \) in any basis is skew-symmetric with **zero diagonal**, and we call such a matrix **alternating**. Symmetry of the situation is worth noting once: since \( \beta(\u,\v) = 0 \) if and only if \( \beta(\v,\u) = 0 \), "orthogonal" needs no left or right, and the radical \( \operatorname{rad}(\beta) \) of @def-radical is what one would want it to be from either side.

## The two-dimensional model

A symmetric form has a one-dimensional model to build from: on a line \( \Span(\v) \) it is \( q(c\v) = c^2 q(\v) \), a scalar multiple of the squaring function, and Section 4 assembled a general symmetric form out of such lines. An alternating form offers nothing on a line at all. For any \( \v \) and any scalars \( c, d \),
\[
\beta(c\v, d\v) = cd\,\beta(\v, \v) = 0 ,
\]
so \( \beta \) restricted to any line is zero. The one-dimensional pieces are all identical and all trivial. The smallest place where an alternating form has something to say is a plane, and there is essentially only one thing it can say there.

::: {#exm-alternating-2x2}
[Alternating Forms on a Plane]

Describe all alternating bilinear forms on \( F^2 \), and decide which are non-degenerate.
:::

::: {.solution}
An alternating \( 2 \times 2 \) matrix has zero diagonal and \( a_{21} = -a_{12} \), so it is
\[
\A = \begin{pmatrix} 0 & a \\ -a & 0 \end{pmatrix}
\]
for a single scalar \( a \in F \), and every such matrix is alternating. By @thm-form-matrix-determines the corresponding form is \( \beta(\x, \y) = a(x_1y_2 - x_2y_1) \). Its determinant is \( a^2 \), so by @prp-nondegenerate-iff-invertible the form is non-degenerate exactly when \( a \ne 0 \).

When \( a \ne 0 \), replacing the basis vector \( \e_2 \) by \( a^{-1}\e_2 \) replaces \( a \) by \( 1 \). So up to a change of basis there are exactly **two** alternating forms on \( F^2 \): the zero form and the one with matrix \( \begin{psmallmatrix} 0 & 1 \\ -1 & 0\end{psmallmatrix} \), whatever the field.
:::

That last matrix is the atom of the theory, and the pair of vectors producing it deserves a name. It is the alternating counterpart of the hyperbolic plane of Section 7: a two-dimensional space carrying a non-degenerate form on which the associated quadratic function vanishes identically. Here the vanishing is automatic, because *every* alternating form vanishes on the diagonal, so the whole content is in the pairing.

*A hyperbolic pair is two vectors that pair to \( 1 \) and to nothing else.*

::: {#def-hyperbolic-pair}
[Hyperbolic Pair]

Let \( \beta \) be an alternating form on \( V \). A **hyperbolic pair** for \( \beta \) is an ordered pair \( (\u, \w) \) of vectors of \( V \) with
\[
\beta(\u, \w) = 1 .
\]
Its **span** \( H = \Span(\u, \w) \) is called a **hyperbolic plane** for \( \beta \).
:::

The definition looks as though it asks for one condition, but it quietly supplies three more. Alternation already gives \( \beta(\u,\u) = \beta(\w,\w) = 0 \), and skewness gives \( \beta(\w, \u) = -1 \). So the matrix of \( \beta \) restricted to \( H \) in the ordered basis \( (\u, \w) \) is exactly \( \begin{psmallmatrix} 0 & 1 \\ -1 & 0\end{psmallmatrix} \). Also, \( \u \) and \( \w \) are automatically linearly independent: if \( \w = c\u \) then \( \beta(\u,\w) = c\,\beta(\u,\u) = 0 \ne 1 \), and \( \u \ne \0 \) for the same reason. So \( H \) really is a plane, \( \dim H = 2 \), and \( \beta \) restricted to \( H \) is non-degenerate.

::: {.warning}
**An alternating form is never diagonalizable, except when it is zero.** Section 4 found an orthogonal basis for every symmetric form in characteristic \( \ne 2 \); no such basis exists here. If \( \sB \) is any basis and \( \mtx{\beta}{\sB}{\sB} \) is diagonal, then its off-diagonal entries vanish by assumption and its diagonal entries vanish because \( \beta \) is alternating, so \( \mtx{\beta}{\sB}{\sB} = \0 \) and \( \beta = 0 \). The standard form below is a block form, and it has to be: the \( 2 \times 2 \) block is irreducible.
:::

## Splitting off a hyperbolic pair

The move that drives the whole section is the one Section 7 used for isotropic vectors: find a small non-degenerate piece, and cut the space along it. Here the small piece is a hyperbolic plane, and it can always be found as soon as \( \beta \) is not identically zero.

::: {#lem-alternating-hyperbolic-pair}
[Peeling Off a Hyperbolic Plane]

Let \( \beta \) be an alternating form on a finite-dimensional \( V \), and suppose \( \beta \ne 0 \).

::: {.enumerate options="label=(\alph*)"}
1. There is a hyperbolic pair \( (\u, \w) \) for \( \beta \).
2. For any such pair, with \( H = \Span(\u, \w) \) and
\[
H^{\perp_\beta} = \{\, \v \in V : \beta(\u, \v) = \beta(\w, \v) = 0 \,\} ,
\]
we have \( V = H \oplus H^{\perp_\beta} \) and \( \dim H^{\perp_\beta} = \dim V - 2 \).
3. \( \operatorname{rad}(\beta) = \operatorname{rad}\bigl(\beta|_{H^{\perp_\beta}}\bigr) \). In particular, if \( \beta \) is non-degenerate then so is its restriction to \( H^{\perp_\beta} \).
:::
:::

::: {.idea}
For (a), the hypothesis \( \beta \ne 0 \) hands us two vectors pairing to something non-zero; divide one of them by that scalar. For (b), the two conditions cutting out \( H^{\perp_\beta} \) are two linear conditions, so the count should be \( \dim V - 2 \), and Rank–Nullity will say so once we check that the two conditions are independent — which is exactly what \( \beta(\u,\w) = 1 \) provides. Part (c) is the bookkeeping that lets the induction in the theorem keep its hypothesis.
:::

::: {.proof}
(a) Since \( \beta \ne 0 \) there are \( \u_0, \w_0 \in V \) with \( c \coloneqq \beta(\u_0, \w_0) \ne 0 \). Put \( \u = \u_0 \) and \( \w = c^{-1}\w_0 \), which is legitimate because \( c \ne 0 \) and \( F \) is a field. Then \( \beta(\u, \w) = c^{-1}\beta(\u_0,\w_0) = 1 \) by linearity in the second argument.

(b) Define \( \varphi \colon V \to F^2 \) by \( \varphi(\v) = \bigl(\beta(\u, \v),\, \beta(\w, \v)\bigr) \). It is linear, because \( \beta \) is linear in its second argument, and \( \ker\varphi = H^{\perp_\beta} \) by the definition of \( H^{\perp_\beta} \). It is surjective:
\[
\varphi(\w) = (\beta(\u,\w), \beta(\w,\w)) = (1, 0), \qquad
\varphi(\u) = (0, -1),
\]
using \( \beta(\w,\w) = \beta(\u,\u) = 0 \) and \( \beta(\w,\u) = -1 \), and these two values span \( F^2 \). Hence \( \rank\varphi = 2 \) and \( \dim H^{\perp_\beta} = \dim V - 2 \) by Rank–Nullity (@thm-rank-nullity).

Next, \( H \cap H^{\perp_\beta} = \{\0\} \). Let \( \v = a\u + b\w \) lie in \( H^{\perp_\beta} \). Then \( 0 = \beta(\u, \v) = a\beta(\u,\u) + b\beta(\u,\w) = b \), and \( 0 = \beta(\w, \v) = a\beta(\w,\u) = -a \), so \( a = b = 0 \). Hence the sum \( H + H^{\perp_\beta} \) is direct (@thm-direct-sum-criteria), and by @thm-dimension-formula-subspace-dim its dimension is \( 2 + (\dim V - 2) = \dim V \), so it is all of \( V \) (@thm-dim-impl-eq).

(c) \( (\supseteq) \) Let \( \v \in H^{\perp_\beta} \) satisfy \( \beta(\z, \v) = 0 \) for every \( \z \in H^{\perp_\beta} \). Any \( \y \in V \) decomposes as \( \y = \h + \z \) with \( \h \in H \) and \( \z \in H^{\perp_\beta} \) by (b), and \( \beta(\h, \v) = -\beta(\v, \h) = 0 \) because \( \v \in H^{\perp_\beta} \) and \( \h \) is a combination of \( \u \) and \( \w \). Hence \( \beta(\y, \v) = 0 \) for every \( \y \in V \), so \( \v \in \operatorname{rad}(\beta) \).

\( (\subseteq) \) Let \( \v \in \operatorname{rad}(\beta) \). Then in particular \( \beta(\u,\v) = \beta(\w,\v) = 0 \), so \( \v \in H^{\perp_\beta} \), and \( \beta(\z,\v) = 0 \) for every \( \z \) at all, so \( \v \) lies in the radical of the restriction. This proves the lemma.
:::

Notice what the proof did **not** use: it never divided by \( 2 \), never distinguished \( \beta \) from \( -\beta \), and never needed a vector with \( \beta(\v,\v) \ne 0 \) — which is fortunate, since no such vector exists. Compare the corresponding step for symmetric forms, @lem-anisotropic-vector-exists in Section 4: there the whole difficulty was producing a vector on which the quadratic form did not vanish, and producing it cost the hypothesis \( \operatorname{char} F \ne 2 \). Here the quadratic form vanishes everywhere and we do not care.

## The standard form

With the lemma in hand the classification is an induction that peels two dimensions at a time.

::: {#thm-symplectic-standard-form}
[Standard Form of an Alternating Form]

Let \( F \) be **any** field, let \( V \) be a vector space over \( F \) with \( \dim V = n \), and let \( \beta \) be an alternating bilinear form on \( V \). Then there are an integer \( m \ge 0 \) with \( 2m \le n \) and a basis
\[
\sB = (\u_1, \dots, \u_m, \w_1, \dots, \w_m, \z_1, \dots, \z_{n-2m})
\]
of \( V \) such that, for all \( i, j \),
\[
\beta(\u_i, \w_j) = \delta_{ij}, \qquad \beta(\u_i, \u_j) = \beta(\w_i, \w_j) = 0 ,
\]
and \( \beta(\z_k, \v) = 0 \) for every \( k \) and every \( \v \in V \). Equivalently, in this basis

\[
\mtx{\beta}{\sB}{\sB} = \vOmega_{2m} \oplus \0_{n-2m}, \qquad
\vOmega_{2m} \coloneqq \begin{pmatrix} \0 & \I_m \\ -\I_m & \0 \end{pmatrix} .
\]{#eq-standard-alternating-matrix}

In particular:

::: {.enumerate options="label=(\alph*)"}
1. every alternating \( \A \in M_n(F) \) is congruent to \( \vOmega_{2m} \oplus \0_{n-2m} \) for exactly one \( m \);
2. if \( \beta \) is non-degenerate then \( n = 2m \) is **even** and \( \mtx{\beta}{\sB}{\sB} = \vOmega_{n} \).
:::
:::

::: {.idea}
Induction on \( n \), two dimensions at a time. ① If \( \beta = 0 \), take \( m = 0 \) and any basis; this is the base case and also the case that stops the recursion. ② Otherwise @lem-alternating-hyperbolic-pair produces a hyperbolic pair \( (\u_1, \w_1) \) and splits \( V = H \oplus H^{\perp_\beta} \) with \( \dim H^{\perp_\beta} = n - 2 \); apply the induction hypothesis to \( \beta \) restricted to \( H^{\perp_\beta} \), and put the pieces together. ③ Finally reorder the basis so that all the \( \u \)'s come before all the \( \w \)'s, which turns a string of \( 2 \times 2 \) blocks into the one block matrix displayed. The radical, by part (c) of the lemma, is exactly what the last stage of the recursion leaves behind.
:::

::: {.proof}
**Existence, by induction on \( n = \dim V \).** For \( n = 0 \) and \( n = 1 \) every alternating form is zero: in dimension \( 1 \), \( \beta(c\v, d\v) = cd\,\beta(\v,\v) = 0 \). Take \( m = 0 \).

Let \( n \ge 2 \) and assume the statement for all spaces of dimension less than \( n \).

*Case 1: \( \beta = 0 \).* Take \( m = 0 \) and any basis of \( V \); every required equation reads \( 0 = 0 \).

*Case 2: \( \beta \ne 0 \).* By @lem-alternating-hyperbolic-pair (a) there is a hyperbolic pair \( (\u_1, \w_1) \), and by (b) we have \( V = H \oplus W \) with \( H = \Span(\u_1, \w_1) \) and \( W = H^{\perp_\beta} \) of dimension \( n - 2 \). The restriction \( \beta|_W \) is again alternating, being a restriction of an alternating form, so the induction hypothesis applies to it: there is a basis
\[
(\u_2, \dots, \u_m,\ \w_2, \dots, \w_m,\ \z_1, \dots, \z_{n-2m})
\]
of \( W \) in which \( \beta|_W(\u_i, \w_j) = \delta_{ij} \), all other pairings among the \( \u \)'s and \( \w \)'s vanish, and each \( \z_k \) lies in \( \operatorname{rad}(\beta|_W) \).

Putting \( \u_1 \) and \( \w_1 \) in front gives a basis of \( V = H \oplus W \). The required equations hold: within \( H \) they are the definition of a hyperbolic pair together with alternation; within \( W \) they are the induction hypothesis; and across the two, every pairing of \( \u_1 \) or \( \w_1 \) with a vector of \( W \) vanishes because \( W = H^{\perp_\beta} \) and \( \beta \) is skew-symmetric. Finally each \( \z_k \) lies in \( \operatorname{rad}(\beta|_W) = \operatorname{rad}(\beta) \) by @lem-alternating-hyperbolic-pair (c), which is the last assertion.

**The matrix.** Order the basis as \( \sB = (\u_1, \dots, \u_m, \w_1, \dots, \w_m, \z_1, \dots, \z_{n-2m}) \). By @def-form-matrix the \( (i,j) \) entry of \( \mtx{\beta}{\sB}{\sB} \) is the pairing of the \( i \)-th and \( j \)-th basis vectors, and the equations above say precisely that the top-left \( m \times m \) block and the \( \w \)-\( \w \) block are \( \0 \), the \( \u \)-\( \w \) block is \( \I_m \), the \( \w \)-\( \u \) block is \( -\I_m \), and every row and column indexed by a \( \z_k \) is zero. That is @eq-standard-alternating-matrix.

**(a).** Given alternating \( \A \in M_n(F) \), let \( \beta(\x,\y) = \x\tp\A\y \) on \( F^n \); it is alternating by @prp-alternating-form-matrix (b). The basis just constructed gives \( \P\tp\A\P = \vOmega_{2m}\oplus\0_{n-2m} \) with \( \P \) the matrix whose columns are the basis vectors, by @thm-change-of-basis-form, so \( \A \simeq \vOmega_{2m}\oplus\0_{n-2m} \). Uniqueness of \( m \): congruence preserves rank (@thm-congruence-preserves-rank), and \( \rank(\vOmega_{2m}\oplus\0_{n-2m}) = 2m \) because \( \vOmega_{2m} \) is invertible, its square being \( -\I_{2m} \). So \( 2m = \rank\A \) is determined by \( \A \).

**(b).** If \( \beta \) is non-degenerate then \( \operatorname{rad}(\beta) = \{\0\} \) by @def-nondegenerate, so there are no \( \z_k \), that is \( n = 2m \). This proves the theorem.
:::

::: {#def-darboux-basis}
[Symplectic Basis]

A basis of \( V \) as in @thm-symplectic-standard-form is a **symplectic basis**, or a **Darboux basis**, for the alternating form \( \beta \). A non-degenerate alternating form on a finite-dimensional space is called a **symplectic form**, and the pair \( (V, \beta) \) a **symplectic vector space**.
:::

Now read the hypotheses of the theorem again, and notice what is missing. There is no "\( \operatorname{char} F \ne 2 \)", and there is no place one could be inserted, because no step of the proof divided by \( 2 \). Compare the statements this chapter has accumulated:

- @thm-alternating-vs-skew: skew implies alternating only when \( \operatorname{char} F \ne 2 \).
- @thm-symmetric-alternating-decomposition: the splitting into halves exists only when \( \operatorname{char} F \ne 2 \).
- @thm-polarization-forms: a symmetric form is recovered from its quadratic form only when \( \operatorname{char} F \ne 2 \).
- @thm-symmetric-form-diagonalizable: a symmetric form has an orthogonal basis only when \( \operatorname{char} F \ne 2 \).
- @thm-symplectic-standard-form: no hypothesis.

Over \( \nF_2 \), where every one of the first four statements is false, the last one is true and gives a complete classification. The reason is visible in the proof: the symmetric theory needs a vector with \( q(\v) \ne 0 \), and that vector is manufactured by a polarization identity that divides by \( 2 \). The alternating theory needs a *pair* with \( \beta(\u,\w) \ne 0 \), and a pair is handed over by the assumption \( \beta \ne 0 \) itself, free of charge. Symmetric forms are hard in characteristic \( 2 \); alternating forms are not hard anywhere.

::: {.check}
Over \( \nF_2 \) we have \( -1 = 1 \), so \( \vOmega_{2m} = \begin{psmallmatrix} \0 & \I_m \\ \I_m & \0\end{psmallmatrix} \), which is a **symmetric** matrix. Does that contradict the warning above, that an alternating form is never diagonalizable?
:::

::: {.solution}
No. Over \( \nF_2 \) every alternating matrix is symmetric, since skew-symmetric and symmetric are the same condition there (@thm-alternating-vs-skew and the warning after it). What distinguishes alternating from merely symmetric over \( \nF_2 \) is the zero diagonal, and \( \vOmega_{2m} \) does have a zero diagonal. The warning says a **diagonal** alternating matrix must be \( \0 \), and \( \vOmega_{2m} \) is symmetric but not diagonal. Concretely, over \( \nF_2 \) the matrix \( \begin{psmallmatrix} 0 & 1 \\ 1 & 0\end{psmallmatrix} \) is the Gram matrix of the alternating form \( \beta(\x,\y) = x_1y_2 + x_2y_1 \), and no change of basis makes it diagonal.
:::

## Running the algorithm

The proof is an algorithm, and it is short enough to carry out by hand. Each round of the induction does three things: find a pair with \( \beta(\u,\w) \ne 0 \), rescale to make the value \( 1 \), and then correct every remaining basis vector so that it becomes orthogonal to both. The correction is a formula worth recording. If \( \beta(\u,\w) = 1 \), put

\[
\v' \coloneqq \v - \beta(\v, \w)\,\u + \beta(\v, \u)\,\w .
\]{#eq-hyperbolic-projection}

Expanding and using \( \beta(\u,\u) = \beta(\w,\w) = 0 \), \( \beta(\u,\w) = 1 \) and \( \beta(\w,\u) = -1 \),
\[
\begin{aligned}
\beta(\v', \u) &= \beta(\v,\u) - \beta(\v,\w)\cdot 0 + \beta(\v,\u)\cdot(-1) = 0, \\
\beta(\v', \w) &= \beta(\v,\w) - \beta(\v,\w)\cdot 1 + \beta(\v,\u)\cdot 0 = 0 ,
\end{aligned}
\]
so \( \v' \in H^{\perp_\beta} \). It is the alternating analogue of subtracting a projection in Gram–Schmidt, with one difference: nothing is divided by a length, so it works over any field.

::: {#exm-darboux-basis-4x4}
[A Symplectic Basis for a 4 × 4 Form]

Let \( \beta(\x,\y) = \x\tp\A\y \) on \( \nQ^4 \), where
\[
\A = \begin{pmatrix}
0 & 1 & 2 & 3 \\
-1 & 0 & 1 & 1 \\
-2 & -1 & 0 & 0 \\
-3 & -1 & 0 & 0
\end{pmatrix} .
\]
Find a symplectic basis, and the matrix \( \P \) with \( \P\tp\A\P = \vOmega_4 \).
:::

::: {.solution}
The matrix is skew-symmetric with zero diagonal, so \( \beta \) is alternating (@prp-alternating-form-matrix (b)).

**Round 1.** The entry \( a_{12} = \beta(\e_1, \e_2) = 1 \) is already \( 1 \), so \( (\u_1, \w_1) = (\e_1, \e_2) \) is a hyperbolic pair and no rescaling is needed. Correct \( \e_3 \) and \( \e_4 \) by @eq-hyperbolic-projection, reading the needed values off the matrix: \( \beta(\e_3,\e_2) = a_{32} = -1 \), \( \beta(\e_3,\e_1) = a_{31} = -2 \), \( \beta(\e_4,\e_2) = a_{42} = -1 \), \( \beta(\e_4,\e_1) = a_{41} = -3 \). So
\[
\begin{aligned}
\v_3 &= \e_3 + \e_1 - 2\e_2 = (1, -2, 1, 0), \\
\v_4 &= \e_4 + \e_1 - 3\e_2 = (1, -3, 0, 1).
\end{aligned}
\]

**Round 2.** Both \( \v_3 \) and \( \v_4 \) pair to zero with \( \e_1 \) and \( \e_2 \), as the formula guarantees, so the recursion continues inside \( \Span(\v_3, \v_4) \). Compute \( \A\v_4 \) row by row with \( \v_4 = (1,-3,0,1) \): row \( 1 \) gives \( 0 - 3 + 0 + 3 = 0 \), row \( 2 \) gives \( -1 + 0 + 0 + 1 = 0 \), row \( 3 \) gives \( -2 + 3 + 0 + 0 = 1 \), row \( 4 \) gives \( -3 + 3 + 0 + 0 = 0 \). So \( \A\v_4 = (0,0,1,0)\tp \), and
\[
\beta(\v_3, \v_4) = \v_3\tp(\A\v_4) = 1\cdot 0 + (-2)\cdot 0 + 1\cdot 1 + 0\cdot 0 = 1 .
\]
The pair \( (\u_2, \w_2) = (\v_3, \v_4) \) is therefore hyperbolic, and the recursion stops: the two remaining dimensions are used up.

**The answer.** The symplectic basis is \( \sB = (\e_1, \v_3, \e_2, \v_4) \), listing the \( \u \)'s first and then the \( \w \)'s. The matrix whose columns are these four vectors is
\[
\P = \begin{pmatrix}
1 & 1 & 0 & 1 \\
0 & -2 & 1 & -3 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix},
\qquad
\P\tp\A\P = \vOmega_4 .
\]
A check of two entries confirms the pattern: the \( (1,3) \) entry of \( \P\tp\A\P \) is \( \beta(\e_1, \e_2) = 1 \) and the \( (2,4) \) entry is \( \beta(\v_3, \v_4) = 1 \), while the \( (1,2) \) entry is \( \beta(\e_1, \v_3) = a_{11} + a_{12}(-2) + a_{13} = 0 - 2 + 2 = 0 \).
:::

## What the standard form classifies

The theorem is a classification, and it is worth reading off exactly what it classifies and how coarsely.

::: {#cor-alternating-even-rank}
[Alternating Matrices Are Classified by Rank]

Let \( F \) be any field and let \( \A, \B \in M_n(F) \) be alternating.

::: {.enumerate options="label=(\alph*)"}
1. \( \rank\A \) is **even**.
2. \( \A \simeq \B \) if and only if \( \rank\A = \rank\B \).
3. There are exactly \( \lfloor n/2 \rfloor + 1 \) congruence classes of alternating matrices in \( M_n(F) \), one for each even rank \( 0, 2, 4, \dots \) up to \( n \).
4. If \( n \) is odd, every alternating \( \A \in M_n(F) \) is singular.
:::
:::

::: {.proof}
(a) By @thm-symplectic-standard-form (a), \( \A \simeq \vOmega_{2m}\oplus\0_{n-2m} \) for some \( m \), and congruence preserves rank (@thm-congruence-preserves-rank), so \( \rank\A = 2m \).

(b) \( (\Rightarrow) \) is @thm-congruence-preserves-rank. \( (\Leftarrow) \) If \( \rank\A = \rank\B = 2m \) then by (a) and @thm-symplectic-standard-form both are congruent to \( \vOmega_{2m}\oplus\0_{n-2m} \), and congruence is an equivalence relation (@prp-congruence-equivalence), so \( \A \simeq \B \).

(c) By (a) and (b) the classes are in bijection with the even integers \( 2m \) satisfying \( 0 \le 2m \le n \), and there are \( \lfloor n/2\rfloor + 1 \) of those.

(d) By (a), \( \rank\A \) is even and at most \( n \); since \( n \) is odd, \( \rank\A \le n - 1 < n \), so \( \A \) is not invertible.
:::

Part (d) deserves a second look, because there is a one-line proof of it that works only half the time. If \( \A\tp = -\A \) with \( n \) odd, then \( \det\A = \det(\A\tp) = \det(-\A) = (-1)^n\det\A = -\det\A \), so \( (1+1)\det\A = 0 \) and \( \det\A = 0 \) — provided \( 1 + 1 \ne 0 \). In characteristic \( 2 \) that argument collapses, and it collapses for a real reason: over \( \nF_2 \) the matrix \( \diag(1,0,0) \) is skew-symmetric (because skew means symmetric there) and has odd rank \( 1 \). Part (d) survives because it is a statement about *alternating* matrices, and the standard form proves it without ever touching the determinant.

::: {.warning}
**"Skew-symmetric" is not enough.** Every statement in @cor-alternating-even-rank is about alternating matrices: skew-symmetric **with zero diagonal**. Over \( \nF_2 \), \( \I_2 \) is skew-symmetric and has rank \( 2 \), which is harmless; but \( \diag(1,0) \in M_2(\nF_2) \) is skew-symmetric of rank \( 1 \), and \( \I_3 \in M_3(\nF_2) \) is skew-symmetric and invertible. Both would contradict the corollary if "skew-symmetric" could be substituted for "alternating". In characteristic \( \ne 2 \) the two words agree (@thm-alternating-vs-skew (b)) and the distinction can be forgotten; nowhere else.
:::

## The determinant, and the Pfaffian

Part (a) of @thm-symplectic-standard-form says that in even size an invertible alternating matrix is congruent to \( \vOmega_n \). Congruence multiplies the determinant by a square (@thm-congruence-determinant-class), so the determinant of an alternating matrix is heavily constrained.

::: {#cor-alternating-determinant-square}
[The Determinant of an Alternating Matrix Is a Square]

Let \( F \) be any field and let \( \A \in M_n(F) \) be alternating. Then \( \det\A \) is a square in \( F \): there is \( c \in F \) with \( \det\A = c^2 \).
:::

::: {.proof}
If \( \A \) is singular then \( \det\A = 0 = 0^2 \). So assume \( \A \) is invertible. Then \( \rank\A = n \) is even by @cor-alternating-even-rank (a), say \( n = 2m \), and @thm-symplectic-standard-form (a) supplies an invertible \( \P \) with \( \P\tp\A\P = \vOmega_{2m} \). Taking determinants and using @thm-congruence-determinant-class,
\[
\det\vOmega_{2m} = (\det\P)^2\det\A .
\]
Now \( \det\vOmega_{2m} = 1 \). Indeed, performing the \( m \) row swaps \( R_i \leftrightarrow R_{m+i} \) for \( i = 1, \dots, m \) turns \( \vOmega_{2m} \) into \( (-\I_m) \oplus \I_m \), so by @thm-det-row-operations (a) and @thm-det-block-triangular,
\[
(-1)^m \det\vOmega_{2m} = \det\bigl((-\I_m)\oplus\I_m\bigr) = (-1)^m ,
\]
and \( (-1)^m \) is invertible, so \( \det\vOmega_{2m} = 1 \). Hence \( \det\A = (\det\P)^{-2} = \bigl((\det\P)^{-1}\bigr)^2 \), a square, since \( \det\P \ne 0 \). This proves the corollary.
:::

The corollary says a square root of \( \det\A \) exists; it does not produce one. In fact there is a canonical choice. For every even \( n \) there is a polynomial \( \operatorname{Pf} \) in the entries \( a_{ij} \) with \( i < j \), with integer coefficients, called the **Pfaffian**, satisfying \( \det\A = \operatorname{Pf}(\A)^2 \) for every alternating \( \A \). Constructing it in general is a piece of multilinear algebra that we do not carry out, so we record only the name and the two smallest cases, both of which can be checked by expanding the determinant.

::: {#exm-pfaffian-small}
[The Pfaffian in Sizes 2 and 4]

For \( n = 2 \),
\[
\A = \begin{pmatrix} 0 & a \\ -a & 0\end{pmatrix}, \qquad \det\A = a^2, \qquad \operatorname{Pf}(\A) = a .
\]
For \( n = 4 \), write the six independent entries as \( a = a_{12} \), \( b = a_{13} \), \( c = a_{14} \), \( d = a_{23} \), \( e = a_{24} \), \( f = a_{34} \). Expanding the \( 4 \times 4 \) determinant gives
\[
\det\A = (af - be + cd)^2, \qquad \operatorname{Pf}(\A) = af - be + cd .
\]
The three terms pair up \( \{1,2\}\{3,4\} \), \( \{1,3\}\{2,4\} \) and \( \{1,4\}\{2,3\} \): the Pfaffian sums over the ways of splitting \( \{1,2,3,4\} \) into two pairs, with a sign. For the matrix \( \A \) of @exm-darboux-basis-4x4 this reads \( \operatorname{Pf}(\A) = 1\cdot 0 - 2\cdot 1 + 3\cdot 1 = 1 \), and indeed \( \det\A = 1 \).
:::

::: {.remark}
The Pfaffian is not merely *a* square root: it is the one that behaves well under congruence, satisfying \( \operatorname{Pf}(\P\tp\A\P) = \det(\P)\operatorname{Pf}(\A) \). That identity is the reason the Pfaffian matters. Section 10 records one of its consequences for the symplectic group, without proof and without leaning on it. We do not prove the identity either.
:::

## Symmetric against alternating

Put the two halves of the chapter side by side. Both are theories of a bilinear form under congruence; the answers could hardly be more different.

| | Symmetric forms | Alternating forms |
|---|---|---|
| Field hypothesis | \( \operatorname{char} F \ne 2 \) for every theorem | none |
| Canonical form | diagonal, entries not canonical | \( \vOmega_{2m}\oplus\0_{n-2m} \) |
| Complete invariants | rank **and** more: over \( \nR \) the signature, over \( \nQ \) the discriminant and local data | rank alone |
| Classes in \( M_n(\nR) \) | \( \tfrac12(n+1)(n+2) \) | \( \lfloor n/2\rfloor + 1 \) |
| Classes in \( M_n(\nC) \) | \( n+1 \) | \( \lfloor n/2\rfloor + 1 \) |
| Classes in \( M_n(\nQ) \) | infinitely many already for \( n = 1 \) | \( \lfloor n/2\rfloor + 1 \) |
| Possible ranks | every \( r \) with \( 0 \le r \le n \) | even \( r \) only |
| Effect of the field | decisive | none |

Two entries carry the point. Over \( \nQ \), the \( 1\times 1 \) symmetric matrices \( [1], [2], [3], [5], \dots \) are pairwise non-congruent, because congruence in size \( 1 \) multiplies by a non-zero square (@thm-congruence-determinant-class) and distinct squarefree positive integers lie in distinct classes of \( \nQ^{\times}/(\nQ^{\times})^2 \). So the symmetric classification over \( \nQ \) is an infinite problem in number theory — Section 4 said as much. The alternating classification over \( \nQ \) has four classes in size \( 6 \), and the same four over \( \nF_2 \), over \( \nR \), and over any field whatsoever.

The reason, one last time, is the two-dimensional model. A symmetric form on a line is \( c \mapsto ac^2 \), and rescaling changes \( a \) by a square, so the diagonal entry carries the field's arithmetic with it. An alternating form on a plane is \( \begin{psmallmatrix} 0 & a \\ -a & 0\end{psmallmatrix} \), and rescaling *one* of the two basis vectors changes \( a \) to \( ca \) for any \( c \ne 0 \) — an arbitrary non-zero scalar, not a square. There is nothing left for the field to remember.

## Exercises

### A. Check your understanding

::: {#exr-symplectic-forms-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define a hyperbolic pair for an alternating form, and say why its two vectors are automatically linearly independent.
2. State @thm-symplectic-standard-form, and say which hypothesis on \( F \) it needs.
3. Determine whether the following is correct: every skew-symmetric matrix over every field has even rank. Justify your answer.
4. Why can an alternating form never have a diagonal Gram matrix, unless the form is zero?
5. How many congruence classes of alternating matrices are there in \( M_5(\nR) \)? In \( M_5(\nF_7) \)?
:::
:::

::: {.solution}
(a) A pair \( (\u,\w) \) with \( \beta(\u,\w) = 1 \) (@def-hyperbolic-pair). If \( \w = c\u \), then \( \beta(\u,\w) = c\,\beta(\u,\u) = 0 \ne 1 \), so \( \w \notin \Span(\u) \); and \( \u \ne \0 \) since \( \beta(\0,\w) = 0 \). Two vectors, neither in the span of the other, are independent.

(b) Every alternating form on an \( n \)-dimensional \( V \) has a basis in which its matrix is \( \vOmega_{2m}\oplus\0_{n-2m} \), with \( 2m = \rank\beta \); equivalently every alternating matrix is congruent to exactly one such matrix. **No** hypothesis on \( F \) is needed — in particular none on \( \operatorname{char} F \).

(c) Incorrect. Over \( \nF_2 \), \( \diag(1,0) \) is skew-symmetric, because \( -1 = 1 \) makes skew-symmetric and symmetric the same condition, and it has rank \( 1 \). The correct statement is about **alternating** matrices, @cor-alternating-even-rank (a). In characteristic \( \ne 2 \) the two notions coincide (@thm-alternating-vs-skew (b)) and the statement is true.

(d) The off-diagonal entries of a diagonal matrix are \( 0 \) by definition, and the diagonal entries of the Gram matrix of an alternating form are \( \beta(\v_i,\v_i) = 0 \). So the whole matrix is \( \0 \), and then \( \beta = 0 \) by @thm-form-matrix-determines (b).

(e) \( \lfloor 5/2\rfloor + 1 = 3 \) in both cases, by @cor-alternating-even-rank (c): the ranks \( 0, 2, 4 \). The field makes no difference.
:::

### B. Practice

::: {#exr-symplectic-forms-b1}
[B1: A symplectic basis]

Let \( \beta(\x,\y) = \x\tp\B\y \) on \( \nQ^4 \), with
\[
\B = \begin{pmatrix}
0 & 0 & 1 & 1 \\
0 & 0 & 2 & 1 \\
-1 & -2 & 0 & 0 \\
-1 & -1 & 0 & 0
\end{pmatrix} .
\]
Find a symplectic basis for \( \beta \) and an invertible \( \P \in M_4(\nQ) \) with \( \P\tp\B\P = \vOmega_4 \).
:::

::: {.solution}
\( \B \) is skew-symmetric with zero diagonal, hence alternating (@prp-alternating-form-matrix (b)).

**Round 1.** Here \( \beta(\e_1,\e_2) = 0 \), so the first two standard basis vectors are **not** a hyperbolic pair; this is the step the worked example did not need. Look for any non-zero entry: \( \beta(\e_1, \e_3) = 1 \). Take \( \u_1 = \e_1 \), \( \w_1 = \e_3 \).

Correct the other two by @eq-hyperbolic-projection, using \( \beta(\e_2,\e_3) = 2 \), \( \beta(\e_2,\e_1) = 0 \), \( \beta(\e_4,\e_3) = 0 \), \( \beta(\e_4,\e_1) = -1 \):
\[
\begin{aligned}
\v_2 &= \e_2 - 2\e_1 + 0\cdot\e_3 = (-2, 1, 0, 0), \\
\v_4 &= \e_4 - 0\cdot\e_1 - \e_3 = (0, 0, -1, 1).
\end{aligned}
\]

**Round 2.** Compute \( \B\v_4 \) with \( \v_4 = (0,0,-1,1) \): row \( 1 \) gives \( -1 + 1 = 0 \), row \( 2 \) gives \( -2 + 1 = -1 \), rows \( 3 \) and \( 4 \) give \( 0 \). So \( \B\v_4 = (0,-1,0,0)\tp \) and
\[
\beta(\v_2, \v_4) = \v_2\tp(\B\v_4) = (-2)\cdot 0 + 1\cdot(-1) = -1 .
\]
This is non-zero but not \( 1 \), so rescale: replace \( \v_4 \) by \( \w_2 \coloneqq -\v_4 = (0,0,1,-1) \), giving \( \beta(\v_2, \w_2) = 1 \). Set \( \u_2 = \v_2 \).

**The answer.** The symplectic basis is \( (\u_1, \u_2, \w_1, \w_2) = (\e_1,\ (-2,1,0,0),\ \e_3,\ (0,0,1,-1)) \), so
\[
\P = \begin{pmatrix}
1 & -2 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 1 \\
0 & 0 & 0 & -1
\end{pmatrix},
\qquad \P\tp\B\P = \vOmega_4 .
\]
\( \P \) is invertible, being block upper triangular with invertible diagonal blocks, and \( \det\P = -1 \ne 0 \).
:::

::: {#exr-symplectic-forms-b2}
[B2: Pfaffians and determinants]

For each matrix below, compute the Pfaffian using the formula of @exm-pfaffian-small, and verify that its square is the determinant.
\[
\A_1 = \begin{pmatrix}
0 & 2 & 0 & 1 \\ -2 & 0 & 1 & 0 \\ 0 & -1 & 0 & 3 \\ -1 & 0 & -3 & 0
\end{pmatrix},
\qquad
\A_2 = \begin{pmatrix}
0 & 1 & 1 & 1 \\ -1 & 0 & 1 & 1 \\ -1 & -1 & 0 & 1 \\ -1 & -1 & -1 & 0
\end{pmatrix} .
\]
Hence write down, for each, an invertible matrix congruence class in the sense of @cor-alternating-even-rank.
:::

::: {.solution}
For \( \A_1 \): \( a = 2 \), \( b = 0 \), \( c = 1 \), \( d = 1 \), \( e = 0 \), \( f = 3 \), so \( \operatorname{Pf}(\A_1) = af - be + cd = 6 - 0 + 1 = 7 \) and \( \det\A_1 = 49 \). Expanding the determinant along the first row confirms \( 49 \).

For \( \A_2 \): \( a = b = c = d = e = f = 1 \), so \( \operatorname{Pf}(\A_2) = 1 - 1 + 1 = 1 \) and \( \det\A_2 = 1 \).

Both determinants are non-zero, so both matrices have rank \( 4 \), and by @cor-alternating-even-rank (b) both lie in the single congruence class of invertible alternating matrices in \( M_4(\nQ) \): each is congruent to \( \vOmega_4 \), and therefore \( \A_1 \simeq \A_2 \). Note that the two have different determinants, \( 49 \) and \( 1 \); congruence changes the determinant by a square (@thm-congruence-determinant-class), and \( 49 = 7^2 \).
:::

::: {#exr-symplectic-forms-b3}
[B3: Determine which of the following]

Determine which of the following matrices are alternating, and for those that are, give the rank and the standard form \( \vOmega_{2m}\oplus\0_{n-2m} \) it is congruent to. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \begin{psmallmatrix} 0 & 5 \\ -5 & 0 \end{psmallmatrix} \) over \( \nQ \).
2. \( \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix} \) over \( \nQ \).
3. \( \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix} \) over \( \nF_2 \).
4. The \( 5\times 5 \) matrix with \( a_{ij} = j - i \) over \( \nQ \).
:::
:::

::: {.solution}
(a) Alternating: zero diagonal and \( a_{21} = -a_{12} \). Its determinant is \( 25 \ne 0 \), so the rank is \( 2 \) and it is congruent to \( \vOmega_2 \). (Explicitly, scaling the second basis vector by \( 1/5 \) does it.)

(b) Not alternating. It is symmetric with \( a_{12} = 1 \ne -1 = -a_{21} \), so it is not even skew-symmetric over \( \nQ \).

(c) Alternating. Over \( \nF_2 \) we have \( 1 = -1 \), so the matrix is skew-symmetric, and its diagonal is zero. Its determinant is \( -1 = 1 \ne 0 \), so the rank is \( 2 \) and it is congruent to \( \vOmega_2 = \begin{psmallmatrix} 0 & 1 \\ 1 & 0\end{psmallmatrix} \) — it **is** \( \vOmega_2 \), since \( -1 = 1 \). Comparing (b) and (c): the same array of symbols is alternating over one field and not over another.

(d) Alternating: \( a_{ii} = 0 \) and \( a_{ji} = i - j = -a_{ij} \). Its rank is even by @cor-alternating-even-rank (a), and it is not zero, so the rank is \( 2 \) or \( 4 \). Every row is a combination of \( (1,2,3,4,5) \) and \( (1,1,1,1,1) \): indeed row \( i \) is \( (j - i)_j = (1,2,3,4,5) - i(1,1,1,1,1) \). So the row space has dimension at most \( 2 \), and rows \( 1 \) and \( 2 \) are independent, giving rank exactly \( 2 \). Hence the matrix is congruent to \( \vOmega_2 \oplus \0_3 \). In particular it is singular, as @cor-alternating-even-rank (d) requires for odd size.
:::

### C. Going deeper

::: {#exr-symplectic-forms-c1}
[C1: Lagrangian subspaces]

Let \( \beta \) be a symplectic form on \( V \) with \( \dim V = 2m \) (@def-darboux-basis), and call a subspace \( U \subseteq V \) **totally isotropic** if \( \beta(\u, \u') = 0 \) for all \( \u, \u' \in U \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \Span(\u_1, \dots, \u_m) \) is totally isotropic, for any symplectic basis.
2. Prove that every totally isotropic subspace satisfies \( \dim U \le m \).
3. Deduce that a symplectic form on a space of dimension \( 2m \) has a totally isotropic subspace of dimension exactly \( m \), and no larger one. (These are the **Lagrangian** subspaces.)
:::

*Hint for (b): compare \( U \) with \( U^{\perp_\beta} \) of @exr-bilinear-forms-c2.*
:::

::: {.solution}
(a) By @thm-symplectic-standard-form, \( \beta(\u_i, \u_j) = 0 \) for all \( i, j \). A general pair of elements of the span is \( \sum_i c_i\u_i \) and \( \sum_j d_j\u_j \), and bilinearity gives \( \sum_{i,j} c_id_j\beta(\u_i,\u_j) = 0 \).

(b) Let \( U \) be totally isotropic. By definition \( \beta(\u, \v) = 0 \) for all \( \u \in U \) and all \( \v \in U \), so \( U \subseteq U^{\perp_\beta} \). Since \( \beta \) is non-degenerate, \( \dim U^{\perp_\beta} = 2m - \dim U \) by @exr-bilinear-forms-c2 (b). Therefore
\[
\dim U \le 2m - \dim U ,
\]
that is \( 2\dim U \le 2m \). Both sides are integers, so \( \dim U \le m \). (No division by \( 2 \) inside the field occurs here: the inequality is between integers, not field elements, so the argument is valid in every characteristic.)

(c) The subspace of (a) has dimension \( m \), since the \( \u_i \) are part of a basis, and it is totally isotropic; by (b) no totally isotropic subspace has dimension greater than \( m \).
:::

::: {#exr-symplectic-forms-c2}
[C2: The inverse of an alternating matrix]

Let \( F \) be any field.

::: {.enumerate options="label=(\alph*)"}
1. Prove that every alternating matrix of **odd** size over \( F \) is singular, without using determinants.
2. Let \( \A \in M_n(F) \) be alternating and invertible. Prove that \( \A^{-1} \) is alternating.
:::

*Hint for (b): the adjugate. The \( (i,i) \) entry of \( \adj\A \) is a minor of \( \A \) of size \( n - 1 \).*
:::

::: {.solution}
(a) This is @cor-alternating-even-rank (d): by @thm-symplectic-standard-form the rank is even, and an even number that is at most an odd \( n \) is at most \( n - 1 \), so the matrix is not invertible. The proof of the standard form uses no determinants.

(b) Since \( \A \) is invertible, @thm-adjugate-identity gives \( \A^{-1} = (\det\A)^{-1}\adj\A \). First, skewness: \( (\A^{-1})\tp = (\A\tp)^{-1} = (-\A)^{-1} = -\A^{-1} \), using @thm-transpose-properties and the fact that inversion turns \( -\A = (-1)\A \) into \( (-1)^{-1}\A^{-1} = -\A^{-1} \).

Now the diagonal. By @def-adjugate the \( (i,i) \) entry of \( \adj\A \) is the cofactor \( C_{ii} = (-1)^{2i}M_{ii} = M_{ii} \), the determinant of the matrix obtained from \( \A \) by deleting row \( i \) and column \( i \). Deleting a row and the matching column of an alternating matrix leaves an alternating matrix, since the surviving entries keep their positions relative to the diagonal. Its size is \( n - 1 \), and \( n \) is even by @cor-alternating-even-rank (a) applied to the invertible \( \A \); so \( n - 1 \) is odd and \( M_{ii} = 0 \) by (a). Hence every diagonal entry of \( \A^{-1} \) is \( 0 \), and with skewness this makes \( \A^{-1} \) alternating.
:::

::: {#exr-symplectic-forms-c3}
[C3: Counting over a finite field]

Let \( q \) be a power of an **odd** prime.

::: {.enumerate options="label=(\alph*)"}
1. How many alternating bilinear forms are there on \( \nF_q^{2m} \)? How many symmetric ones?
2. How many of the alternating forms on \( \nF_q^{2} \) are non-degenerate, and how many congruence classes do they fall into?
3. How many of the symmetric forms on \( \nF_q^{1} \) are non-degenerate, and how many congruence classes do they fall into? *Hint: the squaring map \( \nF_q^{\times} \to \nF_q^{\times} \) has kernel \( \{1, -1\} \).*
4. Explain in one or two sentences why the answers to (b) and (c) differ, in terms of what a change of basis can do to the single free parameter in each case.
:::
:::

::: {.solution}
(a) By @thm-form-matrix-determines (c), forms correspond bijectively to matrices, so we count matrices. An alternating matrix of size \( n = 2m \) is determined freely by its entries above the diagonal, of which there are \( \binom{n}{2} = m(2m-1) \); so there are \( q^{m(2m-1)} \) alternating forms. A symmetric matrix is determined freely by its entries on and above the diagonal, \( \binom{n}{2} + n = m(2m+1) \) of them, giving \( q^{m(2m+1)} \).

(b) The alternating forms on \( \nF_q^2 \) have matrices \( \begin{psmallmatrix} 0 & a \\ -a & 0\end{psmallmatrix} \), so there are \( q \) of them, and the non-degenerate ones are those with \( a \ne 0 \), of which there are \( q - 1 \). By @cor-alternating-even-rank (b) all of these have rank \( 2 \) and so lie in a **single** congruence class.

(c) A symmetric form on \( \nF_q^{1} \) has matrix \( [d] \) and is non-degenerate exactly when \( d \ne 0 \), so there are \( q - 1 \) of them. Congruence in size \( 1 \) replaces \( d \) by \( p^2 d \) with \( p \ne 0 \) (@def-congruent), so the classes are the cosets of the subgroup of squares in \( \nF_q^{\times} \). The squaring homomorphism \( \nF_q^{\times} \to \nF_q^{\times} \) has kernel \( \{x : x^2 = 1\} = \{1, -1\} \), which has **two** elements because \( q \) is odd; so its image has index \( 2 \), and there are exactly **two** congruence classes. For \( q = 5 \), for instance, the squares are \( \{1, 4\} \) and the non-squares \( \{2, 3\} \), and \( [1] \not\simeq [2] \).

(d) In the alternating case a change of basis may replace \( a \) by \( ca \) for **any** \( c \ne 0 \), because the two slots of \( \beta(\u, \w) \) hold different basis vectors and only one of them need be rescaled. In the symmetric case the parameter sits in \( \beta(\v,\v) \), where both slots hold the same vector, so rescaling changes \( d \) to \( c^2d \) — by a **square** only. The square class then survives as an invariant, and over \( \nF_q \) it has two values.
:::
