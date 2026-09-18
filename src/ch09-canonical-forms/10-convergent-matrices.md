# Convergent and Power-Bounded Matrices

Chapter 8 asked what happens to \( \A^{m} \) as \( m \) grows, and could answer only for diagonalizable matrices: the powers of \( \A \) behave like the powers of its eigenvalues. For a Markov chain that left a gap, because a transition matrix need not be diagonalizable. The Jordan form closes the gap completely. This section characterizes, in terms of the eigenvalues and the block sizes alone, when \( \A^{m} \) tends to zero, when it stays bounded, when it converges, and when the geometric series \( \I + \A + \A^{2} + \cdots \) converges.

Convergence here means what it meant in Chapter 8: **entrywise**. No notion of the size of a matrix is used. Chapter 15 introduces norms and re-proves several of these results in a way that also gives numerical bounds; the price of doing without them is that we must look at one entry at a time, and the Jordan form is what makes that possible.

## Entrywise limits and bounds

::: {#def-entrywise-convergence}
[Entrywise Convergence and Boundedness]

Let \( \M_1, \M_2, \dots \) be matrices in \( M_{p \times q}(\nC) \) and \( \M \in M_{p \times q}(\nC) \).

::: {.enumerate options="label=(\alph*)"}
1. The sequence \( (\M_m) \) **converges** to \( \M \), written \( \M_m \to \M \), if for **every** position \( (r, s) \) the sequence of complex numbers \( (\M_m)_{rs} \) converges to \( \M_{rs} \). We then write \( \M = \lim_m \M_m \).
2. The sequence \( (\M_m) \) is **bounded** if there is a real \( c \ge 0 \) with \( \lvert (\M_m)_{rs}\rvert \le c \) for **all** \( m \) and **all** positions \( (r, s) \).
3. A series \( \sum_{k \ge 0} \M_k \) **converges** to \( \M \) if its sequence of partial sums \( \sum_{k=0}^{K}\M_k \) converges to \( \M \).
:::
:::

In words: nothing new is happening. Each of the \( pq \) positions is watched separately, and the words mean for matrices exactly what they mean for the finitely many number sequences at those positions. Since a finite set of bounds can be replaced by their maximum, (b) is the same as asking each entry sequence to be bounded.

::: {.remark}
**What we assume from analysis.** Beyond the four facts quoted in Chapter 8 §11, this section uses exactly the following.

::: {.enumerate options="label=(B\arabic*)"}
1. **Polynomial against geometric decay.** For every integer \( j \ge 0 \) and every real \( r \) with \( 0 \le r < 1 \), \( m^{j}r^{m} \to 0 \) as \( m \to \infty \).
2. **Growth.** For real \( r > 1 \), the sequence \( (r^{m}) \) is unbounded.
3. **Limits.** Limits of convergent sequences of complex numbers respect sums, scalar multiples and products; a convergent sequence is bounded; every subsequence of a convergent sequence converges to the same limit; and \( z_m \to z \) implies \( \lvert z_m\rvert \to \lvert z\rvert \).
4. **Terms of a convergent series.** If \( \sum_k z_k \) converges, then \( z_k \to 0 \).
:::
:::

Two reductions make every proof below short. The first moves the question along a similarity, so that we may assume \( \A \) is a Jordan matrix. The second computes the powers of a single Jordan block.

::: {#lem-powers-transfer-along-similarity}
[Convergence and Boundedness Survive a Similarity]

Let \( \A, \B \in M_n(\nC) \) with \( \B = \P^{-1}\A \P \) for an invertible \( \P \in M_n(\nC) \), and let \( \L \in M_n(\nC) \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \A^{m} \to \L \) if and only if \( \B^{m} \to \P^{-1}\L \P \);
2. \( (\A^{m}) \) is bounded if and only if \( (\B^{m}) \) is bounded.
:::
:::

::: {.proof}
By @prp-similarity-invariants (c), \( \B^{m} = \P^{-1}\A^{m}\P \) for every \( m \ge 0 \). Writing out the products (@def-matrix-multiplication), the \( (r,s) \)-entry of \( \B^{m} \) is
\[
(\B^{m})_{rs} = \sum_{u,v}(\P^{-1})_{ru}\,(\A^{m})_{uv}\,\P_{vs},
\]
a linear combination of the entries of \( \A^{m} \) with coefficients that do not depend on \( m \). So if \( \A^{m} \to \L \), then by (B3) each entry of \( \B^{m} \) converges to the matching combination of the entries of \( \L \), that is, \( \B^{m} \to \P^{-1}\L \P \); and if \( \lvert (\A^{m})_{uv}\rvert \le c \) for all \( m, u, v \), then \( \lvert (\B^{m})_{rs}\rvert \le c\sum_{u,v}\lvert(\P^{-1})_{ru}\rvert\,\lvert \P_{vs}\rvert \), a bound independent of \( m \), so \( (\B^{m}) \) is bounded. The converses follow by exchanging the roles of \( \A \) and \( \B \), using \( \A = \P \B \P^{-1} \).
:::

For the second reduction, recall from @lem-polynomial-of-jordan-block, applied to the polynomial \( x^{m} \), that
\[
\bigl(\J_k(\lambda)^{m}\bigr)_{r,\,r+j} = \binom{m}{j}\lambda^{\,m-j} \qquad (0 \le j \le k-1),
\]
with zeros below the diagonal. Everything in this section is read off this one formula. Two remarks about it: the binomial coefficient is bounded by \( m^{j} \), since
\[
\binom{m}{j} = \frac{m(m-1)\cdots(m-j+1)}{j!} \le \frac{m^{j}}{j!} \le m^{j} \qquad (m \ge j \ge 1),
\]
and \( \binom{m}{1} = m \) grows without bound, while \( \binom{m}{0} = 1 \) is constant. So the only question is whether the geometric factor \( \lambda^{m} \) beats the polynomial factor \( m^{j} \).

::: {.check}
Compute \( \lvert (\J_3(\lambda)^{m})_{1,3}\rvert \) for \( \lambda = \tfrac12 \) and for \( \lambda = 1 \), and say in each case whether it tends to \( 0 \), stays bounded, or grows without bound.
:::

::: {.solution}
Here \( j = 2 \), so the entry is \( \binom{m}{2}\lambda^{m-2} \), of modulus \( \frac{m(m-1)}{2}\lvert\lambda\rvert^{\,m-2} \). For \( \lambda = \tfrac12 \) this is \( 2\cdot\frac{m(m-1)}{2}2^{-m} \le 2m^{2}2^{-m} \), which tends to \( 0 \) by (B1) with \( j = 2 \) and \( r = \tfrac12 \). For \( \lambda = 1 \) it is \( \frac{m(m-1)}{2} \), which grows without bound. The modulus of \( \lambda \) decides, and when \( \lvert\lambda\rvert = 1 \) the block size decides.
:::

## Powers tending to zero

*The powers of \( \A \) die out exactly when every eigenvalue has modulus less than one.*

::: {#thm-matrix-powers-converge-to-zero}
[Powers Tending to Zero]

Let \( \A \in M_n(\nC) \), \( n \ge 1 \). Then \( \A^{m} \to 0 \) if and only if every eigenvalue \( \lambda \) of \( \A \) satisfies \( \lvert\lambda\rvert < 1 \).
:::

::: {.idea}
\( (\Leftarrow) \) Pass to the Jordan form and look at one entry: it is \( \binom{m}{j}\lambda^{m-j} \), a polynomial in \( m \) times a geometric sequence that decays, and geometric decay wins. \( (\Rightarrow) \) The other direction needs no Jordan form at all: an eigenvector turns \( \A^{m} \) into \( \lambda^{m} \).
:::

::: {.proof}
\( (\Leftarrow) \) Suppose \( \lvert\lambda\rvert < 1 \) for every \( \lambda \in \spec(\A) \). By @thm-jordan-canonical-form, \( \A = \P \J \P^{-1} \) with \( \J = \J_{k_1}(\lambda_1) \oplus \dots \oplus \J_{k_d}(\lambda_d) \) a Jordan matrix, whose diagonal entries \( \lambda_i \) are the eigenvalues of \( \A \) (@cor-jordan-invariants (a)). By @thm-block-diagonal-arithmetic (b), \( \J^{m} \) is the direct sum of the blocks \( \J_{k_i}(\lambda_i)^{m} \), so each entry of \( \J^{m} \) is either \( 0 \) for every \( m \) or of the form \( \binom{m}{j}\lambda_i^{\,m-j} \) with \( 0 \le j \le k_i - 1 \). For the latter, with \( r = \lvert\lambda_i\rvert < 1 \), if \( r = 0 \) the entry is \( 0 \) for \( m > j \); otherwise, for \( m \ge j \),
\[
\Bigl\lvert\binom{m}{j}\lambda_i^{\,m-j}\Bigr\rvert \le m^{j}r^{\,m-j} = r^{-j}\,m^{j}r^{m} \longrightarrow 0
\]
by (B1), the factor \( r^{-j} \) being a constant. So \( \J^{m} \to 0 \), and \( \A^{m} \to \P\,0\,\P^{-1} = 0 \) by @lem-powers-transfer-along-similarity (a).

\( (\Rightarrow) \) Suppose \( \A^{m} \to 0 \) and let \( \lambda \in \spec(\A) \) with eigenvector \( \v \ne \0 \). Then \( \A^{m}\v = \lambda^{m}\v \) for every \( m \) (induction on \( m \)). Pick a coordinate \( r \) with \( v_r \ne 0 \). The \( r \)-th entry of \( \A^{m}\v \) is a linear combination of entries of \( \A^{m} \) with coefficients \( v_1, \dots, v_n \), so it tends to \( 0 \) by (B3); that entry is \( \lambda^{m}v_r \), so \( \lambda^{m} \to 0 \) and hence \( \lvert\lambda\rvert^{m} = \lvert\lambda^{m}\rvert \to 0 \) by (B3). If \( \lvert\lambda\rvert \ge 1 \), then \( \lvert\lambda\rvert^{m} \ge 1 \) for every \( m \) and the limit cannot be \( 0 \). Hence \( \lvert\lambda\rvert < 1 \). This proves the theorem.
:::

Note the asymmetry: the hard direction needs the Jordan form, the easy one needs only an eigenvector. That pattern repeats in the next two theorems.

::: {.warning}
**The condition is on the eigenvalues, not on the entries.** Every entry of \( \A = \begin{pmatrix} 0.9 & 0.9 \\ 0.9 & 0.9\end{pmatrix} \) has modulus less than \( 1 \), yet \( \A\1 = 1.8\,\1 \), so \( 1.8 \) is an eigenvalue and \( \A^{m}\1 = 1.8^{m}\1 \) grows without bound. Conversely, a matrix with huge entries can have all eigenvalues \( 0 \): the matrix \( \begin{pmatrix} 0 & 10^{6} \\ 0 & 0\end{pmatrix} \) squares to \( 0 \). Nothing can be concluded from the size of the entries alone.
:::

## Powers that stay bounded

Dropping "tends to zero" to "stays bounded" allows eigenvalues on the unit circle, but only if they carry no chains: a block of size \( \ge 2 \) contributes an entry \( \binom{m}{1}\lambda^{m-1} \) of modulus \( m \).

::: {#thm-matrix-powers-bounded}
[Power-Bounded Matrices]

Let \( \A \in M_n(\nC) \), \( n \ge 1 \), with Jordan form \( \J \). The sequence \( (\A^{m})_{m \ge 0} \) is bounded if and only if

::: {.enumerate options="label=(\roman*)"}
1. every eigenvalue \( \lambda \) of \( \A \) satisfies \( \lvert\lambda\rvert \le 1 \), and
2. every eigenvalue \( \lambda \) with \( \lvert\lambda\rvert = 1 \) has **all** of its blocks in \( \J \) of size \( 1 \), equivalently \( a_{\A}(\lambda) = g_{\A}(\lambda) \), equivalently \( x - \lambda \) occurs to the first power in \( m_{\A} \).
:::
:::

::: {.proof}
Write \( \A = \P \J \P^{-1} \) with \( \J = \J_{k_1}(\lambda_1) \oplus \dots \oplus \J_{k_d}(\lambda_d) \) (@thm-jordan-canonical-form). By @lem-powers-transfer-along-similarity (b), \( (\A^{m}) \) is bounded if and only if \( (\J^{m}) \) is, and by @thm-block-diagonal-arithmetic (b) the latter holds if and only if every block sequence \( \bigl(\J_{k_i}(\lambda_i)^{m}\bigr) \) is bounded. The three reformulations in (ii) are @cor-jordan-invariants (a), (b) and (c): all \( \lambda \)-blocks have size \( 1 \) exactly when their number equals their total size, and exactly when the largest of their sizes is \( 1 \).

\( (\Leftarrow) \) Assume (i) and (ii), and fix a block \( \J_k(\lambda) \) of \( \J \). If \( \lvert\lambda\rvert < 1 \), then \( \J_k(\lambda)^{m} \to 0 \) by @thm-matrix-powers-converge-to-zero applied to the single block \( \J_k(\lambda) \), whose only eigenvalue is \( \lambda \), hence \( \bigl(\J_k(\lambda)^{m}\bigr) \) is bounded by (B3). If \( \lvert\lambda\rvert = 1 \), then \( k = 1 \) by (ii), so \( \J_k(\lambda)^{m} = (\lambda^{m}) \) is a \( 1 \times 1 \) matrix of modulus \( \lvert\lambda\rvert^{m} = 1 \). Either way the block sequence is bounded, so \( (\J^{m}) \) is bounded and so is \( (\A^{m}) \).

\( (\Rightarrow) \) Assume \( (\A^{m}) \) is bounded, hence so is \( (\J^{m}) \), hence so is every block sequence.

*Proof of (i).* Let \( \lambda \) be an eigenvalue and \( \J_k(\lambda) \) one of its blocks. The \( (1,1) \)-entry of \( \J_k(\lambda)^{m} \) is \( \lambda^{m} \), so \( \bigl(\lvert\lambda\rvert^{m}\bigr) \) is bounded; by (B2) this forces \( \lvert\lambda\rvert \le 1 \).

*Proof of (ii).* Suppose some eigenvalue \( \lambda \) with \( \lvert\lambda\rvert = 1 \) had a block \( \J_k(\lambda) \) with \( k \ge 2 \). Its \( (1,2) \)-entry at the \( m \)-th power is \( \binom{m}{1}\lambda^{\,m-1} = m\lambda^{\,m-1} \), of modulus \( m\lvert\lambda\rvert^{\,m-1} = m \), which is unbounded — contradicting the boundedness of that block sequence. So every such block has size \( 1 \). This proves the theorem.
:::

## Powers that converge

Boundedness is not convergence: \( \begin{pmatrix} 0 & 1 \\ 1 & 0\end{pmatrix}^{m} \) alternates between two matrices forever. Among the eigenvalues of modulus \( 1 \), only \( \lambda = 1 \) has convergent powers, because \( \lambda^{m} \) has to sit still.

::: {#thm-matrix-powers-converge}
[Convergent Matrices]

Let \( \A \in M_n(\nC) \), \( n \ge 1 \), with Jordan form \( \J \). Then \( (\A^{m}) \) converges if and only if every eigenvalue \( \lambda \) of \( \A \) satisfies

::: {.enumerate options="label=(\roman*)"}
1. \( \lvert\lambda\rvert < 1 \), or
2. \( \lambda = 1 \) and all of its blocks in \( \J \) have size \( 1 \).
:::

In that case
\[
\lim_{m \to \infty}\A^{m} = \vPi ,
\]
where \( \vPi \in M_n(\nC) \) is the matrix, in the standard basis, of the projection onto \( E_1(\A) \) along \( \bigoplus_{\lambda \ne 1}G_\lambda(\A) \) if \( 1 \in \spec(\A) \), and \( \vPi = 0 \) otherwise.
:::

::: {.idea}
For the shape of the answer, take the Jordan form and let \( m \to \infty \) in each block: the blocks with \( \lvert\lambda\rvert < 1 \) go to \( 0 \), the blocks \( \J_1(1) = (1) \) stay at \( 1 \). So \( \J^{m} \) tends to the \( 0/1 \) diagonal matrix that marks the \( 1 \)-blocks, which is the matrix of a projection; conjugating back identifies the two subspaces. For the converse, the \( (1,1) \)-entry of a block is \( \lambda^{m} \), and if that converges to \( z \) then so does \( \lambda^{m+1} = \lambda\cdot\lambda^{m} \), giving \( z = \lambda z \) and forcing \( \lambda = 1 \) or \( z = 0 \).
:::

::: {.proof}
Write \( \A = \P \J \P^{-1} \) with \( \J = \J_{k_1}(\lambda_1) \oplus \dots \oplus \J_{k_d}(\lambda_d) \) (@thm-jordan-canonical-form), and let \( \sB = (\b_1, \dots, \b_n) \) be the corresponding Jordan basis, the columns of \( \P \). For each \( i \) let \( C_i \subseteq \nC^{n} \) be the span of the \( k_i \) basis vectors belonging to block \( i \), so that \( \nC^{n} = C_1 \oplus \dots \oplus C_d \).

\( (\Leftarrow) \) Suppose every eigenvalue satisfies (i) or (ii). Fix a block. If \( \lvert\lambda_i\rvert < 1 \), then \( \J_{k_i}(\lambda_i)^{m} \to 0 \) by @thm-matrix-powers-converge-to-zero applied to the block \( \J_{k_i}(\lambda_i) \), whose only eigenvalue is \( \lambda_i \). If \( \lambda_i = 1 \), then \( k_i = 1 \) by (ii) and \( \J_1(1)^{m} = (1) \) for every \( m \). By @thm-block-diagonal-arithmetic (b), \( \J^{m} \) is the direct sum of these, so
\[
\J^{m} \longrightarrow \E \coloneqq \text{the diagonal matrix with } 1 \text{ in the positions of the } \lambda_i = 1 \text{ blocks and } 0 \text{ elsewhere.}
\]
By @lem-powers-transfer-along-similarity (a), \( \A^{m} \to \P \E \P^{-1} \).

It remains to identify \( \P \E \P^{-1} \). The matrix \( \E \) is the matrix in the basis \( \sB \) of the projection onto
\[
U \coloneqq \bigoplus_{\lambda_i = 1}C_i \qquad \text{along} \qquad W \coloneqq \bigoplus_{\lambda_i \ne 1}C_i ,
\]
because \( \E \) fixes each basis vector of the first family and kills each of the second (@thm-projection-direct-sum). Since the columns of \( \P \) are the vectors of \( \sB \), \( \P \) is the change-of-coordinates matrix from \( \sB \) to the standard basis, so \( \P \E \P^{-1} \) is the matrix of that projection in the standard basis (@thm-change-of-basis-maps). Now, for any \( \mu \in \spec(\A) \),
\[
\bigoplus_{\lambda_i = \mu}C_i = G_\mu(\A) .
\]
Indeed each \( C_i \) with \( \lambda_i = \mu \) is killed by \( (\A - \mu \I)^{k_i} \), hence lies in \( G_\mu(\A) \) (@cor-generalized-eigenspace-is-kernel (a)); the sum on the left is direct and has dimension \( \sum_{\lambda_i = \mu}k_i = a_{\A}(\mu) \) by @cor-jordan-invariants (a); and \( \dim G_\mu(\A) = a_{\A}(\mu) \) by @thm-generalized-eigenspace-decomposition (c). An inclusion of subspaces with equal dimensions is an equality (@thm-dim-impl-eq, applied inside \( G_\mu(\A) \)). Hence \( W = \bigoplus_{\lambda \ne 1}G_\lambda(\A) \), and \( U = G_1(\A) \) if \( 1 \in \spec(\A) \), with \( U = \{\0\} \) otherwise. Finally, when \( 1 \in \spec(\A) \), condition (ii) says all \( 1 \)-blocks have size \( 1 \), so \( g_{\A}(1) = a_{\A}(1) \) by @cor-jordan-invariants (a), (b); since \( E_1(\A) \subseteq G_1(\A) \) with \( \dim E_1(\A) = g_{\A}(1) = a_{\A}(1) = \dim G_1(\A) \), we get \( G_1(\A) = E_1(\A) \). So \( \lim_m \A^{m} = \vPi \) as stated.

\( (\Rightarrow) \) Suppose \( (\A^{m}) \) converges. By @lem-powers-transfer-along-similarity (a) so does \( (\J^{m}) \), hence so does each block sequence. Fix a block \( \J_k(\lambda) \).

*Case \( \lvert\lambda\rvert > 1 \).* Impossible: a convergent sequence is bounded (B3), so this is excluded by @thm-matrix-powers-bounded.

*Case \( \lvert\lambda\rvert = 1 \) and \( \lambda \ne 1 \).* The \( (1,1) \)-entries give a convergent sequence \( \lambda^{m} \to z \). The sequence \( (\lambda^{m+1})_{m \ge 0} \) is a tail of the same sequence, so it also converges to \( z \); on the other hand \( \lambda^{m+1} = \lambda\cdot\lambda^{m} \to \lambda z \) by (B3). Hence \( z = \lambda z \), that is, \( (1 - \lambda)z = 0 \), and \( \lambda \ne 1 \) forces \( z = 0 \). But \( \lvert\lambda^{m}\rvert = 1 \) for every \( m \), so \( \lvert z\rvert = 1 \) by (B3), a contradiction. So this case does not occur either.

*Case \( \lambda = 1 \).* If \( k \ge 2 \), the \( (1,2) \)-entry of \( \J_k(1)^{m} \) is \( \binom{m}{1}1^{\,m-1} = m \), which does not converge. So \( k = 1 \).

The three cases leave exactly (i) and (ii). This proves the theorem.
:::

The limit deserves a sentence. It is a projection, so \( \vPi^{2} = \vPi \) — which had to be true, since \( \vPi^{2} = \lim_m \A^{m}\lim_m \A^{m} = \lim_m \A^{2m} = \vPi \) by (B3) — and it acts as the identity on the eigenvectors for \( 1 \) and annihilates everything belonging to the other eigenvalues. In the long run, \( \A \) forgets all of \( \nC^{n} \) except the fixed space \( E_1(\A) \).

::: {#exm-powers-of-two-matrices}
[Deciding and Computing Limits of Powers]

For each matrix, decide whether \( \A^{m} \) tends to \( 0 \), stays bounded, converges, and compute \( \lim \A^{m} \) when it exists.

::: {.enumerate options="label=(\alph*)"}
1. \( \A_1 = \begin{pmatrix} 2 & 1 \\ -1 & 0 \end{pmatrix} \).
2. \( \A_2 = \begin{pmatrix} 0 & -\tfrac12 \\ \tfrac12 & 0 \end{pmatrix} \).
3. \( \A_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \tfrac13 & 1 \\ 0 & 0 & \tfrac13\end{pmatrix} \).
:::
:::

::: {.solution}
(a) \( p_{\A_1} = x(x - 2) + 1 = (x-1)^{2} \), so the only eigenvalue is \( 1 \). Put \( \N = \A_1 - \I = \begin{pmatrix} 1 & 1 \\ -1 & -1\end{pmatrix} \); then \( \N \ne 0 \) and \( \N^{2} = \begin{pmatrix} 1-1 & 1-1 \\ -1+1 & -1+1\end{pmatrix} = 0 \), so \( g_{\A_1}(1) = 2 - \rank \N = 1 \) and the Jordan form is \( \J_2(1) \). Condition (ii) of @thm-matrix-powers-bounded fails, so \( (\A_1^{m}) \) is **unbounded**, and in particular does not converge. Explicitly, \( \I \) and \( \N \) commute and \( \N^2 = 0 \), so the binomial theorem gives
\[
\A_1^{m} = (\I + \N)^{m} = \I + m\N = \begin{pmatrix} 1 + m & m \\ -m & 1 - m\end{pmatrix},
\]
which grows linearly.

(b) \( p_{\A_2} = x^{2} + \tfrac14 \), with roots \( \pm\tfrac{i}{2} \), both of modulus \( \tfrac12 < 1 \). By @thm-matrix-powers-converge-to-zero, \( \A_2^{m} \to 0 \) (so also bounded and convergent). Explicitly \( \A_2^{2} = -\tfrac14 \I \), so \( \A_2^{2l} = (-\tfrac14)^{l}\I \) and \( \A_2^{2l+1} = (-\tfrac14)^{l}\A_2 \), and every entry has modulus at most \( 4^{-l} \to 0 \).

(c) \( \A_3 = (1) \oplus \J_2(\tfrac13) \) is already a Jordan matrix. Its eigenvalues are \( 1 \), with a single block of size \( 1 \), and \( \tfrac13 \), with \( \lvert\tfrac13\rvert < 1 \). So condition (i) or (ii) holds for each eigenvalue and \( \A_3^{m} \) converges by @thm-matrix-powers-converge. With \( \P = \I \), the matrix \( \E \) of the proof is \( \diag(1, 0, 0) \), so
\[
\lim_m \A_3^{m} = \diag(1, 0, 0),
\]
the projection onto \( E_1(\A_3) = \Span(\e_1) \) along \( G_{1/3}(\A_3) = \Span(\e_2, \e_3) \). Explicitly, by @lem-polynomial-of-jordan-block,
\[
\A_3^{m} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 3^{-m} & m\,3^{-(m-1)} \\ 0 & 0 & 3^{-m}\end{pmatrix},
\]
and \( m\,3^{-(m-1)} = 3m\,3^{-m} \to 0 \) by (B1).
:::

## Markov chains, finished

Chapter 8 proved that a Markov chain settles down under three hypotheses: \( \A \) diagonalizable over \( \nC \), \( a_{\A}(1) = 1 \), and \( \lvert\lambda\rvert < 1 \) for every other eigenvalue (@thm-markov-limit-diagonalizable). The first hypothesis can now be dropped, and more: for a stochastic matrix, the block condition of @thm-matrix-powers-bounded holds automatically, because the powers of a stochastic matrix have entries in \( [0, 1] \).

::: {#cor-markov-powers-converge}
[Convergence of a Markov Chain]

Let \( \A \in M_n(\nR) \) be stochastic (@def-stochastic-matrix), \( n \ge 1 \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( (\A^{m}) \) is bounded; consequently every eigenvalue \( \lambda \in \nC \) of \( \A \) satisfies \( \lvert\lambda\rvert \le 1 \), and every eigenvalue with \( \lvert\lambda\rvert = 1 \) has only \( 1 \times 1 \) blocks. In particular \( a_{\A}(1) = g_{\A}(1) \).
2. \( (\A^{m}) \) converges if and only if \( 1 \) is the **only** eigenvalue of \( \A \) of modulus \( 1 \); and then \( \lim_m \A^{m} \) is the projection onto \( E_1(\A) \) along \( \bigoplus_{\lambda \ne 1}G_\lambda(\A) \).
:::
:::

::: {.proof}
(a) By @prp-stochastic-properties (b), every \( \A^{m} \) is stochastic, so its entries are non-negative and each of its columns sums to \( 1 \); hence every entry lies in \( [0, 1] \) and \( (\A^{m}) \) is bounded with \( c = 1 \). Now apply the \( (\Rightarrow) \) direction of @thm-matrix-powers-bounded. Since \( 1 \in \spec(\A) \) by @prp-stochastic-properties (c), the \( 1 \)-blocks exist and all have size \( 1 \), so \( a_{\A}(1) = g_{\A}(1) \) by @cor-jordan-invariants (a), (b).

(b) By (a), every eigenvalue has \( \lvert\lambda\rvert \le 1 \) and every eigenvalue of modulus \( 1 \) has only \( 1 \times 1 \) blocks. So the criterion of @thm-matrix-powers-converge — each eigenvalue has \( \lvert\lambda\rvert < 1 \), or equals \( 1 \) with only \( 1 \times 1 \) blocks — holds precisely when no eigenvalue \( \lambda \ne 1 \) has \( \lvert\lambda\rvert = 1 \). The limit is the one given by @thm-matrix-powers-converge.
:::

So the only obstruction to a Markov chain settling down is an eigenvalue of modulus \( 1 \) other than \( 1 \) itself — periodicity, in the language of probability. Chapter 8's warning example, the swap \( \begin{pmatrix} 0&1\\1&0\end{pmatrix} \), has the eigenvalue \( -1 \) and is exactly this obstruction.

::: {#exm-markov-limit-2x2}
[A Two-State Chain]

Let \( \A = \begin{pmatrix} 3/4 & 1/2 \\ 1/4 & 1/2 \end{pmatrix} \). Decide whether \( \A^{m} \) converges and find the limit.
:::

::: {.solution}
\( \A \) is stochastic: the entries are non-negative, and each column sums to \( 1 \). Its characteristic polynomial is
\[
p_{\A} = \bigl(x - \tfrac34\bigr)\bigl(x - \tfrac12\bigr) - \tfrac18 = x^{2} - \tfrac54x + \tfrac14 = (x - 1)\bigl(x - \tfrac14\bigr),
\]
so \( \spec(\A) = \{1, \tfrac14\} \) and the only eigenvalue of modulus \( 1 \) is \( 1 \). By @cor-markov-powers-converge (b), \( \A^{m} \) converges.

For the limit, \( E_1(\A) = \ker(\A - \I) \), and \( \A - \I = \begin{pmatrix} -1/4 & 1/2 \\ 1/4 & -1/2\end{pmatrix} \) gives \( \Span((2,1)) \); the steady state is \( \v = (\tfrac23, \tfrac13) \), the multiple of \( (2,1) \) whose entries sum to \( 1 \). Also \( E_{1/4}(\A) = \ker(\A - \tfrac14 \I) \), and \( \A - \tfrac14\I = \begin{pmatrix} 1/2 & 1/2 \\ 1/4 & 1/4\end{pmatrix} \) gives \( \Span((1,-1)) \). Since the two eigenvalues are distinct, \( G_{1/4}(\A) = E_{1/4}(\A) \) and the limit \( \vPi \) is the projection onto \( \Span((2,1)) \) along \( \Span((1,-1)) \). Computing it in the basis \( \sC = \bigl((2,1), (1,-1)\bigr) \): with \( \Q = \begin{pmatrix} 2 & 1 \\ 1 & -1\end{pmatrix} \), \( \det \Q = -3 \) and \( \Q^{-1} = \tfrac{1}{3}\begin{pmatrix} 1 & 1 \\ 1 & -2\end{pmatrix} \), so
\[
\vPi = \Q\diag(1, 0)\Q^{-1} = \begin{pmatrix} 2 & 0 \\ 1 & 0 \end{pmatrix}\cdot\tfrac13\begin{pmatrix} 1 & 1 \\ 1 & -2\end{pmatrix} = \tfrac13\begin{pmatrix} 2 & 2 \\ 1 & 1\end{pmatrix} = \begin{pmatrix} 2/3 & 2/3 \\ 1/3 & 1/3\end{pmatrix}.
\]
*Check.* \( \vPi = \v\1\tp \), as @thm-markov-limit-diagonalizable predicts; \( \vPi^{2} = \vPi \) since \( \1\tp\v = 1 \); the columns of \( \vPi \) are the steady state, so every initial probability vector \( \x_0 \) gives \( \x_m = \A^{m}\x_0 \to \vPi\x_0 = \v(\1\tp\x_0) = \v \). And \( \A^{2} = \begin{pmatrix} 11/16 & 5/8 \\ 5/16 & 3/8\end{pmatrix} \) is already close to \( \vPi \), the error decaying like \( 4^{-m} \).
:::

## The geometric series of a matrix

The scalar identity \( \sum_k a^{k} = (1-a)^{-1} \) for \( \lvert a\rvert < 1 \) has a matrix version, with the same proof and the same hypothesis read off the eigenvalues.

::: {#thm-neumann-series-spectral}
[Neumann Series]

Let \( \A \in M_n(\nC) \), \( n \ge 1 \). Then the series \( \sum_{k \ge 0}\A^{k} \) converges if and only if every eigenvalue \( \lambda \) of \( \A \) satisfies \( \lvert\lambda\rvert < 1 \). In that case \( \I - \A \) is invertible and
\[
\sum_{k=0}^{\infty}\A^{k} = (\I - \A)^{-1} .
\]
:::

::: {.idea}
Telescoping gives \( (\I - \A)(\I + \A + \dots + \A^{K}) = \I - \A^{K+1} \), an exact identity for every \( K \). If \( \I - \A \) is invertible, solve it for the partial sum and let \( K \to \infty \), where @thm-matrix-powers-converge-to-zero kills \( \A^{K+1} \). Conversely, the terms of a convergent series tend to \( 0 \), which is the hypothesis of that theorem again.
:::

::: {.proof}
\( (\Leftarrow) \) Suppose \( \lvert\lambda\rvert < 1 \) for every \( \lambda \in \spec(\A) \). In particular \( 1 \notin \spec(\A) \), so \( 0 \notin \spec(\I - \A) \) — a vector with \( (\I-\A)\v = \0 \) is a vector with \( \A\v = \v \) — and \( \I - \A \) is invertible (@thm-invertible-tfae-eigen). Put \( \S_K = \sum_{k=0}^{K}\A^{k} \). Multiplying out and canceling,
\[
(\I - \A)\S_K = \sum_{k=0}^{K}\A^{k} - \sum_{k=1}^{K+1}\A^{k} = \I - \A^{K+1},
\]
hence \( \S_K = (\I-\A)^{-1}\bigl(\I - \A^{K+1}\bigr) \). By @thm-matrix-powers-converge-to-zero, \( \A^{K+1} \to 0 \). Each entry of \( \S_K \) is a fixed linear combination of the entries of \( \I - \A^{K+1} \), with coefficients from \( (\I-\A)^{-1} \), so by (B3) it converges to the corresponding combination for \( \I \), that is, \( \S_K \to (\I-\A)^{-1}\I = (\I-\A)^{-1} \).

\( (\Rightarrow) \) Suppose \( \sum_k \A^{k} \) converges. Fix a position \( (r,s) \); the series of complex numbers \( \sum_k (\A^{k})_{rs} \) converges, so \( (\A^{k})_{rs} \to 0 \) by (B4). This holds at every position, so \( \A^{k} \to 0 \), and @thm-matrix-powers-converge-to-zero gives \( \lvert\lambda\rvert < 1 \) for every eigenvalue. This proves the theorem.
:::

::: {#exm-neumann-2x2}
[Inverting by Summing a Series]

Let \( \A = \begin{pmatrix} 0 & 1/2 \\ 1/2 & 0\end{pmatrix} \). Verify that \( \sum_k \A^{k} \) converges, sum it, and compare with \( (\I - \A)^{-1} \).
:::

::: {.solution}
\( p_{\A} = x^{2} - \tfrac14 \), so \( \spec(\A) = \{\tfrac12, -\tfrac12\} \) and both eigenvalues have modulus \( \tfrac12 < 1 \). By @thm-neumann-series-spectral the series converges.

*Summing it.* \( \A^{2} = \tfrac14 \I \), so \( \A^{2l} = 4^{-l}\I \) and \( \A^{2l+1} = 4^{-l}\A \). Grouping the partial sums by parity, which is legitimate because each entry sequence splits into two convergent pieces (B3),
\[
\sum_{k \ge 0}\A^{k} = \Bigl(\sum_{l \ge 0}4^{-l}\Bigr)(\I + \A) = \frac{1}{1 - \tfrac14}(\I + \A) = \tfrac43\begin{pmatrix} 1 & 1/2 \\ 1/2 & 1\end{pmatrix} = \begin{pmatrix} 4/3 & 2/3 \\ 2/3 & 4/3\end{pmatrix},
\]
the scalar sum being the case \( n = 1 \) of @thm-neumann-series-spectral applied to the \( 1 \times 1 \) matrix \( (\tfrac14) \).

*The inverse.* \( \I - \A = \begin{pmatrix} 1 & -1/2 \\ -1/2 & 1\end{pmatrix} \) has determinant \( 1 - \tfrac14 = \tfrac34 \), so by @thm-two-by-two-inverse
\[
(\I - \A)^{-1} = \tfrac43\begin{pmatrix} 1 & 1/2 \\ 1/2 & 1\end{pmatrix},
\]
in agreement.
:::

::: {.remark}
The first thing every criterion in this section looks at is the largest modulus of an eigenvalue,
\[
\rho(\A) = \max\{\lvert\lambda\rvert : \lambda \in \spec(\A)\},
\]
called the **spectral radius** of \( \A \). Two of the criteria need nothing else: \( \A^{m} \to 0 \) if and only if \( \rho(\A) < 1 \), and \( \sum_k \A^{k} \) converges if and only if \( \rho(\A) < 1 \). The other two need more when \( \rho(\A) = 1 \): boundedness also asks for the block sizes at modulus \( 1 \), and convergence asks in addition that \( 1 \) be the only eigenvalue of modulus \( 1 \). Chapter 15 measures matrices by norms, proves that the spectral radius never exceeds the norm of \( \A \) induced by any vector norm, and recovers \( \rho(\A) \) as a limit built from the norms of the powers \( \A^{m} \); that is what turns these exact criteria into usable estimates.
:::

## Exercises

### A. Check your understanding

:::: {#exr-convergent-matrices-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define entrywise convergence and entrywise boundedness for a sequence of matrices.
2. Write down the entries of \( \J_k(\lambda)^{m} \), and say which one shows that a block of size \( \ge 2 \) with \( \lvert\lambda\rvert = 1 \) has unbounded powers.
3. State the three criteria: \( \A^{m} \to 0 \), \( (\A^{m}) \) bounded, \( (\A^{m}) \) convergent.
4. True or false: if every entry of \( \A \) has modulus less than \( 1 \), then \( \A^{m} \to 0 \). Justify your answer.
5. True or false: if \( (\A^{m}) \) is bounded then it converges. Justify your answer.
6. For which \( \A \) does \( \sum_k \A^{k} \) converge, and what is the sum?
:::
::::

::: {.solution}
(a) \( \M_m \to \M \) if \( (\M_m)_{rs} \to \M_{rs} \) for every position \( (r,s) \); \( (\M_m) \) is bounded if there is one constant \( c \) with \( \lvert(\M_m)_{rs}\rvert \le c \) for all \( m \) and all \( (r,s) \) (@def-entrywise-convergence).

(b) \( \bigl(\J_k(\lambda)^{m}\bigr)_{r,r+j} = \binom{m}{j}\lambda^{m-j} \) for \( 0 \le j \le k-1 \), with zeros below the diagonal (@lem-polynomial-of-jordan-block with \( p = x^{m} \)). The entry with \( j = 1 \) is \( m\lambda^{m-1} \), of modulus \( m \) when \( \lvert\lambda\rvert = 1 \).

(c) \( \A^{m} \to 0 \) iff every eigenvalue has \( \lvert\lambda\rvert < 1 \) (@thm-matrix-powers-converge-to-zero); \( (\A^{m}) \) is bounded iff every eigenvalue has \( \lvert\lambda\rvert \le 1 \) and those with \( \lvert\lambda\rvert = 1 \) have only \( 1 \times 1 \) blocks (@thm-matrix-powers-bounded); \( (\A^{m}) \) converges iff every eigenvalue has \( \lvert\lambda\rvert < 1 \) or equals \( 1 \) with only \( 1 \times 1 \) blocks (@thm-matrix-powers-converge).

(d) False. \( \A = \begin{pmatrix} 0.9 & 0.9 \\ 0.9 & 0.9\end{pmatrix} \) has the eigenvalue \( 1.8 \), and \( \A^{m}\1 = 1.8^{m}\1 \) is unbounded; see the warning after @thm-matrix-powers-converge-to-zero.

(e) False. \( \A = \begin{pmatrix} 0 & 1 \\ 1 & 0\end{pmatrix} \) satisfies \( \A^{2} = \I \), so \( \A^{m} \) alternates between \( \I \) and \( \A \) and is bounded but not convergent. Its eigenvalues are \( \pm 1 \), and the eigenvalue \( -1 \) is what @thm-matrix-powers-converge excludes.

(f) Exactly when every eigenvalue has \( \lvert\lambda\rvert < 1 \), and then the sum is \( (\I - \A)^{-1} \) (@thm-neumann-series-spectral).
:::

### B. Practice

:::: {#exr-convergent-matrices-b1}
[B1: Decide the behavior]

For each matrix over \( \nC \), decide whether \( \A^{m} \to 0 \), whether \( (\A^{m}) \) is bounded, and whether \( (\A^{m}) \) converges. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \A_1 = \begin{pmatrix} 1/2 & 1 \\ 0 & 1/2 \end{pmatrix} \).
2. \( \A_2 = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \).
3. \( \A_3 = \J_2(1) \oplus \J_1\bigl(\tfrac12\bigr) \in M_3(\nC) \).
4. \( \A_4 = \begin{pmatrix} 0 & 0 & 5 \\ 0 & 0 & 0 \\ 0 & 0 & 0\end{pmatrix} \).
:::
::::

::: {.solution}
(a) The only eigenvalue is \( \tfrac12 \), of modulus \( < 1 \), so \( \A_1^{m} \to 0 \) by @thm-matrix-powers-converge-to-zero; hence it is bounded and convergent. (The superdiagonal \( 1 \) is irrelevant: by @lem-polynomial-of-jordan-block the \( (1,2) \)-entry of \( \A_1^{m} \) is \( m\,2^{-(m-1)} \to 0 \) by (B1).)

(b) \( p_{\A_2} = x^{2} + 1 \), so \( \spec(\A_2) = \{i, -i\} \), both of modulus \( 1 \), and the eigenvalues are distinct, so every block has size \( 1 \). By @thm-matrix-powers-bounded, \( (\A_2^{m}) \) is **bounded**; it does not tend to \( 0 \) (@thm-matrix-powers-converge-to-zero) and does not converge, since the eigenvalue \( i \) has modulus \( 1 \) and is not \( 1 \) (@thm-matrix-powers-converge). Concretely \( \A_2^{4} = \I \), so the powers cycle through four matrices.

(c) The eigenvalue \( 1 \) has a block of size \( 2 \), so @thm-matrix-powers-bounded (ii) fails: \( (\A_3^{m}) \) is **unbounded**, hence neither convergent nor tending to \( 0 \). The \( (1,2) \)-entry of \( \A_3^{m} \) is \( m \).

(d) \( \A_4^{2} = 0 \), so \( \A_4^{m} = 0 \) for \( m \ge 2 \) and \( \A_4^{m} \to 0 \) trivially: all eigenvalues are \( 0 \). The large entry \( 5 \) does not matter, illustrating the warning after @thm-matrix-powers-converge-to-zero.
:::

:::: {#exr-convergent-matrices-b2}
[B2: Computing limits]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \A = \begin{pmatrix} 1/2 & 1/2 \\ 1/2 & 1/2\end{pmatrix} \). Show that \( \A^{m} \) converges and find the limit, both by @thm-matrix-powers-converge and by a direct computation of \( \A^{m} \).
2. Let \( \B = \begin{pmatrix} 1 & 1/3 \\ 0 & 1/3 \end{pmatrix} \). Find \( \lim_m \B^{m} \) and identify it as a projection.
:::
::::

::: {.solution}
(a) \( p_{\A} = x^{2} - x = x(x-1) \), so \( \spec(\A) = \{0, 1\} \). The eigenvalue \( 0 \) has \( \lvert 0\rvert < 1 \) and the eigenvalue \( 1 \) has \( a_{\A}(1) = 1 \), so its single block has size \( 1 \); by @thm-matrix-powers-converge the powers converge, and the limit is the projection onto \( E_1(\A) \) along \( G_0(\A) = E_0(\A) \). Now \( \A - \I = \begin{pmatrix} -1/2 & 1/2 \\ 1/2 & -1/2\end{pmatrix} \) gives \( E_1(\A) = \Span((1,1)) \) and \( E_0(\A) = \ker \A = \Span((1,-1)) \). With \( \Q = \begin{pmatrix} 1 & 1 \\ 1 & -1\end{pmatrix} \) and \( \Q^{-1} = \tfrac12\begin{pmatrix} 1 & 1 \\ 1 & -1\end{pmatrix} \),
\[
\lim_m \A^{m} = \Q\diag(1,0)\Q^{-1} = \tfrac12\begin{pmatrix} 1 & 1 \\ 1 & 1\end{pmatrix} = \A .
\]
*Directly.* \( \A^{2} = \A \), so \( \A^{m} = \A \) for every \( m \ge 1 \) and the limit is \( \A \). ( \( \A \) is itself a projection, and the theorem returns it unchanged.)

(b) \( \B \) is upper triangular, so \( \spec(\B) = \{1, \tfrac13\} \) (@thm-det-triangular). Both criteria hold: \( \lvert\tfrac13\rvert < 1 \), and \( a_{\B}(1) = 1 \) so the \( 1 \)-block has size \( 1 \). Solving \( (\B - \I)\x = \0 \) with \( \B - \I = \begin{pmatrix} 0 & 1/3 \\ 0 & -2/3\end{pmatrix} \) gives \( E_1(\B) = \Span(\e_1) \); solving \( (\B - \tfrac13\I)\x = \0 \) with \( \B - \tfrac13\I = \begin{pmatrix} 2/3 & 1/3 \\ 0 & 0\end{pmatrix} \) gives \( E_{1/3}(\B) = \Span((1, -2)) \). With \( \Q = \begin{pmatrix} 1 & 1 \\ 0 & -2\end{pmatrix} \) we have \( \det \Q = -2 \) and \( \Q^{-1} = \tfrac{1}{-2}\begin{pmatrix} -2 & -1 \\ 0 & 1\end{pmatrix} = \begin{pmatrix} 1 & 1/2 \\ 0 & -1/2\end{pmatrix} \). Multiplying in two steps, \( \Q\diag(1,0) = \begin{pmatrix} 1 & 0 \\ 0 & 0\end{pmatrix} \) and then
\[
\lim_m \B^{m} = \begin{pmatrix} 1 & 0 \\ 0 & 0\end{pmatrix}\Q^{-1} = \begin{pmatrix} 1 & 1/2 \\ 0 & 0 \end{pmatrix}.
\]
This is the projection onto \( \Span(\e_1) \) along \( \Span((1,-2)) \): it fixes \( \e_1 \) and sends \( (1,-2) \) to \( (1 - 1, 0) = \0 \). *Check.* \( \B^{m} = \begin{pmatrix} 1 & c_m \\ 0 & 3^{-m}\end{pmatrix} \) with \( c_1 = \tfrac13 \) and \( c_{m+1} = \tfrac13(1 + c_m) \), read off \( \B^{m+1} = \B^{m}\B \); the first values are \( \tfrac13, \tfrac49, \tfrac{13}{27} \), climbing towards the fixed point \( c = \tfrac13(1+c) \), that is \( c = \tfrac12 \).
:::

:::: {#exr-convergent-matrices-b3}
[B3: A Neumann series]

Let \( \A = \begin{pmatrix} 1/3 & 1/3 \\ 0 & 1/3\end{pmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Explain why \( \sum_k \A^{k} \) converges.
2. Compute \( (\I - \A)^{-1} \) directly.
3. Compute the partial sum \( \I + \A + \A^{2} \) and compare it with (b).
:::
::::

::: {.solution}
(a) \( \A \) is upper triangular with both diagonal entries \( \tfrac13 \), so \( \spec(\A) = \{\tfrac13\} \) (@thm-det-triangular) and \( \lvert\tfrac13\rvert < 1 \). By @thm-neumann-series-spectral the series converges, with sum \( (\I-\A)^{-1} \).

(b) \( \I - \A = \begin{pmatrix} 2/3 & -1/3 \\ 0 & 2/3\end{pmatrix} \), of determinant \( \tfrac49 \). By @thm-two-by-two-inverse,
\[
(\I-\A)^{-1} = \tfrac94\begin{pmatrix} 2/3 & 1/3 \\ 0 & 2/3\end{pmatrix} = \begin{pmatrix} 3/2 & 3/4 \\ 0 & 3/2\end{pmatrix}.
\]

(c) Write \( \A = \tfrac13(\I + \M) \) with \( \M = \begin{pmatrix} 0&1\\0&0\end{pmatrix} \), \( \M^{2} = 0 \); then \( \A^{k} = 3^{-k}(\I + k\M) \) by the binomial theorem, the two summands commuting. So
\[
\I + \A + \A^{2} = \bigl(1 + \tfrac13 + \tfrac19\bigr)\I + \bigl(\tfrac13 + \tfrac29\bigr)\M = \tfrac{13}{9}\I + \tfrac59 \M = \begin{pmatrix} 13/9 & 5/9 \\ 0 & 13/9\end{pmatrix}.
\]
Summing the whole series the same way, \( (\I-\A)^{-1} = \bigl(\sum_{k \ge 0}3^{-k}\bigr)\I + \bigl(\sum_{k \ge 0}k3^{-k}\bigr)\M \), so comparing with (b) reads off \( \sum_k 3^{-k} = \tfrac32 \) and \( \sum_k k3^{-k} = \tfrac34 \). The two partial sums \( \tfrac{13}{9} \) and \( \tfrac59 \), about \( 1.44 \) and \( 0.56 \), are on their way to \( \tfrac32 \) and \( \tfrac34 \); the convergence is geometric, as the factor \( 3^{-k} \) shows.
:::

### C. Going deeper

:::: {#exr-convergent-matrices-c1}
[C1: Bounded but not convergent]

::: {.enumerate options="label=(\alph*)"}
1. Give an example of \( \A \in M_2(\nR) \) with \( (\A^{m}) \) bounded but not convergent, and one with \( (\A^{m}) \) convergent but \( \A^{m} \not\to 0 \).
2. Prove that if \( \A^{m} \to \L \), then \( \L^{2} = \L \) and \( \A \L = \L \A = \L \).
3. Deduce that if \( \A^{m} \to \L \) with \( \L \) **invertible**, then \( \L = \I \) and \( \A = \I \).
4. Give an invertible \( \A \) with \( \A^{m} \to \L \) and \( \L \notin \{0, \I\} \), so that the invertibility of \( \L \), not of \( \A \), is what part (c) needs.
:::
::::

::: {.solution}
(a) For the first, \( \A = \begin{pmatrix} 0 & 1 \\ 1 & 0\end{pmatrix} \): \( \A^{2} = \I \), so \( \A^{m} \) alternates between \( \I \) and \( \A \) and is bounded but not convergent; its eigenvalues are \( \pm 1 \). For the second, \( \A = \begin{pmatrix} 1 & 0 \\ 0 & 1/2\end{pmatrix} \): \( \A^{m} = \diag(1, 2^{-m}) \to \diag(1, 0) \ne 0 \).

(b) Each entry of \( \A^{m}\A^{m} = \A^{2m} \) is a sum of products of entries of \( \A^{m} \), so by (B3) it converges to the corresponding expression in the entries of \( \L \); hence \( \A^{2m} \to \L^{2} \). But \( (\A^{2m})_m \) is a subsequence of \( (\A^{m})_m \) — more precisely, for each position the sequence \( (\A^{2m})_{rs} \) is a subsequence of the convergent sequence \( (\A^{m})_{rs} \), so it has the same limit \( \L_{rs} \). Hence \( \L^{2} = \L \). Similarly \( \A^{m+1} = \A \A^{m} = \A^{m}\A \), and the left side is a tail of the convergent sequence, so it tends to \( \L \), while the two right sides tend to \( \A \L \) and \( \L \A \) by (B3). Hence \( \A \L = \L \A = \L \).

(c) Suppose \( \A^{m} \to \L \) with \( \L \) invertible. By (b), \( \L^{2} = \L \); multiplying by \( \L^{-1} \) gives \( \L = \I \). Then \( \A \L = \L \) reads \( \A = \I \). (Conversely \( \A = \I \) gives \( \A^{m} = \I \to \I \), so this case really occurs.)

(d) \( \A = \diag(1, \tfrac12) \) is invertible, and \( \A^{m} = \diag(1, 2^{-m}) \to \diag(1, 0) = \L \), which is neither \( 0 \) nor \( \I \) — and not invertible. So no hypothesis on \( \A \) alone forces \( \L \in \{0, \I\} \): by @thm-matrix-powers-converge the limit is the projection onto \( E_1(\A) \) along the other generalized eigenspaces, and that projection is \( 0 \) or \( \I \) only in the extreme cases \( 1 \notin \spec(\A) \) and \( E_1(\A) = \nC^{n} \).
:::

:::: {#exr-convergent-matrices-c2}
[C2: Chapter 8's Markov theorem without diagonalizability]

Let \( \A \in M_n(\nR) \) be stochastic with \( a_{\A}(1) = 1 \) and \( \lvert\lambda\rvert < 1 \) for every eigenvalue \( \lambda \ne 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \1\tp\w = 0 \) for every \( \w \in G_\lambda(\A) \) with \( \lambda \ne 1 \). *Hint: \( \1\tp(\A - \lambda \I) = (1-\lambda)\1\tp \).*
2. Prove that \( (\A^{m}) \) converges to a **stochastic** matrix \( \vPi \), and deduce that \( \A \) has a steady state \( \v \) with \( E_1(\A) = \Span(\v) \).
3. Deduce that \( \vPi = \v\1\tp \) and that \( \A^{m}\x_0 \to \v \) for every probability vector \( \x_0 \), **without** assuming that \( \A \) is diagonalizable.
:::
::::

::: {.solution}
(a) Since \( \A \) is stochastic, \( \1\tp \A = \1\tp \) (@prp-stochastic-properties (c)), so \( \1\tp(\A - \lambda \I) = \1\tp - \lambda\1\tp = (1-\lambda)\1\tp \). Iterating \( n \) times, \( \1\tp(\A - \lambda \I)^{n} = (1-\lambda)^{n}\1\tp \). Let \( \w \in G_\lambda(\A) \), so \( (\A - \lambda \I)^{n}\w = \0 \) (@cor-generalized-eigenspace-is-kernel (a)). Then
\[
0 = \1\tp(\A - \lambda \I)^{n}\w = (1 - \lambda)^{n}\,\1\tp\w ,
\]
and \( \lambda \ne 1 \) gives \( (1-\lambda)^{n} \ne 0 \), so \( \1\tp\w = 0 \).

(b) By hypothesis \( 1 \) is the only eigenvalue of modulus \( 1 \), so \( (\A^{m}) \) converges by @cor-markov-powers-converge (b); call the limit \( \vPi \). Every \( \A^{m} \) is stochastic (@prp-stochastic-properties (b)), so all its entries are \( \ge 0 \) and each of its columns sums to \( 1 \). Both properties pass to the limit: a limit of real numbers \( \ge 0 \) is \( \ge 0 \), and a column sum is a finite sum of entries, so it converges to the sum of the limits (Chapter 8 §11). Hence \( \vPi \) is stochastic, and in particular \( \vPi \ne 0 \).

By @thm-matrix-powers-converge, \( \vPi \) is the projection onto \( E_1(\A) \) along \( \bigoplus_{\lambda \ne 1}G_\lambda(\A) \), so \( \im T_{\vPi} = E_1(\A) \). Since \( a_{\A}(1) = 1 \) and \( 1 \le g_{\A}(1) \le a_{\A}(1) \) (@thm-geometric-le-algebraic), \( E_1(\A) \) is a line. Each column of \( \vPi \) lies in \( \im T_{\vPi} = E_1(\A) \) (@def-matrix-multiplication: column \( j \) is \( \vPi\e_j \)) and is a probability vector, hence is fixed by \( \A \) and is a steady state. Any two probability vectors on the same line are equal: if \( \w = c\v \) with both entry sums equal to \( 1 \), then \( 1 = c \). So all the columns of \( \vPi \) are one and the same steady state \( \v \), and \( E_1(\A) = \Span(\v) \).

(c) All columns of \( \vPi \) equal \( \v \), which is exactly the statement \( \vPi = \v\1\tp \). (Independently of (b), part (a) confirms it: \( \v\1\tp \) fixes \( \v \) because \( \1\tp\v = 1 \), and kills every \( \w \in G_\lambda(\A) \) with \( \lambda \ne 1 \) because \( \1\tp\w = 0 \); by @thm-generalized-eigenspace-decomposition (a) those two conditions determine the projection onto \( E_1(\A) = G_1(\A) \) along the rest, using \( \dim G_1(\A) = a_{\A}(1) = 1 = \dim E_1(\A) \) and @thm-dim-impl-eq.) For a probability vector \( \x_0 \), each entry of \( \A^{m}\x_0 \) is a fixed linear combination of entries of \( \A^{m} \), so by (B3)
\[
\A^{m}\x_0 \longrightarrow \vPi\x_0 = \v\,(\1\tp\x_0) = \v\,(x_{01} + \dots + x_{0n}) = \v .
\]
No diagonalizability was used: the blocks for the eigenvalues \( \lambda \ne 1 \) may have any sizes, since @thm-matrix-powers-converge-to-zero does not care. This removes the diagonalizability hypothesis from @thm-markov-limit-diagonalizable.
:::
