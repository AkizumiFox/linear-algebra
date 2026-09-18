# The Moore–Penrose Pseudoinverse

Chapter 10 solved \( \A\x = \b \) twice over: when there is no solution it produced a least-squares solution, and when there are too many it produced the shortest one. It then left an IOU. The two answers "are usually wanted together: given any \( \A \) and \( \b \), first minimize \( \norm{\A\x - \b} \), then among the minimizers take the shortest. Chapter 12 packages the combined answer as a single matrix, the **pseudoinverse** \( \A^{+} \), with \( \x = \A^{+}\b \) in all cases at once." This section builds that matrix and pays the debt.

Throughout, \( F = \nR \) or \( F = \nC \), \( \A \in M_{m \times n}(F) \), \( p = \min(m, n) \) and \( r = \rank\A \), with singular values \( \sigma_1 \ge \dots \ge \sigma_p \ge 0 \) (@def-singular-values), so \( \sigma_i > 0 \) exactly for \( i \le r \).

## One matrix instead of three formulas

Here is the state of play at the end of Chapter 10. To answer "what is the best \( \x \)?" we had three different recipes, and choosing between them required knowing something about \( \A \) first.

- If \( \A \) is square and invertible, \( \x = \A^{-1}\b \).
- If the columns of \( \A \) are independent, \( \x = (\A^{*}\A)^{-1}\A^{*}\b \) (@cor-least-squares-unique).
- If \( \A\x = \b \) is consistent but \( \A \) has a kernel, \( \x = \x_{\min} \), the unique solution orthogonal to \( \nul(\A) \) (@thm-minimum-norm-solution).

Three recipes, three hypotheses, and a gap: when \( \A \) has both a kernel *and* a column space missing \( \b \), none of them applies. That is not an exotic case. It is what happens whenever a large table of measurements has both redundant columns and noise.

The goal, stated before we know how to reach it, is a single matrix \( \A^{+} \), depending on \( \A \) alone, for which \( \x = \A^{+}\b \) is the right answer in every case. Reading the goal backwards tells us what \( \A^{+} \) must do, and the singular value decomposition tells us how to build it.

## Inverting what can be inverted

Why is there no inverse in general? Two obstructions, and they are the two halves of @thm-four-subspaces-orthogonal. The map \( \x \mapsto \A\x \) may fail to be injective, because \( \nul(\A) \ne \{\0\} \); and it may fail to be surjective, because \( \col(\A) \ne F^m \). Neither obstruction is fatal if we are willing to sacrifice part of the domain and part of the codomain.

Restrict the map to \( \col(\A^{*}) = \nul(\A)^{\perp} \), which throws away the kernel. What is left is a bijection onto \( \col(\A) \), and a bijection has an inverse. Extend that inverse to all of \( F^m \) by declaring it \( \0 \) on \( \col(\A)^{\perp} \), where nothing in the image can tell us anything. That is the whole construction, and it is the same trick that turns \( \sin \) into \( \arcsin \): shrink the domain until the function is injective, shrink the codomain until it is surjective, invert, and say clearly what was given up.

*Invert what can be inverted, and send the rest to zero.*

The singular value decomposition performs all three operations at once, because it presents \( \A \) as a diagonal matrix in orthonormal coordinates, and a diagonal matrix is inverted one entry at a time.

