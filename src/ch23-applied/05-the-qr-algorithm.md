# The QR Algorithm

Chapter 10 §08 brought a square matrix to upper Hessenberg form with reflections and then stopped, with a warning attached: no finite procedure built from arithmetic and square roots can carry that reduction on to triangular form, because such a procedure would extract the roots of an arbitrary polynomial from its coefficients, and the theorem of Abel and Ruffini forbids it — a theorem this book quotes, there and here, and does not prove. Every eigenvalue method must therefore iterate, and nothing proved below rests on that quotation. The iteration this section develops is the one Chapter 10 named in a single sentence — factor \( \Z = \Q\R \), then replace \( \Z \) by \( \R\Q \) — and we now ask why it works, why it is always started from a Hessenberg matrix, and why it is always run with a shift.

## Factor and multiply back

Section 4 iterated a matrix against a **vector**: the power method drives \( \x^{(k)} = \A\x^{(k-1)} \) towards the dominant eigenvector, one eigenvalue at a time. The whole spectrum at once needs an iteration on **matrices**, and it must be an iteration by similarity, or the spectrum would not survive it. Chapter 10's reflections already gave us a supply of similarities that cost little: \( \A \mapsto \Q^{*}\A\Q \) with \( \Q \) unitary. The question is which \( \Q \) to take.

Here is the answer, and it looks like sleight of hand. Factor \( \A = \Q\R \) and then multiply the two factors back **in the other order**. Since \( \Q^{*}\Q = \I \), the product \( \R\Q \) is \( \Q^{*}(\Q\R)\Q = \Q^{*}\A\Q \), so nothing has been lost; and the reversal shifts weight from the upper triangle into the lower one in a way that, repeated, empties the lower triangle altogether.

*Factor the matrix, then put the factors back the wrong way round, and repeat.*

