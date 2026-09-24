# Fields

Linear algebra is about equations like \( 2x + 3y = 7 \), and so far we have met several number systems in which such equations make sense: \( \nQ \), \( \nR \), \( \nC \), and the arithmetic of remainders \( \nZ/n\nZ \). Which of them can serve as the numbers of linear algebra? This section answers by isolating the rules that solving linear equations actually uses. A number system obeying those rules is called a field, and fields are the scalars of every later chapter.

## What solving linear equations needs

Here is a small system, solved the way you learned at school:
\[
\begin{aligned}
2x + 3y &= 7, \\
x - y &= 1.
\end{aligned}
\]
Subtracting twice the second equation from the first gives \( 5y = 5 \). Dividing by \( 5 \) gives \( y = 1 \), and then \( x = 1 + y = 2 \). Check: \( 2 \cdot 2 + 3 \cdot 1 = 7 \) and \( 2 - 1 = 1 \).

Look at what we used. We added and subtracted equations, multiplied an equation by a number, and divided by a **non-zero** number. Silently we also rearranged terms, regrouped them and expanded brackets. Every step of Gaussian elimination is of this kind, and every one of them works in \( \nQ \), \( \nR \) and \( \nC \).

Now try the integers. The equation \( 2x = 1 \) involves only integers, yet it has no integer solution, because the step "divide by \( 2 \)" leaves \( \nZ \). Elimination stalls as soon as a pivot has no inverse. So what separates \( \nZ \) from \( \nQ \) is division, and division is exactly what we must demand.

*A field is a number system where you can add, subtract, multiply, and divide by anything non-zero, with the usual rules.*

## The definition

