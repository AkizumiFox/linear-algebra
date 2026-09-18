# Subspaces

After defining a structure, the next step is to look at the smaller copies of it that sit inside. In the previous section we showed three times, for \( F[x]_{\le n} \), \( \nQ(\sqrt2) \) and the solutions of \( f'' + f = 0 \), that a subset of a known vector space is itself a vector space, and each time the same few checks did the work. This section turns that pattern into a theorem, the subspace test, and makes its three checks a routine we will use for the rest of the book.

## Spaces inside spaces

Consider the set
\[
P = \{ (x, y, z) \in \nR^3 : x + y - z = 0 \},
\]
a plane through the origin in \( \nR^3 \). It contains \( (1, 0, 1) \) and \( (0, 1, 1) \), and also their sum \( (1, 1, 2) \), since \( 1 + 1 - 2 = 0 \). Stretching a vector of \( P \) keeps it in the plane. So \( P \), with the addition and scalar multiplication of \( \nR^3 \), looks like a vector space in its own right.

To prove it we could check all eight axioms again. That is wasteful, and the previous section already showed why. The axioms (VS1), (VS2) and (VS5)–(VS8) are equations that hold for **all** vectors of \( \nR^3 \), so they hold in particular for the vectors of \( P \). What can go wrong is different: a sum or a multiple might leave \( P \), and the zero vector or an additive inverse might not lie in \( P \). The question of this section is which of these checks are really needed.

*A subspace is a subset that is a vector space in its own right, using the same addition and scalar multiplication.*

