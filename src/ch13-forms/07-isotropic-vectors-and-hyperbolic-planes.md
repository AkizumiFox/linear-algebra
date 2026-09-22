# Where the Form Vanishes

Sections 4 and 5 diagonalized a symmetric form and counted the signs on the diagonal. Over \( \nR \) that is the whole story, but it hides the feature that makes indefinite forms geometrically different from inner products: there are non-zero vectors on which the form vanishes. This section takes those vectors seriously. They are not defects to be quarantined; they organize the space, because each one forces a two-dimensional piece of completely standard shape to split off. The result is a decomposition of any non-degenerate space into a pile of identical planes plus a remainder on which the form vanishes nowhere.

Throughout, \( F \) is a field with \( \operatorname{char} F \ne 2 \) (@def-characteristic), \( V \) is a finite-dimensional vector space over \( F \) with \( \dim V = n \), and \( \beta \) is a **symmetric** bilinear form on \( V \) (@def-symmetric-form) with quadratic form \( q(\v) = \beta(\v,\v) \) (@def-quadratic-form). Two vectors are orthogonal when \( \beta \) pairs them to \( 0 \) (@def-orthogonal-basis-form). For a subspace \( U \subseteq V \) we write, as in @exr-bilinear-forms-c2,
\[
U^{\perp_\beta} = \{\, \v \in V : \beta(\u,\v) = 0 \text{ for every } \u \in U \,\},
\]
and we write \( V = U \perp W \) to say that \( V = U \oplus W \) with every vector of \( U \) orthogonal to every vector of \( W \) — an **orthogonal direct sum**. The subscript \( \beta \) is dropped when only one form is in play.

## An intuition to give up

Thirteen chapters have trained one reflex above all others: \( \inner{\v}{\v} = 0 \) forces \( \v = \0 \). It is how we proved that an isometry is injective, that an orthogonal list is independent, that a Gram matrix determines its vectors. It is also the first thing that goes.

Take \( V = \nR^2 \) with
\[
q(x_1, x_2) = x_1^2 - x_2^2, \qquad
\A = \begin{pmatrix} 1 & 0 \\ 0 & -1\end{pmatrix}.
\]
The vector \( \v = (1,1) \) has \( q(\v) = 1 - 1 = 0 \). It is not \( \0 \), and the form is not defective: \( \det \A = -1 \ne 0 \), so \( \beta \) is non-degenerate (@prp-nondegenerate-iff-invertible). Indeed \( \beta(\v, (1,-1)) = 1 - (1)(-1) = 2 \ne 0 \), so \( \v \) is perfectly visible to \( \beta \) — it is only invisible to *itself*. The line \( \Span(\v) \) is a line of "length zero" inside a space where length is otherwise perfectly well behaved.

It gets worse, and the worse case is the one worth internalizing. Take \( V = \nR^4 \) with
\[
q(\x) = x_1^2 + x_2^2 - x_3^2 - x_4^2 ,
\]
of signature \( (2,2) \) and therefore non-degenerate. Let \( W = \Span(\e_1 + \e_3,\ \e_2 + \e_4) \), a plane. For \( \w = a(\e_1+\e_3) + b(\e_2+\e_4) \),
\[
q(\w) = a^2 + b^2 - a^2 - b^2 = 0 ,
\]
and in fact \( \beta \) vanishes on every pair from \( W \), since \( \beta(\e_1+\e_3, \e_2+\e_4) = 0 \) too. So \( \beta \) restricted to \( W \) is the **zero form** on a two-dimensional subspace of a four-dimensional space on which \( \beta \) is non-degenerate.

Say that again, because it is the sentence an inner-product-trained reader will refuse. A non-degenerate form can vanish identically on a subspace of half the dimension of the whole space. Non-degeneracy is a statement about \( V \); it says that no vector is orthogonal to *everything*. It says nothing whatsoever about what \( \beta \) does inside a subspace. The vectors of \( W \) above are orthogonal to each other and to themselves; they are not orthogonal to \( \e_1 - \e_3 \), and that is all non-degeneracy ever promised.

Once that is accepted, the rest of the section is straightforward. The vanishing vectors get a name, and then a structure theorem.

## Isotropic vectors and totally isotropic subspaces

*An isotropic vector is a non-zero vector that the form cannot tell from zero when it looks at it twice.*

