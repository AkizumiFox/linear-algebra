# Irreducible Polynomials and Unique Factorization

Every integer \( n \ge 2 \) is a product of primes, and Chapter 0 remarked that the convention "\( 1 \) is not prime" is what makes such factorizations unique. Polynomials over a field behave the same way, with irreducible polynomials in the role of primes and non-zero constants in the role of \( \pm 1 \). This section defines irreducible polynomials, proves Euclid's lemma from the gcd machinery of the previous section, and proves that every non-constant polynomial factors into irreducibles in exactly one way. The catch is that "irreducible" depends on the field: the same polynomial may factor over \( \nR \) but not over \( \nQ \), or over \( \nF_5 \) but not over \( \nF_3 \). So we also collect tools for deciding irreducibility over specific fields: roots in low degree, the Rational Root Theorem, and Eisenstein's criterion. Throughout, \( F \) is a field.

## Irreducible polynomials

For integers, the building blocks are the primes: integers \( p \ge 2 \) whose only positive divisors are \( 1 \) and \( p \) (@def-divisibility-prime). To transplant this to \( F[x] \), recall from the first section that every non-zero constant divides every polynomial, and that multiplying by a non-zero constant changes nothing for divisibility. So the trivial divisors of \( p \) are the non-zero constants and the associates \( cp \). A building block should have no others.

*An irreducible polynomial is a non-constant polynomial that cannot be split into two factors of smaller degree.*