::: {#def-field}
[Field]

A **field** is a set \( F \) together with two functions, **addition** \( + \colon F \times F \to F \), \( (a, b) \mapsto a + b \), and **multiplication** \( \cdot \colon F \times F \to F \), \( (a, b) \mapsto a \cdot b = ab \), satisfying the following axioms.

::: {.enumerate options="label=(F\arabic*)"}
1. \( a + b = b + a \) **for all** \( a, b \in F \).
2. \( (a + b) + c = a + (b + c) \) **for all** \( a, b, c \in F \).
3. There exists an element \( 0 \in F \) such that \( a + 0 = a \) **for every** \( a \in F \).
4. **For every** \( a \in F \) there exists an element \( -a \in F \) such that \( a + (-a) = 0 \).
5. \( (ab)c = a(bc) \) **for all** \( a, b, c \in F \).
6. \( ab = ba \) **for all** \( a, b \in F \).
7. There exists an element \( 1 \in F \) with **\( 1 \ne 0 \)** such that \( a \cdot 1 = a \) **for every** \( a \in F \).
8. **For every non-zero** \( a \in F \) there exists an element \( a^{-1} \in F \) such that \( a a^{-1} = 1 \).
9. \( a(b + c) = ab + ac \) **for all** \( a, b, c \in F \).
:::
:::

Read the axioms in groups.

- **(F1)–(F4)** are about addition alone. It is commutative and associative, it has a neutral element \( 0 \), and every element has a negative. Subtraction is then defined by \( a - b \coloneqq a + (-b) \).
- **(F5)–(F8)** say the same things about multiplication, with one change: only **non-zero** elements are required to have inverses. Division is defined by \( a / b \coloneqq a b^{-1} \) for \( b \ne 0 \). We never divide by \( 0 \), and the axioms never ask us to.
- **(F7)** also insists that \( 1 \ne 0 \): the two neutral elements are different.
- **(F9)** is the one rule linking the two operations. It is what lets us expand brackets.

Note the order of quantifiers in (F3): **one** element \( 0 \) works **for every** \( a \). This is stronger than "for every \( a \) there is some element \( z_a \) with \( a + z_a = a \)". In (F4) the order is reversed, as it must be: the negative \( -a \) depends on \( a \).

We often say "\( F \) is a field" when the operations are clear, and write \( (F, +, \cdot) \) when they need to be named. Since addition and multiplication are functions into \( F \), sums and products of elements of \( F \) stay in \( F \); when we build a field inside a bigger number system, this "closure" is the first thing to check.

## First consequences of the axioms

The notation in the definition hides a question. We wrote "\( 0 \)", "\( -a \)" and "\( a^{-1} \)" as if each were a single well-defined element. The axioms only say that such elements **exist**. If a field could contain two different elements behaving like \( 0 \), the symbol \( 0 \) would be ambiguous, and so would \( a - b \) and \( a / b \). The next theorem removes this worry and proves the familiar rules of algebra from the nine axioms.

::: {#thm-field-basic-properties}
[Basic Properties of Fields]

Let \( F \) be a field and let \( a, b, c \in F \).

::: {.enumerate options="label=(\alph*)"}
1. The element \( 0 \) in (F3) is unique, and the element \( 1 \) in (F7) is unique.
2. (Cancellation) If \( a + b = a + c \), then \( b = c \). If \( ab = ac \) and \( a \ne 0 \), then \( b = c \).
3. The negative \( -a \) in (F4) is unique, and for \( a \ne 0 \) the inverse \( a^{-1} \) in (F8) is unique.
4. \( 0 \cdot a = 0 \).
5. \( (-1)a = -a \).
6. If \( ab = 0 \), then \( a = 0 \) or \( b = 0 \).
:::
:::

::: {.idea}
Each part is a short chain of axioms, and the chain is found backwards from the goal. For uniqueness we use the standard move: suppose two elements both have the property, and show they are equal. For (d) there is no axiom about \( 0 \cdot a \) at all, so we must create a situation where one applies. The trick is to rewrite \( 0 \) in a fancy way as \( 0 + 0 \), expand with (F9), and cancel. For (f), the hypothesis \( a \ne 0 \) is there to be spent on (F8).
:::

We prove the uniqueness of \( 0 \), additive cancellation, the uniqueness of negatives, (d) and (f). The remaining statements are @exr-fields-b1.

::: {.proof}
(a) Suppose \( 0 \) and \( 0' \) both satisfy (F3). Applying (F3) for \( 0' \) to the element \( 0 \), and (F3) for \( 0 \) to the element \( 0' \), and using (F1),
\[
0 = 0 + 0' = 0' + 0 = 0'.
\]
So the zero element is unique.

(b) Suppose \( a + b = a + c \). Adding \( -a \) on the left of both sides and using (F2),
\[
((-a) + a) + b = ((-a) + a) + c.
\]
By (F1) and (F4), \( (-a) + a = a + (-a) = 0 \). Hence \( 0 + b = 0 + c \), and by (F1) and (F3) this says \( b = c \).

(c) Suppose \( b \) and \( c \) both satisfy (F4) for \( a \), that is, \( a + b = 0 \) and \( a + c = 0 \). Then \( a + b = a + c \), so \( b = c \) by additive cancellation in (b).

(d) By (F3), \( 0 + 0 = 0 \). Therefore, by (F9),
\[
a \cdot 0 = a (0 + 0) = a \cdot 0 + a \cdot 0.
\]
By (F3), also \( a \cdot 0 = a \cdot 0 + 0 \). Comparing, \( a \cdot 0 + 0 = a \cdot 0 + a \cdot 0 \), and additive cancellation (b) gives \( 0 = a \cdot 0 \). Finally \( 0 \cdot a = a \cdot 0 \) by (F6), so \( 0 \cdot a = 0 \).

(f) Suppose \( ab = 0 \). If \( a = 0 \) there is nothing to prove, so suppose \( a \ne 0 \). By (F8), \( a^{-1} \) exists. Then, by (F7), (F8), (F6) and (F5),
\[
b = b \cdot 1 = b(a a^{-1}) = (ba)a^{-1} = (ab)a^{-1} = 0 \cdot a^{-1} = 0,
\]
where the last equality is (d). This shows that \( a = 0 \) or \( b = 0 \).
:::

Two small consequences are used without comment from now on: \( 0 + a = a \) and \( 1 \cdot a = a \), by (F1), (F3), (F6) and (F7). More importantly, every identity of school algebra that is proved from these rules, such as \( (a + b)^2 = a^2 + 2ab + b^2 \) or \( (-a)(-b) = ab \), now holds in every field. Part (f) is the property we will use most: a product of non-zero elements is non-zero.

## Examples

We check the standard examples first, then an exotic one, then a degenerate case.

::: {#exm-fields}
[The Fields \( \nQ \), \( \nR \) and \( \nC \)]

Explain why \( \nQ \), \( \nR \) and \( \nC \), with their usual addition and multiplication, are fields.
:::

::: {.solution}
For \( \nR \), the axioms (F1)–(F9) are the rules of arithmetic for real numbers that we take as familiar, and \( 1 \ne 0 \).

For \( \nQ \), the sum, product and negative of fractions are fractions, and so is the inverse \( \frac{q}{p} \) of a non-zero fraction \( \frac{p}{q} \). So the operations of \( \nR \) restrict to functions \( \nQ \times \nQ \to \nQ \), and \( 0, 1, -a, a^{-1} \) lie in \( \nQ \) whenever \( a \) does. The identities in (F1), (F2), (F5), (F6) and (F9) hold for all real numbers, so in particular for rational ones. Hence \( \nQ \) is a field.

For \( \nC \), the axioms (F1)–(F6) and (F9), together with the existence of \( 1 = 1 + 0i \), are @prp-complex-arithmetic-laws. We have \( 1 = (1, 0) \ne (0, 0) = 0 \). Finally (F8) is @prp-complex-inverse: a non-zero \( z \) has the inverse \( \conj{z} / \lvert z \rvert^2 \). Hence \( \nC \) is a field.
:::

The next example is a field strictly between \( \nQ \) and \( \nR \). It shows that the inverse axiom (F8) can take real work to check.

::: {#exm-q-sqrt2-field}
[\( \nQ(\sqrt{2}) \) Is a Field]

Let \( \nQ(\sqrt2) \coloneqq \{ a + b\sqrt2 : a, b \in \nQ \} \subseteq \nR \), with the addition and multiplication of \( \nR \). Show that \( \nQ(\sqrt2) \) is a field, and find the inverse of \( 1 + 2\sqrt2 \).
:::

::: {.solution}
Let \( x = a + b\sqrt2 \) and \( y = c + d\sqrt2 \) with \( a, b, c, d \in \nQ \).

*Closure.* We have \( x + y = (a + c) + (b + d)\sqrt2 \) and \( xy = (ac + 2bd) + (ad + bc)\sqrt2 \), using \( \sqrt2 \cdot \sqrt2 = 2 \). The coefficients are rational, so \( x + y, xy \in \nQ(\sqrt2) \).

*Axioms that are identities.* (F1), (F2), (F5), (F6) and (F9) hold for all real numbers, hence for the elements of \( \nQ(\sqrt2) \).

*Neutral elements and negatives.* \( 0 = 0 + 0\sqrt2 \) and \( 1 = 1 + 0\sqrt2 \) lie in \( \nQ(\sqrt2) \), and \( 1 \ne 0 \). The negative \( -x = (-a) + (-b)\sqrt2 \) lies in \( \nQ(\sqrt2) \).

*Inverses.* Suppose \( x \ne 0 \). We first claim \( a - b\sqrt2 \ne 0 \). If \( b \ne 0 \) and \( a - b\sqrt2 = 0 \), then \( \sqrt2 = a/b \) would be rational, contradicting @thm-sqrt2-irrational. If \( b = 0 \), then \( a = x \ne 0 \), so \( a - b\sqrt2 = a \ne 0 \). Therefore \( a - b\sqrt2 \ne 0 \), and by @thm-field-basic-properties (f) in \( \nR \),
\[
N \coloneqq (a + b\sqrt2)(a - b\sqrt2) = a^2 - 2b^2 \ne 0.
\]
Since \( N \) is a non-zero rational number, the element
\[
x' \coloneqq \frac{a}{N} + \frac{-b}{N}\sqrt2 \in \nQ(\sqrt2)
\]
satisfies \( x x' = \frac1N (a + b\sqrt2)(a - b\sqrt2) = 1 \). So (F8) holds, and \( \nQ(\sqrt2) \) is a field.

For \( x = 1 + 2\sqrt2 \) we get \( N = 1 - 8 = -7 \), so \( x^{-1} = -\frac17 + \frac27\sqrt2 = \frac{-1 + 2\sqrt2}{7} \). Check: \( (1 + 2\sqrt2)(-1 + 2\sqrt2) = -1 + 2\sqrt2 - 2\sqrt2 + 8 = 7 \).
:::

The method is "rationalize the denominator", the same move as multiplying by the conjugate in \( \nC \). The irrationality of \( \sqrt2 \) is exactly what guarantees the new denominator is not zero.

::: {.check}
Is \( \{ a + b\sqrt3 : a, b \in \nQ \} \), with the operations of \( \nR \), a field?
:::

::: {.solution}
Yes, by the same argument as @exm-q-sqrt2-field. Products stay in the set because \( \sqrt3 \cdot \sqrt3 = 3 \) is rational. For inverses, the number \( a^2 - 3b^2 \) is non-zero whenever \( a + b\sqrt3 \ne 0 \), because \( \sqrt3 \) is irrational (@exr-proofs-b3). The inverse is \( \frac{a - b\sqrt3}{a^2 - 3b^2} \).
:::

**The degenerate case.** Let \( F = \{0\} \) with \( 0 + 0 = 0 \) and \( 0 \cdot 0 = 0 \). Every axiom except one holds: (F1), (F2), (F5), (F6) and (F9) are identities between elements that all equal \( 0 \), (F3) and (F4) hold with \( -0 = 0 \), and (F8) holds vacuously because there is no non-zero element. The only failure is (F7): the one element that could serve as \( 1 \) is \( 0 \), and the axiom demands **\( 1 \ne 0 \)**. So \( \{0\} \) is not a field, and every field has at least the two elements \( 0 \) and \( 1 \). This one-element system is the reason the clause \( 1 \ne 0 \) is there.

## Finite fields

Every field so far is infinite. The arithmetic of remainders gives finite ones, and they are genuinely useful: computer science and coding theory do linear algebra over them all the time.

Recall from @def-equivalence-relation and @def-quotient-set that for an integer \( n \ge 1 \), congruence modulo \( n \) is an equivalence relation on \( \nZ \). We write \( [a] \) for the class of \( a \) and \( \nZ/n\nZ \) for the quotient set. By division with remainder (@exr-proofs-c2), \( \nZ/n\nZ = \{[0], [1], \dots, [n-1]\} \), and these \( n \) classes are distinct. Also \( [a] = [b] \) exactly when \( n \) divides \( a - b \).

::: {#exm-finite-fields}
[Arithmetic on \( \nZ/n\nZ \) and the Field \( \nF_2 \)]

Let \( n \ge 1 \). Define \( [a] + [b] \coloneqq [a + b] \) and \( [a][b] \coloneqq [ab] \). Show that these operations are well defined, that they satisfy every field axiom except possibly (F8) and the clause \( 1 \ne 0 \), and that \( 1 \ne 0 \) holds exactly when \( n \ge 2 \). Write out the tables for \( n = 2 \).
:::

::: {.solution}
*Well-definedness.* The formulas use representatives, so we must check that the answer does not depend on which representatives we pick. For addition this is @exm-addition-mod-n-well-defined. For multiplication, suppose \( [a] = [a'] \) and \( [b] = [b'] \), so \( n \) divides \( a - a' \) and \( b - b' \). Then
\[
ab - a'b' = a(b - b') + (a - a')b'
\]
is divisible by \( n \), so \( [ab] = [a'b'] \).

*Axioms.* Every identity in (F1), (F2), (F5), (F6), (F9) transfers from \( \nZ \), because both sides can be computed on representatives. For instance, for (F9),
\[
[a]([b] + [c]) = [a][b + c] = [a(b + c)] = [ab + ac] = [ab] + [ac] = [a][b] + [a][c].
\]
The same one-line computation works for the other four. The class \( [0] \) satisfies (F3) since \( [a] + [0] = [a] \), the class \( [-a] \) is a negative of \( [a] \) as in (F4), and \( [1] \) satisfies \( [a][1] = [a] \).

*The clause \( 1 \ne 0 \).* We have \( [1] = [0] \) exactly when \( n \) divides \( 1 \), that is, when \( n = 1 \). So \( [1] \ne [0] \) exactly when \( n \ge 2 \).

*Tables for \( n = 2 \).* Writing \( 0, 1 \) for \( [0], [1] \), the set \( \nF_2 \coloneqq \nZ/2\nZ = \{0, 1\} \) has the tables
\[
\begin{array}{c|cc} + & 0 & 1 \\
\hline
0 & 0 & 1 \\
1 & 1 & 0
\end{array}
\qquad\qquad
\begin{array}{c|cc}
\cdot & 0 & 1 \\
\hline
0 & 0 & 0 \\
1 & 0 & 1
\end{array}
\]
The only surprise is \( 1 + 1 = 0 \), since \( 2 \) is even. Here (F8) holds as well, since the only non-zero element is \( 1 \) and \( 1 \cdot 1 = 1 \). Hence \( \nF_2 \) is a field.
:::

So for \( n \ge 2 \), whether \( \nZ/n\nZ \) is a field comes down to one question: does every non-zero class have an inverse? To find an inverse of \( [a] \) we need an integer \( x \) with \( [ax] = [1] \), that is, \( ax + ny = 1 \) for some integer \( y \). The following lemma produces such \( x \) and \( y \).

::: {#lem-bezout-integers}
[Bézout's Lemma for Integers]

Let \( a, n \in \nZ \) with \( n \ge 1 \), and suppose that the only positive integer dividing both \( a \) and \( n \) is \( 1 \). Then there exist \( x, y \in \nZ \) with
\[
ax + ny = 1.
\]
:::

::: {.idea}
Consider all positive integers of the form \( ax + ny \). There is a smallest one, \( d \), by well-ordering. The plan: ① show \( d \) divides \( a \) and \( n \); ② conclude \( d = 1 \) from the hypothesis. For ①, divide \( a \) by \( d \): the remainder is again of the form \( ax + ny \) and is smaller than \( d \), so minimality forces it to be \( 0 \).
:::

::: {.proof}
Let \( S = \{ ax + ny : x, y \in \nZ \} \cap \{1, 2, 3, \dots\} \). Since \( n = a \cdot 0 + n \cdot 1 \ge 1 \), we have \( n \in S \), so \( S \) is a non-empty subset of \( \nN \). By the well-ordering principle (@thm-well-ordering), \( S \) has a smallest element \( d = ax_0 + ny_0 \).

Next we divide \( a \) by \( d \), using well-ordering a second time. Let \( R \) be the collection of non-negative integers of the form \( a - qd \) with \( q \in \nZ \). Taking \( q = -\lvert a \rvert \) gives \( a + \lvert a \rvert d \), which is non-negative because \( d \ge 1 \) forces \( \lvert a \rvert d \ge \lvert a \rvert \ge -a \); so \( R \) is non-empty, and by @thm-well-ordering it has a least element \( r = a - qd \ge 0 \). If \( r \ge d \), then \( r - d = a - (q + 1)d \) would lie in \( R \) and be smaller than \( r \), contradicting minimality. Hence \( 0 \le r < d \), and \( a = qd + r \); this is the division with remainder of @exr-proofs-c2, repeated here in the one case the proof needs. Now
\[
r = a - q(ax_0 + ny_0) = a(1 - qx_0) + n(-qy_0)
\]
has the form \( ax + ny \). If \( r \ge 1 \), then \( r \in S \) and \( r < d \), contradicting the minimality of \( d \). Hence \( r = 0 \), and \( d \) divides \( a \). The same argument with \( n \) in place of \( a \) shows that \( d \) divides \( n \).

Therefore \( d \) is a positive integer dividing both \( a \) and \( n \). By hypothesis \( d = 1 \), so \( ax_0 + ny_0 = 1 \), as claimed.
:::

Now we can decide exactly when \( \nZ/n\nZ \) is a field.

::: {#thm-zp-field-iff-prime}
[\( \nZ/n\nZ \) Is a Field Exactly for Prime \( n \)]

Let \( n \ge 2 \) be an integer. Then \( \nZ/n\nZ \) is a field if and only if \( n \) is prime.
:::

::: {.idea}
By @exm-finite-fields, only (F8) is in question. If \( n \) is prime, a non-zero class \( [a] \) has \( a \) not divisible by \( n \), so \( a \) and \( n \) share no factor, and Bézout hands us the inverse. If \( n = rs \) factors, then \( [r][s] = [n] = [0] \) with both factors non-zero, which no field allows.
:::

::: {.proof}
By @exm-finite-fields, \( \nZ/n\nZ \) satisfies all field axioms except possibly (F8), including \( [1] \ne [0] \) since \( n \ge 2 \).

\( (\Leftarrow) \) Suppose \( n = p \) is prime, and let \( [a] \ne [0] \). Then \( p \) does not divide \( a \). A positive integer dividing \( p \) is \( 1 \) or \( p \), and \( p \) does not divide \( a \), so the only positive common divisor of \( a \) and \( p \) is \( 1 \). By @lem-bezout-integers there are \( x, y \in \nZ \) with \( ax + py = 1 \). Since \( ax - 1 = -py \) is divisible by \( p \),
\[
[a][x] = [ax] = [1].
\]
So \( [x] \) is an inverse of \( [a] \), and (F8) holds. Hence \( \nZ/p\nZ \) is a field.

\( (\Rightarrow) \) We prove the contrapositive. Suppose \( n \ge 2 \) is not prime. Then \( n = rs \) for some integers \( r, s \) with \( 1 < r < n \) and \( 1 < s < n \). Since \( 0 < r < n \), \( n \) does not divide \( r \), so \( [r] \ne [0] \); likewise \( [s] \ne [0] \). But \( [r][s] = [rs] = [n] = [0] \). By @thm-field-basic-properties (f), this cannot happen in a field. Hence \( \nZ/n\nZ \) is not a field. This proves the theorem.
:::

For a prime \( p \) we write \( \nF_p \coloneqq \nZ/p\nZ \), and usually drop the brackets, writing its elements as \( 0, 1, \dots, p - 1 \) and computing "mod \( p \)". So \( \nF_2, \nF_3, \nF_5, \nF_7, \dots \) are fields, while \( \nZ/4\nZ \), \( \nZ/6\nZ \) and \( \nZ/9\nZ \) are not.

::: {.check}
Find the inverse of \( 3 \) in \( \nF_7 \).
:::

::: {.solution}
We need \( x \) with \( 3x \) leaving remainder \( 1 \) on division by \( 7 \). Trying \( x = 1, 2, \dots \): \( 3 \cdot 5 = 15 = 2 \cdot 7 + 1 \). So \( 3^{-1} = 5 \) in \( \nF_7 \). (By @thm-field-basic-properties (c) this is the only inverse.)
:::

Because \( \nF_p \) is a field, the elimination from the start of the section runs unchanged in it. Only the arithmetic is new.

::: {#exm-elimination-f5}
[Elimination over \( \nF_5 \)]

Solve the system \( 2x + y = 3 \), \( 3x + 2y = 4 \) over \( \nF_5 \).
:::

::: {.solution}
In \( \nF_5 \) the inverses are \( 1^{-1} = 1 \), \( 2^{-1} = 3 \), \( 3^{-1} = 2 \), \( 4^{-1} = 4 \), since \( 2 \cdot 3 = 6 = 5 + 1 \) and \( 4 \cdot 4 = 16 = 15 + 1 \). Multiply the first equation by \( 2^{-1} = 3 \): since \( 3 \cdot 2 = 1 \), \( 3 \cdot 1 = 3 \) and \( 3 \cdot 3 = 9 = 4 \), it becomes \( x + 3y = 4 \). Subtract \( 3 \) times this from the second equation: the \( x \)-terms cancel, and we get
\[
(2 - 9)y = 4 - 12, \quad \text{that is,} \quad 3y = 2,
\]
since \( -7 = -10 + 3 \) and \( -8 = -10 + 2 \). Multiply by \( 3^{-1} = 2 \): \( y = 4 \). Then \( x = 4 - 3y = 4 - 12 = -8 = 2 \). Check: \( 2 \cdot 2 + 4 = 8 = 3 \) and \( 3 \cdot 2 + 2 \cdot 4 = 14 = 4 \) in \( \nF_5 \). Hence \( (x, y) = (2, 4) \) is the unique solution.
:::

## Non-examples

Each of these fails some part of the slogan, and it pays to name the exact clause that fails.

- **\( \nZ \).** Everything but (F8) holds: \( \nZ \) is closed under \( + \) and \( \cdot \), contains \( 0 \), \( 1 \) and negatives, and inherits the identities from \( \nR \). But \( 2 \ne 0 \) has no inverse in \( \nZ \), since \( 2m \) is even and never equals \( 1 \). Changing \( \nZ \) to \( \nQ \) is the minimal change that repairs it.
- **\( \nZ/6\nZ \).** This is \( \nF_5 \) with the modulus changed from \( 5 \) to \( 6 \). All axioms but (F8) still hold (@exm-finite-fields), but \( [2][3] = [0] \) with \( [2], [3] \ne [0] \). By @thm-field-basic-properties (f), \( [2] \) cannot have an inverse; indeed \( [2][x] \) is always one of \( [0], [2], [4] \).
- **\( 2 \times 2 \) real matrices**, with the matrix operations you know from school (they are treated properly later in this chapter). The identity matrix plays the role of \( 1 \). Two axioms fail. (F6) fails:
  \[
  \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \qquad \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}.
  \]
  (F8) fails too: \( \E = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \) is not the zero matrix, but every product \( \E\X \) has second row zero, so \( \E\X \) is never the identity.

::: {.warning}
"\( [a] \ne [0] \)" does not mean \( [a] \) can be divided by in \( \nZ/n\nZ \). In \( \nZ/6\nZ \) the equation \( [2]x = [1] \) has no solution, and \( [2]x = [4] \) has two, \( x = [2] \) and \( x = [5] \). Before dividing modulo \( n \), check that \( n \) is prime, or at least that \( a \) and \( n \) share no factor.
:::

## Why these axioms

Each clause is there because something we rely on breaks without it.

- **Without (F8)**, elimination stalls, as \( 2x = 1 \) over \( \nZ \) showed. Worse, the theorems of the next chapters fail: over \( \nZ \), the analogues of vector spaces (called modules) need not have bases, and "a set of \( n \) independent vectors in an \( n \)-dimensional space spans it" becomes false. This book always works over a field.
- **Without (F6)**, scalars would not commute with each other. The matrices above show such systems exist, and there are even systems with division but without commutativity. Linear algebra constantly swaps scalars, as in \( a(b\v) = b(a\v) \) for a vector \( \v \) (Chapter 1), so we keep commutativity.
- **Without \( 1 \ne 0 \)**, the one-element system \( \{0\} \) would count, and every statement of the form "a field has a non-zero element" would fail. Keeping it costs nothing.
- **The name** "field" is historical and carries no extra meaning.

::: {.remark}
Many identities we are used to are consequences of the axioms and hold in **every** field, including \( \nF_2 \). But properties that involve **order** or **size**, such as "squares are non-negative" or "\( 1 + 1 + \dots + 1 \ne 0 \)", are not among the axioms. The first already fails in \( \nC \), where \( i^2 = -1 \), as the warning on ordering in the previous section explains. The second fails in \( \nF_p \), which is the subject of the last part of this section.
:::

## The characteristic of a field

In \( \nQ \) we can add \( 1 \) to itself as often as we like without reaching \( 0 \). In \( \nF_2 \) two copies already give \( 0 \), and in \( \nF_p \) it takes \( p \) copies. This number is the most basic invariant of a field, and it decides whether familiar arguments such as "\( 2x = 0 \) implies \( x = 0 \)" are valid.

First some notation. For \( a \in F \) and \( m \in \nN \), define the **integer multiple** \( m \cdot a \) by \( 0 \cdot a \coloneqq 0 \) and \( (m + 1) \cdot a \coloneqq m \cdot a + a \). So \( m \cdot a = a + a + \dots + a \) with \( m \) terms. This agrees with the field product when \( m = 0 \), by @thm-field-basic-properties (d).

::: {#lem-integer-multiples}
[Integer Multiples]

Let \( F \) be a field, \( a \in F \) and \( m, k \in \nN \). Then
\[
\begin{aligned}
(m \cdot 1) + (k \cdot 1) &= (m + k) \cdot 1, \\
(m \cdot 1)(k \cdot 1) &= (mk) \cdot 1, \\
(m \cdot 1)\, a &= m \cdot a.
\end{aligned}
\]
:::

::: {.proof}
All three follow by induction on one variable (@thm-induction). For the first, induct on \( k \): the case \( k = 0 \) is \( m \cdot 1 + 0 = m \cdot 1 \) by (F3), and if it holds for \( k \), then by (F2) and the definition,
\[
m \cdot 1 + (k + 1) \cdot 1 = (m \cdot 1 + k \cdot 1) + 1 = (m + k) \cdot 1 + 1 = (m + k + 1) \cdot 1.
\]
For the third, induct on \( m \): the case \( m = 0 \) is \( 0 \cdot a = 0 \) by @thm-field-basic-properties (d), and if it holds for \( m \), then by (F6), (F9) and (F7),
\[
((m + 1) \cdot 1)\, a = (m \cdot 1 + 1)\, a = (m \cdot 1)\, a + 1 \cdot a = m \cdot a + a = (m + 1) \cdot a.
\]
The second is the third with \( a = k \cdot 1 \), combined with \( m \cdot (k \cdot 1) = (mk) \cdot 1 \), which follows from the first by induction on \( m \).
:::

::: {#def-characteristic}
[Characteristic]

Let \( F \) be a field. If there is a **positive** integer \( n \) with \( n \cdot 1 = 0 \), the **characteristic** of \( F \) is the **smallest** such \( n \). If there is no such \( n \), the characteristic of \( F \) is \( 0 \).
:::

In words: count how many copies of \( 1 \) must be added to reach \( 0 \). If it never happens, the convention is to say "characteristic \( 0 \)", not "characteristic \( \infty \)": in that case the only integer \( m \ge 0 \) with \( m \cdot 1 = 0 \) is \( m = 0 \).

- **\( \nQ \), \( \nR \), \( \nC \)** have characteristic \( 0 \), because \( n \cdot 1 = n \ne 0 \) for every positive integer \( n \).
- **\( \nF_p \)** has characteristic \( p \): \( n \cdot [1] = [n] \), which is \( [0] \) exactly when \( p \) divides \( n \), and the smallest positive such \( n \) is \( p \).
- **\( \nF_2 \)** is the smallest case: characteristic \( 2 \), because \( 1 + 1 = 0 \).

Can a field have characteristic \( 6 \)? In \( \nZ/6\nZ \), six copies of \( [1] \) give \( [0] \), but \( \nZ/6\nZ \) is not a field. This is no accident.

::: {#thm-characteristic-prime}
[The Characteristic Is \( 0 \) or Prime]

The characteristic of a field is either \( 0 \) or a prime number.
:::

::: {.idea}
Suppose the characteristic \( n \) factors as \( rs \) with smaller factors. Then the elements \( r \cdot 1 \) and \( s \cdot 1 \) are non-zero, by minimality of \( n \), but their product is \( n \cdot 1 = 0 \). A field has no such pairs. This is the same argument as in @thm-zp-field-iff-prime, run inside an arbitrary field.
:::

::: {.proof}
Let \( F \) be a field of characteristic \( n \ne 0 \). Since the integer multiple \( 1 \cdot 1 = 0 + 1 = 1 \) is non-zero by (F7), we have \( n \ne 1 \), so \( n \ge 2 \). Suppose, for a contradiction, that \( n \) is not prime. Then \( n = rs \) with integers \( 1 < r < n \) and \( 1 < s < n \). By @lem-integer-multiples,
\[
(r \cdot 1)(s \cdot 1) = (rs) \cdot 1 = n \cdot 1 = 0.
\]
By @thm-field-basic-properties (f), \( r \cdot 1 = 0 \) or \( s \cdot 1 = 0 \). Either way we have a positive integer smaller than \( n \) whose multiple of \( 1 \) is \( 0 \), contradicting the minimality of \( n \). Hence \( n \) is prime.
:::

So the characteristic is \( 0 \), \( 2 \), \( 3 \), \( 5 \), \( 7 \), and so on. Together with @exr-fields-c2, this says a finite field always has prime characteristic.

::: {.warning}
In a field of characteristic \( 2 \), such as \( \nF_2 \), we have \( 1 + 1 = 0 \), so \( -1 = 1 \) and \( x = -x \) for **every** \( x \). The familiar argument "\( x = -x \), so \( 2x = 0 \), so \( x = 0 \)" divides by \( 2 = 1 + 1 \), which is \( 0 \) there. For example, in \( \nF_2 \) the element \( 1 \) satisfies \( 1 = -1 \) but is not \( 0 \). This is why later results, notably on symmetric bilinear forms in Chapter 14, carry the hypothesis "characteristic \( \ne 2 \)".
:::

With fields in hand, the stage for linear algebra is set: in Chapter 1, a vector space is defined **over a field** \( F \), and every result proved there holds at once for \( \nQ \), \( \nR \), \( \nC \), \( \nQ(\sqrt2) \) and \( \nF_p \).

## Exercises

### A. Check your understanding

::: {#exr-fields-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define what it means for a set \( F \) with two operations to be a field.
2. True or false: in every field, \( a^2 = 0 \) implies \( a = 0 \). Justify your answer.
3. True or false: \( \nZ/8\nZ \) is a field. Justify your answer.
4. True or false: in every field, \( 1 + 1 \ne 0 \). Justify your answer.
5. What are the characteristics of \( \nC \) and of \( \nF_7 \)?
6. The set \( \nN \) with the usual addition and multiplication is not a field. Name two axioms that fail, each with a witness.
:::
:::

::: {.solution}
(a) See @def-field: two operations satisfying (F1)–(F9), including \( 1 \ne 0 \).

(b) True. If \( a \cdot a = 0 \), then \( a = 0 \) or \( a = 0 \) by @thm-field-basic-properties (f).

(c) False. Since \( 8 = 2 \cdot 4 \) is not prime, \( \nZ/8\nZ \) is not a field by @thm-zp-field-iff-prime; concretely \( [2][4] = [0] \) with \( [2], [4] \ne [0] \).

(d) False. In \( \nF_2 \), \( 1 + 1 = 0 \).

(e) \( \nC \) has characteristic \( 0 \), and \( \nF_7 \) has characteristic \( 7 \) (see the examples after @def-characteristic).

(f) (F4) fails: \( 1 \in \nN \), but no \( b \in \nN \) has \( 1 + b = 0 \). (F8) fails: \( 2 \ne 0 \), but no \( b \in \nN \) has \( 2b = 1 \).
:::

### B. Practice

::: {#exr-fields-b1}
[B1: The Remaining Basic Properties]

Let \( F \) be a field and \( a, b, c \in F \). Using only the axioms and the parts of @thm-field-basic-properties proved in the text, prove:

::: {.enumerate options="label=(\alph*)"}
1. the element \( 1 \) in (F7) is unique;
2. if \( ab = ac \) and \( a \ne 0 \), then \( b = c \);
3. for \( a \ne 0 \), the inverse \( a^{-1} \) is unique;
4. \( (-1)a = -a \).
:::

*Hint: for (d), show that \( a + (-1)a = 0 \).*
:::

::: {.solution}
(a) Suppose \( 1 \) and \( 1' \) both satisfy (F7). Then, by (F7) for \( 1' \), (F6), and (F7) for \( 1 \), \( 1 = 1 \cdot 1' = 1' \cdot 1 = 1' \).

(b) Suppose \( ab = ac \) and \( a \ne 0 \). By (F8), \( a^{-1} \) exists, and multiplying both sides by it gives \( (ab)a^{-1} = (ac)a^{-1} \). By (F6) and (F5), \( (ab)a^{-1} = (ba)a^{-1} = b(aa^{-1}) = b \cdot 1 = b \), using (F8) and (F7) at the end. In the same way \( (ac)a^{-1} = c \). Hence \( b = c \).

(c) Suppose \( b \) and \( c \) both satisfy (F8) for \( a \ne 0 \): \( ab = 1 = ac \). By (b), \( b = c \).

(d) By (F7) and (F6), \( a = 1 \cdot a \). Therefore, using (F6) and (F9),
\[
a + (-1)a = 1 \cdot a + (-1)a = a \cdot 1 + a(-1) = a\big(1 + (-1)\big) = a \cdot 0 = 0,
\]
where the last two equalities use (F4) and @thm-field-basic-properties (d). So \( (-1)a \) satisfies (F4) for \( a \). By uniqueness of negatives (@thm-field-basic-properties (c)), \( (-1)a = -a \).
:::

::: {#exr-fields-b2}
[B2: Solving Equations in \( \nF_7 \)]

::: {.enumerate options="label=(\alph*)"}
1. Solve \( 3x + 5 = 2 \) in \( \nF_7 \).
2. Solve the system \( x + 2y = 3 \), \( 3x + y = 1 \) over \( \nF_7 \).
:::
:::

::: {.solution}
(a) Adding \( -5 \) to both sides gives \( 3x = 2 - 5 = -3 = 4 \) in \( \nF_7 \). Since \( 3 \cdot 5 = 15 = 1 \) in \( \nF_7 \), we have \( 3^{-1} = 5 \). Multiplying by \( 5 \), \( x = 20 = 6 \). Check: \( 3 \cdot 6 + 5 = 23 = 2 \) in \( \nF_7 \). Hence \( x = 6 \).

(b) Subtract \( 3 \) times the first equation from the second: \( (1 - 6)y = 1 - 9 \), that is, \( -5y = -8 \), or \( 2y = 6 \) in \( \nF_7 \). Since \( 2 \cdot 4 = 8 = 1 \), \( 2^{-1} = 4 \), so \( y = 24 = 3 \). Then \( x = 3 - 2y = 3 - 6 = -3 = 4 \). Check: \( 4 + 2 \cdot 3 = 10 = 3 \) and \( 3 \cdot 4 + 3 = 15 = 1 \) in \( \nF_7 \). Hence \( (x, y) = (4, 3) \).
:::

::: {#exr-fields-b3}
[B3: Which Are Fields?]

Determine which of the following are fields, with the stated operations. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \nZ/9\nZ \), with the operations of @exm-finite-fields.
2. \( \nQ(i) \coloneqq \{ a + bi : a, b \in \nQ \} \), with the operations of \( \nC \).
3. \( \{ a + bi : a, b \in \nZ \} \), with the operations of \( \nC \).
4. \( \nF_5 \).
:::
:::

::: {.solution}
(a) Not a field. Since \( 9 = 3 \cdot 3 \) is not prime, @thm-zp-field-iff-prime applies; concretely \( [3][3] = [0] \) with \( [3] \ne [0] \), which is impossible in a field by @thm-field-basic-properties (f).

(b) A field. Let \( x = a + bi \) and \( y = c + di \) with \( a, b, c, d \in \nQ \). Then \( x + y = (a + c) + (b + d)i \), \( xy = (ac - bd) + (ad + bc)i \) and \( -x = -a - bi \) have rational parts, and \( 0, 1 \in \nQ(i) \) with \( 1 \ne 0 \). The identities (F1), (F2), (F5), (F6), (F9) hold because they hold in \( \nC \) (@exm-fields). If \( x \ne 0 \), then \( a^2 + b^2 \) is a non-zero rational number, and by @prp-complex-inverse \( x^{-1} = \frac{a}{a^2 + b^2} - \frac{b}{a^2 + b^2} i \), which lies in \( \nQ(i) \). So (F8) holds.

(c) Not a field: (F8) fails for \( 2 \). Suppose \( u = a + bi \) with \( a, b \in \nZ \) satisfied \( 2u = 1 \). This is also an equation in the field \( \nC \), where \( \frac12 \) is an inverse of \( 2 \); by uniqueness of inverses in \( \nC \) (@thm-field-basic-properties (c)), \( u = \frac12 \). But \( \frac12 \) has real part \( \frac12 \notin \nZ \), a contradiction.

(d) A field, by @thm-zp-field-iff-prime, since \( 5 \) is prime.
:::

### C. Going deeper

::: {#exr-fields-c1}
[C1: A Field with Four Elements]

Let \( F = \{ a + b\alpha : a, b \in \nF_2 \} \), a set of four formal symbols \( 0, 1, \alpha, \beta \), where \( \beta \coloneqq 1 + \alpha \). Define
\[
\begin{aligned}
(a + b\alpha) + (c + d\alpha) &\coloneqq (a + c) + (b + d)\alpha, \\
(a + b\alpha)(c + d\alpha) &\coloneqq (ac + bd) + (ad + bc + bd)\alpha,
\end{aligned}
\]
with all coefficient arithmetic in \( \nF_2 \). (The product is what expanding gives if we replace \( \alpha^2 \) by \( \alpha + 1 \).)

::: {.enumerate options="label=(\alph*)"}
1. Write out the addition and multiplication tables of \( F \).
2. Prove that \( F \) is a field.
3. Explain why there is no bijection \( \varphi \colon F \to \nZ/4\nZ \) with \( \varphi(x + y) = \varphi(x) + \varphi(y) \) and \( \varphi(xy) = \varphi(x)\varphi(y) \) for all \( x, y \in F \). So this four-element field is not "\( \nZ/4\nZ \) in disguise".
:::

*Hint: for (c), look for a non-zero element of \( \nZ/4\nZ \) whose square is zero.*
:::

::: {.solution}
(a) Using the formulas, with \( 1 + 1 = 0 \) in \( \nF_2 \):
\[
\begin{array}{c|c c c c} + & 0 & 1 & \alpha & \beta \\
\hline
0 & 0 & 1 & \alpha & \beta \\
1 & 1 & 0 & \beta & \alpha \\
\alpha & \alpha & \beta & 0 & 1 \\
\beta & \beta & \alpha & 1 & 0
\end{array}
\qquad\qquad
\begin{array}{c|c c c c}
\cdot & 0 & 1 & \alpha & \beta \\
\hline
0 & 0 & 0 & 0 & 0 \\
1 & 0 & 1 & \alpha & \beta \\
\alpha & 0 & \alpha & \beta & 1 \\
\beta & 0 & \beta & 1 & \alpha
\end{array}
\]
For instance, \( \alpha \cdot \alpha = (0 + 1\alpha)(0 + 1\alpha) = (0 + 1) + (0 + 0 + 1)\alpha = 1 + \alpha = \beta \), and \( \alpha\beta = (0 + 1\alpha)(1 + 1\alpha) = (0 + 1) + (0 + 1 + 1)\alpha = 1 \).

(b) Let \( x = a + b\alpha \), \( y = c + d\alpha \), \( z = e + f\alpha \) with \( a, \dots, f \in \nF_2 \). Since \( \nF_2 \) is a field (@exm-finite-fields), we may compute with the coefficients using the rules of algebra.

*Addition.* It acts coordinate by coordinate, so (F1) and (F2) follow from the same laws in \( \nF_2 \), the element \( 0 = 0 + 0\alpha \) satisfies (F3), and \( -x = x \) satisfies (F4) because \( a + a = 0 \) and \( b + b = 0 \) in \( \nF_2 \).

*(F6).* The formula for \( xy \) is unchanged when \( (a, b) \) and \( (c, d) \) are swapped: \( ac + bd = ca + db \) and \( ad + bc + bd = cb + da + db \).

*(F7).* With \( 1 = 1 + 0\alpha \), \( x \cdot 1 = (a + 0) + (0 + b + 0)\alpha = x \), and \( 1 \ne 0 \) since the coefficients differ.

*(F9).* Since \( y + z = (c + e) + (d + f)\alpha \),
\[
x(y + z) = \big(a(c + e) + b(d + f)\big) + \big(a(d + f) + b(c + e) + b(d + f)\big)\alpha,
\]
and expanding the coefficients shows this is \( \big((ac + bd) + (ae + bf)\big) + \big((ad + bc + bd) + (af + be + bf)\big)\alpha = xy + xz \).

*(F5).* Write \( xy = g + h\alpha \) with \( g = ac + bd \), \( h = ad + bc + bd \). Then \( (xy)z = (ge + hf) + (gf + he + hf)\alpha \). Expanding,
\[
\begin{aligned}
ge + hf &= ace + adf + bcf + bde + bdf, \\
gf + he + hf &= acf + ade + adf + bce + bcf + bde,
\end{aligned}
\]
where in the second we used \( bdf + bdf = 0 \) in \( \nF_2 \). Similarly \( yz = k + l\alpha \) with \( k = ce + df \), \( l = cf + de + df \), and \( x(yz) = (ak + bl) + (al + bk + bl)\alpha \). Expanding gives \( ak + bl = ace + adf + bcf + bde + bdf \) and \( al + bk + bl = acf + ade + adf + bce + bcf + bde \), again using \( bdf + bdf = 0 \). Hence \( (xy)z = x(yz) \).

*(F8).* From the table, \( 1 \cdot 1 = 1 \), \( \alpha\beta = 1 \) and \( \beta\alpha = 1 \), so every non-zero element has an inverse.

This proves that \( F \) is a field.

(c) Suppose such a bijection \( \varphi \) existed. First, \( \varphi(0) = \varphi(0 + 0) = \varphi(0) + \varphi(0) \), so additive cancellation in \( \nZ/4\nZ \) (adding \( -\varphi(0) \), which only uses (F1)–(F4), valid there by @exm-finite-fields) gives \( \varphi(0) = [0] \). Since \( \varphi \) is surjective, there is \( x \in F \) with \( \varphi(x) = [2] \). As \( [2] \ne [0] = \varphi(0) \), we have \( x \ne 0 \). But
\[
\varphi(x \cdot x) = \varphi(x)\varphi(x) = [2][2] = [4] = [0] = \varphi(0),
\]
so \( x \cdot x = 0 \) because \( \varphi \) is injective. This contradicts @thm-field-basic-properties (f) in the field \( F \) (from (b)). Hence no such \( \varphi \) exists.
:::

::: {#exr-fields-c2}
[C2: Finite Fields Have Prime Characteristic]

::: {.enumerate options="label=(\alph*)"}
1. Let \( F \) be a finite field. Prove that the characteristic of \( F \) is a prime \( p \).
2. Let \( F \) be a field of characteristic \( p > 0 \). Prove that \( p \cdot a = 0 \) for every \( a \in F \).
:::

*Hint: for (a), the elements \( 1 \cdot 1, 2 \cdot 1, 3 \cdot 1, \dots \) cannot all be different.*
:::

::: {.solution}
(a) The elements \( m \cdot 1 \) for \( m = 1, 2, 3, \dots \) all lie in the finite set \( F \), so they cannot all be distinct. Hence there are positive integers \( k < m \) with \( m \cdot 1 = k \cdot 1 \). By @lem-integer-multiples, \( m \cdot 1 = k \cdot 1 + (m - k) \cdot 1 \), so \( k \cdot 1 + (m - k) \cdot 1 = k \cdot 1 + 0 \), and additive cancellation (@thm-field-basic-properties (b)) gives \( (m - k) \cdot 1 = 0 \) with \( m - k \ge 1 \). Therefore the characteristic of \( F \) is not \( 0 \). By @thm-characteristic-prime, it is a prime \( p \).

(b) Let \( a \in F \). By @lem-integer-multiples and the definition of characteristic, \( p \cdot a = (p \cdot 1)\, a = 0 \cdot a = 0 \), where the last step is @thm-field-basic-properties (d).
:::

::: {#exr-fields-c3}
[C3: The Frobenius Identity]

Let \( p \) be a prime.

::: {.enumerate options="label=(\alph*)"}
1. Let \( a, b \in \nZ \) with \( p \) dividing \( ab \). Prove that \( p \) divides \( a \) or \( p \) divides \( b \).
2. Deduce that \( p \) divides the binomial coefficient \( \binom{p}{k} \) for \( 0 < k < p \).
3. Let \( F \) be a field of characteristic \( p \). Prove that \( (x + y)^p = x^p + y^p \) for all \( x, y \in F \).
:::

You may use the binomial theorem \( (x + y)^n = \sum_{k=0}^{n} \binom{n}{k} \cdot (x^k y^{n-k}) \) in any field, with integer multiples as in @lem-integer-multiples; its inductive proof uses only the field axioms.

*Hint: for (a), use @lem-bezout-integers. For (b), use \( p! = \binom{p}{k}\, k!\, (p - k)! \).*
:::

::: {.solution}
(a) Suppose \( p \) does not divide \( a \). A positive integer dividing \( p \) is \( 1 \) or \( p \), so the only positive common divisor of \( a \) and \( p \) is \( 1 \). By @lem-bezout-integers there are \( x, y \in \nZ \) with \( ax + py = 1 \). Multiplying by \( b \), \( b = (ab)x + p(by) \). Both terms on the right are divisible by \( p \), the first because \( p \) divides \( ab \). Hence \( p \) divides \( b \).

(b) First, by (a) and induction on the number of factors, if \( p \) divides a product of integers then it divides one of the factors. The integers \( 1, 2, \dots, p - 1 \) are not divisible by \( p \), so \( p \) divides neither \( k! \) nor \( (p - k)! \) for \( 0 < k < p \), and hence, by (a) once more, not their product. Now \( p \) divides \( p! = \binom{p}{k} \cdot \big(k!\,(p - k)!\big) \). By (a), \( p \) divides \( \binom{p}{k} \).

(c) Let \( x, y \in F \). By the binomial theorem,
\[
(x + y)^p = x^p + y^p + \sum_{k=1}^{p-1} \binom{p}{k} \cdot (x^k y^{p-k}),
\]
since \( \binom{p}{0} = \binom{p}{p} = 1 \). Fix \( 0 < k < p \). By (b), \( \binom{p}{k} = pm \) for some \( m \in \nN \). By @lem-integer-multiples,
\[
\binom{p}{k} \cdot (x^k y^{p-k}) = \big((pm) \cdot 1\big)(x^k y^{p-k}) = (p \cdot 1)(m \cdot 1)(x^k y^{p-k}) = 0,
\]
because \( p \cdot 1 = 0 \) in characteristic \( p \) and \( 0 \) times anything is \( 0 \) (@thm-field-basic-properties (d)). So every middle term vanishes, and \( (x + y)^p = x^p + y^p \), as claimed.
:::
