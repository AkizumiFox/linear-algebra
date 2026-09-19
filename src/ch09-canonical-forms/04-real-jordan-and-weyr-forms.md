# The Real Jordan Form and the Weyr Form

The Jordan form of Section 3 exists only when \( p_T \) splits, and over \( \nR \) that often fails: a rotation of the plane has no real eigenvalue at all. But a real matrix is also a complex matrix, and its complex eigenvalues come in conjugate pairs (@thm-real-matrix-complex-eigenvalues). This section turns a complex Jordan basis into a **real** one by pairing each chain with its conjugate; the price for a conjugate pair is a \( 2 \times 2 \) rotation-scaling block instead of a scalar, and the result is the best real matrix there is. The second half rearranges the same data in another way, the Weyr form, which is the form to reach for when a second operator commutes with the first.

## A block for a conjugate pair

The obstruction is visible in the smallest case. The rotation \( \R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \in M_2(\nR) \) has \( p_{\R} = x^2 + 1 \), so \( \R \) has no real eigenvalue and no real eigenvector (@exm-rotation-invariant-subspaces). Every real matrix similar to \( \R \) therefore has no real eigenvalue either, so it cannot be triangular: whatever basis of \( \nR^2 \) we choose, the matrix of \( \R \) keeps two off-diagonal entries. So \( \R \) is already as simple as it will ever get over \( \nR \), and the honest thing to do is to promote it to a building block.

More generally, for \( \lambda = a + bi \in \nC \) with \( b \ne 0 \), consider
\[
\vLambda = \begin{pmatrix} a & -b \\ b & a \end{pmatrix} \in M_2(\nR), \qquad p_{\vLambda} = (x - a)^2 + b^2 = \big(x - (a + bi)\big)\big(x - (a - bi)\big) .
\]
This matrix carries the conjugate pair \( \lambda, \conj\lambda \) as its complex eigenvalues, has trace \( 2a = 2\operatorname{Re}\lambda \) and determinant \( a^2 + b^2 = \lvert\lambda\rvert^2 \), and is a scaled rotation: it stretches by \( \lvert\lambda\rvert \) and turns by the argument of \( \lambda \). It is the real substitute for the \( 1 \times 1 \) block \( (\lambda) \), and it costs one extra dimension.

*A real Jordan block is a Jordan block with the scalar \( \lambda \) replaced by the \( 2 \times 2 \) rotation-scaling matrix it needs over \( \nR \), and the superdiagonal \( 1 \) replaced by \( \I_2 \).*