::: {#def-pseudoinverse}
[Moore–Penrose pseudoinverse]

Let \( \A \in M_{m \times n}(F) \) and let \( \A = \U\vSigma\V^{*} \) be a singular value decomposition (@thm-svd), so that \( \U \in M_m(F) \) and \( \V \in M_n(F) \) are unitary and \( \vSigma \in M_{m \times n}(F) \) has the singular values \( \sigma_1, \dots, \sigma_p \) on its diagonal and zeros elsewhere. Let \( \vSigma^{+} \in M_{n \times m}(F) \) be the matrix with
\[
(\vSigma^{+})_{ii} = \begin{cases} \sigma_i^{-1}, & \sigma_i > 0, \\ 0, & \sigma_i = 0, \end{cases}
\]
for \( 1 \le i \le p \), and all other entries \( 0 \). The **Moore–Penrose pseudoinverse** of \( \A \) is
\[
\A^{+} \coloneqq \V\vSigma^{+}\U^{*} \in M_{n \times m}(F) .
\]
:::

Clause by clause. The matrix \( \vSigma^{+} \) is \( \vSigma \) **transposed and then inverted where inversion is legal**: the shape flips from \( m \times n \) to \( n \times m \), each non-zero diagonal entry is replaced by its reciprocal, and each zero diagonal entry is left alone — **not** replaced by anything, since \( 0^{-1} \) does not exist. The outer factors are exchanged and starred, exactly as they would be in \( (\U\vSigma\V^{*})^{-1} = \V\vSigma^{-1}\U^{*} \) if \( \vSigma \) were invertible. And the result is \( n \times m \), the shape an inverse of \( \A \) would have to be.

**Well-definedness is a real question here, not a formality.** The singular *values* are determined by \( \A \), but the unitary factors are not (@thm-singular-values-unique), so the recipe above is applied to a choice, and nothing so far says that two choices give the same answer. They do.

::: {#prp-pseudoinverse-well-defined}
[The pseudoinverse does not depend on the decomposition]

Let \( \A \in M_{m \times n}(F) \) and let \( \A = \U\vSigma\V^{*} \) be any singular value decomposition (@thm-svd). Then \( \X = \V\vSigma^{+}\U^{*} \) is the unique matrix in \( M_{n \times m}(F) \) such that

::: {.enumerate options="label=(\roman*)"}
1. for every \( \y \in \col(\A) \), \( \X\y \) is the unique vector of \( \col(\A^{*}) \) that \( \A \) sends to \( \y \);
2. \( \X\y = \0 \) for every \( \y \in \col(\A)^{\perp} \).
:::

In particular \( \A^{+} \) depends on \( \A \) alone.
:::

::: {.idea}
Conditions (i) and (ii) mention only \( \A \), so if one matrix satisfies them, that matrix is determined by \( \A \). The work is to check that they can be satisfied at all — which is the "restrict, invert, extend" story of the previous page written out — and that the matrix built from an arbitrary decomposition is the one that satisfies them. For the second part, the singular vectors are orthonormal bases of the subspaces involved, so both conditions can be checked on basis vectors.
:::

::: {.proof}
**The conditions determine at most one matrix.** First, \( \A \) maps \( \col(\A^{*}) \) bijectively onto \( \col(\A) \). Injectivity: if \( \x \in \col(\A^{*}) \) and \( \A\x = \0 \), then \( \x \in \nul(\A) \cap \nul(\A)^{\perp} = \{\0\} \), since \( \col(\A^{*}) = \nul(\A)^{\perp} \) by @thm-four-subspaces-orthogonal (b). Surjectivity: the image is contained in \( \col(\A) \), and by injectivity it has dimension \( \dim\col(\A^{*}) = \rank\A^{*} = \rank\A = \dim\col(\A) \), the middle equality by @cor-rank-adjoint (a) applied to \( \x \mapsto \A\x \). So (i) prescribes \( \X \) on \( \col(\A) \) and (ii) prescribes it on \( \col(\A)^{\perp} \); since \( F^m = \col(\A) \oplus \col(\A)^{\perp} \) by @thm-orthogonal-decomposition (a), a linear map is determined by the two prescriptions.

**The matrix \( \X = \V\vSigma^{+}\U^{*} \) satisfies them.** Write \( \u_1, \dots, \u_m \) and \( \v_1, \dots, \v_n \) for the columns of \( \U \) and \( \V \). Since rank is unchanged by invertible factors (@thm-rank-product-inequality), \( r = \rank\A = \rank\vSigma \) is the number of non-zero \( \sigma_i \). By @cor-svd-four-subspaces, \( (\u_1, \dots, \u_r) \) is an orthonormal basis of \( \col(\A) \), the remaining \( \u_j \) are an orthonormal basis of \( \col(\A)^{\perp} \), and \( (\v_1, \dots, \v_r) \) is an orthonormal basis of \( \col(\A^{*}) \). Multiplying out the definition,
\[
\X = \sum_{i=1}^{r} \sigma_i^{-1}\v_i\u_i^{*} ,
\]
so \( \X\u_i = \sigma_i^{-1}\v_i \) for \( i \le r \) and \( \X\u_j = \0 \) for \( j > r \). The second statement gives (ii) by linearity.

For (i), let \( \y = \sum_{i \le r}c_i\u_i \in \col(\A) \). Then \( \X\y = \sum_{i \le r}c_i\sigma_i^{-1}\v_i \in \col(\A^{*}) \), and since \( \A\v_i = \sigma_i\u_i \) (the rank-one expansion of @thm-compact-svd read one column at a time),
\[
\A(\X\y) = \sum_{i \le r} c_i\sigma_i^{-1}\sigma_i\u_i = \y .
\]
By the injectivity proved above, \( \X\y \) is the *unique* vector of \( \col(\A^{*}) \) with this property. This proves (i), and with it the proposition.
:::

So \( \A^{+} \) is an honest function of \( \A \). Five examples, simplest first.

::: {#exm-pseudoinverse-first-examples}
[Five pseudoinverses]

::: {.enumerate options="label=(\alph*)"}
1. **\( \A \) invertible.** Then \( m = n = r \), \( \vSigma \) is invertible and \( \vSigma^{+} = \vSigma^{-1} \), so \( \A^{+} = \V\vSigma^{-1}\U^{*} = (\U\vSigma\V^{*})^{-1} = \A^{-1} \). The pseudoinverse extends the inverse, which is the first thing it had to do.
2. **\( \A = \0 \in M_{m \times n}(F) \).** Every singular value is \( 0 \), so \( \vSigma^{+} = \0 \) and \( \A^{+} = \0 \in M_{n \times m}(F) \). The degenerate case is worth keeping in mind: the pseudoinverse of the worst possible matrix is not undefined, it is zero, which is what "invert nothing, kill everything" means.
3. **Diagonal.** \( \diag(2, 0, 5)^{+} = \diag\bigl(\tfrac12, 0, \tfrac15\bigr) \). The zero is left where it is.
4. **A single non-zero column \( \a \in M_{n \times 1}(F) \).** Here \( \sigma_1 = \norm{\a} \), \( \u_1 = \a/\norm{\a} \) and \( \v_1 = 1 \), so \( \a^{+} = \a^{*}/\norm{\a}^2 \), a row vector. Then \( \a^{+}\a = 1 \) but \( \a\a^{+} = \a\a^{*}/\norm{\a}^2 \) is the orthogonal projection onto \( \Span(\a) \).
5. **\( \A = \begin{psmallmatrix} 1 & 1 \\ 1 & 1\end{psmallmatrix} \).** This is \( \sigma_1\u_1\v_1^{*} \) with \( \sigma_1 = 2 \) and \( \u_1 = \v_1 = \tfrac{1}{\sqrt2}(1, 1) \), since \( 2\u_1\v_1^{*} = 2 \cdot \tfrac12\begin{psmallmatrix} 1 & 1 \\ 1 & 1\end{psmallmatrix} = \A \). Hence
\[
\A^{+} = \tfrac12\v_1\u_1^{*} = \frac14\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} .
\]
:::
:::

A **non-example by minimal change.** Item (a) of the list is often written \( \A^{+} = (\A^{*}\A)^{-1}\A^{*} \), and @thm-pseudoinverse-properties below confirms that formula whenever the columns of \( \A \) are independent. Change one column of a \( 3 \times 2 \) matrix into a multiple of the other, and the formula stops existing: \( \A^{*}\A \) is then singular (@lem-kernel-normal-equations), so \( (\A^{*}\A)^{-1} \) is not a matrix at all. The pseudoinverse survives the change; the formula does not. That is the difference between a definition and a recipe.

**Why this definition.** It is forced. Any reasonable "inverse" must undo \( \A \) where \( \A \) can be undone; there is exactly one subspace on which \( \A \) is a bijection and which meets \( \nul(\A) \) only in \( \0 \) while being determined by \( \A \) alone, namely \( \nul(\A)^{\perp} \); and setting the answer to \( \0 \) on \( \col(\A)^{\perp} \) is the only choice that keeps the map linear without inventing information. The names are those of the two people who published the idea, thirty-five years apart: Moore in 1920 through a projection formula, Penrose in 1955 through the four conditions of the next theorem.

::: {.warning}
**\( \A^{+}\A \) is not the identity, and \( \A^{+} \) is \( n \times m \).** Two habits from the invertible case have to go. First the shape: if \( \A \) is \( 3 \times 5 \) then \( \A^{+} \) is \( 5 \times 3 \), so \( \A\A^{+} \) is \( 3 \times 3 \) and \( \A^{+}\A \) is \( 5 \times 5 \) — they are not even the same size, let alone both \( \I \). Second the identity: for \( \A = \begin{psmallmatrix} 1 & 1 \\ 1 & 1\end{psmallmatrix} \) of @exm-pseudoinverse-first-examples (e),
\[
\A^{+}\A = \frac14\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = \frac12\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \ne \I_2 .
\]
The right question is not "is it the identity?" but "the identity on *what*?", and @thm-pseudoinverse-properties answers it: \( \A^{+}\A \) is the identity on \( \col(\A^{*}) \) and zero on \( \nul(\A) \).
:::

::: {.check}
Let \( \A = \begin{psmallmatrix} 1 & 1 \\ 0 & 0 \end{psmallmatrix} \). Find \( \A^{+} \), then compute \( \A\A^{+} \) and \( \A^{+}\A \) and identify each as a projection.
:::

::: {.solution}
Here \( \A = \e_1(1, 1) \) has rank one, so \( \sigma_1 = \norm{\e_1}\,\norm{(1,1)} = \sqrt2 \) with \( \u_1 = \e_1 \) and \( \v_1 = \tfrac{1}{\sqrt2}(1, 1) \), and
\[
\A^{+} = \sigma_1^{-1}\v_1\u_1^{*} = \frac12\begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix} .
\]
Therefore
\[
\A\A^{+} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix},
\qquad
\A^{+}\A = \frac12\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} .
\]
Neither is \( \I_2 \). The first is the orthogonal projection onto \( \Span(\e_1) = \col(\A) \); the second is the orthogonal projection onto \( \Span\bigl((1, 1)\bigr) = \col(\A\tp) \), the row space. Each is the identity exactly on the subspace named, and zero on its orthogonal complement — which is what "as close to the identity as the shapes allow" means.
:::

