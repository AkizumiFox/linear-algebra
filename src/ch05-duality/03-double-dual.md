# The Double Dual

In a finite-dimensional space, the dual basis gives an isomorphism \( V \cong V^{*} \), sending \( \v_i \) to \( \varphi_i \). But that isomorphism depends on the basis: change the basis and the same vector goes to a different functional. Nothing stops us from taking duals twice. The dual \( V^{*} \) is a vector space, so it has a dual of its own, \( V^{**} \), and two chosen bases give \( V \cong V^{*} \cong V^{**} \). This section shows that the composite isomorphism \( V \to V^{**} \) needs **no** choice at all: it is built from evaluation alone. We use it to make one meaning of the word "natural" precise, and to prove that a subspace can be recovered from its annihilator. At the end we see that in infinite dimension the construction still makes sense, but it is no longer an isomorphism.

## Measuring the measurements

We have studied a space \( V \) and its space of measurements \( V^{*} = \cL(V, F) \) (@def-dual-space). The next object is the space of measurements **of** \( V^{*} \).

Look at the expression \( \varphi(\v) \), with \( \varphi \in V^{*} \) and \( \v \in V \). It has two inputs. If we fix \( \varphi \) and let \( \v \) vary, we get the functional \( \varphi \) itself. If we fix \( \v \) and let \( \varphi \) vary, we get a rule that takes a functional and returns a number. For example, take \( \v = (3, -1) \in \nR^2 \). A functional on \( \nR^2 \) is \( \varphi(x, y) = ax + by \) for unique \( a, b \) (@thm-functionals-on-fn), and the rule returns \( \varphi(3, -1) = 3a - b \). So the fixed vector \( (3, -1) \) measures each measurement. This rule appears every time we test a vector against functionals, so it deserves a name.

*A vector measures a functional by letting the functional act on it.*

