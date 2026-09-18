# Permutations and Sign

An alternating form changes sign when two of its arguments are swapped (@thm-alternating-properties). To compare \( f(\v_3, \v_1, \v_2) \) with \( f(\v_1, \v_2, \v_3) \), we reach one list from the other by swaps and collect a factor \( -1 \) per swap. But the same rearrangement can be reached by different sequences of swaps, and Chapter 0 showed that even their number is not unique. If one route used an even number of swaps and another an odd number, we would get \( f(\v_1, \v_2, \v_3) = -f(\v_1, \v_2, \v_3) \) for every alternating form, which is absurd for signed volume. This section rules that out. It attaches to each permutation a sign defined without any choices, proves that the sign is multiplicative, and deduces that the parity of the number of transpositions is well defined, as Chapter 0 promised.

## Permutations, recalled

Recall from Chapter 0 that \( S_n \) is the group of bijections \( \{1, \dots, n\} \to \{1, \dots, n\} \), with \( n! \) elements. A permutation can be written in two-line notation, with \( \sigma(i) \) below \( i \), or as a product of cycles. The product \( \sigma\tau \) is the composition \( \sigma \circ \tau \): **first \( \tau \), then \( \sigma \)**, so products of cycles are read from right to left (@exm-cycle-notation). A transposition \( (i\ j) \) swaps \( i \) and \( j \) and fixes everything else, and for \( n \ge 2 \) every permutation is a product of transpositions (@thm-transpositions-generate). The product is far from unique, since
\[
  (1\ 2\ 3) = (1\ 3)(1\ 2) = (1\ 2)(2\ 3) = (1\ 3)(1\ 2)(1\ 2)(1\ 2).
\]
Here the numbers of transpositions are \( 2, 2, 4 \), all even. The goal is to show this is no accident.

Why can we not simply **define** the sign of \( \sigma \) as \( (-1)^r \), where \( \sigma \) is a product of \( r \) transpositions? Because that definition depends on a choice of product, and we would have to prove that every choice gives the same answer. That is the statement we are trying to prove. We need a definition that involves no choice at all.

## Inversions and the sign

To measure how much a permutation scrambles \( 1, 2, \dots, n \), look at the bottom row \( \sigma(1), \sigma(2), \dots, \sigma(n) \) of its two-line notation and count the pairs of entries that are in the wrong order. A sorted row has none, and each swap of two neighboring entries changes the count by exactly one. So the count is a natural candidate for tracking the parity of swaps.

*The sign of a permutation records whether it puts an even or an odd number of pairs out of order.*