::: {#def-irreducible-polynomial}
[Irreducible Polynomial]

Let \( F \) be a field. A polynomial \( p \in F[x] \) is **irreducible over \( F \)** if

::: {.enumerate options="label=(\arabic*)"}
1. \( p \) is **non-constant**, that is, \( \deg p \ge 1 \); and
2. whenever \( p = gh \) with \( g, h \in F[x] \), **one of** \( g, h \) is a constant.
:::

A non-constant polynomial that is not irreducible is **reducible over \( F \)**.
:::

In words: condition (1) excludes \( 0 \) and the non-zero constants. Condition (2) says every factorization of \( p \) is trivial: one factor is a constant, which is non-zero because \( p \neq 0 \), and the other is then an associate of \( p \). The phrase **over \( F \)** is part of the notion, since \( g \) and \( h \) must lie in \( F[x] \).

Since degrees add (@thm-degree-of-product), a factorization \( p = gh \) with \( p \neq 0 \) has \( \deg g + \deg h = \deg p \). So \( g \) is constant exactly when \( \deg h = \deg p \). This gives a working form of the definition: **a non-constant \( p \) is reducible if and only if \( p = gh \) with \( 1 \le \deg g < \deg p \) and \( 1 \le \deg h < \deg p \).**

::: {#exm-irreducible-polynomials}
[First Irreducible and Reducible Polynomials]

::: {.enumerate options="label=(\alph*)"}
1. Show that every polynomial of degree \( 1 \) is irreducible over every field.
2. Show that the constants \( 0 \) and \( 2 \) are not irreducible over \( \nQ \).
3. Show that \( x^2 + x \) is reducible over every field, and that \( x^3 \) is reducible over every field.
:::
:::

::: {.solution}
(a) If \( \deg p = 1 \) and \( p = gh \), then \( \deg g + \deg h = 1 \) with both degrees in \( \nN \), so one of them is \( 0 \): one factor is a constant. Condition (1) holds since \( \deg p = 1 \). Hence \( p \) is irreducible, whatever the field. For example \( x \), \( 2x + 4 \) and \( x - \sqrt2 \) (over \( \nR \)) are irreducible.

(b) Both are constants, so condition (1) fails. They are the degenerate cases, and they matter: \( 2 \) divides everything in \( \nQ[x] \), like \( 1 \) among the integers, and it is not a building block.

(c) \( x^2 + x = x(x + 1) \) with both factors of degree \( 1 \), and \( x^3 = x \cdot x^2 \) with factors of degrees \( 1 \) and \( 2 \). In each case both factors are non-constant, so condition (2) fails.
:::

Why insist on "non-constant"? For the same reason \( 1 \) is not a prime. If non-zero constants were allowed as building blocks, factorizations could never be unique: \( x = 2 \cdot \tfrac12 x = 2 \cdot 3 \cdot \tfrac16 x = \cdots \) over \( \nQ \), with any number of constant factors. The factorization theorem below pulls out one constant in front and uses only non-constant, monic irreducibles.

For polynomials of degree \( 2 \) and \( 3 \), irreducibility is decided by roots alone.

::: {#thm-irreducible-deg-2-3}
[Irreducibility in Degree 2 and 3]

Let \( F \) be a field and \( p \in F[x] \).

::: {.enumerate options="label=(\alph*)"}
1. \( p \) has a factor of degree \( 1 \) in \( F[x] \) if and only if \( p \) has a root in \( F \). In particular, if \( \deg p \ge 2 \) and \( p \) has a root in \( F \), then \( p \) is reducible over \( F \).
2. If \( \deg p \in \{2, 3\} \), then \( p \) is irreducible over \( F \) if and only if \( p \) has **no** root in \( F \).
:::
:::

::: {.proof}
(a) \( (\Leftarrow) \) If \( c \in F \) is a root, then \( p = (x - c)q \) by @thm-remainder-theorem (b). \( (\Rightarrow) \) If \( p = (ax + b)q \) with \( a \neq 0 \), then \( c = -a^{-1} b \) satisfies \( ac + b = 0 \), so \( p(c) = 0 \cdot q(c) = 0 \) by @thm-evaluation-respects-operations. For the last sentence, if \( \deg p \ge 2 \) and \( p = (x - c)q \), then \( \deg q = \deg p - 1 \ge 1 \), so both factors are non-constant of degree less than \( \deg p \), and \( p \) is reducible.

(b) We prove both directions by contraposition. \( (\Rightarrow) \) If \( p \) has a root, it is reducible by (a), since \( \deg p \ge 2 \). \( (\Leftarrow) \) Suppose \( p \) is reducible. By the working form of the definition, \( p = gh \) with \( \deg g, \deg h \ge 1 \) and \( \deg g + \deg h = \deg p \in \{2, 3\} \). Two integers that are at least \( 1 \) and sum to \( 2 \) or \( 3 \) cannot both be at least \( 2 \), so one of \( g, h \) has degree \( 1 \). By (a), \( p \) has a root in \( F \). This proves the theorem.
:::

Now the standard examples, each checked with the theorem.

- **\( x^2 + 1 \) over \( \nR \) and over \( \nC \).** For real \( c \), \( c^2 + 1 \ge 1 > 0 \), so there is no real root, and \( x^2 + 1 \) is irreducible over \( \nR \) (and over \( \nQ \)). Over \( \nC \), \( x^2 + 1 = (x - i)(x + i) \) is reducible.
- **\( x^2 - 2 \) over \( \nQ \) and over \( \nR \).** A rational root would be a rational number with square \( 2 \), which does not exist (@thm-sqrt2-irrational). So \( x^2 - 2 \) is irreducible over \( \nQ \). Over \( \nR \), \( x^2 - 2 = (x - \sqrt2)(x + \sqrt2) \).
- **\( x^2 + x + 1 \) over \( \nF_2 \).** The values at \( 0 \) and \( 1 \) are \( 1 \) and \( 1 + 1 + 1 = 1 \). No root, so it is irreducible over \( \nF_2 \). It is the only irreducible polynomial of degree \( 2 \) over \( \nF_2 \) (Exercise B3).

The non-example by minimal change is \( x^2 + x \) over \( \nF_2 \): change the constant term of \( x^2 + x + 1 \) from \( 1 \) to \( 0 \), and \( 0 \) becomes a root, so \( x^2 + x = x(x + 1) \) is reducible. What fails is condition (2).

::: {.warning}
"No roots" implies "irreducible" **only in degrees 2 and 3**. The polynomial \( (x^2 + 1)^2 = x^4 + 2x^2 + 1 \) has no real root, since its values are at least \( 1 \), but it is reducible over \( \nR \): it is a product of two factors of degree \( 2 \). In degree \( 4 \) and higher, a polynomial can split into non-linear factors without having any root.
:::

::: {.check}
Over which of the fields \( \nQ \), \( \nQ(\sqrt2) \) (@exm-q-sqrt2-field), \( \nR \) is \( x^2 - 2 \) irreducible? Is \( x^2 + 1 \) irreducible over \( \nF_5 \)?
:::

::: {.solution}
Over \( \nQ \) only. The field \( \nQ(\sqrt2) \) contains \( \sqrt2 \), a root of \( x^2 - 2 \), so \( x^2 - 2 = (x - \sqrt2)(x + \sqrt2) \) is reducible there, and likewise over \( \nR \); over \( \nQ \) it is irreducible, as shown above. Over \( \nF_5 \), \( 2^2 + 1 = 5 = 0 \), so \( 2 \) is a root and \( x^2 + 1 \) is reducible by @thm-irreducible-deg-2-3: indeed \( x^2 + 1 = (x - 2)(x + 2) \) in \( \nF_5[x] \).
:::

## Euclid's lemma

What makes primes useful is not their definition but a property the definition implies: if a prime divides a product, it divides one of the factors. For polynomials this follows quickly from the previous section. The first step is that an irreducible polynomial has only two possible gcds with anything.

::: {#lem-irreducible-gcd}
[The gcd with an Irreducible Polynomial]

Let \( F \) be a field, \( p \in F[x] \) irreducible over \( F \), and \( f \in F[x] \). Then either \( p \mid f \) or \( \gcd(p, f) = 1 \).
:::

::: {.proof}
Let \( d = \gcd(p, f) \). Since \( p \neq 0 \), \( d \) is monic, and \( d \mid p \) by @thm-gcd-properties (a), say \( p = du \). Since \( p \) is irreducible, \( d \) or \( u \) is a constant. If \( d \) is a constant, then \( d = 1 \), since \( d \) is monic. If \( u \) is a constant, it is non-zero, and \( p = ud \) divides every multiple of \( d \); since \( d \mid f \) by @thm-gcd-properties (a), @prp-divisibility-properties (a) gives \( p \mid f \). This proves the lemma.
:::

::: {#thm-euclid-lemma-polynomials}
[Euclid's Lemma for Polynomials]

Let \( F \) be a field and \( p \in F[x] \) irreducible over \( F \). If \( q, r \in F[x] \) and \( p \mid qr \), then \( p \mid q \) or \( p \mid r \).
:::

::: {.proof}
Suppose \( p \nmid q \). By @lem-irreducible-gcd, \( \gcd(p, q) = 1 \). Since \( p \mid qr \), @thm-coprime-divides-product gives \( p \mid r \). This proves the theorem.
:::

The hypothesis "irreducible" is essential. The polynomial \( x^2 \) divides \( x \cdot x \) but divides neither factor; the lemma does not apply because \( x^2 = x \cdot x \) is reducible. Over \( \nF_2 \), \( x^2 + 1 = (x + 1)^2 \) divides \( (x + 1)(x + 1) \) but not \( x + 1 \), for the same reason.

For unique factorization we need the lemma for products of any length, and we need to know what "divides" means between two monic irreducibles.

::: {#cor-euclid-lemma-products}
[Euclid's Lemma for Several Factors]

Let \( F \) be a field and \( p \in F[x] \) irreducible over \( F \).

::: {.enumerate options="label=(\alph*)"}
1. If \( q_1, \dots, q_k \in F[x] \) with \( k \ge 1 \) and \( p \mid q_1 q_2 \cdots q_k \), then \( p \mid q_i \) for some \( i \).
2. If \( q \) is irreducible over \( F \), \( p \mid q \), and \( p, q \) are both monic, then \( p = q \).
:::
:::

::: {.proof}
(a) We use induction on \( k \). For \( k = 1 \) there is nothing to prove. Let \( k \ge 2 \) and assume the statement for \( k - 1 \) factors. Since \( p \mid (q_1 \cdots q_{k-1}) \, q_k \), @thm-euclid-lemma-polynomials gives \( p \mid q_1 \cdots q_{k-1} \) or \( p \mid q_k \). In the first case the induction hypothesis gives \( p \mid q_i \) for some \( i \le k - 1 \). Either way the statement holds for \( k \).

(b) Write \( q = pu \). Since \( q \) is irreducible, \( p \) or \( u \) is constant. But \( p \) is not constant, being irreducible, so \( u \) is a non-zero constant. Comparing leading coefficients of the monic polynomials \( q \) and \( p \) gives \( u = 1 \), so \( p = q \).
:::

## Unique factorization

Here is the theorem that Chapter 0's remark about primes was pointing towards, now for polynomials. The constant in front is forced to be the leading coefficient; the rest is a product of monic irreducibles, unique up to order.

::: {#thm-unique-factorization-polynomials}
[Unique Factorization in \( F\lbrack x\rbrack \)]

Let \( F \) be a field and \( f \in F[x] \) non-constant.

::: {.enumerate options="label=(\alph*)"}
1. **Existence.** There are a non-zero constant \( c \in F \), an integer \( k \ge 1 \), and monic polynomials \( p_1, \dots, p_k \in F[x] \), each irreducible over \( F \), with
\[
f = c \, p_1 p_2 \cdots p_k .
\]
2. **Uniqueness.** If also \( f = c' \, q_1 q_2 \cdots q_l \) with \( c' \in F \) non-zero, \( l \ge 1 \), and \( q_1, \dots, q_l \) monic and irreducible over \( F \), then \( c = c' \), \( k = l \), and after renumbering the \( q_j \) we have \( p_i = q_i \) for every \( i \).
:::

In both factorizations, the constant is the leading coefficient of \( f \).
:::

::: {.idea}
**Existence:** if \( f \) is irreducible, stop; otherwise split it into two factors of smaller degree and factor each of them, which is strong induction on the degree. **Uniqueness:** compare leading coefficients to get \( c = c' \). Then \( p_k \) divides \( q_1 \cdots q_l \), so by Euclid's lemma it equals some \( q_j \). Cancel it from both sides; the two shorter factorizations are equal by induction on the number of factors \( k \). The one thing to watch is that after canceling, the right-hand side must still have at least one factor.
:::

::: {.proof}
First a remark used in both parts. A product of monic polynomials is monic, by @thm-degree-of-product and induction on the number of factors. So if \( f = c \, p_1 \cdots p_k \) with the \( p_i \) monic, then the leading coefficient of \( f \) is \( c \cdot 1 = c \). This proves the final sentence of the theorem.

(a) We prove by strong induction on \( n \ge 1 \) (@thm-strong-induction with \( n_0 = 1 \)) that every \( f \) of degree \( n \) has a factorization as in (a). Let \( \deg f = n \), assume the statement for all degrees \( 1 \le m < n \), and let \( c \) be the leading coefficient of \( f \).

*Case 1: \( f \) is irreducible over \( F \).* Then \( f = c \, (c^{-1} f) \). The polynomial \( c^{-1} f \) is monic, and it is irreducible: it is non-constant, and if \( c^{-1} f = gh \), then \( f = (cg)h \), so \( cg \) or \( h \) is constant, hence \( g \) or \( h \) is constant. So \( k = 1 \), \( p_1 = c^{-1} f \) works.

*Case 2: \( f \) is reducible over \( F \).* By the working form of the definition, \( f = gh \) with \( 1 \le \deg g < n \) and \( 1 \le \deg h < n \). By the induction hypothesis, \( g = a \, p_1 \cdots p_s \) and \( h = b \, p_{s+1} \cdots p_{s+t} \) with \( a, b \) non-zero constants, \( s, t \ge 1 \), and all \( p_i \) monic irreducible. Then \( f = (ab) \, p_1 \cdots p_{s+t} \), with \( ab \neq 0 \) by @thm-field-basic-properties. This is a factorization as in (a), with \( k = s + t \).

(b) By the first remark, \( c \) and \( c' \) are both the leading coefficient of \( f \), so \( c = c' \). Multiplying by \( c^{-1} \), we get \( p_1 \cdots p_k = q_1 \cdots q_l \). So it suffices to prove, by induction on \( k \ge 1 \), the statement

> \( U(k) \): whenever \( p_1 \cdots p_k = q_1 \cdots q_l \) with \( l \ge 1 \) and all \( p_i, q_j \) monic and irreducible over \( F \), we have \( k = l \), and after renumbering the \( q_j \), \( p_i = q_i \) for every \( i \).

We first note: if a monic irreducible \( q \) equals a product \( r_1 \cdots r_m \) of \( m \ge 2 \) monic irreducibles, then \( q = r_1 \cdot (r_2 \cdots r_m) \) with both factors non-constant, since each \( r_i \) has degree at least \( 1 \); this contradicts the irreducibility of \( q \). So **a monic irreducible is never a product of two or more monic irreducibles.** \( (\ast) \)

*Base case \( k = 1 \).* Then \( p_1 = q_1 \cdots q_l \). By \( (\ast) \), \( l = 1 \), and so \( p_1 = q_1 \).

*Inductive step.* Let \( k \ge 2 \) and assume \( U(k - 1) \). Suppose \( p_1 \cdots p_k = q_1 \cdots q_l \). If \( l = 1 \), then \( q_1 = p_1 \cdots p_k \) with \( k \ge 2 \), which is impossible by \( (\ast) \). So \( l \ge 2 \). Now \( p_k \mid q_1 \cdots q_l \), so by @cor-euclid-lemma-products (a), \( p_k \mid q_j \) for some \( j \), and by @cor-euclid-lemma-products (b), \( p_k = q_j \). Renumber the \( q \)'s so that \( j = l \). Then
\[
(p_1 \cdots p_{k-1}) \, p_k = (q_1 \cdots q_{l-1}) \, p_k ,
\]
and since \( p_k \neq 0 \), @cor-polynomial-no-zero-divisors (2) lets us cancel it: \( p_1 \cdots p_{k-1} = q_1 \cdots q_{l-1} \), with \( k - 1 \ge 1 \) and \( l - 1 \ge 1 \) factors. By \( U(k - 1) \), \( k - 1 = l - 1 \), and after renumbering \( q_1, \dots, q_{l-1} \), \( p_i = q_i \) for \( i \le k - 1 \). Together with \( p_k = q_k \), this proves \( U(k) \).

By induction, \( U(k) \) holds for every \( k \ge 1 \), which proves (b).
:::

Grouping equal factors, every non-constant \( f \in F[x] \) can be written uniquely as
\[
f = c \, p_1^{e_1} p_2^{e_2} \cdots p_s^{e_s}
\]
with \( c \) the leading coefficient, \( p_1, \dots, p_s \) **distinct** monic irreducibles over \( F \), and exponents \( e_i \ge 1 \). The monic irreducible factors of the characteristic and minimal polynomials of an operator will organize the structure theory of Chapters 9 and 10.

::: {.warning}
Uniqueness needs the normalization "monic". Without it, constants can move between factors: over \( \nQ \), \( 2x^2 - 2 = (2x - 2)(x + 1) = (x - 1)(2x + 2) = (\tfrac12 x - \tfrac12)(4x + 4) \). All of these are "factorizations into irreducibles", and they differ only by associates. The theorem removes this freedom by collecting all constants into \( c \). Uniqueness also refers to a **fixed** field: over \( \nQ \) the factorization of \( x^2 - 2 \) is \( x^2 - 2 \) itself, and over \( \nR \) it is \( (x - \sqrt2)(x + \sqrt2) \).
:::

The next example shows the field dependence in one table.

::: {#exm-factor-x4-minus-1}
[Factoring \( x^4 - 1 \) Over Six Fields]

Factor \( x^4 - 1 \) into a constant times monic irreducibles over \( \nQ \), \( \nR \), \( \nC \), \( \nF_2 \), \( \nF_3 \), and, for contrast, \( \nF_5 \).
:::

::: {.solution}
Over every field, \( x^4 - 1 = (x^2 - 1)(x^2 + 1) = (x - 1)(x + 1)(x^2 + 1) \), by expanding. The factors \( x - 1 \) and \( x + 1 \) are irreducible by @exm-irreducible-polynomials (a). Everything depends on \( x^2 + 1 \), which by @thm-irreducible-deg-2-3 is irreducible exactly when it has no root in the field. The constant in front is always the leading coefficient \( 1 \).

- **\( \nQ \) and \( \nR \).** For real \( c \), \( c^2 + 1 \ge 1 \), so there is no root, and \( x^2 + 1 \) is irreducible.
- **\( \nC \).** \( x^2 + 1 = (x - i)(x + i) \).
- **\( \nF_2 \).** Here \( -1 = 1 \), so \( x - 1 = x + 1 \), and \( x^2 + 1 = (x + 1)^2 \) because \( 2x = 0 \). All four factors coincide.
- **\( \nF_3 \).** The values of \( x^2 + 1 \) at \( 0, 1, 2 \) are \( 1, 2, 5 = 2 \). No root, so \( x^2 + 1 \) is irreducible. Also \( x - 1 = x + 2 \).
- **\( \nF_5 \).** \( 2^2 + 1 = 5 = 0 \) and \( 3^2 + 1 = 10 = 0 \), so \( x^2 + 1 = (x - 2)(x - 3) = (x + 3)(x + 2) \).

| field | factorization of \( x^4 - 1 \) into monic irreducibles |
|---|---|
| \( \nQ \) | \( (x - 1)(x + 1)(x^2 + 1) \) |
| \( \nR \) | \( (x - 1)(x + 1)(x^2 + 1) \) |
| \( \nC \) | \( (x - 1)(x + 1)(x - i)(x + i) \) |
| \( \nF_2 \) | \( (x + 1)^4 \) |
| \( \nF_3 \) | \( (x + 1)(x + 2)(x^2 + 1) \) |
| \( \nF_5 \) | \( (x + 1)(x + 2)(x + 3)(x + 4) \) |

By @thm-unique-factorization-polynomials, each row is **the** factorization over that field, up to order. Notice that the numbers of irreducible factors are \( 3, 3, 4, 4, 3, 4 \), and that over \( \nF_2 \) a repeated factor appears although \( x^4 - 1 \) has no repeated factor over the other fields.
:::

## Tools over \( \nQ \): rational roots and Eisenstein's criterion

Over \( \nQ \), @thm-irreducible-deg-2-3 reduces irreducibility of a quadratic or cubic to the question of rational roots. There are infinitely many rational numbers to try, but for integer coefficients only finitely many candidates can work. We write \( \nZ[x] \) for the polynomials in \( \nQ[x] \) whose coefficients are all integers, as in the first section. Every rational number can be written as \( u/v \) with \( u \in \nZ \), \( v \ge 1 \), and the only positive integer dividing both \( u \) and \( v \) equal to \( 1 \): take \( v \ge 1 \) as small as possible, since a common divisor \( e > 1 \) would give the representation \( (u/e)/(v/e) \) with a smaller denominator. We say \( u/v \) is **in lowest terms**.

::: {#thm-rational-root}
[Rational Root Theorem]

Let \( f = a_n x^n + a_{n-1} x^{n-1} + \dots + a_0 \in \nZ[x] \) with \( n \ge 1 \) and \( a_n \neq 0 \). If \( u/v \in \nQ \) is in lowest terms and \( f(u/v) = 0 \), then \( u \mid a_0 \) and \( v \mid a_n \).
:::

::: {.idea}
Clear denominators: \( v^n f(u/v) = a_n u^n + a_{n-1} u^{n-1} v + \dots + a_0 v^n = 0 \). Every term except the last contains \( u \), so \( u \) divides \( a_0 v^n \); every term except the first contains \( v \), so \( v \) divides \( a_n u^n \). Since \( u \) and \( v \) share no factor, the powers of \( v \) can be stripped off one at a time, using Bézout for integers.
:::

::: {.proof}
Multiplying \( f(u/v) = 0 \) by \( v^n \) gives
\[
a_n u^n + a_{n-1} u^{n-1} v + \dots + a_1 u v^{n-1} + a_0 v^n = 0 .
\]
Hence \( a_0 v^n = -u \bigl( a_n u^{n-1} + a_{n-1} u^{n-2} v + \dots + a_1 v^{n-1} \bigr) \), so \( u \mid a_0 v^n \); and \( a_n u^n = -v \bigl( a_{n-1} u^{n-1} + \dots + a_0 v^{n-1} \bigr) \), so \( v \mid a_n u^n \).

Since \( v \ge 1 \) and the only positive common divisor of \( u \) and \( v \) is \( 1 \), @lem-bezout-integers gives integers \( s, t \) with \( us + vt = 1 \). If \( b \in \nZ \) and \( k \ge 1 \) with \( u \mid b v^k \), then
\[
b v^{k-1} = b v^{k-1}(us + vt) = u \, (b v^{k-1} s) + t \, (b v^k)
\]
is a sum of two multiples of \( u \), so \( u \mid b v^{k-1} \). Applying this \( n \) times to \( b = a_0 \) gives \( u \mid a_0 \). Similarly, if \( v \mid c u^k \) with \( k \ge 1 \), then \( c u^{k-1} = s \, (c u^k) + v \, (c u^{k-1} t) \), so \( v \mid c u^{k-1} \); applying this \( n \) times to \( c = a_n \) gives \( v \mid a_n \). This proves the theorem.
:::

A polynomial in \( \nQ[x] \) with fractional coefficients can first be multiplied by a common denominator; this does not change its roots or its irreducibility.

::: {#exm-cubic-irreducible-over-q}
[A Cubic That Is Irreducible Over \( \nQ \)]

Decide whether \( f = 2x^3 - 3x^2 + 4x - 1 \) is irreducible over \( \nQ \).
:::

::: {.solution}
By @thm-rational-root, a rational root \( u/v \) in lowest terms has \( u \mid -1 \) and \( v \mid 2 \) with \( v \ge 1 \). So \( u = \pm 1 \) and \( v \in \{1, 2\} \), and the candidates are \( 1, -1, \tfrac12, -\tfrac12 \). Evaluating,
\[
\begin{aligned}
f(1) &= 2, \qquad f(-1) = -10, \\
f\bigl(\tfrac12\bigr) &= \tfrac14 - \tfrac34 + 2 - 1 = \tfrac12, \\
f\bigl(-\tfrac12\bigr) &= -\tfrac14 - \tfrac34 - 2 - 1 = -4 .
\end{aligned}
\]
None is \( 0 \), so \( f \) has no rational root. Since \( \deg f = 3 \), @thm-irreducible-deg-2-3 shows that \( f \) is irreducible over \( \nQ \).
:::

Beyond degree \( 3 \), roots are not enough, as the warning after @thm-irreducible-deg-2-3 showed. One classical criterion handles many polynomials of any degree at once. It looks at divisibility of the coefficients by a prime.

::: {#thm-eisenstein-criterion}
[Eisenstein's Criterion]

Let \( f = a_n x^n + a_{n-1} x^{n-1} + \dots + a_0 \in \nZ[x] \) with \( n \ge 1 \), and let \( p \) be a prime such that

::: {.enumerate options="label=(\arabic*)"}
1. \( p \nmid a_n \);
2. \( p \mid a_i \) for every \( i = 0, 1, \dots, n - 1 \);
3. \( p^2 \nmid a_0 \).
:::

Then \( f \) is irreducible over \( \nQ \).
:::

The proof needs one more idea, **Gauss's lemma**: a polynomial with integer coefficients that factors over \( \nQ \) already factors over \( \nZ \), with factors of the same degrees. With it, one reduces the coefficients modulo \( p \) and compares. Exercise C2 of this section proves Gauss's lemma and then Eisenstein's criterion, step by step; no result of this chapter depends on the criterion. Here we only use it in examples.

::: {#exm-eisenstein}
[Irreducible Polynomials of Every Degree Over \( \nQ \)]

(a) Show that \( x^n - 2 \) is irreducible over \( \nQ \) for every \( n \ge 1 \). (b) Show that \( x^4 + 10x + 5 \) is irreducible over \( \nQ \).
:::

::: {.solution}
(a) Take \( p = 2 \). The leading coefficient \( 1 \) is not divisible by \( 2 \); the coefficients \( a_1, \dots, a_{n-1} \) are \( 0 \) and \( a_0 = -2 \), all divisible by \( 2 \); and \( 4 \nmid -2 \). By @thm-eisenstein-criterion, \( x^n - 2 \) is irreducible over \( \nQ \). So over \( \nQ \) there are irreducible polynomials of every degree. (Over \( \nR \), by contrast, \( x^n - 2 \) has the root \( \sqrt[n]{2} \) and is reducible for \( n \ge 2 \).)

(b) Take \( p = 5 \): \( 5 \nmid 1 \); \( 5 \) divides \( 0, 0, 10, 5 \); and \( 25 \nmid 5 \). So \( x^4 + 10x + 5 \) is irreducible over \( \nQ \). Roots alone could not have shown this, since a quartic may factor into two quadratics.
:::

Eisenstein's criterion is sufficient, not necessary. The polynomial \( x^2 + 1 \) is irreducible over \( \nQ \), but no prime divides its constant term \( 1 \), so condition (2) fails for every \( p \).

## Exercises

### A. Check your understanding

::: {#exr-unique-factorization-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define what it means for \( p \in F[x] \) to be irreducible over \( F \).
2. State the Unique Factorization Theorem in \( F[x] \).
3. Determine whether the following statement is true: "a polynomial in \( \nR[x] \) of degree at least \( 1 \) with no real root is irreducible over \( \nR \)." Justify your answer.
4. Is the constant \( 2 \) irreducible over \( \nQ \)? Is \( 2x + 4 \)?
5. Is \( x^2 + 1 \) irreducible over \( \nF_5 \)? Justify your answer.
6. Name a tool that reduces the irreducibility of a cubic in \( \nZ[x] \) over \( \nQ \) to finitely many evaluations.
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. \( p \) is irreducible over \( F \) if \( \deg p \ge 1 \) and, whenever \( p = gh \) with \( g, h \in F[x] \), one of \( g, h \) is a constant (@def-irreducible-polynomial).
2. Every non-constant \( f \in F[x] \) can be written as \( f = c \, p_1 \cdots p_k \) with \( c \in F \) non-zero and \( p_1, \dots, p_k \) monic and irreducible over \( F \); the constant \( c \) is the leading coefficient of \( f \), and the \( p_i \) are unique up to order (@thm-unique-factorization-polynomials).
3. False. \( (x^2 + 1)^2 \) has no real root, but it is the product of two non-constant factors, so it is reducible over \( \nR \). The statement is true in degrees \( 2 \) and \( 3 \) only (@thm-irreducible-deg-2-3).
4. No: \( 2 \) is constant, and irreducible polynomials are non-constant by definition. Yes: \( 2x + 4 \) has degree \( 1 \), so it is irreducible (@exm-irreducible-polynomials (a)).
5. No. In \( \nF_5 \), \( 2^2 + 1 = 0 \), so \( x^2 + 1 = (x - 2)(x + 2) \) is reducible by @thm-irreducible-deg-2-3.
6. The Rational Root Theorem (@thm-rational-root), combined with @thm-irreducible-deg-2-3.
:::
:::

### B. Practice

::: {#exr-unique-factorization-b1}
[B1: Irreducible or Not?]

Determine whether each polynomial is irreducible over each of the given fields. Justify your answers.

::: {.enumerate options="label=(\alph*)"}
1. \( x^2 + 2 \) over \( \nQ \), \( \nR \), \( \nF_2 \) and \( \nF_3 \).
2. \( x^3 + x + 1 \) over \( \nF_2 \) and over \( \nF_3 \).
3. \( x^3 - 3x - 1 \) over \( \nQ \).
4. \( x^4 + 4 \) over \( \nQ \).
5. \( x^5 - 6x + 3 \) over \( \nQ \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Over \( \nQ \) and \( \nR \): for real \( c \), \( c^2 + 2 \ge 2 > 0 \), so there is no root, and \( x^2 + 2 \) is irreducible by @thm-irreducible-deg-2-3. Over \( \nF_2 \): \( 2 = 0 \), so \( x^2 + 2 = x \cdot x \) is reducible. Over \( \nF_3 \): \( 2 = -1 \), so \( x^2 + 2 = x^2 - 1 = (x - 1)(x + 1) \) is reducible.
2. Over \( \nF_2 \): the values at \( 0 \) and \( 1 \) are \( 1 \) and \( 3 = 1 \), so there is no root, and the cubic is irreducible by @thm-irreducible-deg-2-3. Over \( \nF_3 \): the value at \( 1 \) is \( 3 = 0 \), so it is reducible; indeed \( x^3 + x + 1 = (x - 1)(x^2 + x + 2) \) in \( \nF_3[x] \), as expanding shows: \( x^3 + x^2 + 2x - x^2 - x - 2 = x^3 + x - 2 = x^3 + x + 1 \).
3. By @thm-rational-root, a rational root \( u/v \) in lowest terms has \( u \mid -1 \) and \( v \mid 1 \), so it is \( 1 \) or \( -1 \). The values are \( 1 - 3 - 1 = -3 \) and \( -1 + 3 - 1 = 1 \). No rational root, so the cubic is irreducible over \( \nQ \) by @thm-irreducible-deg-2-3.
4. Reducible, although it has no rational root (its values are at least \( 4 \)): expanding, \( (x^2 + 2x + 2)(x^2 - 2x + 2) = x^4 - 4x^2 + 4 + 4x^2 = x^4 + 4 \). This is the warning after @thm-irreducible-deg-2-3 in action.
5. Irreducible by @thm-eisenstein-criterion with \( p = 3 \): \( 3 \nmid 1 \); \( 3 \) divides the coefficients \( 0, 0, 0, -6, 3 \) of \( x^4, x^3, x^2, x, 1 \); and \( 9 \nmid 3 \).
:::
:::

::: {#exr-unique-factorization-b2}
[B2: Factoring \( x^6 - 1 \) Over \( \nQ \)]

Factor \( x^6 - 1 \) into monic irreducible polynomials over \( \nQ \), and justify that each factor is irreducible. Hence find its factorization into monic irreducibles over \( \nF_2 \) as well. Is it obtained by reducing the coefficients of each rational factor modulo \( 2 \)? Explain why, in general, this has to be checked rather than assumed.
:::

::: {.solution}
Using \( x^6 - 1 = (x^3 - 1)(x^3 + 1) \) and @exr-division-b2 (with \( c = 1 \) and \( c = -1 \)),
\[
x^6 - 1 = (x - 1)(x^2 + x + 1)(x + 1)(x^2 - x + 1) ,
\]
which one checks by expanding: \( (x - 1)(x^2 + x + 1) = x^3 - 1 \) and \( (x + 1)(x^2 - x + 1) = x^3 + 1 \). The linear factors are irreducible. For the quadratics, \( c^2 \pm c + 1 = (c \pm \tfrac12)^2 + \tfrac34 > 0 \) for real \( c \), so they have no rational root and are irreducible by @thm-irreducible-deg-2-3. By @thm-unique-factorization-polynomials this is the factorization over \( \nQ \).

Over \( \nF_2 \), reducing coefficients gives \( (x + 1)(x^2 + x + 1)(x + 1)(x^2 + x + 1) \), since \( -1 = 1 \). Here \( x + 1 \) is irreducible and \( x^2 + x + 1 \) is irreducible over \( \nF_2 \) (it has no root), so the factorization over \( \nF_2 \) is \( (x + 1)^2 (x^2 + x + 1)^2 \). So yes, in this case the factorization is obtained by reduction, but only because the reduced factors happen to stay irreducible, and that has to be checked: two distinct rational factors, \( x - 1 \) and \( x + 1 \), became equal, and in general a factor that is irreducible over \( \nQ \) may become reducible after reduction, as \( x^2 + 1 \) does over \( \nF_2 \) in @exm-factor-x4-minus-1.
:::

::: {#exr-unique-factorization-b3}
[B3: Small Irreducibles Over \( \nF_2 \)]

List all irreducible polynomials over \( \nF_2 \) of degree at most \( 3 \). Justify that your list is complete.

*Hint: a polynomial over \( \nF_2 \) has the root \( 0 \) exactly when its constant term is \( 0 \), and the root \( 1 \) exactly when its number of non-zero terms is even.*
:::

::: {.solution}
Every non-zero polynomial over \( \nF_2 \) is monic, since its leading coefficient is \( 1 \). For \( f = \sum a_k x^k \), \( f(0) = a_0 \) and \( f(1) = \sum a_k \), which is \( 0 \) exactly when the number of non-zero coefficients is even.

*Degree 1:* \( x \) and \( x + 1 \), both irreducible (@exm-irreducible-polynomials (a)).

*Degrees 2 and 3:* by @thm-irreducible-deg-2-3, \( f \) is irreducible exactly when \( f(0) = 1 \) and \( f(1) = 1 \), that is, the constant term is \( 1 \) and the number of non-zero terms is odd. In degree \( 2 \), the polynomials with constant term \( 1 \) are \( x^2 + 1 \) (two terms) and \( x^2 + x + 1 \) (three terms), so only \( x^2 + x + 1 \) is irreducible. In degree \( 3 \), they are \( x^3 + 1 \) (two terms), \( x^3 + x + 1 \) and \( x^3 + x^2 + 1 \) (three terms), and \( x^3 + x^2 + x + 1 \) (four terms). So the irreducible ones are \( x^3 + x + 1 \) and \( x^3 + x^2 + 1 \).

Hence the complete list is \( x \), \( x + 1 \), \( x^2 + x + 1 \), \( x^3 + x + 1 \), \( x^3 + x^2 + 1 \).
:::

### C. Going deeper

::: {#exr-unique-factorization-c1}
[C1: Infinitely Many Irreducibles]

Let \( F \) be any field.

::: {.enumerate options="label=(\alph*)"}
1. Prove that there are infinitely many monic irreducible polynomials over \( F \).
2. Deduce that for every prime \( p \) and every \( N \in \nN \), there is an irreducible polynomial over \( \nF_p \) of degree greater than \( N \).
3. Explain why (a) is immediate when \( F \) is infinite, and use @exr-unique-factorization-b3 to name an irreducible polynomial of degree \( 3 \) over \( \nF_2 \).
:::

*Hint for (a): imitate the proof that there are infinitely many primes (@thm-infinitely-many-primes).*
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. Suppose, for a contradiction, that \( p_1, \dots, p_k \) are all the monic irreducible polynomials over \( F \). The list is non-empty, since \( x \) is monic and irreducible. Let \( f = p_1 p_2 \cdots p_k + 1 \). Each \( p_i \) has degree at least \( 1 \), so \( \deg(p_1 \cdots p_k) \ge 1 \) by @thm-degree-of-product, and \( f \) is non-constant by @thm-degree-of-sum. By @thm-unique-factorization-polynomials (a), \( f \) has a monic irreducible factor, which must be some \( p_j \). Then \( p_j \mid f \) and \( p_j \mid p_1 \cdots p_k \), so \( p_j \mid f - p_1 \cdots p_k = 1 \) by @prp-divisibility-properties (b). By @prp-divisibility-properties (c), \( \deg p_j \le \deg 1 = 0 \), contradicting \( \deg p_j \ge 1 \). Hence there are infinitely many monic irreducibles.
2. A monic polynomial of degree \( n \) over \( \nF_p \) is determined by its \( n \) lower coefficients, so there are exactly \( p^n \) of them, and there are \( 1 + p + \dots + p^N \) monic polynomials of degree at most \( N \), a finite number. By (a), infinitely many monic irreducibles exist, so some of them have degree greater than \( N \).
3. If \( F \) is infinite, the polynomials \( x - c \) for \( c \in F \) are infinitely many distinct monic polynomials of degree \( 1 \), all irreducible by @exm-irreducible-polynomials (a). Over a finite field there are only finitely many polynomials of degree \( 1 \), so the content of (a) is that irreducibles of higher and higher degree keep appearing. Over \( \nF_2 \), for example, \( x^3 + x + 1 \) is irreducible of degree \( 3 \) by @exr-unique-factorization-b3.
:::
:::

::: {#exr-unique-factorization-c2}
[C2: Gauss's Lemma and Eisenstein's Criterion]

Let \( \nZ[x] \) be as in @thm-rational-root, and let \( p \) be a prime. For \( g = \sum b_i x^i \in \nZ[x] \), define its **reduction modulo \( p \)** as \( \bar g = \sum [b_i] x^i \in \nF_p[x] \), where \( [b] \) is the class of \( b \) in \( \nF_p = \nZ/p\nZ \) (@exm-finite-fields).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \overline{g + h} = \bar g + \bar h \) and \( \overline{gh} = \bar g \, \bar h \) for all \( g, h \in \nZ[x] \), and that \( \deg \bar g \le \deg g \).
2. Let \( g, h \in \nZ[x] \), and suppose \( p \) divides every coefficient of \( gh \). Prove that \( p \) divides every coefficient of \( g \) or every coefficient of \( h \).
3. **(Gauss's lemma.)** Let \( f \in \nZ[x] \), and suppose \( f = gh \) with \( g, h \in \nQ[x] \). Prove that there is a non-zero \( \lambda \in \nQ \) with \( \lambda g \in \nZ[x] \) and \( \lambda^{-1} h \in \nZ[x] \).
4. Let \( F \) be a field, \( c \in F \) non-zero, \( n \in \nN \), and \( u, v \in F[x] \) with \( uv = c x^n \). Prove that \( u = \beta x^s \) and \( v = \gamma x^t \) for some non-zero \( \beta, \gamma \in F \) and \( s, t \in \nN \).
5. Prove @thm-eisenstein-criterion.
:::

*Hint for (c): among all ways of writing \( kf = (\alpha g)(\beta h) \) with \( \alpha, \beta \in \nQ \), \( \alpha\beta = k \) a positive integer and \( \alpha g, \beta h \in \nZ[x] \), take \( k \) as small as possible. Hint for (e): suppose \( f = gh \) with \( g, h \) non-constant, use (c), and reduce modulo \( p \).*
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. By @exm-finite-fields, \( [a] + [b] = [a + b] \) and \( [a][b] = [ab] \). Let \( g = \sum b_i x^i \) and \( h = \sum c_i x^i \). The coefficient of \( x^k \) in \( g + h \) is \( b_k + c_k \), whose class is \( [b_k] + [c_k] \), the coefficient of \( x^k \) in \( \bar g + \bar h \). The coefficient of \( x^k \) in \( gh \) is \( \sum_{i + j = k} b_i c_j \), whose class is \( \sum_{i + j = k} [b_i][c_j] \), the coefficient of \( x^k \) in \( \bar g \, \bar h \) (@def-polynomial-ring). Finally, if \( b_i = 0 \) then \( [b_i] = 0 \), so \( \bar g \) has no non-zero coefficient beyond position \( \deg g \).
2. The hypothesis says \( \overline{gh} = 0 \). By (a), \( \bar g \, \bar h = 0 \) in \( \nF_p[x] \). Since \( p \) is prime, \( \nF_p \) is a field (@thm-zp-field-iff-prime), so @cor-polynomial-no-zero-divisors gives \( \bar g = 0 \) or \( \bar h = 0 \). That is, \( p \) divides every coefficient of \( g \) or every coefficient of \( h \).
3. Choose positive integers \( m, n \) with \( mg \in \nZ[x] \) and \( nh \in \nZ[x] \), for instance the products of the denominators of the coefficients. Let \( K \) be the set of positive integers \( k \) for which there are \( \alpha, \beta \in \nQ \) with \( \alpha\beta = k \), \( \alpha g \in \nZ[x] \) and \( \beta h \in \nZ[x] \). Then \( mn \in K \), so by @thm-well-ordering \( K \) has a least element \( k \), with corresponding \( \alpha, \beta \). Suppose \( k > 1 \). By @prp-prime-factor, some prime \( q \) divides \( k \). Now \( (\alpha g)(\beta h) = \alpha\beta \, gh = kf \), and every coefficient of \( kf \) is divisible by \( q \). By (b) with the prime \( q \), \( q \) divides every coefficient of \( \alpha g \) or every coefficient of \( \beta h \); say the first (the other case is symmetric). Then \( (\alpha/q) g \in \nZ[x] \), \( \beta h \in \nZ[x] \), and \( (\alpha/q)\beta = k/q \) is a positive integer smaller than \( k \), which lies in \( K \). This contradicts the minimality of \( k \). Hence \( k = 1 \), so \( \beta = \alpha^{-1} \), and \( \lambda = \alpha \) works.
4. Since \( uv \neq 0 \), both \( u, v \) are non-zero. Write \( u = \sum u_i x^i \), \( v = \sum v_j x^j \), let \( i_0 \) and \( j_0 \) be the smallest indices with \( u_{i_0} \neq 0 \) and \( v_{j_0} \neq 0 \), and let \( s = \deg u \), \( t = \deg v \). The coefficient of \( x^{i_0 + j_0} \) in \( uv \) is \( \sum_{i + j = i_0 + j_0} u_i v_j \). A term with \( i < i_0 \) has \( u_i = 0 \), and a term with \( i > i_0 \) has \( j < j_0 \), so \( v_j = 0 \). So this coefficient is \( u_{i_0} v_{j_0} \neq 0 \). The only non-zero coefficient of \( c x^n \) is at \( x^n \), so \( i_0 + j_0 = n \). By @thm-degree-of-product, also \( s + t = n \). Since \( i_0 \le s \) and \( j_0 \le t \), this forces \( i_0 = s \) and \( j_0 = t \). So \( u \) has exactly one non-zero coefficient, \( u = u_s x^s \), and likewise \( v = v_t x^t \).
5. Suppose \( f \) is reducible over \( \nQ \): \( f = gh \) with \( g, h \in \nQ[x] \), \( \deg g = s \ge 1 \), \( \deg h = t \ge 1 \), and \( s + t = n \). By (c), replacing \( g, h \) by \( \lambda g, \lambda^{-1} h \) (which have the same degrees), we may assume \( g, h \in \nZ[x] \). Write \( g_0, h_0 \) for their constant coefficients, so \( a_0 = g_0 h_0 \). Reduce modulo \( p \). By conditions (1) and (2), \( \bar f = [a_n] x^n \) with \( [a_n] \neq 0 \). By (a), \( \bar g \, \bar h = [a_n] x^n \), so by (d), \( \bar g = \beta x^{s'} \) and \( \bar h = \gamma x^{t'} \) with \( \beta, \gamma \neq 0 \). By @thm-degree-of-product, \( s' + t' = n = s + t \), while \( s' \le s \) and \( t' \le t \) by (a). Hence \( s' = s \ge 1 \) and \( t' = t \ge 1 \). So the constant coefficients of \( \bar g \) and \( \bar h \) are \( 0 \), that is, \( p \mid g_0 \) and \( p \mid h_0 \). Then \( p^2 \mid g_0 h_0 = a_0 \), contradicting condition (3). Therefore \( f \) is irreducible over \( \nQ \); it is non-constant since \( n \ge 1 \).
:::
:::