::: {#def-qr-iteration}
[The QR Iteration]

Let \( \A \in M_n(F) \), where \( F = \nR \) or \( F = \nC \). Set \( \A^{(1)} = \A \), and for \( k \ge 1 \) define
\[
\A^{(k)} = \Q^{(k)}\R^{(k)}, \qquad \A^{(k+1)} = \R^{(k)}\Q^{(k)},
\]
where \( \A^{(k)} = \Q^{(k)}\R^{(k)} \) is **a** factorization with \( \Q^{(k)} \in M_n(F) \) unitary and \( \R^{(k)} \in M_n(F) \) upper triangular. The sequence \( \A^{(1)}, \A^{(2)}, \dots \) is the **unshifted QR iteration** started at \( \A \).
:::

In words: at every step we factor the current matrix, then form the product of its factors in the reversed order, and that product is the next matrix. The superscript in parentheses counts steps, never coordinates.

**Well-definedness.** A factorization exists at every step, for every square matrix and with no hypothesis on its columns, by @thm-qr-householder. It need not be unique: if \( \D \) is diagonal with \( \lvert d_j \rvert = 1 \), then \( (\Q\D)(\D^{*}\R) \) is another one. When \( \A^{(k)} \) is **invertible** the ambiguity is exactly that, and demanding a positive real diagonal in \( \R^{(k)} \) removes it, by @thm-qr-factorization; and if \( \A \) is invertible then so is every \( \A^{(k)} \), being similar to \( \A \). We do not need the normalization for anything below, so the definition leaves the choice open.

::: {#prp-qr-iteration-similar}
[Every Step Is a Unitary Similarity]

In the notation of @def-qr-iteration, \( \A^{(k+1)} = (\Q^{(k)})^{*}\A^{(k)}\Q^{(k)} \) for every \( k \). Consequently all the matrices \( \A^{(k)} \) are unitarily similar to \( \A \), and they share its characteristic polynomial, its eigenvalues with multiplicities, its trace and its determinant.
:::

::: {.proof}
Since \( \Q^{(k)} \) is unitary, \( (\Q^{(k)})^{*}\Q^{(k)} = \I_n \) (@def-unitary-orthogonal), so
\[
(\Q^{(k)})^{*}\A^{(k)}\Q^{(k)} = (\Q^{(k)})^{*}\Q^{(k)}\R^{(k)}\Q^{(k)} = \R^{(k)}\Q^{(k)} = \A^{(k+1)} .
\]
A unitary matrix is invertible with \( \Q^{-1} = \Q^{*} \), so this exhibits \( \A^{(k+1)} \) as similar to \( \A^{(k)} \) (@def-similar-matrices); composing these similarities for \( 1, \dots, k-1 \) makes \( \A^{(k)} \) similar to \( \A^{(1)} = \A \). Similar matrices have the same characteristic polynomial (@thm-charpoly-similarity-invariant), hence the same eigenvalues with multiplicities, and the same trace and determinant. This proves the proposition.
:::

Two examples fix what the iteration does and does not do.

::: {#exm-qr-fixed-points}
[Two matrices the iteration cannot move]

Determine the QR iterates of \( \A = \diag(3, 1) \) and of the rotation \( \B = \begin{pmatrix} 0 & -1 \\ 1 & 0\end{pmatrix} \).
:::

::: {.solution}
For \( \A \): the factorization \( \A = \I_2\A \) has \( \I_2 \) unitary and \( \A \) upper triangular with positive diagonal, so by the uniqueness in @thm-qr-factorization it is *the* factorization. Then \( \A^{(2)} = \A\I_2 = \A \), and the iteration stands still. It has nothing to do: \( \A \) is already triangular and its diagonal already lists the eigenvalues (@thm-diagonal-of-triangular-form).

For \( \B \): here \( \B \) is itself unitary, since its columns \( (0,1) \) and \( (-1,0) \) are orthonormal, so \( \B = \B\,\I_2 \) is a factorization with \( \I_2 \) upper triangular with positive diagonal — again the unique one. So \( \B^{(2)} = \I_2\B = \B \), and the iteration stands still here too. This time it has everything to do: the eigenvalues of \( \B \) are \( \pm i \), and \( \B \) is not triangular. The iteration is stuck.
:::

The second matrix is the section's standing negative example, and the reason it is stuck is visible already: \( \lvert i\rvert = \lvert -i\rvert \). We return to it after the convergence theorem, and repair it with a shift.

::: {.warning}
**Reversing the factors is not a similarity for just any factorization.** The step works because \( \Q \) is unitary, so that \( \Q^{-1} = \Q^{*} \) and \( \R\Q = \Q^{*}\A\Q \). Do the same with an \( \L\U \) factorization and you get \( \U\L = \L^{-1}\A\L \), which is still a similarity — but with \( \L^{-1} \) in place of \( \L^{*} \), and \( \L^{-1} \) can be enormous. That is the older \( \L\R \) iteration, and its instability under rounding is exactly the instability of elimination without pivoting met in Section 2.
:::

## The iteration is the power method in disguise

Nothing said so far suggests that the iterates go anywhere. The identity that explains them is the following, and it is the heart of the section: *the accumulated factors of \( k \) steps are a QR factorization of the \( k \)-th power of \( \A \).* Powers of \( \A \) are what the power method of Section 4 runs on, so the identity says the two methods are the same method, one applied to a vector and the other to a whole basis at once.

Write
\[
\U_k = \Q^{(1)}\Q^{(2)}\cdots\Q^{(k)}, \qquad
\T_k = \R^{(k)}\cdots\R^{(2)}\R^{(1)} .
\]
The first is unitary, as a product of unitary matrices (@prp-orthogonal-group-properties), and the second is upper triangular, as a product of upper triangular matrices.

::: {#thm-qr-is-orthogonal-iteration}
[QR Iterates Factor the Powers]

Let \( \A \in M_n(F) \) and let \( \A^{(k)} \), \( \Q^{(k)} \), \( \R^{(k)} \) be as in @def-qr-iteration. Then for every \( k \ge 1 \),
\[
\A^{(k+1)} = \U_k^{*}\,\A\,\U_k
\qquad\text{and}\qquad
\A^{k} = \U_k\T_k .
\]
In particular \( \U_k\T_k \) is a QR factorization of \( \A^{k} \).
:::

::: {.idea}
Induction on \( k \), with the two statements proved together, because each feeds the other. The similarity statement is @prp-qr-iteration-similar telescoped. For the factorization, the move to find is the one that turns \( \A\U_k \) into something with a \( \Q \) at the front: the similarity statement, read backwards, says \( \A\U_k = \U_k\A^{(k+1)} \), and \( \A^{(k+1)} \) is by definition \( \Q^{(k+1)}\R^{(k+1)} \). One line of bookkeeping then converts \( \A\cdot\A^{k} \) into \( \U_{k+1}\T_{k+1} \).
:::

::: {.proof}
Both statements by induction on \( k \).

For \( k = 1 \): \( \U_1 = \Q^{(1)} \) and \( \T_1 = \R^{(1)} \), so \( \U_1\T_1 = \Q^{(1)}\R^{(1)} = \A^{(1)} = \A \), and \( \U_1^{*}\A\U_1 = \A^{(2)} \) by @prp-qr-iteration-similar.

Let \( k \ge 1 \) and suppose both statements hold for \( k \). By @prp-qr-iteration-similar applied at step \( k+1 \) and the inductive hypothesis,
\[
\A^{(k+2)} = (\Q^{(k+1)})^{*}\A^{(k+1)}\Q^{(k+1)}
= (\Q^{(k+1)})^{*}\U_k^{*}\A\,\U_k\Q^{(k+1)}
= \U_{k+1}^{*}\A\,\U_{k+1},
\]
where the last equality uses \( \U_{k+1} = \U_k\Q^{(k+1)} \) and \( (\X\Y)^{*} = \Y^{*}\X^{*} \). That is the first statement for \( k+1 \).

For the second, multiply the inductive similarity \( \A^{(k+1)} = \U_k^{*}\A\U_k \) on the left by \( \U_k \), which is legitimate because \( \U_k\U_k^{*} = \I_n \):
\[
\A\,\U_k = \U_k\A^{(k+1)} = \U_k\Q^{(k+1)}\R^{(k+1)} = \U_{k+1}\R^{(k+1)} .
\]
Hence, using the inductive factorization \( \A^{k} = \U_k\T_k \),
\[
\A^{k+1} = \A\,(\U_k\T_k) = (\A\,\U_k)\T_k = \U_{k+1}\R^{(k+1)}\T_k = \U_{k+1}\T_{k+1},
\]
since \( \T_{k+1} = \R^{(k+1)}\T_k \) by definition. As \( \U_{k+1} \) is unitary and \( \T_{k+1} \) upper triangular, this is a QR factorization of \( \A^{k+1} \), and the induction is complete.
:::

The consequence to keep is about the **first column**. Comparing first columns in \( \A^{k} = \U_k\T_k \) and writing \( \tau_k = (\T_k)_{11} \), we get
\[
\A^{k}\e_1 = \U_k\T_k\e_1 = \tau_k\,\U_k\e_1 ,
\]{#eq-qr-first-column}
because the first column of an upper triangular matrix is \( \tau_k\e_1 \). So whenever \( \tau_k \neq 0 \), which the Quick check just below records for invertible \( \A \), the first column of \( \U_k \) is the normalized vector \( \A^{k}\e_1/\norm{\A^{k}\e_1} \), up to a scalar of modulus one — which is precisely the \( k \)-th iterate of the power method (@thm-power-method) started at \( \e_1 \). The QR algorithm runs the power method in its first column, and, as the next theorem shows, that alone forces the first column of \( \A^{(k+1)} \) to converge.

::: {.check}
Why is \( \tau_k \neq 0 \) when \( \A \) is invertible?
:::

::: {.solution}
Each \( \A^{(j)} \) is similar to \( \A \) (@prp-qr-iteration-similar), hence invertible, and \( \R^{(j)} = (\Q^{(j)})^{*}\A^{(j)} \) is then invertible as a product of invertible matrices. So \( \T_k \) is invertible, being a product of invertible matrices; an upper triangular matrix is invertible exactly when its diagonal entries are all non-zero (@lem-triangular-invertible), so \( \tau_k = (\T_k)_{11} \neq 0 \).
:::

## What converges, and how fast

::: {#thm-qr-convergence}
[Convergence of the First Column]

Let \( \A \in M_n(\nC) \) be invertible and diagonalizable, say \( \A = \X\vLambda\X^{-1} \) with \( \vLambda = \diag(\lambda_1, \dots, \lambda_n) \) and with \( \v_1, \dots, \v_n \) the columns of \( \X \). Assume a **single dominant eigenvalue**,
\[
\lvert\lambda_1\rvert > \lvert\lambda_2\rvert \ge \dots \ge \lvert\lambda_n\rvert > 0 ,
\]
and write \( \e_1 = c_1\v_1 + \dots + c_n\v_n \), assuming \( c_1 \neq 0 \). Put \( t = \lvert\lambda_2/\lambda_1\rvert < 1 \). Then there is a constant \( C \), depending on \( \A \) and \( \X \) but not on \( k \), such that the unshifted QR iterates satisfy
\[
\norm{\A^{(k+1)}\e_1 - \lambda_1\e_1}_2 \le C\,t^{k} \qquad (k \ge 1) .
\]
In particular \( a^{(k)}_{11} \to \lambda_1 \) and \( a^{(k)}_{i1} \to 0 \) for every \( i \ge 2 \), each at the rate \( t^{k} \). For \( n = 2 \) this says that the iterates converge to upper triangular form, with \( a^{(k)}_{11} \to \lambda_1 \) and \( a^{(k)}_{22} \to \lambda_2 \).
:::

::: {.idea}
By @eq-qr-first-column the first column \( \u_1 \) of \( \U_k \) is the power-method iterate, so it is close to the dominant eigenvector, and the vector \( \A\u_1 - \lambda_1\u_1 \) is small. Now read \( \A^{(k+1)} = \U_k^{*}\A\U_k \) column by column: its first column is \( \U_k^{*}\A\u_1 \), and subtracting \( \lambda_1\e_1 = \U_k^{*}(\lambda_1\u_1) \) leaves \( \U_k^{*}(\A\u_1 - \lambda_1\u_1) \). A unitary matrix does not change lengths, so the whole error in the first column *equals* the length of that small vector. Nothing else is needed.
:::

::: {.proof}
Write \( \u_1 = \U_k\e_1 \) for the first column of \( \U_k \), suppressing \( k \) from the notation.

**Step 1: the error in the first column is a residual.** Since \( \U_k \) is unitary and \( \A^{(k+1)} = \U_k^{*}\A\U_k \) by @thm-qr-is-orthogonal-iteration,
\[
\A^{(k+1)}\e_1 - \lambda_1\e_1 = \U_k^{*}\A\u_1 - \lambda_1\U_k^{*}\u_1 = \U_k^{*}\bigl(\A\u_1 - \lambda_1\u_1\bigr),
\]
using \( \u_1 = \U_k\e_1 \) twice. A unitary matrix preserves the Euclidean norm (@thm-isometry-characterizations), so
\[
\norm{\A^{(k+1)}\e_1 - \lambda_1\e_1}_2 = \norm{\A\u_1 - \lambda_1\u_1}_2 .
\tag{$\ast$}
\]

**Step 2: \( \u_1 \) is a power-method iterate.** By @eq-qr-first-column, \( \A^{k}\e_1 = \tau_k\u_1 \) with \( \tau_k \neq 0 \), as the Quick check above records. Since \( \A\v_i = \lambda_i\v_i \),
\[
\A^{k}\e_1 = \sum_{i=1}^{n} c_i\lambda_i^{k}\v_i = c_1\lambda_1^{k}\bigl(\v_1 + \z_k\bigr),
\qquad
\z_k = \sum_{i \ge 2}\frac{c_i}{c_1}\Bigl(\frac{\lambda_i}{\lambda_1}\Bigr)^{k}\v_i ,
\]
which is legitimate because \( c_1 \neq 0 \) and \( \lambda_1 \neq 0 \). Every ratio obeys \( \lvert\lambda_i/\lambda_1\rvert \le t \), so
\[
\norm{\z_k}_2 \le M t^{k}, \qquad M = \sum_{i\ge2}\frac{\lvert c_i\rvert}{\lvert c_1\rvert}\norm{\v_i}_2 ,
\]
by the triangle inequality (@cor-triangle-inequality). Put \( \y_k = \v_1 + \z_k \). Then \( \u_1 = \A^{k}\e_1/\tau_k = \omega_k\,\y_k/\norm{\y_k}_2 \) for the scalar \( \omega_k = c_1\lambda_1^{k}\norm{\y_k}_2/\tau_k \), and \( \lvert\omega_k\rvert = 1 \) because \( \norm{\u_1}_2 = 1 \).

**Step 3: the residual is small.** Since \( \A\v_1 = \lambda_1\v_1 \), the vector \( \v_1 \) drops out of \( (\A - \lambda_1\I)\y_k \), leaving
\[
\begin{aligned}
\A\u_1 - \lambda_1\u_1
&= \omega_k\,\frac{(\A - \lambda_1\I)\z_k}{\norm{\y_k}_2},\\
\text{so}\qquad
\norm{\A\u_1 - \lambda_1\u_1}_2
&\le \frac{\bigl(\norm{\A}_2 + \lvert\lambda_1\rvert\bigr)M\,t^{k}}{\norm{\y_k}_2} .
\end{aligned}
\]
Choose \( k_0 \) with \( Mt^{k_0} \le \tfrac12\norm{\v_1}_2 \), possible because \( t < 1 \). For \( k \ge k_0 \) the triangle inequality gives \( \norm{\y_k}_2 \ge \norm{\v_1}_2 - Mt^{k} \ge \tfrac12\norm{\v_1}_2 > 0 \), whence
\[
\norm{\A\u_1 - \lambda_1\u_1}_2 \le C_1 t^{k},
\qquad
C_1 = \frac{2\bigl(\norm{\A}_2 + \lvert\lambda_1\rvert\bigr)M}{\norm{\v_1}_2} .
\]
For the finitely many \( k < k_0 \) the crude bound \( \norm{\A\u_1 - \lambda_1\u_1}_2 \le \norm{\A}_2 + \lvert\lambda_1\rvert \) holds, since \( \norm{\u_1}_2 = 1 \). So the displayed estimate holds for all \( k \ge 1 \) with
\[
C = \max\Bigl\{\,C_1,\ \bigl(\norm{\A}_2 + \lvert\lambda_1\rvert\bigr)t^{-k_0}\,\Bigr\} ,
\]
and combining with \( (\ast) \) proves the main estimate. The entrywise statements follow because each coordinate of a vector is at most its Euclidean norm.

For \( n = 2 \), the estimate forces \( a^{(k)}_{21} \to 0 \) and \( a^{(k)}_{11} \to \lambda_1 \); and \( a^{(k)}_{22} = \tr\A^{(k)} - a^{(k)}_{11} = \lambda_1 + \lambda_2 - a^{(k)}_{11} \to \lambda_2 \), the trace being preserved by @prp-qr-iteration-similar. This proves the theorem.
:::

**What is proved here, and what is not.** The theorem above settles the first column, for every \( n \), and with it the whole \( 2 \times 2 \) case. The general statement is this: if \( \A \) is diagonalizable with \( \lvert\lambda_1\rvert > \lvert\lambda_2\rvert > \dots > \lvert\lambda_n\rvert > 0 \), **and** if \( \X^{-1} \) admits an \( \L\U \) factorization without row swaps (@thm-lu-exists-without-swaps), then the whole of \( \A^{(k)} \) below the diagonal tends to zero, with
\[
a^{(k)}_{i+1,i} = O\bigl(\lvert\lambda_{i+1}/\lambda_i\rvert^{k}\bigr)
\quad\text{and}\quad
a^{(k)}_{ii} \to \lambda_i \quad (1 \le i \le n).
\]
This is the classical convergence theorem of the algorithm, due to Rutishauser, Francis and Kublanovskaya; **it is not proved here.** The proof runs through the factorization \( \A^{k} = \X\vLambda^{k}\L\U \) of @thm-qr-is-orthogonal-iteration's identity, the observation that \( \vLambda^{k}\L\vLambda^{-k} \to \I \), and a continuity argument for the QR factorization that this book has not developed. Nothing in this section or later depends on it: the Hessenberg and shifting results below are proved outright, and the worked example at the end exhibits the rates rather than assuming them. The extra hypothesis on \( \X^{-1} \) is not cosmetic, and the strict ordering of the moduli is not either — the next example shows what happens without it.

::: {#exm-rotation-stuck}
[The unshifted algorithm on a rotation]

Let \( \B = \begin{pmatrix} 0 & -1 \\ 1 & 0\end{pmatrix} \). Explain why no unshifted QR iteration can bring \( \B \) closer to triangular form, and say which hypothesis of @thm-qr-convergence fails.
:::

::: {.solution}
By @exm-qr-fixed-points, \( \B^{(k)} = \B \) for every \( k \): the iteration is stationary, and \( \B \) is as far from triangular as a \( 2 \times 2 \) matrix can be, with \( b_{21} = 1 \). The eigenvalues are \( \pm i \), so \( \lvert\lambda_1\rvert = \lvert\lambda_2\rvert = 1 \) and the hypothesis \( \lvert\lambda_1\rvert > \lvert\lambda_2\rvert \) fails. The failure is not an artifact of the proof. Over \( \nR \) the matrix is orthogonally similar to no real triangular matrix at all, since a real triangular matrix has real eigenvalues; and over \( \nC \) the power method has nothing to converge to, because \( \B^{k}\e_1 \) simply rotates around the plane forever (@thm-power-method).
:::

::: {.warning}
**Convergence is to triangular form, not to diagonal form.** Even when the iterates do converge, the strictly upper triangular part generally does not: only the entries **below** the diagonal die out. What is more, in the convergence theorem quoted above — the one this section does not prove — the order in which the eigenvalues appear on the diagonal is decided by the moduli, largest first, so that a run it covers reveals \( \lambda_1 \) in the top-left corner and \( \lambda_n \) in the bottom-right. With shifts, which is how the algorithm is actually run, even that ordering goes away.
:::

## Hessenberg first

As written, one step costs a QR factorization of a full \( n \times n \) matrix and a matrix product: that is \( O(n^3) \) flops, in the counting convention of @prp-lu-cost, and the count really does grow like \( n^3 \), since the product alone touches \( n^2 \) entries with \( n \) terms each. The iteration needs many steps, and no amount of cleverness about the steps rescues a method that spends \( n^3 \) operations on each of them.

The remedy is Chapter 10's. Reduce \( \A \) once to upper Hessenberg form by @thm-hessenberg-form, at a cost of \( O(n^3) \) paid a single time, and then iterate. This pays off only if the pattern survives the step, which is the content of the next proposition — and it is the sentence Chapter 10 §08 closed on: "Chapter 23 develops that iteration and explains why every implementation starts with the reduction proved here."

::: {#prp-hessenberg-preserved}
[A QR Step Preserves Hessenberg Form]

Let \( \Z \in M_n(\nR) \) be upper Hessenberg, \( n \ge 2 \). Then \( \Z \) has a factorization \( \Z = \Q\R \) with \( \Q \) orthogonal and \( \R \) upper triangular in which \( \Q \) is a product of \( n-1 \) Givens rotations and is **itself upper Hessenberg**; and for this factorization \( \R\Q \) is again upper Hessenberg. Producing \( \R \) and then \( \R\Q \) costs about \( 6n^2 \) flops.
:::

::: {.idea}
A Hessenberg matrix has only \( n-1 \) entries in the way of triangularity, one per column, and @def-givens-rotation removes one entry per rotation. So the natural factorization to use is the rotation one, not the reflection one — this is the case Chapter 10 §08 flagged, where "the count reverses". Then two bookkeeping facts finish it: the accumulated product of the rotations is Hessenberg, and upper triangular times upper Hessenberg is upper Hessenberg.
:::

::: {.proof}
For \( 1 \le i \le n-1 \) let \( \G_i = \G(i, i+1; c_i, s_i) \) be a Givens rotation in the coordinates \( i, i+1 \) (@def-givens-rotation). Working left to right, choose \( \G_i \) to annihilate the entry in position \( (i+1, i) \) of the matrix produced so far: if that matrix has entries \( a \) in position \( (i,i) \) and \( b \) in position \( (i+1, i) \) with \( (a, b) \neq (0,0) \), take \( c_i = a/r \) and \( s_i = b/r \) with \( r = \sqrt{a^2 + b^2} \), as in Chapter 10 §08; if \( (a, b) = (0, 0) \), take \( \G_i = \I_n \). This is the only entry below the diagonal in column \( i \): the entries in rows \( i+2, \dots, n \) of that column were zero in \( \Z \), because \( \Z \) is upper Hessenberg, and the earlier rotations \( \G_1, \dots, \G_{i-1} \) touch only rows \( 1, \dots, i \). Left multiplication by \( \G_i \) recombines rows \( i \) and \( i+1 \) only, so it cannot disturb the zeros already created: in a column \( j \le i-1 \) both of the rows being combined are already zero, since \( i \ge j+1 \). Hence
\[
\R = \G_{n-1}\cdots\G_1\Z
\]
is upper triangular, and \( \Z = \Q\R \) with \( \Q = \G_1\tp\G_2\tp\cdots\G_{n-1}\tp \), orthogonal as a product of orthogonal matrices.

::: {.claim}
\( \P_m = \G_1\tp\cdots\G_m\tp \) is upper Hessenberg for \( 1 \le m \le n-1 \), and its columns \( m+2, \dots, n \) are \( \e_{m+2}, \dots, \e_n \).
:::

::: {.proof}
Induction on \( m \). Each \( \G_i\tp \) fixes \( \e_j \) for \( j \notin \{i, i+1\} \), so \( \P_m\e_j = \e_j \) whenever \( j > m+1 \), which is the second assertion. For \( m = 1 \), \( \P_1 = \G_1\tp \) differs from \( \I_n \) only in rows and columns \( 1, 2 \), so its only non-zero entry below the diagonal is in position \( (2,1) \), and it is upper Hessenberg. Let \( m \ge 2 \) and suppose the claim holds for \( m-1 \). Right multiplication by \( \G_m\tp \) changes only columns \( m \) and \( m+1 \), replacing them by the two combinations
\[
c_m\,\P_{m-1}\e_m + s_m\,\P_{m-1}\e_{m+1}
\quad\text{and}\quad
-s_m\,\P_{m-1}\e_m + c_m\,\P_{m-1}\e_{m+1} .
\]
By the inductive hypothesis \( \P_{m-1}\e_m \) has zero entries in rows \( m+2, \dots, n \), being column \( m \) of an upper Hessenberg matrix, and \( \P_{m-1}\e_{m+1} = \e_{m+1} \) since \( m+1 > (m-1)+1 \). So both combinations vanish in rows \( m+2, \dots, n \). Column \( m \) of \( \P_m \) therefore vanishes below row \( m+1 \), as an upper Hessenberg matrix requires; and column \( m+1 \) vanishes below row \( m+1 \), which is more than required. All other columns are unchanged, so \( \P_m \) is upper Hessenberg.
:::

By the Claim, \( \Q = \P_{n-1} \) is upper Hessenberg. Finally,
\[
(\R\Q)_{pq} = \sum_{k} r_{pk}q_{kq}
\]
has a non-zero term only when \( k \ge p \), because \( \R \) is upper triangular, and \( k \le q+1 \), because \( \Q \) is upper Hessenberg; together these force \( p \le q+1 \). So \( \R\Q \) is upper Hessenberg.

*Cost.* Rotation \( \G_i \) alters rows \( i, i+1 \) in columns \( i, \dots, n \) only, since in the earlier columns both of those rows are already zero: that is \( n-i+1 \) pairs of entries, each pair replaced by two combinations of two terms, so \( 6(n-i+1) \) flops. Summing over \( i = 1, \dots, n-1 \) gives \( 3n^2 + O(n) \). Forming \( \R\Q = \R\,\G_1\tp\cdots\G_{n-1}\tp \) applies \( \G_i\tp \) on the right to columns \( i, i+1 \) of the matrix built so far, and the same induction as in the Claim shows that those two columns vanish below row \( i+1 \); so \( 6(i+1) \) flops suffice, and summing gives \( 3n^2 + O(n) \) again. The total is \( 6n^2 + O(n) \), which proves the proposition.
:::

So the reduction is done once, for \( O(n^3) \), and every subsequent step costs \( O(n^2) \) — a saving of a factor of \( n \) on each of the many steps. That is the whole reason every implementation begins with @thm-hessenberg-form.

::: {.remark}
The proposition is stated over \( \nR \) because @def-givens-rotation is. Over \( \nC \) one uses the complex rotations described in Chapter 10 §08 and the argument is unchanged. The conclusion also does not depend on which QR factorization is used, as long as \( \Z \) is invertible: two factorizations then differ by \( \Q \mapsto \Q\D \) and \( \R \mapsto \D^{*}\R \) with \( \D \) unitary diagonal, and \( (\D^{*}\R)(\Q\D) = \D^{*}(\R\Q)\D \) has exactly the same pattern of zeros as \( \R\Q \). Invertibility is doing work there: for \( \Z = \e_1\e_3\tp \in M_3(\nR) \), which is upper Hessenberg and singular, the reversal permutation \( \Q \) (with \( \Q\e_j = \e_{4-j} \)) and \( \R = \e_3\e_3\tp \) give an orthogonal \( \Q \), an upper triangular \( \R \) and \( \Q\R = \Z \), while \( \R\Q = \e_3\e_1\tp \) has a non-zero \( (3,1) \) entry and is not upper Hessenberg.
:::

::: {.check}
A symmetric matrix is upper Hessenberg exactly when it is tridiagonal. What does @prp-hessenberg-preserved then say about a QR step applied to a symmetric tridiagonal matrix?
:::

::: {.solution}
That the step returns a symmetric tridiagonal matrix. Symmetry survives because \( \R\Q = \Q\tp\Z\Q \) is a congruence by an orthogonal matrix as well as a similarity, so \( (\Q\tp\Z\Q)\tp = \Q\tp\Z\tp\Q = \Q\tp\Z\Q \); and Hessenberg form survives by the proposition. A symmetric Hessenberg matrix has \( z_{ij} = 0 \) whenever \( i > j+1 \), hence also whenever \( j > i+1 \), which is tridiagonality. The cost then drops further, to \( O(n) \) per step.
:::

## Shifts

The rate \( \lvert\lambda_{i+1}/\lambda_i\rvert \) is a property of \( \A \), and we cannot change \( \A \). We can change the matrix we iterate on. For any \( \mu \in F \), the matrix \( \A - \mu\I \) has eigenvalues \( \lambda_i - \mu \), so its ratios of moduli are \( \lvert\lambda_{i+1} - \mu\rvert/\lvert\lambda_i - \mu\rvert \) — and a \( \mu \) close to \( \lambda_n \) makes the last of these tiny. This is the same observation that turned the power method into inverse iteration in Section 4, where the shift \( \mu \) was used to make \( (\A - \mu\I)^{-1} \) have a huge dominant eigenvalue (@thm-inverse-iteration).

The **shifted QR step** is
\[
\A^{(k)} - \mu_k\I = \Q^{(k)}\R^{(k)}, \qquad
\A^{(k+1)} = \R^{(k)}\Q^{(k)} + \mu_k\I ,
\]
and it is still a unitary similarity: \( \R^{(k)}\Q^{(k)} = (\Q^{(k)})^{*}(\A^{(k)} - \mu_k\I)\Q^{(k)} \), so adding \( \mu_k\I \) back gives \( \A^{(k+1)} = (\Q^{(k)})^{*}\A^{(k)}\Q^{(k)} \) exactly as in @prp-qr-iteration-similar. The shift may be changed at every step, which is why the ratio can be driven down as the information improves. And since \( \A^{(k)} - \mu_k\I \) is Hessenberg whenever \( \A^{(k)} \) is, @prp-hessenberg-preserved applies to the shifted step: as it stands for a real \( \mu_k \), and in the complex form recorded in the Remark after it for a \( \mu_k \) off the real line, which the second of the two shifts below produces.

Two shifts are standard. The **Rayleigh shift** takes \( \mu_k = a^{(k)}_{nn} \), the trailing diagonal entry; when \( \A \) is Hermitian this is the Rayleigh quotient \( R_{\A^{(k)}}(\e_n) \) of @def-rayleigh-quotient, hence a good eigenvalue estimate as soon as \( \e_n \) is nearly an eigenvector. The **Wilkinson shift** takes \( \mu_k \) to be the eigenvalue of the trailing \( 2 \times 2 \) block of \( \A^{(k)} \) nearer to \( a^{(k)}_{nn} \); it costs one quadratic formula and, unlike the Rayleigh shift, it can leave the real line, which is what lets it break the deadlock of a rotation.

The extreme case says exactly why shifting works.

::: {#prp-exact-shift-deflates}
[An Exact Shift Deflates in One Step]

Let \( \Z \in M_n(F) \) be upper Hessenberg, \( n \ge 2 \), with all its subdiagonal entries \( z_{i+1,i} \) **non-zero** — such a matrix is called **unreduced**, the word @lem-tridiagonal-eigenvector-ends used for the tridiagonal case. Let \( \mu \in F \) be an eigenvalue of \( \Z \). Let \( \Z - \mu\I = \Q\R \) with \( \Q \) unitary and \( \R \) upper triangular, and put \( \Z' = \R\Q + \mu\I \). Then the last row of \( \R \) is zero, and the last row of \( \Z' \) is \( \mu\,\e_n\tp \). In particular \( z'_{n,n-1} = 0 \) and \( z'_{nn} = \mu \).
:::

::: {.idea}
An unreduced Hessenberg matrix cannot lose more than one dimension of rank: its first \( n-1 \) columns are independent whatever the matrix does, because the subdiagonal alone makes them so. Shifting by an eigenvalue makes the matrix singular, so the one missing dimension must be the last one, and in a QR factorization "the last dimension is missing" reads as a zero last row of \( \R \).
:::

::: {.proof}
Write \( \B = \Z - \mu\I \), again upper Hessenberg with the same non-zero subdiagonal entries.

First, the columns \( \b_1, \dots, \b_{n-1} \) of \( \B \) are linearly independent. Delete the first row: what remains is the \( (n-1) \times (n-1) \) matrix with entries \( b_{i+1,j} \) for \( 1 \le i, j \le n-1 \), which is **lower** triangular, since \( b_{i+1,j} = 0 \) for \( i + 1 > j + 1 \), that is for \( i > j \); and its diagonal entries \( b_{j+1,j} \) are non-zero. A triangular matrix with non-zero diagonal is invertible (@lem-triangular-invertible), so those \( n-1 \) truncated columns are independent, and the full columns are independent a fortiori.

Second, \( \rank\B = n-1 \): it is at least \( n-1 \) by the previous paragraph and at most \( n - 1 \) because \( \B \) is singular, \( \mu \) being an eigenvalue of \( \Z \).

Now \( \B = \Q\R \) with \( \Q \) invertible, so \( \rank\R = \rank\B = n-1 \) and the columns \( \R\e_1, \dots, \R\e_{n-1} \) are independent, being \( \Q^{*}\b_1, \dots, \Q^{*}\b_{n-1} \). Since \( \R \) is upper triangular, its last row has the single possibly non-zero entry \( r_{nn} \); if \( r_{nn} \neq 0 \), then \( \R \) would be invertible (@lem-triangular-invertible applied after noting that independence of the first \( n-1 \) columns forces \( r_{11}, \dots, r_{n-1,n-1} \neq 0 \)), contradicting \( \rank\R = n-1 \). Hence \( r_{nn} = 0 \) and the last row of \( \R \) is zero.

A matrix with zero last row keeps it under multiplication on the right: \( (\R\Q)_{nj} = \sum_k r_{nk}q_{kj} = 0 \). So the last row of \( \R\Q \) is zero and the last row of \( \Z' = \R\Q + \mu\I \) is \( \mu\,\e_n\tp \), as claimed.
:::

The proposition is the ideal case, and it explains the practice: the closer \( \mu_k \) is to an eigenvalue, the smaller \( z'_{n,n-1} \) is observed to become, and the algorithm watches that one entry. When it falls below a tolerance it is set to zero, the matrix splits into a smaller Hessenberg block and a known eigenvalue, and the iteration restarts on the block. This is **deflation**, and with it the algorithm is observed to finish after \( O(n) \) steps in total rather than converging forever.

**Two claims in that paragraph are descriptions of observed behavior, not theorems, and this book proves neither**: that a nearer shift always gives a smaller subdiagonal entry, and that the shifted algorithm terminates after \( O(n) \) steps. Nothing in this section or later depends on them. What is proved is the exact case, @prp-exact-shift-deflates, and the example below exhibits it.

::: {#exm-shift-repairs-rotation}
[The shift repairs the rotation, and deflates a symmetric example]

(a) Apply one shifted QR step with \( \mu = i \) to \( \B = \begin{pmatrix} 0 & -1 \\ 1 & 0\end{pmatrix} \).
(b) Apply one shifted QR step with \( \mu = 2 \) to the symmetric tridiagonal matrix \( \A \) with diagonal \( (2,2,2) \) and off-diagonal entries \( 1 \).
:::

::: {.solution}
(a) Here \( \mu = i \) is an eigenvalue, so @prp-exact-shift-deflates predicts an exact deflation. Indeed
\[
\B - i\I = \begin{pmatrix} -i & -1 \\ 1 & -i\end{pmatrix},
\]
whose second column is \( -i \) times the first, so the matrix has rank \( 1 \). Its first column has norm \( \sqrt2 \), so take \( \q_1 = \tfrac{1}{\sqrt2}(-i, 1) \) and \( \q_2 = \tfrac{1}{\sqrt2}(1, -i) \), which is a unit vector orthogonal to \( \q_1 \) since \( \conj{(-i)}\cdot 1 + \conj{1}\cdot(-i) = i - i = 0 \). With \( \Q = (\q_1 \mid \q_2) \) one computes \( \R = \Q^{*}(\B - i\I) \), which is
\[
\R = \begin{pmatrix} \sqrt2 & -i\sqrt2 \\ 0 & 0 \end{pmatrix},
\]
with zero last row as predicted. Then \( \R\Q = \diag(-2i, 0) \), and
\[
\B' = \R\Q + i\I = \diag(-i,\, i) .
\]
One step, and the eigenvalues are on the diagonal. The unshifted iteration would have run forever.

(b) The matrix is
\[
\A = \begin{pmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2\end{pmatrix},
\qquad
\A - 2\I = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0\end{pmatrix},
\]
and \( 2 \) is an eigenvalue of \( \A \), since \( (\A - 2\I)(1,0,-1) = \0 \). Two Givens rotations triangularize \( \A - 2\I \), as in the proof of @prp-hessenberg-preserved. The first uses the entries \( 0 \) and \( 1 \) in positions \( (1,1) \) and \( (2,1) \), so \( r = 1 \), \( c_1 = 0 \), \( s_1 = 1 \), and \( \G_1 \) exchanges rows \( 1 \) and \( 2 \) with a sign, producing rows \( (1,0,1) \), \( (0,-1,0) \), \( (0,1,0) \). The second uses the entries \( -1 \) and \( 1 \) now in positions \( (2,2) \) and \( (3,2) \), so \( r = \sqrt2 \), \( c_2 = -1/\sqrt2 \), \( s_2 = 1/\sqrt2 \), and it turns those two rows into \( (0, \sqrt2, 0) \) and \( \0 \). Hence
\[
\R = \begin{pmatrix} 1 & 0 & 1 \\ 0 & \sqrt2 & 0 \\ 0 & 0 & 0\end{pmatrix},
\qquad
\Q = \G_1\tp\G_2\tp = \begin{pmatrix} 0 & \tfrac{1}{\sqrt2} & \tfrac{1}{\sqrt2} \\ 1 & 0 & 0 \\ 0 & \tfrac{1}{\sqrt2} & -\tfrac{1}{\sqrt2}\end{pmatrix},
\]
with the last row of \( \R \) zero, as @prp-exact-shift-deflates predicts. One checks \( \Q\R = \A - 2\I \) column by column. Multiplying back and restoring the shift,
\[
\A' = \R\Q + 2\I = \begin{pmatrix} 2 & \sqrt2 & 0 \\ \sqrt2 & 2 & 0 \\ 0 & 0 & 2 \end{pmatrix} .
\]
The last row and column have split off, carrying the eigenvalue \( 2 \), and the remaining \( 2 \times 2 \) block has eigenvalues \( 2 \pm \sqrt2 \) — the other two eigenvalues of \( \A \). One shifted step, and the problem is finished.
:::

## Three unshifted steps, watched

::: {#exm-qr-three-steps}
[The subdiagonal shrinking at the predicted rate]

Run the unshifted QR iteration on the symmetric tridiagonal matrix
\[
\A = \begin{pmatrix} 2 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 2\end{pmatrix},
\]
whose eigenvalues are \( 2 + \sqrt2 \), \( 2 \) and \( 2 - \sqrt2 \). Carry out the first step exactly, and tabulate three steps.
:::

::: {.solution}
*Step one, by hand.* Apply @thm-gram-schmidt to the columns \( \a_1 = (2,1,0) \), \( \a_2 = (1,2,1) \), \( \a_3 = (0,1,2) \).

From \( \a_1 \): \( r_{11} = \norm{\a_1} = \sqrt5 \) and \( \q_1 = \tfrac{1}{\sqrt5}(2,1,0) \).

From \( \a_2 \): \( r_{12} = \inner{\a_2}{\q_1} = 4/\sqrt5 \), and
\[
\w_2 = \a_2 - \tfrac45(2,1,0) = \tfrac15(-3, 6, 5),
\qquad
r_{22} = \norm{\w_2} = \sqrt{14/5},
\]
since \( 9 + 36 + 25 = 70 \) and \( \sqrt{70}/5 = \sqrt{14/5} \); so \( \q_2 = \tfrac{1}{\sqrt{70}}(-3,6,5) \).

From \( \a_3 \): \( r_{13} = 1/\sqrt5 \) and \( r_{23} = 16/\sqrt{70} \), and
\[
\w_3 = \a_3 - \tfrac15(2,1,0) - \tfrac{16}{70}(-3,6,5) = \tfrac27(1,-2,3),
\qquad
r_{33} = \tfrac{2\sqrt{14}}{7} ,
\]
so \( \q_3 = \tfrac{1}{\sqrt{14}}(1,-2,3) \). Now \( \A^{(2)} = \R\Q \). Its \( (1,1) \) entry is the first row of \( \R \) against the first column of \( \Q \), namely
\[
\sqrt5\cdot\tfrac{2}{\sqrt5} + \tfrac{4}{\sqrt5}\cdot\tfrac{1}{\sqrt5} + \tfrac{1}{\sqrt5}\cdot 0 = 2 + \tfrac45 = \tfrac{14}{5},
\]
and its \( (2,1) \) entry is \( \sqrt{14/5}\cdot\tfrac{1}{\sqrt5} + \tfrac{16}{\sqrt{70}}\cdot 0 = \sqrt{14}/5 \). Continuing,
\[
\A^{(2)} = \begin{pmatrix}
\tfrac{14}{5} & \tfrac{\sqrt{14}}{5} & 0 \\[3pt]
\tfrac{\sqrt{14}}{5} & \tfrac{82}{35} & \tfrac{2\sqrt5}{7} \\[3pt]
0 & \tfrac{2\sqrt5}{7} & \tfrac{6}{7}
\end{pmatrix}.
\]
Three checks: the matrix is symmetric and tridiagonal, as the Quick check after @prp-hessenberg-preserved predicted; its trace is \( \tfrac{14}{5} + \tfrac{82}{35} + \tfrac67 = \tfrac{98 + 82 + 30}{35} = 6 = \tr\A \); and the entry \( (3,1) \) is zero, not merely small.

*Three steps, to eight places.* The diagonal entries and the two subdiagonal entries run as follows.

| \( k \) | \( a^{(k)}_{11} \) | \( a^{(k)}_{22} \) | \( a^{(k)}_{33} \) | \( \lvert a^{(k)}_{21}\rvert \) | \( \lvert a^{(k)}_{32}\rvert \) |
|---|---|---|---|---|---|
| 1 | 2.00000000 | 2.00000000 | 2.00000000 | 1.000000 | 1.000000 |
| 2 | 2.80000000 | 2.34285714 | 0.85714286 | 0.748331 | 0.638877 |
| 3 | 3.14285714 | 2.24844720 | 0.60869565 | 0.559397 | 0.187848 |
| 4 | 3.30841121 | 2.10394692 | 0.58764187 | 0.372193 | 0.052177 |

The three diagonal entries are heading for \( 2+\sqrt2 = 3.41421356 \), \( 2 \) and \( 2-\sqrt2 = 0.58578644 \), largest modulus first — the order the convergence theorem quoted above predicts, exhibited here rather than proved. The two subdiagonal entries shrink by factors
\[
0.748, \ 0.748, \ 0.665, \dots
\qquad\text{and}\qquad
0.639, \ 0.294, \ 0.278, \dots
\]
The predicted asymptotic factors are \( \lvert\lambda_2/\lambda_1\rvert = 2/(2+\sqrt2) = 0.585786 \) and \( \lvert\lambda_3/\lambda_2\rvert = (2-\sqrt2)/2 = 0.292893 \). The second entry has already settled onto its rate; the first is still approaching it, and by step \( 10 \) its factor is \( 0.5859 \). Convergence is linear, and slow: each step buys about a quarter of a decimal digit in the \( (2,1) \) entry. That is the cost of not shifting.
:::

## Exercises

### A. Check your understanding

:::: {#exr-the-qr-algorithm-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Write down one step of the unshifted QR iteration, and one step of the shifted one, and prove in one line each that both are similarities.
2. State @thm-qr-is-orthogonal-iteration, and say in one sentence what it has to do with the power method.
3. True or false: the QR iterates of a matrix always converge to an upper triangular matrix. Justify your answer.
4. Why is the iteration run on an upper Hessenberg matrix rather than on a full one? Give the two costs.
5. In @prp-exact-shift-deflates, which hypothesis on \( \Z \) is doing the work, and where exactly is it used?
:::
::::

::: {.solution}
(a) Unshifted: \( \A^{(k)} = \Q\R \), \( \A^{(k+1)} = \R\Q \); then \( \R\Q = \Q^{*}\Q\R\Q = \Q^{*}\A^{(k)}\Q \). Shifted: \( \A^{(k)} - \mu\I = \Q\R \), \( \A^{(k+1)} = \R\Q + \mu\I \); then \( \R\Q + \mu\I = \Q^{*}(\A^{(k)} - \mu\I)\Q + \mu\Q^{*}\Q = \Q^{*}\A^{(k)}\Q \).

(b) It says \( \A^{k} = \U_k\T_k \) with \( \U_k = \Q^{(1)}\cdots\Q^{(k)} \) unitary and \( \T_k = \R^{(k)}\cdots\R^{(1)} \) upper triangular, and that \( \A^{(k+1)} = \U_k^{*}\A\U_k \). Comparing first columns, the first column of \( \U_k \) is \( \A^{k}\e_1 \) normalized, which is the \( k \)-th power-method iterate started at \( \e_1 \).

(c) False. The rotation \( \begin{pmatrix} 0 & -1 \\ 1 & 0\end{pmatrix} \) is a fixed point of the unshifted iteration (@exm-qr-fixed-points) and is not triangular; its two eigenvalues have the same modulus, which is exactly the hypothesis @thm-qr-convergence needs.

(d) Because a QR step on a full matrix costs \( O(n^3) \) flops, with the count genuinely growing like \( n^3 \), while a step on a Hessenberg matrix costs about \( 6n^2 \) (@prp-hessenberg-preserved), and the pattern is preserved, so the saving is repeated at every step. The reduction itself is \( O(n^3) \), paid once (@thm-hessenberg-form).

(e) That every subdiagonal entry of \( \Z \) is non-zero. It is used exactly once, to show that the first \( n-1 \) columns of \( \Z - \mu\I \) are independent: deleting the first row leaves a lower triangular matrix whose diagonal is that subdiagonal. Without it \( \Z - \mu\I \) could drop rank in an earlier column, and the zero row of \( \R \) need not be the last.
:::

### B. Practice

::: {#exr-the-qr-algorithm-b1}
[B1: One step by hand]

Let \( \A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \). Compute the QR factorization of \( \A \) in the sense of @thm-qr-factorization, then \( \A^{(2)} = \R\Q \). Verify that \( \A^{(2)} \) is symmetric, has trace \( 4 \) and determinant \( 3 \), and that its off-diagonal entry is smaller than that of \( \A \). Hence estimate how many steps are needed to make the off-diagonal entry smaller than \( 10^{-3} \).
:::

::: {.solution}
The columns are \( \a_1 = (2,1) \) and \( \a_2 = (1,2) \). Then \( r_{11} = \sqrt5 \), \( \q_1 = \tfrac{1}{\sqrt5}(2,1) \), \( r_{12} = \inner{\a_2}{\q_1} = 4/\sqrt5 \), and
\[
\w_2 = (1,2) - \tfrac45(2,1) = \tfrac35(-1, 2),
\qquad r_{22} = \tfrac{3}{\sqrt5},
\qquad \q_2 = \tfrac{1}{\sqrt5}(-1,2) .
\]
So
\[
\Q = \tfrac{1}{\sqrt5}\begin{pmatrix} 2 & -1 \\ 1 & 2\end{pmatrix},
\qquad
\R = \tfrac{1}{\sqrt5}\begin{pmatrix} 5 & 4 \\ 0 & 3\end{pmatrix},
\]
and
\[
\A^{(2)} = \R\Q = \tfrac15\begin{pmatrix} 5 & 4 \\ 0 & 3\end{pmatrix}\begin{pmatrix} 2 & -1 \\ 1 & 2\end{pmatrix}
= \tfrac15\begin{pmatrix} 14 & 3 \\ 3 & 6 \end{pmatrix} .
\]
It is symmetric; its trace is \( 20/5 = 4 = \tr\A \); its determinant is \( (84 - 9)/25 = 3 = \det\A \). The off-diagonal entry fell from \( 1 \) to \( 3/5 \).

The eigenvalues are \( 3 \) and \( 1 \), so @thm-qr-convergence gives the asymptotic factor \( t = 1/3 \) per step. To take \( 3/5 \) below \( 10^{-3} \) needs \( (1/3)^{m} \le 10^{-3}/(3/5) \), that is \( m \ge \log(600)/\log 3 \approx 5.8 \): about six further steps, so seven in all. (The first steps are a little slower than the asymptotic rate, so eight is a safer count.)
:::

::: {#exr-the-qr-algorithm-b2}
[B2: Fixed points]

Determine which of the following matrices are fixed points of the unshifted QR iteration, that is, satisfy \( \A^{(2)} = \A^{(1)} \). Justify your answer; for those that are not, name what changes.

::: {.enumerate options="label=(\alph*)"}
1. any upper triangular \( \A \) with positive real diagonal entries;
2. any unitary \( \A \);
3. \( \A = \begin{pmatrix} 0 & 1 \\ 1 & 0\end{pmatrix} \);
4. any normal \( \A \).
:::
:::

::: {.solution}
(a) Yes. Then \( \A = \I\A \) is a factorization with \( \I \) unitary and \( \A \) upper triangular with positive diagonal, hence the unique one (@thm-qr-factorization), and \( \A^{(2)} = \A\I = \A \).

(b) Yes. Then \( \A = \A\I \) is a factorization with \( \A \) unitary and \( \I \) upper triangular with positive diagonal, hence the unique one, and \( \A^{(2)} = \I\A = \A \).

(c) Yes, by (b): the matrix is a permutation matrix, so its columns are orthonormal. This is worth noticing because its eigenvalues are \( 1 \) and \( -1 \), of equal modulus — another instance of the obstruction of @exm-rotation-stuck, and this one is symmetric, so unlike the rotation it *is* orthogonally similar to a diagonal matrix. The unshifted iteration simply will not find it.

(d) No. A normal matrix need not be fixed: \( \A = \begin{pmatrix} 2 & 1 \\ 1 & 2\end{pmatrix} \) is symmetric, hence normal, and @exr-the-qr-algorithm-b1 computed \( \A^{(2)} = \tfrac15\begin{pmatrix} 14 & 3 \\ 3 & 6\end{pmatrix} \neq \A \). What is preserved is normality, not the matrix: \( \A^{(2)} = \Q^{*}\A\Q \) is unitarily similar to \( \A \), and normality is invariant under unitary similarity.
:::

::: {#exr-the-qr-algorithm-b3}
[B3: A shift that deflates]

Let \( \Z = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \). Take \( \mu \) to be either eigenvalue of \( \Z \) and carry out one shifted QR step. Verify the conclusion of @prp-exact-shift-deflates. *Hint: you need only the last row of \( \R \).*
:::

::: {.solution}
The characteristic polynomial is \( x^2 - 5x - 2 \), with roots \( \mu_{\pm} = (5 \pm \sqrt{33})/2 \). Every \( 2 \times 2 \) matrix is upper Hessenberg, and the single subdiagonal entry \( 3 \) is non-zero, so @prp-exact-shift-deflates applies with \( n = 2 \). Take \( \mu = \mu_+ \). Then
\[
\Z - \mu\I = \begin{pmatrix} 1 - \mu & 2 \\ 3 & 4 - \mu\end{pmatrix}
\]
is singular, of rank \( 1 \) since it is non-zero. Its first column has norm \( r = \sqrt{(1-\mu)^2 + 9} \neq 0 \), so a QR factorization has \( \q_1 = \tfrac1r(1-\mu, 3) \) and \( r_{11} = r \neq 0 \). Because the rank is \( 1 \), the second column of \( \R \) is a multiple of \( \e_1 \), so \( r_{22} = 0 \) and the last row of \( \R \) vanishes. Then the last row of \( \R\Q \) vanishes too, and \( \Z' = \R\Q + \mu\I \) has last row \( (0, \mu) \). Its \( (1,1) \) entry is then \( \tr\Z - \mu = 5 - \mu = \mu_- \), since the trace is preserved. One step produced both eigenvalues exactly.
:::

### C. Going deeper

::: {#exr-the-qr-algorithm-c1}
[C1: Hessenberg form is not enough by itself]

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( \Z \) is upper Hessenberg with \( z_{m+1,m} = 0 \) for some \( 1 \le m \le n-1 \), then \( \spec(\Z) = \spec(\Z_{11}) \cup \spec(\Z_{22}) \), where \( \Z_{11} \) is the leading \( m \times m \) block and \( \Z_{22} \) the trailing \( (n-m) \times (n-m) \) block.
2. Deduce that a QR implementation may, at every step, replace the problem by two smaller ones as soon as one subdiagonal entry vanishes.
3. Give a \( 3 \times 3 \) upper Hessenberg matrix with no zero subdiagonal entry for which the unshifted iteration never reduces any subdiagonal entry at all.
:::
:::

::: {.solution}
(a) With \( z_{m+1,m} = 0 \) and \( \Z \) upper Hessenberg, every entry \( z_{ij} \) with \( i > m \ge j \) vanishes: for \( i > m+1 \) this is \( i > j+1 \), and for \( i = m+1 \) it is either \( j < m \), again \( i > j+1 \), or \( j = m \), the assumed entry. So \( \Z \) is block upper triangular with diagonal blocks \( \Z_{11} \) and \( \Z_{22} \). By @thm-block-multiplication and the determinant of a block triangular matrix (@thm-det-block-triangular), \( p_{\Z}(x) = p_{\Z_{11}}(x)\,p_{\Z_{22}}(x) \), so the eigenvalues of \( \Z \) are those of the two blocks together.

(b) The two blocks are again upper Hessenberg, and by (a) computing their spectra computes that of \( \Z \). Each step on a block of size \( m \) costs about \( 6m^2 \) rather than \( 6n^2 \) (@prp-hessenberg-preserved), so splitting is a strict gain; and part (a) guarantees no eigenvalue is lost. This is deflation.

(c) Take the cyclic permutation matrix
\[
\Z = \begin{pmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix},
\]
which is upper Hessenberg with subdiagonal entries \( 1, 1 \), and is orthogonal. By @exr-the-qr-algorithm-b2 (b) it is a fixed point of the unshifted iteration, so no subdiagonal entry ever moves. Its eigenvalues are the three cube roots of \( 1 \), all of modulus \( 1 \) — the obstruction of @thm-qr-convergence in its purest form.
:::

::: {#exr-the-qr-algorithm-c2}
[C2: Hermitian iterates and the Rayleigh quotient]

Let \( \A \in M_n(\nC) \) be Hermitian and let \( \A^{(k)} \) be its unshifted QR iterates.

::: {.enumerate options="label=(\alph*)"}
1. Prove that every \( \A^{(k)} \) is Hermitian with the same eigenvalues as \( \A \).
2. Prove that \( a^{(k)}_{nn} = R_{\A}(\u_n^{(k)}) \), where \( \u_n^{(k)} \) is the last column of \( \U_{k-1} \) and \( R_{\A} \) is the Rayleigh quotient of @def-rayleigh-quotient.
3. Hence explain, citing @thm-hermitian-residual-bound, why the Rayleigh shift \( \mu_k = a^{(k)}_{nn} \) is a certified eigenvalue estimate, and say what the certificate is.
:::
:::

::: {.solution}
(a) By @thm-qr-is-orthogonal-iteration, \( \A^{(k)} = \U_{k-1}^{*}\A\U_{k-1} \), with \( \U_0 = \I \) at \( k = 1 \), so \( (\A^{(k)})^{*} = \U_{k-1}^{*}\A^{*}\U_{k-1} = \A^{(k)} \), and unitary similarity preserves eigenvalues.

(b) Writing \( \u_n = \U_{k-1}\e_n \), which is a unit vector since \( \U_{k-1} \) is unitary,
\[
a^{(k)}_{nn} = \e_n^{*}\A^{(k)}\e_n = \e_n^{*}\U_{k-1}^{*}\A\U_{k-1}\e_n = \u_n^{*}\A\u_n = R_{\A}(\u_n),
\]
the last equality because \( R_{\A}(\x) = \x^{*}\A\x/\x^{*}\x \) and \( \u_n^{*}\u_n = 1 \).

(c) Put \( \mu = a^{(k)}_{nn} \) and \( \r = \A\u_n - \mu\u_n \). Then \( \mu \) is real, \( \A \) being Hermitian, and @thm-hermitian-residual-bound says that \( \A \) has an eigenvalue in \( [\mu - \norm{\r}_2, \mu + \norm{\r}_2] \). The certificate is \( \norm{\r}_2 \), and it costs nothing extra: by the computation in (b), \( \U_{k-1}^{*}\r = \A^{(k)}\e_n - \mu\e_n \) is the last column of \( \A^{(k)} \) with its diagonal entry removed, so \( \norm{\r}_2 \) is the Euclidean norm of the entries of that column other than the diagonal one. If \( \A \) was first reduced to Hessenberg form, so that every \( \A^{(k)} \) is Hermitian and upper Hessenberg, hence tridiagonal, that norm is the single entry \( \lvert a^{(k)}_{n-1,n}\rvert \). The algorithm is already watching that number.
:::

::: {#exr-the-qr-algorithm-c3}
[C3: Why the powers are the right object]

Let \( \A \in M_n(\nC) \) be invertible, with unshifted QR iterates as in @def-qr-iteration.

::: {.enumerate options="label=(\alph*)"}
1. Prove that for \( 1 \le j \le n \), the subspace spanned by the first \( j \) columns of \( \U_k \) equals \( \A^{k}(\Span(\e_1, \dots, \e_j)) \).
2. Deduce that if the first \( j \) columns of \( \U_k \) converge to a basis of an \( \A \)-invariant subspace \( W \), then the entries of \( \A^{(k+1)} \) in rows \( j+1, \dots, n \) of columns \( 1, \dots, j \) tend to \( 0 \).
:::

*Hint for (b): write the entries as inner products of \( \A \) applied to one column against another.*
:::

::: {.solution}
(a) By @thm-qr-is-orthogonal-iteration, \( \A^{k} = \U_k\T_k \) with \( \T_k \) upper triangular and invertible (Quick check above), so \( \A^{k}\e_i = \U_k\T_k\e_i \) lies in \( \Span(\U_k\e_1, \dots, \U_k\e_i) \) for each \( i \), since \( \T_k\e_i \) has zeros below row \( i \). Hence \( \A^{k}(\Span(\e_1,\dots,\e_j)) \subseteq \Span(\U_k\e_1,\dots,\U_k\e_j) \). Both sides have dimension \( j \): the left because \( \A^{k} \) is invertible, the right because the columns of a unitary matrix are independent. One inclusion plus equal dimension gives equality.

(b) Write \( \u_i = \U_k\e_i \). For \( p > j \ge q \),
\[
a^{(k+1)}_{pq} = \e_p^{*}\U_k^{*}\A\U_k\e_q = \u_p^{*}\A\u_q = \inner{\A\u_q}{\u_p} .
\]
Suppose \( \u_1, \dots, \u_j \) converge to an orthonormal basis \( \w_1, \dots, \w_j \) of an \( \A \)-invariant subspace \( W \), let \( P \) be the orthogonal projection onto \( W \) (@def-orthogonal-projection) and put \( \delta_k = \max_{q \le j}\norm{\u_q - \w_q}_2 \), so \( \delta_k \to 0 \). Since \( \A\w_q \in W \), we have \( (\I - P)\A\w_q = \0 \) and hence \( \norm{(\I - P)\A\u_q}_2 = \norm{(\I-P)\A(\u_q - \w_q)}_2 \le \norm{\A}_2\delta_k \). Since \( \inner{\u_p}{\u_q} = 0 \) for \( q \le j < p \), we have \( \lvert\inner{\u_p}{\w_q}\rvert = \lvert\inner{\u_p}{\w_q - \u_q}\rvert \le \delta_k \) by Cauchy–Schwarz (@thm-cauchy-schwarz), so \( \norm{P\u_p}_2 \le j\,\delta_k \). Splitting \( \u_p \) and using that \( P \) is self-adjoint,
\[
\begin{aligned}
\lvert\inner{\A\u_q}{\u_p}\rvert
&= \bigl\lvert\inner{(\I-P)\A\u_q}{\u_p} + \inner{\A\u_q}{P\u_p}\bigr\rvert \\
&\le \norm{(\I-P)\A\u_q}_2 + \norm{\A}_2\norm{P\u_p}_2
\ \le\ (1 + j)\norm{\A}_2\,\delta_k ,
\end{aligned}
\]
by Cauchy–Schwarz again and \( \norm{\u_p}_2 = \norm{\u_q}_2 = 1 \). The right-hand side tends to \( 0 \), so \( a^{(k+1)}_{pq} \to 0 \). This is @thm-qr-convergence for \( j = 1 \), read as a statement about invariant subspaces rather than about eigenvectors, and it is the form in which the general convergence theorem quoted above is proved.
:::