::: {#def-isotropic-vector}
[Isotropic and Anisotropic]

Let \( \beta \) be a symmetric bilinear form on \( V \) with quadratic form \( q \).

::: {.enumerate options="label=(\alph*)"}
1. A vector \( \v \in V \) is **isotropic** if \( \v \ne \0 \) and \( q(\v) = 0 \), and **anisotropic** if \( q(\v) \ne 0 \).
2. The form \( \beta \) is **anisotropic** if it has no isotropic vectors: that is, if \( q(\v) = 0 \) implies \( \v = \0 \). Otherwise \( \beta \) is **isotropic**.
:::
:::

Both clauses hinge on small words. In (a) the vector is required to be **non-zero**, so \( \0 \) is neither isotropic nor anisotropic; the zero vector always has \( q(\0) = 0 \) and carries no information. In (b), "anisotropic" is a property of the **form on a particular space**. Anisotropy passes down to subspaces, since a subspace has fewer vectors to test; isotropy does not, and a form isotropic on \( V \) is very often anisotropic on a subspace. The word comes from *iso* (equal) and *tropos* (direction): a vector along which the form does not distinguish one direction from another.

Examples, over several fields.

- **A positive definite form has no isotropic vectors.** If \( q(\v) > 0 \) for \( \v \ne \0 \) then \( q(\v) = 0 \) forces \( \v = \0 \). So every inner product is anisotropic, which is exactly the reflex described above. The same holds for negative definite forms.
- **Over \( \nR \), signature \( (1,1) \).** For \( q = x_1^2 - x_2^2 \) the isotropic vectors are the non-zero multiples of \( (1,1) \) and of \( (1,-1) \), since \( q = (x_1-x_2)(x_1+x_2) \). Two lines, and nothing else.
- **Over \( \nC \).** For \( q = x_1^2 + x_2^2 \) on \( \nC^2 \) the factorization \( q = (x_1 + ix_2)(x_1 - ix_2) \) is available, so \( (1, i) \) and \( (1,-i) \) are isotropic. Over \( \nR \) the same \( q \) is positive definite. **Isotropy depends on the field**, not only on the polynomial.
- **Over \( \nF_3 \) and \( \nF_5 \).** For \( q = x_1^2 + x_2^2 \) the squares in \( \nF_3 \) are \( 0 \) and \( 1 \), so \( q(\x) = 0 \) needs \( x_1 = x_2 = 0 \) and the form is anisotropic. In \( \nF_5 \), however, \( 1^2 + 2^2 = 5 = 0 \), so \( (1,2) \) is isotropic. The same formula, two finite fields, two answers.
- **The degenerate case.** Every non-zero vector of the radical is isotropic, since \( \v \in \operatorname{rad}(\beta) \) gives \( \beta(\u,\v) = 0 \) for every \( \u \), in particular for \( \u = \v \). So a degenerate form is automatically isotropic. The converse fails, and the \( \nR^2 \) example above is the witness.

When a whole subspace consists of isotropic vectors, more is true than the definition says, and it deserves its own name.

::: {#def-totally-isotropic-subspace}
[Totally Isotropic Subspace]

A subspace \( W \subseteq V \) is **totally isotropic** for \( \beta \) if \( \beta(\u,\w) = 0 \) for **all** \( \u, \w \in W \); equivalently, if \( W \subseteq W^{\perp_\beta} \). The zero subspace is totally isotropic, trivially.
:::

The two formulations agree because \( W \subseteq W^{\perp_\beta} \) says exactly that every \( \w \in W \) is orthogonal to every \( \u \in W \). A third formulation is available in characteristic \( \ne 2 \) and is the one to use in practice: \( W \) is totally isotropic if and only if \( q(\w) = 0 \) for every \( \w \in W \). One direction is immediate; the other is @thm-polarization-forms applied to the restricted form, which recovers \( \beta \) on \( W \) from \( q \) on \( W \) and so makes it zero. In the \( \nR^4 \) example above we checked exactly this: \( q \) vanished on \( W \), and therefore so did \( \beta \).

Before the first theorem, one dimension count has to be on the table, because almost everything in this section and the next is a step away from it. @exr-bilinear-forms-c2 set it as an exercise in Section 1; here it is with a proof, so that the results below rest on it rather than on the exercise.

::: {#lem-perp-dimension}
[Dimension of an Orthogonal Complement]

Let \( \beta \) be a **non-degenerate** bilinear form on \( V \) with \( \dim V = n \), and let \( U \subseteq V \) be a subspace. Then \( U^{\perp_\beta} \) is a subspace of \( V \), and
\[
\dim U^{\perp_\beta} = n - \dim U .
\]
:::

::: {.idea}
Freezing the second slot of \( \beta \) turns it into a map \( V \to V^{*} \), and restricting a functional to \( U \) turns \( V^{*} \) into \( U^{*} \). The composite has kernel exactly \( U^{\perp_\beta} \), and non-degeneracy makes both maps surjective, so Rank–Nullity converts "onto \( U^{*} \)" into the count.
:::

::: {.proof}
Let \( R \colon V \to V^{*} \) send \( \v \) to the functional \( \beta(\cdot, \v) \) — the map called \( R_\beta \) in Section 1 — and let \( \rho \colon V^{*} \to U^{*} \) be restriction to \( U \). Both are linear, so \( S \coloneqq \rho \circ R \colon V \to U^{*} \) is linear, and \( S(\v) = \beta(\cdot, \v)\big|_U \). By the definition of \( U^{\perp_\beta} \), a vector \( \v \) lies in \( U^{\perp_\beta} \) exactly when \( \beta(\u, \v) = 0 \) for every \( \u \in U \), that is, exactly when \( S(\v) = 0 \). Hence \( U^{\perp_\beta} = \ker S \), which is a subspace.

Since \( \beta \) is non-degenerate, \( R \) is an isomorphism (@prp-nondegenerate-iff-invertible (c)), and \( \rho \) is surjective (@thm-dual-of-subspace). A composite of two surjections is a surjection, so \( \rank S = \dim U^{*} = \dim U \) (@cor-dimension-dual-space). By Rank–Nullity (@thm-rank-nullity),
\[
\dim U^{\perp_\beta} = \dim\ker S = n - \rank S = n - \dim U ,
\]
as claimed.
:::

Totally isotropic subspaces cannot be too large.

::: {#prp-totally-isotropic-bound}
[Half the Dimension, at Most]

Let \( \beta \) be a non-degenerate symmetric form on \( V \) with \( \dim V = n \), and let \( W \subseteq V \) be totally isotropic. Then \( \dim W \le n/2 \).
:::

::: {.proof}
Since \( \beta \) is non-degenerate, \( \dim W^{\perp_\beta} = n - \dim W \) by @lem-perp-dimension. Since \( W \) is totally isotropic, \( W \subseteq W^{\perp_\beta} \), so \( \dim W \le n - \dim W \), which is the claim.
:::

::: {.warning}
**An isotropic vector is not a zero vector, and a form that vanishes on a subspace need not be degenerate.** These are two different errors and both are common. The first confuses \( q(\v) = 0 \) with \( \v = \0 \); over \( \nR^{2} \) with \( q = x_1^2 - x_2^2 \) the vector \( (1,1) \) separates them. The second confuses "\( \beta \) vanishes on \( W \times W \)" with "\( \beta \) vanishes on \( \{\v\} \times V \)". Degeneracy is about the **second**: the radical consists of vectors killed by pairing with *everything*. The plane \( W \) of the \( \nR^4 \) example carries the zero form and contains no radical vector at all.
:::

::: {.check}
Is the plane \( \Span(\e_1, \e_2) \subseteq \nR^4 \) totally isotropic for \( q(\x) = x_1^2 + x_2^2 - x_3^2 - x_4^2 \)? What about \( \Span(\e_1 + \e_3, \e_1 - \e_3) \)?
:::

::: {.solution}
No to both. On \( \Span(\e_1,\e_2) \) the form restricts to \( x_1^2 + x_2^2 \), which is positive definite, so that plane is as far from totally isotropic as possible: it is anisotropic. The second plane is \( \Span(\e_1, \e_3) \), on which \( q \) restricts to \( x_1^2 - x_3^2 \); its two spanning vectors \( \e_1 \pm \e_3 \) are indeed isotropic, but \( \beta(\e_1+\e_3, \e_1-\e_3) = 1 - (-1) = 2 \ne 0 \), so the plane is not totally isotropic. Containing isotropic vectors is not the same as being totally isotropic.
:::

## Splitting off a non-degenerate piece

Everything below rests on one mechanism: if a subspace carries a non-degenerate restriction, it splits off orthogonally and the rest of the space is again non-degenerate. That is the analogue of "restrict to an invariant complement", and it is what makes induction possible.

::: {#prp-nondegenerate-restriction-splits}
[A Non-degenerate Subspace Splits Off]

Let \( \beta \) be a non-degenerate symmetric form on \( V \) with \( \dim V = n \), and let \( U \subseteq V \) be a subspace such that \( \beta|_{U \times U} \) is non-degenerate. Then
\[
V = U \perp U^{\perp_\beta} ,
\]
and \( \beta \) restricted to \( U^{\perp_\beta} \) is non-degenerate.
:::

::: {.idea}
Two things to check and one dimension count. The intersection \( U \cap U^{\perp_\beta} \) is precisely the radical of the restricted form, which the hypothesis kills; the dimension of \( U^{\perp_\beta} \) is \( n - \dim U \) because the global form is non-degenerate; and a vector of \( U^{\perp_\beta} \) orthogonal to \( U^{\perp_\beta} \) is orthogonal to all of \( V \), hence zero.
:::

::: {.proof}
Write \( U^{\perp} = U^{\perp_\beta} \). A vector \( \v \in U \cap U^{\perp} \) lies in \( U \) and satisfies \( \beta(\u,\v) = 0 \) for every \( \u \in U \), so \( \v \in \operatorname{rad}(\beta|_{U\times U}) \), which is \( \{\0\} \) by hypothesis (@def-nondegenerate). Hence \( U \cap U^{\perp} = \{\0\} \) and the sum \( U + U^{\perp} \) is direct (@thm-direct-sum-criteria).

Since \( \beta \) is non-degenerate on \( V \), @lem-perp-dimension gives \( \dim U^{\perp} = n - \dim U \). So \( \dim(U \oplus U^{\perp}) = n \), and a subspace of \( V \) of dimension \( n \) is \( V \) (@thm-dim-impl-eq). The sum is orthogonal by the definition of \( U^{\perp} \) together with the symmetry of \( \beta \), so \( V = U \perp U^{\perp} \).

Finally let \( \w \in U^{\perp} \) satisfy \( \beta(\x, \w) = 0 \) for every \( \x \in U^{\perp} \). For \( \u \in U \) we also have \( \beta(\u,\w) = 0 \), since \( \w \in U^{\perp} \). Every \( \v \in V \) is \( \u + \x \) with \( \u \in U \) and \( \x \in U^{\perp} \), so \( \beta(\v,\w) = 0 \) for every \( \v \in V \), that is \( \w \in \operatorname{rad}(\beta) = \{\0\} \). This proves the proposition.
:::

## Hyperbolic planes

Which two-dimensional forms are isotropic? Over \( \nR \) with signature \( (1,1) \) we found two isotropic lines, and the example \( q = x_1^2 - x_2^2 \) can be rewritten by the substitution \( u = x_1 + x_2 \), \( w = (x_1 - x_2)/2 \) as \( q = 2uw \) — the cross term alone, with no squares at all. That shape is the model, and it is the same over every field.

::: {#def-hyperbolic-plane}
[Hyperbolic Pair, Hyperbolic Plane]

Let \( \beta \) be a symmetric bilinear form on \( V \). A **hyperbolic pair** is an ordered pair \( (\e, \f) \) of vectors of \( V \) with
\[
q(\e) = 0, \qquad q(\f) = 0, \qquad \beta(\e,\f) = 1 .
\]
The subspace \( H = \Span(\e,\f) \) is then called a **hyperbolic plane**, and \( (\e,\f) \) is a **hyperbolic basis** of it.
:::

Four things follow at once. First, \( \e \) and \( \f \) are linearly independent: if \( \f = c\e \) then \( \beta(\e,\f) = c\,q(\e) = 0 \ne 1 \). So \( H \) really is a plane, \( \dim H = 2 \). Second, in the basis \( (\e,\f) \) the Gram matrix of \( \beta|_H \) is
\[
\mtx{\beta|_H}{(\e,\f)}{(\e,\f)} = \begin{pmatrix} 0 & 1 \\ 1 & 0\end{pmatrix},
\]
whose determinant is \( -1 \ne 0 \), so \( \beta|_H \) is **non-degenerate** (@prp-nondegenerate-iff-invertible) and @prp-nondegenerate-restriction-splits applies to it. Third, \( q(a\e + b\f) = 2ab \), so on a hyperbolic plane \( q \) takes **every** value in \( F \): given \( c \in F \), take \( a = c/2 \) and \( b = 1 \). Fourth, over \( \nR \) the Gram matrix has eigenvalues \( 1 \) and \( -1 \), so a hyperbolic plane has signature \( (1,1) \) and is the unique real example up to congruence.

Now the workhorse of this section and the next. It says that one isotropic vector is enough to manufacture a whole hyperbolic plane around it.

::: {#lem-isotropic-extends-to-hyperbolic}
[Every Isotropic Vector Lies in a Hyperbolic Plane]

Let \( \operatorname{char} F \ne 2 \), let \( \beta \) be a **non-degenerate** symmetric bilinear form on \( V \), and let \( \e \in V \) be isotropic. Then there is \( \f \in V \) such that \( (\e, \f) \) is a hyperbolic pair. In particular \( \e \) lies in a hyperbolic plane \( H = \Span(\e,\f) \), and \( \beta|_H \) is non-degenerate.
:::

::: {.idea}
Non-degeneracy hands us some \( \u \) with \( \beta(\e,\u) \ne 0 \), and rescaling makes \( \beta(\e,\u) = 1 \). Only one condition is still missing, \( q(\u) = 0 \), and \( \u \) can be corrected without disturbing what has been achieved: adding a multiple of \( \e \) changes \( q(\u) \) but not \( \beta(\e,\u) \), because \( q(\e) = 0 \). Solving for the multiple is one line, and it divides by \( 2 \) — which is where the characteristic hypothesis is spent, for the third time in this chapter.
:::

::: {.proof}
Since \( \e \ne \0 \) and \( \beta \) is non-degenerate, there is \( \u_0 \in V \) with \( c = \beta(\e,\u_0) \ne 0 \) (@def-nondegenerate). Put \( \u = c^{-1}\u_0 \), so that
\[
\beta(\e, \u) = 1 .
\]
Now set
\[
\f = \u - \tfrac12 q(\u)\,\e ,
\]
which is legitimate because \( \operatorname{char} F \ne 2 \) makes \( 2 = 1 + 1 \) invertible. Then, using bilinearity, symmetry and \( q(\e) = 0 \),
\[
\beta(\e,\f) = \beta(\e,\u) - \tfrac12 q(\u)\,q(\e) = 1 - 0 = 1 ,
\]
and
\[
\begin{aligned}
q(\f) &= q(\u) - 2\cdot\tfrac12 q(\u)\,\beta(\u,\e) + \tfrac14 q(\u)^2\,q(\e)\\
&= q(\u) - q(\u) + 0 = 0 .
\end{aligned}
\]
Together with \( q(\e) = 0 \), this shows that \( (\e,\f) \) is a hyperbolic pair. As noted after @def-hyperbolic-plane, \( \e \) and \( \f \) are independent, so \( H = \Span(\e,\f) \) is a plane, and the Gram matrix \( \begin{psmallmatrix} 0 & 1 \\ 1 & 0\end{psmallmatrix} \) is invertible, so \( \beta|_H \) is non-degenerate. This proves the lemma.
:::

::: {.remark}
Non-degeneracy of \( \beta \) is not decoration here. On \( \nR^2 \) with \( q(\x) = x_1^2 \), the vector \( \e_2 \) is isotropic and lies in no hyperbolic plane, because \( \beta(\e_2, \v) = 0 \) for every \( \v \) and a hyperbolic pair needs \( \beta(\e,\f) = 1 \). What fails is the very first line of the proof.
:::

## The Witt decomposition

Peeling off a hyperbolic plane and repeating is now a two-line induction, and it is the structural theorem of the section: it does for indefinite forms what "peel off an eigenvector" did for operators in Chapter 8.

::: {#thm-witt-decomposition}
[Witt Decomposition]

Let \( \operatorname{char} F \ne 2 \) and let \( \beta \) be a non-degenerate symmetric bilinear form on a finite-dimensional \( V \). Then there are an integer \( m \ge 0 \), hyperbolic planes \( H_1, \dots, H_m \subseteq V \) and a subspace \( V_0 \subseteq V \) such that
\[
V = H_1 \perp H_2 \perp \dots \perp H_m \perp V_0
\]
and \( \beta \) restricted to \( V_0 \) is **anisotropic**. In particular \( \dim V = 2m + \dim V_0 \).
:::

::: {.idea}
Induction on \( \dim V \). Either \( \beta \) is anisotropic, in which case take \( m = 0 \) and \( V_0 = V \) and stop; or there is an isotropic vector, in which case @lem-isotropic-extends-to-hyperbolic wraps a hyperbolic plane \( H_1 \) around it, @prp-nondegenerate-restriction-splits peels \( H_1 \) off with a non-degenerate remainder \( H_1^{\perp} \) of dimension \( \dim V - 2 \), and the induction hypothesis finishes the job there.
:::

::: {.proof}
Induct on \( \dim V \). If \( \dim V = 0 \), take \( m = 0 \) and \( V_0 = \{\0\} \), on which the form is anisotropic vacuously. Let \( \dim V \ge 1 \) and suppose the statement holds for every non-degenerate symmetric form on a space of smaller dimension.

If \( \beta \) is anisotropic, take \( m = 0 \) and \( V_0 = V \).

Otherwise \( \beta \) has an isotropic vector \( \e \). By @lem-isotropic-extends-to-hyperbolic there is \( \f \) with \( (\e,\f) \) a hyperbolic pair, and \( H_1 = \Span(\e,\f) \) is a hyperbolic plane with \( \beta|_{H_1} \) non-degenerate. By @prp-nondegenerate-restriction-splits,
\[
V = H_1 \perp H_1^{\perp_\beta},
\]
and \( \beta \) restricted to \( V' = H_1^{\perp_\beta} \) is non-degenerate, with \( \dim V' = \dim V - 2 < \dim V \). The induction hypothesis applied to \( (V', \beta|_{V'}) \) gives hyperbolic planes \( H_2, \dots, H_m \subseteq V' \) and an anisotropic \( V_0 \subseteq V' \) with \( V' = H_2 \perp \dots \perp H_m \perp V_0 \). Each \( H_i \) with \( i \ge 2 \) and \( V_0 \) lie inside \( V' = H_1^{\perp_\beta} \), so all the summands are pairwise orthogonal, and
\[
V = H_1 \perp H_2 \perp \dots \perp H_m \perp V_0 .
\]
Counting dimensions, \( \dim V = 2m + \dim V_0 \). This completes the induction.
:::

Two questions are now unavoidable: is \( m \) the same for every such decomposition, and is \( V_0 \) determined? The first has an answer here, and it comes from a quantity that mentions no decomposition at all.

::: {#def-witt-index}
[Witt Index]

Let \( \beta \) be a non-degenerate symmetric bilinear form on a finite-dimensional \( V \). The **Witt index** of \( \beta \) is
\[
\operatorname{ind}(\beta) \coloneqq \max\{\, \dim W : W \subseteq V \text{ totally isotropic} \,\} ,
\]
the largest dimension of a totally isotropic subspace. By @prp-totally-isotropic-bound it satisfies \( \operatorname{ind}(\beta) \le n/2 \), and it is \( 0 \) exactly when \( \beta \) is anisotropic.
:::

The maximum exists because the dimensions in question form a non-empty finite set of integers: \( W = \{\0\} \) is always totally isotropic, and all dimensions are at most \( n \). Nothing in the definition refers to a basis or a decomposition, so the Witt index is an invariant of \( (V,\beta) \) by construction. It is also exactly the number of planes.

::: {#prp-witt-index-counts-planes}
[The Number of Hyperbolic Planes Is the Witt Index]

In any decomposition \( V = H_1 \perp \dots \perp H_m \perp V_0 \) as in @thm-witt-decomposition, \( m = \operatorname{ind}(\beta) \). In particular \( m \) is the same for every such decomposition, and so is \( \dim V_0 = n - 2m \).
:::

::: {.idea}
One inequality is a construction: the first vectors \( \e_1, \dots, \e_m \) of the \( m \) hyperbolic bases span a totally isotropic subspace of dimension \( m \), since each is isotropic and different planes are orthogonal. The other inequality is an induction that trades one plane for one dimension: given a totally isotropic \( W \), the vectors of \( W \) orthogonal to \( \e_1 \) project into \( H_1^{\perp} \) as a totally isotropic subspace of dimension at least \( \dim W - 1 \). Repeating \( m \) times lands inside the anisotropic \( V_0 \), where the only totally isotropic subspace is \( \{\0\} \).
:::

::: {.proof}
Let \( (\e_i, \f_i) \) be a hyperbolic basis of \( H_i \) for each \( i \).

**Step 1: \( \operatorname{ind}(\beta) \ge m \).** Put \( W = \Span(\e_1, \dots, \e_m) \). The \( \e_i \) lie in different summands of a direct sum and are non-zero, so they are independent and \( \dim W = m \). For \( i \ne j \) we have \( \beta(\e_i,\e_j) = 0 \) because \( H_i \perp H_j \), and \( \beta(\e_i,\e_i) = q(\e_i) = 0 \). By bilinearity \( \beta \) vanishes on \( W \times W \), so \( W \) is totally isotropic of dimension \( m \).

**Step 2: a plane can be traded for a dimension.**

::: {.claim}
Let \( \beta \) be non-degenerate on \( V \), let \( H = \Span(\e,\f) \subseteq V \) be a hyperbolic plane, let \( V' = H^{\perp_\beta} \), and let \( W \subseteq V \) be totally isotropic. Then \( V' \) contains a totally isotropic subspace of dimension at least \( \dim W - 1 \).
:::

::: {.proof}
By @prp-nondegenerate-restriction-splits, \( V = H \perp V' \); let \( P \colon V \to V' \) be the projection with kernel \( H \), so that \( \v - P(\v) \in H \) for every \( \v \). Put
\[
W_1 = \{\, \w \in W : \beta(\e,\w) = 0 \,\},
\]
the kernel of a linear functional on \( W \), so \( \dim W_1 \ge \dim W - 1 \).

For \( \w \in V \) write \( \w - P(\w) = a\e + b\f \). Since \( \e \in H \) is orthogonal to \( V' \),
\[
\beta(\e,\w) = \beta(\e, a\e + b\f) = a\,q(\e) + b = b .
\]
So \( \w \in W_1 \) forces \( \w - P(\w) \in \Span(\e) \). Consequently, for \( \w, \w' \in W_1 \) the vectors \( \w - P(\w) \) and \( \w' - P(\w') \) both lie in \( \Span(\e) \), where \( \beta \) vanishes because \( q(\e) = 0 \); hence
\[
\beta(P(\w), P(\w')) = \beta(\w,\w') - \beta\bigl(\w - P(\w),\, \w' - P(\w')\bigr) = 0 - 0 = 0 ,
\]
the first equality using the orthogonality of \( H \) and \( V' \). So \( P(W_1) \) is a totally isotropic subspace of \( V' \).

It remains to bound its dimension. By Rank–Nullity (@thm-rank-nullity) applied to \( P|_{W_1} \), whose kernel is \( W_1 \cap H \),
\[
\dim P(W_1) = \dim W_1 - \dim(W_1 \cap H) .
\]
If \( W_1 \cap H = \{\0\} \), then \( \dim P(W_1) = \dim W_1 \ge \dim W - 1 \) and we are done. Otherwise pick \( \x \ne \0 \) in \( W_1 \cap H \). Then \( P(\x) = \0 \), so \( \x = \x - P(\x) \in \Span(\e) \) by the paragraph above, whence \( \e \in W \). But then \( \beta(\e,\w) = 0 \) for every \( \w \in W \), because \( W \) is totally isotropic and \( \e \in W \); so \( W_1 = W \). Moreover every \( \x \in W_1 \cap H \) lies in \( \Span(\e) \) by the same argument, so \( W_1 \cap H = \Span(\e) \) has dimension \( 1 \), and \( \dim P(W_1) = \dim W - 1 \). Either way the claim holds.
:::

**Step 3: \( \operatorname{ind}(\beta) \le m \).** Let \( W \subseteq V \) be totally isotropic. Apply Step 2 to \( H = H_1 \): since \( H_1^{\perp_\beta} = H_2 \perp \dots \perp H_m \perp V_0 \) carries a non-degenerate form, we obtain a totally isotropic subspace of it of dimension at least \( \dim W - 1 \). Repeating with \( H_2, \dots, H_m \) in turn produces a totally isotropic subspace of \( V_0 \) of dimension at least \( \dim W - m \). But \( \beta|_{V_0} \) is anisotropic, so a non-zero vector of \( V_0 \) has \( q \ne 0 \) and the only totally isotropic subspace of \( V_0 \) is \( \{\0\} \). Hence \( \dim W - m \le 0 \).

Steps 1 and 3 give \( \operatorname{ind}(\beta) = m \), and \( \dim V_0 = n - 2m \) follows by counting. This proves the proposition.
:::

So the number of planes is pinned down. What is not yet pinned down is \( V_0 \) itself: different decompositions produce different subspaces, and the claim one wants is that they all carry *the same form* in a suitable sense. Making that precise needs the word "isometry" for forms, and proving it needs Witt's theorems; both are the business of the next section.

## The two familiar fields

Over \( \nR \) and \( \nC \) everything can be computed, because the classification is already known.

::: {#prp-witt-index-real-complex}
[The Witt Index over the Reals and the Complexes]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \beta \) be a non-degenerate symmetric form on a real \( V \) with signature \( (n_+, n_-) \) (@def-signature), so \( n_+ + n_- = n \). Then \( \operatorname{ind}(\beta) = \min(n_+, n_-) \), and the anisotropic part has dimension \( \lvert n_+ - n_-\rvert \) and is definite.
2. Let \( \beta \) be a non-degenerate symmetric form on a complex \( V \) with \( \dim V = n \). Then \( \operatorname{ind}(\beta) = \lfloor n/2 \rfloor \). In particular every such form with \( n \ge 2 \) has an isotropic vector, and the anisotropic part has dimension \( 0 \) or \( 1 \).
:::
:::

::: {.proof}
(a) Put \( k = \min(n_+, n_-) \). By @thm-symmetric-form-diagonalizable and the rescaling that produced @eq-real-canonical-form, together with \( n_0 = 0 \), there is an orthogonal basis \( (\v_1, \dots, \v_n) \) with \( q(\v_i) = 1 \) for \( i \le n_+ \), \( q(\v_i) = -1 \) for \( n_+ < i \le n \), and distinct basis vectors orthogonal. For \( 1 \le i \le k \) set
\[
\e_i = \v_i + \v_{n_+ + i}, \qquad \f_i = \tfrac12\bigl(\v_i - \v_{n_+ + i}\bigr).
\]
Then \( q(\e_i) = 1 + (-1) = 0 \) and \( q(\f_i) = \tfrac14(1 + (-1)) = 0 \), while
\[
\beta(\e_i,\f_i) = \tfrac12\bigl(q(\v_i) - q(\v_{n_+ + i})\bigr) = \tfrac12(1+1) = 1 ,
\]
so \( (\e_i, \f_i) \) is a hyperbolic pair and \( H_i = \Span(\e_i,\f_i) \) a hyperbolic plane. These planes are pairwise orthogonal, since for \( i \ne j \) their spanning vectors involve disjoint sets of the \( \v \)'s. Let \( V_0 \) be the span of the remaining \( \lvert n_+ - n_-\rvert \) basis vectors, all of the same sign; then \( V = H_1 \perp \dots \perp H_k \perp V_0 \), and \( \beta|_{V_0} \) is definite, hence anisotropic. By @prp-witt-index-counts-planes, \( \operatorname{ind}(\beta) = k \).

(b) By @cor-complex-symmetric-classification and non-degeneracy, there is a basis \( (\v_1, \dots, \v_n) \) with \( q(\v_j) = 1 \) for every \( j \) and distinct basis vectors orthogonal. Write \( n = 2k + r \) with \( r \in \{0,1\} \), and let \( i \) denote the imaginary unit. For \( 1 \le j \le k \) set
\[
\e_j = \v_{2j-1} + i\,\v_{2j}, \qquad
\f_j = \tfrac12\bigl(\v_{2j-1} - i\,\v_{2j}\bigr).
\]
Then \( q(\e_j) = 1 + i^2 = 0 \) and likewise \( q(\f_j) = \tfrac14(1 + i^2) = 0 \), while \( \beta(\e_j,\f_j) = \tfrac12(1 + 1) = 1 \). As in (a) these span \( k \) pairwise orthogonal hyperbolic planes, and what is left is the span of \( \v_n \) when \( r = 1 \), on which \( q(c\v_n) = c^2 \ne 0 \) for \( c \ne 0 \), and \( \{\0\} \) when \( r = 0 \). So \( \operatorname{ind}(\beta) = k = \lfloor n/2\rfloor \) by @prp-witt-index-counts-planes. This proves the proposition.
:::

Two readings are worth recording. Over \( \nR \) the Witt index is the smaller of the two counts of signs: a definite form has index \( 0 \), and a form of signature \( (m,m) \) has the largest possible index \( m = n/2 \) — the \( \nR^4 \) example that opened the section, with \( n_+ = n_- = 2 \), sits exactly there. Over \( \nC \) the index is as large as it can be for every non-degenerate form, because \( -1 \) is a square and so a sum of two squares always factors; the only anisotropic complex spaces are \( \{\0\} \) and the lines.

::: {.check}
A non-degenerate real form has signature \( (3,1) \). What is its Witt index, and what is the anisotropic part?
:::

::: {.solution}
The index is \( \min(3,1) = 1 \), so exactly one hyperbolic plane splits off and \( \dim V_0 = 4 - 2 = 2 \). By @prp-witt-index-real-complex (a), \( V_0 \) carries a definite form of dimension \( \lvert 3-1\rvert = 2 \), positive definite here since the positive signs are the ones in surplus. Concretely \( \nR^{3,1} \) with \( q = x_1^2+x_2^2+x_3^2-x_4^2 \) splits as one hyperbolic plane, spanned by \( \e_3 \pm \e_4 \) after rescaling, orthogonal to the positive definite plane \( \Span(\e_1,\e_2) \). The largest totally isotropic subspace is a line, and the lines of this kind sweep out the light cone that Section 11 studies.
:::

## Exercises

### A. Check your understanding

::: {#exr-isotropic-vectors-and-hyperbolic-planes-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define **isotropic vector**, **totally isotropic subspace** and **hyperbolic pair**.
2. Determine whether the following statement is correct, and justify your answer: a non-degenerate form has no isotropic vectors.
3. What is the Witt index of a positive definite form on a space of dimension \( n \)? Of a form of signature \( (4,4) \)?
4. State the Gram matrix of a hyperbolic plane in a hyperbolic basis, and say why it shows the restricted form is non-degenerate.
5. Which hypothesis of @lem-isotropic-extends-to-hyperbolic fails for the form \( q(\x) = x_1^2 \) on \( \nR^2 \) at the isotropic vector \( \e_2 \)?
:::
:::

::: {.solution}
(a) A vector \( \v \) is isotropic if \( \v \ne \0 \) and \( q(\v) = 0 \). A subspace \( W \) is totally isotropic if \( \beta(\u,\w) = 0 \) for all \( \u,\w \in W \). A hyperbolic pair is a pair \( (\e,\f) \) with \( q(\e) = q(\f) = 0 \) and \( \beta(\e,\f) = 1 \).

(b) Incorrect. Non-degeneracy says \( \operatorname{rad}(\beta) = \{\0\} \), a statement about pairing with **every** vector. On \( \nR^2 \) with \( q = x_1^2 - x_2^2 \) the form is non-degenerate, since its Gram matrix has determinant \( -1 \), and \( (1,1) \) is isotropic.

(c) \( 0 \) for a positive definite form, since it is anisotropic, so the only totally isotropic subspace is \( \{\0\} \). For signature \( (4,4) \) the index is \( \min(4,4) = 4 \) by @prp-witt-index-real-complex (a), the largest value @prp-totally-isotropic-bound permits in dimension \( 8 \).

(d) It is \( \begin{psmallmatrix} 0 & 1 \\ 1 & 0 \end{psmallmatrix} \), of determinant \( -1 \ne 0 \), and a form is non-degenerate exactly when its Gram matrix is invertible (@prp-nondegenerate-iff-invertible).

(e) Non-degeneracy of \( \beta \). Here \( \e_2 \in \operatorname{rad}(\beta) \), so there is no \( \u \) with \( \beta(\e_2,\u) \ne 0 \) and the first line of the proof has nothing to choose.
:::

### B. Practice

::: {#exr-isotropic-vectors-and-hyperbolic-planes-b1}
[B1: Find the isotropic vectors]

For each of the following real quadratic forms, find all isotropic vectors, give the signature, and state the Witt index.

::: {.enumerate options="label=(\alph*)"}
1. \( q(x_1,x_2) = x_1^2 + 2x_1x_2 \) on \( \nR^2 \).
2. \( q(x_1,x_2,x_3) = x_1x_2 \) on \( \nR^3 \). *(Is this form non-degenerate?)*
3. \( q(x_1,x_2,x_3) = x_1^2 + x_2^2 + x_3^2 \) on \( \nR^3 \).
:::
:::

::: {.solution}
(a) \( q = x_1(x_1 + 2x_2) \), so \( q = 0 \) exactly on the two lines \( x_1 = 0 \) and \( x_1 = -2x_2 \). The isotropic vectors are the non-zero multiples of \( (0,1) \) and of \( (-2,1) \). The Gram matrix is \( \begin{psmallmatrix} 1 & 1\\ 1 & 0\end{psmallmatrix} \), of determinant \( -1 < 0 \), so the eigenvalues have opposite signs and the signature is \( (1,1) \). The Witt index is \( \min(1,1) = 1 \); indeed \( (0,1) \) is isotropic and by @lem-isotropic-extends-to-hyperbolic the whole space is one hyperbolic plane.

(b) The Gram matrix is \( \begin{psmallmatrix} 0 & 1/2 & 0\\ 1/2 & 0 & 0\\ 0&0&0\end{psmallmatrix} \), of rank \( 2 \), so the form is **degenerate** with \( \operatorname{rad}(\beta) = \Span(\e_3) \) and the notion of Witt index does not apply as defined. The isotropic vectors are those with \( x_1x_2 = 0 \), namely the union of the two planes \( x_1 = 0 \) and \( x_2 = 0 \), minus \( \0 \). On the non-degenerate part \( \Span(\e_1,\e_2) \) the signature is \( (1,1) \) and the index is \( 1 \).

(c) There are none: \( q \) is positive definite, so \( q(\x) = 0 \) forces \( \x = \0 \). The signature is \( (3,0) \) and the Witt index is \( 0 \).
:::

::: {#exr-isotropic-vectors-and-hyperbolic-planes-b2}
[B2: Build a hyperbolic basis]

::: {.enumerate options="label=(\alph*)"}
1. For \( q(x_1,x_2) = x_1^2 + x_2^2 \) on \( \nC^2 \), find a hyperbolic pair.
2. For \( q(x_1,x_2,x_3) = x_1^2 + x_2^2 - x_3^2 \) on \( \nR^3 \), find a hyperbolic pair \( (\e,\f) \) with \( \e = \e_1 + \e_3 \), and identify the anisotropic part \( \Span(\e,\f)^{\perp_\beta} \).
:::
:::

::: {.solution}
(a) Take \( \e = (1, i) \), so \( q(\e) = 1 + i^2 = 0 \). The vector \( \u = (1,-i) \) has \( \beta(\e,\u) = 1\cdot 1 + i\cdot(-i) = 2 \), so rescale: \( \f = \tfrac12(1,-i) \) gives \( \beta(\e,\f) = 1 \) and \( q(\f) = \tfrac14(1 + i^2) = 0 \). So \( \bigl((1,i), \tfrac12(1,-i)\bigr) \) is a hyperbolic pair, and \( \nC^2 \) is a single hyperbolic plane.

(b) \( q(\e) = 1 - 1 = 0 \), so \( \e \) is isotropic. Follow the proof of @lem-isotropic-extends-to-hyperbolic: \( \u_0 = \e_1 \) gives \( \beta(\e,\e_1) = 1 \), so take \( \u = \e_1 \), and \( q(\u) = 1 \), whence
\[
\f = \e_1 - \tfrac12(\e_1 + \e_3) = \tfrac12(\e_1 - \e_3).
\]
Check: \( q(\f) = \tfrac14(1-1) = 0 \) and \( \beta(\e,\f) = \tfrac12(1 + 1) = 1 \). For the complement, \( \v = (v_1,v_2,v_3) \) is orthogonal to both \( \e \) and \( \f \) exactly when \( v_1 - v_3 = 0 \) and \( v_1 + v_3 = 0 \), that is \( v_1 = v_3 = 0 \). So \( \Span(\e,\f)^{\perp_\beta} = \Span(\e_2) \), on which \( q = x_2^2 \) is positive definite. This is the decomposition of @thm-witt-decomposition with \( m = 1 \), matching \( \min(2,1) = 1 \).
:::

::: {#exr-isotropic-vectors-and-hyperbolic-planes-b3}
[B3: A totally isotropic subspace of the largest size]

Let \( q(\x) = x_1x_4 + x_2x_3 \) on \( \nR^4 \).

::: {.enumerate options="label=(\alph*)"}
1. Write down the Gram matrix and verify that \( \beta \) is non-degenerate.
2. Exhibit a totally isotropic subspace of dimension \( 2 \), and explain why none of dimension \( 3 \) exists.
3. Determine the signature of \( q \) and confirm the Witt index by @prp-witt-index-real-complex (a).
:::
:::

::: {.solution}
(a) Halving the cross-term coefficients (@eq-quadratic-in-coordinates),
\[
\A = \tfrac12\begin{pmatrix} 0&0&0&1\\ 0&0&1&0\\ 0&1&0&0\\ 1&0&0&0\end{pmatrix},
\]
whose determinant is \( \tfrac1{16}\det \) of the reversal permutation matrix, namely \( \tfrac1{16} \cdot 1 \ne 0 \). So \( \beta \) is non-degenerate by @prp-nondegenerate-iff-invertible.

(b) Take \( W = \Span(\e_1,\e_2) \). Every \( \w = (a,b,0,0) \) has \( q(\w) = 0 \), and \( \beta(\e_1,\e_2) = 0 \) from the matrix, so \( W \) is totally isotropic of dimension \( 2 \). No totally isotropic subspace has dimension \( 3 \), because @prp-totally-isotropic-bound caps it at \( 4/2 = 2 \).

(c) The two planes \( \Span(\e_1,\e_4) \) and \( \Span(\e_2,\e_3) \) are orthogonal, and \( (\e_1, 2\e_4) \) is a hyperbolic pair, since \( q(\e_1) = q(2\e_4) = 0 \) and \( \beta(\e_1, 2\e_4) = 2\cdot\tfrac12 = 1 \); the same works for \( (\e_2, 2\e_3) \). So each plane is hyperbolic, of signature \( (1,1) \). Hence \( q \) has signature \( (2,2) \) and, by @prp-witt-index-real-complex (a), Witt index \( \min(2,2) = 2 \), attained by the \( W \) of part (b).
:::

### C. Going deeper

::: {#exr-isotropic-vectors-and-hyperbolic-planes-c1}
[C1: Isotropy makes the form surjective]

Let \( \beta \) be a non-degenerate symmetric form on \( V \) over a field \( F \) with \( \operatorname{char} F \ne 2 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( \beta \) has an isotropic vector, then \( q \colon V \to F \) is surjective.
2. Deduce that if some \( c \in F \) is not of the form \( q(\v) \), then \( \beta \) is anisotropic.
3. Use (b) to show that the form \( q(x_1,x_2) = x_1^2 + x_2^2 \) on \( \nF_3^2 \) is anisotropic, and give its Witt index.
:::
:::

::: {.solution}
(a) Let \( \e \) be isotropic. By @lem-isotropic-extends-to-hyperbolic there is \( \f \) with \( (\e,\f) \) a hyperbolic pair. For \( c \in F \), put \( \v = \tfrac{c}{2}\e + \f \); this is legitimate since \( \operatorname{char} F \ne 2 \). Then
\[
q(\v) = \tfrac{c^2}{4}q(\e) + 2\cdot\tfrac{c}{2}\beta(\e,\f) + q(\f) = 0 + c + 0 = c .
\]
So every \( c \in F \) is a value of \( q \).

(b) Contrapositive of (a): if \( q \) is not surjective then \( \beta \) has no isotropic vector.

(c) The squares in \( \nF_3 \) are \( 0^2 = 0 \), \( 1^2 = 1 \), \( 2^2 = 1 \), so the values of \( x_1^2 + x_2^2 \) are \( 0, 1, 2 \) — which is all of \( \nF_3 \), so (b) gives nothing directly. Argue instead from the definition: \( q(\x) = 0 \) needs \( x_1^2 = -x_2^2 = 2x_2^2 \). If \( x_2 \ne 0 \) then \( x_2^2 = 1 \), so \( x_1^2 = 2 \), which is not a square in \( \nF_3 \); hence \( x_2 = 0 \) and then \( x_1 = 0 \). The form is anisotropic, its Witt index is \( 0 \), and the Gram matrix \( \I_2 \) shows it is non-degenerate. Over \( \nF_5 \) the same form is isotropic, since \( 1^2 + 2^2 = 0 \).
:::

::: {#exr-isotropic-vectors-and-hyperbolic-planes-c2}
[C2: A maximal totally isotropic subspace and its complement]

Let \( \beta \) be non-degenerate symmetric on \( V \) with \( \dim V = n \), and let \( W \subseteq V \) be totally isotropic with \( \dim W = \operatorname{ind}(\beta) = m \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \dim W^{\perp_\beta} = n - m \) and \( W \subseteq W^{\perp_\beta} \).
2. Prove that the form induced by \( \beta \) on the quotient \( W^{\perp_\beta}/W \) is well defined and anisotropic. *Hint: a coset with an isotropic representative would enlarge \( W \).*
3. Deduce that \( n - 2m = \dim(W^{\perp_\beta}/W) \) agrees with the dimension of the anisotropic part in @thm-witt-decomposition.
:::
:::

::: {.solution}
(a) The dimension is @lem-perp-dimension, using non-degeneracy, and the inclusion is @def-totally-isotropic-subspace.

(b) For \( \u, \v \in W^{\perp_\beta} \) and \( \w, \w' \in W \),
\[
\beta(\u + \w, \v + \w') = \beta(\u,\v) ,
\]
because each of the three remaining terms pairs a vector of \( W \) with a vector of \( W^{\perp_\beta} \supseteq W \), hence vanishes. So \( \bar\beta(\u + W, \v + W) \coloneqq \beta(\u,\v) \) is well defined, and it is bilinear and symmetric. Suppose \( \bar q(\u + W) = 0 \) with \( \u \notin W \), that is \( q(\u) = 0 \) with \( \u \in W^{\perp_\beta}\setminus W \). Then \( W + \Span(\u) \) is totally isotropic: it is spanned by isotropic vectors, \( \beta(\u,\w) = 0 \) for \( \w \in W \) because \( \u \in W^{\perp_\beta} \), and \( \beta \) vanishes on \( W \times W \). Its dimension is \( m + 1 > \operatorname{ind}(\beta) \), a contradiction. So \( \bar\beta \) is anisotropic.

(c) By (a), \( \dim(W^{\perp_\beta}/W) = (n-m) - m = n - 2m \). By @prp-witt-index-counts-planes the anisotropic part \( V_0 \) of a Witt decomposition also has dimension \( n - 2m \), since the index is \( m \). (That the two anisotropic forms agree, and not merely their dimensions, is proved in the next section.)
:::

::: {#exr-isotropic-vectors-and-hyperbolic-planes-c3}
[C3: Where characteristic 2 breaks]

Work over \( \nF_2 \) and let \( \beta \) be the dot product on \( \nF_2^2 \), with Gram matrix \( \I_2 \).

::: {.enumerate options="label=(\alph*)"}
1. Verify that \( \beta \) is symmetric and non-degenerate, and find all \( \v \) with \( q(\v) = 0 \).
2. Show that \( \beta \) has a vector with \( q(\v) = 0 \) and \( \v \ne \0 \) that lies in no hyperbolic plane, and identify which line of the proof of @lem-isotropic-extends-to-hyperbolic fails.
3. Explain in one sentence why the third description of "totally isotropic" given after @def-totally-isotropic-subspace is unavailable here.
:::
:::

::: {.solution}
(a) The Gram matrix \( \I_2 \) is symmetric and invertible, so \( \beta \) is symmetric and non-degenerate (@prp-nondegenerate-iff-invertible). Here \( q(\x) = x_1^2 + x_2^2 = (x_1+x_2)^2 \) over \( \nF_2 \), which vanishes exactly when \( x_1 = x_2 \). So \( q(\v) = 0 \) for \( \v = \0 \) and for \( \v = (1,1) \).

(b) Take \( \v = (1,1) \). A hyperbolic plane containing it would need \( \f \) with \( q(\f) = 0 \) and \( \beta(\v,\f) = 1 \). The only non-zero vector with \( q = 0 \) is \( \v \) itself, and \( \beta(\v,\v) = q(\v) = 0 \ne 1 \). The step that fails is the correction \( \f = \u - \tfrac12 q(\u)\e \): the element \( 2 = 1 + 1 \) is \( 0 \) in \( \nF_2 \) and is not invertible, so \( \tfrac12 \) does not exist.

(c) Because it is @thm-polarization-forms, which needs \( \operatorname{char} F \ne 2 \) to divide by \( 2 \); over \( \nF_2 \) the line \( \Span((1,1)) \) has \( q \equiv 0 \) on it and is indeed totally isotropic here, but the implication "\( q \) vanishes on \( W \) implies \( \beta \) vanishes on \( W \times W \)" is not available in general.
:::