::: {#def-real-jordan-block}
[Rotation-Scaling Block, Real Jordan Block]

Let \( \lambda = a + bi \in \nC \) with \( a, b \in \nR \) and \( b \ne 0 \). The **rotation-scaling block** of the conjugate pair \( \{\lambda, \conj\lambda\} \) is
\[
\vLambda(\lambda) \coloneqq \begin{pmatrix} a & -b \\ b & a \end{pmatrix} \in M_2(\nR) .
\]
For an integer \( k \ge 1 \), the **real Jordan block** of size \( k \) for the pair \( \{\lambda, \conj\lambda\} \) is the matrix \( \C_k(\lambda) \in M_{2k}(\nR) \), partitioned into \( k \times k \) blocks of size \( 2 \times 2 \), with \( \vLambda(\lambda) \) in every diagonal block, \( \I_2 \) in every **superdiagonal** block, and the zero matrix elsewhere:
\[
\C_k(\lambda) \coloneqq \begin{pmatrix} \vLambda(\lambda) & \I_2 & & \\ & \vLambda(\lambda) & \ddots & \\ & & \ddots & \I_2 \\ & & & \vLambda(\lambda) \end{pmatrix} .
\]
A **real Jordan matrix** is a direct sum of ordinary Jordan blocks \( \J_k(\mu) \) with \( \mu \in \nR \) and real Jordan blocks \( \C_k(\lambda) \) with \( \lambda \notin \nR \) and \( \operatorname{Im}\lambda > 0 \).
:::

In words: \( \C_k(\lambda) \) is built exactly like \( \J_k(\lambda) \) (@def-jordan-block), but every entry of \( \J_k(\lambda) \) is replaced by a \( 2 \times 2 \) block — the diagonal \( \lambda \) by \( \vLambda(\lambda) \), the superdiagonal \( 1 \) by \( \I_2 \), and each \( 0 \) by the \( 2 \times 2 \) zero matrix. It has size \( 2k \), not \( k \). The last clause matters: \( \vLambda(\conj\lambda) = \vLambda(\lambda)\tp \), so the pair \( \{\lambda, \conj\lambda\} \) offers two candidate blocks of each size, and a real Jordan matrix is required to use the member with \( b > 0 \), which makes \( \vLambda(\lambda) \) a rotation through a positive angle. Without that normalization the uniqueness below would fail, since \( \C_k(\lambda) \) and \( \C_k(\conj\lambda) \) are similar over \( \nR \).

**Examples.**

- **Size one.** \( \C_1(\lambda) = \vLambda(\lambda) \). For \( \lambda = i \) this is the rotation \( \R \) above; for \( \lambda = 2 + 3i \) it is \( \begin{pmatrix} 2 & -3 \\ 3 & 2 \end{pmatrix} \).
- **Size two.** For \( \lambda = 1 + i \),
  \[
  \C_2(1 + i) = \begin{pmatrix} 1 & -1 & 1 & 0 \\ 1 & 1 & 0 & 1 \\ 0 & 0 & 1 & -1 \\ 0 & 0 & 1 & 1 \end{pmatrix} \in M_4(\nR).
  \]
  Its characteristic polynomial is \( \big((x-1)^2 + 1\big)^2 = (x^2 - 2x + 2)^2 \), by @thm-det-block-triangular applied to the block upper triangular shape.
- **A real Jordan matrix mixing the two kinds.** \( \J_2(3) \oplus \C_1(i) \in M_4(\nR) \) has characteristic polynomial \( (x - 3)^2(x^2 + 1) \).

**Non-example by minimal change.** Change the sign of the lower-left entry: \( \begin{pmatrix} a & -b \\ -b & a \end{pmatrix} \) is still real, still has trace \( 2a \), and looks just as harmless. But it is symmetric, its characteristic polynomial is \( (x - a)^2 - b^2 \), and its eigenvalues \( a \pm b \) are **real**; for \( a = 0, b = 1 \) it is the coordinate swap, which is diagonalizable over \( \nR \). The clause that fails is that the two off-diagonal entries must have **opposite** signs; that is what makes the eigenvalues non-real.

**Why this definition.** Two conventions are being fixed, and both are only conventions. First, the sign of \( b \): replacing \( \vLambda(\lambda) \) by \( \vLambda(\conj\lambda) = \vLambda(\lambda)\tp \) amounts to changing the sign of every second basis vector, so the two choices give similar matrices. Second, the ones: a real Jordan block could be written with \( \I_2 \) below the diagonal instead, giving the transpose. What is **not** a convention is the size: a conjugate pair cannot be carried by a \( 1 \times 1 \) real block, because a \( 1 \times 1 \) real matrix has a real eigenvalue.

The following computation is the whole idea of the section, and we will use it twice: once to see what \( \C_k(\lambda) \) is over \( \nC \), and once to build the real basis.

::: {#lem-realify-jordan-chain}
[Realifying a Conjugate Pair of Chains]

Let \( \A \in M_n(\nR) \), let \( \lambda = a + bi \) with \( a, b \in \nR \) and \( b \ne 0 \), and let \( (\w_1, \dots, \w_k) \) be a Jordan chain of \( \A \) for \( \lambda \) in \( \nC^n \), so that
\[
(\A - \lambda \I)\w_1 = \0 \qquad \text{and} \qquad (\A - \lambda \I)\w_j = \w_{j-1} \quad (2 \le j \le k).
\]
Write \( \w_j = \u_j - i\v_j \) with \( \u_j, \v_j \in \nR^n \), and put \( \u_0 = \v_0 = \0 \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \A\u_j = a\u_j + b\v_j + \u_{j-1} \) and \( \A\v_j = -b\u_j + a\v_j + \v_{j-1} \) for \( 1 \le j \le k \);
2. \( (\conj{\w_1}, \dots, \conj{\w_k}) \) is a Jordan chain of \( \A \) for \( \conj\lambda \);
3. the \( 2k \) vectors \( \u_1, \v_1, \dots, \u_k, \v_k \) span, over \( \nC \), the same subspace of \( \nC^n \) as the \( 2k \) vectors \( \w_1, \dots, \w_k, \conj{\w_1}, \dots, \conj{\w_k} \), and one of the two lists is linearly independent over \( \nC \) if and only if the other is;
4. if the \( 2k \) vectors \( \u_1, \v_1, \dots, \u_k, \v_k \) are linearly independent over \( \nR \), then \( U = \Span(\u_1, \v_1, \dots, \u_k, \v_k) \subseteq \nR^n \) is invariant under \( \A \), and the matrix of \( T_{\A}|_U \) in the ordered basis \( (\u_1, \v_1, \dots, \u_k, \v_k) \) is \( \C_k(\lambda) \).
:::
:::

::: {.idea}
For (a), write the chain relation as \( \A\w_j = \lambda\w_j + \w_{j-1} \) and compare real and imaginary parts; since \( \A \) is real, \( \A \) acts on the two parts separately, and the only mixing comes from multiplying by \( a + bi \). The minus sign in \( \w_j = \u_j - i\v_j \) is chosen so that the answer comes out with the signs of \( \vLambda(\lambda) \) rather than its transpose. Part (c) is bookkeeping: \( (\u_j, \v_j) \) and \( (\w_j, \conj{\w_j}) \) are obtained from each other by an invertible \( 2 \times 2 \) matrix of scalars. Part (d) just reads off the columns from (a).
:::

::: {.proof}
(a) Every \( \z \in \nC^n \) is uniquely \( \x + i\y \) with \( \x, \y \in \nR^n \), by @def-complex-numbers applied entry by entry; so \( \u_j, \v_j \) are well defined. The chain relation says \( \A\w_j = \lambda\w_j + \w_{j-1} \) for \( 1 \le j \le k \). Expanding both sides with \( \w_j = \u_j - i\v_j \) and \( \lambda = a + bi \),
\[
\begin{aligned}
\A\u_j - i\A\v_j
  &= (a + bi)(\u_j - i\v_j) + \u_{j-1} - i\v_{j-1} \\
  &= \big(a\u_j + b\v_j + \u_{j-1}\big) + i\big(b\u_j - a\v_j - \v_{j-1}\big),
\end{aligned}
\]
where we used \( i^2 = -1 \) and, on the left, that \( \A \) has real entries, so \( \A(\u_j - i\v_j) = \A\u_j - i\A\v_j \) with \( \A\u_j, \A\v_j \in \nR^n \). Comparing real parts gives the first identity, and comparing imaginary parts gives \( -\A\v_j = b\u_j - a\v_j - \v_{j-1} \), that is, the second.

(b) Conjugating the identity \( (\A - \lambda \I)\w_j = \w_{j-1} \) entry by entry and using that \( \A \) is real, \( \conj{\A\z} = \A\conj{\z} \) and \( \conj{\lambda\z} = \conj\lambda\,\conj{\z} \) for every \( \z \in \nC^n \) (@thm-conjugate-properties (a), (b)). Hence \( (\A - \conj\lambda \I)\conj{\w_j} = \conj{\w_{j-1}} \) for \( j \ge 2 \) and \( (\A - \conj\lambda \I)\conj{\w_1} = \0 \), which is the chain condition for \( \conj\lambda \). (That \( \conj{\w_1} \ne \0 \) follows from \( \w_1 \ne \0 \).)

(c) Since \( \w_j = \u_j - i\v_j \) and \( \conj{\w_j} = \u_j + i\v_j \), we have
\[
\u_j = \tfrac12\big(\w_j + \conj{\w_j}\big), \qquad \v_j = \tfrac{i}{2}\big(\w_j - \conj{\w_j}\big) .
\]
So each vector of either list is a \( \nC \)-combination of the other list, and the two spans agree (@thm-span-preservation). The passage from \( (\w_j, \conj{\w_j}) \) to \( (\u_j, \v_j) \) is given, for each \( j \) separately, by the matrix \( \begin{pmatrix} 1/2 & 1/2 \\ i/2 & -i/2 \end{pmatrix} \) of determinant \( -i/2 \ne 0 \), which is invertible; so the change of lists is an invertible linear substitution of the coefficients, and a non-trivial vanishing combination of one list yields one of the other. Hence one list is independent if and only if the other is.

(d) By (a), every \( \A\u_j \) and every \( \A\v_j \) lies in \( U \), so \( U \) is \( \A \)-invariant (@lem-invariance-on-spanning-list). Order the basis as \( (\u_1, \v_1, \dots, \u_k, \v_k) \) and read off the columns (@def-matrix-of-linear-map). By (a), the column of \( \u_j \) has entry \( a \) at \( \u_j \), \( b \) at \( \v_j \), \( 1 \) at \( \u_{j-1} \) and \( 0 \) elsewhere; the column of \( \v_j \) has \( -b \) at \( \u_j \), \( a \) at \( \v_j \), \( 1 \) at \( \v_{j-1} \) and \( 0 \) elsewhere. Grouping the basis into the consecutive pairs \( (\u_j, \v_j) \), the \( (j, j) \) block is \( \begin{pmatrix} a & -b \\ b & a \end{pmatrix} = \vLambda(\lambda) \), the \( (j-1, j) \) block is \( \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \I_2 \), and all other blocks are zero. That is \( \C_k(\lambda) \) (@def-real-jordan-block).
:::

Applying the lemma to the block itself tells us what a real Jordan block looks like over \( \nC \).

::: {#cor-real-block-complex-jordan}
[A Real Jordan Block Splits into Two Complex Ones]

Let \( \lambda \notin \nR \) and \( k \ge 1 \). Then, as matrices over \( \nC \),
\[
\C_k(\lambda) \sim \J_k(\lambda) \oplus \J_k(\conj\lambda) .
\]
In particular \( p_{\C_k(\lambda)} = \big((x - \lambda)(x - \conj\lambda)\big)^{k} \), the polynomial \( \big((x-a)^2 + b^2\big)^k \in \nR[x] \), and \( m_{\C_k(\lambda)} \) is the same polynomial.
:::

::: {.proof}
Put \( \A = \C_k(\lambda) \in M_{2k}(\nR) \) and let \( (\u_1, \v_1, \dots, \u_k, \v_k) \) be the standard basis of \( \nR^{2k} \) in this order. Reading the columns of \( \C_k(\lambda) \) gives exactly the identities of @lem-realify-jordan-chain (a). Put \( \w_j = \u_j - i\v_j \), so that \( \w_1 = \e_1 - i\e_2 \ne \0 \). Combining the two real identities,
\[
\begin{aligned}
\A\w_j = \A\u_j - i\A\v_j
  &= (a\u_j + b\v_j + \u_{j-1}) - i(-b\u_j + a\v_j + \v_{j-1}) \\
  &= (a + bi)\u_j + (b - ai)\v_j + \w_{j-1} \\
  &= \lambda\w_j + \w_{j-1},
\end{aligned}
\]
since \( \lambda(-i\v_j) = (b - ai)\v_j \). So \( (\w_1, \dots, \w_k) \) is a Jordan chain of \( \A \) for \( \lambda \), and by (b) so is \( (\conj{\w_1}, \dots, \conj{\w_k}) \) for \( \conj\lambda \). By (c), the \( 2k \) vectors \( \w_1, \dots, \w_k, \conj{\w_1}, \dots, \conj{\w_k} \) are independent over \( \nC \), because the standard basis is; being \( 2k \) independent vectors in \( \nC^{2k} \), they form a basis (@thm-right-size-basis (a)). On the span of one chain, \( \A - \lambda \I \) has matrix \( \J_k(0) \) by @lem-jordan-chain-independent (b), so \( \A \) has matrix \( \lambda \I_k + \J_k(0) = \J_k(\lambda) \) there, the matrix of a sum of operators being the sum of their matrices (@thm-linear-maps-isomorphic-to-matrices, @def-jordan-block); likewise \( \J_k(\conj\lambda) \) on the span of the conjugate chain. By @thm-direct-sum-invariant-block-diagonal the matrix of \( T_{\A} \) in the combined basis is \( \J_k(\lambda) \oplus \J_k(\conj\lambda) \). Hence \( \C_k(\lambda) \sim \J_k(\lambda) \oplus \J_k(\conj\lambda) \) over \( \nC \) (@thm-similar-iff-same-operator).

The characteristic polynomial of \( \J_k(\mu) \) is \( (x - \mu)^k \) (@thm-det-triangular), and similar matrices have the same characteristic polynomial (@thm-charpoly-similarity-invariant), so \( p_{\C_k(\lambda)} = (x - \lambda)^k(x - \conj\lambda)^k \). For the minimal polynomial, \( m_{\J_k(\mu)} = (x - \mu)^k \) by @cor-jordan-invariants (c), a single Jordan block being a Jordan form of itself with one block, of size \( k \); so \( m_{\C_k(\lambda)} = \operatorname{lcm}\big((x-\lambda)^k, (x - \conj\lambda)^k\big) = (x-\lambda)^k(x - \conj\lambda)^k \) by @prp-minimal-polynomial-block-diagonal and @thm-minimal-polynomial-similarity, the factors being powers of distinct irreducibles.
:::

::: {.check}
What are the complex eigenvalues of \( \C_2(1 + i) \), with their algebraic and geometric multiplicities?
:::

::: {.solution}
By @cor-real-block-complex-jordan, \( \C_2(1+i) \sim \J_2(1+i) \oplus \J_2(1-i) \) over \( \nC \). So the eigenvalues are \( 1 \pm i \), each with \( a(\lambda) = 2 \) (the total size of its blocks) and \( g(\lambda) = 1 \) (the number of its blocks), by @cor-jordan-invariants (a), (b).
:::

## The real Jordan form

Two facts about real matrices are needed before the theorem. The first is that a real matrix has the same kernel over \( \nR \) as over \( \nC \), in the sense that a real basis of the one is a complex basis of the other. Once one knows that \( \tilde U \) is the complexification of \( U \) inside \( \nC^n = (\nR^n)_\nC \) (@def-complexification, @exm-complexification-rn), this is @thm-complexification-basis. It is worth proving directly, because the identification is itself part of what has to be checked, and because the statement is used both to find the real chains and to compare ranks.

::: {#lem-real-null-space-complexifies}
[Real and Complex Null Spaces of a Real Matrix]

Let \( \M \in M_n(\nR) \), let \( U = \{\, \x \in \nR^n : \M\x = \0 \,\} \) be its null space over \( \nR \), and let \( \tilde U = \{\, \z \in \nC^n : \M\z = \0 \,\} \) be its null space over \( \nC \). Then:

::: {.enumerate options="label=(\alph*)"}
1. for \( \z = \x + i\y \) with \( \x, \y \in \nR^n \): \( \z \in \tilde U \) if and only if \( \x \in U \) and \( \y \in U \);
2. every basis of \( U \) over \( \nR \) is a basis of \( \tilde U \) over \( \nC \); in particular \( \dim_\nR U = \dim_\nC \tilde U \) and \( \rank \M \) is the same computed over \( \nR \) and over \( \nC \).
:::
:::

::: {.proof}
(a) Since \( \M \) is real, \( \M\z = \M\x + i\M\y \) with \( \M\x, \M\y \in \nR^n \). By the uniqueness of real and imaginary parts (@def-complex-numbers), \( \M\z = \0 \) if and only if \( \M\x = \0 \) and \( \M\y = \0 \).

(b) Let \( (\x_1, \dots, \x_r) \) be a basis of \( U \) over \( \nR \). *Spanning.* Let \( \z = \x + i\y \in \tilde U \). By (a), \( \x, \y \in U \), so \( \x = \sum_j c_j\x_j \) and \( \y = \sum_j d_j\x_j \) with \( c_j, d_j \in \nR \); hence \( \z = \sum_j (c_j + id_j)\x_j \). *Independence.* Let \( \sum_j \alpha_j\x_j = \0 \) with \( \alpha_j = c_j + id_j \in \nC \). Separating real and imaginary parts, which is legitimate because the \( \x_j \) are real, gives \( \sum_j c_j\x_j = \0 \) and \( \sum_j d_j\x_j = \0 \); independence over \( \nR \) forces every \( c_j = d_j = 0 \). So \( (\x_1, \dots, \x_r) \) is a basis of \( \tilde U \) and \( \dim_\nC \tilde U = r = \dim_\nR U \). The rank statement follows from @thm-rank-nullity-matrix over each field.
:::

Now the theorem. Read it as the Jordan form with one amendment: a conjugate pair of complex blocks of size \( k \) is replaced by a single real block of size \( 2k \).

*Every real matrix is similar, over the reals, to a direct sum of Jordan blocks for its real eigenvalues and real Jordan blocks for its conjugate pairs, and that matrix is unique up to the order of its blocks.*

::: {#thm-real-jordan-form}
[Real Jordan Form]

Let \( \A \in M_n(\nR) \) with \( n \ge 1 \). List the eigenvalues of \( \A \) in \( \nC \) as
\[
\begin{aligned}
&\mu_1, \dots, \mu_p \in \nR \quad\text{(the real ones, distinct)}, \\
&\lambda_1, \conj{\lambda_1}, \dots, \lambda_q, \conj{\lambda_q} \quad\text{(the conjugate pairs, with } \operatorname{Im}\lambda_t > 0).
\end{aligned}
\]

::: {.enumerate options="label=(\alph*)"}
1. **(Existence)** There is an invertible \( \P \in M_n(\nR) \) such that \( \P^{-1}\A \P \) is a real Jordan matrix (@def-real-jordan-block), in which the blocks for a real eigenvalue \( \mu_l \) are ordinary Jordan blocks \( \J_k(\mu_l) \) and the blocks for a pair \( \{\lambda_t, \conj{\lambda_t}\} \) are real Jordan blocks \( \C_k(\lambda_t) \).
2. **(Uniqueness)** In any such matrix, the number of blocks \( \J_k(\mu) \) with \( k \ge j \), for \( \mu \in \nR \), and the number of blocks \( \C_k(\lambda) \) with \( k \ge j \), for \( \lambda \notin \nR \), both equal
   \[
   \rank(\A - \nu \I)^{j-1} - \rank(\A - \nu \I)^{j} \qquad (\nu = \mu \text{ resp. } \nu = \lambda),
   \]
   the ranks being computed over \( \nC \) in the second case. Consequently the real Jordan matrix is determined by \( \A \) up to the order of its blocks.
:::
:::

::: {.idea}
Work over \( \nC \), then come home. ① Split \( \nC^n = \bigoplus G_\nu(\A) \) over all complex eigenvalues \( \nu \) (@thm-generalized-eigenspace-decomposition). ② For a **real** eigenvalue, the generalized eigenspace is the complexification of a real subspace, by @lem-real-null-space-complexifies, and Section 2's structure theorem runs over \( \nR \) on that real subspace: nothing complex is needed. ③ For a **pair**, choose the chains in \( G_{\lambda_t} \) freely, and take their conjugates in \( G_{\conj{\lambda_t}} \) — no choice there. ④ Replace each conjugate pair of chains by its real and imaginary parts; @lem-realify-jordan-chain says the new matrix is \( \C_k(\lambda_t) \), and a count shows the real vectors collected are exactly \( n \) in number and independent. Uniqueness is the uniqueness of the complex Jordan form, since by @cor-real-block-complex-jordan a real Jordan matrix has a known complex Jordan form.
:::

::: {.proof}
Since \( p_{\A} \in \nR[x] \subseteq \nC[x] \) has degree \( n \ge 1 \), it splits over \( \nC \) (@cor-complex-polynomial-splits), and its non-real roots come in conjugate pairs with equal multiplicities (@thm-real-matrix-complex-eigenvalues (a)); so the list of eigenvalues has the displayed shape. Write \( a(\nu) \) for the algebraic multiplicity of \( \nu \) in \( p_{\A} \), so \( a(\lambda_t) = a(\conj{\lambda_t}) \) and
\[
\sum_{l=1}^{p} a(\mu_l) + \sum_{t=1}^{q} 2a(\lambda_t) = n . \tag{$\ast$}
\]
By @thm-generalized-eigenspace-decomposition applied to \( T_{\A} \) over \( \nC \),
\[
\nC^n = \bigoplus_{l=1}^{p} G_{\mu_l}(\A) \ \oplus\ \bigoplus_{t=1}^{q}\big(G_{\lambda_t}(\A) \oplus G_{\conj{\lambda_t}}(\A)\big),
\]
with \( \dim_\nC G_\nu(\A) = a(\nu) \) and \( G_\nu(\A) = \ker(\A - \nu \I)^n \) (@cor-generalized-eigenspace-is-kernel (a)).

**Step 1. Real eigenvalues, handled entirely over \( \nR \).** Fix a real eigenvalue \( \mu = \mu_l \). The matrix \( (\A - \mu \I)^{n} \) is real, so by @lem-real-null-space-complexifies its real null space
\[
U_\mu \coloneqq \{\, \x \in \nR^n : (\A - \mu \I)^{n}\x = \0 \,\}
\]
has a real basis which is a \( \nC \)-basis of \( G_\mu(\A) \); in particular \( \dim_\nR U_\mu = a(\mu) \). The subspace \( U_\mu \) is \( \A \)-invariant, since \( (\A - \mu \I)^n(\A\x) = \A(\A - \mu \I)^n\x = \0 \) for \( \x \in U_\mu \) (@thm-kernel-image-of-polynomial-invariant (b)), and \( N_\mu \coloneqq (\A - \mu \I)|_{U_\mu} \) satisfies \( N_\mu^{\,n} = 0 \), so \( N_\mu \) is nilpotent (@def-nilpotent). By @thm-nilpotent-structure there is a basis \( \sB_\mu \) of the **real** space \( U_\mu \), a concatenation of Jordan chains of \( N_\mu \), with \( [N_\mu]_{\sB_\mu} = \J_{k_1}(0) \oplus \dots \oplus \J_{k_s}(0) \). Since \( T_{\A}|_{U_\mu} = \mu\,\id_{U_\mu} + N_\mu \) and \( [\id_{U_\mu}]_{\sB_\mu} = \I_{k_1} \oplus \dots \oplus \I_{k_s} \), adding the matrices (@thm-linear-maps-isomorphic-to-matrices) blockwise (@thm-block-diagonal-arithmetic (a), @def-jordan-block) gives
\[
[T_{\A}|_{U_\mu}]_{\sB_\mu} = \J_{k_1}(\mu) \oplus \dots \oplus \J_{k_s}(\mu),
\]
a direct sum of ordinary Jordan blocks. Moreover \( \sB_\mu \), viewed in \( \nC^n \), is a Jordan basis of \( G_\mu(\A) \) for \( T_{\A} \) over \( \nC \): the chain relations are the same equations, and \( \sB_\mu \) is a \( \nC \)-basis of \( G_\mu(\A) \) by @lem-real-null-space-complexifies (b).

**Step 2. Conjugate pairs, chosen on one side.** Fix \( t \) and write \( \lambda = \lambda_t \), \( G = G_\lambda(\A) \), \( \conj G = G_{\conj\lambda}(\A) \). By @thm-generalized-eigenspace-decomposition (d), \( (\A - \lambda \I)|_{G} \) is nilpotent, so @thm-nilpotent-structure provides chains whose concatenation is a \( \nC \)-basis of \( G \); as in Step 1 these are Jordan chains of \( \A \) for \( \lambda \), of lengths \( k_1, \dots, k_m \) summing to \( a(\lambda) \).

*Claim: conjugating gives a Jordan basis of \( \conj G \).* Indeed, conjugation maps \( G \) onto \( \conj G \): if \( (\A - \lambda \I)^n\z = \0 \), then \( (\A - \conj\lambda \I)^n\conj\z = \0 \) by the computation in @lem-realify-jordan-chain (b), and conjugating twice returns \( \z \). If \( (\z_1, \dots, \z_d) \) is a \( \nC \)-basis of \( G \), then \( (\conj{\z_1}, \dots, \conj{\z_d}) \) spans \( \conj G \) — any \( \z \in \conj G \) has \( \conj\z \in G \), say \( \conj\z = \sum_j c_j\z_j \), whence \( \z = \sum_j \conj{c_j}\,\conj{\z_j} \) — and it has \( d = \dim_\nC \conj G \) entries, so it is a basis (@thm-right-size-basis (b)). Applying this to the concatenated chains, and using @lem-realify-jordan-chain (b) chain by chain, the conjugated chains form a Jordan basis of \( \conj G \) consisting of chains for \( \conj\lambda \) of the same lengths \( k_1, \dots, k_m \).

**Step 3. Realify each pair of conjugate chains.** Keep \( t \) fixed and let \( (\w_1, \dots, \w_k) \) be one of the chains of Step 2, with \( \w_j = \u_j - i\v_j \), \( \u_j, \v_j \in \nR^n \). By @lem-realify-jordan-chain (c), the \( 2k \) real vectors \( \u_1, \v_1, \dots, \u_k, \v_k \) have the same \( \nC \)-span as the \( 2k \) chain vectors \( \w_1, \dots, \w_k, \conj{\w_1}, \dots, \conj{\w_k} \). Do this for each of the \( m \) chains attached to \( \lambda_t \), and for each \( t \).

**Step 4. The collected real vectors form a basis of \( \nR^n \).** Let \( \sB \) be the list obtained by writing, one after another: the real Jordan bases \( \sB_{\mu_1}, \dots, \sB_{\mu_p} \) of Step 1, and then, for each \( t \) and each chain of Step 2, the block of \( 2k \) real vectors of Step 3. Its length is
\[
\sum_{l=1}^{p} a(\mu_l) + \sum_{t=1}^{q} \sum_{\text{chains}} 2k = \sum_{l=1}^{p}a(\mu_l) + \sum_{t=1}^{q}2a(\lambda_t) = n
\]
by \( (\ast) \), since the chain lengths for \( \lambda_t \) sum to \( a(\lambda_t) \). Its \( \nC \)-span contains a \( \nC \)-basis of each \( G_{\mu_l}(\A) \) (Step 1) and, for each \( t \), all the vectors \( \w_j \) and \( \conj{\w_j} \) (Step 3), which together form a \( \nC \)-basis of \( G_{\lambda_t}(\A) \oplus G_{\conj{\lambda_t}}(\A) \) by Step 2. So the \( \nC \)-span of \( \sB \) is all of \( \nC^n \), and \( \sB \) has exactly \( n \) entries, so \( \sB \) is a \( \nC \)-basis of \( \nC^n \) (@thm-right-size-basis (b)). In particular \( \sB \) is linearly independent over \( \nC \), hence over \( \nR \), and being a list of \( n \) independent vectors in \( \nR^n \) it is a basis of \( \nR^n \) (@thm-right-size-basis (a)).

**Step 5. The matrix.** Each segment of \( \sB \) spans an \( \A \)-invariant real subspace: the spaces \( U_{\mu_l} \) by Step 1, and the spaces \( U \) of @lem-realify-jordan-chain (d) by Step 3 and the independence just proved. Their direct sum is \( \nR^n \), since \( \sB \) is a basis. By @thm-direct-sum-invariant-block-diagonal, \( [T_{\A}]_{\sB} \) is block diagonal with the matrices of the restrictions as diagonal blocks, which are \( \J_k(\mu_l) \)'s by Step 1 and \( \C_k(\lambda_t) \)'s by @lem-realify-jordan-chain (d). Taking \( \P \) to be the real matrix whose columns are the vectors of \( \sB \) gives \( \P^{-1}\A \P = [T_{\A}]_{\sB} \) (@thm-similar-iff-same-operator), which proves (a).

(b) Let \( \B = \P^{-1}\A \P \) be any real Jordan matrix similar to \( \A \) over \( \nR \), and regard the similarity over \( \nC \). By @cor-real-block-complex-jordan and @thm-block-diagonal-arithmetic, replacing each block \( \C_k(\lambda) \) of \( \B \) by \( \J_k(\lambda) \oplus \J_k(\conj\lambda) \) produces a Jordan matrix similar to \( \B \), hence to \( \A \), over \( \nC \). By @thm-jordan-canonical-form (b), for every \( \nu \in \nC \) and \( j \ge 1 \) the number of blocks \( \J_k(\nu) \) with \( k \ge j \) in that Jordan matrix equals \( \rank(\A - \nu \I)^{j-1} - \rank(\A - \nu \I)^{j} \), computed over \( \nC \). For a real \( \mu \), the blocks \( \J_k(\mu) \) of the Jordan matrix are exactly the blocks \( \J_k(\mu) \) of \( \B \), since the replaced blocks contribute only non-real eigenvalues; and the ranks over \( \nC \) agree with the ranks over \( \nR \) by @lem-real-null-space-complexifies (b), applied to the real matrix \( (\A - \mu \I)^j \). For \( \lambda \notin \nR \) with \( \operatorname{Im}\lambda > 0 \), the blocks \( \J_k(\lambda) \) of the Jordan matrix come one each from the blocks \( \C_k(\lambda) \) of \( \B \): a block \( \C_k(\lambda') \) of \( \B \) with \( \lambda' \ne \lambda \) contributes \( \J_k(\lambda') \) and \( \J_k(\conj{\lambda'}) \), and \( \conj{\lambda'} \ne \lambda \) because \( \lambda \) and \( \lambda' \) both have **positive** imaginary part (@def-real-jordan-block). In both cases the count is determined by \( \A \), so any two real Jordan matrices similar to \( \A \) have the same blocks up to order.
:::

So over \( \nR \) the dream of Chapter 3 comes true in the amended form: **every real square matrix is similar over \( \nR \) to a matrix that is block diagonal with blocks \( \J_k(\mu) \) and \( \C_k(\lambda) \)**, and the only new feature is the \( 2 \times 2 \) rotation-scaling block. Counting: a real eigenvalue \( \mu \) contributes \( a(\mu) \) to the size and \( g(\mu) \) blocks; a pair \( \{\lambda, \conj\lambda\} \) contributes \( 2a(\lambda) \) to the size and \( g(\lambda) \) real blocks. For an operator \( T \) on a real vector space \( V \) the same statement holds, applied to \( [T]_{\sC} \) for any basis \( \sC \) of \( V \): the theorem produces a real Jordan matrix similar to it, hence equal to \( [T]_{\sB} \) for another basis \( \sB \) of \( V \) (@thm-similar-iff-same-operator). The complexification \( V_\nC \) of @def-complexification is where the complex chains live; for \( V = \nR^n \) it is \( \nC^n \) (@exm-complexification-rn), which is the case written out above.

::: {.warning}
**A real Jordan matrix is not triangular, and the real form is not obtained by "ignoring" the imaginary parts.** The real Jordan form of a matrix with a non-real eigenvalue **cannot** be triangular, since a triangular real matrix has its diagonal entries as eigenvalues, all real (@thm-diagonal-of-triangular-form). Nor is \( \vLambda(\lambda) \) a diagonal matrix in disguise: it has no real eigenvector. And the real basis is not the real part of the complex one: each complex chain vector \( \w_j \) contributes **two** real vectors, \( \operatorname{Re}\w_j \) and \( -\operatorname{Im}\w_j \), and dropping either of them destroys the invariance.
:::

::: {#exm-real-jordan-4x4}
[The Real Jordan Form of a \( 4 \times 4 \) Matrix]

Let
\[
\A = \begin{pmatrix} 0 & -1 & 1 & 0 \\ 1 & 0 & 0 & 1 \\ -1 & 0 & 2 & -1 \\ 0 & -1 & 1 & 2 \end{pmatrix} \in M_4(\nR), \qquad p_{\A} = (x^2 - 2x + 2)^2 .
\]
Find the real Jordan form of \( \A \) (@thm-real-jordan-form) and an invertible \( \P \in M_4(\nR) \) with \( \P^{-1}\A \P \) in that form.
:::

::: {.solution}
*The eigenvalues.* \( x^2 - 2x + 2 = (x-1)^2 + 1 \) has roots \( 1 \pm i \), so over \( \nC \) the eigenvalues are \( \lambda = 1 + i \) and \( \conj\lambda = 1 - i \), each with \( a(\lambda) = 2 \). There is no real eigenvalue, so the real Jordan form consists of real blocks \( \C_k(1+i) \) only, with sizes \( k \) summing to \( a(\lambda) = 2 \).

*A chain for \( \lambda = 1 + i \).* Put \( \M = \A - (1+i)\I \), so that
\[
\M = \begin{pmatrix} -1-i & -1 & 1 & 0 \\ 1 & -1-i & 0 & 1 \\ -1 & 0 & 1-i & -1 \\ 0 & -1 & 1 & 1-i \end{pmatrix}.
\]
Solve \( \M\z = \0 \) using rows \( 2 \), \( 1 \) and \( 4 \) in that order. Row \( 2 \) gives \( z_1 = (1+i)z_2 - z_4 \); row \( 1 \) gives \( z_3 = (1+i)z_1 + z_2 \). Substituting the first into the second, and writing \( s = z_2 \), \( u = z_4 \),
\[
z_1 = (1+i)s - u, \qquad z_3 = (1+i)\big((1+i)s - u\big) + s = (1 + 2i)s - (1+i)u ,
\]
using \( (1+i)^2 = 2i \). Row \( 4 \) reads \( -z_2 + z_3 + (1-i)z_4 = 0 \), which becomes
\[
-s + (1+2i)s - (1+i)u + (1-i)u = 2is - 2iu = 0 ,
\]
so \( s = u \). Row \( 3 \) is then automatic: with \( s = u = 1 \) we get \( \z = (i, 1, i, 1) \), and row \( 3 \) gives \( -i + (1-i)i - 1 = -i + i + 1 - 1 = 0 \). So
\[
\ker \M = \Span\big((i, 1, i, 1)\big), \qquad g(\lambda) = 1 .
\]
Hence there is exactly one \( \lambda \)-block over \( \nC \) (@cor-jordan-invariants (b)), of size \( a(\lambda) = 2 \), and the real Jordan form is \( \C_2(1 + i) \). For the basis we need the chain: take \( \w_1 = (i, 1, i, 1) \) and solve \( \M\w_2 = \w_1 \). Try \( \w_2 = (0, 0, z_3, z_4) \), so that only columns \( 3 \) and \( 4 \) of \( \M \) are used. Row \( 1 \) then reads \( z_3 = i \) and row \( 2 \) reads \( z_4 = 1 \), so \( \w_2 = (0, 0, i, 1) \) is the only candidate of this shape. Rows \( 3 \) and \( 4 \) confirm it:
\[
(1 - i)i - 1 = (i + 1) - 1 = i \quad\text{and}\quad i + (1 - i) = 1 ,
\]
which are the third and fourth entries of \( \w_1 \). So \( (\w_1, \w_2) \) is a Jordan chain of \( \A \) for \( 1 + i \).

*Normalizing the chain.* If \( (\w_1, \w_2) \) is a chain, so is \( (c\w_1, c\w_2) \) for any \( c \ne 0 \), since the chain relations are linear. Taking \( c = -i \) clears the denominators of the realification:
\[
\w_1' = -i(i,1,i,1) = (1, -i, 1, -i), \qquad \w_2' = -i(0,0,i,1) = (0, 0, 1, -i).
\]
Now read off \( \w_j' = \u_j - i\v_j \) with \( \u_j, \v_j \) real, as @lem-realify-jordan-chain requires:
\[
\u_1 = (1,0,1,0), \quad \v_1 = (0,1,0,1), \qquad \u_2 = (0,0,1,0), \quad \v_2 = (0,0,0,1).
\]

*The answer.* With \( \sB = (\u_1, \v_1, \u_2, \v_2) \),
\[
\P = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \end{pmatrix}, \qquad \P^{-1}\A \P = \C_2(1+i) = \begin{pmatrix} 1 & -1 & 1 & 0 \\ 1 & 1 & 0 & 1 \\ 0 & 0 & 1 & -1 \\ 0 & 0 & 1 & 1 \end{pmatrix} .
\]
\( \P \) is lower triangular with ones on the diagonal, so \( \det \P = 1 \) (@thm-det-triangular) and \( \P \) is invertible.

*The check, column by column.* Writing \( \c_1, \dots, \c_4 \) for the columns of \( \P \), the identity \( \A \P = \P\,\C_2(1+i) \) says
\[
\begin{aligned}
\A\c_1 &= \c_1 + \c_2, \\
\A\c_2 &= -\c_1 + \c_2, \\
\A\c_3 &= \c_1 + \c_3 + \c_4, \\
\A\c_4 &= \c_2 - \c_3 + \c_4 ,
\end{aligned}
\]
read off the four columns of \( \C_2(1+i) \); these are exactly the identities of @lem-realify-jordan-chain (a) with \( a = b = 1 \). Two of them in full:
\[
\begin{aligned}
\A\c_1 = \A(1,0,1,0)
  &= (0 + 1,\ 1 + 0,\ -1 + 2,\ 0 + 1) = (1,1,1,1) \\
  &= (1,0,1,0) + (0,1,0,1) = \c_1 + \c_2,
\end{aligned}
\]
adding columns \( 1 \) and \( 3 \) of \( \A \); and
\[
\begin{aligned}
\A\c_3 = \A(0,0,1,0)
  &= (1, 0, 2, 1) = (1,0,1,0) + (0,0,1,0) + (0,0,0,1) \\
  &= \c_1 + \c_3 + \c_4 ,
\end{aligned}
\]
the third column of \( \A \). The remaining two are the same kind of one-line computation.

*Cross-checks.* \( \tr \A = 0 + 0 + 2 + 2 = 4 \) and \( \tr \C_2(1+i) = 4 \cdot 1 = 4 \). Over \( \nC \), @cor-real-block-complex-jordan gives the complex Jordan form \( \J_2(1+i) \oplus \J_2(1-i) \), whose characteristic polynomial is \( \big((x-1)^2+1\big)^2 = p_{\A} \).
:::

## The Weyr form

The Jordan form of a nilpotent operator is the Young diagram of Section 2 read **by rows**: one row per chain, one block per row. The same diagram can be read **by columns**, and the columns are the jumps of the kernel chain (@def-partition-of-n and the discussion after @thm-nilpotent-block-sizes-from-ranks). Reordering a Jordan basis accordingly costs nothing and gives a second normal form, the Weyr form. It carries exactly the same information — a partition for each eigenvalue — but it wears it differently, and for one purpose it is strictly better: the matrices that commute with a Weyr matrix are block upper triangular, which is false for the Jordan form.

Here is the diagram for the partition \( (2, 2, 1) \) of \( 5 \), whose dual partition is \( (3, 2) \):

\begin{center}
\begin{tikzpicture}[scale=0.62, every node/.style={font=\small}]
  \foreach \r/\len in {0/2, 1/2, 2/1} {
    \foreach \c in {1,...,\len} {
      \draw (\c-1, -\r) rectangle ++(1,-1);
    }
  }
  \draw[very thick] (0,0) rectangle (1,-3);
  \draw[very thick] (1,0) rectangle (2,-2);
  \node at (0.5,0.75) {$w_1 = 3$};
  \node at (1.5,0.75) {$w_2 = 2$};
  \node at (-1.4,-0.5) {$k_1 = 2$};
  \node at (-1.4,-1.5) {$k_2 = 2$};
  \node at (-1.4,-2.5) {$k_3 = 1$};
  \node[align=left, anchor=west] at (3.2,-1.5) {rows: the Jordan block sizes $(2,2,1)$\\ columns: the Weyr structure $(3,2)$\\ the operator moves each box one step left};
\end{tikzpicture}
\end{center}

The basis is the same; only its order changes. Instead of listing chain by chain, list the first column (a basis of the kernel), then the second column, and so on. Since the operator moves each box one step to the left, it maps the \( j \)-th group of basis vectors into the \( (j-1) \)-th, injectively, and the matrix becomes block upper triangular with a very rigid pattern of ones.

::: {#def-weyr-form}
[Basic Weyr Matrix, Weyr Structure, Weyr Form]

Let \( \lambda \in F \) and let \( w_1 \ge w_2 \ge \dots \ge w_s \ge 1 \) be a partition of an integer \( m \ge 1 \) (@def-partition-of-n). The **basic Weyr matrix** with eigenvalue \( \lambda \) and **Weyr structure** \( (w_1, \dots, w_s) \) is the matrix \( \W \in M_m(F) \), partitioned into blocks according to \( m = w_1 + \dots + w_s \), whose blocks are
\[
\W_{jj} = \lambda \I_{w_j}, \qquad \W_{j,j+1} = \begin{pmatrix} \I_{w_{j+1}} \\ 0 \end{pmatrix} \in M_{w_j \times w_{j+1}}(F), \qquad \W_{jl} = 0 \ \text{ otherwise} .
\]
A **Weyr matrix** is a direct sum of basic Weyr matrices. A **Weyr form** of \( T \in \cL(V) \) is a Weyr matrix \( \W \) with \( [T]_{\sB} = \W \) for some basis \( \sB \) of \( V \); for \( \A \in M_n(F) \), a Weyr form of \( \A \) is a Weyr matrix similar to \( \A \).
:::

In words: the diagonal blocks are scalar, of the sizes given by the partition, and the only other non-zero blocks sit **immediately to the right** of the diagonal ones, each being an identity matrix stacked on top of a zero block — so \( \W_{j,j+1} \) has full column rank \( w_{j+1} \), which is possible exactly because \( w_j \ge w_{j+1} \). The matrix is upper triangular, with \( \lambda \) repeated \( m \) times on the diagonal.

**Examples.**

- **One column.** If \( s = 1 \), then \( \W = \lambda \I_{w_1} \): a scalar matrix. This is the diagonalizable case.
- **All parts equal to \( 1 \).** If \( w_1 = \dots = w_s = 1 \), then \( \W = \J_s(\lambda) \): a single Jordan block. So Jordan blocks are the basic Weyr matrices of the thinnest possible structure.
- **The structure \( (3, 2) \) with \( \lambda = 5 \).** Here \( m = 5 \) and
  \[
  \W = \begin{pmatrix} 5 & 0 & 0 & 1 & 0 \\ 0 & 5 & 0 & 0 & 1 \\ 0 & 0 & 5 & 0 & 0 \\ 0 & 0 & 0 & 5 & 0 \\ 0 & 0 & 0 & 0 & 5 \end{pmatrix},
  \]
  with the \( 3 \times 2 \) block \( \begin{pmatrix} \I_2 \\ 0 \end{pmatrix} \) in the upper right corner. As we will see, this is the Weyr form of \( \J_2(5) \oplus \J_2(5) \oplus \J_1(5) \), the diagram drawn above.

**Non-example by minimal change.** Put the identity block in the **lower** part of \( \W_{12} \) instead: with structure \( (2,1) \) and \( \lambda = 0 \), compare
\[
\W = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \qquad\text{and}\qquad \W' = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} .
\]
Both are nilpotent of rank \( 1 \), and indeed \( \W \sim \W' \) (@cor-nilpotent-similar-iff-ranks): the shape is not an extra invariant, and the two matrices represent the same operator in different bases. But only \( \W \) is a Weyr matrix. The clause that fails for \( \W' \) is that the block \( \W_{j,j+1} \) must be an identity matrix stacked **on top of** a zero block, not below it. The ordering is a normalization, and it is the one the commutant property below is proved with: there the block \( \W_{j,j+1} \) is canceled on the left, which uses that its columns are the **first** \( w_{j+1} \) standard basis vectors, in order. Concretely, every matrix commuting with \( \W \) turns out to be upper triangular, while the commutant of \( \W' \) contains the matrix unit \( \E_{21} \).

The existence and uniqueness of the form are now a repackaging of Section 3.

::: {#thm-weyr-form}
[Weyr Form]

Let \( V \) be a finite-dimensional vector space over \( F \) with \( \dim V = n \ge 1 \), and let \( T \in \cL(V) \).

::: {.enumerate options="label=(\alph*)"}
1. **(Existence)** \( T \) has a Weyr form if and only if \( p_T \) splits over \( F \). One can be arranged with one basic Weyr block per eigenvalue.
2. **(Uniqueness)** In any Weyr form of \( T \) with one basic block per eigenvalue, the block for \( \lambda \) has Weyr structure
   \[
   w_j = \dim\ker(T - \lambda\,\id_V)^{j} - \dim\ker(T - \lambda\,\id_V)^{j-1} \qquad (j \ge 1),
   \]
   the non-zero terms of this sequence; equivalently \( (w_1, w_2, \dots) \) is the **dual partition** of the partition formed by the sizes of the \( \lambda \)-blocks of the Jordan form of \( T \). So the Weyr form is determined by \( T \) up to the order of its basic blocks.
:::
:::

::: {.idea}
Both parts come from one observation: a Weyr basis is a Jordan basis in a different order. Arrange the \( \lambda \)-chains of a Jordan basis as the rows of the Young diagram, sorted by decreasing length, and read the diagram **column by column**. The operator \( T - \lambda\,\id \) moves each box one step to the left, so it carries the \( j \)-th column into the \( (j-1) \)-th, matching the \( i \)-th box of one with the \( i \)-th box of the other — which is exactly the block \( \begin{pmatrix} \I \\ 0 \end{pmatrix} \). For uniqueness, count the boxes: the first \( j \) columns of the diagram are a basis of \( \ker(T - \lambda\,\id)^j \), so the column lengths are the jumps of the kernel chain.
:::

::: {.proof}
\( (\Rightarrow) \) A Weyr matrix is upper triangular, so if \( T \) has a Weyr form then \( T \) is triangularizable and \( p_T \) splits (@def-triangularizable, @thm-triangularization).

\( (\Leftarrow) \) Suppose \( p_T \) splits, and let \( \lambda \) be an eigenvalue. By @thm-jordan-canonical-form there is a Jordan basis; fix its part inside \( G_\lambda(T) \), a concatenation of Jordan chains of \( N = T - \lambda\,\id_V \) of lengths \( k_1 \ge k_2 \ge \dots \ge k_r \ge 1 \) summing to \( a(\lambda) \) (@thm-nilpotent-structure, after reindexing so that the lengths decrease). Write \( \b_{i,1}, \dots, \b_{i,k_i} \) for the \( i \)-th chain in the order of @def-jordan-chain, so that
\[
N\b_{i,1} = \0, \qquad N\b_{i,j} = \b_{i,j-1} \quad (2 \le j \le k_i) .
\]
Put \( s = k_1 \) and, for \( 1 \le j \le s \), let \( w_j = \#\{\, i : k_i \ge j \,\} \), the length of the \( j \)-th column of the Young diagram; then \( w_1 \ge \dots \ge w_s \ge 1 \) is the dual partition of \( (k_1, \dots, k_r) \) (@def-partition-of-n), a partition of \( a(\lambda) \). Because the \( k_i \) decrease, \( \{\, i : k_i \ge j \,\} = \{1, 2, \dots, w_j\} \). Let
\[
\sC_j = \big(\b_{1,j}, \b_{2,j}, \dots, \b_{w_j, j}\big)
\]
be the \( j \)-th column, and let \( \sB_\lambda \) be the list \( \sC_1, \sC_2, \dots, \sC_s \) written one after another: a reordering of the chosen basis of \( G_\lambda(T) \), hence a basis of it.

Read the columns of \( [T|_{G_\lambda}]_{\sB_\lambda} \). For \( j = 1 \), \( T\b_{i,1} = \lambda\b_{i,1} \). For \( j \ge 2 \), \( T\b_{i,j} = \lambda\b_{i,j} + \b_{i,j-1} \), and \( \b_{i,j-1} \) is the \( i \)-th entry of \( \sC_{j-1} \), which exists because \( i \le w_j \le w_{j-1} \). In the block partition of \( \sB_\lambda \) by the groups \( \sC_1, \dots, \sC_s \), this says: the \( (j,j) \) block is \( \lambda \I_{w_j} \); the \( (j-1,j) \) block sends the \( i \)-th basis vector of group \( j \) to the \( i \)-th of group \( j-1 \) for \( i = 1, \dots, w_j \), so it is \( \begin{pmatrix} \I_{w_j} \\ 0 \end{pmatrix} \); and every other block is \( 0 \). That is the basic Weyr matrix with eigenvalue \( \lambda \) and structure \( (w_1, \dots, w_s) \) (@def-weyr-form). Writing the lists \( \sB_\lambda \) for the distinct eigenvalues one after another and using \( V = \bigoplus_\lambda G_\lambda(T) \) (@thm-generalized-eigenspace-decomposition) with @thm-direct-sum-invariant-block-diagonal, the resulting basis \( \sB \) makes \( [T]_{\sB} \) a direct sum of basic Weyr matrices, one per eigenvalue.

(b) Let \( \W \) be a Weyr form of \( T \) with one basic block per eigenvalue, and fix \( \lambda \) with basic block of structure \( (w_1, \dots, w_s) \) and size \( m \). Let \( \sB \) be a basis with \( [T]_{\sB} = \W \), and name the basis vectors inside the \( \lambda \)-block \( \c_{i,j} \), where \( j \) indexes the groups and \( i = 1, \dots, w_j \) the entries within a group. The blocks of @def-weyr-form say precisely that
\[
N\c_{i,1} = \0, \qquad N\c_{i,j} = \c_{i,j-1} \quad (j \ge 2), \qquad N = T - \lambda\,\id_V ,
\]
while on the span \( V' \) of the basis vectors belonging to the other basic blocks the operator \( N \) is invertible: \( V' \) is \( T \)-invariant and the matrix of \( N|_{V'} \) is \( \W' - \lambda \I \), where \( \W' \) is a direct sum of basic Weyr matrices with eigenvalues \( \mu \ne \lambda \), hence upper triangular with all diagonal entries \( \mu - \lambda \ne 0 \), so of non-zero determinant (@thm-det-triangular, @thm-det-nonzero-iff-invertible). Hence \( N^{j} \) kills \( \c_{i,l} \) for \( l \le j \) and sends \( \c_{i,l} \mapsto \c_{i,l-j} \) for \( l > j \). Write \( V = U \oplus V' \) with \( U = \Span(\c_{i,l}) \); both summands are \( N \)-invariant, so \( \ker N^j = (\ker N^j \cap U) \oplus (\ker N^j \cap V') \), and the second summand is \( \{\0\} \) because \( N^j|_{V'} \) is invertible. Inside \( U \) the displayed action gives
\[
\ker N^{j} = \Span\big(\c_{i,l} : l \le j\big), \qquad \dim\ker N^{j} = w_1 + \dots + w_j
\]
for \( 0 \le j \le s \), the spanning vectors being members of the basis \( \sB \) and hence independent; and \( \ker N^j = \ker N^s \) for \( j \ge s \). Subtracting consecutive values gives \( w_j = \dim\ker N^{j} - \dim\ker N^{j-1} \) as claimed, a number depending only on \( T \) and \( \lambda \). By @cor-jordan-invariants (d) this is also \( \#\{i : k_i \ge j\} \) for the \( \lambda \)-block sizes \( k_i \) of the Jordan form, that is, the dual partition. Since the structures are determined, so is \( \W \) up to the order in which its basic blocks are listed.
:::

Existence and uniqueness are thus free; what makes the form worth the trouble is the next property. Here \( \K \in M_n(F) \) is called **block upper triangular** for a partition \( n = n_1 + \dots + n_s \), taken as both the row and the column partition (@def-block-partition), when every block \( \K_{pq} \) with \( p > q \) is zero; for \( s = 2 \) this is the shape of Chapter 7.

::: {#prp-weyr-commutant}
[The Commutant of a Basic Weyr Matrix Is Block Triangular]

Let \( \W \in M_m(F) \) be a basic Weyr matrix with eigenvalue \( \lambda \) and Weyr structure \( (w_1, \dots, w_s) \), and let \( \K \in M_m(F) \) satisfy \( \W \K = \K \W \). Then \( \K \) is block upper triangular for the partition \( m = w_1 + \dots + w_s \): its blocks \( \K_{pq} \) vanish for \( p > q \).
:::

::: {.idea}
Write both products blockwise. Because \( \W \) has only one non-zero block in each block row, each block equation is short: \( \E_p \K_{p+1,q} = \K_{p,q-1} \E_{q-1} \), where \( \E_j = \begin{pmatrix} \I_{w_{j+1}} \\ 0 \end{pmatrix} \). Every \( \E_j \) has full column rank, so it can be canceled on the left. Now sweep the block columns from left to right: the first block column forces \( \K_{p1} = 0 \) for \( p > 1 \), and each new column is forced by the previous one.
:::

::: {.proof}
Put \( \N = \W - \lambda \I_m \) and \( \E_j = \begin{pmatrix} \I_{w_{j+1}} \\ 0 \end{pmatrix} \in M_{w_j \times w_{j+1}}(F) \) for \( 1 \le j \le s-1 \), so that \( \N \) has blocks \( \N_{j,j+1} = \E_j \) and all other blocks zero (@def-weyr-form). Since \( \lambda \I_m \) commutes with everything, \( \W \K = \K \W \) is equivalent to \( \N\K = \K \N \). Comparing the \( (p,q) \) blocks with @thm-block-multiplication, and reading an undefined symbol as \( 0 \),
\[
\begin{aligned}
\E_p\,\K_{p+1,q} &= (\N\K)_{pq} = (\K \N)_{pq} = \K_{p,q-1}\,\E_{q-1} \\
&\qquad \text{for all } 1 \le p, q \le s.
\end{aligned} \tag{$\ast$}
\]
Each \( \E_j \) is injective as a map \( F^{w_{j+1}} \to F^{w_j} \), so \( \E_j\X = 0 \) forces \( \X = 0 \) for every matrix \( \X \) with \( w_{j+1} \) rows.

We prove \( \K_{pq} = 0 \) for \( p > q \) by induction on \( q \ge 1 \).

*Case \( q = 1 \).* Let \( p > 1 \). Taking the indices \( (p - 1, 1) \) in \( (\ast) \), the right-hand side involves \( \K_{p-1,0} \), which is undefined and therefore read as \( 0 \). So \( \E_{p-1}\K_{p,1} = 0 \), and \( p - 1 \le s - 1 \) makes \( \E_{p-1} \) one of the listed blocks; injectivity gives \( \K_{p,1} = 0 \).

*Induction step.* Let \( q \ge 2 \) and assume \( \K_{p'q'} = 0 \) whenever \( p' > q' \) and \( q' < q \). Let \( p > q \). Taking the indices \( (p-1, q) \) in \( (\ast) \),
\[
\E_{p-1}\K_{pq} = \K_{p-1,q-1}\E_{q-1} .
\]
Here \( p - 1 > q - 1 \) and \( q - 1 < q \), so \( \K_{p-1,q-1} = 0 \) by the induction hypothesis, and the right-hand side is \( 0 \). Again \( 1 \le p - 1 \le s-1 \), so injectivity of \( \E_{p-1} \) gives \( \K_{pq} = 0 \). This completes the induction and the proof.
:::

::: {.remark}
The Jordan form has no such property, which is the reason the Weyr form exists at all. Take \( \J = \J_2(0) \oplus \J_1(0) \) and \( \W \) the Weyr matrix of the same operator, of structure \( (2,1) \):
\[
\J = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}, \qquad \W = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}.
\]
Solving \( \J \K = \K \J \) entry by entry gives the commutant \( \left\{ \begin{pmatrix} a & b & c \\ 0 & a & 0 \\ 0 & h & i \end{pmatrix} \right\} \), which contains matrices with a non-zero entry **below** the diagonal, in position \( (3,2) \): the commutant of \( \J \) is not contained in the upper triangular matrices, and in particular it is not block upper triangular for the Weyr partition \( 3 = 2 + 1 \) of this operator. Solving \( \W \K = \K \W \) gives \( \left\{ \begin{pmatrix} a & b & c \\ 0 & e & f \\ 0 & 0 & a \end{pmatrix} \right\} \), every member of which is upper triangular, in agreement with @prp-weyr-commutant. This is the property that makes the Weyr form the right one when two commuting operators must be brought to normal form at the same time.
:::

::: {.check}
An operator \( T \) on a \( 7 \)-dimensional complex space has one eigenvalue \( \lambda \), with Jordan block sizes \( (3, 2, 1, 1) \). What is the Weyr structure of its Weyr form, and what is \( \dim\ker(T - \lambda\,\id)^2 \)?
:::

::: {.solution}
The Weyr structure is the dual partition: \( w_1 = \#\{i : k_i \ge 1\} = 4 \), \( w_2 = \#\{i : k_i \ge 2\} = 2 \), \( w_3 = \#\{i : k_i \ge 3\} = 1 \), so \( (4, 2, 1) \), a partition of \( 7 \) as it must be. By @thm-weyr-form (b), \( \dim\ker(T - \lambda\,\id)^2 = w_1 + w_2 = 6 \). (Equivalently, \( \sum_i \min(k_i, 2) = 2 + 2 + 1 + 1 = 6 \), by @cor-jordan-invariants (d).)
:::

## Exercises

### A. Check your understanding

:::: {#exr-real-jordan-and-weyr-forms-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Write down \( \vLambda(\lambda) \) for \( \lambda = a + bi \) and \( \C_2(\lambda) \), and say what their sizes are.
2. State the Real Jordan Form Theorem.
3. True or false: every matrix in \( M_n(\nR) \) is similar over \( \nR \) to an upper triangular real matrix. Justify your answer.
4. Let \( \A \in M_6(\nR) \) have complex eigenvalues \( 2, 2, 1 + i, 1 - i, 1 + i, 1 - i \). What are the possible real Jordan forms?
5. Define the Weyr structure of an eigenvalue and say how it is computed from \( T \).
6. What is the Weyr form of \( \J_3(7) \)? And of \( 7\I_3 \)?
:::
::::

::: {.solution}
(a) \( \vLambda(\lambda) = \begin{pmatrix} a & -b \\ b & a \end{pmatrix} \in M_2(\nR) \) and \( \C_2(\lambda) = \begin{pmatrix} \vLambda(\lambda) & \I_2 \\ 0 & \vLambda(\lambda) \end{pmatrix} \in M_4(\nR) \); the real Jordan block \( \C_k(\lambda) \) has size \( 2k \) (@def-real-jordan-block).

(b) Every \( \A \in M_n(\nR) \) is similar, by a **real** invertible matrix, to a direct sum of blocks \( \J_k(\mu) \) for the real eigenvalues \( \mu \) and \( \C_k(\lambda) \) for the conjugate pairs \( \{\lambda, \conj\lambda\} \), and that matrix is unique up to the order of the blocks (@thm-real-jordan-form).

(c) False. A triangular real matrix has real eigenvalues (@thm-diagonal-of-triangular-form), and similar matrices have the same characteristic polynomial (@thm-charpoly-similarity-invariant); so a real matrix with a non-real eigenvalue, such as the rotation by a right angle, is similar to no real triangular matrix.

(d) The real eigenvalue \( 2 \) has \( a(2) = 2 \), so its blocks are \( \J_2(2) \) or \( \J_1(2) \oplus \J_1(2) \). The pair \( \{1 \pm i\} \) has \( a(1+i) = 2 \), so its real blocks are \( \C_2(1+i) \) (size \( 4 \)) or \( \C_1(1+i) \oplus \C_1(1+i) \). That gives four possible real Jordan forms, of total size \( 2 + 4 = 6 \) in each case.

(e) The Weyr structure of \( \lambda \) is the partition \( (w_1, w_2, \dots) \) with \( w_j = \dim\ker(T - \lambda\,\id_V)^j - \dim\ker(T - \lambda\,\id_V)^{j-1} \), that is, the dual partition of the \( \lambda \)-block sizes of the Jordan form (@thm-weyr-form).

(f) \( \J_3(7) \) has one \( 7 \)-block of size \( 3 \), so the Weyr structure is \( (1,1,1) \) and the Weyr form is \( \J_3(7) \) itself. For \( 7\I_3 \) the block sizes are \( (1,1,1) \), the dual partition is \( (3) \), and the Weyr form is \( 7\I_3 \).
:::

### B. Practice

:::: {#exr-real-jordan-and-weyr-forms-b1}
[B1: Real forms of two by two matrices]

For each real matrix, find the complex eigenvalues, the real Jordan form (@thm-real-jordan-form), and an invertible \( \P \in M_2(\nR) \) putting it in that form. Verify \( \A \P = \P\vLambda \) column by column.

::: {.enumerate options="label=(\alph*)"}
1. \( \A_1 = \begin{pmatrix} 1 & 2 \\ -2 & 1 \end{pmatrix} \).
2. \( \A_2 = \begin{pmatrix} 3 & -5 \\ 1 & -1 \end{pmatrix} \).
:::
::::

::: {.solution}
(a) \( p_{\A_1} = x^2 - (\tr \A_1)x + \det \A_1 = x^2 - 2x + 5 = (x-1)^2 + 4 \), so the eigenvalues are \( 1 \pm 2i \) and the real Jordan form is \( \vLambda(1 + 2i) = \begin{pmatrix} 1 & -2 \\ 2 & 1 \end{pmatrix} \). For \( \lambda = 1 + 2i \), \( \A_1 - \lambda \I = \begin{pmatrix} -2i & 2 \\ -2 & -2i \end{pmatrix} \), and the first row gives \( z_2 = iz_1 \); take \( \w = (1, i) \). Then \( \w = \u - i\v \) with \( \u = (1, 0) \) and \( \v = (0, -1) \), so
\[
\P = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \qquad \P^{-1}\A_1\P = \begin{pmatrix} 1 & -2 \\ 2 & 1 \end{pmatrix}.
\]
Check: \( \A_1\u = (1, -2) = \u + 2\v \) and \( \A_1\v = (-2, -1) = -2\u + \v \), which are the two columns of \( \vLambda(1+2i) \) as @lem-realify-jordan-chain (a) predicts with \( a = 1, b = 2 \).

(b) \( p_{\A_2} = x^2 - 2x + (-3 + 5) = x^2 - 2x + 2 \), with roots \( 1 \pm i \); the real Jordan form is \( \vLambda(1 + i) = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} \). For \( \lambda = 1 + i \), the second row of \( \A_2 - \lambda \I = \begin{pmatrix} 2 - i & -5 \\ 1 & -2-i \end{pmatrix} \) gives \( z_1 = (2+i)z_2 \); take \( \w = (2 + i, 1) \). Then \( \u = (2,1) \) and \( \v = -\operatorname{Im}\w = (-1, 0) \), so
\[
\P = \begin{pmatrix} 2 & -1 \\ 1 & 0 \end{pmatrix}, \qquad \det \P = 1, \qquad \P^{-1}\A_2\P = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}.
\]
Check: \( \A_2\u = (6 - 5, 2 - 1) = (1,1) = \u + \v \) and \( \A_2\v = (-3, -1) = -\u + \v \).
:::

:::: {#exr-real-jordan-and-weyr-forms-b2}
[B2: Weyr forms of Jordan matrices]

For each Jordan matrix, write down the block sizes, the Weyr structure of each eigenvalue, and the Weyr form (@thm-weyr-form).

::: {.enumerate options="label=(\alph*)"}
1. \( \J_3(0) \oplus \J_2(0) \oplus \J_1(0) \in M_6(F) \).
2. \( \J_2(4) \oplus \J_1(4) \oplus \J_1(9) \in M_4(F) \).
3. \( \J_2(0) \oplus \J_2(0) \in M_4(F) \).
:::
::::

::: {.solution}
(a) Block sizes \( (3,2,1) \), a partition of \( 6 \). Dual partition: \( w_1 = 3 \), \( w_2 = 2 \), \( w_3 = 1 \). So the Weyr form is the basic Weyr matrix with \( \lambda = 0 \) and structure \( (3,2,1) \),
\[
\W = \begin{pmatrix} 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{pmatrix},
\]
with the \( 3 \times 2 \) block \( \begin{pmatrix} \I_2 \\ 0 \end{pmatrix} \) and the \( 2 \times 1 \) block \( \begin{pmatrix} \I_1 \\ 0 \end{pmatrix} \) above the diagonal. As a check, \( \rank \W = 3 = \rank \J \) and \( \rank \W^2 = 1 = \rank \J^2 \).

(b) For \( \lambda = 4 \): sizes \( (2,1) \), dual \( (2,1) \). For \( \lambda = 9 \): sizes \( (1) \), dual \( (1) \). The Weyr form is the direct sum of the basic blocks,
\[
\begin{pmatrix} 4 & 0 & 1 \\ 0 & 4 & 0 \\ 0 & 0 & 4 \end{pmatrix} \oplus (9) .
\]

(c) Sizes \( (2,2) \), dual \( w_1 = 2 \), \( w_2 = 2 \). The basic Weyr matrix with \( \lambda = 0 \) and structure \( (2,2) \) is
\[
\W = \begin{pmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix},
\]
which is \( \J_2(0) \oplus \J_2(0) \) with its basis reordered as \( (\e_1, \e_3, \e_2, \e_4) \).
:::

:::: {#exr-real-jordan-and-weyr-forms-b3}
[B3: Real forms of three by three matrices from the characteristic polynomial]

For each characteristic polynomial, list all possible real Jordan forms (@thm-real-jordan-form) of a matrix \( \A \in M_3(\nR) \) with that polynomial.

::: {.enumerate options="label=(\alph*)"}
1. \( p_{\A} = (x - 2)(x^2 + 1) \).
2. \( p_{\A} = (x + 1)(x^2 - 2x + 5) \).
3. \( p_{\A} = (x - 1)^3 \).
4. \( p_{\A} = (x^2 + 1)(x - 1) \) but with \( \A \) required to be diagonalizable over \( \nR \). Is this possible?
:::
::::

::: {.solution}
(a) The real eigenvalue \( 2 \) has \( a(2) = 1 \), giving the block \( \J_1(2) = (2) \). The pair \( \{i, -i\} \) has \( a(i) = 1 \), giving \( \C_1(i) = \vLambda(i) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \). So the real Jordan form is \( (2) \oplus \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \), the only possibility.

(b) \( x^2 - 2x + 5 \) has roots \( 1 \pm 2i \), so the form is \( (-1) \oplus \vLambda(1 + 2i) = (-1) \oplus \begin{pmatrix} 1 & -2 \\ 2 & 1 \end{pmatrix} \), again the only possibility.

(c) All eigenvalues are real, so the real Jordan form is an ordinary Jordan form: the \( 1 \)-block sizes form a partition of \( 3 \), giving \( \J_3(1) \), \( \J_2(1) \oplus \J_1(1) \) or \( \I_3 \).

(d) No. A diagonalizable \( \A \in M_3(\nR) \) is similar over \( \nR \) to a diagonal real matrix, whose characteristic polynomial splits over \( \nR \) (@thm-det-triangular); but \( x^2 + 1 \) has no real root. In fact whenever \( \A \) has a non-real eigenvalue its real Jordan form contains a block \( \vLambda(\lambda) \), which is not diagonal.
:::

### C. Going deeper

:::: {#exr-real-jordan-and-weyr-forms-c1}
[C1: The real form of a companion matrix]

Let \( p = (x^2+1)^2 = x^4 + 2x^2 + 1 \in \nR[x] \) and let \( \C = \C(p) \in M_4(\nR) \) be its companion matrix, with \( 1 \) in each position just below the diagonal and last column \( (-1, 0, -2, 0) \) (@exr-characteristic-polynomial-c1).

::: {.enumerate options="label=(\alph*)"}
1. Write down \( \C \), and explain why \( p_{\C} = m_{\C} = p \).
2. Determine the complex Jordan form of \( \C \).
3. Deduce the real Jordan form of \( \C \).
4. Verify your answer by comparing traces and characteristic polynomials.
:::

*Hint: for (b), the exponent of \( x - i \) in \( m_{\C} \) is the largest size of an \( i \)-block.*
::::

::: {.solution}
(a) With \( a_0 = 1 \), \( a_1 = 0 \), \( a_2 = 2 \), \( a_3 = 0 \),
\[
\C = \begin{pmatrix} 0 & 0 & 0 & -1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & -2 \\ 0 & 0 & 1 & 0 \end{pmatrix}.
\]
By @exr-characteristic-polynomial-c1 (b), \( p_{\C} = p \), and by @exr-minimal-polynomial-b3 (d), \( m_{\C} = p \) as well.

(b) Over \( \nC \), \( p = (x - i)^2(x + i)^2 \), so \( a(i) = a(-i) = 2 \). By @cor-jordan-invariants (c), the exponent \( 2 \) of \( x - i \) in \( m_{\C} \) is the largest size of an \( i \)-block; the sizes form a partition of \( 2 \) with largest part \( 2 \), so there is one block \( \J_2(i) \). Likewise one block \( \J_2(-i) \). The complex Jordan form is \( \J_2(i) \oplus \J_2(-i) \).

(c) By @thm-real-jordan-form, the real Jordan form has no ordinary Jordan blocks (there is no real eigenvalue) and one real block per complex \( i \)-block, of the same size parameter. So it is
\[
\C_2(i) = \begin{pmatrix} 0 & -1 & 1 & 0 \\ 1 & 0 & 0 & 1 \\ 0 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0 \end{pmatrix}.
\]
(Consistently, @cor-real-block-complex-jordan turns \( \C_2(i) \) back into \( \J_2(i) \oplus \J_2(-i) \) over \( \nC \).)

(d) \( \tr \C = 0 = \tr \C_2(i) \), and both matrices have characteristic polynomial \( (x^2+1)^2 \): for \( \C \) by (a), and for \( \C_2(i) \) by @cor-real-block-complex-jordan. Their minimal polynomials agree too, both being \( (x^2+1)^2 \).
:::

:::: {#exr-real-jordan-and-weyr-forms-c2}
[C2: Commuting with a Weyr matrix, and with a Jordan matrix]

Let \( F \) be a field.

::: {.enumerate options="label=(\alph*)"}
1. Let \( \W \in M_3(F) \) be the basic Weyr matrix with \( \lambda = 0 \) and structure \( (2,1) \) (@def-weyr-form). Find all \( \K \in M_3(F) \) with \( \W \K = \K \W \), and check that they are block upper triangular for the partition \( 3 = 2 + 1 \).
2. Let \( \J = \J_2(0) \oplus \J_1(0) \). Find all \( \K \in M_3(F) \) with \( \J \K = \K \J \), and exhibit one that is **not** upper triangular. Which partition of \( 3 \) does it violate?
3. Compute the dimension of each of the two commutants, and explain why they are equal.
:::
::::

::: {.solution}
(a) \( \W = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \). Write \( \K = (k_{ij}) \). Then \( \W \K \) has first row equal to the third row of \( \K \) and other rows zero, while \( \K \W \) has third column equal to the first column of \( \K \) and other columns zero. Equating,
\[
(k_{31}, k_{32}, k_{33}) = (0, 0, k_{11}), \qquad k_{21} = k_{31} = 0 .
\]
So the commutant is
\[
\left\{ \begin{pmatrix} a & b & c \\ 0 & e & f \\ 0 & 0 & a \end{pmatrix} : a, b, c, e, f \in F \right\},
\]
of dimension \( 5 \). The lower-left \( 1 \times 2 \) block is \( (k_{31}, k_{32}) = (0,0) \), so every such \( \K \) is block upper triangular for \( 3 = 2 + 1 \), as @prp-weyr-commutant asserts.

(b) \( \J = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \). Now \( \J \K \) has first row equal to the second row of \( \K \) and other rows zero, while \( \K \J \) has second column equal to the first column of \( \K \) and other columns zero. Equating gives \( k_{21} = 0 \), \( k_{22} = k_{11} \), \( k_{23} = 0 \) and \( k_{31} = 0 \), so the commutant is
\[
\left\{ \begin{pmatrix} a & b & c \\ 0 & a & 0 \\ 0 & h & i \end{pmatrix} \right\},
\]
also of dimension \( 5 \). Take \( \K_0 = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} \), which commutes with \( \J \) (it is the case \( a = b = c = i = 0 \), \( h = 1 \)). Its only non-zero entry sits in position \( (3,2) \), below the diagonal, so \( \K_0 \) is not upper triangular. The partition it violates is \( 3 = 2 + 1 \), the Weyr partition of this operator: the lower-left \( 1 \times 2 \) block of \( \K_0 \) is \( (0, 1) \ne \0 \). So the conclusion of @prp-weyr-commutant genuinely fails for the Jordan form, while (a) confirms it for the Weyr form (@thm-weyr-form) of the same operator.

(c) Both have dimension \( 5 \). They must agree, because \( \J \) and \( \W \) are similar (both are nilpotent with \( \rank = 1 \) and \( \rank^2 = 0 \), so @cor-nilpotent-similar-iff-ranks applies): if \( \W = \P^{-1}\J \P \), then \( \K \mapsto \P^{-1}\K \P \) is a bijection from the commutant of \( \J \) to that of \( \W \), and it is linear and invertible, hence preserves dimension.
:::