## The four Penrose conditions

The definition builds \( \A^{+} \) out of a decomposition. The following theorem characterizes it by four equations that mention nothing but \( \A \), \( \X \) and the star. It is the second, and better, answer to the well-definedness question, and it is how one *verifies* a candidate pseudoinverse in practice: guess, then check four identities.

::: {#thm-penrose-conditions}
[The Penrose Conditions]

Let \( \A \in M_{m \times n}(F) \). Then \( \X = \A^{+} \) is the **unique** matrix in \( M_{n \times m}(F) \) satisfying all four of

::: {.enumerate options="label=(P\arabic*)"}
1. \( \A\X\A = \A \);
2. \( \X\A\X = \X \);
3. \( (\A\X)^{*} = \A\X \);
4. \( (\X\A)^{*} = \X\A \).
:::
:::

::: {.idea}
Existence is a computation with \( \vSigma \): each condition collapses to an identity between \( \vSigma \), \( \vSigma^{+} \) and the diagonal matrix of \( r \) ones. Uniqueness is a puzzle. Given two solutions \( \X_1 \) and \( \X_2 \), the goal is a chain of equalities starting at \( \X_1 \) and ending at \( \X_2 \), so the plan is to walk to a symmetric midpoint: get \( \X_1 = \X_1\A\X_2 \) by pushing \( \X_2 \) in from the right, then run the mirror image of the same argument with \( \X_2 \) as the subject. Two preliminary identities make the walk possible, and both come from starring one of the conditions — the move that manufactures an \( \A^{*} \) when the hypotheses offer only \( \A \).
:::

::: {.proof}
**Existence.** Let \( \A = \U\vSigma\V^{*} \) and \( \X = \V\vSigma^{+}\U^{*} \). Using \( \V^{*}\V = \I_n \) and \( \U^{*}\U = \I_m \),
\[
\A\X = \U\vSigma\vSigma^{+}\U^{*}, \qquad \X\A = \V\vSigma^{+}\vSigma\V^{*} .
\]
Now \( \vSigma\vSigma^{+} \in M_m(F) \) is diagonal with \( \sigma_i\sigma_i^{-1} = 1 \) in the first \( r \) diagonal places and \( 0 \) elsewhere, and \( \vSigma^{+}\vSigma \in M_n(F) \) is diagonal with the same pattern. Both are real diagonal, hence Hermitian, so \( \A\X \) and \( \X\A \) are Hermitian, which is (P3) and (P4). Moreover \( \vSigma\vSigma^{+}\vSigma = \vSigma \) and \( \vSigma^{+}\vSigma\vSigma^{+} = \vSigma^{+} \), because multiplying a diagonal matrix by a diagonal matrix of ones and zeros keeps exactly the entries in the positions marked \( 1 \), and those are the positions where \( \vSigma \) and \( \vSigma^{+} \) are non-zero anyway. Hence
\[
\A\X\A = \U\vSigma\vSigma^{+}\vSigma\V^{*} = \A, \qquad
\X\A\X = \V\vSigma^{+}\vSigma\vSigma^{+}\U^{*} = \X ,
\]
which is (P1) and (P2).

**Uniqueness.** Suppose \( \X \) satisfies (P1)–(P4). Two consequences:
\[
\X\X^{*}\A^{*} = \X, \qquad \A\A^{*}\X^{*} = \A . \tag{$\ast$}
\]
For the first, \( \X = \X\A\X \) by (P2), and \( \A\X = (\A\X)^{*} = \X^{*}\A^{*} \) by (P3), so \( \X = \X(\A\X) = \X\X^{*}\A^{*} \). For the second, \( \A = \A\X\A \) by (P1), and \( \X\A = (\X\A)^{*} = \A^{*}\X^{*} \) by (P4), so \( \A = \A(\X\A) = \A\A^{*}\X^{*} \). Starring the second identity of \( (\ast) \) gives the form we also need,
\[
\X\A\A^{*} = \A^{*} . \tag{$\ast\ast$}
\]

Now let \( \X_1 \) and \( \X_2 \) both satisfy (P1)–(P4). Starting from \( \X_1 \) and working towards a term containing \( \X_2 \),
\[
\begin{aligned}
\X_1 &= \X_1\X_1^{*}\A^{*} = \X_1\X_1^{*}(\A\X_2\A)^{*} \\
 &= \X_1\X_1^{*}\A^{*}(\A\X_2)^{*} = \X_1\X_1^{*}\A^{*}\A\X_2 \\
 &= \X_1\A\X_2 .
\end{aligned}
\]
The first equality is \( (\ast) \) for \( \X_1 \); the second replaces \( \A \) by \( \A\X_2\A \), which is (P1) for \( \X_2 \); the third reverses the product under the star; the fourth is (P3) for \( \X_2 \); and the last is \( (\ast) \) for \( \X_1 \) again, applied to the first three factors.

Now the mirror argument, with \( \X_2 \) as the subject:
\[
\begin{aligned}
\X_1\A\X_2 &= \X_1\A\A^{*}\X_2^{*}\X_2 = \A^{*}\X_2^{*}\X_2 \\
 &= (\X_2\A)^{*}\X_2 = \X_2\A\X_2 = \X_2 .
\end{aligned}
\]
Here the first equality replaces \( \A \) by \( \A\A^{*}\X_2^{*} \), which is \( (\ast) \) for \( \X_2 \); the second is \( (\ast\ast) \) for \( \X_1 \); the fourth is (P4) for \( \X_2 \); and the last is (P2) for \( \X_2 \).

Hence \( \X_1 = \X_2 \). Since \( \A^{+} \) satisfies the four conditions, every matrix satisfying them equals \( \A^{+} \). This proves the theorem.
:::

Both halves of the argument are the same two moves: star a condition to trade \( \A \) for \( \A^{*} \), then use \( (\ast) \) to collapse a triple product. The conditions are also exactly what one should check when an explicit candidate is on the table, and several of the proofs below do nothing else.

::: {.remark}
The four conditions are not independent decoration. Dropping (P2) leaves the **generalized inverses**, matrices with \( \A\X\A = \A \), of which there are many when \( \A \) is singular; dropping (P3) and (P4) leaves more still. Each condition removes freedom, and only all four together remove all of it. Exercise C3 identifies the matrices for which \( \A^{*} \) itself already satisfies them.
:::

## What the pseudoinverse does

::: {#thm-pseudoinverse-properties}
[Properties of the pseudoinverse]

Let \( \A \in M_{m \times n}(F) \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \A\A^{+} = P_{\col(\A)} \) and \( \A^{+}\A = P_{\col(\A^{*})} \), the orthogonal projections onto the column space of \( \A \) in \( F^m \) and onto the column space of \( \A^{*} \) in \( F^n \);
2. \( (\A^{+})^{+} = \A \);
3. \( (\A^{+})^{*} = (\A^{*})^{+} \);
4. \( \rank\A^{+} = \rank\A \);
5. \( \A^{+} = \A^{-1} \) if \( \A \) is invertible; \( \A^{+} = (\A^{*}\A)^{-1}\A^{*} \) if \( \rank\A = n \); and \( \A^{+} = \A^{*}(\A\A^{*})^{-1} \) if \( \rank\A = m \).
:::
:::

::: {.idea}
Clause (a) is the computation already done in the existence half of @thm-penrose-conditions, read through @thm-projection-formula. Clauses (b) and (c) are one line each, because the Penrose conditions are almost symmetric in \( \A \) and \( \X \), and starring all four of them produces the four conditions for \( \A^{*} \). Clause (e) is three checks of the same kind: write down the candidate and confirm (P1)–(P4).
:::

::: {.proof}
(a) With \( \A = \U\vSigma\V^{*} \) and the notation of @prp-pseudoinverse-well-defined, the existence computation gave \( \A\A^{+} = \U\vSigma\vSigma^{+}\U^{*} \), where \( \vSigma\vSigma^{+} \) is diagonal with \( r \) ones followed by zeros. Multiplying out,
\[
\A\A^{+} = \sum_{i=1}^{r} \u_i\u_i^{*} .
\]
For \( \y \in F^m \) this sends \( \y \) to \( \sum_{i \le r}\inner{\y}{\u_i}\u_i \), which by @thm-projection-formula (a) is the orthogonal projection of \( \y \) onto \( \Span(\u_1, \dots, \u_r) = \col(\A) \) (@cor-svd-four-subspaces). The same computation with \( \vSigma^{+}\vSigma \) gives \( \A^{+}\A = \sum_{i \le r}\v_i\v_i^{*} = P_{\col(\A^{*})} \).

(b) The four Penrose conditions for the pair \( (\A, \X) \) become, when the roles of \( \A \) and \( \X \) are exchanged, the list (P2), (P1), (P4), (P3) — the same four conditions. So \( \A \) satisfies the Penrose conditions for \( \A^{+} \), and @thm-penrose-conditions gives \( (\A^{+})^{+} = \A \).

(c) Put \( \X = (\A^{+})^{*} \) and check the four conditions for \( \A^{*} \). Using \( (\B\C)^{*} = \C^{*}\B^{*} \) throughout,
\[
\A^{*}\X\A^{*} = (\A\A^{+}\A)^{*} = \A^{*}, \qquad
\X\A^{*}\X = (\A^{+}\A\A^{+})^{*} = \X ,
\]
which are (P1) and (P2). Next, \( \A^{*}\X = (\A^{+}\A)^{*} = \A^{+}\A \) by (P4) for \( \A \), and \( \A^{+}\A \) is Hermitian, so (P3) holds; and \( \X\A^{*} = (\A\A^{+})^{*} = \A\A^{+} \) by (P3) for \( \A \), which is Hermitian, so (P4) holds. By uniqueness, \( \X = (\A^{*})^{+} \).

(d) \( \A^{+} = \V\vSigma^{+}\U^{*} \) with \( \U, \V \) invertible, so \( \rank\A^{+} = \rank\vSigma^{+} = r \) by @thm-rank-product-inequality, the last equality because \( \vSigma^{+} \) has exactly \( r \) non-zero entries, all in distinct rows and columns.

(e) The invertible case is @exm-pseudoinverse-first-examples (a). Suppose \( \rank\A = n \). Then \( \A^{*}\A \) is invertible (@cor-least-squares-unique), so \( \X = (\A^{*}\A)^{-1}\A^{*} \) is defined, and \( ((\A^{*}\A)^{-1})^{*} = (\A^{*}\A)^{-1} \) since \( \A^{*}\A \) is Hermitian. Then
\[
\X\A = (\A^{*}\A)^{-1}\A^{*}\A = \I_n ,
\]
which is Hermitian, giving (P4); and (P1), (P2) follow at once, since \( \A\X\A = \A\I_n = \A \) and \( \X\A\X = \I_n\X = \X \). For (P3), \( \A\X = \A(\A^{*}\A)^{-1}\A^{*} \), whose conjugate transpose is itself. So \( \X = \A^{+} \).

For the last formula, suppose \( \rank\A = m \). Then \( \rank\A^{*} = m \) is the number of columns of \( \A^{*} \), so the case just proved applies to \( \A^{*} \) and gives \( (\A^{*})^{+} = (\A\A^{*})^{-1}\A \). By (c),
\[
\A^{+} = \bigl((\A^{*})^{+}\bigr)^{*} = \bigl((\A\A^{*})^{-1}\A\bigr)^{*} = \A^{*}(\A\A^{*})^{-1},
\]
using that \( \A\A^{*} \) is Hermitian, hence so is its inverse. This proves the theorem.
:::

Clause (a) is the one to remember, and it answers the question the warning raised. The products \( \A\A^{+} \) and \( \A^{+}\A \) are not identities; they are the identity **restricted to the subspaces where \( \A \) is invertible**, and zero on the complements. Clause (e) shows that the three recipes of Chapter 10 were all the pseudoinverse in disguise, each written in the notation that its hypothesis made available.

::: {.warning}
**\( (\A\B)^{+} \ne \B^{+}\A^{+} \) in general.** The rule \( (\A\B)^{-1} = \B^{-1}\A^{-1} \) does not survive. Take
\[
\A = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}, \qquad
\B = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} .
\]
The Quick check above found \( \A^{+} = \tfrac12\begin{psmallmatrix} 1 & 0 \\ 1 & 0\end{psmallmatrix} \), and one may confirm it against @thm-penrose-conditions: the two products computed there are Hermitian, and \( \A\A^{+}\A = \A \), \( \A^{+}\A\A^{+} = \A^{+} \). Meanwhile \( \B \) is Hermitian and idempotent, so \( \X = \B \) satisfies (P1)–(P4) and \( \B^{+} = \B \). Now \( \A\B = \begin{psmallmatrix} 1 & 0 \\ 0 & 0\end{psmallmatrix} = \B \), so
\[
(\A\B)^{+} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix},
\qquad
\B^{+}\A^{+} = \frac12\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} .
\]
The two differ by a factor of \( 2 \). The reversal rule does hold under extra hypotheses — for instance when \( \A \) has independent columns and \( \B \) has independent rows, which is Exercise C2 — but never assume it.
:::

