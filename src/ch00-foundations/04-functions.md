# Functions

Sets are the objects of this chapter. The next question is how to move between them, and the tool is a function. Almost everything in linear algebra is a question about a function: a linear map is a function, a matrix will turn out to encode one, and "does \( \A\x = \b \) have a solution, and is it unique?" is a question about whether a function is surjective and injective. This section fixes the language of functions, composition and inverses, and proves the handful of facts about them that the rest of the book uses without comment.

## What a function is

At school a function is usually a formula, such as \( x^2 + 1 \). A formula alone is not enough. The same formula \( x^2 \) behaves differently depending on which numbers we feed it and where we allow the answers to land, and whether an equation \( x^2 = c \) can be solved depends on exactly that information. So a function carries three pieces of data, not one.

*A function is a machine with a fixed input set and a fixed target set that turns each input into exactly one output.*

::: {#def-function}
[Function]

Let \( X \) and \( Y \) be sets. A **function** (or **map**) \( f \colon X \to Y \) is a rule that assigns to **every** element \( x \in X \) **exactly one** element \( f(x) \in Y \). The set \( X \) is the **domain** of \( f \), the set \( Y \) is its **codomain**, and \( f(x) \) is the **value** of \( f \) at \( x \). We also write \( x \mapsto f(x) \).

Two functions \( f \colon X \to Y \) and \( g \colon X' \to Y' \) are **equal** if \( X = X' \), \( Y = Y' \), and \( f(x) = g(x) \) for every \( x \in X \).
:::

In words: the first clause says every input gets an output, so nothing in the domain is left out. The second says the output is unique, so the rule never hesitates between two values. The codomain is where outputs are *allowed* to land; nothing says every element of \( Y \) must be hit.

If you want a definition that avoids the vague word "rule", use the Cartesian product (@def-cartesian-product): a function \( X \to Y \) is a subset \( G \subseteq X \times Y \) such that for every \( x \in X \) there is exactly one \( y \in Y \) with \( (x, y) \in G \). The set \( G \) is the **graph** of \( f \), and \( f(x) \) is that unique \( y \). Nothing in this book depends on which version you prefer.

::: {#exm-functions}
[First examples]

Check each of the following against the two clauses of @def-function.

::: {.enumerate options="label=(\alph*)"}
1. \( f \colon \nR \to \nR \), \( f(x) = 3x - 5 \). Every real \( x \) gives one real number \( 3x - 5 \).
2. \( s \colon \nR^2 \to \nR \), \( s(x, y) = x + y \). The domain is a Cartesian product; each pair gives one sum.
3. \( \ell \colon \{\text{finite strings of the letters } a, b\} \to \nN \), sending a string to its length. The empty string has length \( 0 \), which is why it matters that \( \nN \) contains \( 0 \).
4. For any set \( X \), the rule \( x \mapsto x \) is a function \( X \to X \). It looks too simple to matter, but it will play the role that the number \( 1 \) plays for multiplication.
5. For any set \( Y \), there is exactly one function \( \varnothing \to Y \), the **empty function**. Both clauses are about elements of the domain, and there are none, so they hold vacuously. It is a degenerate case that makes statements like "for every set \( X \)" true without exceptions.
:::
:::

The failures are just as instructive. The rule "\( x \mapsto \) the real number \( y \) with \( y^2 = x \)" is **not** a function \( \nR \to \nR \). At \( x = -1 \) there is no such \( y \), so the first clause fails. At \( x = 4 \) there are two, \( y = 2 \) and \( y = -2 \), so the second clause fails. Repairing both problems gives a genuine function \( [0, \infty) \to \nR \), \( x \mapsto \sqrt{x} \), where \( \sqrt{x} \) means the non-negative root.

The equality clause says the codomain is part of the function. The functions \( \nR \to \nR \), \( x \mapsto x^2 \) and \( \nR \to [0, \infty) \), \( x \mapsto x^2 \) have the same values but are **different** functions. This is not pedantry: we will see in a moment that one of them is surjective and the other is not.

::: {.check}
Let \( f, g \colon \nR \to \nR \) be \( f(x) = \lvert x \rvert \) and \( g(x) = \sqrt{x^2} \). Are \( f \) and \( g \) equal?
:::

::: {.solution}
Yes. They have the same domain and the same codomain, and for every real \( x \) we have \( \sqrt{x^2} = \lvert x \rvert \), because \( \lvert x \rvert \) is the non-negative number whose square is \( x^2 \). Different formulas can describe the same function; what counts is the values.
:::

## Images and preimages

Often we want to push a whole set through a function, or ask which inputs land in a given region. Both operations get a name.

::: {#def-image-preimage}
[Image and preimage]

Let \( f \colon X \to Y \) be a function, \( A \subseteq X \) and \( B \subseteq Y \).

- The **image** of \( A \) under \( f \) is \( f(A) \coloneqq \{ f(a) : a \in A \} \subseteq Y \). The set \( f(X) \) is called the **image of \( f \)**.
- The **preimage** of \( B \) under \( f \) is \( f^{-1}(B) \coloneqq \{ x \in X : f(x) \in B \} \subseteq X \).
:::

In words: \( f(A) \) collects the outputs of the inputs in \( A \). The preimage \( f^{-1}(B) \) collects every input whose output lies in \( B \). So \( y \in f(A) \) means "\( y = f(a) \) for **some** \( a \in A \)", while \( x \in f^{-1}(B) \) means "\( f(x) \in B \)", with no existential quantifier at all.

::: {#exm-image-preimage}
[Images and preimages of the squaring map]

Let \( q \colon \nR \to \nR \), \( q(x) = x^2 \). Compute \( q([-1, 2]) \), \( q^{-1}([1, 4]) \) and \( q^{-1}([-5, -1]) \).
:::

::: {.solution}
As \( x \) runs over \( [-1, 2] \), the square \( x^2 \) takes every value in \( [0, 4] \): values in \( [0, 1] \) come from \( [0, 1] \), values in \( [1, 4] \) from \( [1, 2] \), and no square is negative or exceeds \( 2^2 = 4 \) on this interval. Hence \( q([-1, 2]) = [0, 4] \).

Next, \( x^2 \in [1, 4] \) means \( 1 \le \lvert x \rvert \le 2 \). Hence \( q^{-1}([1, 4]) = [-2, -1] \cup [1, 2] \).

Finally, no real square lies in \( [-5, -1] \), so \( q^{-1}([-5, -1]) = \varnothing \). A preimage may be empty; that is not an error.
:::

::: {.warning}
The symbol \( f^{-1}(B) \) is defined for **every** function, invertible or not; it does not mean that an inverse function exists. For the same reason, pushing forward and pulling back need not undo each other. With \( q(x) = x^2 \) on \( \nR \): for \( B = [-1, 4] \) we get \( q^{-1}(B) = [-2, 2] \) and \( q(q^{-1}(B)) = [0, 4] \ne B \); for \( A = [0, 1] \) we get \( q(A) = [0, 1] \) and \( q^{-1}(q(A)) = [-1, 1] \ne A \).
:::

What does survive is one inclusion in each direction.

::: {#prp-image-preimage-inclusions}
[Image and preimage inclusions]

Let \( f \colon X \to Y \), \( A \subseteq X \) and \( B \subseteq Y \). Then
\[
f\big(f^{-1}(B)\big) \subseteq B \qquad \text{and} \qquad A \subseteq f^{-1}\big(f(A)\big).
\]
:::

::: {.proof}
Let \( y \in f(f^{-1}(B)) \). By @def-image-preimage, \( y = f(x) \) for some \( x \in f^{-1}(B) \), and \( x \in f^{-1}(B) \) means \( f(x) \in B \). Hence \( y \in B \).

Let \( a \in A \). Then \( f(a) \in f(A) \) by definition of the image, so \( a \in f^{-1}(f(A)) \) by definition of the preimage. This proves both inclusions.
:::

The warning shows both inclusions can be strict. In @exr-functions-c3 you will find exactly which property of \( f \) turns each one into an equality.

## Injective, surjective, bijective

Given \( f \colon X \to Y \) and a target \( y \in Y \), the most basic question is how many solutions the equation \( f(x) = y \) has. There are two separate issues: whether there is **at least one** solution, and whether there is **at most one**. In linear algebra these become "does \( A\x = \b \) have a solution?" and "is the solution unique?", and they are answered by different tools. So the two halves deserve separate names.

*Injective means no two inputs collide; surjective means every target is hit; bijective means both, so every equation \( f(x) = y \) has exactly one solution.*

::: {#def-injective-surjective-bijective}
[Injective, surjective, bijective]

Let \( f \colon X \to Y \) be a function.

- \( f \) is **injective** (one-to-one) if **for all** \( x_1, x_2 \in X \), \( f(x_1) = f(x_2) \) implies \( x_1 = x_2 \).
- \( f \) is **surjective** (onto) if **for every** \( y \in Y \) **there exists** \( x \in X \) with \( f(x) = y \). Equivalently, \( f(X) = Y \).
- \( f \) is **bijective** if it is both injective and surjective.
:::

In words: injectivity says that if two inputs give the same output, they were the same input. Equivalently, by the contrapositive (@thm-contrapositive-equivalent), distinct inputs give distinct outputs. Surjectivity says the image of \( f \) fills the whole codomain. The quantifiers matter: in surjectivity the \( x \) is allowed to depend on \( y \).

Negating these, as in @exm-negation-injectivity and @exm-negation-surjectivity, tells us what a counterexample looks like. The map \( f \) is **not injective** when there exist \( x_1 \ne x_2 \) with \( f(x_1) = f(x_2) \): one collision is enough. It is **not surjective** when there exists \( y \in Y \) that equals \( f(x) \) for no \( x \in X \): one missed target is enough.

**The standard moves.** To prove \( f \) injective, write "Suppose \( f(x_1) = f(x_2) \)" and work towards \( x_1 = x_2 \). To prove \( f \) surjective, write "Let \( y \in Y \)" and then produce an \( x \), usually found backwards by solving \( f(x) = y \) on scrap paper, and check forwards that \( f(x) = y \).

The picture below shows maps between three-element sets, drawn as arrows. A collision is two arrows landing on one point; a missed target is a point with no arrow.

\begin{center}
\begin{tikzpicture}[>=Stealth, dot/.style={circle,fill,inner sep=1.4pt}]
  \draw (0,0) ellipse (0.7 and 1.4);
  \draw (2.8,0) ellipse (0.7 and 1.4);
  \node at (0,1.75) {$X$};
  \node at (2.8,1.75) {$Y$};
  \node[dot,label=left:{$1$}] (a1) at (0,0.8) {};
  \node[dot,label=left:{$2$}] (a2) at (0,0) {};
  \node[dot,label=left:{$3$}] (a3) at (0,-0.8) {};
  \node[dot,label=right:{$p$}] (b1) at (2.8,0.8) {};
  \node[dot,label=right:{$q$}] (b2) at (2.8,0) {};
  \node[dot,label=right:{$r$}] (b3) at (2.8,-0.8) {};
  \draw[->] (a1) -- (b1);
  \draw[->] (a2) -- (b1);
  \draw[->] (a3) -- (b2);
  \node[align=center] at (1.4,-2.0) {collision at $p$, nothing reaches $r$:\\ neither injective nor surjective};
  \begin{scope}[xshift=6cm]
  \draw (0,0) ellipse (0.7 and 1.4);
  \draw (2.8,0) ellipse (0.7 and 1.4);
  \node at (0,1.75) {$X$};
  \node at (2.8,1.75) {$Y$};
  \node[dot,label=left:{$1$}] (c1) at (0,0.8) {};
  \node[dot,label=left:{$2$}] (c2) at (0,0) {};
  \node[dot,label=left:{$3$}] (c3) at (0,-0.8) {};
  \node[dot,label=right:{$p$}] (d1) at (2.8,0.8) {};
  \node[dot,label=right:{$q$}] (d2) at (2.8,0) {};
  \node[dot,label=right:{$r$}] (d3) at (2.8,-0.8) {};
  \draw[->] (c1) -- (d2);
  \draw[->] (c2) -- (d3);
  \draw[->] (c3) -- (d1);
  \node[align=center] at (1.4,-2.0) {exactly one arrow into each point:\\ bijective};
  \end{scope}
\end{tikzpicture}
\end{center}

::: {#exm-injective-surjective-bijective}
[Deciding injectivity and surjectivity]

Determine which of the following functions are injective, surjective or bijective.

::: {.enumerate options="label=(\alph*)"}
1. \( f \colon \nR \to \nR \), \( f(x) = 3x - 5 \).
2. \( g \colon \nZ \to \nZ \), \( g(n) = 2n \).
3. \( s \colon \nR^2 \to \nR \), \( s(x, y) = x + y \).
4. \( \id_X \colon X \to X \), \( x \mapsto x \), for any set \( X \).
:::
:::

::: {.solution}
(a) Bijective. Suppose \( f(x_1) = f(x_2) \). Then \( 3x_1 - 5 = 3x_2 - 5 \), so \( 3x_1 = 3x_2 \), and dividing by \( 3 \ne 0 \) gives \( x_1 = x_2 \). Hence \( f \) is injective. Let \( y \in \nR \). Solving \( 3x - 5 = y \) suggests \( x = (y + 5)/3 \), and indeed \( f\big((y+5)/3\big) = (y + 5) - 5 = y \). Hence \( f \) is surjective.

(b) Injective, not surjective. Suppose \( 2n_1 = 2n_2 \); then \( n_1 = n_2 \). But \( 1 \) is not hit: \( 2n = 1 \) has no integer solution, since \( 2n \) is even. Note that the same formula \( x \mapsto 2x \) on \( \nR \to \nR \) *is* surjective; the failure comes from the domain and codomain, not the formula.

(c) Surjective, not injective. Let \( t \in \nR \); then \( s(t, 0) = t \), so \( s \) is surjective. But \( s(1, 0) = 1 = s(0, 1) \) while \( (1, 0) \ne (0, 1) \), a collision, so \( s \) is not injective.

(d) Bijective. If \( \id_X(x_1) = \id_X(x_2) \) then \( x_1 = x_2 \) directly, and every \( x \in X \) is hit by itself. This degenerate case is the model of a bijection and reappears as the identity function below.
:::

The cleanest way to see that domain and codomain are part of the question is to keep the formula \( x \mapsto x^2 \) fixed and change only the sets. Write \( [0, \infty) \) for the non-negative reals.

| Function | Injective? | Surjective? |
|---|---|---|
| \( \nR \to \nR \) | no: \( (-1)^2 = 1^2 \) | no: \( -1 \) is not a square |
| \( \nR \to [0, \infty) \) | no: \( (-1)^2 = 1^2 \) | yes: \( y = (\sqrt{y})^2 \) |
| \( [0, \infty) \to \nR \) | yes | no: \( -1 \) is not a square |
| \( [0, \infty) \to [0, \infty) \) | yes | yes |

For the injective rows: if \( x_1, x_2 \ge 0 \) and \( x_1^2 = x_2^2 \), then \( (x_1 - x_2)(x_1 + x_2) = 0 \). Either \( x_1 = x_2 \), or \( x_1 + x_2 = 0 \), which for non-negative numbers forces \( x_1 = x_2 = 0 \). In both cases \( x_1 = x_2 \).

Read the table as a set of minimal changes. Shrinking the domain from \( \nR \) to \( [0, \infty) \) removes the collision between \( -1 \) and \( 1 \), so the injectivity clause now holds. Shrinking the codomain removes the missed targets, so the surjectivity clause now holds. The formula never changed.

::: {.warning}
Do not confuse injectivity with the statement "\( x_1 = x_2 \Rightarrow f(x_1) = f(x_2) \)". That implication is true for **every** function; it is the second clause of @def-function. Injectivity is its converse, "\( f(x_1) = f(x_2) \Rightarrow x_1 = x_2 \)", and \( x \mapsto x^2 \) on \( \nR \) satisfies the first but not the second.
:::

**Why these definitions.** Surjectivity depends on the codomain, and injectivity on the domain, so neither is a property of a formula alone; this is why @def-function insists on both sets. The names are descriptive: "in-jective" throws the domain *into* the codomain without collisions, and "sur-jective" (French *sur*, onto) lands *onto* all of it. In Chapter 3 we will meet a fast test for linear maps: a linear map is injective exactly when the only input sent to \( \0 \) is \( \0 \). That test is special to linear maps and fails for general functions, which is one reason the general definitions come first.

## Composition

If the outputs of one function can be fed into another, we can run them in sequence. This is the operation that matrix multiplication will describe in Chapter 3.

::: {#def-composition}
[Composition]

Let \( f \colon X \to Y \) and \( g \colon Y \to Z \) be functions. The **composition** \( g \circ f \colon X \to Z \) is defined by
\[
(g \circ f)(x) \coloneqq g\big(f(x)\big) \qquad \text{for every } x \in X.
\]
:::

Read \( g \circ f \) as "\( g \) after \( f \)": the function written on the **right** acts **first**. The definition needs the codomain of \( f \) to equal the domain of \( g \), so that \( g(f(x)) \) makes sense.

::: {#exm-composition}
[Order matters]

(a) Let \( f, g \colon \nR \to \nR \) be \( f(x) = x + 3 \) and \( g(x) = 2x \). Compute \( g \circ f \) and \( f \circ g \).

(b) Let \( q \colon \nR \to [0, \infty) \), \( q(x) = x^2 \), and \( r \colon [0, \infty) \to \nR \), \( r(y) = \sqrt{y} \). Compute \( r \circ q \) and \( q \circ r \).
:::

::: {.solution}
(a) \( (g \circ f)(x) = g(x + 3) = 2x + 6 \), while \( (f \circ g)(x) = f(2x) = 2x + 3 \). At \( x = 0 \) these are \( 6 \ne 3 \), so \( g \circ f \ne f \circ g \). Composition is not commutative, even when both orders make sense.

(b) \( r \circ q \colon \nR \to \nR \) is \( x \mapsto \sqrt{x^2} = \lvert x \rvert \). In the other order, \( q \circ r \colon [0, \infty) \to [0, \infty) \) is \( y \mapsto (\sqrt{y})^2 = y \). So \( q \circ r \) does nothing, while \( r \circ q \) forgets the sign of \( x \). The two orders do not even have the same domain. We will return to this pair when we discuss one-sided inverses.
:::

Although the order matters, the grouping does not. This is what lets us write \( h \circ g \circ f \) without brackets.

::: {#thm-composition-associative}
[Associativity of composition]

Let \( f \colon X \to Y \), \( g \colon Y \to Z \) and \( h \colon Z \to W \) be functions. Then \( (h \circ g) \circ f = h \circ (g \circ f) \).
:::

::: {.proof}
Both sides are functions \( X \to W \). Let \( x \in X \). By @def-composition applied twice on each side,
\[
\big((h \circ g) \circ f\big)(x) = (h \circ g)\big(f(x)\big) = h\big(g(f(x))\big) = h\big((g \circ f)(x)\big) = \big(h \circ (g \circ f)\big)(x).
\]
Since the values agree at every \( x \), the two functions are equal by @def-function.
:::

Next, the properties of the previous subsection pass through composition.

::: {#thm-composition-preserves}
[Composition preserves injectivity and surjectivity]

Let \( f \colon X \to Y \) and \( g \colon Y \to Z \) be functions.

::: {.enumerate options="label=(\alph*)"}
1. If \( f \) and \( g \) are injective, then \( g \circ f \) is injective.
2. If \( f \) and \( g \) are surjective, then \( g \circ f \) is surjective.
3. If \( f \) and \( g \) are bijective, then \( g \circ f \) is bijective.
:::
:::

::: {.idea}
For (a), start from a collision of \( g \circ f \) and peel off one function at a time, outermost first: injectivity of \( g \) removes \( g \), then injectivity of \( f \) removes \( f \). For (b), run backwards: reach \( z \) from some \( y \) using \( g \), then reach that \( y \) from some \( x \) using \( f \).
:::

::: {.proof}
(a) Suppose \( (g \circ f)(x_1) = (g \circ f)(x_2) \), that is, \( g(f(x_1)) = g(f(x_2)) \). Since \( g \) is injective, \( f(x_1) = f(x_2) \). Since \( f \) is injective, \( x_1 = x_2 \). Hence \( g \circ f \) is injective.

(b) Let \( z \in Z \). Since \( g \) is surjective, there is \( y \in Y \) with \( g(y) = z \). Since \( f \) is surjective, there is \( x \in X \) with \( f(x) = y \). Then \( (g \circ f)(x) = g(y) = z \). Hence \( g \circ f \) is surjective.

(c) If \( f \) and \( g \) are bijective, then \( g \circ f \) is injective by (a) and surjective by (b), so it is bijective.
:::

The converse of (a) is false, but half of it survives, and that half is surprisingly useful. Suppose \( g \circ f \) is injective. A collision of \( f \) would be a collision of \( g \circ f \), so \( f \) must be injective; but \( g \) is only used on the image \( f(X) \), so \( g \) may still collide outside it. The surjective case is dual.

::: {#thm-composition-partial-converse}
[Partial converse for compositions]

Let \( f \colon X \to Y \) and \( g \colon Y \to Z \) be functions.

::: {.enumerate options="label=(\alph*)"}
1. If \( g \circ f \) is injective, then \( f \) is injective.
2. If \( g \circ f \) is surjective, then \( g \) is surjective.
:::
:::

::: {.proof}
(a) Suppose \( f(x_1) = f(x_2) \). Applying \( g \) to both sides gives \( (g \circ f)(x_1) = (g \circ f)(x_2) \). Since \( g \circ f \) is injective, \( x_1 = x_2 \). Hence \( f \) is injective.

(b) Let \( z \in Z \). Since \( g \circ f \) is surjective, there is \( x \in X \) with \( g(f(x)) = z \). Put \( y = f(x) \in Y \); then \( g(y) = z \). Hence \( g \) is surjective.
:::

::: {.remark}
The other halves really fail. Take \( X = Z = \{1\} \), \( Y = \{1, 2\} \), \( f(1) = 1 \) and \( g(1) = g(2) = 1 \). Then \( g \circ f = \id_{\{1\}} \) is bijective, yet \( g \) is not injective (\( g(1) = g(2) \)) and \( f \) is not surjective (nothing maps to \( 2 \)).
:::

## Identity and one-sided inverses

The function that does nothing deserves a name, because "undoing \( f \)" means "composing with \( f \) gives the function that does nothing".

::: {#def-identity-function}
[Identity function]

For a set \( X \), the **identity function** on \( X \) is \( \id_X \colon X \to X \), \( \id_X(x) = x \).
:::

For every \( f \colon X \to Y \) we have \( f \circ \id_X = f \) and \( \id_Y \circ f = f \), since both sides send \( x \) to \( f(x) \). Notice the subscripts: on the right of \( f \) the identity lives on the domain, on the left on the codomain.

Now look again at @exm-composition (b). There \( q \circ r = \id_{[0, \infty)} \), but \( r \circ q = \lvert\,\cdot\,\rvert \ne \id_{\nR} \). So \( r \) undoes \( q \) from one side only. This one-sided behavior is common enough to need a word.

::: {#def-left-right-inverse}
[Left and right inverses]

Let \( f \colon X \to Y \). A function \( g \colon Y \to X \) is a **left inverse** of \( f \) if \( g \circ f = \id_X \), and a **right inverse** of \( f \) if \( f \circ g = \id_Y \).
:::

"Left" and "right" refer to where \( g \) is written in the composition. A left inverse recovers the input from the output: \( g(f(x)) = x \). A right inverse picks, for each target \( y \), an input that reaches it: \( f(g(y)) = y \). In @exm-composition (b), \( r \) is a right inverse of \( q \), and \( q \) is a left inverse of \( r \). But \( r \) is **not** a left inverse of \( q \), because \( r(q(-1)) = 1 \ne -1 \).

The descriptions "recovers the input" and "reaches every target" should remind you of injective and surjective. They are exactly that.

::: {#thm-left-inverse-iff-injective}
[Left inverses and injectivity]

Let \( f \colon X \to Y \) with \( X \) **non-empty**. Then \( f \) has a left inverse if and only if \( f \) is injective.
:::

::: {.idea}
(⇒) is @thm-composition-partial-converse with \( g \circ f = \id_X \), which is injective. For (⇐) we must define \( g(y) \) for every \( y \in Y \). If \( y \) is in the image, injectivity gives a **unique** \( x \) with \( f(x) = y \), and \( g(y) \) must be that \( x \). If \( y \) is not in the image, the condition \( g \circ f = \id_X \) says nothing about \( g(y) \), so we send \( y \) anywhere in \( X \). That is where non-emptiness is used.
:::

::: {.proof}
(⇒) Suppose \( g \circ f = \id_X \). The identity \( \id_X \) is injective, so \( f \) is injective by @thm-composition-partial-converse (a).

(⇐) Suppose \( f \) is injective. Since \( X \ne \varnothing \), we may fix some \( x_0 \in X \). Define \( g \colon Y \to X \) as follows. If \( y \in f(X) \), there is some \( x \in X \) with \( f(x) = y \), and this \( x \) is unique because \( f \) is injective; set \( g(y) = x \). If \( y \notin f(X) \), set \( g(y) = x_0 \). Every \( y \) receives exactly one value, so \( g \) is a function. For \( x \in X \), the element \( y = f(x) \) lies in \( f(X) \), and the unique input sent to it is \( x \), so \( g(f(x)) = x \). Hence \( g \circ f = \id_X \), as claimed.
:::

The hypothesis \( X \ne \varnothing \) is not decoration. The empty function \( \varnothing \to \{1\} \) is injective (there are no two inputs to collide), but there is no function \( \{1\} \to \varnothing \) at all, since \( 1 \) would have nowhere to go.

::: {#thm-right-inverse-iff-surjective}
[Right inverses and surjectivity]

Let \( f \colon X \to Y \). Then \( f \) has a right inverse if and only if \( f \) is surjective.
:::

::: {.proof}
(⇒) Suppose \( f \circ g = \id_Y \). The identity \( \id_Y \) is surjective, so \( f \) is surjective by @thm-composition-partial-converse (b).

(⇐) Suppose \( f \) is surjective. For each \( y \in Y \) the set \( f^{-1}(\{y\}) \) is non-empty, so we may choose one element of it and call it \( g(y) \). This defines \( g \colon Y \to X \) with \( f(g(y)) = y \) for every \( y \in Y \), that is, \( f \circ g = \id_Y \).
:::

When \( Y \) is infinite, the step "choose one element from each of infinitely many non-empty sets at once" is an axiom of set theory, the **axiom of choice**; we use it freely and never mention it again in this chapter.

Unlike an inverse in the usual sense, one-sided inverses are rarely unique. For \( q \colon \nR \to [0, \infty) \), \( x \mapsto x^2 \), both \( y \mapsto \sqrt{y} \) and \( y \mapsto -\sqrt{y} \) are right inverses: each picks one of the two square roots.

::: {.check}
Give a function \( f \colon \nN \to \nN \) that has a left inverse but no right inverse.
:::

::: {.solution}
Take \( f(n) = n + 1 \). It is injective, since \( n_1 + 1 = n_2 + 1 \) gives \( n_1 = n_2 \), so by @thm-left-inverse-iff-injective it has a left inverse; explicitly, \( g(m) = m - 1 \) for \( m \ge 1 \) and \( g(0) = 0 \) satisfies \( g(f(n)) = n \). It is not surjective, since \( n + 1 = 0 \) has no solution in \( \nN \). So by @thm-right-inverse-iff-surjective it has no right inverse.
:::

## Inverses

When a function has an inverse on both sides, the two one-sided inverses turn out to coincide, and we get the notion of inverse we know from \( e^x \) and \( \ln x \).

::: {#def-inverse-function}
[Inverse function]

Let \( f \colon X \to Y \). A function \( g \colon Y \to X \) is an **inverse** of \( f \) if
\[
g \circ f = \id_X \qquad \text{and} \qquad f \circ g = \id_Y.
\]
If \( f \) has an inverse, \( f \) is **invertible**.
:::

Both conditions are needed: @exm-composition (b) shows a pair with one but not the other. The next theorem says which functions are invertible and that "the" inverse is justified.

::: {#thm-bijective-iff-invertible}
[Bijective if and only if invertible]

A function \( f \colon X \to Y \) is invertible if and only if it is bijective. Moreover, an inverse of \( f \), when it exists, is **unique**; we denote it \( f^{-1} \colon Y \to X \).
:::

::: {.idea}
For (⇐) one could combine the two one-sided theorems, but that route needs \( X \ne \varnothing \) and a choice. A bijection makes both unnecessary: every \( y \) has **exactly one** preimage, so \( f^{-1}(y) \) is forced. For uniqueness, the standard move is to assume two inverses \( g \) and \( h \), and sandwich: \( g = g \circ (f \circ h) = (g \circ f) \circ h = h \).
:::

::: {.proof}
(⇒) Suppose \( g \) is an inverse of \( f \). Since \( g \circ f = \id_X \) is injective, \( f \) is injective by @thm-composition-partial-converse (a). Since \( f \circ g = \id_Y \) is surjective, \( f \) is surjective by @thm-composition-partial-converse (b). Hence \( f \) is bijective.

(⇐) Suppose \( f \) is bijective, and let \( y \in Y \). Since \( f \) is surjective, some \( x \in X \) has \( f(x) = y \), and since \( f \) is injective, this \( x \) is unique. Define \( g(y) \) to be this \( x \). Then \( f(g(y)) = y \) for every \( y \in Y \), so \( f \circ g = \id_Y \). For \( x \in X \), the unique input sent to \( f(x) \) is \( x \) itself, so \( g(f(x)) = x \), and \( g \circ f = \id_X \). Hence \( g \) is an inverse of \( f \).

(Uniqueness) Suppose \( g \) and \( h \) are both inverses of \( f \). Then
\[
g = g \circ \id_Y = g \circ (f \circ h) = (g \circ f) \circ h = \id_X \circ h = h,
\]
where the third equality is @thm-composition-associative. This proves the theorem.
:::

The uniqueness computation used only \( g \circ f = \id_X \) and \( f \circ h = \id_Y \). So it proves more: **if \( f \) has a left inverse \( g \) and a right inverse \( h \), then \( g = h \)**, and this common function is the inverse. The same sandwich will prove that a matrix has at most one inverse.

::: {.warning}
The notation \( f^{-1} \) now has two meanings. The preimage \( f^{-1}(B) \) of a **set** \( B \subseteq Y \) exists for every \( f \). The inverse function \( f^{-1} \), applied to an **element** \( y \in Y \), exists only for bijective \( f \). Writing \( q^{-1}(4) \) for \( q(x) = x^2 \) on \( \nR \) is meaningless, while \( q^{-1}(\{4\}) = \{-2, 2\} \) is fine. When \( f \) is bijective the two agree: \( f^{-1}(\{y\}) = \{ f^{-1}(y) \} \).
:::

::: {#exm-inverse-function}
[Finding inverses]

For each function, decide whether it is invertible, and if so find its inverse.

::: {.enumerate options="label=(\alph*)"}
1. \( f \colon \nR \to \nR \), \( f(x) = 5 - 2x \).
2. \( t \colon \nR^2 \to \nR^2 \), \( t(x, y) = (y, x) \).
3. \( g \colon \nR \to \nR \), \( g(x) = x^2 \).
4. \( h \colon [0, \infty) \to [0, \infty) \), \( h(x) = x^2 \).
:::
:::

::: {.solution}
(a) Solving \( 5 - 2x = y \) gives \( x = (5 - y)/2 \). Put \( k(y) = (5 - y)/2 \). Check: \( k(f(x)) = (5 - (5 - 2x))/2 = x \) and \( f(k(y)) = 5 - (5 - y) = y \). So \( k \) is an inverse of \( f \), and \( f^{-1}(y) = (5 - y)/2 \).

(b) \( t(t(x, y)) = t(y, x) = (x, y) \), so \( t \circ t = \id_{\nR^2} \). Hence \( t \) is its own inverse: \( t^{-1} = t \).

(c) Not invertible. \( g(-1) = g(1) \), so \( g \) is not injective, hence not bijective, and @thm-bijective-iff-invertible says it has no inverse.

(d) Invertible. By the table in the previous subsection \( h \) is bijective, and the inverse is \( h^{-1}(y) = \sqrt{y} \): indeed \( \sqrt{x^2} = x \) for \( x \ge 0 \) and \( (\sqrt{y})^2 = y \) for \( y \ge 0 \).
:::

To undo two steps, undo the last one first. When you dress, the shirt goes on before the jacket; to undress, the jacket comes off first.

::: {#thm-inverse-of-composition}
[Inverse of a composition]

Let \( f \colon X \to Y \) and \( g \colon Y \to Z \) be bijective. Then \( g \circ f \) is bijective and
\[
(g \circ f)^{-1} = f^{-1} \circ g^{-1}.
\]
:::

::: {.proof}
Using @thm-composition-associative to regroup,
\[
(f^{-1} \circ g^{-1}) \circ (g \circ f) = f^{-1} \circ (g^{-1} \circ g) \circ f = f^{-1} \circ \id_Y \circ f = f^{-1} \circ f = \id_X,
\]
and in the same way \( (g \circ f) \circ (f^{-1} \circ g^{-1}) = g \circ (f \circ f^{-1}) \circ g^{-1} = g \circ g^{-1} = \id_Z \). Hence \( f^{-1} \circ g^{-1} \) is an inverse of \( g \circ f \). By @thm-bijective-iff-invertible, \( g \circ f \) is bijective and its unique inverse is \( f^{-1} \circ g^{-1} \), as claimed.
:::

The same reversal will appear for matrices as \( (\A\B)^{-1} = \B^{-1} \A^{-1} \), and for the same reason.

## Maps between finite sets

For functions between two finite sets **of the same size**, one of the two conditions comes for free. This is the pigeonhole principle, and it is the ancestor of a move used constantly from Chapter 3 on: instead of checking both injectivity and surjectivity, count, and check only one.

We write \( \lvert X \rvert \) for the number of elements of a finite set \( X \). We use two counting facts about lists without proof: a list of \( n \) entries with a repeated entry contains at most \( n - 1 \) distinct elements, and a subset of a finite set \( Y \) with \( \lvert Y \rvert \) elements is all of \( Y \).

::: {#thm-finite-injective-iff-surjective}
[Injective iff surjective for finite sets of equal size]

Let \( X \) and \( Y \) be finite sets with \( \lvert X \rvert = \lvert Y \rvert \), and let \( f \colon X \to Y \). Then \( f \) is injective if and only if \( f \) is surjective. In that case \( f \) is bijective.
:::

::: {.idea}
List the elements of \( X \) as \( x_1, \dots, x_n \); the image \( f(X) \) is then listed by \( f(x_1), \dots, f(x_n) \). Injective means this list has no repeats, so it has \( n \) distinct entries and must fill \( Y \). Surjective means the list fills \( Y \), which has \( n \) elements, so there is no room for a repeat.
:::

::: {.proof}
Let \( n = \lvert X \rvert = \lvert Y \rvert \), and write \( X = \{x_1, \dots, x_n\} \) with the \( x_i \) distinct. By @def-image-preimage, \( f(X) \) consists of the entries of the list \( f(x_1), \dots, f(x_n) \).

(⇒) Suppose \( f \) is injective. Since the \( x_i \) are distinct, the entries \( f(x_1), \dots, f(x_n) \) are distinct. Hence \( f(X) \) is a subset of \( Y \) with \( n = \lvert Y \rvert \) elements, so \( f(X) = Y \), and \( f \) is surjective.

(⇐) We prove the contrapositive (@thm-contrapositive-equivalent). Suppose \( f \) is not injective. Then \( f(x_i) = f(x_j) \) for some \( i \ne j \), so the list \( f(x_1), \dots, f(x_n) \) has a repeated entry and \( f(X) \) has at most \( n - 1 \) elements. Hence \( f(X) \ne Y \), and \( f \) is not surjective.

So if \( f \) is injective or surjective, the two directions show that it is both, that is, bijective.
:::

For a finite set \( X \), this applies to every \( f \colon X \to X \): such a map is injective if and only if it is surjective. In Chapter 3 the same shape of statement returns for linear maps \( V \to V \) on a finite-dimensional space, with dimension playing the role of the number of elements.

::: {.warning}
The theorem needs finiteness. The map \( g \colon \nN \to \nN \), \( g(n) = 2n \), is injective but misses every odd number, so it is not surjective, even though domain and codomain are the same set. Infinite sets have room for an injection into a proper part of themselves.
:::

## Exercises

### A. Check your understanding

::: {#exr-functions-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State what it means for \( f \colon X \to Y \) to be injective, and what it means to be surjective.
2. True or false: the functions \( \nR \to \nR \), \( x \mapsto x^3 \) and \( \nR \to \nR \), \( x \mapsto x \cdot x \cdot x \) are equal. Give a reason.
3. True or false: if \( g \circ f \) is injective, then \( g \) is injective. Give a reason.
4. Write down the first line of a proof that a function \( f \) is injective, and the first line of a proof that it is surjective.
5. True or false: the preimage \( f^{-1}(B) \) is defined only when \( f \) is bijective.
6. True or false: every injective function \( \{1, 2, 3\} \to \{1, 2, 3\} \) is bijective. Name the result you use.
:::
:::

::: {.solution}
(a) \( f \) is injective if for all \( x_1, x_2 \in X \), \( f(x_1) = f(x_2) \) implies \( x_1 = x_2 \). It is surjective if for every \( y \in Y \) there exists \( x \in X \) with \( f(x) = y \).

(b) True. They have the same domain and codomain, and \( x^3 = x \cdot x \cdot x \) for every real \( x \). Equality of functions is about values, not formulas.

(c) False. In the remark after @thm-composition-partial-converse, \( g \circ f = \id_{\{1\}} \) is injective but \( g(1) = g(2) \). Only \( f \) is forced to be injective.

(d) Injective: "Suppose \( x_1, x_2 \in X \) satisfy \( f(x_1) = f(x_2) \)." Surjective: "Let \( y \in Y \)."

(e) False. \( f^{-1}(B) = \{ x \in X : f(x) \in B \} \) makes sense for every function; see @def-image-preimage and the warning after it.

(f) True, by @thm-finite-injective-iff-surjective: domain and codomain are finite with the same number of elements, so an injective map is surjective, hence bijective.
:::

### B. Practice

::: {#exr-functions-b1}
[B1: Injective or surjective?]

Determine whether each function is injective, and whether it is surjective. Justify your answers.

::: {.enumerate options="label=(\alph*)"}
1. \( f \colon \nZ \to \nZ \), \( f(n) = 3n + 1 \).
2. \( g \colon \nR^2 \to \nR^2 \), \( g(x, y) = (x + y, x - y) \).
3. \( h \colon \nN \to \nN \), \( h(n) = \lfloor n/2 \rfloor \), the largest integer not exceeding \( n/2 \).
4. \( p \colon \nR \to \nR^2 \), \( p(t) = (t, t^2) \).
:::
:::

::: {.solution}
(a) Injective, not surjective. Suppose \( 3n_1 + 1 = 3n_2 + 1 \). Then \( 3n_1 = 3n_2 \), so \( n_1 = n_2 \). But \( 0 \) is not hit: \( 3n + 1 = 0 \) would give \( n = -1/3 \notin \nZ \).

(b) Bijective. Suppose \( g(x_1, y_1) = g(x_2, y_2) \). Then \( x_1 + y_1 = x_2 + y_2 \) and \( x_1 - y_1 = x_2 - y_2 \). Adding the two equations gives \( 2x_1 = 2x_2 \), and subtracting gives \( 2y_1 = 2y_2 \), so \( (x_1, y_1) = (x_2, y_2) \). Hence \( g \) is injective. Let \( (u, v) \in \nR^2 \). Then
\[
g\Big(\frac{u + v}{2}, \frac{u - v}{2}\Big) = \Big(\frac{u + v}{2} + \frac{u - v}{2},\ \frac{u + v}{2} - \frac{u - v}{2}\Big) = (u, v).
\]
Hence \( g \) is surjective.

(c) Surjective, not injective. Let \( m \in \nN \). Then \( h(2m) = \lfloor m \rfloor = m \), so \( h \) is surjective. But \( h(0) = 0 = h(1) \), a collision, so \( h \) is not injective.

(d) Injective, not surjective. Suppose \( (t_1, t_1^2) = (t_2, t_2^2) \). Comparing first coordinates gives \( t_1 = t_2 \). But \( (0, 1) \) is not hit: \( p(t) = (0, 1) \) forces \( t = 0 \) and then \( t^2 = 0 \ne 1 \).
:::

::: {#exr-functions-b2}
[B2: Inverses]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( f \colon \nR \to \nR \), \( f(x) = 7 - 4x \), is invertible and find \( f^{-1} \).
2. Let \( D = \nR \setminus \{1\} \) and define \( k \colon D \to D \) by \( k(x) = \dfrac{x + 1}{x - 1} \). Show that \( k \) really takes values in \( D \), and that \( k \circ k = \id_D \). Hence deduce that \( k \) is bijective and find \( k^{-1} \).
3. With \( g \) as in B1(b), find \( g^{-1} \). Hence find the inverse of \( g \circ g \) without computing \( g \circ g \) first.
:::
:::

::: {.solution}
(a) Put \( e(y) = (7 - y)/4 \). Then \( e(f(x)) = (7 - (7 - 4x))/4 = x \) and \( f(e(y)) = 7 - (7 - y) = y \). So \( e \) is an inverse of \( f \), and by @thm-bijective-iff-invertible \( f \) is invertible with \( f^{-1}(y) = (7 - y)/4 \).

(b) For \( x \in D \) the denominator \( x - 1 \) is non-zero, so \( k(x) \) is a real number. If \( k(x) = 1 \), then \( x + 1 = x - 1 \), that is, \( 1 = -1 \), which is false. Hence \( k(x) \in D \). Next, for \( x \in D \),
\[
k(k(x)) = \frac{\frac{x+1}{x-1} + 1}{\frac{x+1}{x-1} - 1} = \frac{(x + 1) + (x - 1)}{(x + 1) - (x - 1)} = \frac{2x}{2} = x,
\]
where the second equality multiplies numerator and denominator by \( x - 1 \ne 0 \). So \( k \circ k = \id_D \). This says \( k \) is an inverse of itself, so \( k \) is invertible, hence bijective by @thm-bijective-iff-invertible, and \( k^{-1} = k \).

(c) The solution of B1(b) shows that \( e(u, v) = \big(\frac{u+v}{2}, \frac{u-v}{2}\big) \) satisfies \( g \circ e = \id_{\nR^2} \). Also \( e(g(x, y)) = e(x + y, x - y) = \big(\frac{2x}{2}, \frac{2y}{2}\big) = (x, y) \), so \( e \circ g = \id_{\nR^2} \). Hence \( g^{-1} = e \). By @thm-inverse-of-composition,
\[
(g \circ g)^{-1} = g^{-1} \circ g^{-1}, \qquad g^{-1}\big(g^{-1}(u, v)\big) = g^{-1}\Big(\frac{u+v}{2}, \frac{u-v}{2}\Big) = \Big(\frac{u}{2}, \frac{v}{2}\Big).
\]
(As a check, \( g(g(x, y)) = g(x + y, x - y) = (2x, 2y) \), which \( (u, v) \mapsto (u/2, v/2) \) indeed undoes.)
:::

::: {#exr-functions-b3}
[B3: Images of unions and intersections]

Let \( f \colon X \to Y \) and \( A_1, A_2 \subseteq X \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( f(A_1 \cup A_2) = f(A_1) \cup f(A_2) \).
2. Prove that \( f(A_1 \cap A_2) \subseteq f(A_1) \cap f(A_2) \).
3. Using \( q(x) = x^2 \) on \( \nR \), give an example where the inclusion in (b) is strict.
:::
:::

::: {.solution}
(a) We use double inclusion (@thm-double-inclusion).

(⊆) Let \( y \in f(A_1 \cup A_2) \). Then \( y = f(a) \) for some \( a \in A_1 \cup A_2 \). If \( a \in A_1 \), then \( y \in f(A_1) \); if \( a \in A_2 \), then \( y \in f(A_2) \). In either case \( y \in f(A_1) \cup f(A_2) \).

(⊇) Let \( y \in f(A_1) \cup f(A_2) \). If \( y \in f(A_1) \), then \( y = f(a) \) for some \( a \in A_1 \subseteq A_1 \cup A_2 \), so \( y \in f(A_1 \cup A_2) \). The case \( y \in f(A_2) \) is the same with the roles of \( A_1 \) and \( A_2 \) swapped. This proves the equality.

(b) Let \( y \in f(A_1 \cap A_2) \). Then \( y = f(a) \) for some \( a \in A_1 \cap A_2 \). Since \( a \in A_1 \), \( y \in f(A_1) \), and since \( a \in A_2 \), \( y \in f(A_2) \). Hence \( y \in f(A_1) \cap f(A_2) \).

(c) Take \( A_1 = \{-1\} \) and \( A_2 = \{1\} \). Then \( A_1 \cap A_2 = \varnothing \), so \( q(A_1 \cap A_2) = \varnothing \), while \( q(A_1) \cap q(A_2) = \{1\} \cap \{1\} = \{1\} \). The inclusion is strict. The collision \( q(-1) = q(1) \) is what goes wrong; for an injective \( f \), equality holds in (b).
:::

### C. Going deeper

::: {#exr-functions-c1}
[C1: Left inverses are not unique]

::: {.enumerate options="label=(\alph*)"}
1. Let \( f \colon X \to Y \) be injective but **not** surjective, with \( X \) having at least two elements. Prove that \( f \) has at least two different left inverses.
2. Find two different left inverses of \( f \colon \nN \to \nN \), \( f(n) = n + 1 \).
3. Explain why a bijective function has exactly one left inverse.
:::

*Hint for (a): look at the proof of @thm-left-inverse-iff-injective and ask where it made a free choice.*
:::

::: {.solution}
(a) Since \( f \) is not surjective, there is \( y_0 \in Y \setminus f(X) \). Since \( X \) has at least two elements, there are \( x_0 \ne x_1 \) in \( X \). As in the proof of @thm-left-inverse-iff-injective, for \( y \in f(X) \) let \( \bar{y} \) be the unique \( x \in X \) with \( f(x) = y \). Define \( g_0, g_1 \colon Y \to X \) by \( g_i(y) = \bar{y} \) for \( y \in f(X) \), and \( g_i(y) = x_i \) for \( y \notin f(X) \). The proof of @thm-left-inverse-iff-injective shows that each \( g_i \) is a left inverse of \( f \), since \( g_i(f(x)) = x \) uses only the values on \( f(X) \). But \( g_0(y_0) = x_0 \ne x_1 = g_1(y_0) \), so \( g_0 \ne g_1 \).

(b) The only element missed by \( f \) is \( 0 \). Define \( g_0(m) = m - 1 \) for \( m \ge 1 \) and \( g_0(0) = 0 \); define \( g_1(m) = m - 1 \) for \( m \ge 1 \) and \( g_1(0) = 5 \). Both satisfy \( g_i(n + 1) = n \) for every \( n \in \nN \), and \( g_0(0) \ne g_1(0) \).

(c) Let \( f \) be bijective, and let \( g \) be any left inverse. By @thm-bijective-iff-invertible, \( f \) has an inverse \( f^{-1} \), which in particular is a right inverse. By the observation following that theorem, a left inverse and a right inverse of the same function are equal, so \( g = f^{-1} \). Hence every left inverse equals \( f^{-1} \). Conversely, \( f^{-1} \) is itself a left inverse, since \( f^{-1} \circ f = \id_X \). So \( f \) has exactly one left inverse.
:::

::: {#exr-functions-c2}
[C2: Self-maps of finite and infinite sets]

::: {.enumerate options="label=(\alph*)"}
1. Let \( X \) be a finite set and \( f \colon X \to X \) injective. Prove that \( f \) is bijective.
2. Show that (a) fails for \( X = \nN \): give an injective \( f \colon \nN \to \nN \) that is not bijective.
3. Give a surjective \( h \colon \nN \to \nN \) that is not bijective.
4. Let \( X \) be finite and \( f, g \colon X \to X \) with \( g \circ f = \id_X \). Prove that \( f \circ g = \id_X \) as well.
:::

*Hint for (d): first show that \( f \) is bijective.*
:::

::: {.solution}
(a) The domain and codomain are the same finite set, so \( \lvert X \rvert = \lvert X \rvert \). By @thm-finite-injective-iff-surjective, the injective map \( f \) is bijective.

(b) \( f(n) = n + 1 \) is injective, since \( n_1 + 1 = n_2 + 1 \) gives \( n_1 = n_2 \), but \( 0 \) is not of the form \( n + 1 \) with \( n \in \nN \). Hence \( f \) is not surjective, so not bijective.

(c) Take \( h(n) = \lfloor n/2 \rfloor \). By B1(c) it is surjective but not injective.

(d) Since \( g \circ f = \id_X \) is injective, \( f \) is injective by @thm-composition-partial-converse (a). By (a), \( f \) is bijective, so it has an inverse \( f^{-1} \) by @thm-bijective-iff-invertible. Then
\[
g = g \circ \id_X = g \circ (f \circ f^{-1}) = (g \circ f) \circ f^{-1} = \id_X \circ f^{-1} = f^{-1},
\]
using @thm-composition-associative. Hence \( f \circ g = f \circ f^{-1} = \id_X \), as claimed. (For \( X = \nN \) this fails: with \( f(n) = n + 1 \) and \( g_0 \) from C1(b), \( g_0 \circ f = \id_{\nN} \) but \( f(g_0(0)) = 1 \ne 0 \). The matrix version of (d), "\( \A\B = \I \) implies \( \B\A = \I \) for square matrices", is proved in Chapter 2.)
:::

::: {#exr-functions-c3}
[C3: When images and preimages undo each other]

Let \( f \colon X \to Y \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( f(f^{-1}(B)) = B \) for **every** \( B \subseteq Y \) if and only if \( f \) is surjective.
2. Prove that \( f^{-1}(f(A)) = A \) for **every** \( A \subseteq X \) if and only if \( f \) is injective.
:::

*Hint: for each direction you need only one well-chosen set; try a one-element set.*
:::

::: {.solution}
(a) (⇒) Suppose the equality holds for every \( B \), and let \( y \in Y \). Taking \( B = \{y\} \) gives \( f(f^{-1}(\{y\})) = \{y\} \), so \( y \in f(f^{-1}(\{y\})) \). Hence \( y = f(x) \) for some \( x \), and \( f \) is surjective.

(⇐) Suppose \( f \) is surjective, and let \( B \subseteq Y \). The inclusion \( f(f^{-1}(B)) \subseteq B \) is @prp-image-preimage-inclusions. For the reverse, let \( y \in B \). Since \( f \) is surjective, \( y = f(x) \) for some \( x \in X \). Then \( f(x) \in B \), so \( x \in f^{-1}(B) \), and hence \( y = f(x) \in f(f^{-1}(B)) \). By @thm-double-inclusion, \( f(f^{-1}(B)) = B \).

(b) (⇒) Suppose the equality holds for every \( A \), and suppose \( f(x_1) = f(x_2) \). Taking \( A = \{x_1\} \) gives \( f^{-1}(\{f(x_1)\}) = \{x_1\} \). Since \( f(x_2) = f(x_1) \), we have \( x_2 \in f^{-1}(\{f(x_1)\}) = \{x_1\} \), so \( x_2 = x_1 \). Hence \( f \) is injective.

(⇐) Suppose \( f \) is injective, and let \( A \subseteq X \). The inclusion \( A \subseteq f^{-1}(f(A)) \) is @prp-image-preimage-inclusions. For the reverse, let \( x \in f^{-1}(f(A)) \). Then \( f(x) \in f(A) \), so \( f(x) = f(a) \) for some \( a \in A \). Since \( f \) is injective, \( x = a \in A \). By @thm-double-inclusion, \( f^{-1}(f(A)) = A \).
:::
