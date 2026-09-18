# Existence and Uniqueness of the Determinant

In the first section of this chapter, signed area obeyed three rules: it is linear in each side, it vanishes when two sides are equal, and the unit square has area \( 1 \). In the second section we named functions obeying the first two rules, alternating multilinear forms, and in the third we built the sign of a permutation. This section puts the pieces together. We prove that on \( F^n \) there is **exactly one** alternating \( n \)-linear form that takes the value \( 1 \) on the standard basis, and we find a formula for it. That form is the determinant.

## The goal and the plan

Here is the statement we are after.

> There is exactly one function \( D \colon F^n \times \dots \times F^n \to F \) (with \( n \) factors) that is \( n \)-linear (@def-multilinear-form), alternating (@def-alternating-form), and satisfies \( D(\e_1, \dots, \e_n) = 1 \).

It has two halves of a very different nature. **Uniqueness** says: if such a \( D \) exists, its values are forced. **Existence** says: some function really has all three properties. We prove uniqueness first, because its proof is how we *find* the formula. Suppose \( D \) exists, expand everything using the rules, and see what is left. The formula that comes out is then the only candidate, and existence reduces to checking that the candidate obeys the rules.

Throughout, a list of \( n \) columns \( \a_1, \dots, \a_n \in F^n \) and the matrix \( \A = \begin{pmatrix} \a_1 & \cdots & \a_n \end{pmatrix} \in M_n(F) \) carry the same information, and we pass between them freely. We write \( a_{ij} \) for the \( i \)-th entry of \( \a_j \), so that
\[
\a_j = a_{1j}\e_1 + a_{2j}\e_2 + \dots + a_{nj}\e_n = \sum_{i=1}^{n} a_{ij}\e_i .
\]

## Rearranging the arguments

Expanding a form on basis vectors will produce values like \( f(\e_3, \e_1, \e_2) \): the standard basis in a scrambled order. Alternating forms handle scrambling by a sign, and the sign is exactly the one built from inversions.

