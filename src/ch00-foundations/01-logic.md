# Statements, Implications and Quantifiers

Linear algebra is a subject of proofs. Every theorem in this book has the shape "if these hypotheses hold, then this conclusion holds", and most definitions hide a "for every" or a "there exists". Before we can prove anything, we need to read such sentences exactly: when they are true, what they claim, and what their opposite says. This section builds that reading skill. It is the grammar that the rest of the book is written in.

## Statements and connectives

A **statement** is a sentence that is either true or false, but not both. "\( 7 \) is prime" is a statement, and it is true. "\( 2 + 2 = 5 \)" is a statement, and it is false. "Is \( 7 \) prime?" is not a statement, and neither is "\( x > 3 \)" on its own: its truth depends on \( x \), which nobody has chosen yet. Sentences with a free variable are handled by quantifiers later in this section.

We build longer statements from shorter ones with a few fixed words. Everyday language uses these words loosely, so mathematics pins each one down by saying exactly when the combined statement is true.

*A connective builds a new statement whose truth depends only on the truth of its parts.*

::: {#def-connectives}
[Negation, conjunction, disjunction]

Let \( P \) and \( Q \) be statements.

- The **negation** \( \neg P \) ("not \( P \)") is true when \( P \) is false, and false when \( P \) is true.
- The **conjunction** \( P \wedge Q \) ("\( P \) and \( Q \)") is true when **both** \( P \) and \( Q \) are true, and false otherwise.
- The **disjunction** \( P \vee Q \) ("\( P \) or \( Q \)") is true when **at least one** of \( P \), \( Q \) is true, and false only when both are false.
:::

A **truth table** lists every combination of truth values of the parts, one per row, and records the value of the compound statement. With T for true and F for false:

| \( P \) | \( Q \) | \( \neg P \) | \( P \wedge Q \) | \( P \vee Q \) |
|:-:|:-:|:-:|:-:|:-:|
| T | T | F | T | T |
| T | F | F | F | T |
| F | T | T | F | T |
| F | F | T | F | F |

Two statement forms are **logically equivalent**, written \( \equiv \), if they have the same truth value in every row of the truth table. For example, \( \neg(\neg P) \equiv P \): negating twice returns the original value in both rows.

A few examples, checked against the definition:

- "\( 7 \) is prime **and** \( 7 \) is even" is false, because its second part is false.
- "\( 7 \) is prime **or** \( 7 \) is even" is true, because its first part is true.
- "\( 2 < 3 \) **or** \( 3 < 4 \)" is true. Both parts are true, and that is allowed.

::: {.warning}
In mathematics "or" is **inclusive**: \( P \vee Q \) is true when both parts are true. The menu phrase "soup or salad", which forbids having both, is a different connective. So "\( 6 \) is even or \( 6 \) is divisible by \( 3 \)" is true, even though both halves hold.
:::

## Implication

Almost every theorem is an implication: "if \( P \), then \( Q \)". It is worth being completely precise about when such a sentence counts as true, because the answer surprises many readers in one row of the table.

Think of an implication as a **promise**. A parent says: "If you finish your homework, then you may watch a film." When has the parent broken the promise? Only when the homework is finished and the film is still refused. If the homework is not finished, the promise says nothing about what happens, so whatever happens, the promise was not broken.

*An implication is false only when the hypothesis holds and the conclusion fails.*

::: {#def-implication-converse-contrapositive}
[Implication, converse, contrapositive]

Let \( P \) and \( Q \) be statements.

- The **implication** \( P \Rightarrow Q \) ("if \( P \) then \( Q \)") is false when \( P \) is true and \( Q \) is false, and it is true in **every** other case. We call \( P \) the **hypothesis** and \( Q \) the **conclusion**.
- The **converse** of \( P \Rightarrow Q \) is the implication \( Q \Rightarrow P \).
- The **contrapositive** of \( P \Rightarrow Q \) is the implication \( \neg Q \Rightarrow \neg P \).
:::

In words: the first clause says an implication can only fail in one way, by a true hypothesis leading to a false conclusion. The converse swaps the roles of hypothesis and conclusion. The contrapositive swaps them **and** negates both.

| \( P \) | \( Q \) | \( P \Rightarrow Q \) |
|:-:|:-:|:-:|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

The implication \( P \Rightarrow Q \) is read in many ways, and all of them mean the same thing:

- "\( P \) implies \( Q \)", "\( Q \) whenever \( P \)", "\( Q \) if \( P \)";
- "\( P \) only if \( Q \)";
- "\( P \) is **sufficient** for \( Q \)", "\( Q \) is **necessary** for \( P \)".

The phrase "only if" trips people up. "\( P \) only if \( Q \)" says that \( P \) cannot happen without \( Q \), which is exactly \( P \Rightarrow Q \).

The last two rows of the table, where the hypothesis is false, are called **vacuous** cases. An implication with a false hypothesis is **vacuously true**.

::: {#exm-vacuous-truth}
[A vacuously true implication]

Let \( n \) be an integer. Is the statement "if \( n \) is odd and \( n \) is even, then \( n = 7 \)" true?
:::

::: {.solution}
Yes. No integer is both odd and even, so the hypothesis "\( n \) is odd and \( n \) is even" is false for every integer \( n \). By @def-implication-converse-contrapositive, an implication with a false hypothesis is true, whatever the conclusion says. So the statement is true for every integer \( n \), including \( n = 7 \) and \( n = 0 \). It is true, but it tells us nothing.
:::

**Why this definition.** The two vacuous rows may look like a convention picked for convenience. They are forced once we want implications to work inside "for every" statements. Consider the true fact

> for every integer \( n \), if \( n > 2 \) then \( n^2 > 4 \).

For this to be true, the implication must be true for **every** integer \( n \). Try \( n = -3 \): the hypothesis \( -3 > 2 \) is false, and the conclusion \( 9 > 4 \) is true. Try \( n = 1 \): the hypothesis \( 1 > 2 \) is false, and the conclusion \( 1 > 4 \) is false. If either row were declared false, this perfectly good theorem would become false. So both vacuous rows must be T. In the same way, a theorem with hypotheses says nothing about objects that fail them, and that is exactly how we want to read it.

::: {.remark}
The implication \( P \Rightarrow Q \) does **not** claim that \( P \) causes \( Q \), or that the two are related at all. "If \( 2 + 2 = 4 \), then \( 7 \) is prime" is a true implication, because both parts are true. In practice we only ever prove implications where the hypothesis is used, but the truth value does not depend on that.
:::

The contrapositive is the most useful rewriting of an implication, because it is always interchangeable with the original.

::: {#thm-contrapositive-equivalent}
[Contrapositive equivalence]

For all statements \( P \) and \( Q \), the implication \( P \Rightarrow Q \) is logically equivalent to its contrapositive \( \neg Q \Rightarrow \neg P \).
:::

::: {.proof}
Let \( P \) and \( Q \) be statements. We compute both sides in each of the four rows, using @def-connectives for the negations and @def-implication-converse-contrapositive for the implications.

| \( P \) | \( Q \) | \( \neg Q \) | \( \neg P \) | \( P \Rightarrow Q \) | \( \neg Q \Rightarrow \neg P \) |
|:-:|:-:|:-:|:-:|:-:|:-:|
| T | T | F | F | T | T |
| T | F | T | F | F | F |
| F | T | F | T | T | T |
| F | F | T | T | T | T |

In the second row, \( \neg Q \) is true and \( \neg P \) is false, so \( \neg Q \Rightarrow \neg P \) is false. In every other row the hypothesis \( \neg Q \) is false or the conclusion \( \neg P \) is true, so the contrapositive is true. The last two columns agree in every row. This proves that the two statements are logically equivalent.
:::

So to prove "if \( P \) then \( Q \)" we may instead prove "if \( Q \) fails then \( P \) fails". The next section turns this into a proof technique.

The converse is a different matter. It is a separate statement, and it can be false while the original is true.

::: {.warning}
**The converse is not the contrapositive.** "If \( x = 2 \), then \( x^2 = 4 \)" is true for every real number \( x \). Its converse "if \( x^2 = 4 \), then \( x = 2 \)" is false: \( x = -2 \) satisfies the hypothesis and fails the conclusion. Proving \( P \Rightarrow Q \) never proves \( Q \Rightarrow P \).
:::

Later in the book the converse question comes up constantly. In Chapter 2 we will see that if a square matrix \( \A \) is invertible, then \( \A\x = \0 \) has only the solution \( \x = \0 \). The converse, "if \( \A\x = \0 \) has only the solution \( \x = \0 \), then \( \A \) is invertible", also turns out to be true for square matrices. But it is a separate theorem, it needs its own proof, and that proof takes real work.

::: {.check}
Consider "if an integer \( n \) is divisible by \( 6 \), then \( n \) is even". Write its converse and its contrapositive, and decide which of the three statements are true for every integer \( n \).
:::

::: {.solution}
The converse is "if \( n \) is even, then \( n \) is divisible by \( 6 \)". The contrapositive is "if \( n \) is not even, then \( n \) is not divisible by \( 6 \)", that is, "if \( n \) is odd, then \( 6 \nmid n \)".

The original is true: if \( n = 6k \) then \( n = 2(3k) \) is even. The contrapositive is true, by @thm-contrapositive-equivalent. The converse is false: \( n = 2 \) is even but not divisible by \( 6 \).
:::

When an implication and its converse are both true, we say the two statements are equivalent.

The **biconditional** \( P \Leftrightarrow Q \) ("\( P \) if and only if \( Q \)", often written "\( P \) iff \( Q \)") is the statement \( (P \Rightarrow Q) \wedge (Q \Rightarrow P) \). It is true exactly when \( P \) and \( Q \) have the same truth value:

| \( P \) | \( Q \) | \( P \Rightarrow Q \) | \( Q \Rightarrow P \) | \( P \Leftrightarrow Q \) |
|:-:|:-:|:-:|:-:|:-:|
| T | T | T | T | T |
| T | F | F | T | F |
| F | T | T | F | F |
| F | F | T | T | T |

The phrase splits in two: "\( P \) if \( Q \)" is \( Q \Rightarrow P \), and "\( P \) only if \( Q \)" is \( P \Rightarrow Q \). Other phrasings are "\( P \) is necessary and sufficient for \( Q \)" and "\( P \) and \( Q \) are equivalent". Proving an "iff" therefore always means proving two implications.

## Quantifiers

The sentence "\( x^2 \ge 0 \)" is not yet a statement, because \( x \) is not specified. A sentence \( P(x) \) that becomes a statement once a value of \( x \) is substituted is called a **predicate** (or open sentence) in the variable \( x \). There are two standard ways to turn a predicate into a statement: claim it for every value, or claim it for at least one.

*"For every" makes a claim about each element; "there exists" asks for a single witness.*

::: {#def-quantifiers}
[Quantifiers]

Let \( P(x) \) be a predicate whose variable \( x \) ranges over a fixed collection \( S \).

- The **universal** statement \( \forall x \in S : P(x) \) ("for every \( x \) in \( S \), \( P(x) \)") is true when \( P(x) \) is true for **every** element \( x \) of \( S \), and false otherwise.
- The **existential** statement \( \exists x \in S : P(x) \) ("there exists \( x \) in \( S \) such that \( P(x) \)") is true when \( P(x) \) is true for **at least one** element \( x \) of \( S \), and false otherwise.

The symbols \( \forall \) and \( \exists \) are the **universal** and **existential quantifiers**.
:::

In words: a universal statement is a promise about every element, so a single element where \( P \) fails makes it false. An existential statement needs one element that works. It does not say which one, and it does not say there is only one.

The collection \( S \) is part of the statement. Changing \( S \) can change the truth value, so always ask: *ranging over what?*

::: {#exm-quantifiers}
[Quantified statements]

Decide whether each statement is true.

::: {.enumerate options="label=(\alph*)"}
1. \( \forall x \in \nR : x^2 \ge 0 \).
2. \( \exists x \in \nR : x^2 = -1 \).
3. \( \exists n \in \nZ : n^2 = 2 \).
4. \( \forall n \in \nZ : n^2 \ne 2 \).
:::
:::

::: {.solution}
(a) True. Every real number \( x \) is either \( \ge 0 \) or \( < 0 \), and in both cases \( x^2 = x \cdot x \ge 0 \).

(b) False. By (a), \( x^2 \ge 0 > -1 \) for every real \( x \), so no real \( x \) is a witness. Over the complex numbers (introduced later in this chapter), \( x = i \) is a witness, so the same predicate becomes true when the range changes from \( \nR \) to \( \nC \).

(c) False. If \( \lvert n \rvert \le 1 \) then \( n^2 \le 1 < 2 \), and if \( \lvert n \rvert \ge 2 \) then \( n^2 \ge 4 > 2 \). So no integer squares to \( 2 \).

(d) True. This is the statement shown in (c), said the other way round: every integer fails to square to \( 2 \).
:::

Parts (c) and (d) already show the pattern of the next subsection: "there is no witness" is the same as "everything fails".

**A degenerate case.** What if the range contains no elements at all? Take "every integer \( n \) with \( n^2 < 0 \) satisfies \( n = 7 \)". There are no such integers, so there is nothing that could fail, and the statement is true. It is the quantifier version of vacuous truth: it reads \( \forall n \in \nZ : (n^2 < 0 \Rightarrow n = 7) \), and every instance has a false hypothesis. By contrast, "there exists an integer \( n \) with \( n^2 < 0 \)" is false, because there is no witness. This case matters later: facts about "every element of an empty list" will be vacuously true, and that is what makes certain edge cases of definitions work.

::: {.remark}
We write \( \exists!\, x \in S : P(x) \) for "there exists a **unique** \( x \) in \( S \) with \( P(x) \)". It means two things: some \( x \) satisfies \( P \), and any two elements satisfying \( P \) are equal. The next section shows how each half is proved.
:::

## The order of quantifiers

Most definitions in this book use several quantifiers in a row. Their order is part of the meaning.

::: {#exm-nested-quantifiers}
[Swapping two quantifiers]

Compare the two statements

\[
\text{(i)}\ \ \forall x \in \nR \ \exists y \in \nR : y > x, \qquad \text{(ii)}\ \ \exists y \in \nR \ \forall x \in \nR : y > x.
\]

Decide which is true.
:::

::: {.solution}
Statement (i) says: whichever real \( x \) you are given, you can find a real \( y \) larger than it. This is true. Given \( x \), take \( y = x + 1 \), and then \( y > x \).

Statement (ii) says: there is one real number \( y \) that is larger than every real \( x \). This is false. Whatever \( y \) is proposed, the choice \( x = y + 1 \) gives \( y > x \) false. So no \( y \) is a witness.
:::

The difference is **who chooses first**. In (i), \( x \) is chosen first and \( y \) may depend on it: \( y = x + 1 \) changes with \( x \). In (ii), \( y \) must be fixed before \( x \) is known, so it has to work for all \( x \) at once. Reading quantifiers as a game helps: \( \forall \) is a move by an opponent, \( \exists \) is your reply, and you may only use information already on the table.

::: {.warning}
Never swap a \( \forall \) and an \( \exists \) without a proof. The implication "\( \exists y \, \forall x \Rightarrow \forall x \, \exists y \)" is always valid, since the single \( y \) works for each \( x \). The reverse direction fails, as @exm-nested-quantifiers shows. Two quantifiers of the **same** kind, such as \( \forall x \, \forall y \), may be swapped freely.
:::

::: {.check}
Over the positive real numbers, statement (A) is "\( \forall \varepsilon > 0 \ \exists \delta > 0 : \delta < \varepsilon \)". Statement (B) is obtained by swapping the quantifiers: "\( \exists \delta > 0 \ \forall \varepsilon > 0 : \delta < \varepsilon \)". Are (A) and (B) both true?
:::

::: {.solution}
No. (A) is true: given \( \varepsilon > 0 \), take \( \delta = \varepsilon / 2 \), which is positive and smaller than \( \varepsilon \). (B) is false: whatever \( \delta > 0 \) is proposed, the choice \( \varepsilon = \delta \) makes \( \delta < \varepsilon \) false. In (A) the number \( \delta \) may depend on \( \varepsilon \); in (B) it may not.
:::

## Negation

Much of mathematics consists of showing that something **fails**: a function is not injective, a list is not independent, a claimed theorem is false. To do this we need the negation of the statement written in a usable form. Putting "it is not the case that" in front is correct but useless; we want the negation with the "not" pushed all the way inside, next to a simple condition we can check.

First, the connectives.

::: {#thm-de-morgan-logic}
[De Morgan's laws for statements]

For all statements \( P \) and \( Q \):

::: {.enumerate options="label=(\alph*)"}
1. \( \neg(P \wedge Q) \equiv \neg P \vee \neg Q \);
2. \( \neg(P \vee Q) \equiv \neg P \wedge \neg Q \);
3. \( \neg(P \Rightarrow Q) \equiv P \wedge \neg Q \).
:::
:::

::: {.proof}
Let \( P \) and \( Q \) be statements. We compare truth tables, using @def-connectives and @def-implication-converse-contrapositive.

| \( P \) | \( Q \) | \( \neg(P \wedge Q) \) | \( \neg P \vee \neg Q \) | \( \neg(P \vee Q) \) | \( \neg P \wedge \neg Q \) | \( \neg(P \Rightarrow Q) \) | \( P \wedge \neg Q \) |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| T | T | F | F | F | F | F | F |
| T | F | T | T | F | F | T | T |
| F | T | T | T | F | F | F | F |
| F | F | T | T | T | T | F | F |

For (a), \( P \wedge Q \) is true only in the first row, so its negation is false only there. The statement \( \neg P \vee \neg Q \) is false only when \( \neg P \) and \( \neg Q \) are both false, which is again only the first row. For (b), \( \neg(P \vee Q) \) is true only in the last row, where both parts are false, and so is \( \neg P \wedge \neg Q \). For (c), \( P \Rightarrow Q \) is false only in the second row, so \( \neg(P \Rightarrow Q) \) is true only there, and \( P \wedge \neg Q \) is also true only there. In each case the two columns agree in all four rows, as claimed.
:::

Law (c) deserves a sentence. The negation of an implication is **not** another implication. To refute "if \( P \) then \( Q \)", you must exhibit a situation where \( P \) holds **and** \( Q \) fails.

Now the quantifiers. A universal statement fails exactly when some element fails it, and an existential statement fails exactly when every element fails it. We record this as the rule we will use every time.

*To negate, flip each quantifier and negate what is inside.*

::: {#def-negation-of-quantifiers}
[Negation of quantifiers]

Let \( P(x) \) be a predicate with \( x \) ranging over \( S \). Then

\[
\neg\bigl(\forall x \in S : P(x)\bigr) \ \equiv\ \exists x \in S : \neg P(x),
\qquad
\neg\bigl(\exists x \in S : P(x)\bigr) \ \equiv\ \forall x \in S : \neg P(x).
\]

For a statement with several quantifiers, apply these rules from the outside in: each \( \forall \) becomes \( \exists \), each \( \exists \) becomes \( \forall \), the ranges stay the same, and the innermost condition is negated using @thm-de-morgan-logic.
:::

In words: "not every \( x \) works" means "some \( x \) fails", and "no \( x \) works" means "every \( x \) fails". Both rules are just @def-quantifiers read carefully. The universal statement is false precisely when it is not the case that every element satisfies \( P \), which is precisely when at least one element satisfies \( \neg P \). The **ranges do not change**: the negation of "every real number squared is non-negative" talks about real numbers, not about some other collection.

::: {#exm-negation-basic}
[Negating simple quantified statements]

Negate each statement, and say which of the statement and its negation is true.

::: {.enumerate options="label=(\alph*)"}
1. \( \forall x \in \nR : x^2 \ge 0 \).
2. \( \exists n \in \nZ : n \text{ is even and } n > 10 \).
3. \( \forall x \in \nR \ \exists y \in \nR : y > x \).
:::
:::

::: {.solution}
(a) The negation is \( \exists x \in \nR : x^2 < 0 \). The original is true, by @exm-quantifiers, so the negation is false.

(b) By @def-negation-of-quantifiers and law (a) of @thm-de-morgan-logic, the negation is \( \forall n \in \nZ : n \text{ is odd or } n \le 10 \). The original is true, with witness \( n = 12 \), so the negation is false: \( n = 12 \) is neither odd nor \( \le 10 \).

(c) Flip both quantifiers and negate the inside: \( \exists x \in \nR \ \forall y \in \nR : y \le x \). This says that some real number is at least as large as every real number. The original is true by @exm-nested-quantifiers, so the negation is false.
:::

The next two examples negate definitions that will appear over and over. We use the word **function** informally here, as a rule \( f \) that assigns to each \( a \) in a collection \( A \) one value \( f(a) \) in a collection \( B \); functions are treated properly later in this chapter.

::: {#exm-negation-injectivity}
[What "not injective" means]

A function \( f \) from \( A \) to \( B \) is called **injective** if

\[
\forall a_1 \in A \ \forall a_2 \in A : \bigl( f(a_1) = f(a_2) \Rightarrow a_1 = a_2 \bigr).
\]

Write down, with no "not" in front, what it means for \( f \) to be **not** injective. Then show that \( f(x) = x^2 \), from \( \nR \) to \( \nR \), is not injective.
:::

::: {.solution}
By @def-negation-of-quantifiers, both \( \forall \) become \( \exists \), and the inside implication is negated. By law (c) of @thm-de-morgan-logic, \( \neg\bigl(f(a_1) = f(a_2) \Rightarrow a_1 = a_2\bigr) \equiv f(a_1) = f(a_2) \wedge a_1 \ne a_2 \). So \( f \) is not injective if and only if

\[
\exists a_1 \in A \ \exists a_2 \in A : f(a_1) = f(a_2) \text{ and } a_1 \ne a_2.
\]

In words, two **different** inputs have the same output. For \( f(x) = x^2 \), take \( a_1 = 1 \) and \( a_2 = -1 \). Then \( f(1) = 1 = f(-1) \) and \( 1 \ne -1 \), so \( f \) is not injective.
:::

::: {#exm-negation-surjectivity}
[What "not surjective" means]

A function \( f \) from \( A \) to \( B \) is called **surjective** if

\[
\forall b \in B \ \exists a \in A : f(a) = b.
\]

Negate this, and show that \( f(x) = x^2 \), from \( \nR \) to \( \nR \), is not surjective.
:::

::: {.solution}
Flipping the two quantifiers and negating the equation gives: \( f \) is not surjective if and only if

\[
\exists b \in B \ \forall a \in A : f(a) \ne b.
\]

In words, **one** value in \( B \) is never reached. For \( f(x) = x^2 \), take \( b = -1 \). For every real \( a \) we have \( f(a) = a^2 \ge 0 > -1 \) by @exm-quantifiers, so \( f(a) \ne -1 \). Hence \( f \) is not surjective.
:::

The most important negation in the early chapters is that of a statement ending in "all zero". We meet it here without any vector spaces, using pairs of real numbers added and scaled entry by entry.

::: {#exm-negation-not-all-zero}
[Negating "only the zero combination"]

Consider the pairs \( (1, 2) \), \( (2, 4) \), \( (0, 1) \), and the statement

\[
\forall a, b, c \in \nR : \Bigl( a(1, 2) + b(2, 4) + c(0, 1) = (0, 0) \ \Rightarrow\ a = 0 \wedge b = 0 \wedge c = 0 \Bigr).
\]

Negate it, and decide which of the statement and its negation is true.
:::

::: {.solution}
Flip the quantifier, and use law (c) of @thm-de-morgan-logic for the implication and law (a) for the conjunction. The negation is

\[
\exists a, b, c \in \nR : a(1, 2) + b(2, 4) + c(0, 1) = (0, 0) \ \text{ and } \ \bigl(a \ne 0 \vee b \ne 0 \vee c \ne 0\bigr).
\]

The last condition says that \( a, b, c \) are **not all zero**: at least one of them is non-zero.

The negation is true. Take \( a = 2 \), \( b = -1 \), \( c = 0 \). Then

\[
2(1, 2) - (2, 4) + 0(0, 1) = (2 - 2 + 0,\ 4 - 4 + 0) = (0, 0),
\]

and \( a = 2 \ne 0 \). So the original statement is false.
:::

In Chapter 1 the original statement is what "the list is linearly independent" means, and its negation is "linearly dependent". The small words in the negation carry the weight.

::: {.warning}
**"Not all zero" is not "all non-zero".** The negation of "\( a = b = c = 0 \)" is "at least one of \( a, b, c \) is non-zero". In @exm-negation-not-all-zero the witness is \( (2, -1, 0) \), which has a zero entry. In fact **no** witness has all three entries non-zero: comparing entries, \( a + 2b = 0 \) and \( 2a + 4b + c = 0 \), so \( c = -2(a + 2b) = 0 \). Negating with "all non-zero" would wrongly conclude that the original statement is true.
:::

::: {.check}
Negate "every student passed some exam", with no "not" in front of the whole sentence.
:::

::: {.solution}
Write it as "\( \forall \) students \( s \) \( \exists \) exam \( e \) : \( s \) passed \( e \)". Flipping both quantifiers and negating the inside gives "\( \exists \) student \( s \) \( \forall \) exams \( e \) : \( s \) did not pass \( e \)". In words: **some student passed no exam**. The tempting answer "no student passed any exam" is the negation of "some student passed some exam", a different statement.
:::

::: {.remark}
Each form of statement suggests how to prove or refute it. To prove \( \forall x \in S : P(x) \), take an arbitrary \( x \in S \) and show \( P(x) \). To prove \( \exists x \in S : P(x) \), produce a witness. To refute a \( \forall \), produce one counterexample. To refute an \( \exists \), show every candidate fails. The next section develops these moves into proof techniques.
:::

## Exercises

### A. Check your understanding

::: {#exr-logic-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Decide whether each statement is true: (i) "\( 3 < 2 \) or \( 3 \) is odd"; (ii) "if \( 3 < 2 \), then \( 3 = 5 \)"; (iii) "if \( 3 \) is odd, then \( 3 < 2 \)".
2. Write the converse and the contrapositive of "if an integer \( n \) is divisible by \( 4 \), then \( n \) is even". Which of the three statements are true for every integer \( n \)?
3. Negate \( \forall x \in \nR \ \exists n \in \nZ : n > x \), with no \( \neg \) in front. Which of the statement and its negation is true?
4. True or false: \( \neg(P \wedge Q) \equiv \neg P \wedge \neg Q \) for all statements \( P, Q \). Give a reason.
:::
:::

::: {.solution}
(a) (i) True: the second part is true, and a disjunction needs only one true part. (ii) True: the hypothesis \( 3 < 2 \) is false, so the implication is vacuously true. (iii) False: the hypothesis is true and the conclusion is false, which is the one case where an implication fails.

(b) The converse is "if \( n \) is even, then \( n \) is divisible by \( 4 \)". The contrapositive is "if \( n \) is odd, then \( n \) is not divisible by \( 4 \)". The original is true: \( n = 4k \) gives \( n = 2(2k) \). The contrapositive is true by @thm-contrapositive-equivalent. The converse is false: \( n = 2 \) is even and not divisible by \( 4 \).

(c) By @def-negation-of-quantifiers, the negation is \( \exists x \in \nR \ \forall n \in \nZ : n \le x \). The original is true: given \( x \), some integer exceeds \( x \) (for instance the integer part of \( \lvert x \rvert \) plus \( 1 \)). So the negation is false.

(d) False. Take \( P \) true and \( Q \) false. Then \( P \wedge Q \) is false, so \( \neg(P \wedge Q) \) is true, while \( \neg P \wedge \neg Q \) is false because \( \neg P \) is false. The correct law is \( \neg(P \wedge Q) \equiv \neg P \vee \neg Q \), by @thm-de-morgan-logic.
:::

### B. Practice

::: {#exr-logic-b1}
[B1: Negating definitions]

Write the negation of each definition as a quantified statement with no \( \neg \) in front, and then say it in words.

::: {.enumerate options="label=(\alph*)"}
1. A function \( f \) from \( \nR \) to \( \nR \) is **bounded** if \( \exists M \in \nR \ \forall x \in \nR : \lvert f(x) \rvert \le M \).
2. A function \( f \) from \( A \) to \( B \) is injective if \( \forall a_1, a_2 \in A : \bigl(a_1 \ne a_2 \Rightarrow f(a_1) \ne f(a_2)\bigr) \). Compare your answer with @exm-negation-injectivity.
3. "Every pair of reals is a combination of \( (1, 0) \) and \( (1, 1) \)": \( \forall p, q \in \nR \ \exists a, b \in \nR : (p, q) = a(1, 0) + b(1, 1) \), where pairs are added and scaled entry by entry.
:::
:::

::: {.solution}
(a) By @def-negation-of-quantifiers, \( f \) is not bounded if and only if \( \forall M \in \nR \ \exists x \in \nR : \lvert f(x) \rvert > M \). In words: whatever bound \( M \) is proposed, some value of \( f \) exceeds it in absolute value.

(b) Flip both quantifiers and negate the implication using law (c) of @thm-de-morgan-logic: \( \exists a_1, a_2 \in A : a_1 \ne a_2 \wedge f(a_1) = f(a_2) \). In words: two different inputs share an output. This is the same condition as in @exm-negation-injectivity. That is expected: the given implication is the contrapositive of \( f(a_1) = f(a_2) \Rightarrow a_1 = a_2 \), so by @thm-contrapositive-equivalent the two definitions agree, and so do their negations.

(c) Flip all the quantifiers and negate the equation: \( \exists p, q \in \nR \ \forall a, b \in \nR : (p, q) \ne a(1, 0) + b(1, 1) \). In words: some pair is not a combination of \( (1, 0) \) and \( (1, 1) \), whatever coefficients are used. (The original is in fact true, since \( (p - q)(1, 0) + q(1, 1) = (p, q) \), so this negation is false.)
:::

::: {#exr-logic-b2}
[B2: Integers versus reals]

For each statement, decide whether it is true when \( x \) and \( y \) range over \( \nZ \), and whether it is true when they range over \( \nR \). Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \forall x \ \exists y : x < y < x + 1 \).
2. \( \forall x \ \bigl( x \ne 0 \Rightarrow \exists y : xy = 1 \bigr) \).
3. \( \exists x \ \forall y : xy = y \).
4. \( \forall x \ \exists y : y^2 = x \).
:::
:::

::: {.solution}
(a) Over \( \nZ \): false. Take \( x = 0 \). No integer \( y \) satisfies \( 0 < y < 1 \). Over \( \nR \): true. Given \( x \), take \( y = x + \tfrac12 \); then \( x < y < x + 1 \).

(b) Over \( \nZ \): false. Take \( x = 2 \), which is non-zero. If \( 2y = 1 \) for an integer \( y \), then \( 1 \) would be even, which is false. Over \( \nR \): true. Given \( x \ne 0 \), take \( y = 1/x \), which exists because \( x \ne 0 \), and then \( xy = 1 \).

(c) True over both. Take \( x = 1 \), which lies in \( \nZ \) and in \( \nR \). Then \( xy = y \) for every \( y \). Here one \( x \) works for all \( y \), so the order \( \exists x \, \forall y \) causes no difficulty.

(d) False over both. Take \( x = -1 \). For every \( y \), integer or real, \( y^2 \ge 0 > -1 \) by @exm-quantifiers, so \( y^2 \ne -1 \).
:::

### C. Going deeper

::: {#exr-logic-c1}
[C1: Exporting a hypothesis]

Prove that \( P \Rightarrow (Q \Rightarrow R) \) is logically equivalent to \( (P \wedge Q) \Rightarrow R \) for all statements \( P, Q, R \). Explain in one sentence why this lets a theorem with two hypotheses be stated either way.
:::

::: {.solution}
Let \( P, Q, R \) be statements. By @def-implication-converse-contrapositive, an implication is false exactly when its hypothesis is true and its conclusion is false.

The statement \( (P \wedge Q) \Rightarrow R \) is false exactly when \( P \wedge Q \) is true and \( R \) is false, that is, when \( P \) is true, \( Q \) is true and \( R \) is false.

The statement \( P \Rightarrow (Q \Rightarrow R) \) is false exactly when \( P \) is true and \( Q \Rightarrow R \) is false. By the same definition, \( Q \Rightarrow R \) is false exactly when \( Q \) is true and \( R \) is false. So \( P \Rightarrow (Q \Rightarrow R) \) is false exactly when \( P \) is true, \( Q \) is true and \( R \) is false.

Both statements are false in exactly the same row of the eight-row truth table, and true in the other seven. Hence they are logically equivalent.

Consequently "if \( P \), then (if \( Q \), then \( R \))" and "if \( P \) and \( Q \), then \( R \)" say the same thing, so a theorem may list its hypotheses one after another or all together.
:::

::: {#exr-logic-c2}
[C2: When can a converse fail too?]

::: {.enumerate options="label=(\alph*)"}
1. Determine whether there exist statements \( P \) and \( Q \) such that both \( P \Rightarrow Q \) and its converse \( Q \Rightarrow P \) are false. Justify your answer.
2. Give predicates \( P(n) \) and \( Q(n) \) about integers such that both \( \forall n \in \nZ : \bigl(P(n) \Rightarrow Q(n)\bigr) \) and \( \forall n \in \nZ : \bigl(Q(n) \Rightarrow P(n)\bigr) \) are false.
3. Explain why (a) and (b) do not contradict each other.
:::
:::

::: {.solution}
(a) No such statements exist. Suppose \( P \Rightarrow Q \) is false. By @def-implication-converse-contrapositive, \( P \) is true and \( Q \) is false. Then \( Q \Rightarrow P \) has a false hypothesis, so it is true. Hence an implication and its converse can never both be false.

(b) Let \( P(n) \) be "\( n \) is even" and \( Q(n) \) be "\( n \) is divisible by \( 3 \)". The first universal statement is false: \( n = 2 \) is even and not divisible by \( 3 \). The second is false: \( n = 3 \) is divisible by \( 3 \) and not even.

(c) In (a), \( P \) and \( Q \) are single statements, each with one fixed truth value. In (b), each universal statement is refuted by its own counterexample, and the two counterexamples are **different** integers. At \( n = 2 \) the converse \( Q(2) \Rightarrow P(2) \) is vacuously true, and at \( n = 3 \) the original \( P(3) \Rightarrow Q(3) \) is vacuously true, in line with (a). A "for every" statement can fail at one place while its converse fails somewhere else.
:::
