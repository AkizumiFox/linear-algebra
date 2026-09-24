# Isometries and Unitary Maps

Chapter 3 asked which linear maps are invertible. Now that we can measure, we can ask a sharper question: which linear maps leave the measurements alone? A map that never changes a length never changes an angle either, and the two facts turn out to be the same fact. This section identifies these maps in five equivalent ways, collects them into the orthogonal and unitary groups, and classifies them completely in dimensions two and three, where they are exactly the rotations and reflections that the words suggest. At the end we drop linearity from the hypothesis and get it back as a conclusion.

As throughout the chapter, \( F \) is \( \nR \) or \( \nC \), inner products are linear in the first slot, and spaces are finite-dimensional unless stated otherwise.

## Maps that do not change length

Take the plane with its usual inner product and ask which linear maps move the picture rigidly. Turning the plane about the origin clearly does not change any length. Flipping it across a line through the origin does not either. Scaling by \( 2 \) obviously does. Shearing, \( (x_1, x_2) \mapsto (x_1 + x_2, x_2) \), also does: it fixes \( \e_1 \) but sends \( \e_2 \) to \( (1, 1) \), of length \( \sqrt2 \). So "does not change length" is a genuine restriction, and it is worth a name.

*An isometry is a linear map that every ruler agrees with: the image of a vector is exactly as long as the vector.*

