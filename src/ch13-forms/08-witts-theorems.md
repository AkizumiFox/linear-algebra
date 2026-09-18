# Witt's Extension and Cancellation Theorems

The previous section left one question open. A non-degenerate space splits as hyperbolic planes plus an anisotropic remainder, and the number of planes is pinned down by the Witt index — but the remainder is a subspace chosen along the way, and different choices give different subspaces. What should be true is that they all carry the same form. Proving it needs a theorem with a much wider reach: any isometry between two subspaces of a non-degenerate space is the restriction of an isometry of the whole space. That theorem is the longest proof of the chapter, and the cancellation statement that finishes Section 7 falls out of it in four lines.

Throughout, \( F \) is a field with \( \operatorname{char} F \ne 2 \) (@def-characteristic), all spaces are finite-dimensional over \( F \), and all forms are **symmetric** bilinear forms (@def-symmetric-form). Orthogonal complements \( U^{\perp_\beta} \), orthogonal direct sums \( U \perp W \), and isotropic and hyperbolic vocabulary are as in Section 7.

## Isometries of forms

Chapter 10 called a linear map an isometry when it preserved the inner product (@def-isometry). The same word works here, with the form in place of the inner product and with no positivity anywhere.

*An isometry is a change of variables that the form does not notice.*

::: {#def-form-isometry}
[Isometry of Bilinear Spaces]

Let \( \beta \) be a bilinear form on \( V \) and \( \beta' \) one on \( V' \). An **isometry** from \( (V,\beta) \) to \( (V',\beta') \) is a linear **bijection** \( \sigma \colon V \to V' \) with
\[
\beta'\bigl(\sigma(\u), \sigma(\v)\bigr) = \beta(\u,\v)
\qquad \text{for all } \u, \v \in V .
\]
The two spaces are **isometric**, written \( (V,\beta) \cong (V',\beta') \) or just \( V \cong V' \), if such a \( \sigma \) exists. An isometry of \( (V,\beta) \) with itself is an **isometry of \( V \)**.

When \( U \subseteq V \) and \( U' \subseteq V' \) are subspaces, "an isometry \( U \to U' \)" always means an isometry for the **restricted** forms \( \beta|_{U\times U} \) and \( \beta'|_{U'\times U'} \).
:::

Two clauses need pointing at. The map must be a **bijection**, so that the inverse is again an isometry; and the identity must hold for **all** pairs, though by bilinearity it is enough to check it on a pair of bases. The symbol \( \cong \) is the one used for isomorphism throughout the book, and no confusion arises: an isometry is an isomorphism that also respects the form, and within this chapter \( \cong \) between spaces carrying forms always means isometric.

Three readings make the notion concrete.

- **Isometry is congruence in disguise.** If \( \sB \) is a basis of \( V \) and \( \sB' \) one of \( V' \), then \( \sigma \) is an isometry exactly when the Gram matrices satisfy \( \mtx{\beta}{\sB}{} = \P\tp\,\mtx{\beta'}{\sB'}{}\,\P \) with \( \P = \mtx{\sigma}{\sB}{\sB'} \). So \( (V,\beta) \cong (V',\beta') \) if and only if their Gram matrices are congruent (@def-congruent). Every classification theorem of this chapter is therefore a classification up to isometry.
- **Over \( \nR \).** Two real spaces with non-degenerate symmetric forms are isometric exactly when they have the same signature, by @cor-real-symmetric-classification. So, writing \( \nR^{p,q} \) for \( \nR^{p+q} \) carrying the form of signature \( (p,q) \), we have \( \nR^{2,1} \not\cong \nR^{1,2} \) even though both are three-dimensional and both non-degenerate.
- **The degenerate case.** An isometry carries \( \operatorname{rad}(\beta) \) onto \( \operatorname{rad}(\beta') \), because \( \beta'(\sigma\u, \sigma\v) = \beta(\u,\v) \) and \( \sigma \) is onto. In particular isometric spaces have radicals of equal dimension.

The isometries of a fixed \( (V,\beta) \) form a group under composition; Section 10 names the classical examples. For now only two kinds are needed, and the second is built from the first.

## Reflections

Chapter 10 §08 built Householder reflections out of an inner product, to clear a column. The same formula works for any symmetric form, provided the vector we reflect in is anisotropic, and it is the only explicit isometry this section needs.

::: {#def-form-reflection}
[Reflection in an Anisotropic Vector]

Let \( \beta \) be a symmetric bilinear form on \( V \) and let \( \w \in V \) be anisotropic, that is \( q(\w) \ne 0 \). The **reflection in \( \w \)** is the map
\[
\tau_{\w} \colon V \to V, \qquad
\tau_{\w}(\v) = \v - \frac{2\beta(\v,\w)}{q(\w)}\,\w .
\]
:::

The formula is @def-householder-reflection with \( \inner{\v}{\w} \) replaced by \( \beta(\v,\w) \) and \( \norm{\w}^2 \) by \( q(\w) \); the division is legitimate precisely because \( \w \) is anisotropic.

::: {#prp-form-reflection-properties}
[Reflections Are Involutive Isometries]

Let \( \beta \) be a symmetric bilinear form on \( V \) and \( \w \in V \) anisotropic. Then \( \tau_{\w} \) is linear, and:

::: {.enumerate options="label=(\alph*)"}
1. \( \tau_{\w}(\w) = -\w \), and \( \tau_{\w}(\v) = \v \) for every \( \v \) with \( \beta(\v,\w) = 0 \);
2. \( \tau_{\w} \circ \tau_{\w} = \id_V \); in particular \( \tau_{\w} \) is bijective;
3. \( \beta(\tau_{\w}\u, \tau_{\w}\v) = \beta(\u,\v) \) for all \( \u, \v \in V \).

:::
Hence \( \tau_{\w} \) is an isometry of \( V \).
:::

::: {.proof}
Linearity holds because \( \v \mapsto \beta(\v,\w) \) is linear and \( q(\w) \) is a fixed non-zero scalar. Write \( c(\v) = 2\beta(\v,\w)/q(\w) \).

(a) \( c(\w) = 2q(\w)/q(\w) = 2 \), so \( \tau_{\w}(\w) = \w - 2\w = -\w \). If \( \beta(\v,\w) = 0 \) then \( c(\v) = 0 \) and \( \tau_{\w}(\v) = \v \).

(b) By (a) and linearity, \( \beta(\tau_{\w}\v, \w) = \beta(\v,\w) - c(\v)q(\w) = -\beta(\v,\w) \), so \( c(\tau_{\w}\v) = -c(\v) \) and
\[
\tau_{\w}(\tau_{\w}\v) = \bigl(\v - c(\v)\w\bigr) + c(\v)\w = \v .
\]

(c) Expanding by bilinearity and using symmetry,
\[
\begin{aligned}
\beta(\tau_{\w}\u,\tau_{\w}\v)
&= \beta(\u,\v) - c(\v)\beta(\u,\w) - c(\u)\beta(\w,\v) \\
&\qquad + c(\u)c(\v)q(\w) .
\end{aligned}
\]
Now \( c(\u)c(\v)q(\w) = 4\beta(\u,\w)\beta(\v,\w)/q(\w) \), while the two middle terms together contribute \( -4\beta(\u,\w)\beta(\v,\w)/q(\w) \). They cancel, leaving \( \beta(\u,\v) \). Together with (b) this makes \( \tau_{\w} \) a bijective linear map preserving \( \beta \), that is an isometry.
:::

The use of reflections is that they move one anisotropic vector to any other of the same value — the one explicit construction the long proof below will need.

::: {#lem-reflection-moves-anisotropic}
[Moving One Anisotropic Vector to Another]

Let \( \operatorname{char} F \ne 2 \), let \( \beta \) be a symmetric bilinear form on \( V \), and let \( \u, \u' \in V \) satisfy
\[
q(\u) = q(\u') \ne 0 .
\]
Then there is an isometry \( \rho \) of \( V \) with \( \rho(\u) = \u' \), and \( \rho \) may be taken to be a reflection or a product of two reflections.
:::

::: {.idea}
The reflection in \( \u - \u' \) is the natural candidate, and it works whenever \( \u - \u' \) is anisotropic. It need not be — but \( \u + \u' \) then is, because the two values \( q(\u-\u') \) and \( q(\u+\u') \) add up to \( 4q(\u) \ne 0 \) and so cannot both vanish. Reflecting in \( \u + \u' \) overshoots to \( -\u' \), and one more reflection, in \( \u' \) itself, brings it back.
:::

::: {.proof}
Expanding both by bilinearity and adding,
\[
q(\u-\u') + q(\u+\u') = 2q(\u) + 2q(\u') = 4q(\u) \ne 0 ,
\]
where the last step uses \( q(\u) = q(\u') \ne 0 \). So at least one of \( q(\u-\u') \) and \( q(\u+\u') \) is non-zero.

*Case 1: \( q(\u - \u') \ne 0 \).* Put \( \w = \u - \u' \). Then
\[
q(\w) = q(\u) - 2\beta(\u,\u') + q(\u') = 2\bigl(q(\u) - \beta(\u,\u')\bigr),
\]
while \( \beta(\u,\w) = q(\u) - \beta(\u,\u') \). Hence \( 2\beta(\u,\w)/q(\w) = 1 \), and
\[
\tau_{\w}(\u) = \u - \w = \u' .
\]
Take \( \rho = \tau_{\w} \).

*Case 2: \( q(\u-\u') = 0 \).* Then \( q(\u+\u') = 4q(\u) \ne 0 \); put \( \w = \u + \u' \). The same computation with \( -\u' \) in place of \( \u' \) gives \( q(\w) = 2(q(\u) + \beta(\u,\u')) \) and \( \beta(\u,\w) = q(\u) + \beta(\u,\u') \), so again \( 2\beta(\u,\w)/q(\w) = 1 \) and
\[
\tau_{\w}(\u) = \u - \w = -\u' .
\]
Since \( q(\u') \ne 0 \), the reflection \( \tau_{\u'} \) is defined, and \( \tau_{\u'}(-\u') = \u' \) by @prp-form-reflection-properties (a). Take \( \rho = \tau_{\u'}\circ\tau_{\w} \), a composition of two isometries and hence an isometry. This proves the lemma.
:::

::: {.check}
In \( \nR^3 \) with \( q(\x) = x_1^2 + x_2^2 - x_3^2 \), find a reflection carrying \( \e_1 \) to \( \e_2 \).
:::

::: {.solution}
Both have \( q = 1 \ne 0 \), so @lem-reflection-moves-anisotropic applies. Case 1 works: \( \w = \e_1 - \e_2 \) has \( q(\w) = 1 + 1 = 2 \ne 0 \), so
\[
\tau_{\w}(\v) = \v - \beta(\v,\w)\,\w,
\]
since \( 2/q(\w) = 1 \). Then \( \beta(\e_1,\w) = 1 \) and \( \tau_{\w}(\e_1) = \e_1 - (\e_1 - \e_2) = \e_2 \), as required. The reflection fixes \( \e_1 + \e_2 \) and \( \e_3 \), which are the vectors orthogonal to \( \w \).
:::

## Witt's extension theorem

Here is the chapter's long theorem. Read the statement carefully: the two subspaces live in the **same** space \( V \), and the form on \( V \) is required to be non-degenerate, but nothing at all is assumed about the restrictions to \( U \) and \( U' \) — they may be degenerate, they may be zero.

::: {#thm-witt-extension}
[Witt's Extension Theorem]

Let \( F \) be a field with \( \operatorname{char} F \ne 2 \), let \( V \) be a finite-dimensional vector space over \( F \), and let \( \beta \) be a **non-degenerate** symmetric bilinear form on \( V \). Let \( U, U' \subseteq V \) be subspaces and let
\[
\sigma \colon U \to U'
\]
be an isometry for the restricted forms. Then there is an isometry \( \varphi \) of \( V \) with \( \varphi|_U = \sigma \).
:::

::: {.idea}
Induction, but on what? Two different moves are available, and each improves a different number.

① If \( \beta|_U \) is **non-degenerate**, then \( U \) contains an anisotropic vector \( \u_1 \). A reflection moves \( \sigma(\u_1) \) back to \( \u_1 \), so we may assume \( \sigma \) fixes \( \u_1 \); then everything of \( U \) orthogonal to \( \u_1 \) stays inside the hyperplane \( \u_1^{\perp} \), which is again non-degenerate and **one dimension smaller**. Recurse there and glue.

② If \( \beta|_U \) is **degenerate**, pick a non-zero \( \z \) in its radical. Non-degeneracy of \( \beta \) on \( V \) produces a partner \( \w \) making \( (\z,\w) \) a hyperbolic pair orthogonal to the rest of \( U \), and \( \sigma \) extends to \( U \oplus F\w \) by sending \( \w \) to the matching partner on the other side. The subspace has grown, but its **radical has shrunk by one**.

So the induction runs on the pair \( (\dim V,\ \dim\operatorname{rad}(\beta|_U)) \) read lexicographically: ① lowers the first entry, ② keeps it and lowers the second. Step 0 disposes of \( U = \{\0\} \).
:::

::: {.proof}
We prove the statement for every triple \( (V, U, \sigma) \) satisfying the hypotheses, by induction on the pair
\[
\bigl(\dim V,\ \dim\operatorname{rad}(\beta|_{U\times U})\bigr)
\]
ordered lexicographically: one pair precedes another if its first entry is smaller, or the first entries agree and the second is smaller. This order on pairs of non-negative integers has no infinite descending chain, so the induction is legitimate. Write \( R = \operatorname{rad}(\beta|_{U\times U}) = U \cap U^{\perp_\beta} \).

**Step 0: \( U = \{\0\} \).** Then \( U' = \{\0\} \) and \( \varphi = \id_V \) works.

**Step 1: \( U \ne \{\0\} \) and \( R = \{\0\} \).** Since \( \beta|_U \) is non-degenerate and \( U \ne \{\0\} \), the form \( \beta|_U \) is not the zero form. By @lem-anisotropic-vector-exists, applied to \( \beta|_U \) on \( U \) and using \( \operatorname{char} F \ne 2 \), there is \( \u_1 \in U \) with \( q(\u_1) \ne 0 \).

::: {.claim}
We may assume \( \sigma(\u_1) = \u_1 \).
:::

::: {.proof}
Put \( \u_1' = \sigma(\u_1) \). Then \( q(\u_1') = \beta(\sigma\u_1,\sigma\u_1) = q(\u_1) \ne 0 \), so @lem-reflection-moves-anisotropic gives an isometry \( \rho \) of \( V \) with \( \rho(\u_1) = \u_1' \). The composite \( \tau = \rho^{-1}\circ\sigma \) is an isometry from \( U \) onto \( \rho^{-1}(U') \) with \( \tau(\u_1) = \u_1 \), and if \( \varphi_0 \) is an isometry of \( V \) extending \( \tau \), then \( \rho\circ\varphi_0 \) is an isometry of \( V \) extending \( \sigma \). So it suffices to treat \( \tau \).
:::

Assume then that \( \sigma(\u_1) = \u_1 \). The map \( \u \mapsto \beta(\u_1,\u) \) is a linear functional on \( U \) taking the non-zero value \( q(\u_1) \) at \( \u_1 \), so its kernel
\[
U_1 = \{\, \u \in U : \beta(\u_1,\u) = 0 \,\}
\]
has \( \dim U_1 = \dim U - 1 \) by Rank–Nullity (@thm-rank-nullity), and \( U = \Span(\u_1) \oplus U_1 \), since \( a\u_1 \in U_1 \) forces \( a\,q(\u_1) = 0 \) and hence \( a = 0 \).

Because \( q(\u_1) \ne 0 \), the form restricted to \( \Span(\u_1) \) is non-degenerate, so @prp-nondegenerate-restriction-splits gives
\[
V = \Span(\u_1) \perp W, \qquad W = \Span(\u_1)^{\perp_\beta},
\]
with \( \beta|_W \) non-degenerate and \( \dim W = \dim V - 1 \). Now \( U_1 \subseteq W \) by definition, and \( \sigma(U_1) \subseteq W \) as well: for \( \u \in U_1 \),
\[
\beta(\u_1, \sigma\u) = \beta(\sigma\u_1, \sigma\u) = \beta(\u_1,\u) = 0 .
\]
So \( \sigma|_{U_1} \colon U_1 \to \sigma(U_1) \) is an isometry between two subspaces of \( W \), and \( (W, \beta|_W) \) satisfies the hypotheses of the theorem with \( \dim W < \dim V \). By the induction hypothesis there is an isometry \( \theta \) of \( W \) with \( \theta|_{U_1} = \sigma|_{U_1} \).

Define \( \varphi \colon V \to V \) by
\[
\varphi(a\u_1 + \x) = a\u_1 + \theta(\x)
\qquad (a \in F,\ \x \in W),
\]
which is well defined and linear because \( V = \Span(\u_1)\oplus W \), and bijective because \( \theta \) is. It is an isometry: using the orthogonality of \( \Span(\u_1) \) and \( W \) on both sides,
\[
\begin{aligned}
\beta\bigl(\varphi(a\u_1+\x), \varphi(b\u_1+\y)\bigr)
&= ab\,q(\u_1) + \beta(\theta\x,\theta\y) \\
&= ab\,q(\u_1) + \beta(\x,\y) \\
&= \beta(a\u_1+\x,\ b\u_1+\y) .
\end{aligned}
\]
Finally \( \varphi \) extends \( \sigma \): a vector \( \u \in U \) is \( a\u_1 + \x \) with \( \x \in U_1 \subseteq W \), and
\[
\varphi(\u) = a\u_1 + \theta(\x) = a\sigma(\u_1) + \sigma(\x) = \sigma(\u) .
\]

**Step 2: \( R \ne \{\0\} \).** Choose \( \z \in R \) with \( \z \ne \0 \) and a complement \( U_0 \) of \( \Span(\z) \) in \( U \), so that \( U = \Span(\z) \oplus U_0 \) (@thm-complement-exists). Since \( \sigma \) is an isometry of \( U \) onto \( U' \), it carries \( R \) onto \( \operatorname{rad}(\beta|_{U'}) \); write \( \z' = \sigma(\z) \) and \( U_0' = \sigma(U_0) \), so that \( U' = \Span(\z')\oplus U_0' \) and \( \z' \) lies in the radical of \( \beta|_{U'} \). Note \( q(\z) = 0 \), because \( \z \) pairs to zero with everything in \( U \), in particular with itself; likewise \( q(\z') = 0 \).

::: {.claim}
There is \( \w \in V \) with \( q(\w) = 0 \), \( \beta(\z,\w) = 1 \) and \( \beta(\u_0,\w) = 0 \) for every \( \u_0 \in U_0 \).
:::

::: {.proof}
Consider the linear map \( S \colon V \to U^{*} \) sending \( \v \) to the restriction of \( \beta(\cdot,\v) \) to \( U \). Its kernel is \( U^{\perp_\beta} \), which has dimension \( \dim V - \dim U \) by @exr-bilinear-forms-c2 (b), since \( \beta \) is non-degenerate. By Rank–Nullity (@thm-rank-nullity), \( \rank S = \dim U = \dim U^{*} \), so \( S \) is onto. Let \( \psi_{\z} \in U^{*} \) be the functional with \( \psi_{\z}(\z) = 1 \) and \( \psi_{\z}(U_0) = 0 \), which exists because \( U = \Span(\z)\oplus U_0 \). Pick \( \w_0 \in V \) with \( S(\w_0) = \psi_{\z} \), that is \( \beta(\z,\w_0) = 1 \) and \( \beta(\u_0,\w_0) = 0 \) for \( \u_0 \in U_0 \).

Put \( \w = \w_0 - \tfrac12 q(\w_0)\,\z \), which uses \( \operatorname{char} F \ne 2 \). Since \( q(\z) = 0 \) and \( \beta(\u,\z) = 0 \) for every \( \u \in U \),
\[
\beta(\z,\w) = 1 - \tfrac12q(\w_0)q(\z) = 1, \qquad
\beta(\u_0,\w) = 0 ,
\]
and
\[
q(\w) = q(\w_0) - q(\w_0)\beta(\w_0,\z) + \tfrac14q(\w_0)^2q(\z) = 0 ,
\]
using \( \beta(\w_0,\z) = \beta(\z,\w_0) = 1 \).
:::

Apply the claim on both sides: it gives \( \w \) for \( (\z, U_0) \) and, by the same argument with \( \z' \) and \( U_0' \), a vector \( \w' \) with \( q(\w') = 0 \), \( \beta(\z',\w') = 1 \) and \( \beta(U_0',\w') = 0 \).

The vector \( \w \) is not in \( U \), since \( \beta(\z,\w) = 1 \) while \( \beta(\z,\u) = 0 \) for every \( \u \in U \); likewise \( \w' \notin U' \). So
\[
\widetilde U = U \oplus F\w, \qquad \widetilde U' = U' \oplus F\w'
\]
are subspaces of \( V \) of dimension \( \dim U + 1 \). Define \( \widetilde\sigma(\u + c\w) = \sigma(\u) + c\w' \), a linear bijection \( \widetilde U \to \widetilde U' \). It is an isometry: for \( \u = a\z + \u_0 \in U \) we have
\[
\beta(\u,\w) = a\beta(\z,\w) + \beta(\u_0,\w) = a ,
\]
and \( \sigma(\u) = a\z' + \sigma(\u_0) \) with \( \sigma(\u_0) \in U_0' \), so \( \beta(\sigma\u, \w') = a \) as well. Hence, expanding by bilinearity and using \( q(\w) = q(\w') = 0 \),
\[
\begin{aligned}
\beta\bigl(\widetilde\sigma(\u + c\w),\, \widetilde\sigma(\y + d\w)\bigr)
&= \beta(\sigma\u,\sigma\y) + d\,\beta(\sigma\u,\w') + c\,\beta(\sigma\y,\w') \\
&= \beta(\u,\y) + d\,\beta(\u,\w) + c\,\beta(\y,\w) \\
&= \beta(\u + c\w,\ \y + d\w) .
\end{aligned}
\]

::: {.claim}
\( \operatorname{rad}(\beta|_{\widetilde U}) = R \cap U_0 \), and its dimension is \( \dim R - 1 \).
:::

::: {.proof}
Let \( \x = a\z + \u_0 + c\w \) lie in \( \operatorname{rad}(\beta|_{\widetilde U}) \), with \( a, c \in F \) and \( \u_0 \in U_0 \). Pairing \( \x \) with \( \w \) gives \( a\beta(\z,\w) + \beta(\u_0,\w) + c\,q(\w) = a \), so \( a = 0 \). Pairing \( \x \) with \( \z \) gives \( \beta(\u_0,\z) + c\,\beta(\w,\z) = c \), since \( \z \in R \) kills \( \u_0 \); so \( c = 0 \). Hence \( \x = \u_0 \in U_0 \), and \( \x \) pairs to zero with all of \( U \subseteq \widetilde U \), so \( \x \in R\cap U_0 \). Conversely a vector of \( R \cap U_0 \) pairs to zero with \( U \) and with \( \w \), hence with \( \widetilde U \).

For the dimension: every \( \r \in R \subseteq U \) is \( a\z + \u_0 \), and \( \u_0 = \r - a\z \in R \) because \( \z \in R \); so \( R = \Span(\z)\oplus(R\cap U_0) \) and \( \dim(R\cap U_0) = \dim R - 1 \).
:::

The pair attached to the triple \( (V, \widetilde U, \widetilde\sigma) \) is therefore \( (\dim V, \dim R - 1) \), which precedes \( (\dim V, \dim R) \) in the lexicographic order. By the induction hypothesis there is an isometry \( \varphi \) of \( V \) with \( \varphi|_{\widetilde U} = \widetilde\sigma \). Since \( U \subseteq \widetilde U \) and \( \widetilde\sigma|_U = \sigma \), this \( \varphi \) extends \( \sigma \).

Steps 0, 1 and 2 cover every case, so the induction is complete and the theorem is proved.
:::

Three places earned their hypotheses. Non-degeneracy of \( \beta \) on \( V \) was used twice, once through @prp-nondegenerate-restriction-splits in Step 1 and once through the surjectivity of \( S \) in Step 2. Characteristic \( \ne 2 \) was used twice as well, in @lem-anisotropic-vector-exists and in the correction \( \w = \w_0 - \tfrac12 q(\w_0)\z \), which is the same correction that built a hyperbolic pair in @lem-isotropic-extends-to-hyperbolic. And symmetry is everywhere: without it, "the" radical and "the" orthogonal complement would each split into a left and a right version.

## Cancellation

The corollary is what the theorem is usually used for, and it is where a careless statement goes wrong. Witt cancellation removes a summand from an **orthogonal** decomposition of two spaces that are **already known to be isometric**, and what it produces is an isometry of the complements.

::: {#cor-witt-cancellation}
[Witt's Cancellation Theorem]

Let \( \operatorname{char} F \ne 2 \).

::: {.enumerate options="label=(\alph*)"}
1. Let \( \beta \) be a non-degenerate symmetric form on \( V \), and let \( U, U' \subseteq V \) be isometric subspaces. Then \( U^{\perp_\beta} \cong U'^{\perp_\beta} \).
2. Let \( (V,\beta) \) and \( (V',\beta') \) be finite-dimensional spaces with non-degenerate symmetric forms, and suppose
\[
V = U \perp W, \qquad V' = U' \perp W' .
\]
If \( V \cong V' \) and \( U \cong U' \), then \( W \cong W' \).
:::
:::

::: {.idea}
For (a), extend the isometry \( U \to U' \) to the whole of \( V \) and watch where the complement goes: an isometry of \( V \) carrying \( U \) onto \( U' \) has no choice but to carry \( U^{\perp} \) onto \( U'^{\perp} \). For (b), transport everything into the single space \( V \) along an isometry \( V \to V' \), and apply (a).
:::

::: {.proof}
(a) Let \( \sigma \colon U \to U' \) be an isometry. By @thm-witt-extension there is an isometry \( \varphi \) of \( V \) with \( \varphi|_U = \sigma \); in particular \( \varphi(U) = U' \). If \( \x \in U^{\perp_\beta} \) and \( \u' \in U' \), write \( \u' = \varphi(\u) \) with \( \u \in U \); then
\[
\beta(\u', \varphi\x) = \beta(\varphi\u, \varphi\x) = \beta(\u,\x) = 0 ,
\]
so \( \varphi(U^{\perp_\beta}) \subseteq U'^{\perp_\beta} \). Both subspaces have dimension \( \dim V - \dim U \) by @exr-bilinear-forms-c2 (b), using \( \dim U = \dim U' \), and \( \varphi \) is injective, so the inclusion is an equality. Restricting \( \varphi \) gives an isometry \( U^{\perp_\beta} \to U'^{\perp_\beta} \).

(b) First, \( W = U^{\perp_\beta} \): the orthogonality in \( V = U \perp W \) gives \( W \subseteq U^{\perp_\beta} \), and both have dimension \( \dim V - \dim U \), so they are equal (@thm-dim-impl-eq). Likewise \( W' = U'^{\perp_{\beta'}} \).

Let \( \psi \colon V \to V' \) be an isometry. Then \( \psi^{-1}(U') \) is a subspace of \( V \) isometric to \( U' \), hence isometric to \( U \). Moreover \( \psi^{-1}\bigl(U'^{\perp_{\beta'}}\bigr) = \bigl(\psi^{-1}(U')\bigr)^{\perp_\beta} \), because \( \psi \) preserves the forms and is onto. Applying (a) inside \( V \) to the isometric subspaces \( U \) and \( \psi^{-1}(U') \),
\[
W = U^{\perp_\beta} \cong \bigl(\psi^{-1}(U')\bigr)^{\perp_\beta} = \psi^{-1}(W') \cong W' ,
\]
the last isometry being the restriction of \( \psi \). This proves the corollary.
:::

::: {.warning}
**Cancellation needs the whole spaces to be isometric, and the sums to be orthogonal.** Neither hypothesis can be dropped.

Drop the first: inside \( \nR^2 \) with \( q = x_1^2 + x_2^2 \) and inside \( \nR^2 \) with \( q' = x_1^2 - x_2^2 \), the lines \( \Span(\e_1) \) are isometric, each carrying the form \( \langle 1\rangle \). Their complements are \( \Span(\e_2) \) with \( q = x_2^2 \) and \( \Span(\e_2) \) with \( q' = -x_2^2 \), which are **not** isometric: one is positive definite, the other negative definite. Isometric subspaces of **different** ambient spaces say nothing about complements.

Drop the second: in \( \nR^2 \) with \( q = x_1^2 - x_2^2 \), both
\[
V = \Span(\e_1) \oplus \Span(\e_1 + \e_2)
\quad\text{and}\quad
V = \Span(\e_1) \oplus \Span(\e_2)
\]
are direct sums with the same first summand. The second summands carry \( q(\e_1+\e_2) = 0 \) and \( q(\e_2) = -1 \), so they are not isometric. The first decomposition is not orthogonal, since \( \beta(\e_1, \e_1+\e_2) = 1 \ne 0 \), and that is exactly what breaks.
:::

## The Witt decomposition is unique

We can now close the question Section 7 left open.

::: {#cor-witt-decomposition-unique}
[The Anisotropic Part Is Determined]

Let \( \operatorname{char} F \ne 2 \), let \( \beta \) be a non-degenerate symmetric form on a finite-dimensional \( V \), and let
\[
V = H_1 \perp \dots \perp H_m \perp V_0
= H_1' \perp \dots \perp H_{m'}' \perp V_0'
\]
be two decompositions as in @thm-witt-decomposition. Then \( m = m' = \operatorname{ind}(\beta) \) and \( V_0 \cong V_0' \).
:::

::: {.proof}
That \( m = m' = \operatorname{ind}(\beta) \) is @prp-witt-index-counts-planes. Put \( U = H_1\perp\dots\perp H_m \) and \( U' = H_1'\perp\dots\perp H_m' \). Choosing a hyperbolic basis of each plane gives bases of \( U \) and of \( U' \) in which both Gram matrices are the same block diagonal matrix, namely \( m \) copies of \( \begin{psmallmatrix} 0&1\\1&0\end{psmallmatrix} \) down the diagonal. The linear bijection \( U \to U' \) matching these bases in order is therefore an isometry.

Both \( V_0 \) and \( V_0' \) are complements: \( V_0 \subseteq U^{\perp_\beta} \) by orthogonality, and the dimensions agree, so \( V_0 = U^{\perp_\beta} \) (@thm-dim-impl-eq), and likewise \( V_0' = U'^{\perp_\beta} \). By @cor-witt-cancellation (a), \( V_0 \cong V_0' \). This proves the corollary.
:::

So a non-degenerate symmetric form is completely described by two pieces of data: an integer, the Witt index, and an anisotropic form, determined up to isometry. Classifying all forms over a field \( F \) therefore reduces to classifying the **anisotropic** ones, which is where the arithmetic of \( F \) enters and where the subject stops being linear algebra. Over \( \nR \) the anisotropic forms are the definite ones, so the data \( (\operatorname{ind}, V_0) \) is just the signature again. Over \( \nC \) the anisotropic forms have dimension \( 0 \) or \( 1 \), so the index and the parity of \( n \) are everything. Over \( \nQ \) the classification is a theorem of number theory and is not in this book.

## Exercises

### A. Check your understanding

::: {#exr-witts-theorems-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State Witt's extension theorem, with all its hypotheses.
2. Define the reflection \( \tau_{\w} \) and say which vectors it fixes.
3. Determine whether the following statement is correct, and justify your answer: if \( U \subseteq V \) and \( U' \subseteq V' \) are isometric subspaces of non-degenerate spaces, then \( U^{\perp} \) and \( U'^{\perp} \) are isometric.
4. Where is \( \operatorname{char} F \ne 2 \) used in the proof of @thm-witt-extension?
5. Two real non-degenerate forms of dimension \( 6 \) both have Witt index \( 2 \). Must they be isometric?
:::
:::

::: {.solution}
(a) Let \( \operatorname{char} F \ne 2 \), let \( \beta \) be a non-degenerate symmetric bilinear form on a finite-dimensional \( V \) over \( F \), let \( U, U' \subseteq V \) be subspaces and \( \sigma \colon U \to U' \) an isometry for the restricted forms. Then \( \sigma \) extends to an isometry of \( V \).

(b) \( \tau_{\w}(\v) = \v - \bigl(2\beta(\v,\w)/q(\w)\bigr)\w \), defined for anisotropic \( \w \). It fixes every \( \v \) with \( \beta(\v,\w) = 0 \) and sends \( \w \) to \( -\w \).

(c) Incorrect. The warning after @cor-witt-cancellation gives the witness: the line \( \Span(\e_1) \) inside \( (\nR^2, x_1^2+x_2^2) \) and inside \( (\nR^2, x_1^2-x_2^2) \) are isometric, with complements of opposite definiteness. Cancellation requires the ambient spaces to be isometric too.

(d) Twice. In Step 1, through @lem-anisotropic-vector-exists, which produces an anisotropic vector in a non-zero subspace where the form is not zero. In Step 2, through the correction \( \w = \w_0 - \tfrac12q(\w_0)\z \), which divides by \( 2 \).

(e) No. By @cor-witt-decomposition-unique each is two hyperbolic planes orthogonal to an anisotropic part of dimension \( 6 - 4 = 2 \), and over \( \nR \) an anisotropic form is definite, so that part has signature \( (2,0) \) or \( (0,2) \). The two possibilities give signatures \( (4,2) \) and \( (2,4) \) for the whole space, which are different, so the forms need not be isometric. What @cor-witt-decomposition-unique says is that the anisotropic part is determined by the form, not that the index determines the form.
:::

### B. Practice

::: {#exr-witts-theorems-b1}
[B1: Extend an isometry by hand]

Let \( V = \nR^3 \) with \( q(\x) = x_1^2 + x_2^2 - x_3^2 \), let \( U = \Span(\e_1) \), \( U' = \Span(\e_2) \), and let \( \sigma(\e_1) = \e_2 \).

::: {.enumerate options="label=(\alph*)"}
1. Verify that \( \sigma \) is an isometry of \( U \) onto \( U' \).
2. Extend \( \sigma \) to an isometry of \( V \), and write down its matrix in the standard basis.
3. Determine \( U^{\perp_\beta} \) and \( U'^{\perp_\beta} \) and exhibit the isometry between them produced by your extension.
:::
:::

::: {.solution}
(a) \( \beta(a\e_1, b\e_1) = ab \) and \( \beta(\sigma(a\e_1),\sigma(b\e_1)) = \beta(a\e_2,b\e_2) = ab \), and \( \sigma \) is a linear bijection \( U \to U' \).

(b) Use the Quick check: \( \w = \e_1 - \e_2 \) has \( q(\w) = 2 \), and \( \tau_{\w}(\v) = \v - \beta(\v,\w)\w \) sends \( \e_1 \) to \( \e_2 \). In coordinates \( \beta(\v,\w) = v_1 - v_2 \), so
\[
\tau_{\w}(\v) = (v_2,\ v_1,\ v_3), \qquad
\P = \begin{pmatrix} 0&1&0\\ 1&0&0\\ 0&0&1\end{pmatrix}.
\]
This swaps the first two coordinates and indeed satisfies \( \P\tp\diag(1,1,-1)\P = \diag(1,1,-1) \).

(c) \( U^{\perp_\beta} = \{\v : v_1 = 0\} = \Span(\e_2,\e_3) \) and \( U'^{\perp_\beta} = \Span(\e_1,\e_3) \). The extension maps \( \e_2 \mapsto \e_1 \) and \( \e_3\mapsto\e_3 \), an isometry between them; both carry the form \( \diag(1,-1) \), as @cor-witt-cancellation (a) predicts.
:::

::: {#exr-witts-theorems-b2}
[B2: Cancel a hyperbolic plane]

Let \( H \) denote a hyperbolic plane over \( \nR \), and let \( A \) and \( B \) be non-degenerate real spaces with forms, with \( \dim A = \dim B = 3 \). Suppose \( H \perp A \cong H \perp B \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( A \cong B \).
2. If \( A \) has signature \( (2,1) \), what is the signature of \( B \)?
3. Does \( A \perp B \cong A \perp B \) with \( A \cong A \) allow us to conclude \( B \cong B \)? Say which part of @cor-witt-cancellation is being used and why the statement is not vacuous.
:::
:::

::: {.solution}
(a) Put \( V = H \perp A \) and \( V' = H \perp B \), both non-degenerate. The two copies of \( H \) are isometric, and \( V \cong V' \) by hypothesis, so @cor-witt-cancellation (b) gives \( A \cong B \).

(b) By (a), \( B \cong A \), so \( B \) has signature \( (2,1) \) as well; isometric real spaces have equal signatures by @cor-real-symmetric-classification.

(c) It uses (b) of @cor-witt-cancellation with \( U = U' = A \) and \( W = W' = B \); the conclusion \( B \cong B \) is true but empty. The content of (b) appears only when the two decompositions are genuinely different, as in (a) above, where the hypothesis \( V \cong V' \) is an assumption about the **whole** spaces and not about \( A \) and \( B \).
:::

::: {#exr-witts-theorems-b3}
[B3: Reflections in an indefinite space]

In \( \nR^2 \) with \( q(\x) = x_1^2 - x_2^2 \):

::: {.enumerate options="label=(\alph*)"}
1. Compute the matrix of \( \tau_{\e_1} \) and of \( \tau_{\e_2} \) in the standard basis, and check each satisfies \( \P\tp\A\P = \A \) with \( \A = \diag(1,-1) \).
2. Explain why \( \tau_{\v} \) is undefined for \( \v = (1,1) \), and say what fails.
3. Find an isometry carrying \( (1,0) \) to \( (-1,0) \) and one carrying \( (2,\sqrt3) \) to \( (-2,\sqrt3) \). *(Check the values of \( q \) first.)*
:::
:::

::: {.solution}
(a) \( q(\e_1) = 1 \) and \( \beta(\v,\e_1) = v_1 \), so \( \tau_{\e_1}(\v) = \v - 2v_1\e_1 = (-v_1, v_2) \), with matrix \( \diag(-1,1) \). Similarly \( q(\e_2) = -1 \) and \( \beta(\v,\e_2) = -v_2 \), so the coefficient is \( 2(-v_2)/(-1) = 2v_2 \) and \( \tau_{\e_2}(\v) = \v - 2v_2\e_2 = (v_1,-v_2) \), with matrix \( \diag(1,-1) \). Both matrices \( \P \) are diagonal with entries \( \pm1 \), so \( \P\tp\A\P = \P\A\P = \A \), as each sign is squared.

(b) \( q(1,1) = 1 - 1 = 0 \), so \( (1,1) \) is isotropic and the denominator \( q(\w) \) in @def-form-reflection is zero. The formula divides by \( 0 \); there is no reflection in an isotropic vector.

(c) Both \( (1,0) \) and \( (-1,0) \) have \( q = 1 \ne 0 \). Here \( \u - \u' = (2,0) \) with \( q = 4 \ne 0 \), so Case 1 of @lem-reflection-moves-anisotropic applies: \( \tau_{(2,0)} = \tau_{\e_1} \) works, and indeed \( \tau_{\e_1}(1,0) = (-1,0) \). For the second pair, \( q(2,\sqrt3) = 4 - 3 = 1 = q(-2,\sqrt3) \). Now \( \u - \u' = (4,0) \), with \( q = 16 \ne 0 \), so \( \tau_{\e_1} \) again works: it negates the first coordinate and fixes the second.
:::

### C. Going deeper

::: {#exr-witts-theorems-c1}
[C1: Inertia from cancellation]

Work over \( \nR \) and let \( V \) be an \( n \)-dimensional space with a non-degenerate symmetric form.

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( \nR^{p,q} \) denotes \( \nR^{p+q} \) with the form \( x_1^2 + \dots + x_p^2 - x_{p+1}^2 - \dots - x_{p+q}^2 \), then \( \nR^{p,q} \cong \nR^{p',q'} \) forces \( p = p' \) and \( q = q' \), using only @cor-witt-cancellation and @prp-witt-index-real-complex.
2. Explain in one sentence how this compares with the proof of @thm-sylvester-inertia in Section 5.
:::
:::

::: {.solution}
(a) Suppose \( \nR^{p,q} \cong \nR^{p',q'} \). Equal dimension gives \( p + q = p' + q' = n \). By @prp-witt-index-real-complex (a) the Witt index is an isometry invariant, so \( \min(p,q) = \min(p',q') = k \). By @cor-witt-decomposition-unique each space is \( k \) hyperbolic planes orthogonal to an anisotropic part, and those anisotropic parts are isometric. The anisotropic part of \( \nR^{p,q} \) is positive definite of dimension \( p - q \) when \( p \ge q \) and negative definite of dimension \( q - p \) when \( q > p \). A positive definite form is never isometric to a negative definite one of the same dimension, since \( q > 0 \) on one and \( q < 0 \) on the other away from \( \0 \) — unless both dimensions are \( 0 \). So the two anisotropic parts have the same dimension and the same sign, giving \( p - q = p' - q' \). With \( p + q = p' + q' \) this forces \( p = p' \) and \( q = q' \).

(b) Section 5 proved this directly, by producing a positive subspace and a non-positive subspace whose dimensions are too large to intersect trivially; the route here instead invokes the whole Witt machinery, so it is longer but shows that inertia is the real instance of a statement that holds over every field of characteristic \( \ne 2 \).
:::

::: {#exr-witts-theorems-c2}
[C2: The isometry group acts transitively]

Let \( \beta \) be a non-degenerate symmetric form on \( V \), with \( \operatorname{char} F \ne 2 \), and let \( G \) be the group of isometries of \( V \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( q(\u) = q(\u') \ne 0 \) then some \( \varphi \in G \) has \( \varphi(\u) = \u' \).
2. Prove that if \( \u \) and \( \u' \) are both isotropic and non-zero, then some \( \varphi \in G \) has \( \varphi(\u) = \u' \). *Hint: an isotropic line is a one-dimensional subspace on which the form is zero.*
3. Deduce that \( G \) acts transitively on each "level set" \( \{\v \ne \0 : q(\v) = c\} \) for \( c \ne 0 \), and on the set of non-zero isotropic vectors.
:::
:::

::: {.solution}
(a) This is @lem-reflection-moves-anisotropic, which already produces such an isometry as a product of at most two reflections. Alternatively, \( \Span(\u) \to \Span(\u') \), \( \u \mapsto \u' \), is an isometry of one-dimensional subspaces because \( q(\u) = q(\u') \), so @thm-witt-extension extends it.

(b) The map \( \sigma \colon \Span(\u) \to \Span(\u') \) with \( \sigma(a\u) = a\u' \) is a linear bijection, and
\[
\beta(\sigma(a\u),\sigma(b\u)) = ab\,q(\u') = 0 = ab\,q(\u) = \beta(a\u,b\u),
\]
so it is an isometry of the restricted forms — both of which are zero. By @thm-witt-extension it extends to \( \varphi \in G \). Note the restricted forms here are **degenerate**, which is exactly the case Step 2 of the proof was built for.

(c) Immediate from (a) and (b): any two members of such a set are carried to one another by some \( \varphi \in G \). In particular, over \( \nR^{1,3} \) the isometry group moves any non-zero null vector to any other, which is the statement that the light cone has no distinguished direction.
:::

::: {#exr-witts-theorems-c3}
[C3: What extension does not say]

::: {.enumerate options="label=(\alph*)"}
1. Give an example of a non-degenerate \( (V,\beta) \) and subspaces \( U, U' \) of the **same dimension** that are not isometric, and say why @thm-witt-extension does not apply.
2. Let \( \beta \) be non-degenerate on \( V \) and let \( U \subseteq V \) be totally isotropic with \( \dim U = \operatorname{ind}(\beta) \). Prove that any two such \( U \) are carried onto one another by an isometry of \( V \).
3. Deduce that all maximal totally isotropic subspaces of a non-degenerate space have the same dimension, and compare with @prp-totally-isotropic-bound.
:::
:::

::: {.solution}
(a) Take \( V = \nR^2 \) with \( q = x_1^2 - x_2^2 \), \( U = \Span(\e_1) \) and \( U' = \Span(\e_2) \). Both are lines, but \( q \) is positive on \( U\setminus\{\0\} \) and negative on \( U'\setminus\{\0\} \), so no linear bijection can preserve the form. @thm-witt-extension has nothing to extend: its hypothesis is that an isometry \( U \to U' \) is **given**, and here none exists.

(b) Let \( U \) and \( U' \) be totally isotropic of the same dimension \( k \). Any linear bijection \( \sigma \colon U \to U' \) is an isometry, since both restricted forms are identically zero, so \( \beta(\sigma\u,\sigma\v) = 0 = \beta(\u,\v) \) for all \( \u,\v \in U \). By @thm-witt-extension, \( \sigma \) extends to an isometry \( \varphi \) of \( V \), and \( \varphi(U) = U' \).

(c) Let \( U \) be maximal among totally isotropic subspaces, and let \( U_1 \) be one of the largest dimension \( m = \operatorname{ind}(\beta) \). If \( \dim U < m \), choose any \( k \)-dimensional subspace \( U_2 \subseteq U_1 \) with \( k = \dim U \); it is totally isotropic, so by (b) there is an isometry \( \varphi \) of \( V \) with \( \varphi(U) = U_2 \). Then \( \varphi^{-1}(U_1) \) is totally isotropic of dimension \( m > k \) and contains \( \varphi^{-1}(U_2) = U \), contradicting maximality. So \( \dim U = m \) for every maximal \( U \). @prp-totally-isotropic-bound says only \( m \le n/2 \); the present statement is sharper, since it says that no totally isotropic subspace can be maximal below the top dimension.
:::
