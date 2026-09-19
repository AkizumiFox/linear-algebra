# Tensors in Quantum Mechanics

The chapter ends outside mathematics, and the arrangement is the one Chapter 13 used for Minkowski space and for the second derivative test: physics supplies a modeling assumption, the book quotes it and proves nothing about it, and everything after it is linear algebra. The assumption is that a composite quantum system is the tensor product of its parts. Two things follow. One is a phenomenon, **entanglement**, which turns out to be nothing but §02's observation that not every element of \( V \otimes W \) is a simple tensor. The other is a theorem, the **Schmidt decomposition**, which turns out to be Chapter 12's singular value decomposition wearing different notation. The second is the real payoff, and it is why this section closes Part IV: it joins the two halves of the book's later chapters at a single point.

## What is quoted and what is proved

Quantum mechanics, as a physical theory, is not derived here and cannot be. What we take from it is a short list of modeling conventions, stated once so that the reader can see exactly where the mathematics starts.

::: {.enumerate options="label=(Q\arabic*)"}
1. The states of a quantum system are the **unit vectors** of a complex inner product space \( V \), where two unit vectors differing by a scalar of modulus \( 1 \) describe the same state.
2. If a system \( A \) has state space \( V \) and a system \( B \) has state space \( W \), then the composite system "\( A \) together with \( B \)" has state space \( V \otimes W \).
3. If \( A \) is in the state \( \v \) and \( B \) is in the state \( \w \), then the composite is in the state \( \v \otimes \w \).
:::

None of (Q1)–(Q3) is a theorem, and this book does not argue for any of them. They are quoted exactly as Taylor's theorem was quoted in Chapter 13 §06 — as hypotheses that give the mathematics below something to stand on. Everything proved in this section is a statement about finite-dimensional complex inner product spaces, true whether or not (Q1)–(Q3) describe the world.

Two remarks make the list less arbitrary. First, \( \otimes \) rather than \( \oplus \) is visible in a dimension count: a spin has a two-dimensional state space, a **qubit**, and two spins together have a four-dimensional one, not a three-dimensional one. Of the two standard constructions, only \( \otimes \) produces the observed count, since \( \dim(V \otimes W) = \dim V \cdot \dim W \) by @thm-tensor-basis. Second, (Q3) very nearly forces (Q2): the assignment \( (\v, \w) \mapsto \text{(joint state)} \) is required to be bilinear, and by @def-tensor-product every bilinear map out of \( V \times W \) factors uniquely through \( V \otimes W \). The universal property is the precise statement that the joint state depends on the parts bilinearly and in no other way.

Genuine quantum mechanics uses infinite-dimensional spaces with a completeness condition. Everything below is finite-dimensional, which is where this book lives, and where qubits live too.

Before states can be unit vectors, \( V \otimes W \) needs an inner product. There is only one reasonable candidate, and it exists.

