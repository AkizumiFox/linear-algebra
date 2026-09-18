# Vector Spaces

Chapter 0 met several kinds of objects that can be added and scaled: pairs of real numbers, polynomials, matrices. Each time we checked the same handful of rules by hand. This section collects those rules into one definition, the vector space, and proves the first consequences once, so that they hold in every example at the same time.

## One set of rules in three places

Start with the plane \( \nR^2 \). A pair \( \u = (3, 1) \) can be pictured as an arrow from the origin to the point \( (3, 1) \). Two arrows are added tip to tail, which is the same as taking the diagonal of the parallelogram they span, and an arrow is scaled by stretching it.

\begin{center}
\begin{tikzpicture}[scale=1.1]
  \draw[->] (-0.4,0) -- (4.6,0) node[right] {$x$};
  \draw[->] (0,-0.4) -- (0,3.4) node[above] {$y$};
  \draw[dashed] (3,1) -- (4,3);
  \draw[dashed] (1,2) -- (4,3);
  \draw[thick,->] (0,0) -- (3,1) node[below right] {$\mathbf{u} = (3,1)$};
  \draw[thick,->] (0,0) -- (1,2) node[above left] {$\mathbf{v} = (1,2)$};
  \draw[very thick,->] (0,0) -- (4,3) node[above right] {$\mathbf{u}+\mathbf{v} = (4,3)$};
\end{tikzpicture}
\end{center}

The picture shows one rule at once: going along \( \u \) and then \( \v \) ends at the same corner as going along \( \v \) and then \( \u \), so \( \u + \v = \v + \u \). Other rules are just as familiar. Scaling a sum is the same as adding the scaled arrows, \( 2(\u + \v) = 2\u + 2\v \). Adding the zero arrow changes nothing, and every arrow is undone by its reverse.

Now look at polynomials of degree at most \( 2 \). We add them coefficient by coefficient,
\[
(1 + 2x - x^2) + (3 - x + 4x^2) = 4 + x + 3x^2,
\]
and scale them the same way, \( 2(1 + 2x - x^2) = 2 + 4x - 2x^2 \). There is no picture of arrows here, yet the rules are identical: order does not matter in a sum, the zero polynomial changes nothing, and \( -1 - 2x + x^2 \) undoes \( 1 + 2x - x^2 \).

The same happens for \( 2 \times 2 \) real matrices. @thm-matrix-addition-properties lists the rules for adding matrices and multiplying them by numbers, and they are again the same rules.

Arrows, polynomials and matrices are very different objects, but many arguments about them only use these rules. If we prove a statement from the rules alone, it holds for arrows, polynomials and matrices at once, and for every other system obeying the rules. So we list the rules once and give the systems that obey them a name.

*A vector space is a set whose elements can be added and scaled by numbers from a field, with the usual rules of arithmetic.*

## The definition