::: {#def-isometry}
[Isometry]

Let \( V \) and \( W \) be inner product spaces over \( F \). A linear map \( T \in \cL(V, W) \) is an **isometry** if
\[
\norm{T\v} = \norm{\v} \qquad \text{for every } \v \in V .
\]
:::

In words: the condition is required for **every** vector, not merely for the vectors of a basis, and it compares a norm in \( W \) with a norm in \( V \). The word comes from *iso* (equal) and *metron* (measure). Some authors reserve "isometry" for a bijective such map; we do not, and @def-unitary-orthogonal below names the bijective case separately.

Two consequences are immediate. An isometry is injective, since \( T\v = \0 \) forces \( \norm{\v} = \norm{T\v} = 0 \) and hence \( \v = \0 \) (@thm-injective-iff-trivial-kernel). And if \( T\v = \lambda\v \) with \( \v \neq \0 \), then \( \norm{\v} = \norm{\lambda\v} = \lvert\lambda\rvert\,\norm{\v} \) by @thm-norm-properties (b), so \( \lvert\lambda\rvert = 1 \). We record the second observation, which the classification below will use twice.

::: {#prp-isometry-eigenvalues-modulus-one}
[Eigenvalues of an Isometry Have Modulus 1]

Let \( T \in \cL(V) \) be an isometry of an inner product space over \( F \), and let \( \lambda \in F \) be an eigenvalue of \( T \). Then \( \lvert\lambda\rvert = 1 \). In particular, if \( F = \nR \) then \( \lambda = 1 \) or \( \lambda = -1 \).
:::

::: {.proof}
Let \( \v \neq \0 \) satisfy \( T\v = \lambda\v \) (@def-eigenvalue). Then \( \norm{\v} = \norm{T\v} = \norm{\lambda\v} = \lvert\lambda\rvert\,\norm{\v} \) by @thm-norm-properties (b), and \( \norm{\v} \neq 0 \), so dividing gives \( \lvert\lambda\rvert = 1 \). The only real numbers of modulus \( 1 \) are \( \pm 1 \).
:::

::: {#exm-isometries}
[Isometries and Near-Isometries]

Decide which of the following linear maps are isometries, with the standard inner products.

::: {.enumerate options="label=(\alph*)"}
1. \( T \colon \nR^2 \to \nR^3 \), \( T(x_1, x_2) = (x_1, x_2, 0) \).
2. \( T_{\P} \colon F^n \to F^n \) for a permutation matrix \( \P \) (@def-permutation-matrix).
3. \( T \colon \nC \to \nC \), \( T(z) = \alpha z \), where \( \lvert\alpha\rvert = 1 \).
4. \( T \colon \nR^2 \to \nR^2 \), \( T(x_1, x_2) = (x_1 + x_2, x_2) \).
5. The orthogonal projection \( P_U \) onto a subspace \( U \) with \( \{\0\} \neq U \neq V \).
:::
:::

::: {.solution}
(a) Yes: \( \norm{T\x}^2 = x_1^2 + x_2^2 + 0 = \norm{\x}^2 \). Note that \( T \) is not surjective, so an isometry need not be invertible.

(b) Yes. A permutation matrix has exactly one \( 1 \) in each row and column, so \( \P\x \) is the list \( x_1, \dots, x_n \) in a different order, and \( \norm{\P\x}^2 = \sum_i \lvert x_{\sigma(i)}\rvert^2 = \sum_i \lvert x_i\rvert^2 \), the same sum reordered.

(c) Yes: \( \norm{\alpha z} = \lvert\alpha z\rvert = \lvert\alpha\rvert\lvert z\rvert = \lvert z\rvert \).

(d) No: \( \norm{T\e_2} = \norm{(1, 1)} = \sqrt2 \neq 1 = \norm{\e_2} \). One vector is enough to refute.

(e) No: pick \( \v \in U^{\perp} \) with \( \v \neq \0 \), which exists because \( U \neq V \) (@thm-orthogonal-decomposition (a)). Then \( P_U\v = \0 \) (@thm-projection-formula (a)), so \( \norm{P_U\v} = 0 \neq \norm{\v} \). A projection destroys length by design.
:::

## Five ways to say the same thing

The definition mentions only norms, but norms and inner products determine each other. In one direction this is @def-induced-norm. In the other it is the following identity, which reconstructs the inner product from lengths alone; it is the reason that preserving length automatically preserves angle.

::: {#lem-polarization-identities}
[Polarization Identities]

Let \( V \) be an inner product space over \( F \) and let \( \u, \v \in V \).

::: {.enumerate options="label=(\alph*)"}
1. If \( F = \nR \), then \( \displaystyle \inner{\u}{\v} = \tfrac14\bigl(\norm{\u + \v}^2 - \norm{\u - \v}^2\bigr) \).
2. If \( F = \nC \), then \( \displaystyle \inner{\u}{\v} = \tfrac14\sum_{k=0}^{3} i^k\,\norm{\u + i^k\v}^2 \).
:::
:::

::: {.idea}
Expand every norm squared with \( \norm{\u + \w}^2 = \norm{\u}^2 + 2\operatorname{Re}\inner{\u}{\w} + \norm{\w}^2 \) (@thm-norm-properties (c)). In the real case the two expansions differ only in the middle term, which survives doubled. In the complex case the four terms \( \norm{\u}^2 + \norm{\w}^2 \) are the same in all four summands and are killed by \( \sum_k i^k = 0 \); what is left is a sum in which the \( \inner{\u}{\v} \) parts reinforce and the \( \conj{\inner{\u}{\v}} \) parts cancel.
:::

::: {.proof}
(a) By @thm-norm-properties (c), \( \norm{\u \pm \v}^2 = \norm{\u}^2 \pm 2\inner{\u}{\v} + \norm{\v}^2 \), since over \( \nR \) the inner product is its own real part. Subtracting, \( \norm{\u + \v}^2 - \norm{\u - \v}^2 = 4\inner{\u}{\v} \).

(b) Write \( z = \inner{\u}{\v} \). Since \( \lvert i^k \rvert = 1 \), @thm-norm-properties (b) and (c) give \( \norm{i^k\v} = \norm{\v} \) and
\[
\norm{\u + i^k\v}^2 = \norm{\u}^2 + \norm{\v}^2 + 2\operatorname{Re}\inner{\u}{i^k\v} = \norm{\u}^2 + \norm{\v}^2 + 2\operatorname{Re}\bigl(i^{-k}z\bigr),
\]
where \( \inner{\u}{i^k\v} = \conj{i^k}\,z = i^{-k}z \) by conjugate-linearity in the second slot. Multiply by \( i^k \) and sum over \( k = 0, 1, 2, 3 \). The first two terms contribute \( (\norm{\u}^2 + \norm{\v}^2)\sum_k i^k = 0 \), because \( 1 + i - 1 - i = 0 \). For the remaining terms use \( 2\operatorname{Re}(w) = w + \conj{w} \):
\[
\sum_{k=0}^{3} i^k \cdot 2\operatorname{Re}\bigl(i^{-k}z\bigr) = \sum_{k=0}^{3} i^k\bigl(i^{-k}z + i^{k}\conj{z}\bigr) = \sum_{k=0}^{3} z + \conj{z}\sum_{k=0}^{3} i^{2k} = 4z + 0,
\]
since \( \sum_k i^{2k} = 1 - 1 + 1 - 1 = 0 \). Dividing by \( 4 \) gives the identity.
:::

Now the main theorem. It says that length, angle, the adjoint and orthonormal bases all detect the same class of maps, and it is the reason isometries are easy to work with: whichever of the five descriptions a problem hands you, you may switch to whichever one you want.

::: {#thm-isometry-characterizations}
[Characterizations of Isometries]

Let \( V \) and \( W \) be finite-dimensional inner product spaces over \( F \), and let \( T \in \cL(V, W) \). The following are equivalent.

::: {.enumerate options="label=(\alph*)"}
1. \( T \) is an isometry: \( \norm{T\v} = \norm{\v} \) for every \( \v \in V \).
2. \( T \) preserves inner products: \( \inner{T\u}{T\v} = \inner{\u}{\v} \) for all \( \u, \v \in V \).
3. \( T^{*}T = \id_V \).
4. \( T \) sends **every** orthonormal list in \( V \) to an orthonormal list in \( W \).
5. \( T \) sends **some** orthonormal basis of \( V \) to an orthonormal list in \( W \).
6. For one (equivalently every) pair of orthonormal bases \( \sB \) of \( V \) and \( \sC \) of \( W \), the matrix \( \A = \mtx{T}{\sB}{\sC} \in M_{m \times n}(F) \), where \( n = \dim V \) and \( m = \dim W \), satisfies \( \A^{*}\A = \I_n \); that is, the \( n \) columns of \( \A \) are orthonormal vectors of \( F^m \).
:::

If in addition \( \dim W = \dim V \), then (a)--(f) are further equivalent to each of

::: {.enumerate options="label=(g\arabic*)"}
1. \( T \) is invertible with \( T^{-1} = T^{*} \);
2. \( TT^{*} = \id_W \).
:::
:::

::: {.idea}
Run the cycle (a) \( \Rightarrow \) (b) \( \Rightarrow \) (c) \( \Rightarrow \) (a). The first step is polarization: lengths are all we are given, and @lem-polarization-identities converts them into an inner product. The second is the adjoint doing its job, \( \inner{T\u}{T\v} = \inner{\u}{T^{*}T\v} \), plus non-degeneracy. The third is the same identity read backwards with \( \u = \v \). Then (b) \( \Rightarrow \) (d) \( \Rightarrow \) (e) \( \Rightarrow \) (b) is a second, shorter cycle, and (c) \( \Leftrightarrow \) (f) is @thm-matrix-of-adjoint. The last two need a dimension count: \( T^{*}T = \id \) makes \( T \) injective, and in equal dimensions injective means invertible.
:::

::: {.proof}
(a) \( \Rightarrow \) (b). Suppose \( \norm{T\v} = \norm{\v} \) for all \( \v \). If \( F = \nR \), then by @lem-polarization-identities (a) applied in \( W \) and then in \( V \), and by the linearity of \( T \),
\[
\begin{aligned}
\inner{T\u}{T\v}
  &= \tfrac14\bigl(\norm{T(\u + \v)}^2 - \norm{T(\u - \v)}^2\bigr) \\
  &= \tfrac14\bigl(\norm{\u + \v}^2 - \norm{\u - \v}^2\bigr) = \inner{\u}{\v} .
\end{aligned}
\]
If \( F = \nC \), the same two lines work with @lem-polarization-identities (b), since \( T(\u + i^k\v) = T\u + i^kT\v \).

(b) \( \Rightarrow \) (c). For all \( \u, \v \in V \), @def-adjoint gives \( \inner{\u}{T^{*}T\v} = \inner{T\u}{T\v} = \inner{\u}{\v} \), so \( \inner{\u}{T^{*}T\v - \v} = 0 \) for every \( \u \). Taking \( \u = T^{*}T\v - \v \) makes its norm zero, so \( T^{*}T\v = \v \) for every \( \v \).

(c) \( \Rightarrow \) (a). \( \norm{T\v}^2 = \inner{T\v}{T\v} = \inner{\v}{T^{*}T\v} = \inner{\v}{\v} = \norm{\v}^2 \), and norms are non-negative, so \( \norm{T\v} = \norm{\v} \).

(b) \( \Rightarrow \) (d). Let \( (\u_1, \dots, \u_k) \) be orthonormal in \( V \), so \( \inner{\u_i}{\u_j} = \delta_{ij} \). Then \( \inner{T\u_i}{T\u_j} = \inner{\u_i}{\u_j} = \delta_{ij} \), which is exactly what it means for \( (T\u_1, \dots, T\u_k) \) to be orthonormal (@def-orthonormal-list).

(d) \( \Rightarrow \) (e). \( V \) is finite-dimensional, so it has an orthonormal basis by @thm-gram-schmidt, and (d) applies to it.

(e) \( \Rightarrow \) (b). Let \( \sB = (\v_1, \dots, \v_n) \) be an orthonormal basis of \( V \) with \( (T\v_1, \dots, T\v_n) \) orthonormal. Given \( \u, \v \in V \), expand them in \( \sB \) as \( \u = \sum_i a_i\v_i \) and \( \v = \sum_j b_j\v_j \). Expanding both slots and using orthonormality twice,
\[
\inner{T\u}{T\v} = \sum_{i, j} a_i\conj{b_j}\inner{T\v_i}{T\v_j} = \sum_{i} a_i\conj{b_i} = \sum_{i, j} a_i\conj{b_j}\inner{\v_i}{\v_j} = \inner{\u}{\v},
\]
since in both double sums only the terms with \( i = j \) survive.

(c) \( \Leftrightarrow \) (f). Fix orthonormal bases \( \sB \) and \( \sC \) and put \( \A = \mtx{T}{\sB}{\sC} \). By @thm-matrix-of-adjoint, \( \mtx{T^{*}}{\sC}{\sB} = \A^{*} \), and by @thm-matrix-of-composition, \( \mtx{T^{*}T}{\sB}{\sB} = \A^{*}\A \). Since a map is determined by its matrix in fixed bases, \( T^{*}T = \id_V \) if and only if \( \A^{*}\A = \I_n \). The \( (i, j) \) entry of \( \A^{*}\A \) is the standard inner product of column \( j \) with column \( i \), so this says the columns are orthonormal. As (c) does not mention the bases, the condition holds for one pair of orthonormal bases if and only if it holds for every pair.

Now assume \( \dim W = \dim V \).

(c) \( \Rightarrow \) (g1). By (c) and @thm-injective-iff-trivial-kernel, \( T \) is injective, so \( \rank T = \dim V = \dim W \) by @thm-rank-nullity, and \( T \) is surjective. Hence \( T \) is invertible, and multiplying \( T^{*}T = \id_V \) on the right by \( T^{-1} \) gives \( T^{*} = T^{-1} \).

(g1) \( \Rightarrow \) (g2). \( TT^{*} = TT^{-1} = \id_W \).

(g2) \( \Rightarrow \) (c). \( TT^{*} = \id_W \) makes \( T \) surjective, hence invertible by the equal dimensions and @thm-rank-nullity, and multiplying on the left by \( T^{-1} \) gives \( T^{*} = T^{-1} \), so \( T^{*}T = \id_V \). This proves the theorem.
:::

Condition (f) is the one to use on a concrete matrix: **check that the columns are orthonormal**. Condition (c) is the one to use in a proof. Condition (e) is the cheapest to verify on an abstract map, since one basis suffices, and (d) is what you get out afterwards.

::: {.warning}
**\( T^{*}T = \id \) does not give \( TT^{*} = \id \) when the dimensions differ.** Let \( T \colon \nR^2 \to \nR^3 \) be \( T(x_1, x_2) = (x_1, x_2, 0) \), with matrix \( \A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix} \). Then \( \A\tp\A = \I_2 \), so \( T \) is an isometry; but
\[
\A\A\tp = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix} \neq \I_3 .
\]
Ask *identity on what?* The composite \( TT^{*} \) is the orthogonal projection of \( \nR^3 \) onto \( \im T \), the \( x_1x_2 \)-plane, and it is the identity there and nowhere else. Only when \( T \) is surjective can both products be identities.
:::

::: {.check}
Is \( \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \) the matrix of an isometry of \( \nR^2 \)? If not, is some scalar multiple of it?
:::

::: {.solution}
No: the first column has norm \( \sqrt2 \neq 1 \), so the columns are not orthonormal and condition (f) of @thm-isometry-characterizations fails. The columns are, however, orthogonal, so dividing by \( \sqrt2 \) normalizes both and \( \tfrac{1}{\sqrt2}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \) is an isometry.
:::

## Unitary and orthogonal maps

Conditions (g1) and (g2) describe the case that matters most, an isometry of a space with itself. It is the case with a name.

::: {#def-unitary-orthogonal}
[Unitary and Orthogonal]

Let \( V \) be a finite-dimensional inner product space over \( F \). An operator \( T \in \cL(V) \) is **unitary** if
\[
T^{*}T = TT^{*} = \id_V ,
\]
equivalently if \( T \) is an invertible isometry. When \( F = \nR \), such a \( T \) is also called **orthogonal**.

A matrix \( \A \in M_n(\nC) \) with \( \A^{*}\A = \I_n \) is a **unitary matrix**; a matrix \( \A \in M_n(\nR) \) with \( \A\tp\A = \I_n \) is an **orthogonal matrix**.
:::

For a **square** matrix the one-sided condition \( \A^{*}\A = \I \) already forces \( \A\A^{*} = \I \), by part (g2) of @thm-isometry-characterizations, or directly by @thm-one-sided-inverse. The warning above shows that squareness is not a formality.

::: {#def-unitary-orthogonal-groups}
[The Unitary and Orthogonal Groups]

For \( n \ge 1 \) set
\[
\Unit(n) \coloneqq \{ \A \in M_n(\nC) : \A^{*}\A = \I_n \}, \qquad
\Orth(n) \coloneqq \{ \A \in M_n(\nR) : \A\tp\A = \I_n \},
\]
and \( \SO(n) \coloneqq \{ \A \in \Orth(n) : \det \A = 1 \} \), the **special orthogonal group**.
:::

::: {#prp-orthogonal-group-properties}
[The Groups and Their Determinants]

::: {.enumerate options="label=(\alph*)"}
1. \( \Unit(n) \) and \( \Orth(n) \) are groups under matrix multiplication, and \( \Orth(n) = \Unit(n) \cap M_n(\nR) \).
2. If \( \A \in \Unit(n) \) then \( \lvert\det \A\rvert = 1 \). If \( \A \in \Orth(n) \) then \( \det \A = 1 \) or \( \det \A = -1 \).
3. \( \SO(n) \) is a subgroup of \( \Orth(n) \).
:::
:::

::: {.proof}
(a) \( \I^{*}\I = \I \), so \( \I \in \Unit(n) \). If \( \A, \B \in \Unit(n) \) then \( (\A\B)^{*}(\A\B) = \B^{*}\A^{*}\A\B = \B^{*}\B = \I \), so \( \A\B \in \Unit(n) \). Each \( \A \in \Unit(n) \) is invertible with \( \A^{-1} = \A^{*} \), and \( (\A^{*})^{*}\A^{*} = \A\A^{*} = \I \), so \( \A^{-1} \in \Unit(n) \). Associativity is inherited from matrix multiplication. The same three lines prove the claim for \( \Orth(n) \), with \( \A^{*} = \A\tp \) for a real matrix, which is also the last assertion.

(b) The determinant is the sum \( \sum_{\sigma} \sgn(\sigma)a_{\sigma(1)1}\cdots a_{\sigma(n)n} \) of @def-determinant, and conjugation of complex numbers respects sums and products, so \( \det \conj{\A} = \conj{\det \A} \). With @thm-det-transpose this gives \( \det \A^{*} = \det\bigl(\conj{\A}\tp\bigr) = \det\conj{\A} = \conj{\det \A} \). Hence, by @thm-det-multiplicative,
\[
1 = \det \I_n = \det(\A^{*}\A) = \conj{\det \A}\,\det \A = \lvert\det \A\rvert^2 .
\]
For real \( \A \) the determinant is real, and the real numbers of modulus \( 1 \) are \( \pm 1 \).

(c) \( \det \I = 1 \), and \( \det \) is multiplicative (@thm-det-multiplicative), so \( \det(\A\B) = 1 \) and \( \det(\A^{-1}) = (\det \A)^{-1} = 1 \) whenever \( \det \A = \det \B = 1 \).
:::

::: {.warning}
**\( \lvert\lambda\rvert = 1 \) does not mean \( \lambda = \pm1 \), and \( \det \A = 1 \) does not mean "rotation".** The matrix \( -\I_4 \in \SO(4) \) has determinant \( (-1)^4 = 1 \), but it fixes no non-zero vector, so it is not a rotation about an axis in any sense. Likewise \( -\I_3 \in \Orth(3) \) has determinant \( -1 \) but is not a reflection in a plane: a reflection fixes a plane pointwise, and \( -\I_3 \) fixes only \( \0 \). The clean classification below is a feature of dimensions \( 2 \) and \( 3 \), not a general theorem.
:::

## The Frobenius norm and unitary factors

Section 1 made \( M_{m \times n}(F) \) into an inner product space by declaring
\[
\inner{\A}{\B} = \tr(\B^{*}\A) ,
\]
the **Frobenius inner product**, and observing that it is nothing but the standard inner product of \( F^{mn} \) after the entries are listed in a single column. Its induced norm (@def-induced-norm) was named there but never given a symbol. This is the place to give it one, because the single property that makes it useful is a statement about unitary factors, and unitary factors have only just arrived.

For \( \A \in M_{m \times n}(\nC) \), the **Frobenius norm** of \( \A \) is
\[
\norm{\A}_F \coloneqq \sqrt{\inner{\A}{\A}}
= \Bigl( \sum_{i,j} \lvert a_{ij} \rvert^2 \Bigr)^{1/2} .
\]
The subscript \( F \) is there because \( \norm{\cdot} \) with no subscript already means the norm of a *vector*, and a matrix will later be asked to be both. Two remarks on the formula. First, it treats \( \A \) as a list of \( mn \) numbers and forgets that they are arranged in a rectangle: it is blind to the difference between \( \begin{pmatrix} 1 & 0 \\ 0 & 0\end{pmatrix} \) and \( \begin{pmatrix} 0 & 1 \\ 0 & 0\end{pmatrix} \). Second, it is computable with no eigenvalues, no row reduction and no choices: add up \( mn \) squared moduli.

The trace form of the same quantity is the one that does the work.

::: {.check}
Why is \( \norm{\A}_F^2 = \tr(\A^{*}\A) \)?
:::

::: {.solution}
The \( (j, j) \) entry of \( \A^{*}\A \) is \( \sum_i \conj{a_{ij}}a_{ij} = \sum_i \lvert a_{ij}\rvert^2 \), the squared length of the \( j \)-th column. Summing over \( j \) sweeps every entry of \( \A \) exactly once, so \( \tr(\A^{*}\A) = \sum_{i,j}\lvert a_{ij}\rvert^2 \). Equivalently, it is \( \inner{\A}{\A} \) read off the definition of the Frobenius inner product.
:::

Now the property that makes this the right yardstick whenever orthonormal bases are in play: unitary factors are invisible to it.

::: {#lem-frobenius-unitarily-invariant}
[Unitary Invariance of the Frobenius Norm]

Let \( \A \in M_{m \times n}(\nC) \), let \( \U \in \Unit(m) \) and let \( \V \in \Unit(n) \). Then
\[
\norm{\U\A}_F = \norm{\A}_F = \norm{\A\V}_F .
\]
In particular, if \( \A \) is square and \( \U \) is unitary then \( \norm{\U^{*}\A\U}_F = \norm{\A}_F \).
:::

::: {.proof}
Using \( \norm{\B}_F^2 = \tr(\B^{*}\B) \), then \( (\U\A)^{*} = \A^{*}\U^{*} \) and \( \U^{*}\U = \I_m \),
\[
\norm{\U\A}_F^2 = \tr(\A^{*}\U^{*}\U\A) = \tr(\A^{*}\A) = \norm{\A}_F^2 .
\]
For the right-hand factor, @thm-trace-properties (3) lets the \( \V \) travel around the trace, and \( \V\V^{*} = \I_n \):
\[
\norm{\A\V}_F^2 = \tr(\V^{*}\A^{*}\A\V) = \tr(\A^{*}\A\V\V^{*}) = \norm{\A}_F^2 .
\]
Both norms are non-negative reals, so equality of the squares gives equality of the norms. For the last statement, \( \U^{*} \) is unitary too, since \( (\U^{*})^{*}\U^{*} = \U\U^{*} = \I \); apply the first equality to the left factor \( \U^{*} \) and the second to the right factor \( \U \).
:::

The consequence to keep in mind is this. If \( T \in \cL(V) \) is an operator on a finite-dimensional complex inner product space and we compute \( \norm{\mtx{T}{\sB}{\sB}}_F \) in an **orthonormal** basis \( \sB \), the answer does not depend on which orthonormal basis we chose, because two such matrices differ by a unitary similarity (@thm-change-of-basis-maps). So the Frobenius norm is a property of \( T \), not of our coordinates — exactly like the trace and the determinant, and unlike, say, the largest entry.

## Rotations and reflections of the plane

In dimension \( 2 \) the group \( \Orth(2) \) can be written down completely, and the two determinant values split it into exactly the two families the words suggest. For \( \theta \in \nR \) put
\[
\R_{\theta} \coloneqq \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix},
\qquad
\M_{\theta} \coloneqq \begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix} .
\]

\begin{center}
\begin{tikzpicture}[scale=1.7, lab/.style={font=\small}]
    \draw[->, gray] (-1.35,0) -- (1.4,0);
    \draw[->, gray] (0,-0.35) -- (0,1.4);
    \draw[dashed, black!40] (0,0) circle (1);
    \draw[->, thick, black!55] (0,0) -- (1,0) node[below right, black, lab] {$\e_1$};
    \draw[->, thick, black!55] (0,0) -- (0,1) node[above right, black, lab] {$\e_2$};
    \draw[->, very thick] (0,0) -- (38:1) node[right, lab] {$\R_{\theta}\e_1$};
    \draw[->, very thick] (0,0) -- (128:1) node[above left, lab] {$\R_{\theta}\e_2$};
    \draw (0.42,0) arc (0:38:0.42);
    \node[lab] at (19:0.58) {$\theta$};
    \draw (90:0.5) arc (90:128:0.5);
    \node[lab] at (109:0.66) {$\theta$};
    \node[lab, align=center] at (0.05,-1.32) {the columns of $\R_{\theta}$ are the rotated axes};
\end{tikzpicture}
\end{center}

The first matrix rotates the plane by \( \theta \): its columns are \( \e_1 \) and \( \e_2 \) turned through \( \theta \). The second is a reflection, and the picture says in which mirror.

\begin{center}
\begin{tikzpicture}[scale=1.7, lab/.style={font=\small}]
    \draw[->, gray] (-1.4,0) -- (1.5,0);
    \draw[->, gray] (0,-0.9) -- (0,1.35);
    \draw[very thick] (-1.25,-0.583) -- (1.25,0.583) node[above right, lab] {$L$};
    \draw[->, very thick] (0,0) -- (80:1.2) node[above, lab] {$\v$};
    \draw[->, very thick] (0,0) -- (-30:1.2) node[below right, lab] {$\M_{\theta}\v$};
    \draw[dashed, thick] (80:1.2) -- (-30:1.2);
    \fill (25:0.688) circle (1.3pt) node[above left=1pt, lab] {$P_L\v$};
    \draw (0.3,0) arc (0:25:0.3);
    \node[lab] at (12:0.45) {$\theta/2$};
    \node[lab, align=center] at (0.1,-1.15) {$\M_{\theta}$ reflects in the line $L$ at angle $\theta/2$};
\end{tikzpicture}
\end{center}

::: {#thm-orthogonal-2x2}
[Classification of the Plane Isometries]

Let \( \A \in \Orth(2) \).

::: {.enumerate options="label=(\alph*)"}
1. If \( \det \A = 1 \), then \( \A = \R_{\theta} \) for a unique \( \theta \in [0, 2\pi) \).
2. If \( \det \A = -1 \), then \( \A = \M_{\theta} \) for a unique \( \theta \in [0, 2\pi) \). In this case \( \A^2 = \I \), the eigenvalues of \( \A \) are \( 1 \) and \( -1 \), and \( \A \) is the reflection in the line \( L = \Span\bigl((\cos\tfrac\theta2, \sin\tfrac\theta2)\bigr) \): it fixes \( L \) pointwise and negates \( L^{\perp} \).
:::

Consequently \( \Orth(2) = \{\R_{\theta}\} \cup \{\M_{\theta}\} \), and \( \SO(2) = \{\R_{\theta} : \theta \in [0, 2\pi)\} \).
:::

::: {.idea}
Condition (f) of @thm-isometry-characterizations says the two columns are orthonormal. A unit vector of \( \nR^2 \) is \( (\cos\theta, \sin\theta) \) for exactly one \( \theta \in [0, 2\pi) \), and there are exactly two unit vectors orthogonal to it. So there are only two candidates once the first column is chosen, and the determinant tells them apart. The geometric description of \( \M_{\theta} \) is then a two-line verification: guess the fixed vector from the picture and check it.
:::

::: {.proof}
Write \( \A = \begin{pmatrix} a & c \\ b & d \end{pmatrix} \in \Orth(2) \). By @thm-isometry-characterizations (f), the columns are orthonormal: \( a^2 + b^2 = 1 \), \( c^2 + d^2 = 1 \) and \( ac + bd = 0 \). Since \( (a, b) \) is a unit vector of \( \nR^2 \), there is a unique \( \theta \in [0, 2\pi) \) with \( a = \cos\theta \) and \( b = \sin\theta \). The vectors orthogonal to \( (a, b) \) form a line, spanned by \( (-b, a) \), which is already a unit vector; so the unit vectors on that line are \( \pm(-b, a) \), and \( (c, d) = \pm(-\sin\theta, \cos\theta) \). The two choices give
\[
\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} = \R_{\theta}
\quad\text{and}\quad
\begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix} = \M_{\theta},
\]
with determinants \( \cos^2\theta + \sin^2\theta = 1 \) and \( -\cos^2\theta - \sin^2\theta = -1 \). This proves (a) and the first sentence of (b), and uniqueness of \( \theta \) in both cases, since \( \theta \) is already determined by the first column.

For the rest of (b), put \( \u = (\cos\tfrac\theta2, \sin\tfrac\theta2) \) and \( \w = (-\sin\tfrac\theta2, \cos\tfrac\theta2) \), two orthogonal unit vectors. Writing \( \theta = \tfrac\theta2 + \tfrac\theta2 \) and using the subtraction formulas for cosine and sine,
\[
\M_{\theta}\u = \begin{pmatrix} \cos\theta\cos\tfrac\theta2 + \sin\theta\sin\tfrac\theta2 \\ \sin\theta\cos\tfrac\theta2 - \cos\theta\sin\tfrac\theta2 \end{pmatrix}
= \begin{pmatrix} \cos\tfrac\theta2 \\ \sin\tfrac\theta2 \end{pmatrix} = \u ,
\]
\[
\M_{\theta}\w = \begin{pmatrix} -\cos\theta\sin\tfrac\theta2 + \sin\theta\cos\tfrac\theta2 \\ -\sin\theta\sin\tfrac\theta2 - \cos\theta\cos\tfrac\theta2 \end{pmatrix}
= \begin{pmatrix} \sin\tfrac\theta2 \\ -\cos\tfrac\theta2 \end{pmatrix} = -\w .
\]
So \( (\u, \w) \) is an orthonormal basis of eigenvectors with eigenvalues \( 1 \) and \( -1 \), and \( \M_{\theta}^2 \) fixes both of them, hence \( \M_{\theta}^2 = \I \). Since \( L = \Span(\u) \), we have \( L^{\perp} = \Span(\w) \), because \( \w \perp \u \) and \( \dim L^{\perp} = 1 \) (@thm-orthogonal-decomposition (c)), so \( \M_{\theta} \) fixes \( L \) pointwise and negates \( L^{\perp} \), which is the description of a reflection. This proves the theorem.
:::

So \( \SO(2) \) is the circle of rotations, and the other half of \( \Orth(2) \) is the circle of reflections. Multiplying two rotations adds the angles, \( \R_{\alpha}\R_{\beta} = \R_{\alpha + \beta} \), so \( \SO(2) \) is abelian; @exr-isometries-and-unitary-maps-c3 shows what happens when two reflections are multiplied.

::: {#exm-plane-isometry-classified}
[Naming Two Plane Isometries]

Classify each of the following as a rotation or a reflection, and give the angle or the mirror line.

::: {.enumerate options="label=(\alph*)"}
1. \( \A = \tfrac12\begin{pmatrix} 1 & -\sqrt3 \\ \sqrt3 & 1 \end{pmatrix} \).
2. \( \B = \tfrac15\begin{pmatrix} 3 & 4 \\ 4 & -3 \end{pmatrix} \).
:::
:::

::: {.solution}
(a) The columns \( \tfrac12(1, \sqrt3) \) and \( \tfrac12(-\sqrt3, 1) \) have norm \( \tfrac12\sqrt{1 + 3} = 1 \) and inner product \( \tfrac14(-\sqrt3 + \sqrt3) = 0 \), so \( \A \in \Orth(2) \). Its determinant is \( \tfrac14(1 + 3) = 1 \), so \( \A = \R_{\theta} \) with \( \cos\theta = \tfrac12 \) and \( \sin\theta = \tfrac{\sqrt3}{2} \): rotation by \( \theta = \pi/3 \).

(b) The columns \( \tfrac15(3, 4) \) and \( \tfrac15(4, -3) \) are orthonormal, and \( \det \B = \tfrac1{25}(-9 - 16) = -1 \), so \( \B = \M_{\theta} \) with \( \cos\theta = \tfrac35 \) and \( \sin\theta = \tfrac45 \). The mirror is \( L = \Span\bigl((\cos\tfrac\theta2, \sin\tfrac\theta2)\bigr) \), and rather than halve the angle we find the fixed line directly: \( \B\x = \x \) reads \( 3x_1 + 4x_2 = 5x_1 \), that is \( x_1 = 2x_2 \). So \( L = \Span\bigl((2, 1)\bigr) \). Check: \( \B(2, 1) = \tfrac15(6 + 4, 8 - 3) = (2, 1) \), and \( \B(-1, 2) = \tfrac15(-3 + 8, -4 - 6) = (1, -2) = -(-1, 2) \), as a reflection must do to \( L^{\perp} \).
:::

## Rotations of space

In dimension \( 3 \) the answer is the one physics assumes: every orientation-preserving isometry of \( \nR^3 \) is a rotation about a line. The proof is where Chapter 8 is needed, for one reason only: to produce an eigenvector.

::: {#thm-so3-rotation}
[Every Element of SO(3) Is a Rotation]

Let \( \A \in \SO(3) \). Then there is a unit vector \( \u \in \nR^3 \) with \( \A\u = \u \), and an orthonormal basis \( \sB = (\u, \w_1, \w_2) \) of \( \nR^3 \) in which
\[
\mtx{T_{\A}}{\sB}{\sB} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{pmatrix}
\]
for some \( \theta \). That is, \( \A \) fixes the **axis** \( \Span(\u) \) and rotates the plane \( \Span(\u)^{\perp} \) by \( \theta \). Moreover \( \tr \A = 1 + 2\cos\theta \).
:::

::: {.idea}
Three steps. ① Get a real eigenvalue: the characteristic polynomial is real of degree \( 3 \), and an odd-degree real polynomial has a real root. ② That eigenvalue is \( \pm1 \), since \( T_{\A} \) is an isometry. ③ Split off the eigenline: its orthogonal complement is invariant, the restriction there lies in \( \Orth(2) \), and @thm-orthogonal-2x2 finishes. If the eigenvalue was \( -1 \) the restriction has determinant \( -1 \), so it is a reflection and supplies a \( +1 \) eigenvector inside the plane; feed that back into step ③.
:::

::: {.proof}
Write \( T = T_{\A} \), an isometry of \( \nR^3 \) by @thm-isometry-characterizations.

**Step 1: a real eigenvalue exists.** By @thm-charpoly-coefficients, \( p_{\A} \in \nR[x] \) is monic of degree \( 3 \), which is odd, so \( p_{\A} \) has a real root \( \lambda \) by @cor-odd-degree-real-root, and \( \lambda \) is an eigenvalue of \( \A \) by @thm-eigenvalue-characterizations. By @prp-isometry-eigenvalues-modulus-one, \( \lambda = 1 \) or \( \lambda = -1 \). Fix a unit eigenvector \( \u_0 \) for \( \lambda \), possible after dividing by its norm.

**Step 2: the orthogonal complement of an invariant line is invariant.**

::: {.claim}
If \( U \subseteq \nR^3 \) is a subspace with \( T(U) \subseteq U \), then \( T(U^{\perp}) \subseteq U^{\perp} \).

::: {.proof}
\( T|_U \colon U \to U \) is injective, because \( T \) is, so it is surjective by @thm-invertible-operator-tfae applied on the finite-dimensional space \( U \). Let \( \w \in U^{\perp} \) and \( \u \in U \). Write \( \u = T\u' \) with \( \u' \in U \). Then \( \inner{T\w}{\u} = \inner{T\w}{T\u'} = \inner{\w}{\u'} = 0 \), the middle step by @thm-isometry-characterizations (b) and the last because \( \u' \in U \). So \( T\w \in U^{\perp} \).
:::
:::

**Step 3: reduce to the plane.** Put \( U = \Span(\u_0) \), which is \( T \)-invariant. By the claim, \( P \coloneqq U^{\perp} \) is \( T \)-invariant, and \( \dim P = 2 \) by @thm-orthogonal-decomposition (c). Choose an orthonormal basis \( (\w_1, \w_2) \) of \( P \) (@thm-gram-schmidt); then \( \sB_0 = (\u_0, \w_1, \w_2) \) is an orthonormal basis of \( \nR^3 \), and in it
\[
\mtx{T}{\sB_0}{\sB_0} = \begin{pmatrix} \lambda & 0 & 0 \\ 0 & c_{11} & c_{12} \\ 0 & c_{21} & c_{22} \end{pmatrix},
\qquad \C \coloneqq \begin{pmatrix} c_{11} & c_{12} \\ c_{21} & c_{22} \end{pmatrix} ,
\]
the first column because \( T\u_0 = \lambda\u_0 \), and the two zeros in the first row because \( T\w_1, T\w_2 \in P \) have no \( \u_0 \)-component. This matrix is orthogonal, being the matrix of an isometry in orthonormal bases (@thm-isometry-characterizations (f)), so its second and third columns are orthonormal, which says \( \C\tp\C = \I_2 \) and \( \C \in \Orth(2) \); and \( \C \) is the matrix of \( T|_P \) in the basis \( (\w_1, \w_2) \). Expanding the determinant along the first column, and using that similar matrices have equal determinants (@cor-det-similarity-invariant, with @thm-similar-iff-same-operator (a)), \( 1 = \det \A = \lambda\det \C \), so \( \det \C = \lambda \).

*Case \( \lambda = 1 \).* Then \( \det \C = 1 \), so \( \C = \R_{\theta} \) for some \( \theta \) by @thm-orthogonal-2x2 (a), and \( \sB = \sB_0 \) and \( \u = \u_0 \) are as required.

*Case \( \lambda = -1 \).* Then \( \det \C = -1 \), so by @thm-orthogonal-2x2 (b) the restriction \( T|_P \) is a reflection of the plane \( P \) and has \( 1 \) as an eigenvalue. Let \( \u \in P \) be a unit eigenvector for \( 1 \), so \( T\u = \u \). Now rerun Steps 2 and 3 with \( \u \) in place of \( \u_0 \). Because \( \u \) was chosen with \( T\u = \u \), the eigenvalue this time is \( 1 \), so the rerun lands in the previous case and cannot return here.

Finally, \( \A \) and \( \mtx{T}{\sB}{\sB} \) are matrices of the same operator, hence similar (@thm-similar-iff-same-operator (a)), and similar matrices have equal traces (@thm-trace-similarity-invariant), so \( \tr \A = 1 + 2\cos\theta \). This proves the theorem.
:::

The angle is determined by \( \A \) up to sign, since reversing the order of \( \w_1, \w_2 \) replaces \( \theta \) by \( -\theta \); the trace formula \( \cos\theta = \tfrac12(\tr \A - 1) \) gives \( \lvert\theta\rvert \) with no computation at all. This settles \( \Orth(3) \) as well: if \( \det \A = -1 \) then \( -\A \in \SO(3) \), so \( \A \) is a rotation composed with the antipodal map.

::: {#exm-so3-axis-angle}
[Axis and Angle of a Rotation]

Let \( \A = \tfrac13\begin{pmatrix} 2 & -2 & 1 \\ 1 & 2 & 2 \\ -2 & -1 & 2 \end{pmatrix} \). Verify that \( \A \in \SO(3) \) and find its axis and angle.
:::

::: {.solution}
*Orthogonality.* The three columns are \( \tfrac13(2, 1, -2) \), \( \tfrac13(-2, 2, -1) \) and \( \tfrac13(1, 2, 2) \). Their squared norms are \( \tfrac19(4 + 1 + 4) = 1 \), \( \tfrac19(4 + 4 + 1) = 1 \) and \( \tfrac19(1 + 4 + 4) = 1 \), and their pairwise inner products are \( \tfrac19(-4 + 2 + 2) = 0 \), \( \tfrac19(2 + 2 - 4) = 0 \) and \( \tfrac19(-2 + 4 - 2) = 0 \). So the columns are orthonormal and \( \A \in \Orth(3) \) by @thm-isometry-characterizations (f).

*Determinant.* Expanding along the first row, \( 27\det \A = 2(4 + 2) - (-2)(2 + 4) + 1(-1 + 4) = 12 + 12 + 3 = 27 \), so \( \det \A = 1 \) and \( \A \in \SO(3) \).

*Axis.* Solve \( \A\u = \u \), that is \( (3\I - 3\A)\u = \0 \):
\[
\begin{pmatrix} 1 & 2 & -1 \\ -1 & 1 & -2 \\ 2 & 1 & 1 \end{pmatrix}\u = \0 .
\]
Adding row one to row two gives \( 3u_2 - 3u_3 = 0 \), so \( u_2 = u_3 \); then row one gives \( u_1 = -u_2 \). The axis is \( \Span\bigl((-1, 1, 1)\bigr) \), and indeed \( \A(-1, 1, 1) = \tfrac13(-2 - 2 + 1, -1 + 2 + 2, 2 - 1 + 2) = (-1, 1, 1) \).

*Angle.* \( \tr \A = \tfrac13(2 + 2 + 2) = 2 \), so \( \cos\theta = \tfrac12(2 - 1) = \tfrac12 \) and \( \lvert\theta\rvert = \pi/3 \). The map is a rotation by \( 60^{\circ} \) about the line through \( (-1, 1, 1) \).
:::

::: {.check}
A matrix \( \A \in \SO(3) \) has \( \tr \A = -1 \). What is its angle, and what is \( \A^2 \)?
:::

::: {.solution}
\( \cos\theta = \tfrac12(-1 - 1) = -1 \), so \( \theta = \pi \): a half-turn about the axis. Then \( \A^2 \) is the rotation by \( 2\pi \) about the same axis, which is \( \I_3 \). (In the basis of @thm-so3-rotation the matrix is \( \diag(1, -1, -1) \), whose square is \( \I_3 \).)
:::

## Rigid motions

We assumed linearity from the start. It is worth knowing that we did not have to: for maps of \( \nR^n \) that fix the origin, preserving distance forces linearity.

::: {#thm-rigid-motion-linear}
[Distance-Preserving Maps Are Affine]

Let \( f \colon \nR^n \to \nR^n \) be any function, not assumed linear, with
\[
\norm{f(\x) - f(\y)} = \norm{\x - \y} \qquad \text{for all } \x, \y \in \nR^n .
\]

::: {.enumerate options="label=(\alph*)"}
1. If \( f(\0) = \0 \), then \( f \) is linear and orthogonal.
2. In general, \( f(\x) = \A\x + \b \) for a unique \( \A \in \Orth(n) \) and a unique \( \b \in \nR^n \).
:::
:::

::: {.idea}
Setting \( \y = \0 \) turns the hypothesis into "preserves norms", and expanding the squared distance then turns it into "preserves inner products" without any polarization at all. Once inner products are preserved, \( f \) sends the standard basis to an orthonormal basis, and @thm-orthonormal-coordinates writes \( f(\x) \) as an explicit linear expression in the coordinates of \( \x \). Part (b) is part (a) applied to \( \x \mapsto f(\x) - f(\0) \).
:::

::: {.proof}
(a) Assume \( f(\0) = \0 \). Taking \( \y = \0 \) gives \( \norm{f(\x)} = \norm{\x} \) for all \( \x \). Expanding both sides of the hypothesis with @thm-norm-properties (c),
\[
\norm{f(\x)}^2 - 2\inner{f(\x)}{f(\y)} + \norm{f(\y)}^2 = \norm{\x}^2 - 2\inner{\x}{\y} + \norm{\y}^2 ,
\]
and the four outer terms cancel in pairs, leaving
\[
\inner{f(\x)}{f(\y)} = \inner{\x}{\y} \qquad \text{for all } \x, \y . \tag{$\ast$}
\]
Put \( \f_i \coloneqq f(\e_i) \). By \( (\ast) \), \( \inner{\f_i}{\f_j} = \inner{\e_i}{\e_j} = \delta_{ij} \), so \( (\f_1, \dots, \f_n) \) is an orthonormal list of \( n \) vectors in \( \nR^n \), hence an orthonormal basis (it is independent by @thm-orthogonal-independent and has \( n = \dim \nR^n \) elements). Now let \( \x = (x_1, \dots, x_n) \) be arbitrary. By @thm-orthonormal-coordinates applied to the basis \( (\f_1, \dots, \f_n) \), and then by \( (\ast) \),
\[
f(\x) = \sum_{i=1}^{n} \inner{f(\x)}{\f_i}\,\f_i = \sum_{i=1}^{n} \inner{f(\x)}{f(\e_i)}\,\f_i = \sum_{i=1}^{n} \inner{\x}{\e_i}\,\f_i = \sum_{i=1}^{n} x_i\,\f_i .
\]
The right-hand side is linear in \( \x \), so \( f \) is linear; and it preserves norms, so it is an isometry, hence orthogonal by @def-unitary-orthogonal, since it maps \( \nR^n \) to \( \nR^n \).

(b) Put \( \b \coloneqq f(\0) \) and \( g(\x) \coloneqq f(\x) - \b \). Then \( g \) preserves distances, since the translation cancels, and \( g(\0) = \0 \); by (a), \( g \) is orthogonal, say \( g(\x) = \A\x \) with \( \A \in \Orth(n) \), and \( f(\x) = \A\x + \b \). For uniqueness, evaluating at \( \0 \) recovers \( \b \), and then \( \A\x = f(\x) - \b \) determines \( \A \). This proves the theorem.
:::

So the rigid motions of \( \nR^n \) are exactly the maps "rotate or reflect, then translate", and the linear ones are exactly the orthogonal maps. That is the sense in which \( \Orth(n) \) is the symmetry group of Euclidean geometry, and it is why the same group reappears whenever a problem has a distance in it.

## Exercises

### A. Check your understanding

::: {#exr-isometries-and-unitary-maps-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define an isometry \( T \in \cL(V, W) \), and state two conditions equivalent to it.
2. What must be checked about a square matrix \( \A \) to decide whether it is unitary? State the check in terms of its columns.
3. True or false: every isometry is invertible. Justify your answer.
4. True or false: if \( \det \A = 1 \) for \( \A \in \Orth(n) \), then \( \A \) fixes a non-zero vector. Justify your answer.
5. Give the two families of matrices making up \( \Orth(2) \), and say how the determinant distinguishes them.
6. An operator \( T \) on a complex inner product space is unitary. Why must every eigenvalue of \( T \) lie on the unit circle?
:::
:::

::: {.solution}
(a) \( \norm{T\v} = \norm{\v} \) for every \( \v \in V \) (@def-isometry). Equivalent: \( \inner{T\u}{T\v} = \inner{\u}{\v} \) for all \( \u, \v \); and \( T^{*}T = \id_V \) (@thm-isometry-characterizations).

(b) That its columns are orthonormal in \( F^n \), that is \( \A^{*}\A = \I_n \) (@thm-isometry-characterizations (f)). For a square matrix this already gives \( \A\A^{*} = \I_n \).

(c) False. \( T \colon \nR^2 \to \nR^3 \), \( T(x_1, x_2) = (x_1, x_2, 0) \), is an isometry and is not surjective (@exm-isometries (a)). An isometry is always injective, and it is invertible exactly when \( \dim W = \dim V \).

(d) False for even \( n \): \( -\I_4 \in \SO(4) \) has determinant \( 1 \) and fixes only \( \0 \). It is true for odd \( n \), though not by the argument of @thm-so3-rotation, which uses the \( \Orth(2) \) classification of a 2-dimensional complement. The general reason is a count: the non-real eigenvalues of a real \( \A \) come in conjugate pairs \( \lambda, \conj\lambda \) with \( \lambda\conj\lambda = \lvert\lambda\rvert^2 = 1 \) for an isometry, so they contribute \( 1 \) to the determinant and an even number to the count. With \( n \) odd, an odd number of eigenvalues are real, each \( \pm 1 \), and their product is \( \det \A = 1 \); an odd number of factors \( \pm 1 \) with product \( 1 \) cannot all be \( -1 \), so \( 1 \) is an eigenvalue and some non-zero vector is fixed.

(e) The rotations \( \R_{\theta} \), with determinant \( 1 \), and the reflections \( \M_{\theta} \), with determinant \( -1 \) (@thm-orthogonal-2x2).

(f) A unitary operator is an isometry, so @prp-isometry-eigenvalues-modulus-one applies: \( \lvert\lambda\rvert = 1 \).
:::

### B. Practice

::: {#exr-isometries-and-unitary-maps-b1}
[B1: Determine which are unitary]

Determine which of the following matrices are orthogonal or unitary. Justify your answer; for those that are not, name the failing condition.

::: {.enumerate options="label=(\alph*)"}
1. \( \tfrac13\begin{pmatrix} 2 & -2 & 1 \\ 1 & 2 & 2 \\ -2 & -1 & 2 \end{pmatrix} \) over \( \nR \).
2. \( \tfrac1{\sqrt2}\begin{pmatrix} 1 & i \\ i & 1 \end{pmatrix} \) over \( \nC \).
3. \( \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \) over \( \nR \).
4. \( \tfrac15\begin{pmatrix} 3 & 4 \\ 4 & 3 \end{pmatrix} \) over \( \nR \).
:::
:::

::: {.solution}
(a) Orthogonal, as computed in @exm-so3-axis-angle: the three columns are orthonormal.

(b) Unitary. The columns are \( \tfrac1{\sqrt2}(1, i) \) and \( \tfrac1{\sqrt2}(i, 1) \), of norm \( \tfrac1{\sqrt2}\sqrt{1 + 1} = 1 \), and their inner product is
\[
\tfrac12\bigl(1 \cdot \conj{i} + i \cdot \conj{1}\bigr) = \tfrac12(-i + i) = 0 .
\]
So \( \A^{*}\A = \I_2 \). (It is unitary but not orthogonal, since it is not real.)

(c) Not orthogonal. The second column \( (1, 1) \) has norm \( \sqrt2 \neq 1 \), so the columns are not orthonormal. Equivalently, the map stretches \( \e_2 \).

(d) Not orthogonal. Both columns are unit vectors, \( \tfrac15(3, 4) \) and \( \tfrac15(4, 3) \), but their inner product is \( \tfrac1{25}(12 + 12) = \tfrac{24}{25} \neq 0 \). Unit columns are not enough; they must also be orthogonal. (Its determinant is \( \tfrac1{25}(9 - 16) = -\tfrac7{25} \), neither \( 1 \) nor \( -1 \), which confirms it by @prp-orthogonal-group-properties.)
:::

::: {#exr-isometries-and-unitary-maps-b2}
[B2: Name the plane isometry]

Each of the following lies in \( \Orth(2) \). Decide whether it is a rotation or a reflection, and give the angle of rotation or the mirror line.

::: {.enumerate options="label=(\alph*)"}
1. \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \).
2. \( \tfrac1{\sqrt2}\begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix} \).
3. \( \tfrac1{13}\begin{pmatrix} 5 & 12 \\ 12 & -5 \end{pmatrix} \).
:::
:::

::: {.solution}
(a) Determinant \( -1 \), so a reflection. \( \A\x = \x \) reads \( x_2 = x_1 \), so the mirror is \( L = \Span\bigl((1, 1)\bigr) \), the line \( x_2 = x_1 \). Check: \( \A(1, -1) = (-1, 1) = -(1, -1) \).

(b) Determinant \( \tfrac12(1 + 1) = 1 \), so a rotation \( \R_{\theta} \). Comparing with \( \R_{\theta} \), \( \cos\theta = \tfrac1{\sqrt2} \) and \( \sin\theta = -\tfrac1{\sqrt2} \), so \( \theta = -\pi/4 \): a clockwise half of a right angle.

(c) Determinant \( \tfrac1{169}(-25 - 144) = -1 \), so a reflection. \( \A\x = \x \) reads \( 5x_1 + 12x_2 = 13x_1 \), that is \( 3x_2 = 2x_1 \), so \( L = \Span\bigl((3, 2)\bigr) \). Check: \( \A(3, 2) = \tfrac1{13}(15 + 24, 36 - 10) = (3, 2) \).
:::

::: {#exr-isometries-and-unitary-maps-b3}
[B3: Permutations are orthogonal]

Let \( \sigma \in S_n \) and let \( \P_{\sigma} \in M_n(\nR) \) be its permutation matrix (@def-permutation-matrix), whose \( j \)-th column is \( \e_{\sigma(j)} \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \P_{\sigma} \in \Orth(n) \).
2. Deduce that \( \det \P_{\sigma} = \pm1 \), and identify the sign.
3. Show that \( \P_{\sigma}^{-1} = \P_{\sigma}\tp = \P_{\sigma^{-1}} \).
:::
:::

::: {.solution}
(a) Column \( j \) of \( \P_{\sigma} \) is \( \e_{\sigma(j)} \), by @def-permutation-matrix. So each column is a unit vector, and for \( i \neq j \) the columns \( \e_{\sigma(i)} \) and \( \e_{\sigma(j)} \) are distinct standard basis vectors, because \( \sigma \) is injective, hence orthogonal. By @thm-isometry-characterizations (f), \( \P_{\sigma} \in \Orth(n) \).

(b) By @prp-orthogonal-group-properties (b), \( \det \P_{\sigma} = \pm1 \). The sign is \( \sgn(\sigma) \): permuting the columns of \( \I_n \) by \( \sigma \) multiplies the determinant by \( \sgn(\sigma) \) (@thm-alternating-properties), and \( \det \I_n = 1 \).

(c) \( \P_{\sigma}^{-1} = \P_{\sigma}\tp \) holds because \( \P_{\sigma} \) is orthogonal, by (a). For the second equality, \( (\P_{\sigma})_{ij} = 1 \) exactly when \( i = \sigma(j) \), so \( (\P_{\sigma}\tp)_{ij} = (\P_{\sigma})_{ji} = 1 \) exactly when \( j = \sigma(i) \), that is when \( i = \sigma^{-1}(j) \); and that is the defining condition for \( (\P_{\sigma^{-1}})_{ij} = 1 \).
:::

### C. Going deeper

::: {#exr-isometries-and-unitary-maps-c1}
[C1: Determinant as a homomorphism]

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \det \colon \Orth(n) \to \{1, -1\} \) is a surjective group homomorphism with kernel \( \SO(n) \), and deduce that exactly half of \( \Orth(n) \) has determinant \( -1 \), in the sense that \( \Orth(n) \) is the disjoint union of \( \SO(n) \) and one coset \( \A_0\SO(n) \).
2. Prove that \( \det \colon \Unit(n) \to \{ z \in \nC : \lvert z\rvert = 1 \} \) is a surjective group homomorphism.
3. Describe \( \Orth(1) \) and \( \Unit(1) \) completely.
:::
:::

::: {.solution}
(a) \( \det \) is multiplicative (@thm-det-multiplicative) and takes only the values \( \pm1 \) on \( \Orth(n) \) (@prp-orthogonal-group-properties (b)), so it is a homomorphism into \( \{1, -1\} \). It is surjective: \( \det \I_n = 1 \), and \( \A_0 \coloneqq \diag(-1, 1, \dots, 1) \) is orthogonal, since its columns are \( \pm\e_i \), with \( \det \A_0 = -1 \). Its kernel is \( \{\A : \det \A = 1\} = \SO(n) \) by definition. If \( \det \A = -1 \) then \( \det(\A_0^{-1}\A) = 1 \), so \( \A \in \A_0\SO(n) \); and no matrix has both determinants, so the union is disjoint.

(b) Multiplicativity again, and \( \lvert\det \A\rvert = 1 \) on \( \Unit(n) \) by @prp-orthogonal-group-properties (b). For surjectivity, given \( z \) with \( \lvert z\rvert = 1 \), the matrix \( \diag(z, 1, \dots, 1) \) has orthonormal columns, hence lies in \( \Unit(n) \), and its determinant is \( z \) (@thm-det-triangular).

(c) A \( 1 \times 1 \) matrix \( (a) \) satisfies \( \conj{a}a = 1 \) exactly when \( \lvert a\rvert = 1 \). So \( \Unit(1) \) is the unit circle of \( \nC \) and \( \Orth(1) = \{(1), (-1)\} \). Consistently, \( \SO(1) = \{(1)\} \) is trivial.
:::

::: {#exr-isometries-and-unitary-maps-c2}
[C2: Linearity is a hypothesis, not a consequence]

::: {.enumerate options="label=(\alph*)"}
1. Let \( c \colon \nC \to \nC \) be \( c(z) = \conj{z} \), where \( \nC \) carries \( \inner{z}{w} = z\conj{w} \). Show that \( \norm{c(z)} = \norm{z} \) for every \( z \), that \( c \) is not linear over \( \nC \), and that \( c \) does not preserve the inner product. Which step of @thm-isometry-characterizations fails?
2. Let \( V \) be a **complex** inner product space and let \( T \in \cL(V) \) satisfy \( \inner{T\v}{\v} = 0 \) for every \( \v \in V \). Prove that \( T = 0 \).
3. Show that (b) fails over \( \nR \) by exhibiting a non-zero \( T \in \cL(\nR^2) \) with \( \inner{T\v}{\v} = 0 \) for all \( \v \).
:::

*Hint for (b): apply the hypothesis to \( \v = \u + \w \) and to \( \v = \u + i\w \).*
:::

::: {.solution}
(a) \( \norm{c(z)} = \lvert\conj{z}\rvert = \lvert z\rvert = \norm{z} \). But \( c(iz) = \conj{iz} = -i\conj{z} = -ic(z) \neq ic(z) \) unless \( z = 0 \), so \( c \) is not \( \nC \)-linear. And \( \inner{c(1)}{c(i)} = \inner{1}{-i} = 1 \cdot \conj{-i} = i \), while \( \inner{1}{i} = -i \). The proof of (a) \( \Rightarrow \) (b) in @thm-isometry-characterizations uses \( T(\u + i^k\v) = T\u + i^kT\v \), which is exactly what \( c \) does not satisfy.

(b) Let \( \u, \w \in V \). Applying the hypothesis to \( \u + \w \) and expanding both slots,
\[
\begin{aligned}
0 = \inner{T(\u + \w)}{\u + \w}
  &= \inner{T\u}{\u} + \inner{T\u}{\w} + \inner{T\w}{\u} + \inner{T\w}{\w} \\
  &= \inner{T\u}{\w} + \inner{T\w}{\u} .
\end{aligned} \tag{1}
\]
Applying it to \( \u + i\w \), and using \( \inner{T\u}{i\w} = -i\inner{T\u}{\w} \), \( \inner{T(i\w)}{\u} = i\inner{T\w}{\u} \) and \( \inner{T(i\w)}{i\w} = i\conj{i}\inner{T\w}{\w} = 0 \),
\[
0 = -i\inner{T\u}{\w} + i\inner{T\w}{\u} .
\]
Multiplying by \( i \) gives
\[
\inner{T\u}{\w} - \inner{T\w}{\u} = 0 . \tag{2}
\]
Adding (1) and (2), \( 2\inner{T\u}{\w} = 0 \), so \( \inner{T\u}{\w} = 0 \) for all \( \u, \w \). Taking \( \w = T\u \) gives \( \norm{T\u}^2 = 0 \), so \( T\u = \0 \) for every \( \u \), that is \( T = 0 \).

(c) Let \( T \) be the rotation \( \R_{\pi/2} \), that is \( T(x_1, x_2) = (-x_2, x_1) \). Then \( \inner{T\x}{\x} = -x_2x_1 + x_1x_2 = 0 \) for every \( \x \), and \( T \neq 0 \). The complex proof breaks down because the second equation is unavailable: there is no \( i \) to substitute.
:::

::: {#exr-isometries-and-unitary-maps-c3}
[C3: Two reflections make a rotation]

Let \( \alpha, \beta \in \nR \) and let \( \M_{\alpha}, \M_{\beta} \in \Orth(2) \) be the reflections of @thm-orthogonal-2x2, in the lines \( L_{\alpha} \) and \( L_{\beta} \) at angles \( \alpha/2 \) and \( \beta/2 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \M_{\alpha}\M_{\beta} = \R_{\alpha - \beta} \).
2. Deduce that the composite of the reflections in two lines through the origin is the rotation by **twice** the angle from the second line to the first, and that every rotation of the plane is a product of two reflections.
3. Deduce that \( \Orth(2) \) is not abelian, by computing \( \M_{\beta}\M_{\alpha} \).
:::
:::

::: {.solution}
(a) Multiplying out,
\[
\M_{\alpha}\M_{\beta} = \begin{pmatrix} \cos\alpha & \sin\alpha \\ \sin\alpha & -\cos\alpha \end{pmatrix}\begin{pmatrix} \cos\beta & \sin\beta \\ \sin\beta & -\cos\beta \end{pmatrix}
= \begin{pmatrix} c & -s \\ s & c \end{pmatrix},
\]
where \( c = \cos\alpha\cos\beta + \sin\alpha\sin\beta = \cos(\alpha - \beta) \) and \( s = \sin\alpha\cos\beta - \cos\alpha\sin\beta = \sin(\alpha - \beta) \), by the subtraction formulas. The top-right entry is \( \cos\alpha\sin\beta - \sin\alpha\cos\beta = -\sin(\alpha - \beta) \), as displayed. So \( \M_{\alpha}\M_{\beta} = \R_{\alpha - \beta} \).

(b) The angle from \( L_{\beta} \) to \( L_{\alpha} \) is \( \tfrac\alpha2 - \tfrac\beta2 \), and (a) says the composite is the rotation by \( \alpha - \beta \), twice that. Conversely, given \( \theta \), choose \( \alpha = \theta \) and \( \beta = 0 \); then \( \R_{\theta} = \M_{\theta}\M_{0} \), a product of two reflections.

(c) By (a) with the roles exchanged, \( \M_{\beta}\M_{\alpha} = \R_{\beta - \alpha} = \R_{\alpha - \beta}^{-1} \). These two agree only when \( \R_{\alpha-\beta}^2 = \I \), that is when \( \alpha - \beta \) is a multiple of \( \pi \). Taking \( \alpha = \pi/2 \) and \( \beta = 0 \) gives \( \M_{\pi/2}\M_0 = \R_{\pi/2} \neq \R_{-\pi/2} = \M_0\M_{\pi/2} \), so \( \Orth(2) \) is not abelian.
:::
