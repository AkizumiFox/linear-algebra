# The Fast Fourier Transform

Chapter 11 §09 built one unitary matrix, \( \F \), that diagonalizes every circulant of its size, and then counted the cost of using it. Forming \( \F\b \) as a matrix–vector product takes about \( n^2 \) multiplications, so the elegant three-step recipe "transform, divide, transform back" for a circulant system costs \( O(n^2) \) — better than elimination, but not dramatically so. The section closed by naming the way out: the powers of \( \omega \) repeat, splitting one transform of length \( n \) into two of length \( n/2 \) costs almost nothing, and iterating "brings the cost down to about \( n\log n \)". That algorithm is the **fast Fourier transform**, and Chapter 11 handed it here, "together with the cost accounting that makes 'quickly' precise".

This section pays that debt. There is no new theorem about \( \F \) here; there is one matrix identity, proved by computing an entry, and one recurrence, solved exactly.

Throughout, as in Chapter 11 §09, **rows, columns and vector entries are numbered \( 0, 1, \dots, n-1 \)**, and \( \omega_n \coloneqq e^{2\pi i/n} \). We write \( \F_n \) for the Fourier matrix of size \( n \) of @thm-fourier-matrix-unitary, so \( (\F_n)_{jk} = \omega_n^{jk}/\sqrt n \); Chapter 11 wrote it \( \F \), the size being fixed there.

## Counting the cost of a transform

Chapter 11 §09 defined the **discrete Fourier transform** of \( \c \in \nC^n \) to be \( \widehat{\c} = \sqrt n\,\F_n\c \), the vector of eigenvalues \( p_{\c}(\omega_n^j) \) of the circulant with first row \( \c \). It is the unnormalized transform that the algorithm computes, so it is convenient to give its matrix a name of its own.