::: {#def-evaluation-map}
[Double Dual and Evaluation Map]

Let \( V \) be a vector space over \( F \). The **double dual** of \( V \) is \( V^{**} \coloneqq (V^{*})^{*} \), the space of linear functionals on \( V^{*} \).

For \( \v \in V \), **evaluation at \( \v \)** is the function
\[
\ev_{\v} \colon V^{*} \to F, \qquad \ev_{\v}(\varphi) \coloneqq \varphi(\v).
\]
The **evaluation map** of \( V \) is
\[
\ev_V \colon V \to V^{**}, \qquad \v \mapsto \ev_{\v}.
\]
When only one space is in play we write \( \ev \) for \( \ev_V \).
:::

In words, clause by clause:

- \( V^{**} \) consists of **linear** maps \( V^{*} \to F \). Its elements take a whole functional as input.
- \( \ev_{\v} \) is **defined on \( V^{*} \)**, not on \( V \). The vector \( \v \) is fixed once and for all; the variable is \( \varphi \).
- The evaluation map sends each vector \( \v \) to the function \( \ev_{\v} \). A bold subscript \( \ev_{\v} \) is a single element of \( V^{**} \); an italic capital \( \ev_V \) is the whole map.

**Well-definedness.** The definition claims that \( \ev_{\v} \in V^{**} \), so we must check that \( \ev_{\v} \) is linear. The operations on \( V^{*} = \cL(V, F) \) are pointwise (@def-space-of-linear-maps). So for \( \varphi, \psi \in V^{*} \) and \( a, b \in F \),
\[
\ev_{\v}(a\varphi + b\psi) = (a\varphi + b\psi)(\v) = a\varphi(\v) + b\psi(\v) = a\ev_{\v}(\varphi) + b\ev_{\v}(\psi).
\]
Notice what the definition did **not** use: no basis, no coordinates, no choice of any kind. Only \( \v \) and the meaning of "functional" appear.

::: {#exm-evaluation-map}
[Evaluation in Three Spaces]

::: {.enumerate options="label=(\alph*)"}
1. Let \( V = F^n \). Describe \( \ev_{\x} \) for \( \x \in F^n \) in terms of row vectors.
2. Let \( V = \nR[x]_{\le 2} \), and let \( (\varphi_0, \varphi_1, \varphi_2) \) be the dual basis of \( (1, x, x^2) \), so that \( \varphi_k(p) \) is the coefficient of \( x^k \) in \( p \) (@exm-dual-basis-polynomials). Compute \( \ev_{x^2} \) on \( \varphi_0, \varphi_1, \varphi_2 \) and on the functional \( \varepsilon_3(p) = p(3) \). Which element of \( V^{**} \) is \( \ev_{x^2} \)?
3. Describe \( \ev_{\0} \), and the evaluation map of \( V = \{\0\} \).
:::
:::

::: {.solution}
(a) By @thm-functionals-on-fn, every \( \varphi \in (F^n)^{*} \) has the form \( \varphi(\y) = \a\tp\y \) for a unique \( \a \in F^n \). So \( \ev_{\x}(\varphi) = \a\tp\x \): the vector \( \x \) measures the row \( \a\tp \) by standing to its right in the product. The same product \( \a\tp\x \) is read as "\( \a\tp \) measures \( \x \)" or "\( \x \) measures \( \a\tp \)", depending on which factor we hold fixed.

(b) \( \ev_{x^2}(\varphi_k) = \varphi_k(x^2) \), the coefficient of \( x^k \) in \( x^2 \). So the values on \( \varphi_0, \varphi_1, \varphi_2 \) are \( 0, 0, 1 \). Also \( \ev_{x^2}(\varepsilon_3) = \varepsilon_3(x^2) = 9 \). A linear functional on \( V^{*} \) is determined by its values on the basis \( (\varphi_0, \varphi_1, \varphi_2) \) of \( V^{*} \) (@thm-linear-transform-basis). The values \( 0, 0, 1 \) say that \( \ev_{x^2} \) is the third vector of the dual basis of \( (\varphi_0, \varphi_1, \varphi_2) \) (@thm-dual-basis). In the same way, \( \ev_1 \) and \( \ev_x \) are the first and second vectors of that dual basis. We will see that this is no accident.

(c) \( \ev_{\0}(\varphi) = \varphi(\0) = 0 \) for every \( \varphi \), because a linear map sends \( \0 \) to \( 0 \) (@thm-zero-maps-to-zero). So \( \ev_{\0} \) is the zero functional on \( V^{*} \). If \( V = \{\0\} \), the only functional on \( V \) is the zero functional, so \( V^{*} = \{0\} \) and \( V^{**} = \{0\} \), and \( \ev_V \) is the only map \( \{\0\} \to \{0\} \). This degenerate case is a first sign that \( \ev \) loses nothing: the only vector it sends to zero is \( \0 \).
:::

Here is a non-example by minimal change. On \( V = \nR^2 \), replace \( \ev_{\v} \) by \( q_{\v}(\varphi) \coloneqq \varphi(\v)^2 \). It is still a function \( V^{*} \to \nR \), and it is still built without any choice. But take \( \v = (1, 0) \) and \( \varphi(x, y) = x \). Then \( q_{\v}(2\varphi) = 2^2 = 4 \), while \( 2q_{\v}(\varphi) = 2 \). The clause that fails is **linearity** on \( V^{*} \), so \( q_{\v} \notin V^{**} \).

**Why this definition.** Given only a vector \( \v \) and a functional \( \varphi \), the one number we can form without choosing anything is \( \varphi(\v) \); anything else, such as \( \varphi(\v)^2 \), is built from it and usually breaks linearity. The pointwise operations of @def-space-of-linear-maps are exactly what make \( \varphi \mapsto \varphi(\v) \) linear. The name "double dual" is literal: it is the dual of the dual.

::: {.warning}
**Two different "evaluations".** On \( V = \nR[x]_{\le 2} \), the functional \( \varepsilon_3 \colon p \mapsto p(3) \) lies in \( V^{*} \): it evaluates **polynomials at a number**. The element \( \ev_p \colon \varphi \mapsto \varphi(p) \) lies in \( V^{**} \): it evaluates **functionals at a polynomial**. They meet in one number, \( \ev_p(\varepsilon_3) = p(3) = \varepsilon_3(p) \), read from opposite sides. Also, \( \ev_{\v} \) is not the vector \( \v \): it is a function on \( V^{*} \).
:::

::: {.check}
Let \( \v = (1, 2) \in \nR^2 \). Compute \( \ev_{\v}(\varphi) \) for \( \varphi(x, y) = 3x - y \). Is there a **non-zero** \( \psi \in (\nR^2)^{*} \) with \( \ev_{\v}(\psi) = 0 \)?
:::

::: {.solution}
\( \ev_{\v}(\varphi) = \varphi(1, 2) = 3 - 2 = 1 \). Yes: \( \psi(x, y) = 2x - y \) is non-zero and \( \psi(1, 2) = 0 \). A single \( \ev_{\v} \) kills many functionals; what the next theorem says is that for \( \v \neq \0 \) it does not kill **all** of them.
:::

## The evaluation map never loses information

The first result says that \( \ev \) is a linear map, and that it is injective in every vector space, of any dimension.

::: {#thm-evaluation-map-linear-injective}
[The Evaluation Map Is Linear and Injective]

Let \( V \) be any vector space over \( F \). Then the evaluation map \( \ev_V \colon V \to V^{**} \) is linear and injective.
:::

::: {.idea}
Linearity is an identity between two elements of \( V^{**} \), that is, between two functions on \( V^{*} \); compare them at an arbitrary \( \varphi \). For injectivity, use the kernel test. If \( \ev_{\v} = 0 \), then **every** functional vanishes at \( \v \). This is the signature move of the chapter: to show a vector is zero, test it against every functional. In finite dimension @thm-functionals-separate-points does the job. In general we repeat its proof with the Basis Extension Theorem for arbitrary spaces.
:::

::: {.proof}
*Linear.* Let \( \u, \v \in V \) and \( a, b \in F \). For every \( \varphi \in V^{*} \), since \( \varphi \) is linear and the operations on \( V^{**} \) are pointwise (@def-space-of-linear-maps),
\[
\ev_{a\u + b\v}(\varphi) = \varphi(a\u + b\v) = a\varphi(\u) + b\varphi(\v) = (a\ev_{\u} + b\ev_{\v})(\varphi).
\]
Two functions on \( V^{*} \) that agree at every \( \varphi \) are equal, so \( \ev_{a\u + b\v} = a\ev_{\u} + b\ev_{\v} \).

*Injective.* By @thm-injective-iff-trivial-kernel it suffices to show that \( \ev_{\v} = 0 \) implies \( \v = \0 \). We prove the contrapositive. Let \( \v \neq \0 \). If \( V \) is finite-dimensional, @thm-functionals-separate-points (a) gives \( \varphi \in V^{*} \) with \( \varphi(\v) = 1 \). In general, \( \{\v\} \) is linearly independent, so by @thm-basis-extension-general there is a basis \( B \) of \( V \) with \( \v \in B \). By @thm-linear-map-from-any-basis, which allows infinite bases, there is a linear map \( \varphi \colon V \to F \) with \( \varphi(\v) = 1 \) and \( \varphi(\b) = 0 \) for every \( \b \in B \setminus \{\v\} \). In either case \( \varphi \in V^{*} \) and \( \ev_{\v}(\varphi) = \varphi(\v) = 1 \neq 0 \), so \( \ev_{\v} \neq 0 \). This proves that \( \ev_V \) is injective.
:::

In infinite dimension the proof repeats the remark after @thm-functionals-separate-points, and Zorn's Lemma enters through @thm-basis-extension-general. In finite dimension no choice principle is needed.

So every vector \( \v \) is completely remembered by the list of all its measurements \( \varphi(\v) \). In finite dimension a count turns "injective" into "bijective".

::: {#thm-double-dual-isomorphism}
[The Double Dual Isomorphism]

Let \( V \) be a finite-dimensional vector space over \( F \). Then the evaluation map \( \ev_V \colon V \to V^{**} \) is an isomorphism. Moreover, if \( \sB = (\v_1, \dots, \v_n) \) is a basis of \( V \) with dual basis \( \sB^{*} = (\varphi_1, \dots, \varphi_n) \), then \( (\ev_{\v_1}, \dots, \ev_{\v_n}) \) is the dual basis of \( \sB^{*} \).
:::

::: {.idea}
Count instead of check. The dual basis has as many vectors as the basis, so \( \dim V^{*} = \dim V \), and the same holds one level up. An injective linear map between spaces of the same finite dimension is bijective. For the second statement, "dual basis" is the condition \( \theta_i(\varphi_j) = \delta_{ij} \), and for \( \theta_i = \ev_{\v_i} \) that condition is the definition of \( \varphi_j \) read backwards.
:::

::: {.proof}
Let \( n = \dim V \). By @cor-dimension-dual-space, \( V^{*} \) is finite-dimensional with \( \dim V^{*} = n \), and applying it again to \( V^{*} \) gives \( \dim V^{**} = n \). By @thm-evaluation-map-linear-injective, \( \ev_V \) is linear and injective. Since \( \dim V = \dim V^{**} \) is finite, @cor-rank-nullity-consequences (e) shows that \( \ev_V \) is bijective, hence an isomorphism (@def-isomorphism).

For the second statement, \( \ev_{\v_i}(\varphi_j) = \varphi_j(\v_i) = \delta_{ji} = \delta_{ij} \) for all \( i, j \), by the definition of the dual basis. By the uniqueness in @thm-dual-basis (a), applied to the basis \( \sB^{*} \) of \( V^{*} \), the dual basis of \( \sB^{*} \) (@def-dual-basis) is the only list \( (\theta_1, \dots, \theta_n) \) in \( V^{**} \) with \( \theta_i(\varphi_j) = \delta_{ij} \). Hence it is \( (\ev_{\v_1}, \dots, \ev_{\v_n}) \), as claimed.
:::

The theorem says: **every** linear functional on \( V^{*} \) is evaluation at exactly one vector. To find the vector, read off its coordinates from the values on a dual basis. For instance, on \( V = \nR[x]_{\le 2} \) with the coefficient functionals \( \varphi_0, \varphi_1, \varphi_2 \) of @exm-evaluation-map, let \( \theta \in V^{**} \) be the functional with \( \theta(\varphi_0) = 2 \), \( \theta(\varphi_1) = 0 \), \( \theta(\varphi_2) = -1 \). By the second statement, \( \theta = 2\ev_1 - \ev_{x^2} = \ev_{2 - x^2} \), since both sides agree on the basis \( (\varphi_0, \varphi_1, \varphi_2) \) and \( \ev \) is linear. So, for example, \( \theta(\varepsilon_2) = \varepsilon_2(2 - x^2) = -2 \), where \( \varepsilon_2(p) = p(2) \). Part (b) of @exm-evaluation-map was the case \( \theta = \ev_{x^2} \).

## What "natural" means

Both \( V \cong V^{*} \) and \( V \cong V^{**} \) hold in finite dimension, and both follow from counting dimensions. Yet they are very different isomorphisms. The difference is whether a choice is needed.

**The isomorphism \( V \to V^{*} \) depends on the basis.** For a basis \( \sB = (\v_1, \dots, \v_n) \) of \( V \), let \( \Theta_{\sB} \colon V \to V^{*} \) be the linear map with \( \Theta_{\sB}(\v_i) = \varphi_i \) (@thm-linear-transform-basis). It sends a basis to a basis, so it is an isomorphism, by the argument in the proof of @thm-isomorphic-iff-same-dimension. Now take \( V = \nR \), a space of dimension \( 1 \). With the basis \( (1) \), the dual basis is \( \varphi(t) = t \), and \( \Theta_{(1)}(1) \) is \( t \mapsto t \). With the basis \( (2) \), the dual basis is \( \varphi(t) = t/2 \), since that is the functional sending \( 2 \) to \( 1 \). So \( \Theta_{(2)}(2) = (t \mapsto t/2) \), and by linearity \( \Theta_{(2)}(1) = \tfrac12\Theta_{(2)}(2) \) is \( t \mapsto t/4 \). The same vector \( 1 \) goes to two different functionals. Every basis is as good as any other, so none of these isomorphisms is preferred.

**The isomorphism \( V \to V^{**} \) does not.** Build it the same way, choosing bases twice. First \( \Theta_{\sB} \colon V \to V^{*} \) sends \( \v_i \mapsto \varphi_i \). Then, using the basis \( \sB^{*} \) of \( V^{*} \), the map \( \Theta_{\sB^{*}} \colon V^{*} \to V^{**} \) sends each \( \varphi_i \) to the \( i \)-th vector of the dual basis of \( \sB^{*} \). By @thm-double-dual-isomorphism, that vector is \( \ev_{\v_i} \). So the composite \( \Theta_{\sB^{*}}\Theta_{\sB} \) sends \( \v_i \mapsto \ev_{\v_i} \) for every \( i \). The linear map \( \ev_V \) does the same, so by the uniqueness part of @thm-linear-transform-basis,
\[
\Theta_{\sB^{*}}\,\Theta_{\sB} = \ev_V \qquad \text{for every basis } \sB \text{ of } V.
\]
Each factor depends on \( \sB \), but the composite does not: the two choices cancel. This is the first meaning of **natural**: an isomorphism is natural if it can be defined without choosing anything, and \( \ev_V \) is defined by the formula \( \ev_{\v}(\varphi) = \varphi(\v) \) alone.

There is a second, sharper meaning. A choice-free construction should be compatible with every linear map: if \( T \colon V \to W \), then first applying \( T \) and then identifying \( W \) with \( W^{**} \) should agree with first identifying \( V \) with \( V^{**} \) and then applying "the map that \( T \) induces on double duals". To state this we need to know how a linear map acts on functionals. That is the **dual map**, the subject of the next section, where we prove that \( \ev \) is compatible with every linear map, and see that no family of isomorphisms \( V \to V^{*} \) can be.

::: {.check}
In \( V = \nR \) with the basis \( \sB = (2) \), compute \( \Theta_{\sB^{*}}\Theta_{\sB}(1) \) as an element of \( V^{**} \), and evaluate it on \( \psi(t) = 5t \). Compare with \( \ev_1(\psi) \).
:::

::: {.solution}
The dual basis of \( \sB \) is \( \varphi_1(t) = t/2 \), so \( \Theta_{\sB}(1) = \tfrac12\Theta_{\sB}(2) = \tfrac12\varphi_1 \). The dual basis of \( \sB^{*} = (\varphi_1) \) is the \( \theta \in V^{**} \) with \( \theta(\varphi_1) = 1 \), and \( \ev_2(\varphi_1) = \varphi_1(2) = 1 \), so \( \theta = \ev_2 \) and \( \Theta_{\sB^{*}}(\varphi_1) = \ev_2 \). Hence \( \Theta_{\sB^{*}}\Theta_{\sB}(1) = \tfrac12\ev_2 = \ev_1 \), using linearity of \( \ev \). On \( \psi \) it gives \( \ev_1(\psi) = \psi(1) = 5 \). The factor \( \tfrac12 \) from the first step and the factor \( 2 \) hidden in \( \ev_2 \) cancel, exactly as the general computation predicts.
:::

::: {.remark}
Because \( \ev_V \) is natural, it is common to **identify** a finite-dimensional \( V \) with \( V^{**} \), and to regard a vector \( \v \) as the functional \( \varphi \mapsto \varphi(\v) \) on \( V^{*} \). We will do this only with an explicit "under the identification \( \v \leftrightarrow \ev_{\v} \)", as in the next corollary.
:::

## Consequences in finite dimension

Throughout this subsection, \( V \) is finite-dimensional. The isomorphism \( \ev_V \) lets us run arguments about \( V^{*} \) "one level up" and bring the answer back to \( V \).

The dual basis construction goes from a basis of \( V \) to a basis of \( V^{*} \). Does every basis of \( V^{*} \) arise this way? A list of \( n \) independent measurements should be the coordinate functions of some basis, and the double dual shows it is.

::: {#cor-every-basis-of-dual-is-dual}
[Every Basis of the Dual Is a Dual Basis]

Let \( V \) be a finite-dimensional vector space over \( F \), and let \( (\psi_1, \dots, \psi_n) \) be a basis of \( V^{*} \). Then there is exactly one basis \( (\v_1, \dots, \v_n) \) of \( V \) whose dual basis is \( (\psi_1, \dots, \psi_n) \), that is, with
\[
\psi_i(\v_j) = \delta_{ij} \qquad \text{for all } i, j.
\]
:::

::: {.idea}
Go up one level, where the problem is already solved. The basis \( (\psi_1, \dots, \psi_n) \) of \( V^{*} \) has a dual basis \( (\theta_1, \dots, \theta_n) \) in \( V^{**} \). Every \( \theta_j \) is evaluation at some vector, because \( \ev \) is onto. Those vectors are the answer, since \( \theta_j(\psi_i) = \delta_{ij} \) says \( \psi_i(\v_j) = \delta_{ij} \). Uniqueness is a "test against functionals" argument.
:::

::: {.proof}
*Existence.* Here \( V^{*} \) is finite-dimensional (@cor-dimension-dual-space). By @thm-dual-basis applied to \( V^{*} \), there is a basis \( (\theta_1, \dots, \theta_n) \) of \( V^{**} \) with \( \theta_j(\psi_i) = \delta_{ij} \). By @thm-double-dual-isomorphism, \( \ev_V \) is an isomorphism, so there are unique \( \v_j \in V \) with \( \ev_{\v_j} = \theta_j \). Its inverse is an isomorphism (@thm-isomorphic-equivalence-relation), so \( (\v_1, \dots, \v_n) \) is a basis of \( V \) by @thm-isomorphism-preserves-bases. For all \( i, j \),
\[
\psi_i(\v_j) = \ev_{\v_j}(\psi_i) = \theta_j(\psi_i) = \delta_{ij}.
\]
By the uniqueness in @thm-dual-basis (a), the dual basis of \( (\v_1, \dots, \v_n) \) is \( (\psi_1, \dots, \psi_n) \).

*Uniqueness.* Suppose \( (\u_1, \dots, \u_n) \) is also a basis with \( \psi_i(\u_j) = \delta_{ij} \). Fix \( j \). Then \( \psi_i(\v_j - \u_j) = \delta_{ij} - \delta_{ij} = 0 \) for every \( i \). Every \( \varphi \in V^{*} \) is a combination of the \( \psi_i \), so \( \varphi(\v_j - \u_j) = 0 \) for every \( \varphi \in V^{*} \). By @thm-functionals-separate-points (b), \( \v_j - \u_j = \0 \). Hence \( \u_j = \v_j \) for every \( j \).
:::

In coordinates this is a matrix inversion, the mirror image of @exm-dual-basis-inverse-rows. There, a basis was given and its dual basis appeared as the rows of an inverse matrix. Here the functionals are given, and the basis appears as the columns of an inverse matrix.

::: {#exm-basis-from-dual-basis}
[A Basis With Prescribed Dual Basis]

On \( V = \nR[x]_{\le 2} \), consider the functionals
\[
\psi_1(p) = p(0), \qquad \psi_2(p) = p(1), \qquad \psi_3(p) = p'(1).
\]
Show that \( (\psi_1, \psi_2, \psi_3) \) is a basis of \( V^{*} \), and find the basis \( (p_1, p_2, p_3) \) of \( V \) whose dual basis it is.
:::

::: {.solution}
*Write down a matrix.* For \( p = a + bx + cx^2 \), with \( \coord{p}{\sE} = (a, b, c) \) in \( \sE = (1, x, x^2) \),
\[
\psi_1(p) = a, \qquad \psi_2(p) = a + b + c, \qquad \psi_3(p) = b + 2c .
\]
So \( \psi_i(p) = \r_i\coord{p}{\sE} \), where \( \r_i \) is row \( i \) of
\[
\A = \begin{pmatrix} 1 & 0 & 0 \\ 1 & 1 & 1 \\ 0 & 1 & 2 \end{pmatrix}.
\]
*Translate the condition.* Let \( \P \) be the \( 3 \times 3 \) matrix whose \( j \)-th column is \( \coord{p_j}{\sE} \). By @thm-three-views-of-product, the \( (i, j) \) entry of \( \A\P \) is \( \r_i\coord{p_j}{\sE} = \psi_i(p_j) \). So the condition \( \psi_i(p_j) = \delta_{ij} \) says exactly \( \A\P = \I_3 \).

*Solve.* Row reduction (@thm-inverse-by-row-reduction) gives
\[
\A^{-1} = \begin{pmatrix} 1 & 0 & 0 \\ -2 & 2 & -1 \\ 1 & -1 & 1 \end{pmatrix},
\]
and one checks \( \A\A^{-1} = \I_3 \), so \( \A \) is invertible by @thm-one-sided-inverse. Multiplying \( \A\P = \I_3 \) on the left by \( \A^{-1} \) forces \( \P = \A^{-1} \). Since the columns of the invertible matrix \( \P \) are independent, \( (p_1, p_2, p_3) \) is a basis of \( V \) (via the coordinate isomorphism, @cor-coordinate-isomorphism). By the uniqueness in @thm-dual-basis (a), its dual basis is \( (\psi_1, \psi_2, \psi_3) \), which in particular is a basis of \( V^{*} \). Reading the columns,
\[
p_1 = 1 - 2x + x^2 = (1 - x)^2, \qquad p_2 = 2x - x^2, \qquad p_3 = x^2 - x .
\]
*Check.* \( p_1(0) = 1 \), \( p_1(1) = 0 \), \( p_1'(1) = 0 \); \( p_2(0) = 0 \), \( p_2(1) = 1 \), \( p_2'(1) = 2 - 2 = 0 \); \( p_3(0) = 0 \), \( p_3(1) = 0 \), \( p_3'(1) = 1 \).

So every \( p \in \nR[x]_{\le 2} \) is \( p = p(0)\,p_1 + p(1)\,p_2 + p'(1)\,p_3 \): the coordinates of \( p \) in this basis are the three measurements.
:::

The next consequence is the one we will use most. A subspace \( U \) determines the set \( U^{0} \) of functionals vanishing on it. Going back, the functionals in \( U^{0} \) vanish together on some set of vectors, which contains \( U \). Is it exactly \( U \)?

::: {#cor-annihilator-of-annihilator}
[The Annihilator of the Annihilator]

Let \( V \) be a finite-dimensional vector space over \( F \), and let \( U \) be a subspace of \( V \). Write \( U^{00} \coloneqq (U^{0})^{0} \subseteq V^{**} \). Then
\[
U^{00} = \ev_V(U) = \{ \ev_{\u} : \u \in U \}.
\]
So, under the identification \( \v \leftrightarrow \ev_{\v} \), we have \( U^{00} = U \). Equivalently,
\[
U = \{ \v \in V : \varphi(\v) = 0 \text{ for every } \varphi \in U^{0} \}.
\]
:::

::: {.idea}
One inclusion is a tautology: if \( \u \in U \) and \( \varphi \) kills \( U \), then \( \ev_{\u}(\varphi) = \varphi(\u) = 0 \). For the other, count. The dimension formula applied twice, once in \( V \) and once in \( V^{*} \), gives \( \dim U^{00} = \dim U \), and \( \ev \) is injective, so \( \dim \ev_V(U) = \dim U \) too. One inclusion plus equal dimension gives equality.
:::

::: {.proof}
Let \( n = \dim V \), so \( \dim V^{*} = n \) by @cor-dimension-dual-space.

*Inclusion.* Let \( \u \in U \). For every \( \varphi \in U^{0} \), \( \ev_{\u}(\varphi) = \varphi(\u) = 0 \) by @def-annihilator. Hence \( \ev_{\u} \in (U^{0})^{0} \), and \( \ev_V(U) \subseteq U^{00} \).

*Dimensions.* By @thm-dimension-annihilator in \( V \), \( \dim U^{0} = n - \dim U \). By @thm-dimension-annihilator in the \( n \)-dimensional space \( V^{*} \), applied to its subspace \( U^{0} \),
\[
\dim U^{00} = n - \dim U^{0} = n - (n - \dim U) = \dim U .
\]
The restriction of \( \ev_V \) to \( U \) is linear and injective (@thm-evaluation-map-linear-injective), so it is an isomorphism onto its image \( \ev_V(U) \), and \( \dim \ev_V(U) = \dim U \) (@thm-isomorphic-iff-same-dimension). So \( \ev_V(U) \) is a subspace of \( U^{00} \) of the same finite dimension, and @thm-dim-impl-eq gives \( \ev_V(U) = U^{00} \).

*The equivalent form.* Let \( \v \in V \). Then \( \varphi(\v) = 0 \) for every \( \varphi \in U^{0} \) if and only if \( \ev_{\v} \in U^{00} = \ev_V(U) \), if and only if \( \ev_{\v} = \ev_{\u} \) for some \( \u \in U \). Since \( \ev_V \) is injective, this happens if and only if \( \v \in U \).
:::

The last form says: **a subspace is exactly the common zero set of the functionals that vanish on it.** No vector outside \( U \) sneaks through all the equations. In section 6 of this chapter this becomes the statement that every subspace of \( F^n \) is the solution set of a homogeneous linear system. An immediate consequence is that the annihilator loses no information.

::: {#cor-subspaces-determined-by-annihilator}
[Subspaces Are Determined by Their Annihilators]

Let \( V \) be a finite-dimensional vector space, and let \( U \) and \( W \) be subspaces of \( V \). Then \( U = W \) if and only if \( U^{0} = W^{0} \).
:::

::: {.proof}
\( (\Rightarrow) \) is immediate. \( (\Leftarrow) \) Suppose \( U^{0} = W^{0} \). By @cor-annihilator-of-annihilator, \( U = \{ \v : \varphi(\v) = 0 \text{ for all } \varphi \in U^{0} \} = \{ \v : \varphi(\v) = 0 \text{ for all } \varphi \in W^{0} \} = W \).
:::

::: {.check}
Is @cor-subspaces-determined-by-annihilator still true if \( U \) and \( W \) are allowed to be arbitrary **subsets** of \( V \)?
:::

::: {.solution}
No. In \( \nR^2 \), take \( U = \{(1, 0)\} \) and \( W = \{(2, 0)\} \). A functional \( \varphi(x, y) = ax + by \) vanishes at \( (1, 0) \) exactly when \( a = 0 \), and at \( (2, 0) \) exactly when \( 2a = 0 \), that is, again when \( a = 0 \). So \( U^{0} = W^{0} \) but \( U \neq W \). An annihilator only sees the span, \( U^{0} = (\Span U)^{0} \) (@thm-annihilator-properties (b)).
:::

## Infinite dimension: the evaluation map is not onto

Nothing in @def-evaluation-map or @thm-evaluation-map-linear-injective needed finite dimension. The count in @thm-double-dual-isomorphism did.

::: {.warning}
**\( V \cong V^{**} \) through \( \ev \) is a finite-dimensional fact.** For \( V = F[x] \), the evaluation map is injective but **not** surjective: there is a linear functional on \( F[x]^{*} \) that is not evaluation at any polynomial. The next example constructs one.
:::

::: {#exm-evaluation-not-surjective}
[A Functional on \( F\lbrack x\rbrack^{*} \) That Is Not an Evaluation]

Let \( \varphi_k \in F[x]^{*} \) (\( k \in \nN \)) be the coordinate functionals, \( \varphi_k(p) = \) the coefficient of \( x^k \) in \( p \), and let \( \varepsilon_1(p) = p(1) \), as in @prp-coordinate-functionals-do-not-span. Show that there is \( \theta \in F[x]^{**} \) with \( \theta \neq \ev_p \) for every \( p \in F[x] \).
:::

::: {.solution}
*Step 1: \( S = \{ \varphi_k : k \in \nN \} \cup \{\varepsilon_1\} \) is linearly independent.* By @prp-coordinate-functionals-do-not-span, the \( \varphi_k \) form an independent set and \( \varepsilon_1 \notin \Span\{ \varphi_k : k \in \nN \} \). Let \( L \) be a finite list of distinct elements of \( S \). If \( \varepsilon_1 \) is not in \( L \), then \( L \) is independent. Otherwise, list \( \varepsilon_1 \) last; the others are independent and \( \varepsilon_1 \) is not in their span, so \( L \) is independent by @lem-append-independent.

*Step 2: build \( \theta \).* By @thm-basis-extension-general there is a basis \( B \) of \( F[x]^{*} \) containing \( S \). By @thm-linear-map-from-any-basis for the (infinite) basis \( B \), there is a linear \( \theta \colon F[x]^{*} \to F \) with \( \theta(\varepsilon_1) = 1 \) and \( \theta(\beta) = 0 \) for every \( \beta \in B \setminus \{\varepsilon_1\} \). In particular \( \theta(\varphi_k) = 0 \) for all \( k \).

*Step 3: \( \theta \) is not an evaluation.* Suppose \( \theta = \ev_p \) for some \( p \in F[x] \). Then for every \( k \), the coefficient of \( x^k \) in \( p \) is \( \varphi_k(p) = \ev_p(\varphi_k) = \theta(\varphi_k) = 0 \). So \( p = 0 \), and \( \theta = \ev_0 = 0 \). This contradicts \( \theta(\varepsilon_1) = 1 \). Hence \( \theta \notin \ev(F[x]) \), and \( \ev \) is not surjective.
:::

The functional \( \theta \) exists, but nobody can write it down: it comes from Zorn's Lemma through @thm-basis-extension-general. The deeper reason for the failure is size. \( F[x]^{*} \) is so much bigger than \( F[x] \) (@exr-linear-functionals-c4 identifies it with the whole sequence space \( F^{\nN} \)) that \( F[x]^{**} \) is bigger still, and in fact no isomorphism \( F[x] \cong F[x]^{**} \) exists at all, a statement about the sizes of bases that we do not prove. In finite dimension, sizes cannot grow, and the evaluation map is the perfect dictionary of @thm-double-dual-isomorphism.

## Exercises

### A. Check your understanding

::: {#exr-double-dual-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define \( \ev_{\v} \) for \( \v \in V \), and the evaluation map \( \ev_V \). In which space does \( \ev_{\v} \) live?
2. State a hypothesis on \( V \) under which \( \ev_V \) is an isomorphism, and a space for which it is not.
3. True or false: if \( V \) is finite-dimensional and \( \v \neq \0 \), then \( \ev_{\v}(\varphi) \neq 0 \) for **every** non-zero \( \varphi \in V^{*} \). Justify your answer.
4. True or false: if \( U \) and \( W \) are subspaces of \( \nR^5 \) with \( U^{0} = W^{0} \), then \( U = W \). Justify your answer.
5. Name the method used to prove \( U^{00} = \ev_V(U) \) in @cor-annihilator-of-annihilator.
:::
:::

::: {.solution}
(a) \( \ev_{\v} \colon V^{*} \to F \), \( \ev_{\v}(\varphi) = \varphi(\v) \), and \( \ev_V \colon V \to V^{**} \), \( \v \mapsto \ev_{\v} \) (@def-evaluation-map). \( \ev_{\v} \) lives in \( V^{**} \).

(b) If \( V \) is finite-dimensional, \( \ev_V \) is an isomorphism (@thm-double-dual-isomorphism). For \( V = F[x] \) it is not surjective (@exm-evaluation-not-surjective).

(c) False. It says only that **some** \( \varphi \) has \( \varphi(\v) \neq 0 \) (@thm-evaluation-map-linear-injective). In \( \nR^2 \), \( \v = (1, 2) \) and \( \varphi(x, y) = 2x - y \neq 0 \) give \( \ev_{\v}(\varphi) = 0 \).

(d) True, by @cor-subspaces-determined-by-annihilator, since \( \nR^5 \) is finite-dimensional.

(e) One inclusion plus equal dimension: \( \ev_V(U) \subseteq U^{00} \) directly, then \( \dim U^{00} = \dim U = \dim \ev_V(U) \) from the dimension formula for annihilators (twice) and injectivity of \( \ev \), and @thm-dim-impl-eq.
:::

### B. Practice

::: {#exr-double-dual-b1}
[B1: A basis with a given dual basis]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \psi_1(x, y) = 2x + y \) and \( \psi_2(x, y) = x + y \) on \( \nR^2 \). Find the basis \( (\v_1, \v_2) \) of \( \nR^2 \) whose dual basis is \( (\psi_1, \psi_2) \).
2. Let \( \psi_1(p) = p(0) \) and \( \psi_2(p) = \int_0^1 p(x)\,\dd x \) on \( \nR[x]_{\le 1} \). Find the basis \( (p_1, p_2) \) of \( \nR[x]_{\le 1} \) whose dual basis is \( (\psi_1, \psi_2) \).
:::
:::

::: {.solution}
(a) As in @exm-basis-from-dual-basis, \( \psi_i(\v) = \r_i\v \) with \( \r_i \) the rows of \( \A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \), and the condition \( \psi_i(\v_j) = \delta_{ij} \) says \( \A\P = \I_2 \) for \( \P = \begin{pmatrix} \v_1 & \v_2 \end{pmatrix} \). Here \( 2 \cdot 1 - 1 \cdot 1 = 1 \neq 0 \), so by @thm-two-by-two-inverse
\[
\A^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix},
\]
\( \P = \A^{-1} \), so \( \v_1 = (1, -1) \) and \( \v_2 = (-1, 2) \). These are independent (the columns of an invertible matrix), hence a basis. Check: \( \psi_1(\v_1) = 1 \), \( \psi_2(\v_1) = 0 \), \( \psi_1(\v_2) = 0 \), \( \psi_2(\v_2) = 1 \). By the uniqueness part of @thm-dual-basis, the dual basis of \( (\v_1, \v_2) \) is \( (\psi_1, \psi_2) \).

(b) For \( p = a + bx \), \( \psi_1(p) = a \) and \( \psi_2(p) = a + \tfrac12 b \). So \( \A = \begin{pmatrix} 1 & 0 \\ 1 & 1/2 \end{pmatrix} \) and
\[
\P = \A^{-1} = \begin{pmatrix} 1 & 0 \\ -2 & 2 \end{pmatrix},
\]
whose columns are the coordinates of \( p_1 = 1 - 2x \) and \( p_2 = 2x \) in \( (1, x) \). Check: \( p_1(0) = 1 \), \( \int_0^1 (1 - 2x)\,\dd x = 1 - 1 = 0 \), \( p_2(0) = 0 \), \( \int_0^1 2x\,\dd x = 1 \). As in (a), \( (p_1, p_2) \) is a basis with dual basis \( (\psi_1, \psi_2) \).
:::

::: {#exr-double-dual-b2}
[B2: \( U^{00} = U \) for a line]

Let \( U = \Span\bigl((1, 2, -1)\bigr) \subseteq \nR^3 \).

::: {.enumerate options="label=(\alph*)"}
1. Find a basis of \( U^{0} \).
2. Find all \( \v \in \nR^3 \) with \( \varphi(\v) = 0 \) for every \( \varphi \in U^{0} \), and check that the answer is \( U \).
3. Hence verify that \( U^{00} = \ev(U) \), and confirm the dimension count.
:::
:::

::: {.solution}
(a) A functional \( \varphi(x, y, z) = ax + by + cz \) (@thm-functionals-on-fn) lies in \( U^{0} \) iff it vanishes at \( (1, 2, -1) \) (@thm-annihilator-properties (b)), that is, \( a + 2b - c = 0 \). The solutions are \( (a, b, c) = s(-2, 1, 0) + t(1, 0, 1) \), so \( \varphi_1(x, y, z) = 2x - y \) and \( \varphi_2(x, y, z) = x + z \) span \( U^{0} \) (we replaced \( (-2, 1, 0) \) by its negative). They are independent, since neither is a multiple of the other, so \( (\varphi_1, \varphi_2) \) is a basis of \( U^{0} \). This matches \( \dim U^{0} = 3 - 1 = 2 \) (@thm-dimension-annihilator).

(b) Every \( \varphi \in U^{0} \) is a combination of \( \varphi_1, \varphi_2 \), so \( \varphi(\v) = 0 \) for all \( \varphi \in U^{0} \) iff \( \varphi_1(\v) = \varphi_2(\v) = 0 \), that is, \( 2x - y = 0 \) and \( x + z = 0 \). With \( x = t \): \( y = 2t \), \( z = -t \), so \( \v = t(1, 2, -1) \). The set is exactly \( U \).

(c) Let \( \theta \in U^{00} \subseteq (\nR^3)^{**} \). By @thm-double-dual-isomorphism, \( \theta = \ev_{\v} \) for some \( \v \), and \( \theta \in (U^{0})^{0} \) means \( \varphi(\v) = 0 \) for all \( \varphi \in U^{0} \). By (b), \( \v \in U \), so \( U^{00} \subseteq \ev(U) \); the reverse inclusion is immediate from @def-annihilator. Dimensions: \( \dim U^{00} = 3 - \dim U^{0} = 1 = \dim U \).
:::

::: {#exr-double-dual-b3}
[B3: Recognizing an evaluation]

Let \( V = \nR[x]_{\le 2} \), with the coefficient functionals \( \varphi_0, \varphi_1, \varphi_2 \) of @exm-evaluation-map. Let \( \theta \in V^{**} \) be the linear functional with \( \theta(\varphi_0) = 1 \), \( \theta(\varphi_1) = -3 \), \( \theta(\varphi_2) = 2 \). Find \( p \in V \) with \( \theta = \ev_p \). Hence compute \( \theta(\varepsilon_1) \) and \( \theta(\psi) \), where \( \varepsilon_1(q) = q(1) \) and \( \psi(q) = q'(0) \).
:::

::: {.solution}
By @thm-double-dual-isomorphism, \( (\ev_1, \ev_x, \ev_{x^2}) \) is the dual basis of \( (\varphi_0, \varphi_1, \varphi_2) \). Hence \( \ev_1 - 3\ev_x + 2\ev_{x^2} \) takes the values \( 1, -3, 2 \) on \( \varphi_0, \varphi_1, \varphi_2 \). So does \( \theta \), and a linear functional is determined by its values on a basis (@thm-linear-transform-basis). Since \( \ev \) is linear (@thm-evaluation-map-linear-injective),
\[
\theta = \ev_1 - 3\ev_x + 2\ev_{x^2} = \ev_{p}, \qquad p = 1 - 3x + 2x^2 .
\]
Hence \( \theta(\varepsilon_1) = \varepsilon_1(p) = 1 - 3 + 2 = 0 \) and \( \theta(\psi) = \psi(p) = p'(0) = -3 \).
:::

### C. Going deeper

::: {#exr-double-dual-c1}
[C1: Subspaces of \( V \) and of \( V^{*} \)]

Let \( V \) be a finite-dimensional vector space over \( F \). Prove that \( U \mapsto U^{0} \) is a bijection from the set of subspaces of \( V \) to the set of subspaces of \( V^{*} \), and that it reverses inclusions in both directions: \( U \subseteq W \) if and only if \( W^{0} \subseteq U^{0} \).

*Hint: for surjectivity, given a subspace \( X \subseteq V^{*} \), consider \( U = \{ \v \in V : \varphi(\v) = 0 \text{ for all } \varphi \in X \} \).*
:::

::: {.solution}
Let \( n = \dim V = \dim V^{*} \) (@cor-dimension-dual-space). By @prp-annihilator-subspace, \( U^{0} \) is a subspace of \( V^{*} \), so the map is well defined.

*Injective.* This is @cor-subspaces-determined-by-annihilator.

*Inclusions.* If \( U \subseteq W \), then \( W^{0} \subseteq U^{0} \) by @thm-annihilator-properties (a). Conversely, suppose \( W^{0} \subseteq U^{0} \), and let \( \u \in U \). Every \( \varphi \in W^{0} \) lies in \( U^{0} \), so \( \varphi(\u) = 0 \). By @cor-annihilator-of-annihilator (the equivalent form, for \( W \)), \( \u \in W \). Hence \( U \subseteq W \).

*Surjective.* Let \( X \) be a subspace of \( V^{*} \), and let \( U = \{ \v \in V : \varphi(\v) = 0 \text{ for all } \varphi \in X \} \). For \( \v \in V \), \( \v \in U \) iff \( \ev_{\v}(\varphi) = 0 \) for all \( \varphi \in X \) iff \( \ev_{\v} \in X^{0} \), where \( X^{0} \subseteq V^{**} \). So \( U = \ev_V^{-1}(X^{0}) \), and since \( \ev_V \) is an isomorphism (@thm-double-dual-isomorphism), \( U \) is a subspace and \( \ev_V \) restricts to an isomorphism \( U \to X^{0} \). By @thm-dimension-annihilator in \( V^{*} \), \( \dim U = \dim X^{0} = n - \dim X \). By definition of \( U \), every \( \varphi \in X \) vanishes on \( U \), so \( X \subseteq U^{0} \). By @thm-dimension-annihilator in \( V \), \( \dim U^{0} = n - \dim U = \dim X \). By @thm-dim-impl-eq, \( X = U^{0} \). This proves the claim.
:::

::: {#exr-double-dual-c2}
[C2: Spans cut out by equations]

Let \( V \) be finite-dimensional and \( S \subseteq V \) any subset.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \{ \v \in V : \varphi(\v) = 0 \text{ for every } \varphi \in S^{0} \} = \Span(S) \).
2. Deduce: a vector \( \v \) lies in \( \Span(S) \) if and only if every functional that vanishes on \( S \) vanishes at \( \v \).
3. Show by an example that (a) can fail if "\( \Span(S) \)" is replaced by "\( S \)".
:::
:::

::: {.solution}
(a) \( \Span(S) \) is a subspace (@thm-span-subspace), and \( S^{0} = (\Span S)^{0} \) by @thm-annihilator-properties (b). Applying @cor-annihilator-of-annihilator to \( U = \Span(S) \),
\[
\{ \v : \varphi(\v) = 0 \ \forall \varphi \in S^{0} \} = \{ \v : \varphi(\v) = 0 \ \forall \varphi \in (\Span S)^{0} \} = \Span(S).
\]
(b) This is (a) read for a single vector \( \v \).

(c) Take \( S = \{(1, 0)\} \subseteq \nR^2 \). Then \( S^{0} \) consists of the functionals \( (x, y) \mapsto by \), and their common zero set is the whole \( x \)-axis, which contains \( (2, 0) \notin S \).
:::

::: {#exr-double-dual-c3}
[C3: Where finite dimension is needed]

Let \( V = F[x] \), let \( \varphi_k \) and \( \varepsilon_1 \) be as in @exm-evaluation-not-surjective, and let \( X = \Span\{ \varphi_k : k \in \nN \} \subseteq V^{*} \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \{ p \in F[x] : \varphi(p) = 0 \text{ for all } \varphi \in X \} = \{0\} \).
2. Deduce that \( X \neq U^{0} \) for **every** subspace \( U \) of \( F[x] \). So the map \( U \mapsto U^{0} \) of @exr-double-dual-c1 is not surjective for \( F[x] \).
3. Which step of the solution of @exr-double-dual-c1 fails here?
:::
:::

::: {.solution}
(a) If \( \varphi(p) = 0 \) for all \( \varphi \in X \), then in particular \( \varphi_k(p) = 0 \) for every \( k \), so every coefficient of \( p \) is \( 0 \) and \( p = 0 \). Conversely \( \varphi(0) = 0 \) for every \( \varphi \).

(b) Suppose \( X = U^{0} \). Every \( \varphi \in X = U^{0} \) vanishes on \( U \), so \( U \subseteq \{ p : \varphi(p) = 0 \ \forall \varphi \in X \} = \{0\} \) by (a). Hence \( U = \{0\} \) and \( U^{0} = V^{*} \) (every functional vanishes at \( 0 \)). But \( \varepsilon_1 \in V^{*} \) and \( \varepsilon_1 \notin X \), by @prp-coordinate-functionals-do-not-span. So \( X \neq V^{*} = U^{0} \), a contradiction.

(c) The dimension count. In @exr-double-dual-c1 we used that \( \ev_V \) is onto and that \( \dim U + \dim U^{0} = \dim V \) to force \( X = U^{0} \) from \( X \subseteq U^{0} \). Here \( U = \{0\} \) and \( X \subsetneq U^{0} = V^{*} \): the inclusion holds, but there is no finite dimension to compare, and a proper subspace of an infinite-dimensional space can be "as large as" the whole space.
:::