::: {#def-inversion}
[Inversion]

Let \( \sigma \in S_n \). An **inversion** of \( \sigma \) is a pair \( (i, j) \) of positions with \( 1 \le i < j \le n \) **and** \( \sigma(i) > \sigma(j) \). We write \( \operatorname{inv}(\sigma) \) for the number of inversions of \( \sigma \).
:::

::: {#def-sign-permutation}
[Sign of a Permutation]

The **sign** of \( \sigma \in S_n \) is
\[
  \sgn \sigma = (-1)^{\operatorname{inv}(\sigma)} \in \{1, -1\}.
\]
The permutation \( \sigma \) is **even** if \( \sgn \sigma = 1 \) and **odd** if \( \sgn \sigma = -1 \).
:::

In words: an inversion is a pair of positions whose order \( \sigma \) **reverses**. The condition \( i < j \) makes each pair of positions count once, and \( \sigma(i) > \sigma(j) \) says the values come out in the opposite order. Since \( \operatorname{inv}(\sigma) \) is the size of a subset of the finite set of pairs \( i < j \), it is a well-defined integer between \( 0 \) and \( n(n-1)/2 \), and there is nothing to choose. That is the whole reason for this definition.

**The identity.** Its bottom row is sorted, so \( \operatorname{inv}(\id) = 0 \) and \( \id \) is even. In \( S_1 = \{\id\} \) this is the only permutation, with sign \( 1 \). The degenerate case matters: the identity is the empty product of transpositions, and its sign \( 1 = (-1)^0 \) is what a product of \( 0 \) swaps should give.

**All of \( S_3 \).** Here is each permutation with its bottom row and inversions.

| \( \sigma \) | \( \id \) | \( (1\,2) \) | \( (2\,3) \) | \( (1\,3) \) | \( (1\,2\,3) \) | \( (1\,3\,2) \) |
|---|---|---|---|---|---|---|
| bottom row | \( 1\,2\,3 \) | \( 2\,1\,3 \) | \( 1\,3\,2 \) | \( 3\,2\,1 \) | \( 2\,3\,1 \) | \( 3\,1\,2 \) |
| inversions | none | \( (1,2) \) | \( (2,3) \) | \( (1,2), (1,3), (2,3) \) | \( (1,3), (2,3) \) | \( (1,2), (1,3) \) |
| \( \sgn \) | \( 1 \) | \( -1 \) | \( -1 \) | \( -1 \) | \( 1 \) | \( 1 \) |

For \( (1\ 2\ 3) \), the bottom row is \( \sigma(1), \sigma(2), \sigma(3) = 2, 3, 1 \), and the out-of-order pairs of positions are \( (1, 3) \), since \( 2 > 1 \), and \( (2, 3) \), since \( 3 > 1 \).

Two things stand out. The three transpositions are odd, although \( (1\ 3) \) has three inversions, not one. And the two \( 3 \)-cycles are even, consistent with \( (1\ 2\ 3) = (1\ 3)(1\ 2) \) being a product of two transpositions.

**Why all pairs, not just neighbors.** A tempting shortcut counts only **adjacent** positions \( (i, i + 1) \) with \( \sigma(i) > \sigma(i + 1) \). For \( (1\ 3) \), with bottom row \( 3, 2, 1 \), this count is \( 2 \), which would make \( (1\ 3) \) "even". But \( (1\ 3) = (1\ 2)(2\ 3)(1\ 2) \), as one checks by following \( 1 \mapsto 2 \mapsto 3 \mapsto 3 \), \( 2 \mapsto 1 \mapsto 1 \mapsto 2 \), \( 3 \mapsto 3 \mapsto 2 \mapsto 1 \), and each factor has adjacent count \( 1 \). A count that is to be multiplicative must give \( (-1)^3 = -1 \) here, so the adjacent count is the wrong one.

::: {.check}
Find \( \sgn (1\ 4) \) in \( S_4 \) by counting inversions.
:::

::: {.solution}
The bottom row is \( 4, 2, 3, 1 \). The pairs of positions in the wrong order are \( (1, 2), (1, 3), (1, 4) \), since \( 4 \) is larger than everything after it, and \( (2, 4), (3, 4) \), since \( 2 > 1 \) and \( 3 > 1 \). The pair \( (2, 3) \) is in order. So \( \operatorname{inv}(1\ 4) = 5 \) and \( \sgn (1\ 4) = -1 \).
:::

## The sign is multiplicative

The key property is that signs multiply when permutations are composed.

::: {#thm-sign-multiplicative}
[The Sign Is Multiplicative]

For all \( \sigma, \tau \in S_n \),
\[
  \sgn(\sigma\tau) = \sgn \sigma \cdot \sgn \tau .
\]
:::

::: {.idea}
Count inversions one pair at a time, and record each pair as \( +1 \) (order kept) or \( -1 \) (order reversed). The sign is the product of these \( \pm1 \)'s. Applying \( \tau \) and then \( \sigma \) moves a pair of positions \( \{i, j\} \) to \( \{\tau(i), \tau(j)\} \) and then to \( \{\sigma\tau(i), \sigma\tau(j)\} \). The order is reversed overall exactly when it is reversed at one of the two stages but not both, which is multiplication of \( \pm1 \)'s. Finally, as \( \{i, j\} \) runs over all pairs, so does \( \{\tau(i), \tau(j)\} \), so the contributions of \( \sigma \) multiply to \( \sgn \sigma \), just in a different order.
:::

::: {.proof}
For a non-zero integer \( m \) let \( s(m) = 1 \) if \( m > 0 \) and \( s(m) = -1 \) if \( m < 0 \). Then \( s(mm') = s(m)s(m') \) for non-zero integers \( m, m' \), by the sign rules for products of integers.

Let \( \mathcal{P} \) be the set of \( 2 \)-element subsets \( \{i, j\} \) of \( \{1, \dots, n\} \). For \( \rho \in S_n \) and \( \{i, j\} \in \mathcal{P} \), define
\[
  \varepsilon_\rho(\{i, j\}) = s\bigl((\rho(i) - \rho(j))(i - j)\bigr).
\]
This is defined: \( i \neq j \) and \( \rho(i) \neq \rho(j) \) since \( \rho \) is injective, so the product is non-zero; and exchanging the names \( i \) and \( j \) negates both factors, so the product does not depend on the order in which the subset is written. If \( i < j \), then \( i - j < 0 \), so \( \varepsilon_\rho(\{i, j\}) = -1 \) exactly when \( \rho(i) > \rho(j) \), that is, when \( (i, j) \) is an inversion of \( \rho \). Hence, by @def-sign-permutation,
\[
  \sgn \rho = \prod_{P \in \mathcal{P}} \varepsilon_\rho(P). \tag{1}
\]

Now let \( \{i, j\} \in \mathcal{P} \). Since \( \tau(i) \neq \tau(j) \), we have \( (\tau(i) - \tau(j))^2 > 0 \). Multiplying inside \( s \) by this positive integer does not change the value, so
\[
  \begin{aligned}
  \varepsilon_{\sigma\tau}(\{i, j\}) &= s\Bigl(\bigl(\sigma(\tau(i)) - \sigma(\tau(j))\bigr)\bigl(\tau(i) - \tau(j)\bigr) \cdot \bigl(\tau(i) - \tau(j)\bigr)(i - j)\Bigr) \\
  &= \varepsilon_\sigma(\{\tau(i), \tau(j)\})\ \varepsilon_\tau(\{i, j\}).
  \end{aligned}
\]
Let \( \hat\tau \colon \mathcal{P} \to \mathcal{P} \), \( \{i, j\} \mapsto \{\tau(i), \tau(j)\} \); the image has two elements because \( \tau \) is injective. The same construction with \( \tau^{-1} \) gives an inverse function, so \( \hat\tau \) is a bijection (@thm-bijective-iff-invertible). Taking the product over all \( P \in \mathcal{P} \) and using (1) three times,
\[
  \sgn(\sigma\tau) = \prod_{P \in \mathcal{P}} \varepsilon_\sigma(\hat\tau(P)) \cdot \prod_{P \in \mathcal{P}} \varepsilon_\tau(P) = \prod_{Q \in \mathcal{P}} \varepsilon_\sigma(Q) \cdot \sgn \tau = \sgn \sigma \cdot \sgn \tau,
\]
where the second equality substitutes \( Q = \hat\tau(P) \), which runs over \( \mathcal{P} \) exactly once because \( \hat\tau \) is a bijection, and reorders the finite product of integers. This proves the theorem.
:::

By induction on the number of factors, \( \sgn(\sigma_1 \sigma_2 \cdots \sigma_r) = \sgn \sigma_1 \cdots \sgn \sigma_r \). In the language of Chapter 0, the set \( \{1, -1\} \) is a group under multiplication (it contains \( 1 \), and it is closed under products and inverses, since \( (-1)^{-1} = -1 \)), and the theorem says exactly that
\[
  \sgn \colon S_n \to \{1, -1\}
\]
is a group homomorphism (@def-group-homomorphism).

## Transpositions and parity

Now we can compute the sign of the building blocks.

::: {#cor-sign-transposition}
[Sign of a Transposition]

Every transposition is odd: \( \sgn (i\ j) = -1 \) for all \( i \neq j \) in \( \{1, \dots, n\} \).
:::

::: {.proof}
Since \( (i\ j) = (j\ i) \), we may assume \( i < j \). Let \( \tau = (i\ j) \) and let \( p < q \) be positions. We decide when \( \tau(p) > \tau(q) \).

- If neither \( p \) nor \( q \) lies in \( \{i, j\} \), then \( \tau(p) = p < q = \tau(q) \): no inversion.
- If \( (p, q) = (i, j) \), then \( \tau(i) = j > i = \tau(j) \): one inversion.
- If \( p = i \) and \( q \neq j \), then \( \tau(p) = j \) and \( \tau(q) = q \), an inversion exactly when \( i < q < j \). This gives \( j - i - 1 \) inversions.
- If \( q = j \) and \( p \neq i \), then \( \tau(p) = p \) and \( \tau(q) = i \), an inversion exactly when \( i < p < j \). This gives \( j - i - 1 \) inversions.
- If \( p = j \) (so \( q > j \)), then \( \tau(p) = i < q = \tau(q) \); if \( q = i \) (so \( p < i \)), then \( \tau(p) = p < j = \tau(q) \): no inversion.

These cases cover every pair, so \( \operatorname{inv}(\tau) = 1 + 2(j - i - 1) \), an odd number. Hence \( \sgn \tau = -1 \).
:::

The Quick check above is the case \( (i, j) = (1, 4) \): \( 1 + 2 \cdot 2 = 5 \) inversions. Combining the corollary with multiplicativity gives the fact that Chapter 0 left open.

::: {#cor-parity-well-defined}
[Parity Is Well Defined]

Let \( n \ge 2 \) and \( \sigma \in S_n \). If \( \sigma = \tau_1 \cdots \tau_r \) is a product of \( r \) transpositions, then \( \sgn \sigma = (-1)^r \). Consequently, if also \( \sigma = \tau_1' \cdots \tau_s' \) with transpositions \( \tau_m' \), then \( r \) and \( s \) are both even or both odd.
:::

::: {.proof}
By @thm-sign-multiplicative, extended to \( r \) factors, and @cor-sign-transposition, \( \sgn \sigma = \sgn \tau_1 \cdots \sgn \tau_r = (-1)^r \). In the same way \( \sgn \sigma = (-1)^s \). Hence \( (-1)^r = (-1)^s \), so \( r - s \) is even.
:::

So a permutation is even exactly when it is a product of an even number of transpositions, and the "number of swaps" has a well-defined parity even though the number itself is not defined.

::: {#prp-sign-of-cycle}
[Sign of a Cycle]

A \( k \)-cycle has sign \( (-1)^{k-1} \). In particular, cycles of even length are odd and cycles of odd length are even.
:::

::: {.proof}
For \( k = 1 \) the cycle is \( \id \), with sign \( 1 = (-1)^0 \). Let \( k \ge 2 \) and let \( \gamma = (i_1\ i_2\ \cdots\ i_k) \). We claim
\[
  \gamma = (i_1\ i_k)(i_1\ i_{k-1}) \cdots (i_1\ i_3)(i_1\ i_2).
\]
Apply the factors from right to left. The element \( i_1 \) is sent to \( i_2 \) by \( (i_1\ i_2) \), and no later factor involves \( i_2 \). For \( 2 \le m \le k - 1 \), the element \( i_m \) is fixed by the factors before \( (i_1\ i_m) \), sent to \( i_1 \) by it, then to \( i_{m+1} \) by \( (i_1\ i_{m+1}) \), and no later factor involves \( i_{m+1} \). The element \( i_k \) is fixed until the last factor \( (i_1\ i_k) \) sends it to \( i_1 \). Elements outside the cycle are fixed by every factor. This agrees with \( \gamma \) everywhere, proving the claim. The product has \( k - 1 \) transpositions, so \( \sgn \gamma = (-1)^{k-1} \) by @cor-parity-well-defined.
:::

::: {.warning}
**Only the parity of the number of transpositions is determined, and it is not the parity of the cycle length.** The identity in \( S_3 \) equals \( (1\ 2)(1\ 2) \) and also \( (1\ 2)(1\ 3)(1\ 2)(1\ 3)(1\ 2)(1\ 3) \), since \( ((1\ 2)(1\ 3))^3 = (1\ 3\ 2)^3 = \id \); the numbers \( 2 \) and \( 6 \) differ, only their parity agrees. And a \( 3 \)-cycle, "of length \( 3 \)", is **even**: \( (1\ 2\ 3) = (1\ 3)(1\ 2) \). One more trap concerns order: \( (1\ 3)(1\ 2) = (1\ 2\ 3) \) but \( (1\ 2)(1\ 3) = (1\ 3\ 2) \). Multiplying in the wrong order gives the wrong permutation and the wrong bottom row, even though, by @thm-sign-multiplicative, it happens to give the right sign.
:::

## The alternating group

Since \( \sgn \) is a homomorphism, its kernel is a subgroup of \( S_n \) (@thm-homomorphism-basic-properties).

::: {#def-alternating-group}
[Alternating Group]

The **alternating group** \( A_n \) is the kernel of \( \sgn \colon S_n \to \{1, -1\} \), that is, the subgroup of **even** permutations in \( S_n \).
:::

For example, \( A_3 = \{\id, (1\ 2\ 3), (1\ 3\ 2)\} \) by the table above, and \( A_2 = \{\id\} \). For \( n \ge 2 \), exactly half of the permutations are even (Exercise C1). The odd permutations do **not** form a subgroup: they do not contain \( \id \). The name is no coincidence: as we see below and in the next section, rearranging the arguments of an alternating form by an even permutation leaves its value unchanged.

## Back to alternating forms

Here is why this section exists. Let \( f \) be an alternating \( 3 \)-linear form and compare \( f(\v_3, \v_1, \v_2) \) with \( f(\v_1, \v_2, \v_3) \). Swapping the first two arguments of \( (\v_3, \v_1, \v_2) \) gives \( (\v_1, \v_3, \v_2) \), and swapping the last two then gives \( (\v_1, \v_2, \v_3) \). By @thm-alternating-properties (a) each swap costs a factor \( -1 \), so \( f(\v_3, \v_1, \v_2) = (-1)^2 f(\v_1, \v_2, \v_3) = f(\v_1, \v_2, \v_3) \). The list \( (\v_3, \v_1, \v_2) \) is \( (\v_{\sigma(1)}, \v_{\sigma(2)}, \v_{\sigma(3)}) \) for \( \sigma = (1\ 3\ 2) \), with bottom row \( 3, 1, 2 \), and the factor \( 1 \) we found is \( \sgn \sigma \).

A different sequence of swaps could have been used, possibly a longer one. By @cor-parity-well-defined, every such sequence has an even number of swaps, so every route gives the same factor. In general, the next section proves that \( f(\v_{\sigma(1)}, \dots, \v_{\sigma(k)}) = \sgn \sigma \cdot f(\v_1, \dots, \v_k) \) for every alternating \( k \)-linear form, and uses it to turn each of the \( n! \) surviving terms of the expansion sketched in the first section of this chapter into \( \pm D(\e_1, \dots, \e_n) \). Without the corollary, the factor computed swap by swap could depend on the route, and could not be identified with \( \sgn \sigma \).

## Computing signs in practice

There are now two independent ways to find a sign: count inversions, or factor into cycles and use @prp-sign-of-cycle with multiplicativity. Doing both is a good check.

::: {#exm-sign-two-ways}
[A Sign Computed Two Ways]

Find the sign of the permutation \( \sigma \in S_6 \) with two-line notation \( \begin{pmatrix} 1 & 2 & 3 & 4 & 5 & 6 \\ 4 & 5 & 3 & 6 & 2 & 1 \end{pmatrix} \), first by counting inversions and then from its cycles.
:::

::: {.solution}
*Inversions.* Go through the bottom row \( 4, 5, 3, 6, 2, 1 \) from left to right, and for each entry count the **later** entries that are smaller:

| position \( i \) | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| \( \sigma(i) \) | 4 | 5 | 3 | 6 | 2 | 1 |
| later and smaller | 3, 2, 1 | 3, 2, 1 | 2, 1 | 2, 1 | 1 | none |
| count | 3 | 3 | 2 | 2 | 1 | 0 |

So \( \operatorname{inv}(\sigma) = 3 + 3 + 2 + 2 + 1 + 0 = 11 \), which is odd, and \( \sgn \sigma = -1 \).

*Cycles.* Following elements as in @exm-cycle-notation: \( 1 \mapsto 4 \mapsto 6 \mapsto 1 \), then \( 2 \mapsto 5 \mapsto 2 \), and \( 3 \mapsto 3 \). So \( \sigma = (1\ 4\ 6)(2\ 5) \). By @prp-sign-of-cycle, the \( 3 \)-cycle has sign \( 1 \) and the transposition has sign \( -1 \), so by @thm-sign-multiplicative, \( \sgn \sigma = 1 \cdot (-1) = -1 \). The two methods agree.
:::

The following cell checks the example, and also tests @thm-sign-multiplicative and @prp-sign-of-cycle on all of \( S_5 \) by brute force. Permutations are stored as tuples of values \( (\sigma(1), \dots, \sigma(n)) \), shifted to start at \( 0 \).

```{.python .run #cell-sign-two-ways}
from itertools import permutations, combinations

def inv(s):
    return sum(1 for i, j in combinations(range(len(s)), 2) if s[i] > s[j])

def sgn(s):
    return (-1) ** inv(s)

def compose(s, t):          # (s t)(i) = s(t(i)): first t, then s
    return tuple(s[t[i]] for i in range(len(t)))

def cycle(entries, n):      # the cycle (entries[0] entries[1] ...), 0-based
    s = list(range(n))
    for a, b in zip(entries, entries[1:] + entries[:1]):
        s[a] = b
    return tuple(s)

sigma = (4, 5, 3, 6, 2, 1)
sigma0 = tuple(x - 1 for x in sigma)
print("inversions:", inv(sigma0), " sign:", sgn(sigma0))
print("(1 4 6)(2 5) equals sigma:", compose(cycle([0, 3, 5], 6), cycle([1, 4], 6)) == sigma0)

S5 = list(permutations(range(5)))
print("multiplicative on S_5:", all(sgn(compose(s, t)) == sgn(s) * sgn(t) for s in S5 for t in S5))
print("k-cycles have sign (-1)^(k-1):", all(sgn(cycle(list(range(k)), 5)) == (-1) ** (k - 1) for k in range(1, 6)))
```

## Exercises

### A. Check your understanding

:::: {#exr-permutations-and-sign-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define an inversion of \( \sigma \in S_n \) and the sign \( \sgn \sigma \).
2. True or false: every \( 3 \)-cycle is odd. Justify your answer.
3. True or false: some permutation is a product of \( 5 \) transpositions and also a product of \( 8 \) transpositions. Justify your answer.
4. What is the kernel of \( \sgn \colon S_n \to \{1, -1\} \)? Is the set of odd permutations a subgroup?
5. True or false: \( \sgn(\sigma\tau) = \sgn(\tau\sigma) \) for all \( \sigma, \tau \in S_n \), even when \( \sigma\tau \neq \tau\sigma \). Justify your answer.
6. Let \( f \) be an alternating \( 3 \)-linear form. Express \( f(\v_2, \v_3, \v_1) \) in terms of \( f(\v_1, \v_2, \v_3) \).
:::
::::

::: {.solution}
(a) An inversion of \( \sigma \) is a pair \( (i, j) \) with \( 1 \le i < j \le n \) and \( \sigma(i) > \sigma(j) \) (@def-inversion); \( \sgn \sigma = (-1)^{\operatorname{inv}(\sigma)} \) (@def-sign-permutation).

(b) False. By @prp-sign-of-cycle a \( 3 \)-cycle has sign \( (-1)^{2} = 1 \), so it is even; for instance \( (1\ 2\ 3) = (1\ 3)(1\ 2) \).

(c) False. By @cor-parity-well-defined the numbers of transpositions in two such products have the same parity, and \( 5 \) and \( 8 \) do not.

(d) The kernel is the alternating group \( A_n \) of even permutations (@def-alternating-group). The odd permutations do not form a subgroup: \( \id \) is even, so it is not among them.

(e) True. By @thm-sign-multiplicative both sides equal \( \sgn \sigma \cdot \sgn \tau \), and multiplication of integers is commutative. For example \( (1\ 3)(1\ 2) \neq (1\ 2)(1\ 3) \), but both are \( 3 \)-cycles, with sign \( 1 \).

(f) Swapping the first two arguments of \( (\v_2, \v_3, \v_1) \) gives \( (\v_3, \v_2, \v_1) \), and swapping the first and third then gives \( (\v_1, \v_2, \v_3) \). Each swap costs a factor \( -1 \) by @thm-alternating-properties (a), so \( f(\v_2, \v_3, \v_1) = f(\v_1, \v_2, \v_3) \). This matches the sign of the rearrangement \( \sigma \) with bottom row \( 2, 3, 1 \), namely \( \sigma = (1\ 2\ 3) \), which is even.
:::

### B. Practice

:::: {#exr-permutations-and-sign-b1}
[B1: Computing Signs]

Find the sign of each permutation, both by counting inversions and by using cycles.

::: {.enumerate options="label=(\alph*)"}
1. \( \sigma \in S_4 \) with two-line notation \( \begin{pmatrix} 1 & 2 & 3 & 4 \\ 2 & 4 & 1 & 3 \end{pmatrix} \).
2. \( (1\ 2)(3\ 4\ 5) \in S_5 \).
3. \( (1\ 2\ 3)(2\ 3\ 4) \in S_4 \).
:::
::::

::: {.solution}
(a) *Inversions.* In the bottom row \( 2, 4, 1, 3 \), the entry \( 2 \) is followed by the smaller entry \( 1 \), the entry \( 4 \) by \( 1 \) and \( 3 \), and the entry \( 1 \) by nothing smaller. So \( \operatorname{inv}(\sigma) = 1 + 2 + 0 = 3 \) and \( \sgn \sigma = -1 \). *Cycles.* \( 1 \mapsto 2 \mapsto 4 \mapsto 3 \mapsto 1 \), so \( \sigma = (1\ 2\ 4\ 3) \), a \( 4 \)-cycle, with sign \( (-1)^3 = -1 \) by @prp-sign-of-cycle.

(b) *Cycles.* By @prp-sign-of-cycle and @thm-sign-multiplicative, the sign is \( (-1) \cdot (-1)^2 = -1 \). *Inversions.* The permutation sends \( 1 \mapsto 2 \), \( 2 \mapsto 1 \), \( 3 \mapsto 4 \), \( 4 \mapsto 5 \), \( 5 \mapsto 3 \), so the bottom row is \( 2, 1, 4, 5, 3 \). The inversions are \( (1, 2) \), \( (3, 5) \) and \( (4, 5) \), so there are \( 3 \), and the sign is \( -1 \).

(c) *Cycles.* Both factors are \( 3 \)-cycles, so the sign is \( 1 \cdot 1 = 1 \). *Inversions.* Apply \( (2\ 3\ 4) \) first: \( 1 \mapsto 1 \mapsto 2 \), \( 2 \mapsto 3 \mapsto 1 \), \( 3 \mapsto 4 \mapsto 4 \), \( 4 \mapsto 2 \mapsto 3 \). The bottom row is \( 2, 1, 4, 3 \), with inversions \( (1, 2) \) and \( (3, 4) \). So the sign is \( (-1)^2 = 1 \), and in fact the product is \( (1\ 2)(3\ 4) \).
:::

:::: {#exr-permutations-and-sign-b2}
[B2: Sign of the Inverse]

Prove that \( \sgn(\sigma^{-1}) = \sgn \sigma \) for every \( \sigma \in S_n \).
::::

::: {.solution}
Let \( \sigma \in S_n \). By @thm-sign-multiplicative, \( \sgn \sigma \cdot \sgn(\sigma^{-1}) = \sgn(\sigma\sigma^{-1}) = \sgn(\id) = 1 \), since \( \id \) has no inversions. Since \( \sgn \sigma \in \{1, -1\} \) and \( (\pm1)^{-1} = \pm1 \), multiplying both sides by \( \sgn \sigma \) gives \( \sgn(\sigma^{-1}) = \sgn \sigma \).
:::

:::: {#exr-permutations-and-sign-b3}
[B3: The Reversal Permutation]

Let \( \rho \in S_n \) be the reversal, \( \rho(i) = n + 1 - i \). Show that \( \operatorname{inv}(\rho) = n(n-1)/2 \). Hence find the \( n \) for which \( \rho \) is even, and decide the sign of \( \rho \) for \( n = 6 \) and \( n = 9 \).
::::

::: {.solution}
For \( 1 \le i < j \le n \), \( \rho(i) = n + 1 - i > n + 1 - j = \rho(j) \). So **every** pair \( i < j \) is an inversion, and \( \operatorname{inv}(\rho) \) is the number of \( 2 \)-element subsets of \( \{1, \dots, n\} \), which is \( n(n-1)/2 \). Hence \( \sgn \rho = (-1)^{n(n-1)/2} \).

Write \( n = 4q + t \) with \( t \in \{0, 1, 2, 3\} \). Then \( n(n-1)/2 \) is \( 2q(4q - 1) \) for \( t = 0 \), \( 2q(4q + 1) \) for \( t = 1 \), \( (4q + 1)(2q + 1) \) for \( t = 2 \), and \( (2q + 1)(4q + 3) \) for \( t = 3 \). The first two are even and the last two are odd. So \( \rho \) is even exactly when \( n \) leaves remainder \( 0 \) or \( 1 \) on division by \( 4 \). For \( n = 6 \), \( \operatorname{inv}(\rho) = 15 \) and \( \rho \) is odd; for \( n = 9 \), \( \operatorname{inv}(\rho) = 36 \) and \( \rho \) is even.
:::

### C. Going deeper

:::: {#exr-permutations-and-sign-c1}
[C1: Half the Permutations Are Even]

Let \( n \ge 2 \). Prove that exactly \( n!/2 \) permutations in \( S_n \) are even.

*Hint: consider \( \sigma \mapsto (1\ 2)\sigma \).*
::::

::: {.solution}
Let \( E \) and \( O \) be the sets of even and odd permutations; they are disjoint and \( E \cup O = S_n \), so \( \lvert E \rvert + \lvert O \rvert = n! \). Let \( \tau = (1\ 2) \), which exists since \( n \ge 2 \), and define \( L \colon S_n \to S_n \), \( L(\sigma) = \tau\sigma \). By @thm-sign-multiplicative and @cor-sign-transposition, \( \sgn L(\sigma) = -\sgn \sigma \), so \( L \) maps \( E \) into \( O \) and \( O \) into \( E \). Since \( \tau\tau = \id \), \( L(L(\sigma)) = \sigma \), so \( L \) restricted to \( E \) is a bijection \( E \to O \) with inverse \( L \) restricted to \( O \) (@thm-bijective-iff-invertible). Hence \( \lvert E \rvert = \lvert O \rvert = n!/2 \).
:::

:::: {#exr-permutations-and-sign-c2}
[C2: Sign from the Number of Cycles]

Suppose \( \sigma \in S_n \) is written as a product \( \sigma = \gamma_1 \gamma_2 \cdots \gamma_c \) of **disjoint** cycles (no element appears in two of them) whose lengths \( k_1, \dots, k_c \) add up to \( n \), where fixed points are included as cycles of length \( 1 \). (Such a product always exists: follow each element around its loop, as in @exm-cycle-notation.)

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \sgn \sigma = (-1)^{n - c} \).
2. Use (a) to find the sign of \( \sigma = (1\ 4\ 6)(2\ 5) \in S_6 \), and compare with @exm-sign-two-ways.
3. Deduce that an \( n \)-cycle in \( S_n \) and the identity in \( S_n \) have the same sign exactly when \( n \) is odd.
:::
::::

::: {.solution}
(a) By @thm-sign-multiplicative and @prp-sign-of-cycle,
\[
  \sgn \sigma = \prod_{m=1}^{c} \sgn \gamma_m = \prod_{m=1}^{c} (-1)^{k_m - 1} = (-1)^{(k_1 + \dots + k_c) - c} = (-1)^{n - c}.
\]

(b) Including the fixed point \( 3 \) as the cycle \( (3) \), \( \sigma = (1\ 4\ 6)(2\ 5)(3) \), with lengths \( 3 + 2 + 1 = 6 \) and \( c = 3 \). So \( \sgn \sigma = (-1)^{6 - 3} = -1 \), as in @exm-sign-two-ways.

(c) An \( n \)-cycle has \( c = 1 \) and sign \( (-1)^{n-1} \); the identity consists of \( n \) cycles of length \( 1 \), so \( c = n \) and its sign is \( (-1)^0 = 1 \). These agree exactly when \( n - 1 \) is even, that is, when \( n \) is odd.
:::