## Least squares and minimum norm, in one matrix

Everything is now in place to pay Chapter 10's debt.

::: {#thm-pseudoinverse-least-squares}
[The pseudoinverse solves both problems at once]

Let \( \A \in M_{m \times n}(F) \) and \( \b \in F^m \), and put \( \x^{+} = \A^{+}\b \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \x^{+} \) is a least-squares solution of \( \A\x = \b \), that is, \( \norm{\A\x^{+} - \b} \le \norm{\A\z - \b} \) for every \( \z \in F^n \);
2. \( \norm{\x^{+}} < \norm{\x} \) for every other least-squares solution \( \x \);
3. if \( \A\x = \b \) is consistent, \( \x^{+} \) is its minimum-norm solution in the sense of @thm-minimum-norm-solution; if \( \A \) is invertible, \( \x^{+} = \A^{-1}\b \).
:::
:::

::: {.idea}
Both halves are already proved; the pseudoinverse only has to be recognized inside them. For (a), \( \A\x^{+} = \A\A^{+}\b \) is the projection of \( \b \) onto \( \col(\A) \), which is precisely condition (b) of the Least Squares Theorem. For (b), the least-squares solutions are the solutions of one consistent system, so the Minimum-Norm Solution Theorem applies to that system and singles out the solution lying in \( \nul(\A)^{\perp} \); and \( \A^{+}\b \) lies there, because every column of \( \A^{+} \) does.
:::

::: {.proof}
(a) By @thm-pseudoinverse-properties (a), \( \A\x^{+} = \A\A^{+}\b = P_{U}\b \) with \( U = \col(\A) \). This is condition (b) of @thm-least-squares, so \( \x^{+} \) is a least-squares solution.

(b) By @thm-least-squares, the least-squares solutions of \( \A\x = \b \) are exactly the solutions of the system \( \A\x = P_U\b \), which is consistent because \( P_U\b \in U = \col(\A) \). Apply @thm-minimum-norm-solution to that system: exactly one of its solutions lies in \( \nul(\A)^{\perp} \), and it is strictly shorter than all the others.

It remains to see that \( \x^{+} \) is that one. By (P2), \( \A^{+} = \A^{+}\A\A^{+} = P_{\col(\A^{*})}\A^{+} \) using @thm-pseudoinverse-properties (a), so every column of \( \A^{+} \), and hence every vector \( \A^{+}\b \), lies in \( \col(\A^{*}) \). By @thm-four-subspaces-orthogonal (b), \( \col(\A^{*}) = \nul(\A)^{\perp} \). So \( \x^{+} \) is the minimum-norm solution of \( \A\x = P_U\b \), which by the previous paragraph is what (b) asserts.

(c) If \( \A\x = \b \) is consistent then \( \b \in \col(\A) \), so \( P_U\b = \b \) and the least-squares solutions are the actual solutions; (b) then says \( \x^{+} \) is the shortest of them, which is @thm-minimum-norm-solution's \( \x_{\min} \). If \( \A \) is invertible, \( \A^{+} = \A^{-1} \) by @thm-pseudoinverse-properties (e). This proves the theorem.
:::

**The promise, discharged.** Section 4 of Chapter 10 said that the two answers are usually wanted together — first minimize \( \norm{\A\x - \b} \), then among the minimizers take the shortest — and that Chapter 12 would package the combined answer as a single matrix \( \A^{+} \), with \( \x = \A^{+}\b \) in all cases at once. That is @thm-pseudoinverse-least-squares, word for word: clause (a) does the minimizing, clause (b) takes the shortest, and clause (c) plus @thm-pseudoinverse-properties (e) checks that the three special recipes of Chapter 10 are recovered as special cases. There is no hypothesis on \( \A \) anywhere in the statement.

**The notation, settled.** Chapter 10 wrote \( \x_{\min} \) for the minimum-norm solution of a *consistent* system and left the symbol without a formula. From now on it has one, and its meaning extends to every system:
\[
\x_{\min} = \A^{+}\b ,
\]
the minimum-norm least-squares solution of \( \A\x = \b \). For a consistent system this agrees with Chapter 10's \( \x_{\min} \), by @thm-pseudoinverse-least-squares (c); for an inconsistent one it is the shortest of the minimizers of \( \norm{\A\x - \b} \), by clauses (a) and (b). One symbol, one formula, no case distinction.

::: {#exm-pseudoinverse-recovers-minimum-norm}
[Chapter 10's minimum-norm solution, recomputed]

In Chapter 10 the system
\[
x_1 + x_2 + x_3 = 3, \qquad x_1 + 2x_2 + 3x_3 = 7
\]
was solved for its shortest solution by intersecting the solution line with \( \nul(\A)^{\perp} \), as @thm-minimum-norm-solution prescribes. Recompute \( \x_{\min} \) as \( \A^{+}\b \).
:::

::: {.solution}
Here
\[
\A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \end{pmatrix}, \qquad \b = (3, 7) .
\]
The two rows are independent, so \( \rank\A = 2 = m \) and @thm-pseudoinverse-properties (e) gives \( \A^{+} = \A\tp(\A\A\tp)^{-1} \). Now
\[
\A\A\tp = \begin{pmatrix} 3 & 6 \\ 6 & 14 \end{pmatrix},
\qquad
(\A\A\tp)^{-1} = \frac16\begin{pmatrix} 14 & -6 \\ -6 & 3 \end{pmatrix},
\]
since the determinant is \( 42 - 36 = 6 \). Therefore
\[
\A^{+} = \frac16\begin{pmatrix} 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{pmatrix}\begin{pmatrix} 14 & -6 \\ -6 & 3 \end{pmatrix}
= \frac16\begin{pmatrix} 8 & -3 \\ 2 & 0 \\ -4 & 3 \end{pmatrix},
\]
and
\[
\x_{\min} = \A^{+}\b = \frac16\begin{pmatrix} 24 - 21 \\ 6 + 0 \\ -12 + 21 \end{pmatrix} = \Bigl(\tfrac12, 1, \tfrac32\Bigr) .
\]
This is exactly the answer Chapter 10 obtained by hand, and \( \norm{\x_{\min}}^2 = \tfrac14 + 1 + \tfrac94 = \tfrac72 \) as before. The system is consistent — \( \tfrac12 + 1 + \tfrac32 = 3 \) and \( \tfrac12 + 2 + \tfrac92 = 7 \) — so no projection was needed; what the pseudoinverse did was replace a geometric argument by one matrix product.
:::

The next example is the case no formula of Chapter 10 reaches: the system is inconsistent **and** underdetermined at the same time.

::: {#exm-pseudoinverse-neither-formula}
[Inconsistent and underdetermined at once]

Find \( \x_{\min} \) for
\[
\A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}, \qquad \b = (1, 3) ,
\]
and verify directly that it minimizes the residual and is the shortest minimizer.
:::

::: {.solution}
The system reads \( x_1 + x_2 = 1 \) and \( x_1 + x_2 = 3 \), so it is inconsistent; and \( \nul(\A) = \Span\bigl((1, -1)\bigr) \ne \{\0\} \), so the columns are dependent. Neither \( \A^{-1} \) nor \( (\A^{*}\A)^{-1}\A^{*} \) exists. From @exm-pseudoinverse-first-examples (e), \( \A^{+} = \tfrac14\begin{psmallmatrix} 1 & 1 \\ 1 & 1\end{psmallmatrix} \), so
\[
\x_{\min} = \A^{+}\b = \frac14(1 + 3, 1 + 3) = (1, 1) .
\]

*Check.* \( \col(\A) = \Span\bigl((1, 1)\bigr) \), and the projection of \( \b = (1, 3) \) onto it is \( \tfrac{1 + 3}{2}(1, 1) = (2, 2) \). Indeed \( \A(1, 1) = (2, 2) \), so the residual is \( \b - (2, 2) = (-1, 1) \), of squared length \( 2 \) — the smallest possible. The least-squares solutions are all \( \x \) with \( x_1 + x_2 = 2 \), that is \( (1, 1) + t(1, -1) \), and
\[
\norm{(1, 1) + t(1, -1)}^2 = 2 + 2t^2 ,
\]
which is smallest exactly at \( t = 0 \). So \( (1, 1) \) is the shortest least-squares solution, as @thm-pseudoinverse-least-squares (b) predicts.
:::

## The block criterion, finished

Section 6 tested a block matrix for positive definiteness one block at a time, and had to assume the corner block invertible: the Schur complement \( \M/\A = \C - \B^{*}\A^{-1}\B \) is meaningless otherwise. The pseudoinverse removes that hypothesis, and the promise Section 6 made is paid here.

::: {#prp-block-psd-general}
[The Semidefinite Block Criterion]

Let \( \A \in M_k(F) \) and \( \C \in M_l(F) \) be self-adjoint and put
\[
\M = \begin{pmatrix} \A & \B \\ \B^{*} & \C \end{pmatrix} \in M_{k+l}(F) .
\]
Then \( \M \succeq 0 \) if and only if \( \A \succeq 0 \), every column of \( \B \) lies in \( \col(\A) \), and \( \C - \B^{*}\A^{+}\B \succeq 0 \).
:::

::: {.idea}
Section 6 cleared the corner with the shear \( \begin{psmallmatrix} \I & -\A^{-1}\B \\ \0 & \I\end{psmallmatrix} \). Write \( \A^{+} \) in place of \( \A^{-1} \) and the same shear still clears it — but only because \( \A\A^{+} \) is the projection onto \( \col(\A) \), so \( \A\A^{+}\B = \B \) exactly when the columns of \( \B \) are already in \( \col(\A) \). That condition is not a technicality: it is what the two-sided test forces.
:::

::: {.proof}
Suppose first that \( \M \succeq 0 \). Taking \( \v = (\x, \0) \) gives \( \inner{\A\x}{\x} \ge 0 \), so \( \A \succeq 0 \). For the column condition, let \( \x \in \nul(\A) \) and \( \y \in F^l \), and put \( \v_t = (t\x, \y) \) for \( t \in \nR \). Then
\[
\inner{\M\v_t}{\v_t} = t^2\inner{\A\x}{\x} + 2t\,\Re\inner{\B\y}{\x} + \inner{\C\y}{\y} = 2t\,\Re\inner{\B\y}{\x} + \inner{\C\y}{\y} ,
\]
using \( \A\x = \0 \). A real affine function of \( t \) that is non-negative for every \( t \) has zero slope, so \( \Re\inner{\B\y}{\x} = 0 \) for all \( \y \); replacing \( \y \) by \( i\y \) over \( \nC \) kills the imaginary part too. Hence \( \inner{\B\y}{\x} = 0 \) for every \( \y \), that is \( \B^{*}\x = \0 \). So \( \nul(\A) \subseteq \nul(\B^{*}) \), and taking orthogonal complements with @thm-four-subspaces-orthogonal gives \( \col(\B) \subseteq \col(\A) \), since \( \A \) is self-adjoint.

Now assume \( \A \succeq 0 \) and \( \col(\B) \subseteq \col(\A) \); we show \( \M \succeq 0 \) is equivalent to \( \C - \B^{*}\A^{+}\B \succeq 0 \), which finishes both directions. By @thm-pseudoinverse-properties (a), \( \A\A^{+} = P_{\col(\A)} \), so \( \A\A^{+}\B = \B \); taking adjoints, and using that \( \A \) and \( \A^{+} \) are self-adjoint (@thm-pseudoinverse-properties (c)), also \( \B^{*}\A^{+}\A = \B^{*} \). Put
\[
\S = \begin{pmatrix} \I_k & -\A^{+}\B \\ \0 & \I_l \end{pmatrix},
\]
which is invertible. Multiplying out and cancelling with the two identities just recorded,
\[
\S^{*}\M\S = \begin{pmatrix} \A & \0 \\ \0 & \C - \B^{*}\A^{+}\B \end{pmatrix} .
\]
Since \( \S \) is invertible, @prp-congruence-positivity (a) applied to \( \S \) and then to \( \S^{-1} \) shows that \( \M \succeq 0 \) if and only if \( \S^{*}\M\S \succeq 0 \), and a block diagonal matrix is positive semidefinite exactly when both blocks are. This shows the three conditions together are equivalent to \( \M \succeq 0 \).
:::

The column condition cannot be dropped. With
\[
\A = \begin{pmatrix} 2 & 0 \\ 0 & 0\end{pmatrix}, \qquad \C = (1),
\]
the choice \( \B = (1, 0)\tp \) has its column in \( \col(\A) \) and gives \( \C - \B^{*}\A^{+}\B = (\tfrac12) \succeq 0 \), so \( \M \succeq 0 \). The choice \( \B = (0, 1)\tp \) does not, and there \( \M \) is not positive semidefinite even though \( \A \succeq 0 \), \( \C \succeq 0 \) and \( \B^{*}\A^{+}\B = \0 \) makes the third condition hold trivially.

## Exercises

### A. Check your understanding

:::: {#exr-pseudoinverse-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define \( \A^{+} \) in terms of a singular value decomposition of \( \A \) (@thm-svd), and say what size it is.
2. State the four Penrose conditions, and say what @thm-penrose-conditions asserts about them.
3. What are \( \A\A^{+} \) and \( \A^{+}\A \)? Under what condition on \( \A \) is the second of them \( \I_n \)?
4. Write down \( \0^{+} \) for the zero matrix \( \0 \in M_{m \times n}(F) \), and \( \A^{+} \) for an invertible \( \A \).
5. True or false: \( (\A\B)^{+} = \B^{+}\A^{+} \) whenever the product \( \A\B \) is defined. Justify your answer.
:::
::::

::: {.solution}
(a) If \( \A = \U\vSigma\V^{*} \), then \( \A^{+} = \V\vSigma^{+}\U^{*} \), where \( \vSigma^{+} \in M_{n \times m}(F) \) has \( \sigma_i^{-1} \) in the \( (i, i) \) place for each \( \sigma_i > 0 \) and zeros elsewhere. It is \( n \times m \), the transpose of the shape of \( \A \).

(b) \( \A\X\A = \A \), \( \X\A\X = \X \), \( (\A\X)^{*} = \A\X \), \( (\X\A)^{*} = \X\A \). The theorem says \( \A^{+} \) satisfies all four and is the only matrix that does; so the four conditions may be used as a definition, and checking them is enough to identify a candidate.

(c) \( \A\A^{+} = P_{\col(\A)} \) and \( \A^{+}\A = P_{\col(\A^{*})} \) (@thm-pseudoinverse-properties (a)). The second is \( \I_n \) exactly when \( \col(\A^{*}) = F^n \), that is when \( \rank\A = n \), that is when the columns of \( \A \) are independent.

(d) \( \0^{+} = \0 \in M_{n \times m}(F) \); \( \A^{+} = \A^{-1} \) when \( \A \) is invertible.

(e) False. With \( \A = \begin{psmallmatrix} 1 & 1 \\ 0 & 0\end{psmallmatrix} \) and \( \B = \begin{psmallmatrix} 1 & 0 \\ 0 & 0\end{psmallmatrix} \) the two sides are \( \begin{psmallmatrix} 1 & 0 \\ 0 & 0\end{psmallmatrix} \) and \( \tfrac12\begin{psmallmatrix} 1 & 0 \\ 0 & 0\end{psmallmatrix} \), as computed in the warning above.
:::

### B. Practice

:::: {#exr-pseudoinverse-b1}
[B1: Four pseudoinverses]

Compute \( \A^{+} \) for each of the following, stating which method you used.

::: {.enumerate options="label=(\alph*)"}
1. \( \A = \diag(3, 0, 0, 4) \in M_4(\nR) \);
2. \( \A = (1, 2, 2)\tp \in M_{3 \times 1}(\nR) \);
3. \( \A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} \in M_2(\nR) \);
4. \( \A = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{pmatrix} \in M_{2 \times 3}(\nR) \).
:::
::::

::: {.solution}
(a) A diagonal matrix is its own singular value decomposition (@thm-svd) up to ordering, so invert the non-zero entries in place: \( \A^{+} = \diag\bigl(\tfrac13, 0, 0, \tfrac14\bigr) \).

(b) A single non-zero column, so @exm-pseudoinverse-first-examples (d) applies with \( \norm{\A}^2 = 1 + 4 + 4 = 9 \):
\[
\A^{+} = \tfrac19(1, 2, 2) \in M_{1 \times 3}(\nR) .
\]

(c) Rank one: \( \A = \u\v\tp \) with \( \u = (1, 2) \) and \( \v = (1, 2) \). Then \( \sigma_1 = \norm{\u}\,\norm{\v} = 5 \) with \( \u_1 = \u/\sqrt5 \) and \( \v_1 = \v/\sqrt5 \), so
\[
\A^{+} = \tfrac15\v_1\u_1\tp = \tfrac{1}{25}\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} .
\]
(Check: \( \A\A^{+} = \tfrac{1}{25}\begin{psmallmatrix} 5 & 10 \\ 10 & 20\end{psmallmatrix} \) is Hermitian and idempotent, and \( \A\A^{+}\A = \A \).)

(d) The rows are independent, so \( \rank\A = 2 = m \) and @thm-pseudoinverse-properties (e) gives \( \A^{+} = \A\tp(\A\A\tp)^{-1} \). Here \( \A\A\tp = \begin{psmallmatrix} 2 & 1 \\ 1 & 2\end{psmallmatrix} \) with inverse \( \tfrac13\begin{psmallmatrix} 2 & -1 \\ -1 & 2\end{psmallmatrix} \), so
\[
\A^{+} = \frac13\begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}
= \frac13\begin{pmatrix} 2 & -1 \\ -1 & 2 \\ 1 & 1 \end{pmatrix} .
\]
:::

:::: {#exr-pseudoinverse-b2}
[B2: A system that is both inconsistent and underdetermined]

Let
\[
\A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \\ 1 & 2 \end{pmatrix}, \qquad \b = (1, 4, 1) .
\]
Compute \( \A^{+} \) and \( \x_{\min} = \A^{+}\b \). Verify that \( \A\x_{\min} \) is the orthogonal projection of \( \b \) onto \( \col(\A) \), and compare \( \norm{\x_{\min}} \) with the norm of one other least-squares solution.
::::

::: {.solution}
Both columns are multiples of \( \u = (1, 2, 1) \), so \( \A = \u\v\tp \) with \( \v = (1, 2) \), and \( \rank\A = 1 \). Then \( \norm{\u}^2 = 6 \), \( \norm{\v}^2 = 5 \) and \( \sigma_1 = \sqrt{30} \), with \( \u_1 = \u/\sqrt6 \) and \( \v_1 = \v/\sqrt5 \). Hence
\[
\A^{+} = \sigma_1^{-1}\v_1\u_1\tp = \frac{1}{30}\v\u\tp = \frac{1}{30}\begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \end{pmatrix} .
\]
Therefore
\[
\x_{\min} = \A^{+}\b = \frac{1}{30}(1 + 8 + 1,\ 2 + 16 + 2) = \Bigl(\tfrac13, \tfrac23\Bigr) .
\]

*Projection.* \( \col(\A) = \Span(\u) \) and \( \inner{\b}{\u} = 1 + 8 + 1 = 10 \), so \( P_{\col(\A)}\b = \tfrac{10}{6}\u = \tfrac53(1, 2, 1) \). And \( \A\x_{\min} = \u\bigl(\v\tp\x_{\min}\bigr) = \u\bigl(\tfrac13 + \tfrac43\bigr) = \tfrac53\u \). They agree.

*Shortest.* The least-squares solutions are the \( \x \) with \( \v\tp\x = x_1 + 2x_2 = \tfrac53 \). Another one is \( \bigl(\tfrac53, 0\bigr) \), of squared norm \( \tfrac{25}{9} \), against \( \norm{\x_{\min}}^2 = \tfrac19 + \tfrac49 = \tfrac59 \). The pseudoinverse solution is shorter, as @thm-pseudoinverse-least-squares (b) requires.
:::

:::: {#exr-pseudoinverse-b3}
[B3: Checking a candidate]

Let \( \A = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{pmatrix} \) and \( \X = \dfrac13\begin{pmatrix} 2 & 1 & -1 \\ -1 & 1 & 2 \end{pmatrix} \). Verify the four Penrose conditions for \( \X \), and hence find the minimum-norm least-squares solution of \( \A\x = (1, 2, 3) \).
::::

::: {.solution}
Compute the two products first:
\[
\X\A = \frac13\begin{pmatrix} 3 & 0 \\ 0 & 3 \end{pmatrix} = \I_2,
\qquad
\A\X = \frac13\begin{pmatrix} 2 & 1 & -1 \\ 1 & 2 & 1 \\ -1 & 1 & 2 \end{pmatrix} .
\]
(P4): \( \X\A = \I_2 \) is Hermitian. (P3): \( \A\X \) is visibly symmetric. (P1): \( \A\X\A = \A(\X\A) = \A\I_2 = \A \). (P2): \( \X\A\X = \I_2\X = \X \). All four hold, so \( \X = \A^{+} \) by @thm-penrose-conditions.

Then
\[
\x_{\min} = \X(1, 2, 3) = \frac13(2 + 2 - 3,\ -1 + 2 + 6) = \Bigl(\tfrac13, \tfrac73\Bigr) .
\]
(The columns of \( \A \) are independent, so this is also \( (\A\tp\A)^{-1}\A\tp\b \), and it is the unique least-squares solution; the normal equations \( \begin{psmallmatrix} 2 & 1 \\ 1 & 2\end{psmallmatrix}\x = (3, 5) \) confirm it.)
:::

### C. Going deeper

:::: {#exr-pseudoinverse-c1}
[C1: Pseudoinverses of \( \A^{*}\A \)]

Let \( \A \in M_{m \times n}(F) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( (\A^{*}\A)^{+} = \A^{+}(\A^{+})^{*} \).
2. Deduce that \( \A^{+} = (\A^{*}\A)^{+}\A^{*} \), the formula \( (\A^{*}\A)^{-1}\A^{*} \) with the inverse replaced by the pseudoinverse.
:::

*Hint: use a singular value decomposition and reduce each identity to an identity between diagonal matrices.*
::::

::: {.solution}
Write \( \A = \U\vSigma\V^{*} \).

(a) Then \( \A^{*}\A = \V\vSigma^{*}\vSigma\V^{*} \), and \( \vSigma^{*}\vSigma \in M_n(F) \) is diagonal with entries \( \sigma_1^2, \dots, \sigma_p^2 \) followed by zeros. That display is a singular value decomposition of \( \A^{*}\A \) in the sense of @thm-svd (both outer factors are \( \V \), which is unitary, and the middle factor is diagonal with non-negative entries), so
\[
(\A^{*}\A)^{+} = \V(\vSigma^{*}\vSigma)^{+}\V^{*},
\]
where \( (\vSigma^{*}\vSigma)^{+} \) is diagonal with entries \( \sigma_i^{-2} \) for \( i \le r \) and \( 0 \) elsewhere. On the other side, \( (\A^{+})^{*} = (\V\vSigma^{+}\U^{*})^{*} = \U(\vSigma^{+})^{*}\V^{*} \), so
\[
\A^{+}(\A^{+})^{*} = \V\vSigma^{+}\U^{*}\U(\vSigma^{+})^{*}\V^{*} = \V\vSigma^{+}(\vSigma^{+})^{*}\V^{*} .
\]
The middle factor \( \vSigma^{+}(\vSigma^{+})^{*} \) is diagonal with entries \( \sigma_i^{-1}\sigma_i^{-1} = \sigma_i^{-2} \) for \( i \le r \) and \( 0 \) elsewhere, which is \( (\vSigma^{*}\vSigma)^{+} \). Hence the two sides agree.

(b) Using (a) and \( \A^{*} = \V\vSigma^{*}\U^{*} \),
\[
(\A^{*}\A)^{+}\A^{*} = \V\vSigma^{+}(\vSigma^{+})^{*}\vSigma^{*}\U^{*} .
\]
Now \( (\vSigma^{+})^{*}\vSigma^{*} = (\vSigma\vSigma^{+})^{*} = \vSigma\vSigma^{+} \), which is the \( m \times m \) diagonal matrix with \( r \) ones and then zeros; and \( \vSigma^{+} \) multiplied by it on the right is \( \vSigma^{+} \), since \( \vSigma^{+} \) has non-zero entries only in the first \( r \) columns. So the right-hand side is \( \V\vSigma^{+}\U^{*} = \A^{+} \).
:::

:::: {#exr-pseudoinverse-c2}
[C2: When the reversal rule does hold]

Let \( \A \in M_{m \times n}(F) \) with \( \rank\A = n \) and \( \B \in M_{n \times q}(F) \) with \( \rank\B = n \). Prove that
\[
(\A\B)^{+} = \B^{+}\A^{+} .
\]
*Hint: write both pseudoinverses with the formulas of @thm-pseudoinverse-properties (e) and verify the Penrose conditions for the product.*
::::

::: {.solution}
By @thm-pseudoinverse-properties (e), \( \A^{+} = (\A^{*}\A)^{-1}\A^{*} \) and \( \B^{+} = \B^{*}(\B\B^{*})^{-1} \), the two inverses existing because \( \rank\A = n \) and \( \rank\B^{*} = n \). Put
\[
\X = \B^{+}\A^{+} = \B^{*}(\B\B^{*})^{-1}(\A^{*}\A)^{-1}\A^{*} .
\]
Throughout we use \( \A^{+}\A = \I_n \) and \( \B\B^{+} = \I_n \), which the two formulas give at once.

(P1): \( (\A\B)\X(\A\B) = \A(\B\B^{+})(\A^{+}\A)\B = \A\I_n\I_n\B = \A\B \).

(P2): \( \X(\A\B)\X = \B^{+}(\A^{+}\A)(\B\B^{+})\A^{+} = \B^{+}\A^{+} = \X \).

(P3): \( (\A\B)\X = \A(\B\B^{+})\A^{+} = \A\A^{+} = \A(\A^{*}\A)^{-1}\A^{*} \), which equals its own conjugate transpose, since \( \A^{*}\A \) is Hermitian and so is its inverse.

(P4): \( \X(\A\B) = \B^{+}(\A^{+}\A)\B = \B^{+}\B = \B^{*}(\B\B^{*})^{-1}\B \), Hermitian for the same reason.

All four hold, so \( \X = (\A\B)^{+} \) by @thm-penrose-conditions.
:::

:::: {#exr-pseudoinverse-c3}
[C3: When the pseudoinverse is the adjoint]

Let \( \A \in M_{m \times n}(F) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \A^{+} = \A^{*} \) if and only if \( \A\A^{*}\A = \A \).
2. Deduce that \( \A^{+} = \A^{*} \) if and only if every non-zero singular value of \( \A \) equals \( 1 \).
3. Give an example of such an \( \A \) in \( M_2(\nR) \) which is neither unitary nor an orthogonal projection.
:::
::::

::: {.solution}
(a) \( (\Rightarrow) \) If \( \A^{+} = \A^{*} \), then (P1) reads \( \A\A^{*}\A = \A \).

\( (\Leftarrow) \) Suppose \( \A\A^{*}\A = \A \) and put \( \X = \A^{*} \). Then (P1) is the hypothesis; (P2) is \( \A^{*}\A\A^{*} = (\A\A^{*}\A)^{*} = \A^{*} \); (P3) is \( (\A\A^{*})^{*} = \A\A^{*} \), true for every \( \A \); and (P4) is \( (\A^{*}\A)^{*} = \A^{*}\A \), likewise. By @thm-penrose-conditions, \( \A^{+} = \A^{*} \).

(b) With \( \A = \U\vSigma\V^{*} \) we have \( \A^{*} = \V\vSigma^{*}\U^{*} \) and \( \A^{+} = \V\vSigma^{+}\U^{*} \). Since \( \U \) and \( \V \) are invertible, \( \A^{+} = \A^{*} \) if and only if \( \vSigma^{+} = \vSigma^{*} \), that is if and only if \( \sigma_i^{-1} = \sigma_i \) for every \( i \le r \), that is if and only if every non-zero singular value is \( 1 \) (the equation \( \sigma^2 = 1 \) with \( \sigma > 0 \) forces \( \sigma = 1 \)).

(c) Take
\[
\A = \frac{1}{\sqrt2}\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} .
\]
Then \( \A\A\tp = \begin{psmallmatrix} 1 & 0 \\ 0 & 0\end{psmallmatrix} \), so \( \A\A\tp\A = \A \) and (a) applies. Its singular values are \( 1 \) and \( 0 \), matching (b). It is not unitary, since it is singular, and not an orthogonal projection, since \( \A\tp \ne \A \). Such a matrix maps \( \col(\A^{*}) \) isometrically onto \( \col(\A) \) and sends \( \nul(\A) \) to \( \0 \): a unitary matrix on the part of the space where it is invertible, and nothing at all elsewhere.
:::
