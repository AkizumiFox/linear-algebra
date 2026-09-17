# How Proofs Are Built

The previous section taught us to read statements: what an implication claims, what the quantifiers demand, and how to negate. Now we write proofs of them. A proof is a chain of statements, each one justified by a definition, a hypothesis or an earlier result, that ends in the statement we want. This section collects the handful of shapes that almost every proof in this book takes, shows each on a small fact about integers, and ends with the conventions that the book's proofs follow.

Throughout, a theorem will usually come with two blocks. The **Idea** says how the argument was found, often by working backwards from the goal. The **Proof** then presents the argument forwards, one justified step at a time. Read the Idea first, then check the Proof line by line.

## Direct proof

Most statements have the form "for every \( x \), if \( P(x) \) then \( Q(x) \)". The direct way to prove this follows the shape of the statement:

1. **Let** \( x \) be arbitrary. By @def-quantifiers, a universal statement is a claim about each element, so we must not pick a convenient one.
2. **Suppose** \( P(x) \). By @def-implication-converse-contrapositive, the implication can only fail when \( P(x) \) is true, so that is the only case we need to handle.
3. **Unwind** \( P(x) \) and \( Q(x) \) into their definitions. Then push forward from what we have towards what we want, often working backwards from the goal on scrap paper first.

Before we can prove anything about integers, we need definitions to unwind.