::: {#lem-alternating-permute-arguments}
[Permuting the arguments of an alternating form]

Let \( f \) be an alternating \( n \)-linear form on a vector space \( V \) over \( F \), let \( \v_1, \dots, \v_n \in V \), and let \( \sigma \in S_n \). Then
\[
f(\v_{\sigma(1)}, \v_{\sigma(2)}, \dots, \v_{\sigma(n)}) = \sgn(\sigma)\, f(\v_1, \v_2, \dots, \v_n).
\]
:::

::: {.idea}
A transposition swaps two arguments, and each swap costs a factor \( -1 \) by @thm-alternating-properties. Every permutation is a product of transpositions, so the value picks up \( (-1)^k \) for a product of \( k \) of them. Multiplicativity of the sign says that \( (-1)^k \) is \( \sgn(\sigma) \), whichever product we chose.
:::

::: {.proof}
If \( n = 1 \), then \( S_1 = \{\id\} \) and \( \sgn(\id) = 1 \), since the identity has no inversions (@def-sign-permutation); there is nothing to prove. Let \( n \ge 2 \). For \( \pi \in S_n \), write \( f_\pi = f(\v_{\pi(1)}, \dots, \v_{\pi(n)}) \).

First let \( \pi \in S_n \) and let \( \tau = (p\ q) \) be a transposition. The \( j \)-th argument of \( f_{\pi\tau} \) is \( \v_{\pi(\tau(j))} \). For \( j \ne p, q \) this is \( \v_{\pi(j)} \); for \( j = p \) it is \( \v_{\pi(q)} \); for \( j = q \) it is \( \v_{\pi(p)} \). So the arguments of \( f_{\pi\tau} \) are those of \( f_\pi \) with positions \( p \) and \( q \) exchanged. By @thm-alternating-properties, swapping two arguments changes the sign, so
\[
f_{\pi\tau} = -f_\pi . \tag{$\ast$}
\]

Now let \( \sigma \in S_n \). By @thm-transpositions-generate, \( \sigma = \tau_1\tau_2\cdots\tau_k \) for some transpositions \( \tau_1, \dots, \tau_k \) with \( k \ge 1 \). Put \( \pi_0 = \id \) and \( \pi_m = \tau_1\cdots\tau_m \), so that \( \pi_m = \pi_{m-1}\tau_m \). Applying \( (\ast) \) \( k \) times,
\[
f_\sigma = f_{\pi_k} = -f_{\pi_{k-1}} = \dots = (-1)^k f_{\pi_0} = (-1)^k f(\v_1, \dots, \v_n).
\]
On the other hand, by @thm-sign-multiplicative and @cor-sign-transposition, \( \sgn(\sigma) = \sgn(\tau_1)\cdots\sgn(\tau_k) = (-1)^k \). This proves the lemma.
:::

The proof chose a factorization of \( \sigma \) into transpositions, and different choices can have different lengths. The answer does not depend on the choice, because only the parity of \( k \) enters, and @cor-parity-well-defined says the parity is determined by \( \sigma \). In the proof this is absorbed into the equation \( (-1)^k = \sgn(\sigma) \).

## Uniqueness

We now expand an alternating form completely. It helps to see the case \( n = 2 \) first.

::: {#thm-alternating-form-uniqueness}
[Uniqueness of Alternating Forms]

Let \( f \) be an alternating \( n \)-linear form on \( F^n \), and let \( \a_1, \dots, \a_n \in F^n \) have entries \( a_{ij} \) as above. Then
\[
f(\a_1, \dots, \a_n) = f(\e_1, \dots, \e_n) \sum_{\sigma \in S_n} \sgn(\sigma)\, a_{\sigma(1)1}\, a_{\sigma(2)2} \cdots a_{\sigma(n)n} .
\]
In particular, an alternating \( n \)-linear form on \( F^n \) is determined by the single value \( f(\e_1, \dots, \e_n) \).
:::

::: {.idea}
For \( n = 2 \), write \( \a_1 = a_{11}\e_1 + a_{21}\e_2 \) and \( \a_2 = a_{12}\e_1 + a_{22}\e_2 \). Linearity in the first argument, then in the second, gives four terms:
\[
\begin{aligned}
f(\a_1, \a_2) &= a_{11}\, f(\e_1, \a_2) + a_{21}\, f(\e_2, \a_2) \\
&= a_{11}a_{12}\, f(\e_1, \e_1) + a_{11}a_{22}\, f(\e_1, \e_2) + a_{21}a_{12}\, f(\e_2, \e_1) + a_{21}a_{22}\, f(\e_2, \e_2) .
\end{aligned}
\]
The first and last terms vanish because two arguments are equal, and \( f(\e_2, \e_1) = -f(\e_1, \e_2) \). What is left is \( (a_{11}a_{22} - a_{21}a_{12})\, f(\e_1, \e_2) \), the formula for \( n = 2 \).

In general the four terms become one term for each way of choosing, for every argument \( j \), which basis vector \( \e_{\varphi(j)} \) to take from \( \a_j \). A choice is a function \( \varphi \colon \{1, \dots, n\} \to \{1, \dots, n\} \), and there are \( n^n \) of them. The ones that pick some basis vector twice die. The survivors pick every basis vector once, so they are permutations, and @lem-alternating-permute-arguments converts each into a sign.
:::

::: {.proof}
Write \( [k] = \{1, \dots, k\} \) for \( k \ge 1 \). We first expand the arguments one at a time.

::: {.claim}
For each \( k \in \{0, 1, \dots, n\} \),
\[
f(\a_1, \dots, \a_n) = \sum_{\varphi \colon [k] \to [n]} a_{\varphi(1)1} \cdots a_{\varphi(k)k}\; f(\e_{\varphi(1)}, \dots, \e_{\varphi(k)}, \a_{k+1}, \dots, \a_n),
\]
where the sum runs over **all** functions \( \varphi \colon [k] \to [n] \). For \( k = 0 \) we read the right side as the single term \( f(\a_1, \dots, \a_n) \).

::: {.proof}
We use induction on \( k \). For \( k = 0 \) both sides are \( f(\a_1, \dots, \a_n) \). Suppose the claim holds for some \( k < n \). In each term, the argument in position \( k + 1 \) is \( \a_{k+1} = \sum_{i=1}^n a_{i,k+1}\e_i \). Since \( f \) is linear in argument \( k + 1 \),
\[
f(\e_{\varphi(1)}, \dots, \e_{\varphi(k)}, \a_{k+1}, \dots, \a_n) = \sum_{i=1}^{n} a_{i,k+1}\, f(\e_{\varphi(1)}, \dots, \e_{\varphi(k)}, \e_i, \a_{k+2}, \dots, \a_n).
\]
Substituting this into the induction hypothesis gives a sum over all pairs \( (\varphi, i) \) with \( \varphi \colon [k] \to [n] \) and \( i \in [n] \). Such a pair is the same thing as a function \( \psi \colon [k+1] \to [n] \), namely \( \psi(j) = \varphi(j) \) for \( j \le k \) and \( \psi(k+1) = i \); and each \( \psi \) arises from exactly one pair. The term for the pair \( (\varphi, i) \) is \( a_{\psi(1)1} \cdots a_{\psi(k+1),k+1}\, f(\e_{\psi(1)}, \dots, \e_{\psi(k+1)}, \a_{k+2}, \dots, \a_n) \). This is the claim for \( k + 1 \).
:::
:::

Taking \( k = n \) in the claim,
\[
f(\a_1, \dots, \a_n) = \sum_{\varphi \colon [n] \to [n]} a_{\varphi(1)1} \cdots a_{\varphi(n)n}\; f(\e_{\varphi(1)}, \dots, \e_{\varphi(n)}). \tag{$\ast\ast$}
\]
We sort the functions \( \varphi \) into two kinds.

*Case 1: \( \varphi \) is not injective.* Then \( \varphi(p) = \varphi(q) \) for some \( p \ne q \), so the arguments in positions \( p \) and \( q \) of \( f(\e_{\varphi(1)}, \dots, \e_{\varphi(n)}) \) are equal. Since \( f \) is alternating, this value is \( 0 \), and the whole term is \( 0 \).

*Case 2: \( \varphi \) is injective.* Since \( [n] \) is finite, \( \varphi \) is bijective by @thm-finite-injective-iff-surjective, so \( \varphi = \sigma \) for some \( \sigma \in S_n \). By @lem-alternating-permute-arguments with \( \v_i = \e_i \),
\[
f(\e_{\sigma(1)}, \dots, \e_{\sigma(n)}) = \sgn(\sigma)\, f(\e_1, \dots, \e_n).
\]

Hence only the terms of Case 2 survive in \( (\ast\ast) \), there is exactly one for each \( \sigma \in S_n \), and
\[
f(\a_1, \dots, \a_n) = \sum_{\sigma \in S_n} a_{\sigma(1)1} \cdots a_{\sigma(n)n}\, \sgn(\sigma)\, f(\e_1, \dots, \e_n),
\]
which is the stated formula after moving the scalar \( f(\e_1, \dots, \e_n) \) to the front. This proves the theorem.
:::

So the three rules leave no freedom at all. If a normalized alternating form exists, it **must** be
\[
\a_1, \dots, \a_n \ \longmapsto\ \sum_{\sigma \in S_n} \sgn(\sigma)\, a_{\sigma(1)1} \cdots a_{\sigma(n)n} .
\]
Out of \( n^n \) terms, the rules killed all but \( n! \). For \( n = 3 \) that is \( 6 \) out of \( 27 \).

## Existence

The candidate has been found. Now we check it against the rules, forgetting where it came from.

::: {#thm-leibniz-formula-alternating}
[Existence: the Leibniz Formula]

Define \( D \colon F^n \times \dots \times F^n \to F \) by
\[
D(\a_1, \dots, \a_n) = \sum_{\sigma \in S_n} \sgn(\sigma)\, a_{\sigma(1)1}\, a_{\sigma(2)2} \cdots a_{\sigma(n)n} ,
\]
where \( a_{ij} \) is the \( i \)-th entry of \( \a_j \). Then \( D \) is an alternating \( n \)-linear form on \( F^n \), and \( D(\e_1, \dots, \e_n) = 1 \).
:::

::: {.idea}
Linearity is visible: each product takes exactly one entry from each column. For alternation, suppose columns \( p \) and \( q \) are equal. Pair each \( \sigma \) with \( \sigma(p\ q) \). The two permutations have opposite signs. Their products use the same entries, except that the entries taken from columns \( p \) and \( q \) trade places, and those two columns are equal. So each pair contributes \( x - x = 0 \).

Why pair terms instead of arguing "swapping the equal columns changes \( D \) to \( -D \), so \( D = -D \) and \( D = 0 \)"? Because \( D = -D \) gives \( 2D = 0 \), and over a field with \( 1 + 1 = 0 \), such as \( \nF_2 \), that says nothing. The pairing argument never divides by \( 2 \).
:::

::: {.proof}
*Multilinearity.* Fix \( k \in [n] \) and fix all columns except the \( k \)-th. For a fixed \( \sigma \), the product \( a_{\sigma(1)1} \cdots a_{\sigma(n)n} \) contains exactly one entry of \( \a_k \), namely \( a_{\sigma(k)k} \), the \( \sigma(k) \)-th coordinate of \( \a_k \). So the term for \( \sigma \) equals \( c_\sigma\, a_{\sigma(k)k} \), where \( c_\sigma = \sgn(\sigma) \prod_{j \ne k} a_{\sigma(j)j} \) does not depend on \( \a_k \). The map \( \a_k \mapsto a_{\sigma(k)k} \) is linear, since coordinates of a sum are sums of coordinates and coordinates of \( c\a_k \) are \( c \) times the coordinates. So each term is linear in \( \a_k \), and hence so is their sum \( D \).

*Alternation.* Suppose \( \a_p = \a_q \) with \( p < q \), that is, \( a_{ip} = a_{iq} \) for all \( i \). Let \( \tau = (p\ q) \), let \( A_n = \{\sigma \in S_n : \sgn(\sigma) = 1\} \) be the even permutations (@def-alternating-group), so that \( S_n \setminus A_n = \{\sigma \in S_n : \sgn(\sigma) = -1\} \) consists of the odd ones. Since \( \sgn(\sigma\tau) = \sgn(\sigma)\sgn(\tau) = -\sgn(\sigma) \) by @thm-sign-multiplicative and @cor-sign-transposition, the map \( \sigma \mapsto \sigma\tau \) sends \( A_n \) to \( S_n \setminus A_n \). It is a bijection \( A_n \to S_n \setminus A_n \), because \( \rho \mapsto \rho\tau \) sends \( S_n \setminus A_n \) back to \( A_n \) and \( \sigma\tau\tau = \sigma \). Every \( \sigma \in S_n \) has sign \( 1 \) or \( -1 \), so
\[
D(\a_1, \dots, \a_n) = \sum_{\sigma \in A_n} \Big( \prod_{j=1}^{n} a_{\sigma(j)j} - \prod_{j=1}^{n} a_{\sigma\tau(j)\,j} \Big).
\]
Fix \( \sigma \in A_n \) and compare the two products factor by factor. For \( j \ne p, q \), \( \sigma\tau(j) = \sigma(j) \), so the factors agree. For \( j = p \), the second product has \( a_{\sigma(q)p} = a_{\sigma(q)q} \), which is the factor of the first product at \( j = q \). For \( j = q \), the second product has \( a_{\sigma(p)q} = a_{\sigma(p)p} \), the factor of the first product at \( j = p \). So the two products consist of the same \( n \) factors in a different order, and they are equal because multiplication in \( F \) is commutative. Every bracket is \( 0 \), and \( D(\a_1, \dots, \a_n) = 0 \).

*Normalization.* For \( \a_j = \e_j \), \( a_{ij} \) is \( 1 \) if \( i = j \) and \( 0 \) otherwise. The product \( a_{\sigma(1)1} \cdots a_{\sigma(n)n} \) is therefore \( 1 \) if \( \sigma(j) = j \) for all \( j \), and \( 0 \) otherwise. Only \( \sigma = \id \) contributes, and \( \sgn(\id) = 1 \). Hence \( D(\e_1, \dots, \e_n) = 1 \). This proves the theorem.
:::

Uniqueness and existence together answer the question of the first section: the rules of signed area single out exactly one function.

## The determinant

We now have a function of square matrices that is forced on us by three reasonable rules, and it deserves a name. It is the central notion of this chapter.

*The determinant is the only way to attach a number to \( n \) vectors in \( F^n \) that is linear in each vector, vanishes when two vectors coincide, and gives \( 1 \) on the standard basis.*

::: {#def-determinant}
[Determinant]

Let \( n \ge 1 \) and \( \A = (a_{ij}) \in M_n(F) \). The **determinant** of \( \A \) is
\[
\det \A \coloneqq \sum_{\sigma \in S_n} \sgn(\sigma)\, a_{\sigma(1)1}\, a_{\sigma(2)2} \cdots a_{\sigma(n)n} \ \in F .
\]
For columns \( \a_1, \dots, \a_n \in F^n \) we also write \( \det(\a_1, \dots, \a_n) \) for the determinant of the matrix \( \begin{pmatrix} \a_1 & \cdots & \a_n \end{pmatrix} \).
:::

In words: run over **all** \( n! \) permutations \( \sigma \). For each, pick from column \( j \) the entry in row \( \sigma(j) \); this picks one entry in every column and, because \( \sigma \) is a bijection, one entry in every row. Multiply the \( n \) picked entries, attach the sign of \( \sigma \), and add up. The determinant is defined **only for square matrices**, and its value lies in the field \( F \) of the entries.

**Well-definedness.** The formula is a finite sum, so it always gives a number. What the name "**the** determinant" really claims is that nothing else satisfies the three rules, and that is @thm-alternating-form-uniqueness; @thm-leibniz-formula-alternating shows \( \det \) does satisfy them. The sign \( \sgn(\sigma) \) is fixed by counting inversions (@def-sign-permutation), and by @cor-parity-well-defined any factorization of \( \sigma \) into transpositions gives the same sign, so either method may be used to evaluate the formula.

**Examples.**

- **\( n = 1 \).** \( S_1 = \{\id\} \), so \( \det(a) = a \). A degenerate case, but it is the base of every induction on size.
- **\( n = 2 \).** \( S_2 = \{\id, (1\ 2)\} \), with signs \( 1 \) and \( -1 \). The identity picks \( a_{11}a_{22} \), and \( (1\ 2) \) picks \( a_{21}a_{12} \). So
  \[
  \det \begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - cb,
  \]
  the value derived from the rules in @exm-two-by-two-from-rules, and the number whose non-vanishing decides invertibility in @thm-two-by-two-inverse.
- **\( n = 3 \).** The six permutations of \( S_3 \) and their signs (a \( 3 \)-cycle has sign \( 1 \), a transposition \( -1 \)) give
  \[
  \begin{aligned}
  \det \A = {}& a_{11}a_{22}a_{33} - a_{21}a_{12}a_{33} - a_{31}a_{22}a_{13} - a_{11}a_{32}a_{23} \\
  &+ a_{21}a_{32}a_{13} + a_{31}a_{12}a_{23},
  \end{aligned}
  \]
  the terms coming from \( \id, (1\ 2), (1\ 3), (2\ 3), (1\ 2\ 3), (1\ 3\ 2) \) in this order. For instance \( \sigma = (1\ 2\ 3) \) has \( \sigma(1) = 2 \), \( \sigma(2) = 3 \), \( \sigma(3) = 1 \), and picks \( a_{21}a_{32}a_{13} \).
- **A numerical \( 3 \times 3 \).** For \( \A = \begin{pmatrix} 2 & 1 & 3 \\ 0 & 4 & 1 \\ 5 & 2 & 1 \end{pmatrix} \), the six terms in the same order are \( 8 \), \( -0 \), \( -60 \), \( -4 \), \( 0 \) and \( 5 \), so \( \det \A = 8 - 60 - 4 + 5 = -51 \).
- **Identity and zero.** \( \det \I_n = 1 \) by the normalization in @thm-leibniz-formula-alternating, and \( \det 0 = 0 \), since every product contains a zero factor.

**Non-example by minimal change.** Delete the sign. The **permanent** \( \operatorname{per} \A = \sum_{\sigma} a_{\sigma(1)1} \cdots a_{\sigma(n)n} \) is still \( n \)-linear in the columns, by the same argument as in @thm-leibniz-formula-alternating, and still gives \( 1 \) at \( \I_n \). But it is not alternating: \( \operatorname{per} \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = 1 + 1 = 2 \), which is non-zero over \( \nR \) although the two columns are equal. The sign is exactly what makes the pairing argument cancel.

**Why this definition.** Each rule has a job. Without normalization, the uniqueness theorem only pins the form down up to the scalar \( f(\e_1, \dots, \e_n) \). Without alternation, the permanent and many other functions qualify. Multilinearity is what let us expand at all. The choice of **columns** rather than rows is a convention: we show below that the transpose has the same determinant, so rows would give the same function. We have avoided "Sarrus's rule" on purpose. It is a picture of the six-term formula for \( n = 3 \) and nothing more, and for \( n = 4 \) its diagonal pattern would produce \( 8 \) products while the Leibniz formula has \( 24 \).

::: {.warning}
**The determinant is not linear.** It is linear in **each column separately**, not in the matrix. For \( n = 2 \), \( \det \I_2 = 1 \) but \( \det(\I_2 + \I_2) = \det(2\I_2) = 4 \ne 1 + 1 \). In general each product in the Leibniz formula has \( n \) factors, and scaling \( \A \) scales every factor, so
\[
\det(c\A) = c^n \det \A, \qquad \text{in particular} \qquad \det(-\A) = (-1)^n \det \A .
\]
So \( \det(-\A) = \det \A \) for \( 2 \times 2 \) matrices, not \( -\det \A \).
:::

::: {.check}
Which permutations give a non-zero term in the determinant of \( \begin{pmatrix} 0 & 0 & 1 \\ 0 & 2 & 0 \\ 3 & 0 & 0 \end{pmatrix} \), and what is the determinant?
:::

::: {.solution}
Column \( 1 \) has its only non-zero entry in row \( 3 \), column \( 2 \) in row \( 2 \), and column \( 3 \) in row \( 1 \). A non-zero term needs \( a_{\sigma(j)j} \ne 0 \) for every \( j \), so \( \sigma(1) = 3 \), \( \sigma(2) = 2 \), \( \sigma(3) = 1 \), that is, \( \sigma = (1\ 3) \), of sign \( -1 \). The determinant is \( -3 \cdot 2 \cdot 1 = -6 \).
:::

The payoff for the forms of the second section is immediate. There we saw that the alternating \( n \)-linear forms on \( F^n \) form a vector space (@thm-alternating-forms-space) and promised its dimension.

::: {#cor-alternating-forms-one-dimensional}
[Alternating \( n \)-Forms on \( F^n \) Form a Line]

The vector space of alternating \( n \)-linear forms on \( F^n \) has dimension \( 1 \), with basis \( (\det) \). Explicitly, every alternating \( n \)-linear form \( f \) on \( F^n \) satisfies
\[
f(\a_1, \dots, \a_n) = f(\e_1, \dots, \e_n)\, \det(\a_1, \dots, \a_n) .
\]
:::

::: {.proof}
By @thm-leibniz-formula-alternating, \( \det \) is an element of this space, and it is not the zero form since \( \det(\e_1, \dots, \e_n) = 1 \). So the list \( (\det) \) is linearly independent. By @thm-alternating-form-uniqueness and @def-determinant, every \( f \) in the space satisfies the displayed formula, so \( f = f(\e_1, \dots, \e_n) \det \) lies in the span of \( \det \). Hence \( (\det) \) is a basis, and the dimension is \( 1 \).
:::

This corollary is the most useful form of uniqueness. To prove that some function \( g \) of \( n \) columns is a multiple of the determinant, check that \( g \) is multilinear and alternating, and compute \( g(\e_1, \dots, \e_n) \). The multiplicativity of the determinant in the next section is proved exactly this way.

## Transposes and triangular matrices

The definition read the matrix column by column. Reading it row by row gives nothing new.

::: {#thm-det-transpose}
[Determinant of the Transpose]

For every \( \A \in M_n(F) \), \( \det \A\tp = \det \A \). Consequently, \( \det \A \) is also an alternating \( n \)-linear function of the **rows** of \( \A \), with value \( 1 \) at \( \I_n \).
:::

::: {.idea}
A term of \( \det \A\tp \) picks the entries \( a_{j\sigma(j)} \), one in each row. The same \( n \) positions are also "one in each column": position \( (j, \sigma(j)) \) is \( (\sigma^{-1}(i), i) \) with \( i = \sigma(j) \). So the term is the term of \( \det \A \) for \( \sigma^{-1} \), and \( \sigma^{-1} \) has the same sign as \( \sigma \).
:::

::: {.proof}
The \( (i, j) \)-entry of \( \A\tp \) is \( a_{ji} \) (@def-transpose), so by @def-determinant
\[
\det \A\tp = \sum_{\sigma \in S_n} \sgn(\sigma)\, a_{1\sigma(1)}\, a_{2\sigma(2)} \cdots a_{n\sigma(n)} .
\]
Fix \( \sigma \). As \( j \) runs through \( [n] \), \( i = \sigma(j) \) runs through \( [n] \) exactly once, and \( j = \sigma^{-1}(i) \). Since multiplication in \( F \) is commutative, we may reorder the factors by \( i \):
\[
\prod_{j=1}^{n} a_{j\sigma(j)} = \prod_{i=1}^{n} a_{\sigma^{-1}(i)\, i} .
\]
Next, \( \sgn(\sigma)\sgn(\sigma^{-1}) = \sgn(\sigma\sigma^{-1}) = \sgn(\id) = 1 \) by @thm-sign-multiplicative, and both signs lie in \( \{1, -1\} \), so \( \sgn(\sigma^{-1}) = \sgn(\sigma) \). Therefore
\[
\det \A\tp = \sum_{\sigma \in S_n} \sgn(\sigma^{-1}) \prod_{i=1}^{n} a_{\sigma^{-1}(i)\, i} = \sum_{\rho \in S_n} \sgn(\rho) \prod_{i=1}^{n} a_{\rho(i)\, i} = \det \A,
\]
where the second equality substitutes \( \rho = \sigma^{-1} \); this is allowed because \( \sigma \mapsto \sigma^{-1} \) is a bijection of \( S_n \) onto itself, being its own inverse.

For the second statement, let \( \r_1, \dots, \r_n \) be the rows of \( \A \). The columns of \( \A\tp \) are \( \r_1\tp, \dots, \r_n\tp \), so \( \det \A = \det \A\tp = \det(\r_1\tp, \dots, \r_n\tp) \). The map \( \r \mapsto \r\tp \) is linear (@thm-transpose-properties), so by @thm-leibniz-formula-alternating the function \( (\r_1, \dots, \r_n) \mapsto \det(\r_1\tp, \dots, \r_n\tp) \) is linear in each \( \r_i \). If \( \r_p = \r_q \) for some \( p \ne q \), then \( \r_p\tp = \r_q\tp \), and the value is \( 0 \). Finally \( \I_n\tp = \I_n \). This proves the theorem.
:::

So every statement about columns has a twin about rows. In particular @thm-alternating-properties applies to rows: swapping two rows changes the sign of \( \det \), and adding a multiple of one row to another does not change it. The next section turns this into a method of computation.

Before that, one class of matrices whose determinant can be read off directly. Recall that \( \A \) is upper triangular if \( a_{ij} = 0 \) whenever \( i > j \) (@def-upper-triangular).

::: {#thm-det-triangular}
[Determinant of a Triangular Matrix]

If \( \A \in M_n(F) \) is upper triangular or lower triangular, then
\[
\det \A = a_{11}\, a_{22} \cdots a_{nn} .
\]
:::

::: {.idea}
Which permutations can pick only entries on or above the diagonal? Picking \( a_{\sigma(j)j} \) with \( \sigma(j) \le j \) for every \( j \) forces \( \sigma = \id \): the numbers \( \sigma(1), \dots, \sigma(n) \) are \( 1, \dots, n \) in some order, so they have the same sum, and none of them is allowed to exceed its partner.
:::

::: {.proof}
Suppose \( \A \) is upper triangular, and let \( \sigma \in S_n \) with \( \sigma \ne \id \). We claim \( \sigma(j) > j \) for some \( j \). Otherwise \( \sigma(j) \le j \) for all \( j \). Since \( \sigma \) is a bijection of \( [n] \), \( \sum_{j=1}^n \sigma(j) = \sum_{j=1}^n j \), so \( \sum_{j=1}^n \big(j - \sigma(j)\big) = 0 \) is a sum of non-negative integers equal to \( 0 \). Hence \( \sigma(j) = j \) for every \( j \), contradicting \( \sigma \ne \id \). For such \( j \), \( a_{\sigma(j)j} = 0 \) by upper triangularity, so the term of \( \sigma \) is \( 0 \). Only the identity remains, and \( \det \A = \sgn(\id)\, a_{11} \cdots a_{nn} = a_{11} \cdots a_{nn} \).

If \( \A \) is lower triangular, then \( \A\tp \) is upper triangular with the same diagonal, and \( \det \A = \det \A\tp = a_{11} \cdots a_{nn} \) by @thm-det-transpose. This proves the theorem.
:::

For example, \( \det \begin{pmatrix} 2 & 7 & -1 \\ 0 & 3 & 5 \\ 0 & 0 & -4 \end{pmatrix} = 2 \cdot 3 \cdot (-4) = -24 \): six terms, five of which vanish. Diagonal matrices are a special case, \( \det \diag(d_1, \dots, d_n) = d_1 \cdots d_n \). Together with Chapter 2's result that an upper triangular matrix is invertible exactly when its diagonal entries are non-zero (@lem-triangular-invertible), this already shows that for upper triangular matrices, \( \A \) is invertible if and only if \( \det \A \ne 0 \). The next section proves this for all square matrices.

## Determinants over a commutative ring

The characteristic polynomial at the end of this chapter is the determinant of a matrix whose entries are **polynomials**, such as \( \begin{pmatrix} x - 1 & -2 \\ -3 & x - 4 \end{pmatrix} \). Polynomials form no field, since \( x \) has no inverse in \( F[x] \). So we record exactly what this section used.

::: {.remark}
**Commutative rings.** A **commutative ring** is a set \( R \) with an addition and a multiplication satisfying all the axioms of a field (@def-field) except, possibly, the existence of multiplicative inverses (F8). The integers \( \nZ \) and the polynomials \( F[x] \) are examples (@thm-polynomial-ring-laws). For \( \A \in M_n(R) \), the Leibniz formula of @def-determinant still defines \( \det \A \in R \), reading \( \sgn(\sigma)\, r \) as \( r \) or \( -r \).

**Every proof in this section uses only addition, subtraction and multiplication**, together with commutativity, and never a multiplicative inverse. So the following hold verbatim over any commutative ring \( R \), with "linear in each argument" meaning additive and compatible with multiplication by elements of \( R \): @lem-alternating-permute-arguments, @thm-alternating-form-uniqueness, @thm-leibniz-formula-alternating, @thm-det-transpose and @thm-det-triangular. The only outside input is the swap rule of @thm-alternating-properties, and it too is division-free: expanding \( 0 = f(\dots, \u + \v, \dots, \u + \v, \dots) \) by additivity leaves \( f(\dots, \u, \dots, \v, \dots) + f(\dots, \v, \dots, \u, \dots) = 0 \). The parts of @thm-alternating-properties about dependent arguments are not used; they involve solving for one vector in terms of others, which needs division.
:::

In the characteristic-polynomial section we will apply these results with \( R = F[x] \). The next two sections flag, in the same way, which of their proofs survive the passage to a ring.

## Exercises

### A. Check your understanding

::: {#exr-existence-and-uniqueness-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the three properties that characterize \( \det \colon M_n(F) \to F \), and write down the Leibniz formula.
2. How many terms does the Leibniz formula have for \( n = 4 \)? How many of the corresponding permutations have sign \( 1 \)?
3. True or false: \( \det(\A + \B) = \det \A + \det \B \) for all \( \A, \B \in M_2(\nR) \). Justify your answer.
4. True or false: \( \det(-\A) = -\det \A \) for all \( \A \in M_3(\nR) \). Justify your answer.
5. In the proof of @thm-alternating-form-uniqueness, why does a term with a non-injective \( \varphi \) vanish?
6. Explain why the existence proof pairs \( \sigma \) with \( \sigma(p\ q) \) instead of arguing "\( D = -D \), so \( D = 0 \)".
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. \( \det \) is \( n \)-linear in the columns, alternating (zero whenever two columns are equal), and \( \det \I_n = 1 \). By @thm-alternating-form-uniqueness and @thm-leibniz-formula-alternating it is the only such function, and \( \det \A = \sum_{\sigma \in S_n} \sgn(\sigma)\, a_{\sigma(1)1} \cdots a_{\sigma(n)n} \).
2. One term per permutation: \( 4! = 24 \). In the proof of @thm-leibniz-formula-alternating, \( \sigma \mapsto \sigma(1\ 2) \) is a bijection from the permutations of sign \( 1 \) to those of sign \( -1 \), so each set has \( 12 \) elements.
3. False. For \( \A = \B = \I_2 \), \( \det(\A + \B) = \det(2\I_2) = 4 \) but \( \det \A + \det \B = 2 \).
4. True. Each Leibniz product has \( 3 \) factors, each multiplied by \( -1 \), so \( \det(-\A) = (-1)^3 \det \A = -\det \A \). (For \( n = 2 \) it is false.)
5. If \( \varphi(p) = \varphi(q) \) with \( p \ne q \), the form is evaluated with the equal arguments \( \e_{\varphi(p)} \) in positions \( p \) and \( q \), and an alternating form vanishes there.
6. \( D = -D \) only gives \( 2D = 0 \). Over a field in which \( 2 = 0 \), such as \( \nF_2 \), this does not imply \( D = 0 \). The pairing shows that the terms cancel in pairs, which works over every field.
:::
:::

### B. Practice

::: {#exr-existence-and-uniqueness-b1}
[B1: Six-term determinants]

Using the Leibniz formula, listing all six terms, compute the determinants of
\[
\A = \begin{pmatrix} 3 & 1 & 2 \\ 1 & 0 & 4 \\ 2 & 5 & 1 \end{pmatrix}, \qquad \B = \begin{pmatrix} 1 & -1 & 2 \\ 0 & 3 & 1 \\ 4 & 2 & -2 \end{pmatrix} \in M_3(\nR).
\]
Then compute \( \det \A\tp \) in the same way, and hence verify @thm-det-transpose for this \( \A \).
:::

::: {.solution}
We use the order \( \id, (1\ 2), (1\ 3), (2\ 3), (1\ 2\ 3), (1\ 3\ 2) \) and the six-term formula from the examples after @def-determinant:
\[
a_{11}a_{22}a_{33},\ -a_{21}a_{12}a_{33},\ -a_{31}a_{22}a_{13},\ -a_{11}a_{32}a_{23},\ a_{21}a_{32}a_{13},\ a_{31}a_{12}a_{23}.
\]
For \( \A \): \( 3 \cdot 0 \cdot 1 = 0 \); \( -1 \cdot 1 \cdot 1 = -1 \); \( -2 \cdot 0 \cdot 2 = 0 \); \( -3 \cdot 5 \cdot 4 = -60 \); \( 1 \cdot 5 \cdot 2 = 10 \); \( 2 \cdot 1 \cdot 4 = 8 \). Hence \( \det \A = 0 - 1 + 0 - 60 + 10 + 8 = -43 \).

For \( \B \): \( 1 \cdot 3 \cdot (-2) = -6 \); \( -0 \cdot (-1) \cdot (-2) = 0 \); \( -4 \cdot 3 \cdot 2 = -24 \); \( -1 \cdot 2 \cdot 1 = -2 \); \( 0 \cdot 2 \cdot 2 = 0 \); \( 4 \cdot (-1) \cdot 1 = -4 \). Hence \( \det \B = -6 + 0 - 24 - 2 + 0 - 4 = -36 \).

For \( \A\tp = \begin{pmatrix} 3 & 1 & 2 \\ 1 & 0 & 5 \\ 2 & 4 & 1 \end{pmatrix} \): \( 3 \cdot 0 \cdot 1 = 0 \); \( -1 \cdot 1 \cdot 1 = -1 \); \( -2 \cdot 0 \cdot 2 = 0 \); \( -3 \cdot 4 \cdot 5 = -60 \); \( 1 \cdot 4 \cdot 2 = 8 \); \( 2 \cdot 1 \cdot 5 = 10 \). The sum is \( -43 = \det \A \), as @thm-det-transpose predicts; the six terms are the same numbers, with the two \( 3 \)-cycles exchanged, because \( (1\ 2\ 3)^{-1} = (1\ 3\ 2) \).
:::

::: {#exr-existence-and-uniqueness-b2}
[B2: The determinant of \( \P_\sigma \)]

Let \( \sigma \in S_n \) and let \( \P_\sigma = \begin{pmatrix} \e_{\sigma(1)} & \cdots & \e_{\sigma(n)} \end{pmatrix} \) be its permutation matrix (@def-permutation-matrix).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \det \P_\sigma = \sgn(\sigma) \).
2. Hence compute \( \det \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} \) and \( \det \begin{pmatrix} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix} \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. By @thm-leibniz-formula-alternating, \( \det \) is an alternating \( n \)-linear form on \( F^n \). By @lem-alternating-permute-arguments with \( \v_i = \e_i \),
   \[
   \det \P_\sigma = \det(\e_{\sigma(1)}, \dots, \e_{\sigma(n)}) = \sgn(\sigma) \det(\e_1, \dots, \e_n) = \sgn(\sigma) \det \I_n = \sgn(\sigma).
   \]
2. The first matrix has columns \( \e_2, \e_3, \e_1 \), so it is \( \P_\sigma \) with \( \sigma(1) = 2 \), \( \sigma(2) = 3 \), \( \sigma(3) = 1 \), that is, \( \sigma = (1\ 2\ 3) \). A \( 3 \)-cycle is \( (1\ 3)(1\ 2) \) (@exm-cycle-notation), a product of two transpositions, so its sign is \( 1 \) and the determinant is \( 1 \). The second matrix has columns \( \e_2, \e_1, \e_4, \e_3 \), so it is \( \P_\sigma \) with \( \sigma = (1\ 2)(3\ 4) \), of sign \( (-1)^2 = 1 \) by @thm-sign-multiplicative and @cor-sign-transposition. Its determinant is \( 1 \).
:::
:::

::: {#exr-existence-and-uniqueness-b3}
[B3: A zero row]

Let \( \A \in M_n(F) \) have a zero row. Prove directly from @def-determinant, without using @thm-det-transpose, that \( \det \A = 0 \). Then prove the same for a zero column.
:::

::: {.solution}
Suppose row \( i \) of \( \A \) is zero, and let \( \sigma \in S_n \). Since \( \sigma \) is surjective, there is \( j \) with \( \sigma(j) = i \). The factor \( a_{\sigma(j)j} = a_{ij} \) of the term for \( \sigma \) is \( 0 \), so the term is \( 0 \). This holds for every \( \sigma \), so \( \det \A = 0 \).

Suppose column \( j \) is zero. For every \( \sigma \), the term for \( \sigma \) contains the factor \( a_{\sigma(j)j} = 0 \), so again every term vanishes and \( \det \A = 0 \).
:::

### C. Going deeper

::: {#exr-existence-and-uniqueness-c1}
[C1: Too many zeros]

Let \( \A \in M_n(F) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that if more than \( n^2 - n \) entries of \( \A \) are zero, then \( \det \A = 0 \).
2. Show that the bound is sharp: give, for each \( n \), a matrix with exactly \( n^2 - n \) zero entries and non-zero determinant.
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. If more than \( n^2 - n \) entries are zero, then fewer than \( n \) entries are non-zero. For \( \sigma \in S_n \), the term for \( \sigma \) is a product of the \( n \) entries in positions \( (\sigma(1), 1), \dots, (\sigma(n), n) \). These positions are distinct, since their column indices are distinct. They cannot all hold non-zero entries, because there are fewer than \( n \) such entries. So at least one factor is \( 0 \), and the term is \( 0 \). Hence \( \det \A = 0 \).
2. \( \I_n \) has exactly \( n^2 - n \) zero entries, and \( \det \I_n = 1 \ne 0 \).
:::
:::

::: {#exr-existence-and-uniqueness-c2}
[C2: Counting the cost]

A computer performs about \( 10^9 \) multiplications per second.

::: {.enumerate options="label=(\alph*)"}
1. Show that evaluating the Leibniz formula term by term for an \( n \times n \) matrix takes \( n! \, (n - 1) \) multiplications. Estimate the time this takes for \( n = 20 \).
2. Gaussian elimination (Chapter 2) brings \( \A \) to upper triangular form. Suppose no row swaps are needed. At step \( k \) (for \( k = 1, \dots, n - 1 \)), each of the \( n - k \) rows below the pivot requires one division to find its multiplier and \( n - k \) multiplications to update its entries in columns \( k + 1, \dots, n \). Show that the total number of multiplications and divisions is \( \frac{(n-1)n(n+1)}{3} \), and evaluate it for \( n = 20 \).
:::

In the next section we will see that the determinant can be read off from this triangular form with \( n - 1 \) further multiplications.
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. There is one term for each \( \sigma \in S_n \), that is, \( n! \) terms, and each is a product of \( n \) entries, which takes \( n - 1 \) multiplications. For \( n = 20 \), \( 20! \cdot 19 = 46\,225\,138\,155\,356\,160\,000 \approx 4.6 \times 10^{19} \). At \( 10^9 \) per second this takes about \( 4.6 \times 10^{10} \) seconds, roughly \( 1\,460 \) years.
2. Step \( k \) costs \( (n - k)(1 + (n - k)) \) operations. With \( m = n - k \) running from \( 1 \) to \( n - 1 \), the total is
   \[
   \sum_{m=1}^{n-1} m(m + 1) = \sum_{m=1}^{n-1} m^2 + \sum_{m=1}^{n-1} m = \frac{(n-1)n(2n-1)}{6} + \frac{(n-1)n}{2} = \frac{(n-1)n\big((2n - 1) + 3\big)}{6} = \frac{(n-1)n(n+1)}{3}.
   \]
   For \( n = 20 \) this is \( \frac{19 \cdot 20 \cdot 21}{3} = 2\,660 \), a few microseconds. The Leibniz formula is a definition and a proof tool, not an algorithm.
:::
:::

::: {#exr-existence-and-uniqueness-c3}
[C3: The permanent, and a change of field]

For \( \A \in M_n(F) \) define \( \operatorname{per} \A = \sum_{\sigma \in S_n} a_{\sigma(1)1} \cdots a_{\sigma(n)n} \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \operatorname{per} \) is \( n \)-linear in the columns and \( \operatorname{per} \I_n = 1 \).
2. Let \( n \ge 2 \). Prove that over \( \nR \), \( \operatorname{per} \) is **not** alternating.
3. Prove that over \( \nF_2 \), \( \operatorname{per} \A = \det \A \) for every \( \A \in M_n(\nF_2) \). Explain why this does not contradict (b) and @thm-alternating-form-uniqueness.
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. The proof of multilinearity in @thm-leibniz-formula-alternating never used the signs: for fixed \( k \), the term for \( \sigma \) is a constant times \( a_{\sigma(k)k} \), which is linear in the \( k \)-th column. The normalization argument there also applies: only \( \sigma = \id \) contributes at \( \I_n \), with product \( 1 \).
2. Let \( \J \in M_n(\nR) \) have every entry equal to \( 1 \). Its first two columns are equal, but every term of \( \operatorname{per} \J \) is \( 1 \), so \( \operatorname{per} \J = n! \ne 0 \) in \( \nR \).
3. In \( \nF_2 \), \( -1 = 1 \), so \( \sgn(\sigma) \cdot r = r \) for every \( r \), and the two formulas agree term by term. There is no contradiction: (b) is a statement over \( \nR \), where \( n! \ne 0 \). Over \( \nF_2 \), \( \operatorname{per} \J = n! \cdot 1 = 0 \) for \( n \ge 2 \), and \( \operatorname{per} = \det \) is alternating, as @thm-leibniz-formula-alternating guarantees. Uniqueness is about a fixed field, and over each field there is exactly one normalized alternating form.
:::
:::