::: {#def-subspace}
[Subspace]

Let \( V \) be a vector space over \( F \). A subset \( U \subseteq V \) is a **subspace** of \( V \) if \( U \) is **itself a vector space over \( F \)** when it is given the addition and the scalar multiplication of \( V \).

For that sentence to make sense, \( U \) must first be closed under those two operations:
\[
\u + \w \in U \quad\text{and}\quad a\u \in U \qquad \text{for all } \u, \w \in U \text{ and all } a \in F .
\]
:::

In words: take the plus and the dot that \( V \) already has, use them only on vectors of \( U \), and ask whether \( U \) is a vector space with them. Nothing new is defined; \( U \) borrows everything from \( V \). The displayed condition is what makes the borrowing possible, because an operation on \( U \) must land **in \( U \)**: if \( \u, \w \in U \) but \( \u + \w \notin U \), then addition is not an operation on \( U \) at all, and the question of the axioms never arises. Once the condition holds, the eight axioms are asked of \( U \) exactly as they were asked of \( V \) in the previous section. In particular \( U \) must contain **a** zero vector of its own, and every vector of \( U \) must have an additive inverse **lying in \( U \)**. The field does not change: a subspace of a space over \( F \) is again a space over \( F \).

Two words of the definition carry all the weight. **Itself a vector space** is the whole content. **The same operations** is what distinguishes a subspace from a subset that merely happens to be a vector space under some other rule: \( \nR_{>0} \) with the operations of @exm-positive-reals is a vector space and a subset of \( \nR \), but it is not a subspace of \( \nR \), because those are not the operations of \( \nR \).

There is a question hidden in "a zero vector of its own". Could \( U \) have a zero vector different from the zero vector of \( V \)? The proof of the subspace test below shows that it cannot.

The two extreme cases come first.

::: {#exm-trivial-subspaces}
[Trivial Subspaces]

Let \( V \) be a vector space over \( F \). Show that \( V \) and \( \{\0\} \) are subspaces of \( V \), and that the empty set \( \varnothing \) is not.
:::

::: {.solution}
For \( V \) itself, the restricted operations are the operations of \( V \), and \( V \) is a vector space by assumption.

For \( \{\0\} \), the only sum is \( \0 + \0 = \0 \) by (VS3), and \( a\0 = \0 \) for every \( a \in F \) by @thm-scalar-zero-vector. So both operations stay in \( \{\0\} \), and \( \{\0\} \) with them is the zero space, a vector space as noted in the previous section.

For \( \varnothing \), axiom (VS3) demands that some element \( \0 \) exists in the set. The empty set has no elements, so (VS3) fails and \( \varnothing \) is not a subspace.
:::

The subspace \( \{\0\} \) is the **zero subspace**. A subspace other than \( V \) is called **proper**. The zero subspace is small, but it is the answer to many questions later: the solutions of a system with only the trivial solution, or the intersection of two lines through the origin that are not equal.

## The subspace test

The following theorem says that three checks suffice. Two of them are the closure conditions of the definition, and the third replaces all of the axioms.

::: {#thm-subspace-test}
[Subspace Test]

Let \( V \) be a vector space over \( F \) and let \( U \subseteq V \). Then \( U \) is a subspace of \( V \) if and only if the following three conditions hold.

::: {.enumerate options="label=(\arabic*)"}
1. \( \0 \in U \), where \( \0 \) is the zero vector of \( V \).
2. \( U \) is **closed under addition**: \( \u + \w \in U \) for all \( \u, \w \in U \).
3. \( U \) is **closed under scalar multiplication**: \( a\u \in U \) for all \( a \in F \) and \( \u \in U \).
:::
:::

::: {.idea}
Sort the eight axioms into two kinds. Six of them, (VS1), (VS2) and (VS5)–(VS8), say "an equation holds **for all** vectors"; they are true in \( V \), so they are automatically true for the fewer vectors in \( U \). The other two, (VS3) and (VS4), say "**there exists** a vector", and a witness must be found **inside** \( U \). Condition (1) supplies the zero. For inverses, the results of the previous section give \( -\u = (-1)\u \), so closure under scaling supplies them for free. For \( (\Rightarrow) \), the only non-obvious point is that the zero vector of \( U \) is the zero vector of \( V \); cancellation in \( V \) settles it.
:::

::: {.proof}
\( (\Rightarrow) \) Suppose \( U \) is a subspace of \( V \). Conditions (2) and (3) are the closure condition of @def-subspace. By (VS3) in \( U \), there is \( \z \in U \) with \( \u + \z = \u \) for every \( \u \in U \); in particular \( \z + \z = \z \). By (VS3) in \( V \), also \( \z + \0 = \z \). Hence \( \z + \z = \z + \0 \), and @thm-left-cancellation in \( V \) gives \( \z = \0 \). Therefore \( \0 \in U \), which is (1).

\( (\Leftarrow) \) Suppose (1), (2) and (3) hold. By (2) and (3), addition and scalar multiplication of \( V \) restrict to functions \( U \times U \to U \) and \( F \times U \to U \). We check the axioms for \( U \) with these operations.

- (VS1), (VS2), (VS5), (VS6), (VS7) and (VS8) state that certain equations hold for all vectors and scalars. They hold for all vectors of \( V \), since \( V \) is a vector space, so in particular for all vectors of \( U \).
- (VS3): by (1), \( \0 \in U \), and \( \u + \0 = \u \) for every \( \u \in U \) by (VS3) in \( V \).
- (VS4): let \( \u \in U \). By (3), \( (-1)\u \in U \). By @thm-negation-scalar, \( (-1)\u = -\u \), so \( \u + (-1)\u = \0 \). Thus \( \u \) has an additive inverse in \( U \).

Hence \( U \) is a vector space over \( F \) with the operations of \( V \), that is, a subspace of \( V \).
:::

From now on we never check eight axioms for a subset of a known vector space. We check three things, always in the same order and with the same wording. This is the first named move of the chapter.

**The three-check move.** To show that a subset \( U \) of a vector space \( V \) is a subspace:

- make sure \( U \) is a subset of \( V \) (what are its elements, and do they lie in \( V \)?);
- **(1) Zero vector.** Show \( \0 \in U \) by checking that \( \0 \) satisfies the condition defining \( U \). End with "Therefore \( \0 \in U \)."
- **(2) Closed under addition.** Let \( \u, \w \in U \). Write down what membership in \( U \) means for each, then regroup \( \u + \w \) so that those conditions appear. End with "This shows that \( U \) is closed under addition."
- **(3) Closed under scalar multiplication.** Let \( a \in F \) and \( \u \in U \), and do the same for \( a\u \). End with "This shows that \( U \) is closed under scalar multiplication."
- Conclude: "Hence \( U \) is a subspace of \( V \) by the subspace test (@thm-subspace-test)."

To show that \( U \) is **not** a subspace, one failure suffices. Check (1) first, since it is the cheapest, and if it holds, look for a concrete pair of vectors or a concrete scalar that leads out of \( U \).

::: {.remark}
Condition (1) may be replaced by "\( U \) is non-empty". Indeed, if \( U \) contains some \( \u \), then (3) gives \( 0\u \in U \), and \( 0\u = \0 \) by @thm-zero-scalar-mult. We still prefer (1): the zero vector is the easiest element to test, and when it is missing we have a refutation in one line.
:::

::: {.warning}
**The empty set is never a subspace.** It is tempting to check only (2) and (3). But \( \varnothing \) satisfies both, vacuously: there are no vectors in it to add or scale. It fails only (1). So whichever version of the test you use, do not skip the first condition, and remember that "\( \0 \in U \)" and "\( U \) is non-empty" are interchangeable only in the presence of (3).
:::

## Examples: the three-check move

Every example below follows the move exactly. The first is the model.

::: {#exm-line-subspace}
[A Line through the Origin]

Show that \( U = \{ (x, y) \in \nR^2 : x + 2y = 0 \} \) is a subspace of \( \nR^2 \).
:::

::: {.solution}
By definition, \( U \) is a subset of \( \nR^2 \).

**(1) Zero vector.** The zero vector \( (0, 0) \) satisfies \( 0 + 2 \cdot 0 = 0 \). Therefore \( \0 \in U \).

**(2) Closed under addition.** Let \( \u = (x_1, y_1) \) and \( \w = (x_2, y_2) \) be in \( U \), so that \( x_1 + 2y_1 = 0 \) and \( x_2 + 2y_2 = 0 \). Then \( \u + \w = (x_1 + x_2, y_1 + y_2) \), and
\[
(x_1 + x_2) + 2(y_1 + y_2) = (x_1 + 2y_1) + (x_2 + 2y_2) = 0 + 0 = 0.
\]
Therefore \( \u + \w \in U \). This shows that \( U \) is closed under addition.

**(3) Closed under scalar multiplication.** Let \( a \in \nR \) and \( \u = (x, y) \in U \), so that \( x + 2y = 0 \). Then \( a\u = (ax, ay) \), and
\[
ax + 2(ay) = a(x + 2y) = a \cdot 0 = 0.
\]
Therefore \( a\u \in U \). This shows that \( U \) is closed under scalar multiplication.

Hence \( U \) is a subspace of \( \nR^2 \) by the subspace test (@thm-subspace-test).
:::

Change the right-hand side from \( 0 \) to \( 3 \), and everything breaks.

::: {#exm-line-not-subspace}
[A Line Missing the Origin]

Show that \( L = \{ (x, y) \in \nR^2 : x + 2y = 3 \} \) is **not** a subspace of \( \nR^2 \).
:::

::: {.solution}
Condition (1) fails: the zero vector has \( 0 + 2 \cdot 0 = 0 \ne 3 \), so \( \0 \notin L \). By the subspace test (@thm-subspace-test), \( L \) is not a subspace of \( \nR^2 \).
:::

The other two conditions fail as well, as we saw in the previous section: \( (3, 0) + (1, 1) = (4, 1) \notin L \), and \( 2(3, 0) = (6, 0) \notin L \). One failure is enough, though, and (1) is the cheapest to find.

\begin{center}
\begin{tikzpicture}[scale=0.8]
  \draw[->] (-4.2,0) -- (4.2,0) node[right] {$x$};
  \draw[->] (0,-2.2) -- (0,2.6) node[above] {$y$};
  \draw[very thick] (-4,2) -- (4,-2) node[below right] {$x + 2y = 0$};
  \draw[very thick, dashed] (-1,2) -- (4.2,-0.6) node[above right] {$x + 2y = 3$};
  \fill (0,0) circle (2pt) node[below left] {$\mathbf{0}$};
\end{tikzpicture}
\end{center}

The solid line \( U \) passes through the origin; the dashed line \( L \) is parallel to it and misses the origin. The line \( L \) is a translate of a subspace, a kind of set we will study in Chapter 3, but it is not a subspace.

The line \( U \) is the set of solutions of one homogeneous equation. The same three checks work for any number of homogeneous equations, written as one matrix equation.

::: {#exm-null-space-subspace}
[Solutions of a Homogeneous System]

Let \( \A \in M_{m \times n}(F) \). Show that \( N = \{ \x \in F^n : \A\x = \0 \} \) is a subspace of \( F^n \).
:::

::: {.solution}
By definition, \( N \) is a subset of \( F^n \). Recall that \( F^n = M_{n \times 1}(F) \), so \( \A\x \in F^m \) is a matrix product, and we may use @thm-matrix-multiplication-properties.

**(1) Zero vector.** By the zero rule of @thm-matrix-multiplication-properties, \( \A\0 = \0 \), where the first \( \0 \) is the zero column in \( F^n \) and the second is the zero column in \( F^m \). Therefore \( \0 \in N \).

**(2) Closed under addition.** Let \( \x, \y \in N \), so that \( \A\x = \0 \) and \( \A\y = \0 \). By distributivity (@thm-matrix-multiplication-properties),
\[
\A(\x + \y) = \A\x + \A\y = \0 + \0 = \0.
\]
Therefore \( \x + \y \in N \). This shows that \( N \) is closed under addition.

**(3) Closed under scalar multiplication.** Let \( a \in F \) and \( \x \in N \). By the scalar rule of @thm-matrix-multiplication-properties and @thm-scalar-zero-vector in \( F^m \),
\[
\A(a\x) = a(\A\x) = a\0 = \0.
\]
Therefore \( a\x \in N \). This shows that \( N \) is closed under scalar multiplication.

Hence \( N \) is a subspace of \( F^n \) by the subspace test (@thm-subspace-test).
:::

With \( \A = \begin{pmatrix} 1 & 2 \end{pmatrix} \) and \( F = \nR \), this is @exm-line-subspace again, and with \( \A = \begin{pmatrix} 1 & 1 & -1 \end{pmatrix} \) it is the plane \( P \) from the start of the section. The word **homogeneous** (right-hand side \( \0 \)) is essential: @exm-line-not-subspace is a system with right-hand side \( 3 \). This subspace will be called the null space of \( \A \) in Chapter 2.

Next, polynomials. The pair "degree at most \( n \)" and "degree exactly \( n \)" is another minimal change. The previous section checked the first of them by hand; here it is as a three-check move.

::: {#exm-poly-degree-bound}
[Polynomials of Bounded Degree]

Let \( n \in \nN \). Show that \( F[x]_{\le n} \) is a subspace of \( F[x] \).
:::

::: {.solution}
By @def-polynomials-bounded-degree, \( F[x]_{\le n} \) is a subset of \( F[x] \).

**(1) Zero vector.** The zero polynomial has degree \( -\infty \le n \) (@def-degree). Therefore \( \0 \in F[x]_{\le n} \).

**(2) Closed under addition.** Let \( p, q \in F[x]_{\le n} \), so that \( \deg p \le n \) and \( \deg q \le n \). By @thm-degree-of-sum, \( \deg(p + q) \le \max(\deg p, \deg q) \le n \). Therefore \( p + q \in F[x]_{\le n} \). This shows that \( F[x]_{\le n} \) is closed under addition.

**(3) Closed under scalar multiplication.** Let \( c \in F \) and \( p = a_0 + a_1 x + \dots + a_n x^n \in F[x]_{\le n} \). Then \( cp = ca_0 + ca_1 x + \dots + ca_n x^n \), whose coefficients of \( x^k \) for \( k > n \) are all \( 0 \). So \( \deg(cp) \le n \), and therefore \( cp \in F[x]_{\le n} \). This shows that \( F[x]_{\le n} \) is closed under scalar multiplication.

Hence \( F[x]_{\le n} \) is a subspace of \( F[x] \) by the subspace test (@thm-subspace-test).
:::

::: {#exm-poly-exact-degree}
[Polynomials of Exact Degree]

Let \( n \in \nN \). Show that \( F[x]_{=n} \) is **not** a subspace of \( F[x] \).
:::

::: {.solution}
Condition (1) fails: the zero polynomial has degree \( -\infty \ne n \), so \( \0 \notin F[x]_{=n} \). By the subspace test (@thm-subspace-test), \( F[x]_{=n} \) is not a subspace of \( F[x] \).
:::

Even if we added the zero polynomial by hand, condition (2) would still fail for \( n \ge 1 \): the polynomials \( x^n + 1 \) and \( -x^n \) have degree exactly \( n \), but their sum is the constant \( 1 \), of degree \( 0 \). The leading terms cancel, and nothing in "degree exactly \( n \)" prevents it.

The same move works in function spaces. Here the facts we need come from calculus.

::: {#exm-differentiable-functions}
[Differentiable Functions]

Let \( D \) be the set of differentiable functions \( \nR \to \nR \). Show that \( D \) is a subspace of \( \nR^{\nR} \).
:::

::: {.solution}
Every element of \( D \) is a function \( \nR \to \nR \), so \( D \subseteq \nR^{\nR} \).

**(1) Zero vector.** The zero vector of \( \nR^{\nR} \) is the zero function (@exm-vector-spaces), which is constant and hence differentiable. Therefore \( \0 \in D \).

**(2) Closed under addition.** Let \( f, g \in D \). By the sum rule of calculus, \( f + g \) is differentiable, with \( (f + g)' = f' + g' \). Therefore \( f + g \in D \). This shows that \( D \) is closed under addition.

**(3) Closed under scalar multiplication.** Let \( a \in \nR \) and \( f \in D \). By the constant multiple rule, \( af \) is differentiable, with \( (af)' = af' \). Therefore \( af \in D \). This shows that \( D \) is closed under scalar multiplication.

Hence \( D \) is a subspace of \( \nR^{\nR} \) by the subspace test (@thm-subspace-test).
:::

The same three checks show that the continuous functions \( \nR \to \nR \) form a subspace of \( \nR^{\nR} \), and that \( D \) is a subspace of it. A subspace of a subspace is a subspace, since the operations are the same throughout.

Finally, two families of matrices. Each uses one rule from Chapter 0 for all three checks.

::: {#exm-symmetric-matrices}
[Symmetric Matrices]

Show that the set \( S = \{ \A \in M_n(F) : \A\tp = \A \} \) of symmetric matrices (@def-symmetric-matrix) is a subspace of \( M_n(F) \).
:::

::: {.solution}
By definition, \( S \) is a subset of \( M_n(F) \).

**(1) Zero vector.** Every entry of the zero matrix is \( 0 \), so \( (0)_{ji} = 0 = (0)_{ij} \) for all \( i, j \), and the zero matrix is symmetric. Therefore \( \0 \in S \).

**(2) Closed under addition.** Let \( \A, \B \in S \), so that \( \A\tp = \A \) and \( \B\tp = \B \). By @thm-transpose-properties,
\[
(\A + \B)\tp = \A\tp + \B\tp = \A + \B.
\]
Therefore \( \A + \B \in S \). This shows that \( S \) is closed under addition.

**(3) Closed under scalar multiplication.** Let \( c \in F \) and \( \A \in S \). By @thm-transpose-properties, \( (c\A)\tp = c\A\tp = c\A \). Therefore \( c\A \in S \). This shows that \( S \) is closed under scalar multiplication.

Hence \( S \) is a subspace of \( M_n(F) \) by the subspace test (@thm-subspace-test).
:::

::: {#exm-trace-free-matrices}
[Trace-Free Matrices]

Show that the set \( T = \{ \A \in M_n(F) : \tr \A = 0 \} \) of trace-free matrices is a subspace of \( M_n(F) \).
:::

::: {.solution}
By definition, \( T \) is a subset of \( M_n(F) \).

**(1) Zero vector.** The zero matrix has trace \( 0 + \dots + 0 = 0 \). Therefore \( \0 \in T \).

**(2) Closed under addition.** Let \( \A, \B \in T \), so that \( \tr \A = \tr \B = 0 \). By @thm-trace-properties, \( \tr(\A + \B) = \tr \A + \tr \B = 0 + 0 = 0 \). Therefore \( \A + \B \in T \). This shows that \( T \) is closed under addition.

**(3) Closed under scalar multiplication.** Let \( c \in F \) and \( \A \in T \). By @thm-trace-properties, \( \tr(c\A) = c \tr \A = c \cdot 0 = 0 \). Therefore \( c\A \in T \). This shows that \( T \) is closed under scalar multiplication.

Hence \( T \) is a subspace of \( M_n(F) \) by the subspace test (@thm-subspace-test).
:::

The pattern in the last two examples, and in @exm-null-space-subspace, is the same: the condition defining the set is "some rule that respects sums and scalar multiples sends the element to zero". Chapter 3 gives such rules a name, linear maps, and this pattern becomes a single theorem about their kernels.

## Non-examples

Here are two more subsets of \( \nR^2 \) that fail, each in a different way.

- **The unit circle** \( \{ (x, y) : x^2 + y^2 = 1 \} \) fails (1), since \( 0^2 + 0^2 \ne 1 \). It fails (2) and (3) as well: \( (1, 0) + (0, 1) = (1, 1) \) and \( 2(1, 0) = (2, 0) \) are not on the circle.
- **The set \( Q = \{ (x, y) : xy \ge 0 \} \)**, the first and third quadrants together with both axes. Here (1) holds, since \( 0 \cdot 0 = 0 \ge 0 \). Condition (3) holds too: if \( xy \ge 0 \) and \( a \in \nR \), then \( (ax)(ay) = a^2 xy \ge 0 \). But (2) fails: \( (1, 0) \) and \( (0, -1) \) lie in \( Q \), while their sum \( (1, -1) \) has \( 1 \cdot (-1) = -1 < 0 \). So \( Q \) is not a subspace.

The set \( Q \) shows that (3) does not imply (2). The next check shows that (2) does not imply (3).

::: {.check}
Find a subset of \( \nR^2 \) that contains \( \0 \) and is closed under addition, but is not a subspace. Which condition of the subspace test fails?
:::

::: {.solution}
Take the closed first quadrant \( U = \{ (x, y) : x \ge 0 \text{ and } y \ge 0 \} \). It contains \( (0, 0) \), and if \( x_1, y_1, x_2, y_2 \ge 0 \), then \( x_1 + x_2 \ge 0 \) and \( y_1 + y_2 \ge 0 \), so it is closed under addition. Condition (3) fails: \( (1, 0) \in U \) but \( (-1)(1, 0) = (-1, 0) \notin U \). Another answer is \( \nZ^2 \): it contains \( \0 \) and is closed under addition, but \( \tfrac12 (1, 0) \notin \nZ^2 \).
:::

## Why this definition

The definition insists on **the same** operations. This is not a formality. The positive reals \( \nR_{>0} \) form a vector space over \( \nR \) (@exm-positive-reals), and \( \nR_{>0} \) is a subset of the vector space \( \nR \). But \( \nR_{>0} \) is **not** a subspace of \( \nR \): with the operations of \( \nR \), it does not contain the zero vector \( 0 \), and \( (-1) \cdot 1 = -1 \) leaves it. Its vector space structure uses different operations, multiplication and powers, and those do not count.

The definition also keeps the field. For example, \( \nR^2 \) is a subset of \( \nC^2 \), and it is closed under addition and under multiplication by **real** scalars. But it is not a subspace of \( \nC^2 \) over \( \nC \), because \( i(1, 0) = (i, 0) \notin \nR^2 \). Condition (3) quantifies over **every** scalar of the field.

Finally, why "(1) \( \0 \in U \)" rather than "\( U \) is non-empty"? The two are equivalent given (3), as the remark after the test explains. We choose the version that is quicker to check and quicker to refute.

## Intersections of subspaces

Given several subspaces, can we build new ones? The first way is to take the vectors they have in common. Recall from @def-indexed-family that the intersection of a **non-empty** family of sets \( (U_i)_{i \in I} \) consists of the elements lying in every \( U_i \).

::: {#thm-intersection-subspaces}
[Intersection of Subspaces]

Let \( V \) be a vector space over \( F \), and let \( (U_i)_{i \in I} \) be a family of subspaces of \( V \) with \( I \) non-empty. Then \( \bigcap_{i \in I} U_i \) is a subspace of \( V \).
:::

::: {.proof}
Let \( U = \bigcap_{i \in I} U_i \). Each \( U_i \) is a subset of \( V \), so \( U \subseteq V \). We use the subspace test (@thm-subspace-test) for \( U \), and for each \( U_i \) its direction \( (\Rightarrow) \).

(1) For every \( i \in I \), \( \0 \in U_i \), since \( U_i \) is a subspace. Therefore \( \0 \in U \).

(2) Let \( \u, \w \in U \). Then \( \u, \w \in U_i \) for every \( i \in I \). Since each \( U_i \) is closed under addition, \( \u + \w \in U_i \) for every \( i \in I \). Therefore \( \u + \w \in U \). This shows that \( U \) is closed under addition.

(3) Let \( a \in F \) and \( \u \in U \). Then \( \u \in U_i \) for every \( i \in I \), and since each \( U_i \) is closed under scalar multiplication, \( a\u \in U_i \) for every \( i \in I \). Therefore \( a\u \in U \). This shows that \( U \) is closed under scalar multiplication.

Hence \( U \) is a subspace of \( V \) by the subspace test (@thm-subspace-test).
:::

The index set may be infinite, and this matters. In the next section we will build the smallest subspace containing a given set of vectors, and one way to describe it is as the intersection of **all** subspaces containing that set.

For two subspaces, the theorem gives familiar pictures: two different planes through the origin in \( \nR^3 \) meet in a line through the origin. It also explains @exm-null-space-subspace from a new angle. The solution set of \( \A\x = \0 \) is the intersection of the solution sets of its \( m \) individual equations, each of which is a subspace of \( F^n \). An algebraic example: in \( M_2(F) \), the matrices that are both symmetric and trace-free (@exm-symmetric-matrices, @exm-trace-free-matrices) are those of the form \( \begin{pmatrix} a & b \\ b & -a \end{pmatrix} \), and they form a subspace.

## Unions of subspaces

Intersections behave well. Unions do not, and the reason is visible in the simplest picture.

::: {#exm-union-axes}
[The Union of the Two Axes]

In \( \nR^2 \), let \( U = \{ (x, 0) : x \in \nR \} \) be the \( x \)-axis and \( W = \{ (0, y) : y \in \nR \} \) the \( y \)-axis. Show that \( U \) and \( W \) are subspaces of \( \nR^2 \), but \( U \cup W \) is not.
:::

::: {.solution}
The \( x \)-axis is the solution set of the homogeneous equation \( y = 0 \), that is, of \( \A\x = \0 \) with \( \A = \begin{pmatrix} 0 & 1 \end{pmatrix} \). By @exm-null-space-subspace, \( U \) is a subspace. In the same way \( W \) is the solution set of \( x = 0 \), so it is a subspace.

For the union, condition (2) fails. We have \( (1, 0) \in U \subseteq U \cup W \) and \( (0, 1) \in W \subseteq U \cup W \), but
\[
(1, 0) + (0, 1) = (1, 1),
\]
which is on neither axis, since both of its entries are non-zero. So \( (1, 1) \notin U \cup W \), and \( U \cup W \) is not a subspace of \( \nR^2 \).
:::

The union passes (1) and (3): it contains \( \0 \), and scaling a vector on an axis keeps it on that axis. Only addition breaks it, by mixing a vector from each axis. That observation is the whole proof of the general fact.

::: {#prp-union-subspaces}
[Union of Two Subspaces]

Let \( V \) be a vector space over \( F \), and let \( U \) and \( W \) be subspaces of \( V \). Then \( U \cup W \) is a subspace of \( V \) if and only if \( U \subseteq W \) or \( W \subseteq U \).
:::

::: {.idea}
The direction \( (\Leftarrow) \) is immediate, because the union is then just the bigger of the two. For \( (\Rightarrow) \), a statement of the form "one of two inclusions holds" invites contradiction. If neither inclusion holds, there is a vector \( \u \) of \( U \) outside \( W \) and a vector \( \w \) of \( W \) outside \( U \), exactly like \( (1, 0) \) and \( (0, 1) \) for the axes. Look at \( \u + \w \). It must lie in \( U \) or in \( W \). If it lies in \( U \), subtracting \( \u \) keeps us in \( U \) and leaves \( \w \), which is not in \( U \).
:::

::: {.proof}
\( (\Leftarrow) \) If \( U \subseteq W \), then \( U \cup W = W \), which is a subspace. If \( W \subseteq U \), then \( U \cup W = U \), which is a subspace.

\( (\Rightarrow) \) Suppose \( U \cup W \) is a subspace of \( V \), and suppose, for a contradiction, that \( U \not\subseteq W \) and \( W \not\subseteq U \). Then there exist \( \u \in U \) with \( \u \notin W \), and \( \w \in W \) with \( \w \notin U \). Both lie in \( U \cup W \), so \( \u + \w \in U \cup W \) by condition (2) of the subspace test (@thm-subspace-test).

*Case 1: \( \u + \w \in U \).* Since \( U \) is a subspace and \( \u \in U \), condition (3) gives \( (-1)\u \in U \), and \( (-1)\u = -\u \) by @thm-negation-scalar. By condition (2) for \( U \), \( (\u + \w) + (-\u) \in U \). By (VS1), (VS2), (VS4) and (VS3),
\[
(\u + \w) + (-\u) = \w + (\u + (-\u)) = \w + \0 = \w.
\]
So \( \w \in U \), contradicting the choice of \( \w \).

*Case 2: \( \u + \w \in W \).* Swapping the roles of \( U \) and \( W \), and of \( \u \) and \( \w \), in Case 1 gives \( \u \in W \), contradicting the choice of \( \u \).

Both cases lead to a contradiction. Hence \( U \subseteq W \) or \( W \subseteq U \).
:::

::: {.warning}
**Do not combine subspaces by taking their union.** Apart from the case where one subspace already contains the other, the union of two subspaces is never a subspace, by @prp-union-subspaces. The two axes in \( \nR^2 \) are the standard failing case: their union misses \( (1, 1) \), and in fact misses every vector with two non-zero entries.
:::

The right way to combine two subspaces \( U \) and \( W \) is to take all sums \( \u + \w \) with \( \u \in U \) and \( \w \in W \). For the two axes this gives all of \( \nR^2 \). This construction, the sum of subspaces, is the subject of a later section of this chapter; @exr-subspaces-c2 gives a preview.

We now have a supply of vector spaces for free: every subspace of a known space is one, and every theorem of the previous section applies to it. In the next section we ask a sharper question. Given a few vectors, what is the smallest subspace that contains them? Its answer, the span, is the first step toward measuring the size of a vector space.

## Exercises

### A. Check your understanding

::: {#exr-subspaces-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define what it means for a subset \( U \) of a vector space \( V \) over \( F \) to be a subspace.
2. State the subspace test.
3. True or false: \( \varnothing \) is a subspace of every vector space. Justify your answer.
4. True or false: if \( U \) is a subspace of \( V \) and \( W \) is a subspace of \( U \), then \( W \) is a subspace of \( V \). Justify your answer.
5. True or false: the union of two subspaces is never a subspace. Justify your answer.
6. Which condition of the subspace test would you check first to show that \( \{ (x, y, z) \in \nR^3 : x + y + z = 1 \} \) is not a subspace of \( \nR^3 \)? Carry out the check.
:::
:::

::: {.solution}
(a) See @def-subspace: \( U \) is closed under the addition and scalar multiplication of \( V \), and with these operations it is a vector space over \( F \).

(b) See @thm-subspace-test: \( U \subseteq V \) is a subspace if and only if \( \0 \in U \), \( U \) is closed under addition, and \( U \) is closed under scalar multiplication.

(c) False. The empty set does not contain \( \0 \), so condition (1) fails (@exm-trivial-subspaces).

(d) True. Since \( W \) is a subspace of \( U \), it contains the zero vector of \( U \), which is \( \0 \) (the proof of @thm-subspace-test shows the zero vector of a subspace is the zero vector of the big space). The operations of \( U \) are those of \( V \), so closure of \( W \) under the operations of \( U \) is closure under the operations of \( V \). By the subspace test (@thm-subspace-test), \( W \) is a subspace of \( V \).

(e) False. If \( U \subseteq W \), then \( U \cup W = W \) is a subspace (@prp-union-subspaces). For example, \( \{\0\} \cup V = V \).

(f) Condition (1). The zero vector has \( 0 + 0 + 0 = 0 \ne 1 \), so it is not in the set, and the set is not a subspace.
:::

### B. Practice

::: {#exr-subspaces-b1}
[B1: Which Are Subspaces?]

Determine which of the following are subspaces of the given vector space over \( \nR \). Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \{ (x, y, z) \in \nR^3 : x - 2y + z = 0 \} \) in \( \nR^3 \).
2. \( \{ (x, y, z) \in \nR^3 : x = y^2 \} \) in \( \nR^3 \).
3. \( \{ \A \in M_2(\nR) : \A \text{ is invertible} \} \) in \( M_2(\nR) \).
4. \( \{ \A \in M_2(\nR) : a_{12} = 2a_{21} \} \) in \( M_2(\nR) \).
5. \( \{ p \in \nR[x] : p(2) = 0 \text{ and } p'(2) = 0 \} \) in \( \nR[x] \), where \( p' \) is the derivative of \( p \).
6. The even functions \( \{ f \in \nR^{\nR} : f(-t) = f(t) \text{ for all } t \in \nR \} \) in \( \nR^{\nR} \).
7. \( \{ f \in \nR^{\nR} : f(0) = 1 \} \) in \( \nR^{\nR} \).
8. The continuous functions \( \nR \to \nR \), in \( \nR^{\nR} \).
:::
:::

::: {.solution}
(a) A subspace. It is \( \{ \x \in \nR^3 : \A\x = \0 \} \) with \( \A = \begin{pmatrix} 1 & -2 & 1 \end{pmatrix} \), a subspace by @exm-null-space-subspace.

(b) Not a subspace: (3) fails. The vector \( (1, 1, 0) \) lies in the set, since \( 1 = 1^2 \). But \( 2(1, 1, 0) = (2, 2, 0) \) does not, since \( 2 \ne 2^2 \).

(c) Not a subspace: (1) fails. The zero matrix is not invertible, because \( 0 \cdot \B = 0 \ne \I_2 \) for every \( \B \in M_2(\nR) \).

(d) A subspace. Call the set \( U \).

**(1)** The zero matrix has \( a_{12} = 0 = 2 \cdot 0 = 2a_{21} \). Therefore \( \0 \in U \).

**(2)** Let \( \A, \B \in U \), so \( a_{12} = 2a_{21} \) and \( b_{12} = 2b_{21} \). The \( (1, 2) \)-entry of \( \A + \B \) is \( a_{12} + b_{12} = 2a_{21} + 2b_{21} = 2(a_{21} + b_{21}) \), which is twice its \( (2, 1) \)-entry. Therefore \( \A + \B \in U \). This shows that \( U \) is closed under addition.

**(3)** Let \( c \in \nR \) and \( \A \in U \). The \( (1, 2) \)-entry of \( c\A \) is \( ca_{12} = c(2a_{21}) = 2(ca_{21}) \), twice its \( (2, 1) \)-entry. Therefore \( c\A \in U \). This shows that \( U \) is closed under scalar multiplication.

Hence \( U \) is a subspace of \( M_2(\nR) \) by the subspace test (@thm-subspace-test).

(e) A subspace. Call the set \( U \). We use @thm-evaluation-respects-operations for values, and the sum and constant multiple rules for derivatives.

**(1)** The zero polynomial has value \( 0 \) at \( 2 \), and its derivative is the zero polynomial, also with value \( 0 \) at \( 2 \). Therefore \( \0 \in U \).

**(2)** Let \( p, q \in U \). Then \( (p + q)(2) = p(2) + q(2) = 0 \) and \( (p + q)'(2) = p'(2) + q'(2) = 0 \). Therefore \( p + q \in U \). This shows that \( U \) is closed under addition.

**(3)** Let \( c \in \nR \) and \( p \in U \). Then \( (cp)(2) = c\,p(2) = 0 \) and \( (cp)'(2) = c\,p'(2) = 0 \). Therefore \( cp \in U \). This shows that \( U \) is closed under scalar multiplication.

Hence \( U \) is a subspace of \( \nR[x] \) by the subspace test (@thm-subspace-test).

(f) A subspace. Call the set \( E \).

**(1)** The zero function satisfies \( \0(-t) = 0 = \0(t) \) for all \( t \). Therefore \( \0 \in E \).

**(2)** Let \( f, g \in E \). For every \( t \in \nR \), \( (f + g)(-t) = f(-t) + g(-t) = f(t) + g(t) = (f + g)(t) \). Therefore \( f + g \in E \). This shows that \( E \) is closed under addition.

**(3)** Let \( a \in \nR \) and \( f \in E \). For every \( t \in \nR \), \( (af)(-t) = af(-t) = af(t) = (af)(t) \). Therefore \( af \in E \). This shows that \( E \) is closed under scalar multiplication.

Hence \( E \) is a subspace of \( \nR^{\nR} \) by the subspace test (@thm-subspace-test).

(g) Not a subspace: (1) fails. The zero function has value \( 0 \ne 1 \) at \( 0 \).

(h) A subspace. **(1)** The zero function is constant, hence continuous. **(2)** A sum of continuous functions is continuous. **(3)** A constant multiple of a continuous function is continuous. Hence the continuous functions form a subspace of \( \nR^{\nR} \) by the subspace test (@thm-subspace-test).
:::

::: {#exr-subspaces-b2}
[B2: Matrices Commuting with a Given Matrix]

Fix \( \B \in M_n(F) \), and let \( C(\B) = \{ \A \in M_n(F) : \A\B = \B\A \} \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( C(\B) \) is a subspace of \( M_n(F) \).
2. Let \( n = 2 \), \( F = \nR \) and \( \B = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix} \). Find all \( \A \in C(\B) \). Hence describe \( C(\B) \) in words.
:::
:::

::: {.solution}
(a) By definition, \( C(\B) \subseteq M_n(F) \). We use @thm-matrix-multiplication-properties throughout.

**(1)** By the zero rule, \( 0\B = 0 = \B0 \). Therefore \( \0 \in C(\B) \).

**(2)** Let \( \A_1, \A_2 \in C(\B) \), so \( \A_1 \B = \B\A_1 \) and \( \A_2 \B = \B\A_2 \). By distributivity,
\[
(\A_1 + \A_2)\B = \A_1 \B + \A_2 \B = \B\A_1 + \B\A_2 = \B(\A_1 + \A_2).
\]
Therefore \( \A_1 + \A_2 \in C(\B) \). This shows that \( C(\B) \) is closed under addition.

**(3)** Let \( c \in F \) and \( \A \in C(\B) \). By the scalar rule, \( (c\A)\B = c(\A\B) = c(\B\A) = \B(c\A) \). Therefore \( c\A \in C(\B) \). This shows that \( C(\B) \) is closed under scalar multiplication.

Hence \( C(\B) \) is a subspace of \( M_n(F) \) by the subspace test (@thm-subspace-test).

(b) Let \( \A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \). Then
\[
\A\B = \begin{pmatrix} a & 2b \\ c & 2d \end{pmatrix}, \qquad \B\A = \begin{pmatrix} a & b \\ 2c & 2d \end{pmatrix}.
\]
So \( \A\B = \B\A \) if and only if \( 2b = b \) and \( c = 2c \), that is, \( b = 0 \) and \( c = 0 \). Hence \( C(\B) \) is the set of diagonal matrices \( \begin{pmatrix} a & 0 \\ 0 & d \end{pmatrix} \) with \( a, d \in \nR \).
:::

::: {#exr-subspaces-b3}
[B3: Intersection and Union of Two Planes]

In \( \nR^3 \), let \( U = \{ (x, y, z) : x + y + z = 0 \} \) and \( W = \{ (x, y, z) : x - y = 0 \} \).

::: {.enumerate options="label=(\alph*)"}
1. Explain why \( U \) and \( W \) are subspaces of \( \nR^3 \), and find \( U \cap W \).
2. Find \( \u \in U \) with \( \u \notin W \) and \( \w \in W \) with \( \w \notin U \). Hence show directly that \( U \cup W \) is not a subspace of \( \nR^3 \).
:::
:::

::: {.solution}
(a) \( U \) and \( W \) are the solution sets of \( \A\x = \0 \) for \( \A = \begin{pmatrix} 1 & 1 & 1 \end{pmatrix} \) and \( \A = \begin{pmatrix} 1 & -1 & 0 \end{pmatrix} \), so they are subspaces by @exm-null-space-subspace. A vector \( (x, y, z) \) lies in \( U \cap W \) exactly when \( x + y + z = 0 \) and \( x = y \). Substituting \( y = x \) gives \( z = -2x \). Hence
\[
U \cap W = \{ (t, t, -2t) : t \in \nR \},
\]
a line through the origin, which is a subspace by @thm-intersection-subspaces.

(b) Take \( \u = (1, -1, 0) \), which lies in \( U \) since \( 1 - 1 + 0 = 0 \), but not in \( W \) since \( 1 - (-1) = 2 \ne 0 \). Take \( \w = (1, 1, 0) \), which lies in \( W \), but not in \( U \) since \( 1 + 1 + 0 = 2 \ne 0 \). Both lie in \( U \cup W \). Their sum is \( (2, 0, 0) \), which is not in \( U \) (as \( 2 + 0 + 0 \ne 0 \)) and not in \( W \) (as \( 2 - 0 \ne 0 \)). Hence \( U \cup W \) is not closed under addition, and it is not a subspace of \( \nR^3 \).
:::

### C. Going deeper

::: {#exr-subspaces-c1}
[C1: Covering a Space by Subspaces]

::: {.enumerate options="label=(\alph*)"}
1. Let \( V \) be a vector space over any field \( F \). Prove that \( V \) is not the union of two proper subspaces.
2. Show that \( \nF_2^2 \) is the union of three proper subspaces.
:::

*Hint: for (a), use @prp-union-subspaces.*
:::

::: {.solution}
(a) Suppose, for a contradiction, that \( V = U \cup W \) with \( U \) and \( W \) proper subspaces of \( V \). Then \( U \cup W = V \) is a subspace of \( V \), so by @prp-union-subspaces, \( U \subseteq W \) or \( W \subseteq U \). In the first case \( V = U \cup W = W \), and in the second \( V = U \). Either way one of the subspaces equals \( V \), contradicting that both are proper. Hence \( V \) is not the union of two proper subspaces.

(b) The space \( \nF_2^2 \) has the four elements \( (0, 0), (1, 0), (0, 1), (1, 1) \). Let \( \v \) be one of the three non-zero elements, and let \( U_{\v} = \{ \0, \v \} \). We check that \( U_{\v} \) is a subspace with the three-check move.

**(1)** \( \0 \in U_{\v} \) by construction.

**(2)** The possible sums are \( \0 + \0 = \0 \), \( \0 + \v = \v + \0 = \v \), and \( \v + \v = (1 + 1)\v = 0\v = \0 \), using (VS8), (VS6), \( 1 + 1 = 0 \) in \( \nF_2 \), and @thm-zero-scalar-mult. All lie in \( U_{\v} \), so \( U_{\v} \) is closed under addition.

**(3)** The only scalars are \( 0 \) and \( 1 \). For \( \u \in U_{\v} \), \( 0\u = \0 \) by @thm-zero-scalar-mult and \( 1\u = \u \) by (VS8), both in \( U_{\v} \). So \( U_{\v} \) is closed under scalar multiplication.

Hence each \( U_{\v} \) is a subspace. Each has two elements, so it is proper. Every element of \( \nF_2^2 \) is \( \0 \) or one of the three non-zero vectors, so
\[
\nF_2^2 = U_{(1,0)} \cup U_{(0,1)} \cup U_{(1,1)}.
\]
So three proper subspaces can cover a vector space, although (a) shows two never can.
:::

::: {#exr-subspaces-c2}
[C2: The Sum of Two Subspaces]

Let \( U \) and \( W \) be subspaces of a vector space \( V \) over \( F \), and let
\[
U + W = \{ \u + \w : \u \in U, \ \w \in W \}.
\]

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( U + W \) is a subspace of \( V \) containing both \( U \) and \( W \).
2. Prove that if \( X \) is a subspace of \( V \) with \( U \cup W \subseteq X \), then \( U + W \subseteq X \).
3. For the two axes \( U \) and \( W \) of @exm-union-axes, show that \( U + W = \nR^2 \).
:::
:::

::: {.solution}
(a) Every \( \u + \w \) is a vector of \( V \), so \( U + W \subseteq V \).

**(1)** Since \( \0 \in U \) and \( \0 \in W \), and \( \0 + \0 = \0 \) by (VS3), we get \( \0 \in U + W \).

**(2)** Let \( \u_1 + \w_1 \) and \( \u_2 + \w_2 \) be in \( U + W \), with \( \u_1, \u_2 \in U \) and \( \w_1, \w_2 \in W \). By (VS1) and (VS2),
\[
(\u_1 + \w_1) + (\u_2 + \w_2) = (\u_1 + \u_2) + (\w_1 + \w_2).
\]
Since \( U \) and \( W \) are closed under addition, \( \u_1 + \u_2 \in U \) and \( \w_1 + \w_2 \in W \). Therefore the sum lies in \( U + W \). This shows that \( U + W \) is closed under addition.

**(3)** Let \( a \in F \) and \( \u + \w \in U + W \). By (VS5), \( a(\u + \w) = a\u + a\w \), with \( a\u \in U \) and \( a\w \in W \) by closure. Therefore \( a(\u + \w) \in U + W \). This shows that \( U + W \) is closed under scalar multiplication.

Hence \( U + W \) is a subspace of \( V \). For \( \u \in U \), we have \( \u = \u + \0 \) with \( \0 \in W \), so \( \u \in U + W \); thus \( U \subseteq U + W \). Swapping the roles of \( U \) and \( W \) gives \( W \subseteq U + W \), using (VS1).

(b) Let \( \u + \w \in U + W \) with \( \u \in U \) and \( \w \in W \). Then \( \u, \w \in U \cup W \subseteq X \). Since \( X \) is a subspace, it is closed under addition, so \( \u + \w \in X \). Hence \( U + W \subseteq X \).

(c) By (a), \( U + W \subseteq \nR^2 \). Conversely, let \( (x, y) \in \nR^2 \). Then \( (x, y) = (x, 0) + (0, y) \) with \( (x, 0) \in U \) and \( (0, y) \in W \), so \( (x, y) \in U + W \). Hence \( U + W = \nR^2 \), whereas \( U \cup W \) is only the two axes.
:::

::: {#exr-subspaces-c3}
[C3: A One-Line Test, and a Test over \( \nF_2 \)]

Let \( V \) be a vector space over \( F \) and \( U \subseteq V \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( U \) is a subspace of \( V \) if and only if \( U \ne \varnothing \) and \( a\u + \w \in U \) for all \( a \in F \) and \( \u, \w \in U \).
2. Suppose \( F = \nF_2 \). Prove that \( U \) is a subspace of \( V \) if and only if \( \0 \in U \) and \( U \) is closed under addition.
3. Show by an example that the statement in (b) is false over \( \nR \).
:::
:::

::: {.solution}
(a) \( (\Rightarrow) \) Suppose \( U \) is a subspace. By the subspace test (@thm-subspace-test), \( \0 \in U \), so \( U \ne \varnothing \). For \( a \in F \) and \( \u, \w \in U \), condition (3) gives \( a\u \in U \), and then condition (2) gives \( a\u + \w \in U \).

\( (\Leftarrow) \) Suppose \( U \ne \varnothing \) and \( a\u + \w \in U \) for all \( a \in F \), \( \u, \w \in U \). Pick \( \u_0 \in U \). Taking \( a = -1 \) and \( \u = \w = \u_0 \), and using @thm-negation-scalar and (VS4),
\[
(-1)\u_0 + \u_0 = -\u_0 + \u_0 = \0 \in U,
\]
where \( -\u_0 + \u_0 = \u_0 + (-\u_0) \) by (VS1). This is condition (1). For \( \u, \w \in U \), taking \( a = 1 \) and using (VS8) gives \( \u + \w = 1\u + \w \in U \), which is (2). For \( a \in F \) and \( \u \in U \), taking \( \w = \0 \in U \) and using (VS3) gives \( a\u = a\u + \0 \in U \), which is (3). By the subspace test (@thm-subspace-test), \( U \) is a subspace.

(b) \( (\Rightarrow) \) This is part of the subspace test (@thm-subspace-test). \( (\Leftarrow) \) Suppose \( \0 \in U \) and \( U \) is closed under addition. The only scalars in \( \nF_2 \) are \( 0 \) and \( 1 \). For \( \u \in U \), \( 0\u = \0 \in U \) by @thm-zero-scalar-mult, and \( 1\u = \u \in U \) by (VS8). So \( U \) is closed under scalar multiplication, and by the subspace test (@thm-subspace-test) \( U \) is a subspace.

(c) Take \( V = \nR^2 \) and \( U = \nZ^2 \). Then \( \0 \in U \), and the sum of two integer vectors is an integer vector. But \( \tfrac12 (1, 0) = (\tfrac12, 0) \notin U \), so \( U \) is not a subspace. Over \( \nR \) there are many more scalars to test than \( 0 \) and \( 1 \).
:::