::: {#def-parity}
[Even and odd]

An integer \( n \) is **even** if there **exists** an integer \( k \) with \( n = 2k \). An integer \( n \) is **odd** if there **exists** an integer \( k \) with \( n = 2k + 1 \).
:::

So \( 0 = 2 \cdot 0 \) is even, \( -6 = 2 \cdot (-3) \) is even, and \( 7 = 2 \cdot 3 + 1 \) is odd. Each definition is an existential statement: to show a number is even, we must produce the integer \( k \). We use the school fact that **every integer is even or odd, and not both**; an exercise at the end of this section proves a more general fact about remainders.

::: {#prp-sum-of-evens}
[Sum of even integers]

For all integers \( m \) and \( n \), if \( m \) and \( n \) are even, then \( m + n \) is even.
:::

::: {.idea}
Givens: \( m = 2a \) and \( n = 2b \) for some integers \( a, b \). Goal: \( m + n = 2k \) for some integer \( k \). So we must *find* \( k \). Adding the givens gives \( m + n = 2a + 2b = 2(a + b) \), and \( k = a + b \) is the witness.
:::

::: {.proof}
Let \( m \) and \( n \) be even integers. By @def-parity, there exist integers \( a \) and \( b \) with \( m = 2a \) and \( n = 2b \). Then
\[
m + n = 2a + 2b = 2(a + b).
\]
Since \( a + b \) is an integer, @def-parity shows that \( m + n \) is even. This proves the claim.
:::

The pattern is worth naming. The hypothesis "\( m \) is even" is an **existence** statement, so using it hands us an integer \( a \) to work with. The goal "\( m + n \) is even" is also an existence statement, so proving it means **producing** an integer, here \( a + b \). The two letters \( a \) and \( b \) must be different: \( m \) and \( n \) are arbitrary, so their halves have nothing to do with each other.

::: {.warning}
**A proof of a "for every" statement cannot start with a specific example.** Writing "\( 4 + 6 = 10 \), which is even" checks one case and proves nothing about all even integers. Equally, writing \( m = 2k \) and \( n = 2k \) with the **same** \( k \) silently assumes \( m = n \), so it only proves that \( 2m \) is even.
:::

## Proof by contrapositive

Sometimes the direct route stalls. Consider the statement "if \( n^2 \) is even, then \( n \) is even". Going directly, we would suppose \( n^2 = 2k \) and try to say something about \( n \). But \( n = \pm\sqrt{2k} \) is not visibly of the form \( 2 \cdot (\text{integer}) \), and we are stuck.

By @thm-contrapositive-equivalent, "if \( P \) then \( Q \)" is equivalent to "if not \( Q \) then not \( P \)". Here the contrapositive is "if \( n \) is not even, then \( n^2 \) is not even", that is, "if \( n \) is odd, then \( n^2 \) is odd". Now the hypothesis hands us a formula for \( n \), and squaring a formula is easy.

::: {#prp-square-even}
[Even squares]

For every integer \( n \), if \( n^2 \) is even, then \( n \) is even.
:::

::: {.idea}
The hypothesis \( n^2 \) even says little about \( n \), but "\( n \) odd" gives \( n = 2k + 1 \) explicitly. So prove the contrapositive: from \( n = 2k + 1 \), expand \( n^2 \) and look for the form \( 2(\ldots) + 1 \).
:::

::: {.proof}
Let \( n \) be an integer. By @thm-contrapositive-equivalent, it suffices to prove that if \( n \) is not even, then \( n^2 \) is not even. Suppose \( n \) is not even. Since every integer is even or odd, \( n \) is odd, so by @def-parity there is an integer \( k \) with \( n = 2k + 1 \). Then
\[
n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1.
\]
Since \( 2k^2 + 2k \) is an integer, \( n^2 \) is odd by @def-parity. Since no integer is both even and odd, \( n^2 \) is not even. This proves the contrapositive, and hence the statement.
:::

A contrapositive proof is a direct proof of a different, equivalent implication. Use it when the negated conclusion gives more to work with than the hypothesis does.

## Proof by contradiction

To prove a statement \( S \) by **contradiction**, suppose that \( S \) is false and deduce something impossible: a statement together with its negation. Why does this work? We have shown that the implication \( \neg S \Rightarrow (R \wedge \neg R) \) is true, for some statement \( R \). Its conclusion \( R \wedge \neg R \) is false in every row, so by @def-implication-converse-contrapositive the implication can only be true if its hypothesis \( \neg S \) is false. Hence \( S \) is true.

Contradiction is the natural tool for statements that say something **cannot** happen, or that there is **no** object of some kind. Such statements give nothing to start from directly, while their negation hands us an object to study.

Statements about fractions and primes need the language of divisibility.

::: {#def-divisibility-prime}
[Divisibility and primes]

Let \( a \) and \( b \) be integers. We say \( a \) **divides** \( b \), written \( a \mid b \), if there **exists** an integer \( k \) with \( b = ak \). An integer \( p \) is **prime** if \( p \ge 2 \) and the only **positive** divisors of \( p \) are \( 1 \) and \( p \).
:::

For example, \( 3 \mid 12 \) since \( 12 = 3 \cdot 4 \), and \( 3 \nmid 7 \). The first primes are \( 2, 3, 5, 7, 11 \). The integer \( 1 \) is **not** prime, because the definition requires \( p \ge 2 \); this convention is what makes factorizations into primes unique. In this language, \( n \) is even exactly when \( 2 \mid n \).

A real number is **rational** if it equals \( a/b \) for some integers \( a \) and \( b \) with \( b \ne 0 \), and **irrational** otherwise. We use the school fact that every rational number can be written **in lowest terms**: as \( a/b \) with \( b \ge 1 \), where no integer \( d \ge 2 \) divides both \( a \) and \( b \). (We justify this fact at the end of this section.)

::: {#thm-sqrt2-irrational}
[Irrationality of \( \sqrt{2} \)]

There is no rational number whose square is \( 2 \). That is, \( \sqrt{2} \) is irrational.
:::

::: {.idea}
"There is no rational \( x \) with \( x^2 = 2 \)" gives nothing to hold, so suppose there is one, and write it in lowest terms \( a/b \). Clearing denominators gives \( a^2 = 2b^2 \), an integer equation. Then @prp-square-even applies twice: first \( a \) is even, then (after substituting \( a = 2c \)) \( b \) is even. That contradicts lowest terms.
:::

::: {.proof}
Suppose, for a contradiction, that some rational number \( x \) satisfies \( x^2 = 2 \). Write \( x = a/b \) in lowest terms, so \( b \ge 1 \) and no integer \( d \ge 2 \) divides both \( a \) and \( b \). Then \( a^2 / b^2 = 2 \), and multiplying by \( b^2 \), which is non-zero, gives
\[
a^2 = 2b^2.
\]
Therefore \( a^2 \) is even by @def-parity, and hence \( a \) is even by @prp-square-even. Write \( a = 2c \) with \( c \) an integer. Substituting gives \( 4c^2 = 2b^2 \), so \( b^2 = 2c^2 \) is even. By @prp-square-even again, \( b \) is even. Thus \( 2 \) divides both \( a \) and \( b \), which contradicts the choice of \( a/b \) in lowest terms. Hence no rational number has square \( 2 \).
:::

The contradiction came from the lowest-terms condition, which is the hypothesis we chose to impose. That is typical: in a contradiction proof, look for the assumption you have not yet used, because the contradiction usually comes from there.

::: {.remark}
If a contradiction proof of "\( P \Rightarrow Q \)" assumes \( P \) and \( \neg Q \) and then only ever derives \( \neg P \), it is really a contrapositive proof in disguise. Write it as a contrapositive; it is shorter and clearer.
:::

A second classic contradiction proof, that there are infinitely many primes, needs one more tool and appears at the end of this section.

## Proof by cases

When a hypothesis splits naturally into possibilities, handle each one separately. If \( P_1 \vee P_2 \) is true, and both \( P_1 \Rightarrow Q \) and \( P_2 \Rightarrow Q \) are true, then \( Q \) is true: whichever of \( P_1, P_2 \) holds, its implication delivers \( Q \). The cases must **cover every possibility**. They are allowed to overlap.

::: {#prp-n-squared-plus-n-even}
[\( n^2 + n \) is even]

For every integer \( n \), the integer \( n^2 + n \) is even.
:::

::: {.idea}
Nothing about \( n \) is given, but every integer is even or odd, and each case gives a formula for \( n \). Factoring first, \( n^2 + n = n(n + 1) \), makes each case a one-line computation.
:::

::: {.proof}
Let \( n \) be an integer. Then \( n^2 + n = n(n + 1) \). Since every integer is even or odd, there are two cases.

*Case 1: \( n \) is even.* By @def-parity, \( n = 2k \) for some integer \( k \). Then \( n(n + 1) = 2\bigl(k(n + 1)\bigr) \), and \( k(n + 1) \) is an integer.

*Case 2: \( n \) is odd.* By @def-parity, \( n = 2k + 1 \) for some integer \( k \). Then \( n + 1 = 2(k + 1) \), so \( n(n + 1) = 2\bigl(n(k + 1)\bigr) \), and \( n(k + 1) \) is an integer.

In both cases \( n^2 + n \) is even by @def-parity. This shows the claim for every integer \( n \).
:::

## Proving "if and only if"

By the definition of the biconditional in the previous section, \( P \Leftrightarrow Q \) means \( (P \Rightarrow Q) \wedge (Q \Rightarrow P) \). So a proof of an "iff" has **two directions**, labeled \( (\Rightarrow) \) and \( (\Leftarrow) \), and each is proved by any method we like. Often one direction is already known.

::: {#prp-even-iff-square-even}
[Parity of a square]

For every integer \( n \), \( n \) is even if and only if \( n^2 \) is even.
:::

::: {.proof}
Let \( n \) be an integer.

\( (\Rightarrow) \) Suppose \( n \) is even, so \( n = 2k \) for some integer \( k \) by @def-parity. Then \( n^2 = 4k^2 = 2(2k^2) \), and \( 2k^2 \) is an integer, so \( n^2 \) is even.

\( (\Leftarrow) \) This is @prp-square-even.

Both directions hold, so \( n \) is even if and only if \( n^2 \) is even.
:::

::: {.warning}
**Reversing the steps is not automatic.** A common slip is to "prove the converse" by rewriting the same argument backwards without checking that every step reverses. For instance, from \( x = 2 \) we get \( x^2 = 4 \); but from \( x^2 = 4 \) we only get \( x = 2 \) **or** \( x = -2 \). Each direction needs its own justification.
:::

## Existence and uniqueness

To prove "there exists \( x \) with \( P(x) \)", the most direct method is to **produce a witness** and check it. For example, "there exists an integer \( n \) with \( n^2 = n + 2 \)" is proved by \( n = 2 \): indeed \( 2^2 = 4 = 2 + 2 \).

To prove "there is **at most one** \( x \) with \( P(x) \)", the standard move is: *suppose \( x \) and \( x' \) both satisfy \( P \), and show \( x = x' \).* Notice that we do not assume \( x \ne x' \); we simply take two objects with the property and prove they are the same. "There exists a **unique** \( x \)" means both existence and at most one, so it takes both arguments.

Here is an example that we will meet again when we study fields and groups. A **binary operation** \( \ast \) on a collection \( S \) is a rule that assigns to each ordered pair \( a, b \) of elements of \( S \) an element \( a \ast b \) of \( S \). Addition and multiplication of integers are binary operations on \( \nZ \). An **identity element** for \( \ast \) is an element \( e \) of \( S \) such that \( e \ast a = a \) and \( a \ast e = a \) for **every** \( a \) in \( S \).

::: {#prp-identity-element-unique}
[Uniqueness of the identity]

Let \( \ast \) be a binary operation on \( S \). Then \( \ast \) has at most one identity element.
:::

::: {.idea}
Suppose \( e \) and \( e' \) are both identities. The only thing we know about them is how they behave in a product, so look at the one product that involves both, \( e \ast e' \), and evaluate it in two ways.
:::

::: {.proof}
Suppose \( e \) and \( e' \) are both identity elements for \( \ast \). Since \( e' \) is an identity, \( e \ast e' = e \), taking \( a = e \) in its defining property. Since \( e \) is an identity, \( e \ast e' = e' \), taking \( a = e' \) in its defining property. Therefore \( e = e \ast e' = e' \). This shows that any two identity elements are equal.
:::

So \( 0 \) is **the** identity for addition on \( \nZ \), and \( 1 \) is **the** identity for multiplication. The result says nothing about existence. Subtraction on \( \nZ \) has no identity at all: \( a - e = a \) for every \( a \) forces \( e = 0 \), but then \( e - a = -a \), which is not \( a \) when \( a = 1 \). Uniqueness proofs of exactly this shape will recur for zero vectors, negatives, inverse matrices and inverse functions.

## Counterexamples

By @def-negation-of-quantifiers, the negation of "\( \forall x : P(x) \)" is "\( \exists x : \neg P(x) \)". So to **refute** a universal statement, one witness suffices: a single \( x \) where \( P(x) \) fails. Such an \( x \) is a **counterexample**. Conversely, no number of examples can prove a universal statement over an infinite range.

::: {#exm-every-prime-odd}
[Refuting "every prime is odd"]

Decide whether every prime number is odd. Justify your answer.
:::

::: {.solution}
False. The statement is \( \forall p \) prime : \( p \) is odd, so by @def-negation-of-quantifiers one prime that is not odd refutes it. Take \( p = 2 \). It is prime, since \( 2 \ge 2 \) and a positive divisor of \( 2 \) is at most \( 2 \), so it is \( 1 \) or \( 2 \). It is even, since \( 2 = 2 \cdot 1 \), and hence not odd. So \( 2 \) is a counterexample.
:::

::: {.warning}
**Many examples prove nothing.** The number \( n^2 + n + 41 \) is prime for every integer \( n \) from \( 0 \) to \( 39 \). Yet the statement "\( n^2 + n + 41 \) is prime for every \( n \ge 0 \)" is false: at \( n = 40 \) we get \( 40^2 + 40 + 41 = 1681 = 41^2 \), which is not prime.
:::

## Mathematical induction

Some statements are really infinitely many statements, one for each natural number: "for every \( n \ge 1 \), \( 1 + 2 + \cdots + n = n(n+1)/2 \)". Checking cases one at a time never finishes. Induction replaces the infinite list of checks by two finite tasks, like knocking over a row of dominoes: push the first one, and make sure each domino knocks over the next.

We take this as a basic property of the integers, not something to prove.

::: {#thm-induction}
[Principle of Mathematical Induction]

Let \( n_0 \) be an integer, and for each integer \( n \ge n_0 \) let \( P(n) \) be a statement. Suppose

::: {.enumerate options="label=(\roman*)"}
1. (**base case**) \( P(n_0) \) is true, and
2. (**inductive step**) for **every** integer \( n \ge n_0 \), if \( P(n) \) is true then \( P(n + 1) \) is true.
:::

Then \( P(n) \) is true for every integer \( n \ge n_0 \).
:::

In the inductive step, the assumption "\( P(n) \) is true" is called the **induction hypothesis**. It is not circular: we do not assume the whole conclusion, only that the statement holds at one arbitrary \( n \), and we prove that it then holds at \( n + 1 \).

::: {#prp-sum-first-n}
[Sum of the first \( n \) integers]

For every integer \( n \ge 1 \),
\[
1 + 2 + \cdots + n = \frac{n(n+1)}{2}.
\]
:::

::: {.idea}
Passing from \( n \) to \( n + 1 \) adds exactly one term, \( n + 1 \), to the left side. So the step reduces to the algebra identity \( \frac{n(n+1)}{2} + (n + 1) = \frac{(n+1)(n+2)}{2} \), which holds after taking out the factor \( n + 1 \).
:::

::: {.proof}
We prove this by induction on \( n \), using @thm-induction with \( n_0 = 1 \). Let \( P(n) \) be the statement \( 1 + 2 + \cdots + n = n(n+1)/2 \).

*Base case.* For \( n = 1 \) the left side is \( 1 \) and the right side is \( 1 \cdot 2 / 2 = 1 \). So \( P(1) \) is true.

*Inductive step.* Let \( n \ge 1 \) and suppose \( P(n) \) is true. Then
\[
1 + 2 + \cdots + n + (n + 1) = \frac{n(n+1)}{2} + (n + 1) = (n + 1)\Bigl(\frac{n}{2} + 1\Bigr) = \frac{(n+1)(n+2)}{2},
\]
where the first equality uses the induction hypothesis \( P(n) \). This is \( P(n + 1) \).

By @thm-induction, \( P(n) \) is true for every integer \( n \ge 1 \), as claimed.
:::

The base case does not have to be \( 1 \), and the step does not have to be an equation. In this book the **natural numbers** are \( \nN = \{0, 1, 2, \dots\} \): they **include** \( 0 \). (Some books start at \( 1 \); the next section fixes our convention formally.)

::: {#prp-power-of-two}
[\( 2^n > n \)]

For every natural number \( n \), we have \( 2^n > n \).
:::

::: {.proof}
We prove this by induction on \( n \), with \( n_0 = 0 \). For \( n = 0 \), \( 2^0 = 1 > 0 \). Now let \( n \ge 0 \) and suppose \( 2^n > n \). Then
\[
2^{n+1} = 2^n + 2^n > n + 2^n \ge n + 1,
\]
where the strict inequality uses the induction hypothesis and the last step uses \( 2^n \ge 1 \). Hence \( 2^{n+1} > n + 1 \). By @thm-induction, \( 2^n > n \) for every \( n \in \nN \).
:::

The inductive step must work for **every** \( n \ge n_0 \), including the smallest ones. The following fake proof fails exactly there.

::: {.warning}
**The "all horses are the same color" fallacy.** *Claim:* in every group of \( n \ge 1 \) horses, all horses have the same color. *"Proof":* for \( n = 1 \) there is nothing to show. Suppose the claim holds for groups of \( n \) horses, and take a group of \( n + 1 \) horses \( h_1, \dots, h_{n+1} \). The group \( h_1, \dots, h_n \) is single-colored by the induction hypothesis, and so is \( h_2, \dots, h_{n+1} \). The two groups share a horse, so all \( n + 1 \) horses have its color. The claim is plainly false, so this "proof" has a gap. Before opening the check below, try to find the exact value of \( n \) where the step breaks.
:::

:::: {.check}
Where does the inductive step in the horse argument fail?

::: {.solution}
It fails when passing from \( n = 1 \) to \( n + 1 = 2 \). The two groups are then \( \{h_1\} \) and \( \{h_2\} \), which share **no** horse, so nothing links the color of \( h_1 \) to that of \( h_2 \). The sentence "the two groups share a horse" is true only when \( n \ge 2 \). Since the step \( P(1) \Rightarrow P(2) \) is not proved, the chain of dominoes breaks at the very first push, and the base case alone gives nothing.
:::
::::

## Strong induction and well-ordering

In some arguments, knowing \( P(n) \) alone is not enough to reach \( P(n+1) \): we need the statement at some **earlier** value, and we do not know in advance which one. Strong induction allows the hypothesis at all earlier values at once.

::: {#thm-strong-induction}
[Strong induction]

Let \( n_0 \) be an integer, and for each integer \( n \ge n_0 \) let \( P(n) \) be a statement. Suppose that for **every** integer \( n \ge n_0 \),
\[
\text{if } P(k) \text{ is true for all integers } k \text{ with } n_0 \le k < n, \text{ then } P(n) \text{ is true.}
\]
Then \( P(n) \) is true for every integer \( n \ge n_0 \).
:::

::: {.idea}
Ordinary induction applies to the stronger statement \( Q(n) \): "\( P(k) \) holds for all \( k \) from \( n_0 \) to \( n \)". The hypothesis is exactly what pushes \( Q(n) \) to \( Q(n+1) \). At \( n = n_0 \) the condition "for all \( k \) with \( n_0 \le k < n_0 \)" is vacuous, so the hypothesis already contains the base case.
:::

::: {.proof}
For each integer \( n \ge n_0 \), let \( Q(n) \) be the statement "\( P(k) \) is true for all integers \( k \) with \( n_0 \le k \le n \)". We prove \( Q(n) \) for all \( n \ge n_0 \) by @thm-induction.

*Base case.* There is no integer \( k \) with \( n_0 \le k < n_0 \), so the condition "\( P(k) \) is true for all such \( k \)" is vacuously true. By the hypothesis with \( n = n_0 \), \( P(n_0) \) is true. Hence \( Q(n_0) \) is true.

*Inductive step.* Let \( n \ge n_0 \) and suppose \( Q(n) \) is true, so \( P(k) \) holds for all \( k \) with \( n_0 \le k < n + 1 \). By the hypothesis applied to \( n + 1 \), \( P(n + 1) \) is true. Together with \( Q(n) \), this gives \( Q(n + 1) \).

By @thm-induction, \( Q(n) \) holds for all \( n \ge n_0 \). In particular \( P(n) \) holds for all \( n \ge n_0 \), since \( Q(n) \) includes \( k = n \). This proves the theorem.
:::

The same property of the natural numbers can be phrased without any statements \( P(n) \) at all: there is no endless strictly decreasing sequence of natural numbers, so every search for a smallest example ends.

::: {#thm-well-ordering}
[Well-Ordering Principle]

Every non-empty collection of natural numbers has a least element: an element \( m \) of the collection with \( m \le s \) for every \( s \) in the collection.
:::

We take this as a basic property too. It is equivalent to the Principle of Mathematical Induction, in the sense that each can be proved from the other, but we will not need that. Well-ordering is the natural language for "take a smallest counterexample" arguments, which are contradiction proofs in disguise.

Here is a result that needs strong induction, because the smaller number we reach is not \( n - 1 \).

::: {#prp-prime-factor}
[Existence of a prime factor]

Every integer \( n \ge 2 \) has a prime divisor.
:::

::: {.idea}
If \( n \) is prime, \( n \) itself works. If not, \( n = ab \) with \( 1 < a < n \), and a prime dividing \( a \) also divides \( n \). The factor \( a \) can be any size below \( n \), so we need the statement for all smaller values, which is strong induction.
:::

::: {.proof}
We use @thm-strong-induction with \( n_0 = 2 \). Let \( n \ge 2 \), and suppose every integer \( k \) with \( 2 \le k < n \) has a prime divisor.

*Case 1: \( n \) is prime.* Then \( n \mid n \), so \( n \) is a prime divisor of \( n \).

*Case 2: \( n \) is not prime.* Since \( n \ge 2 \), @def-divisibility-prime gives a positive divisor \( a \) of \( n \) with \( a \ne 1 \) and \( a \ne n \). Write \( n = ab \) with \( b \) an integer. Since \( a \) and \( n \) are positive, \( b \ge 1 \), and \( b \ne 1 \) because \( a \ne n \); so \( b \ge 2 \) and \( a = n/b < n \). Thus \( 2 \le a < n \), and by the hypothesis \( a \) has a prime divisor \( p \), say \( a = pc \). Then \( n = p(cb) \), so \( p \mid n \).

In both cases \( n \) has a prime divisor. By @thm-strong-induction, this holds for every \( n \ge 2 \).
:::

Now the promised contradiction proof.

::: {#thm-infinitely-many-primes}
[Infinitely many primes]

There are infinitely many prime numbers.
:::

::: {.idea}
Suppose the primes form a finite list. Build a number that no prime on the list can divide: multiply them all and add \( 1 \). Dividing by any \( p_i \) leaves remainder \( 1 \). But @prp-prime-factor says this number has some prime divisor, and that prime must be on the list.
:::

::: {.proof}
Suppose, for a contradiction, that there are only finitely many primes, and list them all as \( p_1, p_2, \dots, p_k \). Let
\[
N = p_1 p_2 \cdots p_k + 1.
\]
The list is non-empty, since \( 2 \) is prime, and each \( p_i \ge 2 \); hence \( N \ge 3 \). By @prp-prime-factor, \( N \) has a prime divisor \( p \). Since the list contains every prime, \( p = p_i \) for some \( i \). Then \( p_i \mid N \) and \( p_i \mid p_1 p_2 \cdots p_k \), so there are integers \( s, t \) with \( N = p_i s \) and \( p_1 \cdots p_k = p_i t \). Subtracting gives \( 1 = p_i(s - t) \). Since \( s - t \) is an integer and \( p_i \ge 2 \), this is impossible: \( p_i(s - t) \) is \( 0 \) when \( s = t \), and has absolute value at least \( 2 \) otherwise. This contradiction shows that there are infinitely many primes.
:::

::: {.remark}
Well-ordering also justifies the "lowest terms" fact used in @thm-sqrt2-irrational. Let \( x \) be rational. There is at least one way of writing \( x = a/b \) with \( b \ge 1 \): if \( x = a/b \) with \( b < 0 \), then also \( x = (-a)/(-b) \) with \( -b \ge 1 \). Among all such ways, the collection of possible denominators \( b \) is a non-empty collection of natural numbers, so by @thm-well-ordering it has a least element. Take a representation \( a/b \) with that least \( b \). If some \( d \ge 2 \) divided both, say \( a = da' \) and \( b = db' \), then \( x = a'/b' \) with \( 1 \le b' < b \), contradicting minimality. So \( a/b \) is in lowest terms.
:::

## Writing proofs in this book

The proofs in this book follow a few conventions. Knowing them makes proofs faster to read, and copying them makes your own proofs easier to check.

- **The first sentence does mathematics.** Proofs open with "Let …", "Suppose …", "Since …" or "By …". The motivation has already been given in the Idea block.
- **Every step names its reason.** Each line cites a hypothesis, a definition, or an earlier result by name, as in "by @prp-square-even". When a display hides a reason, a clause such as "where the first equality uses the induction hypothesis" points to it.
- **Structure is marked.** Two directions of an iff are labeled \( (\Rightarrow) \) and \( (\Leftarrow) \), cases are labeled *Case 1* and *Case 2*, and inductions name their base case and inductive step.
- **No hidden gaps.** Words like "obviously" and "clearly" never stand in for an argument. If a step is short, it is written out; if it is routine and has been done before, the proof says so.
- **The ending restates the result**: "This shows …", "This proves …", "as claimed".

**How to read a proof here.** First read the statement and identify the givens and the goal. Then read the Idea, which says why the argument has the shape it has. Then read the Proof with a pencil. At each line, ask which earlier line or result justifies it; if you cannot answer, that is the line to reread. Finally, ask which hypothesis each step used. If a hypothesis was never used, either it was not needed or you have missed a step.

## Exercises

### A. Check your understanding

::: {#exr-proofs-a1}
[A1]

For each statement, name the proof technique you would use first (direct, contrapositive, contradiction, cases, induction, or counterexample), and give a one-sentence reason. Then carry out the proof or refutation.

::: {.enumerate options="label=(\alph*)"}
1. The sum of two odd integers is even.
2. For every integer \( n \), if \( 3n + 2 \) is odd, then \( n \) is odd.
3. For every integer \( n \ge 1 \), \( 3 \mid 4^n - 1 \).
4. For every integer \( n \ge 1 \), \( n^2 \ge 2n \).
5. There is no largest integer.
:::
:::

::: {.solution}
(a) *Direct.* The hypothesis gives formulas to add. Let \( m = 2a + 1 \) and \( n = 2b + 1 \) with \( a, b \) integers, by @def-parity. Then \( m + n = 2(a + b + 1) \), which is even.

(b) *Contrapositive.* The conclusion's negation "\( n \) even" gives a formula, while "\( 3n + 2 \) odd" does not. By @thm-contrapositive-equivalent it suffices to show: if \( n \) is even then \( 3n + 2 \) is even. If \( n = 2k \), then \( 3n + 2 = 2(3k + 1) \), which is even, hence not odd.

(c) *Induction.* It is a statement for every \( n \ge 1 \), and \( 4^{n+1} - 1 \) is built from \( 4^n - 1 \). For \( n = 1 \), \( 4 - 1 = 3 = 3 \cdot 1 \). If \( 4^n - 1 = 3k \), then \( 4^{n+1} - 1 = 4(4^n - 1) + 3 = 3(4k + 1) \). By @thm-induction the claim holds for all \( n \ge 1 \).

(d) *Counterexample.* The statement is false, so a single witness refutes it. At \( n = 1 \), \( n^2 = 1 < 2 = 2n \).

(e) *Contradiction.* It says an object does not exist, so assume it does. Suppose \( m \) is a largest integer. Then \( m + 1 \) is an integer with \( m + 1 > m \), contradicting the choice of \( m \). Hence there is no largest integer.
:::

### B. Practice

::: {#exr-proofs-b1}
[B1: Contrapositive]

Prove that for every integer \( n \), if \( n^2 \) is odd, then \( n \) is odd.
:::

::: {.solution}
Let \( n \) be an integer. By @thm-contrapositive-equivalent, it suffices to prove that if \( n \) is not odd, then \( n^2 \) is not odd. Suppose \( n \) is not odd. Since every integer is even or odd, \( n \) is even, so \( n = 2k \) for some integer \( k \) by @def-parity. Then \( n^2 = 4k^2 = 2(2k^2) \), so \( n^2 \) is even. Since no integer is both even and odd, \( n^2 \) is not odd. This proves the statement.
:::

::: {#exr-proofs-b2}
[B2: Induction]

Prove that for every integer \( n \ge 1 \), the sum of the first \( n \) odd numbers is \( n^2 \):
\[
1 + 3 + 5 + \cdots + (2n - 1) = n^2.
\]
:::

::: {.solution}
We prove this by induction on \( n \), using @thm-induction with \( n_0 = 1 \). Let \( P(n) \) be the displayed statement.

*Base case.* For \( n = 1 \) the left side is \( 1 \) and the right side is \( 1^2 = 1 \), so \( P(1) \) is true.

*Inductive step.* Let \( n \ge 1 \) and suppose \( P(n) \) is true. The \( (n+1) \)-st odd number is \( 2(n + 1) - 1 = 2n + 1 \). Then
\[
1 + 3 + \cdots + (2n - 1) + (2n + 1) = n^2 + 2n + 1 = (n + 1)^2,
\]
where the first equality uses the induction hypothesis. This is \( P(n + 1) \).

By @thm-induction, \( P(n) \) holds for every \( n \ge 1 \).
:::

::: {#exr-proofs-b3}
[B3: \( \sqrt{3} \) is irrational]

You may use the school fact that every integer has exactly one of the forms \( 3k \), \( 3k + 1 \), \( 3k + 2 \) with \( k \) an integer.

::: {.enumerate options="label=(\alph*)"}
1. Prove that for every integer \( n \), if \( 3 \mid n^2 \) then \( 3 \mid n \).
2. Hence prove that there is no rational number whose square is \( 3 \).
:::
:::

::: {.solution}
(a) Let \( n \) be an integer. By @thm-contrapositive-equivalent, it suffices to show that if \( 3 \nmid n \) then \( 3 \nmid n^2 \). Suppose \( 3 \nmid n \). Then \( n = 3k + 1 \) or \( n = 3k + 2 \) for some integer \( k \).

*Case 1: \( n = 3k + 1 \).* Then \( n^2 = 9k^2 + 6k + 1 = 3(3k^2 + 2k) + 1 \).

*Case 2: \( n = 3k + 2 \).* Then \( n^2 = 9k^2 + 12k + 4 = 3(3k^2 + 4k + 1) + 1 \).

In both cases \( n^2 \) has the form \( 3j + 1 \) with \( j \) an integer. Since an integer has only one of the three forms, \( n^2 \) is not of the form \( 3j \), so \( 3 \nmid n^2 \). This proves (a).

(b) Suppose, for a contradiction, that a rational number \( x \) satisfies \( x^2 = 3 \). Write \( x = a/b \) in lowest terms, so \( b \ge 1 \) and no integer \( d \ge 2 \) divides both \( a \) and \( b \). Multiplying \( a^2/b^2 = 3 \) by \( b^2 \ne 0 \) gives \( a^2 = 3b^2 \). Therefore \( 3 \mid a^2 \), and by (a), \( 3 \mid a \). Write \( a = 3c \). Then \( 9c^2 = 3b^2 \), so \( b^2 = 3c^2 \) and \( 3 \mid b^2 \). By (a) again, \( 3 \mid b \). Thus \( 3 \) divides both \( a \) and \( b \), contradicting lowest terms. Hence no rational number has square \( 3 \).
:::

### C. Going deeper

::: {#exr-proofs-c1}
[C1: Stamps of 4 and 5]

::: {.enumerate options="label=(\alph*)"}
1. Show that each of \( 12, 13, 14, 15 \) can be written as \( 4a + 5b \) with \( a, b \in \nN \).
2. Prove by strong induction that every integer \( n \ge 12 \) can be written as \( 4a + 5b \) with \( a, b \in \nN \).
3. Show that \( 11 \) cannot be written in this form, so the bound \( 12 \) in (b) cannot be lowered to \( 11 \).
:::

*Hint: for \( n \ge 16 \), look at \( n - 4 \).*
:::

::: {.solution}
(a) \( 12 = 4 \cdot 3 + 5 \cdot 0 \), \( 13 = 4 \cdot 2 + 5 \cdot 1 \), \( 14 = 4 \cdot 1 + 5 \cdot 2 \), and \( 15 = 4 \cdot 0 + 5 \cdot 3 \).

(b) We use @thm-strong-induction with \( n_0 = 12 \). Let \( n \ge 12 \), and suppose every integer \( k \) with \( 12 \le k < n \) can be written as \( 4a + 5b \) with \( a, b \in \nN \).

*Case 1: \( 12 \le n \le 15 \).* Then \( n \) has the required form by (a).

*Case 2: \( n \ge 16 \).* Then \( k = n - 4 \) satisfies \( 12 \le k < n \), so by the hypothesis \( n - 4 = 4a + 5b \) with \( a, b \in \nN \). Hence \( n = 4(a + 1) + 5b \), and \( a + 1 \in \nN \).

In both cases \( n \) has the required form. By @thm-strong-induction, every integer \( n \ge 12 \) does.

(c) Suppose \( 11 = 4a + 5b \) with \( a, b \in \nN \). Since \( 5b \le 11 \), \( b \in \{0, 1, 2\} \). If \( b = 0 \) then \( 4a = 11 \); if \( b = 1 \) then \( 4a = 6 \); if \( b = 2 \) then \( 4a = 1 \). None of \( 11, 6, 1 \) is a multiple of \( 4 \), so no such \( a \) exists. Hence \( 11 \) is not of the form \( 4a + 5b \).
:::

::: {#exr-proofs-c2}
[C2: Division with remainder]

Let \( a \) and \( b \) be integers with \( b \ge 1 \). Let \( R \) be the collection of all **non-negative** integers of the form \( a - qb \) with \( q \) an integer.

::: {.enumerate options="label=(\alph*)"}
1. Show that \( R \) is non-empty.
2. Let \( r \) be the least element of \( R \), which exists by @thm-well-ordering, and write \( r = a - qb \). Prove that \( 0 \le r < b \).
3. Prove that the pair \( (q, r) \) is unique: if \( a = qb + r = q'b + r' \) with \( 0 \le r < b \) and \( 0 \le r' < b \), then \( q = q' \) and \( r = r' \).
:::

*Hint for (a): try \( q = -\lvert a \rvert \).*
:::

::: {.solution}
(a) Take \( q = -\lvert a \rvert \). Then \( a - qb = a + \lvert a \rvert b \). Since \( b \ge 1 \) and \( \lvert a \rvert \ge 0 \), we have \( \lvert a \rvert b \ge \lvert a \rvert \), so \( a + \lvert a \rvert b \ge a + \lvert a \rvert \ge 0 \), where the last step uses \( \lvert a \rvert \ge -a \). Hence \( a + \lvert a \rvert b \) belongs to \( R \), and \( R \) is non-empty.

(b) By (a) and @thm-well-ordering, \( R \) has a least element \( r = a - qb \) with \( q \in \nZ \). Since \( r \) belongs to \( R \), \( r \ge 0 \). Suppose, for a contradiction, that \( r \ge b \). Then \( r - b = a - (q + 1)b \ge 0 \), and \( q + 1 \in \nZ \), so \( r - b \) belongs to \( R \). But \( b \ge 1 \) gives \( r - b < r \), contradicting the choice of \( r \) as the least element of \( R \). Hence \( 0 \le r < b \).

(c) Suppose \( qb + r = q'b + r' \) with \( 0 \le r, r' < b \). Then \( r' - r = (q - q')b \), so \( b \mid r' - r \). From the bounds, \( -b < r' - r < b \). Suppose \( q \ne q' \). Then \( \lvert q - q' \rvert \ge 1 \), so \( \lvert r' - r \rvert = \lvert q - q' \rvert\, b \ge b \), contradicting \( -b < r' - r < b \). Hence \( q = q' \), and then \( r' - r = 0 \), so \( r = r' \). This proves uniqueness.

Together, (a)–(c) show that for integers \( a \) and \( b \ge 1 \) there are unique integers \( q, r \) with \( a = qb + r \) and \( 0 \le r < b \). With \( b = 2 \), this is the fact that every integer is even or odd, and not both.
:::