::: {#def-vector-space}
[Vector Space]

Let \( F \) be a field. A **vector space over \( F \)** is a set \( V \) together with two functions
\[
+ \colon V \times V \to V, \ (\u, \v) \mapsto \u + \v, \qquad \cdot \colon F \times V \to V, \ (a, \v) \mapsto a\v,
\]
called **addition** and **scalar multiplication**, such that the following axioms hold.

::: {.enumerate options="label=(VS\arabic*)"}
1. \( \u + \v = \v + \u \) **for all** \( \u, \v \in V \).
2. \( (\u + \v) + \w = \u + (\v + \w) \) **for all** \( \u, \v, \w \in V \).
3. There exists an element \( \0 \in V \) such that \( \v + \0 = \v \) **for every** \( \v \in V \).
4. **For every** \( \v \in V \) there exists an element \( \v' \in V \) such that \( \v + \v' = \0 \).
5. \( a(\u + \v) = a\u + a\v \) **for all** \( a \in F \) and \( \u, \v \in V \).
6. \( (a + b)\v = a\v + b\v \) **for all** \( a, b \in F \) and \( \v \in V \).
7. \( a(b\v) = (ab)\v \) **for all** \( a, b \in F \) and \( \v \in V \).
8. \( 1\v = \v \) **for every** \( \v \in V \), where \( 1 \) is the identity element of \( F \).
:::
:::

Read the definition clause by clause.

- **The two functions.** Addition takes two elements of \( V \) and returns an element **of \( V \)**. Scalar multiplication takes a number from \( F \) and an element of \( V \) and returns an element **of \( V \)**. So "the sum stays in the set" and "a multiple stays in the set" are not extra axioms: they are built into the word "function into \( V \)". When we test a candidate, this closure is the first thing to check.
- **(VS1)–(VS4)** concern addition alone. It is commutative and associative, there is a vector \( \0 \) that changes nothing, and every vector can be undone. These are the axioms (F1)–(F4) of @def-field, now for vectors.
- **(VS5) and (VS6)** are the two distributive laws. In (VS6) the symbol \( + \) appears twice with two meanings: on the left it adds scalars in \( F \), on the right it adds vectors in \( V \).
- **(VS7)** says scaling by \( b \) and then by \( a \) is scaling by the product \( ab \), computed in \( F \).
- **(VS8)** says the scalar \( 1 \) acts as it should. It looks too obvious to state, but we will see below that it cannot be dropped.

Note the order of quantifiers in (VS3): **one** vector \( \0 \) works for **every** \( \v \). In (VS4) the vector \( \v' \) is allowed to depend on \( \v \).

::: {#def-vectors-scalars}
[Vectors and Scalars]

Let \( V \) be a vector space over \( F \). The elements of \( V \) are called **vectors**, and the elements of \( F \) are called **scalars**. The element \( \0 \) in (VS3) is a **zero vector** of \( V \), and an element \( \v' \) as in (VS4) is an **additive inverse** of \( \v \).
:::

A vector space over \( \nR \) is also called a **real vector space**, and one over \( \nC \) a **complex vector space**. When the operations are clear from context, we say "\( V \) is a vector space over \( F \)" instead of naming the triple \( (V, +, \cdot) \). The field is part of the data, and we will see shortly that changing it changes the space.

We wrote "**a** zero vector" and "**an** additive inverse" on purpose. The axioms only say these exist. That there is only one of each is a theorem, proved later in this section.

::: {.warning}
**Two different zeros.** The scalar \( 0 \in F \) and the zero vector \( \0 \in V \) are different objects. In \( M_2(\nR) \), the scalar is the number \( 0 \) and the zero vector is the zero matrix; in \( \nR^3 \), the zero vector is \( (0, 0, 0) \). This book writes the zero vector in bold. An equation such as \( 0\v = \0 \) has a scalar on the left and a vector on the right, and mixing them up produces statements that make no sense, such as "\( \v = 0 \)" for a matrix \( \v \).
:::

## Examples

We start with the families we will use throughout the book. For each, the work is to say what the operations are and why the axioms hold. We check some axioms in full and point out the pattern for the rest.

::: {#exm-vector-spaces}
[The Standard Vector Spaces]

Let \( F \) be a field. Explain why each of the following is a vector space over \( F \).

::: {.enumerate options="label=(\alph*)"}
1. \( F^n \), with entrywise addition and scalar multiplication.
2. \( M_{m \times n}(F) \), with the matrix operations of @def-matrix-addition and @def-scalar-multiplication.
3. \( F[x] \), with the addition of @def-polynomial-ring and \( c \sum a_k x^k \coloneqq \sum (c a_k) x^k \).
4. For a set \( X \), the set \( F^X \) of **all** functions \( X \to F \), with the **pointwise** operations
   \[
   (f + g)(t) \coloneqq f(t) + g(t), \qquad (af)(t) \coloneqq a f(t) \qquad \text{for all } t \in X.
   \]
5. The set \( F^{\nN} \) of all sequences \( (s_0, s_1, s_2, \dots) \) of elements of \( F \), with termwise operations.
:::
:::

::: {.solution}
(b) The sum and scalar multiple of \( m \times n \) matrices are \( m \times n \) matrices, so both operations are functions into \( M_{m \times n}(F) \). The eight axioms are exactly the rules of @thm-matrix-addition-properties, with the zero matrix as \( \0 \) and \( -\A \) as an additive inverse of \( \A \).

(a) Chapter 0 defines \( F^n = M_{n \times 1}(F) \), the column vectors, and the entrywise operations are the matrix operations. So (a) is the case of (b) with \( n \) rows and \( 1 \) column. The zero vector is \( (0, \dots, 0) \).

(d) The formulas define functions \( f + g \) and \( af \) from \( X \) to \( F \), so the operations land in \( F^X \). Two functions \( X \to F \) are equal when they take the same value at every \( t \in X \) (@def-function), so each axiom is checked one point at a time. For (VS3), let \( \0 \) be the zero function, \( \0(t) = 0 \) for all \( t \). Then \( (f + \0)(t) = f(t) + 0 = f(t) \) for every \( t \), by (F3), so \( f + \0 = f \). For (VS4), let \( f'(t) \coloneqq -f(t) \). Then \( (f + f')(t) = f(t) + (-f(t)) = 0 = \0(t) \) by (F4), so \( f + f' = \0 \). For (VS6), let \( a, b \in F \). For every \( t \in X \),
\[
((a + b)f)(t) = (a + b)f(t) = af(t) + bf(t) = (af)(t) + (bf)(t) = (af + bf)(t),
\]
where the second equality is (F9) together with (F6) in \( F \). Hence \( (a + b)f = af + bf \). The other five axioms reduce in the same way to a field axiom at each point: (VS1) to (F1), (VS2) to (F2), (VS5) to (F9), (VS7) to (F5), and (VS8) to (F7) with (F6).

(e) A sequence \( (s_0, s_1, \dots) \) is a function \( \nN \to F \), \( k \mapsto s_k \), and the termwise operations are the pointwise ones. So (e) is (d) with \( X = \nN \).

(c) Let \( p = \sum a_k x^k \in F[x] \) and \( c \in F \). Only finitely many \( a_k \) are non-zero, and \( a_k = 0 \) forces \( c a_k = 0 \), so \( cp \) is again a polynomial. The sum of polynomials is a polynomial by @def-polynomial-ring. By @thm-polynomial-ring-laws (parts 1 and 2), addition satisfies (VS1)–(VS4), with the zero polynomial as \( \0 \) and \( -p \) as an additive inverse. Since polynomials are equal when their coefficients agree (@def-polynomial), (VS5)–(VS8) are checked coefficient by coefficient. For instance, the coefficient of \( x^k \) in \( (c + d)p \) is \( (c + d)a_k = c a_k + d a_k \), which is the coefficient of \( x^k \) in \( cp + dp \). The others reduce in the same way: (VS5) to (F9), (VS7) to (F5), and (VS8) to (F7) with (F6).
:::

The pattern is worth naming. Whenever the operations are defined **entry by entry**, **point by point** or **coefficient by coefficient**, each axiom for vectors is a field axiom applied in each slot. In fact (a), (b) and (e) are all instances of (d): a column in \( F^n \) is a function \( \{1, \dots, n\} \to F \), and a matrix in \( M_{m \times n}(F) \) is a function on the set of positions \( \{1, \dots, m\} \times \{1, \dots, n\} \).

A **subset** of a known space often works just as well, provided the operations do not lead out of it.

The set \( F[x]_{\le n} \) of @def-polynomials-bounded-degree is a vector space over \( F \), with the operations of \( F[x] \). Closure is the only real issue. If \( \deg p \le n \) and \( \deg q \le n \), then \( \deg(p + q) \le \max(\deg p, \deg q) \le n \) by @thm-degree-of-sum. If \( a_k = 0 \) for all \( k > n \), then \( c a_k = 0 \) for all \( k > n \), so \( \deg(cp) \le n \). The zero polynomial has degree \( -\infty \le n \), and \( -p \) has the same coefficients as \( p \) up to sign, so it stays in \( F[x]_{\le n} \). The six axioms (VS1), (VS2), (VS5)–(VS8) are equations that hold for **all** polynomials, so in particular for those of degree at most \( n \).

The next example applies the same pattern to a set of real numbers, with a smaller field of scalars.

::: {#exm-q-adjoin-sqrt2}
[\( \nQ(\sqrt{2}) \) over \( \nQ \)]

Let \( \nQ(\sqrt2) = \{ a + b\sqrt2 : a, b \in \nQ \} \), with the addition of \( \nR \) and with scalar multiplication \( c(a + b\sqrt2) \coloneqq ca + cb\sqrt2 \) for \( c \in \nQ \). Show that \( \nQ(\sqrt2) \) is a vector space over \( \nQ \).
:::

::: {.solution}
Let \( \u = a + b\sqrt2 \) and \( \v = a' + b'\sqrt2 \) with \( a, b, a', b' \in \nQ \), and let \( c \in \nQ \).

*Closure.* We have \( \u + \v = (a + a') + (b + b')\sqrt2 \) and \( c\u = ca + cb\sqrt2 \). Sums and products of rationals are rational, so both lie in \( \nQ(\sqrt2) \). Hence addition is a function \( \nQ(\sqrt2) \times \nQ(\sqrt2) \to \nQ(\sqrt2) \), and scalar multiplication is a function \( \nQ \times \nQ(\sqrt2) \to \nQ(\sqrt2) \).

*Zero and additive inverses.* The number \( 0 = 0 + 0\sqrt2 \) lies in \( \nQ(\sqrt2) \) and satisfies \( \u + 0 = \u \), so (VS3) holds. The number \( -\u = (-a) + (-b)\sqrt2 \) lies in \( \nQ(\sqrt2) \) and satisfies \( \u + (-\u) = 0 \), so (VS4) holds.

*The identities.* Scalar multiplication by \( c \in \nQ \) is the multiplication of real numbers, since \( c(a + b\sqrt2) = ca + cb\sqrt2 \) in \( \nR \). So each of (VS1), (VS2) and (VS5)–(VS8) is an identity between real numbers, and it holds by the field axioms of \( \nR \): (VS1) is (F1), (VS2) is (F2), (VS5) is (F9), (VS6) is (F9) with (F6), (VS7) is (F5), and (VS8) is (F7) with (F6). Hence \( \nQ(\sqrt2) \) is a vector space over \( \nQ \).
:::

We saw in @exm-q-sqrt2-field that \( \nQ(\sqrt2) \) is even a field. As a vector space over \( \nQ \), we simply ignore how to multiply two of its elements together and keep only multiplication by rationals.

The same set can carry more than one field of scalars. The next example makes this concrete.

::: {#exm-same-set-different-field}
[The Same Set over Different Fields]

Explain why \( \nC \) is a vector space over \( \nC \) and also over \( \nR \), and why \( \nR \) is a vector space over \( \nR \) and also over \( \nQ \). In each case the addition is the usual one and the scalar multiplication is the usual product.
:::

::: {.solution}
\( \nC \) over \( \nC \) is \( F^1 \) for \( F = \nC \), covered by @exm-vector-spaces (a). For \( \nC \) over \( \nR \), a real number \( r \) is the complex number \( r + 0i \), and \( rz \) is their complex product, which lies in \( \nC \). Each axiom is an identity among complex numbers in which some of the numbers happen to be real, so it holds by @prp-complex-arithmetic-laws: (VS5) and (VS6) by distributivity together with commutativity, (VS7) by associativity of multiplication, and (VS8) since \( 1 \cdot z = z \). The argument for \( \nR \) over \( \nQ \) is the same, with the field axioms of \( \nR \) in place of the laws of \( \nC \).
:::

As sets, \( \nC \) over \( \nC \) and \( \nC \) over \( \nR \) are the same. As vector spaces they differ, because the scalars available differ. In \( \nC \) over \( \nC \), the vector \( i \) is a scalar multiple of the vector \( 1 \). In \( \nC \) over \( \nR \) it is not, since \( r \cdot 1 = i \) has no real solution \( r \). Later in this chapter this difference becomes a difference in dimension. That is why we always say **over which field**.

**The degenerate case.** The set \( \{\0\} \) with one element, with \( \0 + \0 = \0 \) and \( a\0 = \0 \) for every \( a \in F \), is a vector space over any field. Every axiom is an equation between elements that all equal \( \0 \), and \( \0 \) serves as the zero vector and as its own additive inverse. It is called the **zero space**. It matters because it turns up constantly as an answer: the only solution of a system, or the smallest vector space inside every other one. Unlike a field, which must contain \( 1 \ne 0 \) (@def-field), a vector space is allowed to have a single element, since no axiom asks for a vector different from \( \0 \).

A final example looks strange, but it satisfies every axiom.

::: {#exm-positive-reals}
[Positive Reals with Exotic Operations]

Let \( V = \nR_{>0} = \{ t \in \nR : t > 0 \} \). For \( u, v \in V \) and \( c \in \nR \), define
\[
u \boxplus v \coloneqq uv, \qquad c \boxdot v \coloneqq v^{c}.
\]
Show that these operations are functions into \( V \), find the zero vector and the additive inverse of \( v \), and check (VS6) and (VS8).
:::

::: {.solution}
*Closure.* For \( u, v > 0 \) and \( c \in \nR \), the product \( uv \) is positive and the power \( v^{c} \) is positive. So \( \boxplus \colon V \times V \to V \) and \( \boxdot \colon \nR \times V \to V \).

*(VS3).* We need \( z \in V \) with \( v \boxplus z = v \), that is, \( vz = v \), for every \( v > 0 \). The number \( z = 1 \) works, since \( v \cdot 1 = v \). So the zero vector of \( V \) is the real number \( 1 \).

*(VS4).* For \( v \in V \), we need \( v' \in V \) with \( v \boxplus v' = 1 \), that is, \( vv' = 1 \). The number \( v' = 1/v \) is positive and works. So the additive inverse of \( v \) is \( 1/v \).

*(VS6).* For \( a, b \in \nR \) and \( v \in V \), by the laws of exponents,
\[
(a + b) \boxdot v = v^{a + b} = v^{a} v^{b} = (a \boxdot v) \boxplus (b \boxdot v).
\]

*(VS8).* \( 1 \boxdot v = v^{1} = v \).

The remaining axioms (VS1), (VS2), (VS5) and (VS7) are @exr-vector-spaces-b3. So \( V \) is a real vector space.
:::

This example earns its place for one reason. The words "zero vector" and "addition" describe **roles** fixed by the axioms, not the familiar number \( 0 \) or the familiar \( + \). Here the vector playing the role of \( \0 \) is the number \( 1 \), and "adding" means multiplying.

::: {.check}
Explain why each of the following, with the usual operations, is a vector space over \( \nR \).

::: {.enumerate options="label=(\alph*)"}
1. The set \( S \) of twice-differentiable functions \( f \colon \nR \to \nR \) with \( f'' + f = 0 \).
2. The set of symmetric matrices \( \A \in M_2(\nR) \), that is, those with \( \A\tp = \A \).
:::
:::

::: {.solution}
Both are subsets of known spaces, so we use the pattern after @exm-vector-spaces: check closure, the zero vector and additive inverses; the other six axioms are identities inherited from the big space.

(a) \( S \subseteq \nR^{\nR} \). If \( f, g \in S \) and \( c \in \nR \), then by the sum and constant multiple rules of calculus, \( f + g \) and \( cf \) are twice differentiable, with \( (f + g)'' + (f + g) = (f'' + f) + (g'' + g) = 0 \) and \( (cf)'' + cf = c(f'' + f) = 0 \). So both lie in \( S \). The zero function \( \0 \) satisfies \( \0'' + \0 = \0 \), so \( \0 \in S \). If \( f \in S \), its additive inverse in \( \nR^{\nR} \) is \( t \mapsto -f(t) \), and \( -f(t) = (-1)f(t) \) by @thm-field-basic-properties (e); so it is the function \( (-1)f \), which lies in \( S \) by closure under scaling. The identities hold in \( \nR^{\nR} \) (@exm-vector-spaces (d)), hence in \( S \). For instance \( \sin \) and \( \cos \) lie in \( S \).

(b) By @thm-transpose-properties, \( (\A + \B)\tp = \A\tp + \B\tp = \A + \B \) and \( (c\A)\tp = c\A\tp = c\A \) when \( \A\tp = \A \) and \( \B\tp = \B \). The zero matrix is symmetric, and the additive inverse \( -\A \), which Chapter 0 defines as \( (-1)\A \), is symmetric by closure under scaling. The identities hold in \( M_2(\nR) \), hence for symmetric matrices.
:::

## Non-examples

Each non-example below is a small change to an example. We say what still works and name the exact clause that fails.

- **Change scalar multiplication on \( \nR^2 \) to \( c(x, y) \coloneqq (cx, 0) \)**, keeping the usual addition. Addition is untouched, so (VS1)–(VS4) hold. (VS5) holds: \( c\big((x, y) + (x', y')\big) = (c(x + x'), 0) = (cx, 0) + (cx', 0) \). In the same way (VS6) and (VS7) hold. But \( 1(0, 1) = (0, 0) \ne (0, 1) \), so **(VS8) fails**.
- **Change the line \( x + 2y = 0 \) to \( x + 2y = 3 \).** Let \( L = \{ (x, y) \in \nR^2 : x + 2y = 3 \} \) with the operations of \( \nR^2 \). The points \( (3, 0) \) and \( (1, 1) \) lie on \( L \), but their sum \( (4, 1) \) has \( 4 + 2 \cdot 1 = 6 \ne 3 \). So addition is **not a function** \( L \times L \to L \), and \( L \) is not a vector space with these operations.
- **Change "degree at most \( 2 \)" to "degree exactly \( 2 \)".** In \( \nR[x]_{=2} \) (@def-polynomials-exact-degree), \( x^2 + 2x \) and \( -x^2 + 3 \) have degree \( 2 \), but their sum \( 2x + 3 \) has degree \( 1 \). Again addition leaves the set. There is no zero vector either: the zero polynomial has degree \( -\infty \), not \( 2 \).
- **Change the entries from real to integer**, keeping \( \nR \) as the field. For \( \nZ^2 \subseteq \nR^2 \), addition is fine, but \( \tfrac12 (1, 0) = (\tfrac12, 0) \notin \nZ^2 \). So scalar multiplication is **not a function** \( \nR \times \nZ^2 \to \nZ^2 \).

## Why these axioms

Each axiom is there for a reason, and a few conventions deserve a comment.

- **(VS8) cannot be dropped.** The first non-example satisfies all other axioms. Without (VS8), the "scalar multiplication" \( c\v = \0 \) for all \( c \) and \( \v \) would also be allowed, and scaling would carry no information at all.
- **(VS1) is in fact redundant.** Commutativity of addition follows from the other seven axioms, by expanding \( (1 + 1)(\u + \v) \) in two ways (@exr-vector-spaces-c1). It is kept because the proof is fiddly and nobody wants to repeat it.
- **Closure is not optional.** Two of the non-examples fail only because an operation leads out of the set. That is why the definition asks for **functions into \( V \)**.
- **The scalars form a field.** We use division by non-zero scalars in the zero product law at the end of the next subsection. The warning after it shows what goes wrong without division.
- **The name.** "Vector" originally meant an arrow in physics. The word is kept for elements of any vector space, even when they are polynomials or functions.

## First consequences of the axioms

The definition says a zero vector and additive inverses **exist**, not that they are unique. Before writing \( \0 \) and \( -\v \) as if each named one thing, we prove uniqueness. We also prove that familiar rules such as \( 0\v = \0 \) follow from the axioms. None of this is obvious from the axioms: in @exm-positive-reals, \( 0 \boxdot v = v^0 = 1 \), which happens to be the zero vector there, and it takes a proof to see that this is no coincidence.

Throughout, we use one fact about functions without further comment: if two inputs are equal, the outputs are equal. So from \( \v = \w \) we may conclude \( \u + \v = \u + \w \) and \( a\v = a\w \).

The first tool lets us cancel a vector from both sides of an equation.

::: {#thm-left-cancellation}
[Left Cancellation Law]

Let \( V \) be a vector space over \( F \) and let \( \u, \v, \w \in V \). If \( \u + \v = \u + \w \), then \( \v = \w \).
:::

::: {.proof}
Suppose \( \u + \v = \u + \w \). By (VS4) there is \( \u' \in V \) with \( \u + \u' = \0 \). Adding \( \u' \) on the left of both sides gives \( \u' + (\u + \v) = \u' + (\u + \w) \), and by (VS2),
\[
(\u' + \u) + \v = (\u' + \u) + \w.
\]
By (VS1) and the choice of \( \u' \), \( \u' + \u = \u + \u' = \0 \). Hence \( \0 + \v = \0 + \w \). By (VS1) this is \( \v + \0 = \w + \0 \), and by (VS3), \( \v = \w \).
:::

::: {#thm-right-cancellation}
[Right Cancellation Law]

Let \( V \) be a vector space over \( F \) and let \( \u, \v, \w \in V \). If \( \v + \u = \w + \u \), then \( \v = \w \).
:::

::: {.proof}
By (VS1), the hypothesis says \( \u + \v = \u + \w \). By @thm-left-cancellation, \( \v = \w \).
:::

Uniqueness uses the standard move from Chapter 0: suppose there are two, and show they are equal.

::: {#thm-zero-unique}
[Zero Vector Is Unique]

Let \( V \) be a vector space over \( F \). There is exactly one element \( \0 \in V \) satisfying (VS3).
:::

::: {.proof}
Existence is (VS3). Suppose \( \0 \) and \( \0' \) both satisfy (VS3). Applying (VS3) for \( \0' \) to the vector \( \0 \), then (VS1), then (VS3) for \( \0 \) to the vector \( \0' \),
\[
\0 = \0 + \0' = \0' + \0 = \0'.
\]
This shows the zero vector is unique.
:::

::: {#thm-inverse-unique}
[Additive Inverse Is Unique]

Let \( V \) be a vector space over \( F \) and \( \v \in V \). There is exactly one \( \v' \in V \) with \( \v + \v' = \0 \).
:::

::: {.proof}
Existence is (VS4). Suppose \( \v + \v' = \0 \) and \( \v + \v'' = \0 \). Then \( \v + \v' = \v + \v'' \), and @thm-left-cancellation gives \( \v' = \v'' \).
:::

Since the inverse is unique, it deserves a name.

::: {#def-additive-inverse-notation}
[Notation for the Additive Inverse]

Let \( V \) be a vector space over \( F \) and \( \v \in V \). The unique additive inverse of \( \v \) is denoted \( -\v \). For \( \u, \v \in V \) we write \( \u - \v \coloneqq \u + (-\v) \).
:::

For example, \( \v + (-\v) = \0 \) and \( (-\v) + \v = \0 \) by (VS1), so \( \v \) is the additive inverse of \( -\v \). By @thm-inverse-unique, \( -(-\v) = \v \).

::: {.remark}
Axioms (VS1)–(VS4) say that \( V \) with addition is an abelian group (@def-group). So the four results above are also special cases of @thm-group-basic-properties. We proved them directly to practice citing the axioms.
:::

Now to scalars. No axiom mentions \( 0\v \), so we must create a situation in which one applies. The move is to write the scalar \( 0 \) in a fancy way, as \( 0 + 0 \), expand with a distributive law, and cancel. We will call it **expand zero and cancel**.

::: {#thm-zero-scalar-mult}
[Zero Scalar Gives the Zero Vector]

Let \( V \) be a vector space over \( F \). Then \( 0\v = \0 \) for every \( \v \in V \).
:::

::: {.proof}
Let \( \v \in V \). Since \( 0 + 0 = 0 \) in \( F \) by (F3), (VS6) gives
\[
0\v + 0\v = (0 + 0)\v = 0\v = 0\v + \0,
\]
where the last equality is (VS3). By @thm-left-cancellation, \( 0\v = \0 \).
:::

The same move, with the zero vector in place of the zero scalar, handles \( a\0 \).

::: {#thm-scalar-zero-vector}
[Scalar Multiple of the Zero Vector]

Let \( V \) be a vector space over \( F \). Then \( a\0 = \0 \) for every \( a \in F \).
:::

::: {.proof}
Let \( a \in F \). Since \( \0 + \0 = \0 \) by (VS3), (VS5) gives
\[
a\0 + a\0 = a(\0 + \0) = a\0 = a\0 + \0,
\]
where the last equality is (VS3). By @thm-left-cancellation, \( a\0 = \0 \).
:::

To identify a vector as \( -\v \), it is enough to show it adds with \( \v \) to \( \0 \), by @thm-inverse-unique. This gives the next two results.

::: {#thm-negation-scalar}
[Negation as Scalar Multiplication]

Let \( V \) be a vector space over \( F \). Then \( (-1)\v = -\v \) for every \( \v \in V \).
:::

::: {.proof}
Let \( \v \in V \). By (VS8), (VS6), (F4) and @thm-zero-scalar-mult,
\[
\v + (-1)\v = 1\v + (-1)\v = (1 + (-1))\v = 0\v = \0.
\]
So \( (-1)\v \) is an additive inverse of \( \v \), and by @thm-inverse-unique it equals \( -\v \).
:::

::: {#thm-negative-scalar-dist}
[Negative Scalars]

Let \( V \) be a vector space over \( F \). Then \( (-a)\v = -(a\v) \) for every \( a \in F \) and \( \v \in V \).
:::

::: {.proof}
Let \( a \in F \) and \( \v \in V \). By (VS6), (F4) and @thm-zero-scalar-mult,
\[
a\v + (-a)\v = (a + (-a))\v = 0\v = \0.
\]
So \( (-a)\v \) is an additive inverse of \( a\v \), and by @thm-inverse-unique it equals \( -(a\v) \).
:::

The companion rules \( a(-\v) = -(a\v) \) and \( a(\u - \v) = a\u - a\v \) are @exr-vector-spaces-b2. From now on, we compute with \( + \), \( - \) and scalars as in school algebra, citing these results when a step is not a single axiom.

The last result is the one we will use most. In a field, a product of non-zero numbers is non-zero (@thm-field-basic-properties (f)). The same holds for a scalar times a vector.

::: {#thm-zero-product}
[Zero Product Law]

Let \( V \) be a vector space over \( F \), let \( a \in F \) and \( \v \in V \). Then \( a\v = \0 \) if and only if \( a = 0 \) or \( \v = \0 \).
:::

::: {.idea}
The direction \( (\Leftarrow) \) is the two zero results above, @thm-zero-scalar-mult and @thm-scalar-zero-vector. For \( (\Rightarrow) \), the only way to get rid of \( a \) is to multiply by \( a^{-1} \), and that is exactly where the hypothesis \( a \ne 0 \) and the field axiom (F8) are spent.
:::

::: {.proof}
\( (\Leftarrow) \) If \( a = 0 \), then \( a\v = \0 \) by @thm-zero-scalar-mult. If \( \v = \0 \), then \( a\v = \0 \) by @thm-scalar-zero-vector.

\( (\Rightarrow) \) Suppose \( a\v = \0 \). If \( a = 0 \) there is nothing to prove, so suppose \( a \ne 0 \). By (F8), \( a \) has an inverse \( a^{-1} \in F \). Then
\[
\v = 1\v = (a^{-1}a)\v = a^{-1}(a\v) = a^{-1}\0 = \0,
\]
by (VS8), (F8) with (F6), (VS7), the hypothesis, and @thm-scalar-zero-vector. This shows \( a = 0 \) or \( \v = \0 \).
:::

::: {.warning}
**The zero product law needs division by scalars.** Suppose we allowed integer "scalars" and let \( V = \nF_2 = \{0, 1\} \) with its own addition, where \( n \cdot v \) is \( v \) for odd \( n \) and \( 0 \) for even \( n \) (for \( n \ge 0 \) this is \( v + \dots + v \) with \( n \) terms). Every rule of the shape (VS1)–(VS8) still holds. But \( 2 \cdot 1 = 1 + 1 = 0 \), although \( 2 \ne 0 \) in \( \nZ \) and \( 1 \ne 0 \) in \( V \). The proof above breaks exactly where it multiplies by \( a^{-1} \): the integer \( 2 \) has no inverse in \( \nZ \). This is one reason vector spaces are defined **over a field**.
:::

As a first use, here is a fact about sizes. Let \( \v \ne \0 \) be a vector in a space over \( \nR \). If \( a\v = b\v \), then \( (a - b)\v = a\v - b\v = \0 \) by (VS6) and @thm-negative-scalar-dist, so \( a = b \) by @thm-zero-product. So the multiples \( a\v \), \( a \in \nR \), are all different, and a real vector space other than \( \{\0\} \) has infinitely many elements (@exr-vector-spaces-c2 treats a general field). This is our first glimpse of the question at the heart of this chapter: all these spaces are infinite sets, so how should we measure their size? The next section starts on the answer by looking at the vector spaces that sit inside a given one.

## Exercises

### A. Check your understanding

::: {#exr-vector-spaces-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the eight axioms of a vector space over a field \( F \), and say which of them involve scalars.
2. Identify the zero vector in each of: \( M_{2 \times 3}(\nR) \); \( \nR[x]_{\le 2} \); \( \nR^{\nR} \); the space \( \nR_{>0} \) of @exm-positive-reals.
3. True or false: a vector space can have exactly two elements. Justify your answer.
4. True or false: in every vector space, \( \v + \v = \0 \) implies \( \v = \0 \). Justify your answer.
5. True or false: if \( a\v = b\v \) and \( \v \ne \0 \), then \( a = b \). Justify your answer.
:::
:::

::: {.solution}
(a) See @def-vector-space. The axioms (VS5)–(VS8) involve scalars; (VS1)–(VS4) involve only addition.

(b) The zero matrix of size \( 2 \times 3 \); the zero polynomial; the zero function \( t \mapsto 0 \); the number \( 1 \) (@exm-positive-reals).

(c) True. Let \( F = \nF_2 \). By @exm-vector-spaces (a), \( \nF_2^1 = \nF_2 = \{0, 1\} \) is a vector space over \( \nF_2 \), and it has exactly two elements.

(d) False. In the vector space \( \nF_2 \) over \( \nF_2 \) from (c), the vector \( 1 \ne 0 \) satisfies \( 1 + 1 = 0 \). (Over \( \nR \) the statement is true: \( \v + \v = (1 + 1)\v = 2\v \) by (VS8) and (VS6), and \( 2 \ne 0 \), so \( \v = \0 \) by @thm-zero-product.)

(e) True. By (VS6) and @thm-negative-scalar-dist, \( (a - b)\v = a\v + (-b)\v = a\v - b\v = \0 \). Since \( \v \ne \0 \), @thm-zero-product gives \( a - b = 0 \), so \( a = b \).
:::

### B. Practice

::: {#exr-vector-spaces-b1}
[B1: Which Are Vector Spaces?]

Determine which of the following are vector spaces. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \nR^2 \) over \( \nR \), with the usual scalar multiplication but with addition \( (x, y) + (x', y') \coloneqq (x + x', 0) \).
2. The set of upper triangular matrices in \( M_2(\nR) \), over \( \nR \), with the matrix operations.
3. \( \{ p \in \nR[x] : p(1) = 0 \} \), over \( \nR \), with the operations of \( \nR[x] \).
4. \( \{ p \in \nR[x] : p(1) = 1 \} \), over \( \nR \), with the operations of \( \nR[x] \).
5. \( \nR^2 \) over \( \nC \), with \( c(x, y) \coloneqq (cx, cy) \) and the usual addition.
:::
:::

::: {.solution}
(a) Not a vector space: (VS3) fails. Suppose \( \0 = (z_1, z_2) \) satisfied (VS3). Then \( (0, 1) + (z_1, z_2) = (z_1, 0) \) would equal \( (0, 1) \), which is impossible since the second entries differ.

(b) A vector space. Let \( \A = \begin{pmatrix} a & b \\ 0 & d \end{pmatrix} \) and \( \B = \begin{pmatrix} a' & b' \\ 0 & d' \end{pmatrix} \) be upper triangular and \( c \in \nR \). Then \( \A + \B = \begin{pmatrix} a + a' & b + b' \\ 0 & d + d' \end{pmatrix} \) and \( c\A = \begin{pmatrix} ca & cb \\ 0 & cd \end{pmatrix} \) are upper triangular, so the operations land in the set. The zero matrix is upper triangular, and so is \( -\A = (-1)\A \). The identities (VS1), (VS2), (VS5)–(VS8) hold for all matrices in \( M_2(\nR) \) by @exm-vector-spaces (b), hence for upper triangular ones.

(c) A vector space. Let \( U = \{ p \in \nR[x] : p(1) = 0 \} \), \( p, q \in U \) and \( c \in \nR \). By @thm-evaluation-respects-operations, \( (p + q)(1) = p(1) + q(1) = 0 \). Also \( cp \) is the product of the constant polynomial \( c \) with \( p \), since by the product formula of @def-polynomial-ring that product has coefficients \( c a_k \). So \( (cp)(1) = c\, p(1) = 0 \). Hence \( p + q, cp \in U \). The zero polynomial has value \( 0 \) at \( 1 \), and \( -p = (-1)p \in U \) by closure under scaling. The identities hold in \( \nR[x] \) by @exm-vector-spaces (c), hence in \( U \).

(d) Not a vector space: addition leaves the set. The constant polynomial \( 1 \) lies in the set, but \( (1 + 1)(1) = 2 \ne 1 \), so \( 1 + 1 \) does not.

(e) Not a vector space: scalar multiplication leaves the set. We have \( i \in \nC \) and \( (1, 0) \in \nR^2 \), but \( i(1, 0) = (i, 0) \notin \nR^2 \). So the rule is not a function \( \nC \times \nR^2 \to \nR^2 \).
:::

::: {#exr-vector-spaces-b2}
[B2: More Rules for Signs]

Let \( V \) be a vector space over \( F \), let \( a, b \in F \) and \( \u, \v \in V \). Prove that:

::: {.enumerate options="label=(\alph*)"}
1. \( a(-\v) = -(a\v) \);
2. \( (-a)(-\v) = a\v \);
3. \( a(\u - \v) = a\u - a\v \) and \( (a - b)\v = a\v - b\v \).
:::

*Hint: to show a vector equals \( -(a\v) \), use @thm-inverse-unique.*
:::

::: {.solution}
(a) By (VS5), (VS4) and @thm-scalar-zero-vector,
\[
a\v + a(-\v) = a(\v + (-\v)) = a\0 = \0.
\]
So \( a(-\v) \) is an additive inverse of \( a\v \). By @thm-inverse-unique, \( a(-\v) = -(a\v) \).

(b) By (a) applied with the scalar \( -a \), then @thm-negative-scalar-dist, then the remark after @def-additive-inverse-notation,
\[
(-a)(-\v) = -\big((-a)\v\big) = -\big(-(a\v)\big) = a\v.
\]

(c) By @def-additive-inverse-notation, (VS5) and (a),
\[
a(\u - \v) = a(\u + (-\v)) = a\u + a(-\v) = a\u + (-(a\v)) = a\u - a\v.
\]
Similarly, since \( a - b = a + (-b) \) in \( F \), (VS6) and @thm-negative-scalar-dist give \( (a - b)\v = a\v + (-b)\v = a\v + (-(b\v)) = a\v - b\v \).
:::

::: {#exr-vector-spaces-b3}
[B3: Finishing the Positive Reals]

Let \( V = \nR_{>0} \) with the operations \( \boxplus \) and \( \boxdot \) of @exm-positive-reals.

::: {.enumerate options="label=(\alph*)"}
1. Verify (VS1), (VS2), (VS5) and (VS7). Hence \( V \) is a vector space over \( \nR \).
2. Compute the vector \( (2 \boxdot 3) \boxplus \big((-1) \boxdot 6\big) \).
3. Find the vector \( -(2 \boxdot 3) \), and check your answer against @thm-negative-scalar-dist.
:::
:::

::: {.solution}
(a) Let \( u, v, w \in V \) and \( a, b \in \nR \). By the laws of real multiplication and of exponents for positive bases:

- (VS1): \( u \boxplus v = uv = vu = v \boxplus u \).
- (VS2): \( (u \boxplus v) \boxplus w = (uv)w = u(vw) = u \boxplus (v \boxplus w) \).
- (VS5): \( a \boxdot (u \boxplus v) = (uv)^{a} = u^{a} v^{a} = (a \boxdot u) \boxplus (a \boxdot v) \).
- (VS7): \( a \boxdot (b \boxdot v) = (v^{b})^{a} = v^{ab} = (ab) \boxdot v \).

Together with closure, (VS3), (VS4), (VS6) and (VS8) from @exm-positive-reals, all eight axioms hold. Hence \( V \) is a vector space over \( \nR \).

(b) \( 2 \boxdot 3 = 3^2 = 9 \) and \( (-1) \boxdot 6 = 6^{-1} = \tfrac16 \). So the vector is \( 9 \boxplus \tfrac16 = 9 \cdot \tfrac16 = \tfrac32 \).

(c) By @exm-positive-reals, the additive inverse of a vector \( v \) is \( 1/v \). Since \( 2 \boxdot 3 = 9 \), we get \( -(2 \boxdot 3) = \tfrac19 \). By @thm-negative-scalar-dist, this should equal \( (-2) \boxdot 3 = 3^{-2} = \tfrac19 \), and it does.
:::

### C. Going deeper

::: {#exr-vector-spaces-c1}
[C1: Commutativity Comes for Free]

Let \( V \) be a set with operations \( + \colon V \times V \to V \) and \( \cdot \colon F \times V \to V \) satisfying (VS2)–(VS8), but **not necessarily** (VS1). Fix \( \0 \) as in (VS3).

::: {.enumerate options="label=(\alph*)"}
1. Let \( \v \in V \) and \( \v' \) as in (VS4). Put \( \w = \v' + \v \). Show that \( \w + \w = \w \), and deduce that \( \w = \0 \).
2. Show that \( \0 + \v = \v \) for every \( \v \in V \).
3. Deduce that both cancellation laws hold: \( \u + \v = \u + \w \) implies \( \v = \w \), and \( \v + \u = \w + \u \) implies \( \v = \w \).
4. By expanding \( (1 + 1)(\u + \v) \) in two ways, prove that \( \u + \v = \v + \u \) for all \( \u, \v \in V \).
:::

*Hint: in (a), add an additive inverse of \( \w \) on the right. The proof of @thm-left-cancellation used (VS1), so it cannot be quoted in (c).*
:::

::: {.solution}
Throughout we use only (VS2)–(VS8), and we drop brackets in sums whenever (VS2) allows it.

(a) Since \( \v + \v' = \0 \) and \( \v' + \0 = \v' \) by (VS3),
\[
\w + \w = \v' + (\v + \v') + \v = \v' + \0 + \v = \v' + \v = \w.
\]
By (VS4) choose \( \w' \) with \( \w + \w' = \0 \). Adding \( \w' \) on the right of \( \w + \w = \w \) gives \( \w + (\w + \w') = \w + \w' \), that is, \( \w + \0 = \0 \). By (VS3), \( \w = \0 \). So \( \v' + \v = \0 \) as well.

(b) Let \( \v \in V \) and \( \v' \) as in (VS4). By (a), (VS2) and (VS3),
\[
\0 + \v = (\v + \v') + \v = \v + (\v' + \v) = \v + \0 = \v.
\]

(c) Suppose \( \u + \v = \u + \w \), and let \( \u' \) be as in (VS4). Adding \( \u' \) on the left and using (VS2), \( (\u' + \u) + \v = (\u' + \u) + \w \). By (a), \( \u' + \u = \0 \), so \( \0 + \v = \0 + \w \), and (b) gives \( \v = \w \). Now suppose \( \v + \u = \w + \u \). Adding \( \u' \) on the right and using (VS2), \( \v + (\u + \u') = \w + (\u + \u') \), so \( \v + \0 = \w + \0 \), and (VS3) gives \( \v = \w \).

(d) Let \( \u, \v \in V \). On the one hand, by (VS6) and (VS8),
\[
(1 + 1)(\u + \v) = 1(\u + \v) + 1(\u + \v) = \u + \v + \u + \v.
\]
On the other hand, by (VS5), then (VS6) and (VS8),
\[
(1 + 1)(\u + \v) = (1 + 1)\u + (1 + 1)\v = \u + \u + \v + \v.
\]
Hence \( \u + (\v + \u) + \v = \u + (\u + \v) + \v \), grouping by (VS2). Canceling \( \u \) on the left and then \( \v \) on the right, by (c), gives \( \v + \u = \u + \v \). This proves (VS1).
:::

::: {#exr-vector-spaces-c2}
[C2: How Big Is a Vector Space?]

::: {.enumerate options="label=(\alph*)"}
1. Let \( F \) be an infinite field and \( V \ne \{\0\} \) a vector space over \( F \). Prove that \( V \) is an infinite set.
2. Let \( p \) be a prime and \( n \ge 1 \). How many elements does the vector space \( \nF_p^n \) over \( \nF_p \) have? Explain why this does not contradict (a).
:::

*Hint: for (a), fix \( \v \ne \0 \) and consider the function \( F \to V \), \( a \mapsto a\v \).*
:::

::: {.solution}
(a) Since \( V \ne \{\0\} \) and \( \0 \in V \), there is \( \v \in V \) with \( \v \ne \0 \). Consider \( \varphi \colon F \to V \), \( \varphi(a) = a\v \). Suppose \( \varphi(a) = \varphi(b) \), so \( a\v = b\v \). By @exr-vector-spaces-b2 (c), \( (a - b)\v = a\v - b\v = \0 \). Since \( \v \ne \0 \), @thm-zero-product gives \( a - b = 0 \), so \( a = b \). Therefore \( \varphi \) is injective. An injective function from an infinite set has an infinite image, so \( V \), which contains the image of \( \varphi \), is infinite.

(b) An element of \( \nF_p^n \) is a list \( (x_1, \dots, x_n) \) with each \( x_i \) chosen freely from the \( p \) elements of \( \nF_p \). So \( \nF_p^n \) has \( p^n \) elements. There is no contradiction, because (a) assumes the field is infinite and \( \nF_p \) is finite. The proof of (a) still shows that \( a \mapsto a\v \) is injective, so a non-zero space over \( \nF_p \) has at least \( p \) elements.
:::

::: {#exr-vector-spaces-c3}
[C3: Shrinking the Field]

Let \( F \) be a field and let \( K \subseteq F \) be a subset with \( 0, 1 \in K \) that is closed under addition, multiplication, negatives, and inverses of non-zero elements. (So \( K \) is itself a field with the operations of \( F \); for example \( \nQ \subseteq \nR \subseteq \nC \).)

::: {.enumerate options="label=(\alph*)"}
1. Let \( V \) be a vector space over \( F \). Prove that \( V \), with the same addition and with scalar multiplication restricted to \( K \times V \), is a vector space over \( K \).
2. Deduce that \( \nC^n \) is a vector space over \( \nR \) and over \( \nQ \).
3. Explain why \( \nR \), with its usual addition and multiplication, is **not** a vector space over \( \nC \).
:::
:::

::: {.solution}
(a) The addition is unchanged, so it is a function \( V \times V \to V \) satisfying (VS1)–(VS4). Scalar multiplication \( F \times V \to V \) restricts to a function \( K \times V \to V \), since \( K \subseteq F \). The axioms (VS5)–(VS7) are statements about **all** scalars in \( F \), so they hold in particular for all scalars in \( K \); the operations \( a + b \) and \( ab \) appearing in them are the same in \( K \) as in \( F \). For (VS8), the identity of \( K \) is the identity \( 1 \) of \( F \), and \( 1\v = \v \) holds in \( V \) over \( F \). Hence \( V \) is a vector space over \( K \).

(b) \( \nC^n \) is a vector space over \( \nC \) by @exm-vector-spaces (a). The subsets \( \nR \subseteq \nC \) and \( \nQ \subseteq \nC \) contain \( 0 \) and \( 1 \) and are closed under the four operations, so (a) applies to both.

(c) The only candidate for scalar multiplication is \( (c, t) \mapsto ct \), the product in \( \nC \). But it does not land in \( \nR \): \( i \in \nC \) and \( 1 \in \nR \), while \( i \cdot 1 = i \notin \nR \). So there is no function \( \nC \times \nR \to \nR \) given by this rule, and \( \nR \) is not a vector space over \( \nC \) with these operations.
:::