::: {#def-dft-matrix}
[The transform matrix]

For \( n \ge 1 \) let
\[
\W_n \coloneqq \sqrt n\,\F_n \in M_n(\nC), \qquad (\W_n)_{jk} = \omega_n^{jk} \quad (0 \le j,k \le n-1),
\]
so that \( \widehat{\c} = \W_n\c \) for every \( \c \in \nC^n \).
:::

A **cost** in this section is a count of arithmetic operations, where one complex addition, one complex subtraction, one complex multiplication and one complex division each count as **one operation**; a multiplication by the constant \( 1 \) is free, because it is not performed. What is being counted is the work of applying \( \W_n \) to an arbitrary vector, not the work of writing \( \W_n \) down.

Applying \( \W_n \) as a plain matrix–vector product costs
\[
n^2 \text{ multiplications} + n(n-1) \text{ additions} = 2n^2 - n
\]
operations: each of the \( n \) entries of \( \W_n\c \) is a sum of \( n \) products. This figure charges every one of those products, including the \( 2n-1 \) whose factor is an entry \( \omega_n^{0} = 1 \) of row \( 0 \) or column \( 0 \); it is the plain matrix–vector product as it is ordinarily performed, and the comparisons below use it as it stands. For \( n = 1024 \) that is \( 2\,096\,128 \) operations. The whole of this section is about replacing that number by about \( 15\,000 \).

## Splitting a transform in two

Where can a saving possibly come from? The entries of \( \W_n \) are powers of \( \omega_n \), and there are only \( n \) distinct ones, so the \( n^2 \) products \( \omega_n^{jk}c_k \) involve enormous repetition. The single algebraic fact that organizes the repetition is
\[
\omega_n^2 = e^{4\pi i/n} = e^{2\pi i/m} = \omega_m, \qquad \text{where } n = 2m .
\]
Squaring a primitive \( n \)-th root of unity gives a primitive \( m \)-th root of unity. So if we separate the even-numbered entries of \( \c \) from the odd-numbered ones, the even half is transformed by \( \W_m \), not by anything new. Two objects give the bookkeeping a name.

::: {#def-butterfly-and-twiddle}
[The even-odd permutation, the twiddle matrix and the butterfly]

Let \( n = 2m \) with \( m \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. The **even-odd permutation matrix** \( \P_n \in M_n(\nC) \) is the permutation matrix determined by
   \[
   (\P_n\x)_t = x_{2t}, \qquad (\P_n\x)_{m+t} = x_{2t+1} \qquad (0 \le t \le m-1);
   \]
   it lists the even-numbered entries of \( \x \) first, then the odd-numbered ones, each in their original order.
2. The **twiddle matrix** is \( \D_m \coloneqq \diag\bigl(1, \omega_n, \omega_n^2, \dots, \omega_n^{m-1}\bigr) \in M_m(\nC) \). Its entries are powers of \( \omega_n \), **not** of \( \omega_m \).
3. The **butterfly matrix** is
   \[
   \B_n \coloneqq \begin{pmatrix} \I_m & \D_m \\ \I_m & -\D_m \end{pmatrix} \in M_n(\nC) .
   \]
:::
:::

In words: \( \P_n \) is pure data movement and does no arithmetic; \( \D_m \) supplies the \( m \) twiddles that the odd half needs because it starts one place late; and \( \B_n \) forms the \( m \) sums and the \( m \) differences that recombine the two halves. Applied to a vector \( (\u, \v) \) split into two halves of length \( m \), the butterfly returns \( (\u + \D_m\v,\ \u - \D_m\v) \).

::: {#thm-fft-factorization}
[The Radix-Two Factorization]

Let \( n = 2m \) with \( m \ge 1 \). Then
\[
\W_n = \B_n \begin{pmatrix} \W_m & 0 \\ 0 & \W_m \end{pmatrix} \P_n .
\]
Equivalently, for the unitary Fourier matrices,
\[
\F_n = \frac{1}{\sqrt2}\,\B_n \begin{pmatrix} \F_m & 0 \\ 0 & \F_m \end{pmatrix} \P_n .
\]
:::

::: {.idea}
Apply both sides to an arbitrary \( \x \) and compute entry \( j \) of the left side. Split the defining sum \( \sum_k \omega_n^{jk}x_k \) into its even \( k = 2t \) and odd \( k = 2t+1 \) parts; the relation \( \omega_n^2 = \omega_m \) turns each part into a transform of length \( m \), and the odd part carries one spare factor \( \omega_n^j \). That is the whole computation, and it already gives the top half of the answer. For the bottom half, write \( j = m + i \); the relation \( \omega_m^m = 1 \) makes the two transforms of length \( m \) repeat what they gave at \( i \), while \( \omega_n^m = -1 \) flips the sign of the spare factor. Sum and difference: the butterfly.
:::

::: {.proof}
Let \( \x \in \nC^n \) and put
\[
\u \coloneqq \W_m\bigl(x_0, x_2, \dots, x_{n-2}\bigr), \qquad
\v \coloneqq \W_m\bigl(x_1, x_3, \dots, x_{n-1}\bigr),
\]
so that \( u_i = \sum_{t=0}^{m-1}\omega_m^{it}x_{2t} \) and \( v_i = \sum_{t=0}^{m-1}\omega_m^{it}x_{2t+1} \) for \( 0 \le i \le m-1 \), by @def-dft-matrix. By @def-butterfly-and-twiddle (a), \( \P_n\x \) is exactly the pair of these two argument vectors stacked, so the right-hand side applied to \( \x \) is \( \B_n(\u, \v) = (\u + \D_m\v,\ \u - \D_m\v) \).

Now compute entry \( j \) of \( \W_n\x \). Splitting the index \( k \) into \( k = 2t \) and \( k = 2t+1 \) with \( 0 \le t \le m-1 \), and using \( \omega_n^{2} = \omega_m \),
\[
\begin{aligned}
(\W_n\x)_j &= \sum_{k=0}^{n-1}\omega_n^{jk}x_k
= \sum_{t=0}^{m-1}\omega_n^{2jt}x_{2t} + \sum_{t=0}^{m-1}\omega_n^{j(2t+1)}x_{2t+1} \\
&= \sum_{t=0}^{m-1}\omega_m^{jt}x_{2t} + \omega_n^{j}\sum_{t=0}^{m-1}\omega_m^{jt}x_{2t+1} .
\end{aligned}
\]

*Top half.* For \( 0 \le j \le m-1 \) the two sums are \( u_j \) and \( v_j \), so
\[
(\W_n\x)_j = u_j + \omega_n^{j}v_j = \bigl(\u + \D_m\v\bigr)_j ,
\]
the last equality by @def-butterfly-and-twiddle (b), the \( j \)-th diagonal entry of \( \D_m \) being \( \omega_n^{j} \).

*Bottom half.* For \( j = m+i \) with \( 0 \le i \le m-1 \), we have \( \omega_m^{jt} = \omega_m^{mt}\omega_m^{it} = \omega_m^{it} \), since \( \omega_m^{m} = 1 \); so both sums repeat their values at \( i \), namely \( u_i \) and \( v_i \). The spare factor is
\[
\omega_n^{m+i} = \omega_n^{m}\,\omega_n^{i} = e^{\pi i}\,\omega_n^{i} = -\omega_n^{i} ,
\]
because \( \omega_n^m = e^{2\pi i m/n} = e^{\pi i} = -1 \). Hence
\[
(\W_n\x)_{m+i} = u_i - \omega_n^{i}v_i = \bigl(\u - \D_m\v\bigr)_i .
\]

The two halves together say that \( \W_n\x \) equals the right-hand side applied to \( \x \), for every \( \x \in \nC^n \); so the two matrices are equal. For the second display, substitute \( \W_n = \sqrt n\,\F_n \) and \( \W_m = \sqrt m\,\F_m \) and divide by \( \sqrt n \), using \( \sqrt m/\sqrt n = 1/\sqrt2 \).
:::

The identity is a factorization of one matrix into three, and each of the three is cheap for a different reason: \( \P_n \) does no arithmetic, the middle factor is two copies of a **smaller instance of the same problem**, and \( \B_n \) costs \( O(n) \). That is the entire content of the fast Fourier transform. Everything below is bookkeeping.

::: {.check}
Write out @thm-fft-factorization for \( n = 2 \) and check it directly.
:::

::: {.solution}
Here \( m = 1 \), so \( \P_2 = \I_2 \) (it lists \( x_0 \) then \( x_1 \)), \( \W_1 = (1) \), and \( \D_1 = (\omega_2^0) = (1) \). Hence
\[
\B_2 = \begin{pmatrix} 1 & 1 \\ 1 & -1\end{pmatrix},
\]
and the right-hand side is \( \B_2\I_2\I_2 = \B_2 \). And \( (\W_2)_{jk} = \omega_2^{jk} = (-1)^{jk} \), which is the same matrix.
:::

::: {#exm-fft-four}
[The factorization for \( n = 4 \)]

Write out @thm-fft-factorization for \( n = 4 \), and check it against the matrix \( \F \) of @exm-fourier-matrix-4.
:::

::: {.solution}
Here \( m = 2 \) and \( \omega_4 = i \), so \( \D_2 = \diag(1, i) \) and
\[
\B_4 = \begin{pmatrix} 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & i \\ 1 & 0 & -1 & 0 \\ 0 & 1 & 0 & -i\end{pmatrix},
\quad
\P_4 = \begin{pmatrix} 1&0&0&0 \\ 0&0&1&0 \\ 0&1&0&0 \\ 0&0&0&1\end{pmatrix},
\quad
\W_2 = \begin{pmatrix} 1 & 1 \\ 1 & -1\end{pmatrix}.
\]
Multiplying, \( \begin{pmatrix}\W_2 & 0 \\ 0 & \W_2\end{pmatrix}\P_4 \) has rows \( (1,0,1,0) \), \( (1,0,-1,0) \), \( (0,1,0,1) \), \( (0,1,0,-1) \). Applying \( \B_4 \) adds row 3 to row 1, adds \( i \) times row 4 to row 2, and so on, giving
\[
\B_4\begin{pmatrix}\W_2 & 0 \\ 0 & \W_2\end{pmatrix}\P_4
= \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & i & -1 & -i \\ 1 & -1 & 1 & -1 \\ 1 & -i & -1 & i\end{pmatrix} = \W_4 ,
\]
whose \( (j,k) \)-entry is \( i^{jk} \). Dividing by \( \sqrt4 = 2 \) returns the matrix \( \F = \tfrac12\W_4 \) written out in @exm-fourier-matrix-4.
:::

::: {.warning}
**The twiddles are powers of \( \omega_n \), not of \( \omega_m \).** If \( \D_2 \) in @exm-fft-four is taken to be \( \diag(1, \omega_2) = \diag(1,-1) \), the product becomes the **real** matrix with rows \( (1,1,1,1) \), \( (1,-1,-1,1) \), \( (1,-1,1,-1) \), \( (1,1,-1,-1) \), whereas the second row of \( \W_4 \) is \( (1, i, -1, -i) \). The single factor \( \omega_n^{j} \) in the proof is what remembers that the odd-numbered entries start one step later, and it is the only place where the transform of size \( n \) differs from two transforms of size \( m \).
:::

## The cost, exactly

Read @thm-fft-factorization from right to left as a procedure.

::: {.algorithm}
**Input.** \( \x \in \nC^n \), with \( n = 2^p \) a power of two.

**Output.** \( \W_n\x \).

1. If \( n = 1 \), return \( \x \).
2. Split \( \x \) into its even-numbered and odd-numbered entries (no arithmetic).
3. Compute \( \u \) and \( \v \), the transforms of the two halves, by applying this procedure to each of them.
4. Multiply: set \( v'_0 \coloneqq v_0 \), and \( v'_i \coloneqq \omega_n^{i}v_i \) for \( 1 \le i \le m-1 \), where \( m = n/2 \).
5. Return \( (\u + \v',\ \u - \v') \).
:::

The procedure returns \( \W_n\x \) for every \( n = 2^p \), by induction on \( p \): for \( p = 0 \) step 1 returns \( \x = \W_1\x \), and for \( n = 2m \) the inductive hypothesis makes the \( \u \) and \( \v \) of step 3 the two transforms of length \( m \) named in the proof of @thm-fft-factorization, so steps 4 and 5 return \( (\u + \D_m\v,\ \u - \D_m\v) \), which that proof identifies with \( \W_n\x \). What is left is the cost.

::: {#thm-fft-cost}
[The Cost of the Fast Fourier Transform]

Let \( C(n) \) be the number of operations the procedure above performs on an input of length \( n = 2^p \), with \( p \ge 0 \). Then \( C(1) = 0 \),
\[
C(2m) = 2C(m) + 3m - 1 \qquad (m \ge 1),
\]
and the solution of this recurrence is exactly
\[
C(2^p) = \tfrac32\,p\,2^{p} - 2^{p} + 1,
\qquad\text{that is}\qquad
C(n) = \tfrac32\,n\log_2 n - n + 1 .
\]
In particular \( C(n) = O(n\log n) \).
:::

::: {.idea}
Step 3 is where the recursion sits and contributes \( 2C(m) \); steps 4 and 5 are the only arithmetic outside it, and both are linear in \( n \). Count them once, carefully: step 4 is \( m-1 \) multiplications, the factor \( \omega_n^0 = 1 \) at \( i = 0 \) not being applied at all, and step 5 is \( m \) additions and \( m \) subtractions. Then solve the recurrence by induction on \( p \), which works because the recursion halves the length exactly.
:::

::: {.proof}
For \( n = 1 \) the procedure returns its input and does nothing, so \( C(1) = 0 \).

Let \( n = 2m \) with \( m \ge 1 \). Step 2 only moves data. Step 3 calls the procedure twice on length \( m \), costing \( 2C(m) \). Step 4 copies \( v_0 \), which is no arithmetic, and forms \( \omega_n^i v_i \) for \( i = 1, \dots, m-1 \), which is \( m-1 \) multiplications. Step 5 forms \( m \) sums and \( m \) differences, which is \( 2m \) operations. Adding,
\[
C(2m) = 2C(m) + (m-1) + 2m = 2C(m) + 3m - 1 .
\]

Now induct on \( p \). For \( p = 0 \), the formula gives \( \tfrac32\cdot0\cdot1 - 1 + 1 = 0 = C(1) \). Let \( p \ge 1 \) and suppose \( C(2^{p-1}) = \tfrac32(p-1)2^{p-1} - 2^{p-1} + 1 \). Taking \( m = 2^{p-1} \) in the recurrence,
\[
\begin{aligned}
C(2^{p}) &= 2\Bigl(\tfrac32(p-1)2^{p-1} - 2^{p-1} + 1\Bigr) + 3\cdot2^{p-1} - 1 \\
&= \tfrac32(p-1)2^{p} - 2^{p} + 2 + \tfrac32 \cdot 2^{p} - 1 \\
&= \tfrac32 p\,2^{p} - 2^{p} + 1 ,
\end{aligned}
\]
where the last line collects \( \tfrac32(p-1)2^p + \tfrac32 2^p = \tfrac32 p 2^p \). This completes the induction. Substituting \( n = 2^p \), so \( p = \log_2 n \), gives the stated formula, and \( \tfrac32 n\log_2 n - n + 1 \le \tfrac32 n \log_2 n \) for \( n \ge 1 \), so \( C(n) = O(n\log n) \).
:::

The exact formula is worth tabulating against the \( 2n^2 - n \) of a plain matrix–vector product.

| \( n \) | \( C(n) \) | \( 2n^2 - n \) |
|---|---|---|
| \( 2 \) | \( 2 \) | \( 6 \) |
| \( 8 \) | \( 29 \) | \( 120 \) |
| \( 32 \) | \( 209 \) | \( 2\,016 \) |
| \( 1024 \) | \( 14\,337 \) | \( 2\,096\,128 \) |

At \( n = 1024 \) the ratio is about \( 146 \), and it grows without bound, because \( (2n^2-n)/C(n) \) behaves like \( \tfrac43 n/\log_2 n \). This is the sense in which the transform can be applied "quickly": the exponent drops from \( 2 \) to \( 1 \), up to a logarithm, and the constant \( \tfrac32 \) in front is small.

::: {.warning}
**The recursion needs \( n \) even at every level, so \( n = 2^p \) is the clean case.** For \( n \) odd and greater than \( 1 \) the factorization of @thm-fft-factorization does not apply at all, and the procedure above cannot start. For \( n = 2^a q \) with \( q \) odd, it descends \( a \) levels and then must transform vectors of length \( q \) some other way; if \( q \) is large, nothing has been gained. The remedy is either to split by other factors of \( n \), as in @exr-the-fast-fourier-transform-c1, or, for the convolution use below, to pad with zeros up to the next power of two — which at most doubles \( n \) and so changes the cost by a bounded factor.
:::

::: {#exm-fft-eight}
[A transform of length eight]

Compute \( \W_8\c \) for \( \c = (1,2,3,4,1,2,3,4) \) by the procedure, showing every level, and check the result against the direct definition at one entry.
:::

::: {.solution}
*Level 1.* The even-numbered entries are \( (1,3,1,3) \) and the odd-numbered ones are \( (2,4,2,4) \).

*Level 2, applied to \( (1,3,1,3) \).* Its even and odd halves are \( (1,1) \) and \( (3,3) \), whose transforms are \( \W_2(1,1) = (2,0) \) and \( \W_2(3,3) = (6,0) \). Here \( n = 4 \), so \( \D_2 = \diag(1,i) \) and \( \D_2(6,0) = (6,0) \). The butterfly gives \( (2+6,\ 0+0,\ 2-6,\ 0-0) = (8,0,-4,0) \). So \( \u = (8,0,-4,0) \).

*Level 2, applied to \( (2,4,2,4) \).* Its even and odd halves are \( (2,2) \) and \( (4,4) \), whose transforms are \( \W_2(2,2) = (4,0) \) and \( \W_2(4,4) = (8,0) \). Again \( n = 4 \) and \( \D_2(8,0) = (8,0) \), so the butterfly gives \( (4+8,\ 0,\ 4-8,\ 0) \). So \( \v = (12,0,-4,0) \).

*Level 1, recombination.* Now \( n = 8 \) and \( \D_4 = \diag(1, \omega_8, i, \omega_8^3) \) with \( \omega_8 = e^{\pi i/4} \), so
\[
\D_4\v = (12,\ 0,\ -4i,\ 0) ,
\]
the irrational entries of \( \D_4 \) never appearing because \( v_1 = v_3 = 0 \). The butterfly gives
\[
\W_8\c = \bigl(20,\ 0,\ -4-4i,\ 0,\ -4,\ 0,\ -4+4i,\ 0\bigr) .
\]

*Check at \( j = 2 \).* By @def-dft-matrix, \( (\W_8\c)_2 = \sum_k \omega_8^{2k}c_k = \sum_k i^{k}c_k \) since \( \omega_8^2 = i \). This is
\[
1 + 2i - 3 - 4i + 1 + 2i - 3 - 4i = -4 - 4i ,
\]
matching. The zeros in the odd positions are not an accident. Since \( \c \) repeats with period \( 4 \), that is \( c_{k+4} = c_k \), splitting the defining sum at \( k = 4 \) gives
\[
(\W_8\c)_j = \sum_{k=0}^{3}c_k\bigl(\omega_8^{jk} + \omega_8^{j(k+4)}\bigr) = \bigl(1 + (-1)^{j}\bigr)\sum_{k=0}^{3}\omega_8^{jk}c_k ,
\]
using \( \omega_8^{4j} = (e^{\pi i})^{j} = (-1)^{j} \). The factor \( 1 + (-1)^{j} \) is \( 0 \) at every odd \( j \).
:::

## What the speed buys

Two corollaries, both immediate now, and both paying off Chapter 11 §09.

Chapter 11 §09 proved the Convolution Theorem: \( \widehat{\c \ast \d} = \widehat{\c}\odot\widehat{\d} \) entrywise (@thm-convolution-theorem (b)). Before this section that identity converted an \( O(n^2) \) convolution into three \( O(n^2) \) transforms, which is no gain at all. With @thm-fft-cost it becomes a genuine algorithm.

::: {#cor-fast-convolution}
[Convolution in \( O(n\log n) \)]

Let \( n = 2^p \). The cyclic convolution \( \c \ast \d \) of two vectors in \( \nC^n \) can be computed in
\[
3C(n) + 2n = \tfrac92\,n\log_2 n - n + 3
\]
operations, where \( C \) is as in @thm-fft-cost. Consequently, the product of two polynomials in \( \nC[x] \) of degree at most \( d \) can be computed in \( O(d\log d) \) operations.
:::

::: {.proof}
**The inverse transform costs the same.** By @thm-fourier-matrix-unitary, \( \F_n^{-1} = \F_n^{*} \), and \( \F_n \) is symmetric because \( (\F_n)_{jk} = \omega_n^{jk}/\sqrt n \) is unchanged by swapping \( j \) and \( k \); hence \( \F_n^{*} = \conj{\F_n} \) and
\[
\W_n^{-1} = \tfrac{1}{\sqrt n}\F_n^{-1} = \tfrac{1}{\sqrt n}\conj{\F_n} = \tfrac1n\conj{\W_n} .
\]
Conjugating the identity of @thm-fft-factorization entry by entry, and noting that \( \P_n \) is real, gives
\[
\conj{\W_n} = \conj{\B_n}\begin{pmatrix} \conj{\W_m} & 0 \\ 0 & \conj{\W_m}\end{pmatrix}\P_n ,
\]
which is the same factorization with every \( \omega_n \) replaced by \( \conj{\omega_n} = \omega_n^{-1} \). The procedure therefore runs verbatim with \( \omega_n^{-1} \) in place of \( \omega_n \) and computes \( \conj{\W_n}\y \) in \( C(n) \) operations.

**The algorithm.** By @thm-convolution-theorem (b) and the definition \( \widehat{\c} = \W_n\c \),
\[
\W_n(\c\ast\d) = (\W_n\c)\odot(\W_n\d),
\qquad\text{so}\qquad
\c\ast\d = \tfrac1n\,\conj{\W_n}\bigl((\W_n\c)\odot(\W_n\d)\bigr) .
\]
Computing \( \W_n\c \) and \( \W_n\d \) costs \( 2C(n) \); the \( n \) entrywise products cost \( n \); the inverse transform costs \( C(n) \); the \( n \) divisions by \( n \) cost \( n \). The total is \( 3C(n) + 2n \), and substituting the formula of @thm-fft-cost gives \( \tfrac92 n\log_2 n - 3n + 3 + 2n \), as stated.

**Polynomials.** Let \( p = \sum_{l=0}^{d}p_lx^{l} \) and \( q = \sum_{l=0}^{d}q_lx^{l} \), and choose \( n = 2^{P} \) with \( n \ge 2d+1 \) and \( n < 4d+2 \), which is possible since the powers of two are spaced by a factor of two. Let \( \c, \d \in \nC^n \) be the coefficient vectors padded with zeros. The coefficient of \( x^{r} \) in \( pq \), for \( 0 \le r \le 2d \), is \( \sum_{l} c_l d_{r-l} \) summed over \( 0 \le l \le r \), while \( (\c\ast\d)_r = \sum_{l=0}^{n-1}c_ld_{r-l} \) with the subscript read modulo \( n \). The two agree: a term of the second sum with \( l > r \) has \( d \)-subscript \( r-l+n \), and it can be non-zero only if \( l \le d \) and \( r-l+n \le d \), which forces \( n \le d + l - r \le 2d \), contradicting \( n \ge 2d+1 \). So the coefficients of \( pq \) are the first \( 2d+1 \) entries of \( \c\ast\d \), computable in \( 3C(n) + 2n \) operations with \( n < 4d+2 \), which is \( O(d\log d) \).
:::

::: {.warning}
**Convolution wraps around; polynomial multiplication does not.** Padding to length \( n \ge 2d+1 \) is not a convenience, it is the hypothesis. Take \( p = q = 1 + x \), so \( d = 1 \), and convolve the unpadded vectors \( \c = \d = (1,1) \) in \( \nC^2 \): the answer is \( (c_0d_0 + c_1d_1,\ c_0d_1 + c_1d_0) = (2,2) \), the coefficient vector of \( 2 + 2x \), whereas \( (1+x)^2 = 1 + 2x + x^2 \). The \( x^2 \) term has wrapped around onto the constant term, because in \( \nC^n \) the exponents are read modulo \( n \) and \( x^2 \equiv 1 \). Padding to \( \c = \d = (1,1,0,0) \) in \( \nC^4 \) gives \( (1,2,1,0) \), which is right.
:::

::: {#cor-fast-circulant-solve}
[Solving a Circulant System in \( O(n\log n) \)]

Let \( n = 2^p \), let \( \C \in M_n(\nC) \) be an invertible circulant with first row \( \c \), and let \( \b \in \nC^n \). Then the solution of \( \C\x = \b \) can be computed in \( 3C(n) + 2n \) operations.
:::

::: {.proof}
By @thm-circulant-diagonalization, \( \C = \F_n\vLambda\F_n^{*} \) with \( \vLambda = \diag(p_{\c}(1), \dots, p_{\c}(\omega_n^{n-1})) \), and the diagonal of \( \vLambda \) is exactly \( \widehat{\c} = \W_n\c \); the letter \( \D \) is reserved here for the twiddle matrix of @def-butterfly-and-twiddle. Since \( \C \) is invertible, every \( \widehat{c}_j \ne 0 \) by @cor-circulants-algebra (d), so \( \vLambda^{-1} \) exists and
\[
\x = \C^{-1}\b = \F_n\vLambda^{-1}\F_n^{*}\b = \tfrac1n\,\W_n\Bigl(\bigl(\conj{\W_n}\b\bigr) \oslash \widehat{\c}\Bigr),
\]
where \( \oslash \) is entrywise division and the last equality uses \( \F_n = n^{-1/2}\W_n \) and \( \F_n^{*} = n^{-1/2}\conj{\W_n} \), as in the proof of @cor-fast-convolution. The three transforms cost \( C(n) \) each, by @thm-fft-cost and the first part of that proof; the \( n \) divisions and the \( n \) final scalings by \( 1/n \) cost \( 2n \). Sanity check at \( \C = \I_n \): then \( \c = \e_0 \), \( \widehat{\c} = (1,\dots,1) \), and the formula returns \( \tfrac1n\W_n\conj{\W_n}\b = \tfrac1n(n\I_n)\b = \b \), using \( \W_n\conj{\W_n} = n\F_n\F_n^{*} = n\I_n \).
:::

::: {.remark}
None of this is a new theorem about the discrete Fourier transform. The matrix \( \F_n \), the factorization \( \C = \F_n\vLambda\F_n^{*} \) of @thm-circulant-diagonalization and the Convolution Theorem (@thm-convolution-theorem) are exactly as Chapter 11 left them; @thm-fft-factorization is an identity between matrices all of which were already known, and @thm-fft-cost counts operations. The transform is a change of basis, and the fast Fourier transform is a way of applying that change of basis in \( O(n\log n) \) operations instead of \( O(n^2) \). What changes is not what can be computed but what can be computed at the sizes that occur.
:::

## Exercises

### A. Check your understanding

::: {#exr-the-fast-fourier-transform-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Write down the matrix \( \W_n \), and say how it is related to the Fourier matrix \( \F_n \) of Chapter 11.
2. State @thm-fft-factorization, and say what each of the three factors on the right costs to apply.
3. How many operations does \( \W_n\x \) cost as a plain matrix–vector product, and how many by the fast algorithm when \( n = 2^p \)?
4. True or false: the fast Fourier transform computes a different transform from the one in Chapter 11, which is why it is faster. Justify your answer.
5. Why does the algorithm require \( n \) to be a power of two, and what is done when it is not?
:::
:::

::: {.solution}
(a) \( \W_n = \sqrt n\,\F_n \), with \( (\W_n)_{jk} = \omega_n^{jk} \) for \( 0 \le j,k \le n-1 \) and \( \omega_n = e^{2\pi i/n} \) (@def-dft-matrix). It is the matrix of the discrete Fourier transform \( \c \mapsto \widehat{\c} \) of Chapter 11 §09.

(b) \( \W_n = \B_n\left(\begin{smallmatrix}\W_m & 0\\ 0 & \W_m\end{smallmatrix}\right)\P_n \) for \( n = 2m \). Applying \( \P_n \) costs nothing, since it only moves entries; the middle factor costs two transforms of length \( m \); and \( \B_n \) costs \( m-1 \) multiplications and \( 2m \) additions and subtractions.

(c) Directly: \( n^2 \) multiplications and \( n(n-1) \) additions, that is \( 2n^2 - n \). By the algorithm: \( C(n) = \tfrac32 n\log_2 n - n + 1 \) (@thm-fft-cost).

(d) False. @thm-fft-factorization is an identity between matrices, so the algorithm returns \( \W_n\x \) exactly, in exact arithmetic. It is faster because it applies the same matrix by a cheaper route, not because it computes something else.

(e) The factorization needs \( n = 2m \), and the recursion needs that at every level, so it needs \( n = 2^p \). For other \( n \) one either pads with zeros to the next power of two, which is legitimate for convolution provided the padded length still exceeds the degree of the product (see the warning after @cor-fast-convolution), or splits by a different factor of \( n \), as in @exr-the-fast-fourier-transform-c1.
:::

### B. Practice

::: {#exr-the-fast-fourier-transform-b1}
[B1: A transform of length four]

Let \( \c = (1, 1, -1, -1) \in \nC^4 \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \W_4\c \) by the procedure of this section, showing the two halves and the twiddles.
2. Check the answer by evaluating the symbol \( p_{\c} \) at the fourth roots of unity.
3. Count the operations your computation in (a) used, and compare with \( C(4) \).
:::
:::

::: {.solution}
(a) The even-numbered entries are \( (1,-1) \) and the odd-numbered ones are \( (1,-1) \). Both transform to \( \W_2(1,-1) = (1 - 1,\ 1 + 1) = (0, 2) \), so \( \u = \v = (0,2) \). With \( n = 4 \), \( \D_2 = \diag(1, i) \), so \( \D_2\v = (0, 2i) \). The butterfly gives
\[
\W_4\c = \bigl(0 + 0,\ 2 + 2i,\ 0 - 0,\ 2 - 2i\bigr) = (0,\ 2+2i,\ 0,\ 2-2i) .
\]

(b) The symbol is \( p_{\c}(x) = 1 + x - x^2 - x^3 \) (@def-circulant), and \( \widehat{c}_j = p_{\c}(i^{j}) \). Then \( p_{\c}(1) = 1+1-1-1 = 0 \); \( p_{\c}(i) = 1 + i + 1 + i = 2+2i \), using \( -i^2 = 1 \) and \( -i^3 = i \); \( p_{\c}(-1) = 1 - 1 - 1 + 1 = 0 \); and \( p_{\c}(-i) = 1 - i + 1 - i = 2-2i \). The four values agree with (a).

(c) Each \( \W_2 \) costs \( 2 \) operations (one sum, one difference), so the two halves cost \( 4 \); the twiddles cost \( 1 \), since the factor \( 1 \) is free and only \( i\cdot2 \) is a multiplication; the final butterfly costs \( 4 \). The total is \( 9 \), and \( C(4) = \tfrac32\cdot4\cdot2 - 4 + 1 = 9 \). A direct matrix–vector product would cost \( 2\cdot16 - 4 = 28 \).
:::

::: {#exr-the-fast-fourier-transform-b2}
[B2: A transform of length eight]

Let \( \c = (2, 1, 0, 3, 2, 1, 0, 3) \in \nC^8 \). Compute \( \W_8\c \) by the procedure, showing both levels, and verify entry \( j = 2 \) directly from @def-dft-matrix.
:::

::: {.solution}
*Level 1.* Even-numbered entries \( (2, 0, 2, 0) \); odd-numbered entries \( (1, 3, 1, 3) \).

*Level 2 on \( (2,0,2,0) \).* Halves \( (2,2) \) and \( (0,0) \), with transforms \( (4,0) \) and \( (0,0) \). Here the inner \( n \) is \( 4 \), so \( \D_2 = \diag(1,i) \) and \( \D_2(0,0) = (0,0) \). The butterfly gives \( \u = (4, 0, 4, 0) \).

*Level 2 on \( (1,3,1,3) \).* Halves \( (1,1) \) and \( (3,3) \), with transforms \( (2,0) \) and \( (6,0) \); \( \D_2(6,0) = (6,0) \); the butterfly gives \( \v = (8, 0, -4, 0) \).

*Level 1, recombination.* Now \( n = 8 \) and \( \D_4 = \diag(1, \omega_8, i, \omega_8^3) \), so \( \D_4\v = (8, 0, -4i, 0) \). Hence
\[
\begin{aligned}
\W_8\c &= (4+8,\ 0,\ 4-4i,\ 0,\ 4-8,\ 0,\ 4+4i,\ 0)\\
&= (12, 0, 4-4i, 0, -4, 0, 4+4i, 0).
\end{aligned}
\]

*Check at \( j = 2 \).* Since \( \omega_8^2 = i \), @def-dft-matrix gives \( (\W_8\c)_2 = \sum_k i^{k}c_k = 2 + i + 0 - 3i + 2 + i + 0 - 3i = 4 - 4i \), as computed.
:::

::: {#exr-the-fast-fourier-transform-b3}
[B3: A product of polynomials by convolution]

Let \( p = 1 + 2x + 3x^2 \) and \( q = 2 + x \) in \( \nC[x] \).

::: {.enumerate options="label=(\alph*)"}
1. What is the smallest power of two \( n \) for which the recipe in the proof of @cor-fast-convolution is valid? Write down the padded coefficient vectors \( \c \) and \( \d \).
2. Compute \( \c \ast \d \) directly from the definition of cyclic convolution, and read off \( pq \).
3. Show that using \( n = 3 \) instead would give the wrong answer, and identify which coefficient wraps onto which.
:::
:::

::: {.solution}
(a) The product \( pq \) has degree \( 3 \), so \( 4 \) coefficients are needed and any \( n \ge 4 \) works; the smallest power of two is \( n = 4 \). The padded vectors are \( \c = (1,2,3,0) \) and \( \d = (2,1,0,0) \).

(b) With subscripts modulo \( 4 \) and \( d_0 = 2 \), \( d_1 = 1 \), \( d_2 = d_3 = 0 \), the sum \( (\c\ast\d)_r = \sum_l c_l d_{r-l} \) keeps only \( l = r \) and \( l = r-1 \), so \( (\c\ast\d)_r = 2c_r + c_{r-1} \):
\[
\c \ast \d = (2 + 0,\ 4 + 1,\ 6 + 2,\ 0 + 3) = (2, 5, 8, 3) .
\]
Hence \( pq = 2 + 5x + 8x^2 + 3x^3 \), which one checks by expanding: \( (1+2x+3x^2)(2+x) = 2 + x + 4x + 2x^2 + 6x^2 + 3x^3 \).

(c) Length \( 3 \) holds \( p \) and \( q \) but not the four coefficients of \( pq \), and although \( 3 \) is not a power of two it shows the wrap plainly: with \( \c = (1,2,3) \), \( \d = (2,1,0) \) and subscripts modulo \( 3 \),
\[
\c \ast \d = (2 + 3,\ 4 + 1,\ 6 + 2) = (5, 5, 8) ,
\]
which is \( pq \) with the coefficient \( 3 \) of \( x^3 \) added onto the constant term, since \( x^3 \equiv 1 \) modulo \( x^3 - 1 \). The requirement \( n \ge 2d+1 \) in @cor-fast-convolution is exactly what rules this out.
:::

### C. Going deeper

::: {#exr-the-fast-fourier-transform-c1}
[C1: Splitting into three]

Let \( n = 3m \) with \( m \ge 1 \), let \( \omega_n = e^{2\pi i/n} \), and for \( s = 0, 1, 2 \) let
\[
\u^{(s)} \coloneqq \W_m\bigl(x_s,\ x_{3+s},\ \dots,\ x_{3(m-1)+s}\bigr) \in \nC^m .
\]

::: {.enumerate options="label=(\alph*)"}
1. Prove that for \( 0 \le q \le 2 \) and \( 0 \le i \le m-1 \),
   \[
   (\W_n\x)_{qm+i} = \sum_{s=0}^{2} \omega_3^{qs}\,\omega_n^{is}\,u^{(s)}_i ,
   \]
   where \( \omega_3 = e^{2\pi i/3} \).
2. Deduce a recursive procedure for \( n = 3^p \), and show that its cost \( C_3 \) satisfies \( C_3(3m) \le 3C_3(m) + 12m \) and hence \( C_3(3^p) \le 4p\,3^p = 4n\log_3 n \).
:::

*Hint for (a): imitate the proof of @thm-fft-factorization, splitting the index \( k \) by its remainder modulo \( 3 \) and using \( \omega_n^3 = \omega_m \) and \( \omega_n^m = \omega_3 \).*
:::

::: {.solution}
(a) Write \( k = 3t + s \) with \( 0 \le s \le 2 \) and \( 0 \le t \le m-1 \), which lists each \( k \in \{0, \dots, n-1\} \) exactly once. Then, using \( \omega_n^{3} = e^{6\pi i/n} = e^{2\pi i/m} = \omega_m \),
\[
(\W_n\x)_j = \sum_{s=0}^{2}\sum_{t=0}^{m-1}\omega_n^{j(3t+s)}x_{3t+s}
= \sum_{s=0}^{2}\omega_n^{js}\sum_{t=0}^{m-1}\omega_m^{jt}x_{3t+s} .
\]
Put \( j = qm + i \). Since \( \omega_m^{m} = 1 \), we get \( \omega_m^{jt} = \omega_m^{it} \), so the inner sum is \( u^{(s)}_i \) by @def-dft-matrix. And \( \omega_n^{m} = e^{2\pi i m/n} = e^{2\pi i/3} = \omega_3 \), so
\[
\omega_n^{js} = \omega_n^{(qm+i)s} = \bigl(\omega_n^{m}\bigr)^{qs}\omega_n^{is} = \omega_3^{qs}\,\omega_n^{is} .
\]
Substituting gives the stated formula.

(b) The procedure is: split \( \x \) by the remainder of the index modulo \( 3 \) (no arithmetic); transform the three parts recursively, getting \( \u^{(0)}, \u^{(1)}, \u^{(2)} \); multiply \( u^{(s)}_i \) by \( \omega_n^{is} \) for \( s = 1, 2 \) and all \( i \); and for each \( i \) apply \( \W_3 \) to the resulting triple, placing the three outputs at positions \( i \), \( m+i \) and \( 2m+i \). Correctness is (a).

Cost. The recursive calls cost \( 3C_3(m) \). The twiddles are \( 2m \) multiplications, the factors for \( s = 0 \) being \( 1 \). Each three-point transform \( (a,b,c) \mapsto (a+b+c,\ a+\omega_3 b + \omega_3^2 c,\ a + \omega_3^2 b + \omega_3 c) \) costs at most \( 4 \) multiplications and \( 6 \) additions, that is \( 10 \) operations, and there are \( m \) of them. Hence \( C_3(3m) \le 3C_3(m) + 2m + 10m = 3C_3(m) + 12m \).

Now put \( D_p = C_3(3^p)/3^p \). The inequality with \( m = 3^{p-1} \) reads \( 3^{p}D_p \le 3\cdot3^{p-1}D_{p-1} + 12\cdot3^{p-1} \), that is \( D_p \le D_{p-1} + 4 \). Since \( D_0 = C_3(1) = 0 \), induction gives \( D_p \le 4p \), so \( C_3(3^p) \le 4p\,3^p \). With \( n = 3^p \), that is \( 4n\log_3 n = O(n\log n) \).
:::

::: {#exr-the-fast-fourier-transform-c2}
[C2: The fourth power of the transform]

Let \( n \ge 1 \) and let \( \R_n \in M_n(\nC) \) be the permutation matrix with \( (\R_n)_{jl} = 1 \) when \( j + l \equiv 0 \pmod n \) and \( 0 \) otherwise, so that \( (\R_n\x)_j = x_{n-j} \) with the subscript read modulo \( n \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \W_n^2 = n\,\R_n \).
2. Deduce that \( \W_n^4 = n^2\I_n \) and \( \F_n^4 = \I_n \), and that every eigenvalue of \( \F_n \) lies in \( \{1, i, -1, -i\} \).
3. Deduce a second proof that \( \W_n^{-1} = \tfrac1n\conj{\W_n} \).
:::
:::

::: {.solution}
(a) By @def-dft-matrix and the definition of the matrix product,
\[
(\W_n^2)_{jl} = \sum_{k=0}^{n-1}\omega_n^{jk}\,\omega_n^{kl} = \sum_{k=0}^{n-1}\bigl(\omega_n^{j+l}\bigr)^{k} .
\]
Put \( z = \omega_n^{j+l} \), so \( z^{n} = 1 \). If \( n \) divides \( j+l \), then \( z = 1 \) and the sum is \( n \). Otherwise \( z \ne 1 \) by @exm-roots-of-unity, and the geometric-series identity \( (z-1)(1 + z + \dots + z^{n-1}) = z^{n}-1 = 0 \) used in the proof of @thm-fourier-matrix-unitary gives \( \sum_k z^{k} = 0 \), since \( z - 1 \ne 0 \). So \( (\W_n^2)_{jl} = n \) exactly when \( j+l \equiv 0 \pmod n \) and \( 0 \) otherwise, which is \( n\R_n \).

(b) The map \( j \mapsto -j \) modulo \( n \) is its own inverse, so \( \R_n^2 = \I_n \) and \( \W_n^4 = (n\R_n)^2 = n^2\I_n \). Since \( \W_n = \sqrt n\,\F_n \), we get \( n^2\F_n^4 = n^2\I_n \), so \( \F_n^4 = \I_n \). Hence \( x^4 - 1 \) annihilates \( \F_n \); if \( \F_n\v = \lambda\v \) with \( \v \ne \0 \), then \( \v = \F_n^4\v = \lambda^4\v \), so \( \lambda^4 = 1 \) and \( \lambda \in \{1, i, -1, -i\} \) by @exm-roots-of-unity.

(c) From (a), \( \W_n\cdot\tfrac1n\W_n\R_n = \R_n\R_n = \I_n \), so \( \W_n^{-1} = \tfrac1n\W_n\R_n \). Its \( (j,l) \)-entry is \( \tfrac1n \) times entry \( (j, n-l) \) of \( \W_n \), namely \( \tfrac1n\omega_n^{j(n-l)} = \tfrac1n\omega_n^{-jl} = \tfrac1n\conj{\omega_n^{jl}} \), using \( \omega_n^{n} = 1 \) and \( \lvert\omega_n\rvert = 1 \). That is the \( (j,l) \)-entry of \( \tfrac1n\conj{\W_n} \).
:::