::: {#prp-tensor-inner-product}
[The Inner Product on a Tensor Product]

Let \( V \) and \( W \) be finite-dimensional inner product spaces over \( F = \nC \) (or over \( \nR \)). Then there is **exactly one** inner product on \( V \otimes W \) satisfying
\[
\inner{\v \otimes \w}{\v' \otimes \w'}
= \inner{\v}{\v'}\,\inner{\w}{\w'}
\]
for all \( \v, \v' \in V \) and \( \w, \w' \in W \). Moreover, if \( \sE \) and \( \sF \) are orthonormal bases of \( V \) and \( W \), then \( (\e_i \otimes \f_j) \) is an orthonormal basis of \( V \otimes W \).
:::

::: {.proof}
*Uniqueness.* The simple tensors span \( V \otimes W \) (@prp-simple-tensors-span), and an inner product is additive in the first slot and conjugate-additive in the second, so its values on all pairs of vectors are determined by its values on pairs of simple tensors.

*Existence.* Fix orthonormal bases \( \sE = (\e_1, \dots, \e_m) \) of \( V \) and \( \sF = (\f_1, \dots, \f_n) \) of \( W \), which exist by @thm-gram-schmidt. By @thm-tensor-basis the \( mn \) vectors \( \e_i \otimes \f_j \) form a basis of \( V \otimes W \), so the rule
\[
\Bigl\langle \sum_{i,j} c_{ij}\,\e_i \otimes \f_j ,\;
\sum_{i,j} d_{ij}\,\e_i \otimes \f_j \Bigr\rangle
\coloneqq \sum_{i,j} c_{ij}\conj{d_{ij}}
\]
is well defined; it is the standard inner product of coordinate vectors, hence satisfies (IP1)–(IP3) of @def-inner-product. To check the product formula, write \( \v = \sum_i a_i\e_i \) and \( \w = \sum_j b_j\f_j \). Bilinearity of \( \otimes \) gives \( \v \otimes \w = \sum_{i,j} a_ib_j\,\e_i\otimes\f_j \), and likewise for \( \v' \otimes \w' \), so
\[
\inner{\v \otimes \w}{\v' \otimes \w'}
= \sum_{i,j} a_ib_j\conj{a'_ib'_j}
= \Bigl(\sum_i a_i\conj{a'_i}\Bigr)\Bigl(\sum_j b_j\conj{b'_j}\Bigr),
\]
which is \( \inner{\v}{\v'}\inner{\w}{\w'} \) by @thm-orthonormal-coordinates. Finally, the product formula gives \( \inner{\e_i\otimes\f_j}{\e_k\otimes\f_l} = \delta_{ik}\delta_{jl} \) for **any** orthonormal \( \sE \) and \( \sF \), so the displayed construction did not depend on the pair chosen. This proves the proposition.
:::

## Entanglement is failure of simplicity

The whole phenomenon fits in the language the chapter already has. A state of the composite is a unit vector of \( V \otimes W \), and a state of the form \( \v \otimes \w \) is one in which each part has a state of its own. Section 02 proved that not every vector of a tensor product has that form; a composite state that does not describes a system whose parts have no separate states at all.

*A state is entangled when it is a vector of \( V \otimes W \) that is not a simple tensor.*

::: {#def-entangled}
[Product State, Entangled State]

Let \( V \) and \( W \) be finite-dimensional complex inner product spaces, and let \( \z \in V \otimes W \) be a unit vector. Then \( \z \) is a **product state**, also called **separable**, if
\[
\z = \v \otimes \w \quad\text{for some } \v \in V,\ \w \in W,
\]
and \( \z \) is **entangled** otherwise. The same words are used for any non-zero \( \z \in V \otimes W \), the unit-length condition playing no part in the distinction.
:::

Clause by clause. **Product state** is a synonym for "simple tensor", the term of §02; only the context is new. The definition is relative to the **splitting** \( V \otimes W \), not to the vector alone: "entangled" is a statement about a vector *and* a choice of two factors. And \( \v \) and \( \w \) need not be unit vectors, though they can be taken so: \( \norm{\v \otimes \w} = \norm{\v}\norm{\w} \) by @prp-tensor-inner-product, so rescaling one factor up and the other down costs nothing.

::: {#exm-bell-state}
[The Bell state]

In \( \nC^2 \otimes \nC^2 \), write \( \sE = (\e_1, \e_2) \) for the standard orthonormal basis of the first factor and \( \sF = (\f_1, \f_2) \) for the same basis regarded as sitting in the second factor, the two names being there only to keep the factors apart. Let
\[
\z_0 \coloneqq \tfrac{1}{\sqrt2}\bigl(\e_1 \otimes \f_1 + \e_2 \otimes \f_2\bigr).
\]
Show that \( \z_0 \) is a unit vector, and that it is entangled.
:::

::: {.solution}
By @prp-tensor-inner-product the four vectors \( \e_i \otimes \f_j \) are orthonormal, so \( \norm{\z_0}^2 = \tfrac12(1 + 1) = 1 \).

For entanglement there is nothing to prove that §02 has not already proved. Once the two bases are recognized as the same one, \( \e_1\otimes\f_1 + \e_2\otimes\f_2 \) is exactly the tensor of @exm-non-simple-tensor, and \( \z_0 \) is a non-zero multiple of it: if \( \z_0 = \v\otimes\w \) then \( \e_1\otimes\f_1 + \e_2\otimes\f_2 = (\sqrt2\,\v)\otimes\w \), which @exm-non-simple-tensor rules out. So \( \z_0 \) is entangled.
:::

The physical reading is one paragraph long, and the book stops there. Under (Q1)–(Q3), a composite in the state \( \z_0 \) is a pair of qubits of which two things are true at once: the pair has a completely specified state, and neither member has a state at all, since \( \z_0 \) is not of the form \( \v \otimes \w \). Nothing about the individual qubits is being suppressed; the postulates simply do not assign them states. That is what is meant by calling the two qubits entangled, and it is why the word attaches to a piece of linear algebra rather than to a measurement. Whether the postulates are true of the world is a question this book does not address.

::: {.warning}
**A sum of simple tensors can still be simple.** "Entangled" does not mean "written as a sum of more than one term". In \( \nC^2 \otimes \nC^2 \),
\[
\tfrac12\bigl(\e_1\otimes\f_1 + \e_1\otimes\f_2
 + \e_2\otimes\f_1 + \e_2\otimes\f_2\bigr)
= \tfrac{\e_1+\e_2}{\sqrt2} \otimes \tfrac{\f_1+\f_2}{\sqrt2},
\]
a four-term expression for a product state. Entanglement is a property of the **vector**, not of an expression for it, and deciding it needs an invariant. Supplying one is the job of the rest of this section.
:::

::: {.check}
Is \( \z = \tfrac{1}{\sqrt3}\bigl(\e_1\otimes\f_1 + \e_1\otimes\f_2 + \e_2\otimes\f_1\bigr) \) in \( \nC^2\otimes\nC^2 \) entangled?
:::

::: {.solution}
Yes. Suppose \( \z = \v \otimes \w \) with \( \v = a_1\e_1 + a_2\e_2 \) and \( \w = b_1\f_1 + b_2\f_2 \). Expanding, \( \v \otimes \w = \sum_{i,j} a_ib_j\,\e_i\otimes\f_j \), and the \( \e_i\otimes\f_j \) are a basis (@thm-tensor-basis), so comparing coefficients gives
\[
a_1b_1 = a_1b_2 = a_2b_1 = \tfrac{1}{\sqrt3},
\qquad a_2b_2 = 0 .
\]
Then \( (a_1b_1)(a_2b_2) = 0 \) while \( (a_1b_2)(a_2b_1) = \tfrac13 \); but both products equal \( a_1a_2b_1b_2 \). So no such \( \v, \w \) exist.
:::

## The Schmidt decomposition

The Quick check used a \( 2 \times 2 \) determinant on an array of coefficients, and that is a hint about where to look. Section 03 already said what the array is: by @thm-tensor-hom-iso a tensor **is** a linear map, and a linear map between finite-dimensional spaces is a matrix. Chapter 12 knows exactly one thing about an arbitrary matrix, and it knows it completely.

Write out the identification for the case at hand. Fix bases \( \sE = (\e_1, \dots, \e_m) \) of \( V \) and \( \sF = (\f_1, \dots, \f_n) \) of \( W \), and let \( (\varphi_1, \dots, \varphi_n) \) be the basis of \( W^{*} \) dual to \( \sF \) (@thm-dual-basis). The map
\[
V \times W \to \cL(W^{*}, V),
\qquad (\v, \w) \mapsto \bigl(\varphi \mapsto \varphi(\w)\,\v\bigr),
\]
is bilinear in \( (\v, \w) \), so by @def-tensor-product it induces a linear \( \Theta \colon V \otimes W \to \cL(W^{*}, V) \). It sends \( \e_i \otimes \f_j \) to the map \( \varphi_k \mapsto \delta_{jk}\e_i \), whose matrix from \( (\varphi_1, \dots, \varphi_n) \) to \( \sE \) is the matrix unit \( \E_{ij} \). The matrix units are a basis of \( M_{m \times n}(\nC) \) and taking the matrix of a map in fixed bases is an isomorphism (@thm-linear-maps-isomorphic-to-matrices), so \( \Theta \) carries a basis to a basis and is itself an isomorphism. It is @thm-tensor-hom-iso with the two factors in the other order and \( W \) identified with \( W^{**} \) (@thm-evaluation-natural), and for coordinate spaces it is §02's matrix model @thm-tensor-fn-matrices; the letter is shared for that reason. What matters below is the consequence: the matrix of \( \Theta(\z) \) is the array of coefficients of \( \z \) in the basis \( (\e_i \otimes \f_j) \).

::: {#thm-schmidt-decomposition}
[Schmidt Decomposition]

Let \( V \) and \( W \) be finite-dimensional complex inner product spaces of dimensions \( m \) and \( n \), and let \( \z \in V \otimes W \) be non-zero. Then there are an integer \( r \) with \( 1 \le r \le \min(m,n) \), real numbers
\[
\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_r > 0 ,
\]
an orthonormal list \( (\x_1, \dots, \x_r) \) in \( V \) and an orthonormal list \( (\y_1, \dots, \y_r) \) in \( W \) such that
\[
\z = \sum_{k=1}^{r} \sigma_k\,\x_k \otimes \y_k .
\]{#eq-schmidt}
Moreover \( r \) and the numbers \( \sigma_1, \dots, \sigma_r \) are determined by \( \z \): they do not depend on the lists chosen, nor on any basis. Finally \( \norm{\z}^2 = \sum_{k} \sigma_k^2 \), so \( \z \) is a unit vector exactly when \( \sum_k \sigma_k^2 = 1 \).
:::

::: {.idea}
The statement is the singular value decomposition of @thm-svd with the words changed, so the plan is to change the words back. ① Fix orthonormal bases on both sides; @thm-tensor-basis turns \( \z \) into a matrix \( \C \) of coefficients, which by the paragraph above is the matrix of the linear map \( \Theta(\z) \). ② Feed \( \C \) to the compact singular value decomposition, @thm-compact-svd, which over \( \nC \) still returns **real positive** numbers \( \sigma_k \) and two orthonormal lists of complex column vectors. ③ Read the column vectors back as vectors of \( V \) and \( W \); orthonormal columns become orthonormal vectors because coordinates in an orthonormal basis compute inner products. For uniqueness, run ③ backwards: any expression of the shape @eq-schmidt turns into a factorization \( \C = \X\D\Y\tp \) with \( \X, \Y \) having orthonormal columns, and then \( \C\C^{*} = \X\D^2\X^{*} \) hands over the \( \sigma_k^2 \) as the non-zero eigenvalues of a matrix built from \( \z \) alone.
:::

::: {.proof}
**Step 1: turn \( \z \) into a matrix.** Fix orthonormal bases \( \sE = (\e_1, \dots, \e_m) \) of \( V \) and \( \sF = (\f_1, \dots, \f_n) \) of \( W \) (@thm-gram-schmidt). By @thm-tensor-basis there are unique scalars \( c_{ij} \in \nC \) with \( \z = \sum_{i,j} c_{ij}\,\e_i \otimes \f_j \). Let \( \C \in M_{m \times n}(\nC) \) be the matrix with entries \( c_{ij} \); it is the matrix of the linear map \( \Theta(\z) \) described above, and it is non-zero because \( \z \) is.

**Step 2: decompose the matrix.** Put \( r = \rank\C \ge 1 \). By @thm-compact-svd there are orthonormal lists \( (\u_1, \dots, \u_r) \) in \( \nC^m \) and \( (\v_1, \dots, \v_r) \) in \( \nC^n \), and the non-zero singular values \( \sigma_1 \ge \dots \ge \sigma_r > 0 \) of \( \C \) (@def-singular-values), with
\[
\C = \sum_{k=1}^{r} \sigma_k\,\u_k\v_k^{*},
\qquad\text{that is}\qquad
c_{ij} = \sum_{k=1}^{r} \sigma_k (\u_k)_i \conj{(\v_k)_j} .
\]
The \( \sigma_k \) are real and positive even though \( \C \) is complex, since they are square roots of eigenvalues of the positive semidefinite matrix \( \C^{*}\C \). Also \( r = \rank\C \le \min(m,n) \).

**Step 3: read the columns back.** Set
\[
\begin{aligned}
\x_k &\coloneqq \sum_{i=1}^{m} (\u_k)_i\,\e_i \ \in V , \\
\y_k &\coloneqq \sum_{j=1}^{n} \conj{(\v_k)_j}\,\f_j \ \in W .
\end{aligned}
\]
Substituting the formula for \( c_{ij} \) into \( \z = \sum_{i,j} c_{ij}\,\e_i\otimes\f_j \) and interchanging the three finite sums, bilinearity of \( \otimes \) gives
\[
\z = \sum_{k=1}^{r}\sigma_k
\Bigl(\sum_i (\u_k)_i\e_i\Bigr) \otimes
\Bigl(\sum_j \conj{(\v_k)_j}\f_j\Bigr)
= \sum_{k=1}^{r}\sigma_k\,\x_k\otimes\y_k .
\]
Since \( \sE \) is orthonormal, @thm-orthonormal-coordinates gives
\[
\inner{\x_k}{\x_l} = \sum_i (\u_k)_i\conj{(\u_l)_i}
= \inner{\u_k}{\u_l} = \delta_{kl},
\]
and likewise, since \( \sF \) is orthonormal,
\[
\inner{\y_k}{\y_l} = \sum_j \conj{(\v_k)_j}(\v_l)_j
= \inner{\v_l}{\v_k} = \delta_{kl} .
\]
So both lists are orthonormal, and @eq-schmidt holds.

**Step 4: uniqueness.** Suppose \( \z = \sum_{k=1}^{s}\tau_k\,\x'_k\otimes\y'_k \) is **any** expression of the stated shape, with \( \tau_1 \ge \dots \ge \tau_s > 0 \) and both lists orthonormal. Keep the bases \( \sE, \sF \) and write \( \x'_k = \sum_i \xi_{ik}\e_i \) and \( \y'_k = \sum_j \eta_{jk}\f_j \). Let \( \X \in M_{m \times s}(\nC) \) have entries \( \xi_{ik} \) and \( \Y \in M_{n \times s}(\nC) \) have entries \( \eta_{jk} \). Orthonormality of the two lists says, by @thm-orthonormal-coordinates again, that the columns of \( \X \) and of \( \Y \) are orthonormal, that is
\[
\X^{*}\X = \I_s, \qquad \Y^{*}\Y = \I_s .
\]
Expanding the expression for \( \z \) in the basis \( (\e_i\otimes\f_j) \) and comparing with the unique coefficients \( c_{ij} \) of Step 1,
\[
c_{ij} = \sum_{k=1}^{s}\tau_k\,\xi_{ik}\eta_{jk},
\qquad\text{i.e.}\qquad
\C = \X\D\Y\tp ,
\]
where \( \D = \diag(\tau_1, \dots, \tau_s) \). Taking conjugate transposes and using \( \Y\tp\conj{\Y} = \conj{\Y^{*}\Y} = \I_s \),
\[
\C\C^{*} = \X\D\bigl(\Y\tp\conj{\Y}\bigr)\D\X^{*} = \X\D^2\X^{*} .
\]
Now read off the eigenvalues of \( \C\C^{*} \in M_m(\nC) \). For each \( k \), the \( k \)-th column \( \X\e_k \) satisfies
\[
\C\C^{*}(\X\e_k) = \X\D^2\X^{*}\X\e_k = \X\D^2\e_k = \tau_k^2\,(\X\e_k),
\]
and these \( s \) columns are orthonormal. If instead \( \z' \in \nC^m \) is orthogonal to every column of \( \X \) then \( \X^{*}\z' = \0 \), so \( \C\C^{*}\z' = \0 \). Since \( \nC^m = \col(\X) \oplus \col(\X)^{\perp} \) by @thm-orthogonal-decomposition, putting an orthonormal basis of \( \col(\X)^{\perp} \) beside the columns of \( \X \) produces an orthonormal basis of \( \nC^m \) consisting of eigenvectors of \( \C\C^{*} \). Hence the eigenvalue list of \( \C\C^{*} \), with multiplicity, is \( \tau_1^2, \dots, \tau_s^2 \) together with \( m - s \) zeros.

Every \( \tau_k^2 \) is positive, so \( s \) is the number of non-zero eigenvalues of \( \C\C^{*} \), and \( (\tau_1^2, \dots, \tau_s^2) \) is the list of those eigenvalues in decreasing order. Both are determined by \( \C \), which is determined by \( \z \) once \( \sE \) and \( \sF \) are fixed. So any two expressions of the shape @eq-schmidt have the same \( s \) and the same \( \tau_k \); in particular they agree with the \( r \) and \( \sigma_k \) of Steps 2 and 3, and since the statement "\( \z \) admits @eq-schmidt with these \( r, \sigma_k \)" mentions no basis, the numbers cannot depend on \( \sE \) and \( \sF \) either.

**Step 5: the norm.** By @prp-tensor-inner-product, \( \inner{\x_k\otimes\y_k}{\x_l\otimes\y_l} = \inner{\x_k}{\x_l}\inner{\y_k}{\y_l} = \delta_{kl} \), so the \( r \) vectors \( \x_k\otimes\y_k \) are orthonormal in \( V \otimes W \). By @thm-pythagoras, \( \norm{\z}^2 = \sum_k \sigma_k^2 \). This proves the theorem.
:::

::: {#def-schmidt-rank}
[Schmidt Coefficients, Schmidt Rank]

Let \( \z \in V \otimes W \) be non-zero. The numbers \( \sigma_1 \ge \dots \ge \sigma_r > 0 \) of @thm-schmidt-decomposition are the **Schmidt coefficients** of \( \z \), and the integer \( r \) is the **Schmidt rank** of \( \z \). By convention the Schmidt rank of \( \0 \) is \( 0 \).
:::

Both are well defined precisely because of Step 4, and the proof identifies them: the Schmidt coefficients are the non-zero singular values of the coefficient matrix of \( \z \) in any pair of orthonormal bases, and the Schmidt rank is the rank of that matrix. That is the invariant the warning above asked for, and it is also §02's: the smallest number of simple tensors summing to \( \z \) is the rank of \( \Theta(\z) \), and @thm-schmidt-decomposition now exhibits a shortest such sum, with its terms orthogonal on both sides at once.

::: {#cor-schmidt-rank-one-separable}
[Entanglement Is Schmidt Rank at Least Two]

A non-zero \( \z \in V \otimes W \) is a product state if and only if its Schmidt rank is \( 1 \). Hence a state is entangled exactly when its Schmidt rank is at least \( 2 \).
:::

::: {.proof}
\( (\Leftarrow) \) If \( r = 1 \) then \( \z = \sigma_1\x_1\otimes\y_1 = (\sigma_1\x_1)\otimes\y_1 \), a simple tensor.

\( (\Rightarrow) \) Suppose \( \z = \v\otimes\w \). Neither factor is \( \0 \), since \( \z \ne \0 \). Put \( \x_1 = \v/\norm{\v} \) and \( \y_1 = \w/\norm{\w} \), which is legitimate because \( \norm{\v}, \norm{\w} > 0 \). Then \( \z = \sigma_1\x_1\otimes\y_1 \) with \( \sigma_1 = \norm{\v}\norm{\w} > 0 \), and the one-term lists \( (\x_1) \), \( (\y_1) \) are orthonormal. This is an expression of the shape @eq-schmidt with one term, so the uniqueness clause of @thm-schmidt-decomposition gives \( r = 1 \).
:::

::: {.warning}
**The Schmidt coefficients are determined; the vectors are not.** For the Bell state \( \z_0 \) of @exm-bell-state the coefficient matrix is \( \tfrac{1}{\sqrt2}\I_2 \), whose singular values are \( \tfrac1{\sqrt2}, \tfrac1{\sqrt2} \). Repeated coefficients leave the lists free, exactly as a repeated eigenvalue of \( \A^{*}\A \) leaves \( \V \) free in @thm-singular-values-unique: for **every** orthonormal basis \( (\x_1, \x_2) \) of \( \nC^2 \) one has \( \z_0 = \tfrac1{\sqrt2}(\x_1\otimes\y_1 + \x_2\otimes\y_2) \) for a suitable orthonormal \( (\y_1, \y_2) \). Never speak of *the* Schmidt vectors; speak of *the* Schmidt coefficients.
:::

::: {#exm-schmidt-computed}
[A Schmidt decomposition in two by three]

In \( \nC^2 \otimes \nC^3 \), find the Schmidt decomposition, the Schmidt rank and the Schmidt coefficients of
\[
\z = \tfrac12\bigl(\e_1\otimes\f_1 + \e_1\otimes\f_3
 + \e_2\otimes\f_2 - \e_2\otimes\f_3\bigr),
\]
where \( \sE \) and \( \sF \) are the standard orthonormal bases.
:::

::: {.solution}
The coefficient matrix is
\[
\C = \tfrac12\begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & -1 \end{pmatrix}
\in M_{2 \times 3}(\nR) .
\]
This is half the matrix of @exm-svd-2x3, so by @exr-singular-value-decomposition-b4 (b) its singular values are half of those found there: \( \sigma_1 = \tfrac{\sqrt3}{2} \) and \( \sigma_2 = \tfrac12 \). Both are non-zero, so \( \rank\C = 2 \) and the Schmidt rank is \( 2 \); by @cor-schmidt-rank-one-separable, \( \z \) is entangled. As a check, \( \sigma_1^2 + \sigma_2^2 = \tfrac34 + \tfrac14 = 1 \), and indeed \( \norm{\z}^2 = 4 \cdot \tfrac14 = 1 \).

For the vectors, @thm-compact-svd asks for an orthonormal eigenbasis of the \( 3 \times 3 \) matrix \( \C^{*}\C \); as in @exm-svd-2x3 it is cheaper to work with the smaller \( \C\C\tp = \tfrac14\begin{psmallmatrix} 2 & -1 \\ -1 & 2\end{psmallmatrix} \), whose orthonormal eigenvectors are the left singular vectors \( \u_k \). They are \( \tfrac1{\sqrt2}(1,-1) \) for the eigenvalue \( \tfrac34 \) and \( \tfrac1{\sqrt2}(1,1) \) for \( \tfrac14 \). So \( \u_1 = \tfrac1{\sqrt2}(1,-1) \) and \( \u_2 = \tfrac1{\sqrt2}(1,1) \), and the relation \( \C^{*}\u_i = \sigma_i\v_i \) of @eq-singular-vector-pairing gives
\[
\v_1 = \tfrac{\C\tp\u_1}{\sigma_1} = \tfrac{1}{\sqrt6}(1,-1,2),
\qquad
\v_2 = \tfrac{\C\tp\u_2}{\sigma_2} = \tfrac{1}{\sqrt2}(1,1,0).
\]
All entries are real, so the conjugation in Step 3 of @thm-schmidt-decomposition does nothing here, and reading the columns back gives
\[
\begin{aligned}
\x_1 &= \tfrac{1}{\sqrt2}(\e_1 - \e_2), &
\y_1 &= \tfrac{1}{\sqrt6}(\f_1 - \f_2 + 2\f_3), \\
\x_2 &= \tfrac{1}{\sqrt2}(\e_1 + \e_2), &
\y_2 &= \tfrac{1}{\sqrt2}(\f_1 + \f_2),
\end{aligned}
\]
so that \( \z = \tfrac{\sqrt3}{2}\,\x_1\otimes\y_1 + \tfrac12\,\x_2\otimes\y_2 \). Multiplying out recovers \( \z \): the two terms are \( \tfrac14(\e_1-\e_2)\otimes(\f_1-\f_2+2\f_3) \) and \( \tfrac14(\e_1+\e_2)\otimes(\f_1+\f_2) \), whose coefficients at \( \e_1\otimes\f_2 \) and at \( \e_2\otimes\f_1 \) cancel, leaving \( \tfrac12 \) at \( \e_1\otimes\f_1 \), \( \e_1\otimes\f_3 \) and \( \e_2\otimes\f_2 \) and \( -\tfrac12 \) at \( \e_2\otimes\f_3 \).
:::

::: {.remark}
Truncating @eq-schmidt after \( k \) terms is truncating a singular value decomposition, so @thm-eckart-young applies verbatim: the closest state of Schmidt rank at most \( k \) is the truncated sum, at distance \( (\sum_{i>k}\sigma_i^2)^{1/2} \). @exr-tensors-in-quantum-mechanics-c2 works this out. The remark also marks the limit of the theorem: everything here concerns **two** factors, because a matrix has two indices. For \( V \otimes W \otimes U \) a general vector admits no expression as a sum of simple tensors built from three orthonormal families; the book records that without proof.
:::

## Looking back at Part IV

Part IV asked one question in two ways. Chapter 13 took a single bilinear form and asked what it is up to a change of basis; Chapter 14 asked what all multilinear maps have in common, and answered by building the space that turns every one of them into a linear map.

The two chapters answer each other. Chapter 13 worked one form at a time and classified: congruence rather than similarity, complete the square, split off a hyperbolic plane, count signs rather than values. Every invariant it produced — the inertia of @thm-sylvester-inertia, the Witt index of @def-witt-index, the discriminant of @def-discriminant — was a number attached to a form that survives a change of basis, and every classification theorem said that a short list of such numbers is all there is. Chapter 14 worked with all forms at once and constructed: define by universal property and then build a model, impose relations by a quotient, define a map out of a quotient upstairs first, and count a basis by counting index tuples. Where Chapter 13 diagonalized a symmetric form by completing the square, Chapter 14 produced the space \( \Sym^2 V \) on which that form is a single linear functional; where Chapter 13 proved that alternating is the characteristic-free strengthening of skew, Chapter 14 built \( \Lambda^k V \) by killing \( \v\otimes\v \) for exactly that reason; and where Chapter 13 could only say that a Clifford algebra is unique if it exists, Chapter 14 built one out of \( T(V) \) and settled its dimension.

This last section adds a third connection, backwards rather than sideways. The Schmidt decomposition is not a new theorem; it is @thm-compact-svd with \( V \otimes W \) written in place of \( M_{m\times n} \). Part III spent a chapter on what a matrix does to two orthonormal bases, one in each of two spaces; Part IV spent a chapter on the space in which a pair of vectors, one from each of two spaces, becomes a single object. Those are the same statement read in two directions, and @thm-tensor-hom-iso is the sentence that says so. Asked years from now what the tensor product is for, a reader may answer that it is where a bilinear map becomes linear; the shortest true answer is that \( V \otimes W \) is where the two sides of a matrix live.

## Exercises

### A. Check your understanding

::: {#exr-tensors-in-quantum-mechanics-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the three modeling assumptions (Q1)–(Q3) of this section, and say which of them this book proves.
2. Define **product state** and **entangled state**, and say what data the words depend on besides the vector itself.
3. State the Schmidt decomposition, with every hypothesis, and say what is unique in it and what is not.
4. Define the Schmidt rank, and give the criterion for entanglement in terms of it.
5. True or false: a state written as a sum of three simple tensors has Schmidt rank \( 3 \). Justify your answer.
6. Which theorem of Chapter 12 is the Schmidt decomposition, and which theorem of §03 licenses the translation?
:::
:::

::: {.solution}
(a) (Q1) states are unit vectors of a complex inner product space, up to a scalar of modulus \( 1 \); (Q2) the state space of a composite system is the tensor product of the state spaces of the parts; (Q3) if the parts are in states \( \v \) and \( \w \), the composite is in the state \( \v \otimes \w \). The book proves none of them: they are quoted from physics.

(b) A unit vector \( \z \in V \otimes W \) is a product state if \( \z = \v\otimes\w \) for some \( \v \in V \) and \( \w \in W \), and entangled otherwise (@def-entangled). The words depend on the **splitting**: the pair of factors \( V \) and \( W \), not the vector alone.

(c) @thm-schmidt-decomposition: for \( V, W \) finite-dimensional complex inner product spaces and \( \z \in V\otimes W \) non-zero, there are \( r \ge 1 \), reals \( \sigma_1 \ge \dots \ge \sigma_r > 0 \) and orthonormal lists \( (\x_k) \) in \( V \) and \( (\y_k) \) in \( W \) with \( \z = \sum_k \sigma_k\x_k\otimes\y_k \). The number \( r \) and the \( \sigma_k \) are unique; the lists are not.

(d) The Schmidt rank is that \( r \) (@def-schmidt-rank). By @cor-schmidt-rank-one-separable, \( \z \) is entangled exactly when \( r \ge 2 \).

(e) False. The Schmidt rank is at most \( 3 \), but need not equal \( 3 \): the warning after @def-entangled displays a four-term sum whose Schmidt rank is \( 1 \).

(f) It is @thm-compact-svd, the compact form of the Singular Value Decomposition @thm-svd. The translation is licensed by @thm-tensor-hom-iso, which identifies a tensor with a linear map and hence, in bases, with a matrix.
:::

### B. Practice

::: {#exr-tensors-in-quantum-mechanics-b1}
[B1: Determine which are entangled]

Work in \( \nC^2\otimes\nC^2 \) with the standard orthonormal bases. Determine which of the following unit vectors are entangled. Justify your answer, and for each product state exhibit the two factors.

::: {.enumerate options="label=(\alph*)"}
1. \( \tfrac12(\e_1\otimes\f_1 + \e_1\otimes\f_2 + \e_2\otimes\f_1 + \e_2\otimes\f_2) \)
2. \( \tfrac{1}{\sqrt2}(\e_1\otimes\f_2 - \e_2\otimes\f_1) \)
3. \( \tfrac{1}{\sqrt3}(\e_1\otimes\f_1 + \e_1\otimes\f_2 + \e_2\otimes\f_2) \)
4. \( \tfrac{1}{\sqrt{10}}(\e_1\otimes\f_1 + 2\e_1\otimes\f_2 - \e_2\otimes\f_1 - 2\e_2\otimes\f_2) \)
:::
:::

::: {.solution}
By @cor-schmidt-rank-one-separable and the identification of the Schmidt rank with the rank of the coefficient matrix, it suffices to compute \( \rank\C \) in each case, and for a \( 2\times2 \) matrix that is decided by the determinant.

(a) \( \C = \tfrac12\begin{psmallmatrix}1&1\\1&1\end{psmallmatrix} \), with \( \det\C = 0 \) and \( \C \ne \0 \), so \( \rank\C = 1 \): a product state. Indeed it equals \( \tfrac{1}{\sqrt2}(\e_1+\e_2) \otimes \tfrac{1}{\sqrt2}(\f_1+\f_2) \).

(b) \( \C = \tfrac{1}{\sqrt2}\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix} \), with \( \det\C = \tfrac12 \ne 0 \), so \( \rank\C = 2 \): entangled.

(c) \( \C = \tfrac{1}{\sqrt3}\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix} \), with \( \det\C = \tfrac13 \ne 0 \), so \( \rank\C = 2 \): entangled.

(d) \( \C = \tfrac{1}{\sqrt{10}}\begin{psmallmatrix}1&2\\-1&-2\end{psmallmatrix} \), with \( \det\C = 0 \) and \( \C \ne \0 \), so \( \rank\C = 1 \): a product state, equal to \( \tfrac{1}{\sqrt2}(\e_1-\e_2) \otimes \tfrac{1}{\sqrt5}(\f_1+2\f_2) \).
:::

::: {#exr-tensors-in-quantum-mechanics-b2}
[B2: A Schmidt decomposition]

In \( \nC^2\otimes\nC^2 \), let
\[
\z = \tfrac{1}{\sqrt{10}}\bigl(\e_1\otimes\f_1 + 2\e_1\otimes\f_2
 + 2\e_2\otimes\f_1 + \e_2\otimes\f_2\bigr).
\]
Find the Schmidt coefficients, the Schmidt rank and a Schmidt decomposition of \( \z \), and verify that \( \sum_k\sigma_k^2 = 1 \).
:::

::: {.solution}
The coefficient matrix is \( \C = \tfrac{1}{\sqrt{10}}\begin{psmallmatrix}1&2\\2&1\end{psmallmatrix} \), which is real symmetric. Then
\[
\C\C\tp = \tfrac{1}{10}\begin{pmatrix}5&4\\4&5\end{pmatrix},
\]
with characteristic polynomial \( x^2 - x + \tfrac{9}{100} \) and eigenvalues \( \tfrac{9}{10} \) and \( \tfrac1{10} \). So the Schmidt coefficients are \( \sigma_1 = \tfrac{3}{\sqrt{10}} \) and \( \sigma_2 = \tfrac{1}{\sqrt{10}} \), the Schmidt rank is \( 2 \), and \( \sigma_1^2 + \sigma_2^2 = \tfrac9{10} + \tfrac1{10} = 1 \).

Eigenvectors of \( \C\C\tp \) are \( \u_1 = \tfrac1{\sqrt2}(1,1) \) for \( \tfrac9{10} \) and \( \u_2 = \tfrac1{\sqrt2}(1,-1) \) for \( \tfrac1{10} \). Then
\[
\v_1 = \tfrac{\C\tp\u_1}{\sigma_1} = \tfrac1{\sqrt2}(1,1),
\qquad
\v_2 = \tfrac{\C\tp\u_2}{\sigma_2} = \tfrac1{\sqrt2}(-1,1).
\]
All entries are real, so reading the columns back as in Step 3 of @thm-schmidt-decomposition,
\[
\begin{aligned}
\x_1 &= \tfrac{\e_1+\e_2}{\sqrt2}, & \y_1 &= \tfrac{\f_1+\f_2}{\sqrt2}, \\
\x_2 &= \tfrac{\e_1-\e_2}{\sqrt2}, & \y_2 &= \tfrac{-\f_1+\f_2}{\sqrt2},
\end{aligned}
\]
and \( \z = \tfrac{3}{\sqrt{10}}\,\x_1\otimes\y_1 + \tfrac{1}{\sqrt{10}}\,\x_2\otimes\y_2 \). Expanding the two terms gives \( \tfrac{1}{2\sqrt{10}}(3 - 1)\e_1\otimes\f_1 \) and similarly for the other three coefficients, recovering \( \z \).
:::

::: {#exr-tensors-in-quantum-mechanics-b3}
[B3: How large can the Schmidt rank be?]

Let \( V \) and \( W \) be complex inner product spaces with \( \dim V = m \) and \( \dim W = n \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that every non-zero \( \z \in V \otimes W \) has Schmidt rank at most \( \min(m, n) \).
2. Give, for each \( r \) with \( 1 \le r \le \min(m,n) \), a unit vector of Schmidt rank exactly \( r \).
:::
:::

::: {.solution}
(a) Fix orthonormal bases and let \( \C \in M_{m\times n}(\nC) \) be the coefficient matrix of \( \z \). By @thm-schmidt-decomposition the Schmidt rank is \( \rank\C \), and the rank of an \( m \times n \) matrix is at most \( \min(m,n) \) because \( \rank\C = \dim\col(\C) \le m \) and \( \rank\C = \dim\row(\C) \le n \).

(b) Take \( \z_r = \tfrac{1}{\sqrt r}\sum_{k=1}^{r}\e_k\otimes\f_k \). The lists \( (\e_1, \dots, \e_r) \) and \( (\f_1, \dots, \f_r) \) are orthonormal and every coefficient \( 1/\sqrt r \) is positive, so this is already an expression of the shape @eq-schmidt; by the uniqueness clause the Schmidt rank is \( r \). It is a unit vector since \( r \cdot (1/\sqrt r)^2 = 1 \).
:::

### C. Going deeper

::: {#exr-tensors-in-quantum-mechanics-c1}
[C1: Acting on one part at a time]

Let \( S \in \cL(V) \) and \( T \in \cL(W) \) be unitary, and let \( \z \in V \otimes W \) be non-zero.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( (S \otimes T)(\z) \) has the same Schmidt coefficients, and hence the same Schmidt rank, as \( \z \).
2. Hence deduce that no operator of the form \( S \otimes T \) with \( S, T \) unitary carries the Bell state \( \z_0 \) of @exm-bell-state to a product state.
:::

*Hint for (a): apply \( S \otimes T \) to a Schmidt decomposition.*
:::

::: {.solution}
(a) Write \( \z = \sum_{k=1}^{r}\sigma_k\,\x_k\otimes\y_k \) as in @thm-schmidt-decomposition. By @def-tensor-of-maps, \( (S\otimes T)(\x_k\otimes\y_k) = S\x_k\otimes T\y_k \), so by linearity
\[
(S\otimes T)(\z) = \sum_{k=1}^{r}\sigma_k\,(S\x_k)\otimes(T\y_k).
\]
A unitary operator preserves inner products (@thm-isometry-characterizations), so \( \inner{S\x_k}{S\x_l} = \inner{\x_k}{\x_l} = \delta_{kl} \) and likewise for \( T \). Both lists are therefore orthonormal, the \( \sigma_k \) are still positive and decreasing, and the display is an expression of the shape @eq-schmidt for \( (S\otimes T)(\z) \). By the uniqueness clause of @thm-schmidt-decomposition, its Schmidt coefficients are \( \sigma_1, \dots, \sigma_r \) and its Schmidt rank is \( r \).

(b) The Schmidt rank of \( \z_0 \) is \( 2 \), as computed in the warning after @cor-schmidt-rank-one-separable. By (a), \( (S\otimes T)(\z_0) \) also has Schmidt rank \( 2 \), and by @cor-schmidt-rank-one-separable a product state has Schmidt rank \( 1 \). So \( (S \otimes T)(\z_0) \) is entangled.
:::

::: {#exr-tensors-in-quantum-mechanics-c2}
[C2: Best approximation by a state of small Schmidt rank]

Let \( \z \in V \otimes W \) be non-zero with Schmidt decomposition \( \z = \sum_{k=1}^{r}\sigma_k\,\x_k\otimes\y_k \), and let \( 0 \le k \le r \). Put \( \z_{(k)} = \sum_{i=1}^{k}\sigma_i\,\x_i\otimes\y_i \).

::: {.enumerate options="label=(\alph*)"}
1. Fix orthonormal bases of \( V \) and \( W \) and let \( \C \) be the coefficient matrix of \( \z \). Prove that \( \norm{\z} = \norm{\C}_F \), and that the Schmidt rank of a vector equals the rank of its coefficient matrix.
2. Hence deduce that for every \( \z' \in V \otimes W \) of Schmidt rank at most \( k \),
\[
\norm{\z - \z'} \ \ge\ \Bigl(\sum_{i>k}\sigma_i^2\Bigr)^{1/2},
\]
with equality for \( \z' = \z_{(k)} \).
:::
:::

::: {.solution}
(a) By @prp-tensor-inner-product the basis \( (\e_i\otimes\f_j) \) of \( V\otimes W \) is orthonormal, so \( \norm{\z}^2 = \sum_{i,j}\lvert c_{ij}\rvert^2 \) by @thm-parseval-identity, and that sum is \( \norm{\C}_F^2 \) by the definition of the Frobenius norm. For the second claim, Step 2 of @thm-schmidt-decomposition produced the Schmidt coefficients as the non-zero singular values of \( \C \), and @thm-svd says there are \( \rank\C \) of them.

(b) The map \( \z \mapsto \C \) is the coordinate isomorphism attached to the basis \( (\e_i\otimes\f_j) \) (@cor-coordinate-isomorphism), with the \( mn \) coordinates arranged in a rectangle, so it is linear and bijective; and by (a) it carries \( \norm{\cdot} \) to \( \norm{\cdot}_F \) and Schmidt rank to matrix rank. Let \( \B \) be the coefficient matrix of \( \z' \), so \( \rank\B \le k \). By @thm-eckart-young,
\[
\norm{\z - \z'} = \norm{\C - \B}_F \ \ge\ \Bigl(\sum_{i>k}\sigma_i^2\Bigr)^{1/2},
\]
since the non-zero \( \sigma_i \) are the singular values of \( \C \). Running Step 3 of @thm-schmidt-decomposition backwards turns \( \z_{(k)} \) into the rank-\( k \) truncation \( \C_k \) (@def-truncated-svd) of a compact singular value decomposition of \( \C \) (@thm-compact-svd), and @thm-eckart-young attains equality there.
:::

::: {#exr-tensors-in-quantum-mechanics-c3}
[C3: Does the field matter?]

Let \( V \) and \( W \) be **real** inner product spaces of dimensions \( m \) and \( n \), with orthonormal bases \( \sE \) and \( \sF \), and let \( \z \in V\otimes W \) have coefficient matrix \( \C \in M_{m\times n}(\nR) \). Let \( \z_{\nC} \in \nC^m \otimes \nC^n \) be the vector whose coefficient matrix in the standard orthonormal bases is the same \( \C \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that @thm-schmidt-decomposition holds verbatim over \( \nR \), with orthonormal lists of real vectors.
2. Prove that \( \z \) and \( \z_{\nC} \) have the same Schmidt coefficients and the same Schmidt rank.
3. Is the same true of the Schmidt **vectors**? Justify your answer.
:::
:::

::: {.solution}
(a) Every step of the proof runs over \( F = \nR \). @thm-gram-schmidt, @thm-tensor-basis, @thm-compact-svd, @thm-orthonormal-coordinates and @thm-orthogonal-decomposition are all stated for \( F = \nR \) or \( \nC \), and over \( \nR \) the conjugations in Step 3 and Step 4 are the identity, so \( \y_k = \sum_j (\v_k)_j\f_j \) and \( \C\C\tp = \X\D^2\X\tp \).

(b) By Step 4 of @thm-schmidt-decomposition, read over each field in turn, the Schmidt coefficients of \( \z \) and of \( \z_{\nC} \) are both times the positive square roots of the non-zero eigenvalues of \( \C\C\tp \), and both Schmidt ranks equal \( \rank\C \). This is one and the same real symmetric matrix with one and the same characteristic polynomial, so the eigenvalues agree; and \( \rank\C \) is unchanged because row reduction over \( \nR \) is row reduction over \( \nC \).

(c) No. The warning after @cor-schmidt-rank-one-separable says why: a repeated Schmidt coefficient leaves the vectors free, and over \( \nC \) there is more freedom to use. For \( \z_0 \) the orthonormal pair \( \x_1 = \tfrac{1}{\sqrt2}(\e_1 + i\e_2) \), \( \x_2 = \tfrac{1}{\sqrt2}(\e_1 - i\e_2) \) occurs in a complex Schmidt decomposition — with \( \y_1 = \tfrac{1}{\sqrt2}(\f_1 - i\f_2) \) and \( \y_2 = \tfrac{1}{\sqrt2}(\f_1 + i\f_2) \) — and has no real counterpart. What is invariant is the coefficient list, not the vectors.
:::
