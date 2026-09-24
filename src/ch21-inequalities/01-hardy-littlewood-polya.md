# Doubly Stochastic Maps

Chapter 17 §08 defined majorization and Chapter 19 §07 proved one half of the fact that makes it useful: a doubly stochastic matrix can only even a vector out, \( \S\y \prec \y \). The other half was promised twice. Chapter 19 §07 ended by saying that "this converse of the proposition is part of the theorem of Hardy, Littlewood and Pólya, which Chapter 21 takes up", and Chapter 19 §09 listed among its unfinished business "the theorem of Hardy, Littlewood and Pólya, that \( \x \prec \y \) exactly when \( \x = \D\y \) for a doubly stochastic \( \D \)". This section pays both. The proof builds \( \D \) out of one very simple move, repeated: average two coordinates and leave the rest alone.

**Throughout, vectors are real**, \( \x, \y \in \nR^n \), and \( \prec \) and \( \prec_w \) are Chapter 17 §08's @def-majorization. Recall \( \x^{\downarrow} \), the decreasing rearrangement, and \( \Omega_n \), the set of doubly stochastic matrices of @def-doubly-stochastic: non-negative entries, every row and every column adding up to \( 1 \). Recall also @prp-doubly-stochastic-image-majorized, the half already proved: if \( \S \in \Omega_n \) and \( \y \in \nR^n \), then \( \S\y \prec \y \).

## What is still missing

Chapter 19 got the easy direction from Birkhoff's theorem in three lines. A doubly stochastic \( \S \) is an average of permutation matrices, a permutation only rearranges \( \y \), and majorization cannot see a rearrangement; so \( \S\y \) is an average of vectors all majorized by \( \y \), and the set of such vectors is convex.

Read backwards, that argument gives nothing. It starts from a matrix and produces a majorization. We now want to start from the majorization \( \x \prec \y \), which is a list of \( n - 1 \) inequalities about sorted partial sums together with one equality of totals, and manufacture a matrix. Nothing in @def-majorization mentions a matrix, so one has to be built.

One such matrix is in fact already available. Chapter 19 §07 observed that @thm-schur-horn realizes any \( \x \prec \y \) as the diagonal of a Hermitian \( \A \) with \( \vlambda(\A) = \y^{\downarrow} \), while @lem-diagonal-doubly-stochastic-image writes that diagonal as \( \S\y^{\downarrow} \) for a doubly stochastic \( \S \); composing with the permutation matrix that sorts \( \y \) gives \( \x = \D\y \) with \( \D \in \Omega_n \). What that route does not give is any grip on \( \D \), which arrives as the squared moduli of the entries of a unitary matrix supplied by an existence theorem. The construction below builds \( \D \) by hand instead, as a product of at most \( n - 1 \) factors, each of which averages a single pair of coordinates and fixes the rest.

Here is the smallest case, done by hand, to see what a construction might look like. Let \( n = 2 \) and \( \x \prec \y \) with both decreasing, so \( x_1 + x_2 = y_1 + y_2 \) and \( x_1 \le y_1 \). Also \( x_2 \ge y_2 \), since subtracting \( x_1 \le y_1 \) from the equal totals reverses the inequality. So \( y_2 \le x_1 \le y_1 \), and \( x_1 \) is a weighted average of \( y_1 \) and \( y_2 \): if \( y_1 = y_2 \) then \( \x = \y \), and otherwise
\[
x_1 = (1 - t)y_1 + ty_2 , \qquad t = \frac{y_1 - x_1}{y_1 - y_2} \in [0, 1] .
\]
The equal totals then force \( x_2 = ty_1 + (1-t)y_2 \). In matrix form,
\[
\begin{pmatrix} x_1 \\ x_2 \end{pmatrix}
= \begin{pmatrix} 1 - t & t \\ t & 1 - t \end{pmatrix}
\begin{pmatrix} y_1 \\ y_2 \end{pmatrix} ,
\]
and the matrix is doubly stochastic. So for \( n = 2 \) and sorted vectors the converse holds, with a \( \D \) of a very special shape.

This is the same computation as @lem-horn-two-by-two, where the weights were \( c^2 \) and \( s^2 \) for a rotation and the averaged numbers were two eigenvalues. There the averaging was performed by conjugating a diagonal matrix; here it is performed on the vector directly. Both say: *any number between two others is an average of them*, and that single fact is the engine of this section.

## Averaging two coordinates

The \( 2 \times 2 \) matrix above can be planted inside \( \I_n \), at any pair of positions. That gives the move we will repeat.

*A T-transform mixes two coordinates and leaves every other coordinate alone.*

::: {#def-t-transform}
[T-transform]

Let \( n \ge 2 \), let \( 1 \le j < k \le n \), and let \( \Q \in M_n(\nR) \) be the permutation matrix (@def-permutation-matrix) of the transposition interchanging \( j \) and \( k \). For a real number \( t \) with \( 0 \le t \le 1 \), the matrix
\[
\T = (1 - t)\I + t\Q
\]
is called a **T-transform**, and we say that it **acts on the pair** \( \{j, k\} \).
:::

In words: \( \T \) is the convex combination, with weights \( 1 - t \) and \( t \), of doing nothing and swapping two coordinates. Applied to a vector,
\[
\begin{aligned}
(\T\y)_j &= (1 - t)y_j + ty_k , \\
(\T\y)_k &= ty_j + (1 - t)y_k , \\
(\T\y)_i &= y_i \qquad (i \ne j, k) .
\end{aligned}
\]{#eq-t-transform-action}
The two moved entries are averages of the old \( y_j \) and \( y_k \), with the **same** pair of weights used in both slots, exchanged. In particular \( (\T\y)_j + (\T\y)_k = y_j + y_k \): a T-transform conserves the total, and indeed conserves the total of the pair it touches.

The first thing to check is that these matrices belong in the discussion at all.

::: {#prp-t-transform-doubly-stochastic}
[T-transforms Are Doubly Stochastic]

Every T-transform lies in \( \Omega_n \).
:::

::: {.proof}
Let \( \T = (1-t)\I + t\Q \) with \( 0 \le t \le 1 \), and let \( \{j, k\} \) be the pair \( \Q \) interchanges. In the two positions \( (j,j) \) and \( (k,k) \) the entry of \( \T \) is \( 1 - t \), in the two positions \( (j,k) \) and \( (k,j) \) it is \( t \), in the remaining \( n - 2 \) diagonal positions both \( \I \) and \( \Q \) carry a \( 1 \), so the entry is \( 1 \), and everywhere else it is \( 0 \). Each entry is therefore \( 1 \), \( 1 - t \), \( t \) or \( 0 \), hence non-negative, since \( t \ge 0 \) and \( 1 - t \ge 0 \). A permutation matrix has exactly one \( 1 \) in each row and each column and zeros elsewhere (the remark after @def-permutation-matrix), so \( \Q\1 = \1 \) and \( \1\tp\Q = \1\tp \); the same is true of \( \I \), which is the permutation matrix of the identity permutation. Hence
\[
\T\1 = (1-t)\1 + t\1 = \1 , \qquad \1\tp\T = (1-t)\1\tp + t\1\tp = \1\tp ,
\]
which says that every row and every column of \( \T \) adds up to \( 1 \). By @def-doubly-stochastic, \( \T \in \Omega_n \).
:::

::: {#exm-t-transform-basic}
[Three T-transforms, and two impostors]

Take \( n = 3 \) and \( \y = (6, 3, 0) \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \T\y \) for the T-transform on \( \{1, 3\} \) with \( t = \tfrac13 \), and for the ones with \( t = 0 \) and \( t = 1 \).
2. Is the matrix \( \tfrac12(\I + \P) \), with \( \P \) the permutation matrix of the \( 3 \)-cycle \( 1 \mapsto 2 \mapsto 3 \mapsto 1 \), a T-transform?
3. Is \( -\I + 2\Q \), with \( \Q \) the transposition matrix of \( \{1, 2\} \), a T-transform?
:::
:::

::: {.solution}
(a) With \( j = 1 \), \( k = 3 \) and \( t = \tfrac13 \), @eq-t-transform-action gives
\[
\T\y = \bigl(\tfrac23 \cdot 6 + \tfrac13 \cdot 0,\ 3,\ \tfrac13 \cdot 6 + \tfrac23 \cdot 0\bigr) = (4, 3, 2) .
\]
At \( t = 0 \), \( \T = \I \) and \( \T\y = \y \); at \( t = 1 \), \( \T = \Q \) and \( \T\y = (0, 3, 6) \). So the endpoints of the family are "do nothing" and "swap".

(b) No. It is doubly stochastic, by the computation in @prp-t-transform-doubly-stochastic with \( \Q \) replaced by \( \P \), but @def-t-transform asks for the permutation matrix of a **transposition**. Concretely, \( \tfrac12(\I + \P) \) changes all three coordinates of \( \y \), while a T-transform fixes at least \( n - 2 \) of them.

(c) No: \( t = 2 \) is outside \( [0, 1] \), and the matrix has the entry \( -1 \) in position \( (1,1) \), so it is not even doubly stochastic. Applied to \( \y \) it gives \( (0, 9, 0) \), whose first two entries are further apart than \( 6 \) and \( 3 \): with \( t \notin [0,1] \) the "average" is not between the two numbers, and the move spreads rather than evens.
:::

::: {.check}
Let \( \T \) be the T-transform on \( \{1, 2\} \) with \( t = \tfrac14 \), and let \( \y = (8, 4, 1) \). Compute \( \T\y \), and verify \( \T\y \prec \y \) directly from @def-majorization.
:::

::: {.solution}
\( (\T\y)_1 = \tfrac34\cdot 8 + \tfrac14\cdot 4 = 7 \) and \( (\T\y)_2 = \tfrac14\cdot 8 + \tfrac34\cdot 4 = 5 \), so \( \T\y = (7, 5, 1) \). Both vectors are decreasing with total \( 13 \), and the running totals are \( 7, 12 \) against \( 8, 12 \). Since \( 7 \le 8 \) and \( 12 \le 12 \), (M1) holds, and (M2) is the equal totals. So \( \T\y \prec \y \), as @prp-doubly-stochastic-image-majorized already promised, since \( \T \in \Omega_n \).
:::

::: {.warning}
**A product of T-transforms is usually not a T-transform.** T-transforms are doubly stochastic, and so are their products (this is checked inside the proof of the main theorem below), but the product of two of them can move every coordinate. Averaging coordinates \( 1 \) and \( 2 \), then coordinates \( 2 \) and \( 3 \), changes all three. The theorem below produces a product, not a single T-transform.
:::

## One averaging step

Now the engine. Given \( \x \prec \y \), we want to push \( \y \) toward \( \x \) by one T-transform, and we want a measure of progress that cannot stall. The measure is the number of coordinates in which the two vectors already agree.

::: {#lem-t-transform-step}
[One Averaging Step]

Let \( \x, \y \in \nR^n \) be **decreasing**, with \( \x \prec \y \) and \( \x \ne \y \). Then there is a T-transform \( \T \) such that \( \y' = \T\y \) satisfies

::: {.enumerate options="label=(\alph*)"}
1. \( \y' \) is decreasing;
2. \( \x \prec \y' \);
3. \( y'_i = x_i \) for strictly more indices \( i \) than \( y_i = x_i \) does.
:::
:::

::: {.idea}
Both vectors are sorted, so compare them entry by entry. Somewhere \( \y \) is too big and somewhere it is too small. Let \( j \) be the **last** place where \( \y \) is too big and \( k \) the **first** place after \( j \) where it is too small; between them the two vectors already agree. Averaging coordinates \( j \) and \( k \) moves \( y_j \) down and \( y_k \) up by the same amount, and we move by exactly as much as the tighter of the two deficits allows, so that one of the two positions lands on \( \x \) exactly. Two things then need checking, and they are not equally hard. The partial sums are the easy one: the only ones that drop are those between \( j \) and \( k \), and they have slack at least \( y_j - x_j \) to give away, while we give away no more than that. The delicate one is that \( \y' \) must come out **decreasing**, since otherwise the lemma cannot be applied to it again; that is what taking \( j \) last buys, because it makes the entries between \( j \) and \( k \) agree with \( \x \)'s.
:::

::: {.proof}
Write \( X_m = x_1 + \dots + x_m \) and \( Y_m = y_1 + \dots + y_m \), with \( X_0 = Y_0 = 0 \). Since both vectors are decreasing, @def-majorization says \( X_m \le Y_m \) for \( m = 1, \dots, n-1 \) and \( X_n = Y_n \).

**Step 1: the two indices.** Some index has \( y_i > x_i \): otherwise \( y_i \le x_i \) for every \( i \), and since \( \x \ne \y \) at least one inequality is strict, so \( Y_n < X_n \), contradicting \( X_n = Y_n \). Let \( j \) be the **largest** index with \( y_j > x_j \).

Next, some index \( i > j \) has \( y_i < x_i \). Suppose not. By the choice of \( j \), \( y_i \le x_i \) for every \( i > j \); so \( y_i = x_i \) for every \( i > j \), and subtracting these from \( X_n = Y_n \) gives \( X_j = Y_j \). Then
\[
X_{j-1} = X_j - x_j > Y_j - y_j = Y_{j-1} ,
\]
because \( x_j < y_j \). For \( j \ge 2 \) this contradicts \( X_{j-1} \le Y_{j-1} \), and for \( j = 1 \) it reads \( 0 > 0 \), which is false. So we may let \( k \) be the **smallest** index with \( k > j \) and \( y_k < x_k \).

By the maximality of \( j \) we have \( y_i \ge x_i \) for \( j < i < k \), and by the minimality of \( k \) we have \( y_i \le x_i \) there. Hence
\[
y_i = x_i \qquad (j < i < k) .
\tag{$\ast$}
\]

**Step 2: the transform.** Put
\[
\delta = \min\{\,y_j - x_j,\ x_k - y_k\,\} > 0 .
\]
Since \( \x \) is decreasing and \( j < k \), \( x_j \ge x_k \), so
\[
y_j > x_j \ge x_k > y_k ,
\]
and in particular \( y_j - y_k > 0 \). Also \( \delta \le y_j - x_j \le y_j - y_k \), using \( x_j \ge x_k > y_k \). So
\[
t = \frac{\delta}{y_j - y_k}
\]
satisfies \( 0 < t \le 1 \), and @def-t-transform gives a T-transform \( \T \) acting on \( \{j, k\} \) with this \( t \). By @eq-t-transform-action,
\[
y'_j = y_j - t(y_j - y_k) = y_j - \delta , \qquad y'_k = y_k + \delta ,
\]
and \( y'_i = y_i \) for every other \( i \).

**Step 3: (c), the count.** By the choice of \( \delta \), either \( \delta = y_j - x_j \), and then \( y'_j = x_j \); or \( \delta = x_k - y_k \), and then \( y'_k = x_k \). So \( \y' \) agrees with \( \x \) in at least one of the positions \( j, k \). Neither position agreed before, since \( y_j > x_j \) and \( y_k < x_k \). Every other position is untouched. Hence the number of agreements strictly increases.

**Step 4: (a), the sorted order.** Only positions \( j \) and \( k \) change, and \( \delta > 0 \) lowers \( y_j \) and raises \( y_k \). From \( \delta \le y_j - x_j \) and \( \delta \le x_k - y_k \),
\[
y'_j \ge x_j , \qquad y'_k \le x_k .
\]
If \( j \ge 2 \), then \( y'_{j-1} = y_{j-1} \ge y_j > y'_j \). If \( j + 1 < k \), then \( y'_{j+1} = y_{j+1} = x_{j+1} \) by \( (\ast) \), and \( x_{j+1} \le x_j \le y'_j \). If \( j + 1 = k \), then \( y'_{j+1} = y'_k \le x_k \le x_j \le y'_j \). Symmetrically, if \( k - 1 > j \) then \( y'_{k-1} = x_{k-1} \ge x_k \ge y'_k \), and if \( k \le n - 1 \) then \( y'_{k+1} = y_{k+1} \le y_k < y'_k \). Every remaining consecutive pair consists of two untouched entries of the decreasing \( \y \). So \( \y' \) is decreasing.

**Step 5: (b), the majorization.** Write \( Y'_m = y'_1 + \dots + y'_m \). Since \( \y' \) differs from \( \y \) only at \( j \) and \( k \), by \( -\delta \) and \( +\delta \),
\[
Y'_m = \begin{cases} Y_m - \delta & (j \le m \le k - 1), \\ Y_m & (\text{otherwise}). \end{cases}
\]
In particular \( Y'_n = Y_n = X_n \), which is (M2). For \( m < j \) and for \( m \ge k \) we have \( Y'_m = Y_m \ge X_m \), which is (M1) there. For \( j \le m \le k - 1 \), the identity \( (\ast) \) gives \( y_i = x_i \) for \( j < i \le m \), hence
\[
Y_m - X_m = Y_j - X_j .
\]
Now \( Y_j - X_j = (Y_{j-1} - X_{j-1}) + (y_j - x_j) \ge y_j - x_j \ge \delta \), using \( Y_{j-1} \ge X_{j-1} \) (which is (M1), or \( 0 \ge 0 \) when \( j = 1 \)) and the definition of \( \delta \). Therefore
\[
Y'_m - X_m = (Y_m - X_m) - \delta = (Y_j - X_j) - \delta \ge 0 ,
\]
which is (M1) at \( m \). So \( \x \prec \y' \). This proves the lemma.
:::

The choice of the two indices is the only delicate part, and it is worth saying why the obvious alternative fails, and where. Suppose \( j \) were taken as the *smallest* index with \( y_j > x_j \), keeping \( k \) as the smallest index after \( j \) with \( y_k < x_k \). Step 5 would survive: the minimality of \( k \) still gives \( y_i \ge x_i \) for \( j < i < k \), so the slack \( Y_m - X_m \) is non-decreasing on \( j \le m \le k - 1 \) instead of constant, and it is therefore at least its value \( Y_j - X_j \ge y_j - x_j \ge \delta \) at \( m = j \). What breaks is Step 4. The entries strictly between \( j \) and \( k \) need no longer agree with \( \x \)'s, and lowering \( y_j \) by \( \delta \) can push it below \( y_{j+1} \), so that \( \y' \) comes out unsorted and @lem-t-transform-step cannot be applied to it a second time. Take \( \x = (5, 5, 0) \) and \( \y = (6, 6, -2) \), both decreasing, with \( \x \prec \y \) since \( 5 \le 6 \), \( 10 \le 12 \) and both totals are \( 10 \). Choosing \( j \) smallest gives \( j = 1 \) and \( k = 3 \), so \( \delta = \min\{6 - 5,\ 0 - (-2)\} = 1 \) and \( \y' = (5, 6, -1) \), which is not decreasing; the rule of the lemma gives \( j = 2 \) instead, and \( \y' = (6, 5, -1) \), which is. Taking \( j \) last and \( k \) first after it makes the interval between them a stretch where the two vectors already coincide, and that stretch is what protects the order.

## The theorem

::: {#thm-hardy-littlewood-polya}
[Hardy–Littlewood–Pólya Theorem]

Let \( \x, \y \in \nR^n \). Then
\[
\x \prec \y \quad\Longleftrightarrow\quad \x = \D\y \ \text{ for some } \D \in \Omega_n .
\]
Moreover, if \( \x \) and \( \y \) are both decreasing, \( \D \) may be taken to be a product of at most \( n - 1 \) T-transforms.
:::

::: {.idea}
\( (\Leftarrow) \) is Chapter 19's @prp-doubly-stochastic-image-majorized and needs nothing new.

For \( (\Rightarrow) \), sort both vectors first, since neither side of the equivalence sees the order. Then count agreements. @lem-t-transform-step raises that count by at least one, keeps both hypotheses alive, and therefore may be applied again; the count is at most \( n \), so the process stops, at \( \y \) turned into \( \x \). The bound \( n - 1 \) comes from noticing that the count can never be exactly \( n - 1 \): two vectors with equal totals that agree in all but one coordinate agree in that one too.
:::

::: {.proof}
\( (\Leftarrow) \) If \( \x = \D\y \) with \( \D \in \Omega_n \), then \( \x \prec \y \) by @prp-doubly-stochastic-image-majorized.

\( (\Rightarrow) \) Suppose \( \x \prec \y \).

**Step 1: the decreasing case.** Assume first that \( \x \) and \( \y \) are both decreasing. For \( \u, \v \in \nR^n \) write \( \operatorname{dis}(\u, \v) \) for the number of indices \( i \) with \( u_i \ne v_i \). We claim:

::: {.claim}
If \( \x \) and \( \y \) are decreasing with \( \x \prec \y \) and \( d = \operatorname{dis}(\x, \y) \), then \( \x = \T_r\cdots\T_1\y \) for some T-transforms \( \T_1, \dots, \T_r \) with \( r = 0 \) if \( d = 0 \), and \( r \le d - 1 \) otherwise.

::: {.proof}
First, \( d \ne 1 \): if \( \x \) and \( \y \) agreed in all indices but one, say \( i_0 \), then subtracting those \( n-1 \) equalities from the equal totals (M2) would give \( x_{i_0} = y_{i_0} \) too, so \( d = 0 \). We induct on \( d \).

If \( d = 0 \) then \( \x = \y \), and the empty product, \( r = 0 \), works. Let \( d \ge 2 \), and assume the claim for every smaller value. By @lem-t-transform-step there is a T-transform \( \T_1 \) with \( \y' = \T_1\y \) decreasing, \( \x \prec \y' \) and \( d' = \operatorname{dis}(\x, \y') \le d - 1 \). If \( d' = 0 \), then \( \x = \T_1\y \) and \( r = 1 \le d - 1 \). Otherwise \( d' \ge 2 \), since \( d' \ne 1 \) by the first paragraph applied to \( \x \) and \( \y' \); the inductive hypothesis gives \( \x = \T_r\cdots\T_2\y' \) with \( r - 1 \le d' - 1 \), so \( r \le d' \le d - 1 \). This proves the claim.
:::
:::

Since \( d \le n \), the claim gives \( r \le d - 1 \le n - 1 \) in every case. This proves the "moreover" clause.

**Step 2: products stay doubly stochastic.** If \( \A, \B \in \Omega_n \), then \( \A\B \) has non-negative entries, and \( \A\B\1 = \A\1 = \1 \), \( \1\tp\A\B = \1\tp\B = \1\tp \); so \( \A\B \in \Omega_n \) by @def-doubly-stochastic. By induction, any finite product of doubly stochastic matrices is doubly stochastic. With @prp-t-transform-doubly-stochastic, the matrix \( \D_0 = \T_r\cdots\T_1 \) of Step 1 lies in \( \Omega_n \).

**Step 3: the general case.** Let \( \x \prec \y \) be arbitrary. Majorization sees only rearrangements (the remark after @def-majorization), so \( \x^{\downarrow} \prec \y^{\downarrow} \), and Step 1 gives \( \D_0 \in \Omega_n \) with \( \x^{\downarrow} = \D_0\y^{\downarrow} \). Choose permutations \( \sigma, \tau \in S_n \) with \( \y^{\downarrow} = \P_\sigma\y \) and \( \x = \P_\tau\x^{\downarrow} \); these exist because \( \y^{\downarrow} \) is a rearrangement of \( \y \) and \( \x \) of \( \x^{\downarrow} \). Each \( \P_\sigma \) is doubly stochastic, having exactly one \( 1 \) in each row and each column and zeros elsewhere (the remark after @def-permutation-matrix), so by Step 2
\[
\D = \P_\tau\D_0\P_\sigma \in \Omega_n , \qquad \D\y = \P_\tau\D_0\y^{\downarrow} = \P_\tau\x^{\downarrow} = \x .
\]
This proves the theorem.
:::

Two remarks on what the theorem does and does not say. It converts a family of \( n - 1 \) inequalities and one equality into a single algebraic identity \( \x = \D\y \), and an identity is much easier to feed into another argument, as the next section does, one row of \( \D \) at a time. And the \( n - 1 \) in the "moreover" clause is sharp; @exr-hardy-littlewood-polya-c3 exhibits a pair needing that many.

::: {.remark}
The word **decreasing** in the "moreover" clause is not decoration. For \( \y = (6, 4, 2, 0) \) and the unsorted \( \x = (\tfrac32, 1, \tfrac92, 5) \) we have \( \x \prec \y \), since \( \x^{\downarrow} = (5, \tfrac92, \tfrac32, 1) \) has running totals \( 5, \tfrac{19}2, 11 \) against \( 6, 10, 12 \) and both totals are \( 12 \); yet no product of three T-transforms equals \( \x \), since for each of the finitely many choices of the three pairs the best the three parameters can do still misses it. Four transforms suffice: the transforms on \( \{1,2\} \), \( \{3,4\} \), \( \{1,3\} \), \( \{2,4\} \) with \( t = \tfrac12, \tfrac12, \tfrac78, 1 \) carry \( \y \) through \( (5,5,2,0) \), \( (5,5,1,1) \) and \( (\tfrac32, 5, \tfrac92, 1) \) to \( \x \). Step 3 of the proof handles an unsorted pair with permutations instead, and a permutation matrix is a T-transform only when it is a transposition.
:::

::: {#exm-hlp-four-vector}
[Four coordinates, two transforms]

Let \( \y = (7, 5, 3, 1) \) and \( \x = (5, 5, 4, 2) \). Verify \( \x \prec \y \), run the construction of @thm-hardy-littlewood-polya, and write out the resulting \( \D \).
:::

::: {.solution}
Both vectors are decreasing with total \( 16 \), and the running totals are \( 5, 10, 14 \) for \( \x \) against \( 7, 12, 15 \) for \( \y \). So (M1) and (M2) hold and \( \x \prec \y \).

*First step.* Here \( \y - \x = (2, 0, -1, -1) \), so the only index with \( y_i > x_i \) is \( i = 1 \), giving \( j = 1 \); the smallest index above it with \( y_i < x_i \) is \( k = 3 \). Then
\[
\delta = \min\{7 - 5,\ 4 - 3\} = 1 , \qquad t = \frac{1}{7 - 3} = \tfrac14 ,
\]
and \( \T_1 \) is the T-transform on \( \{1, 3\} \) with \( t = \tfrac14 \):
\[
\y' = \T_1\y = \bigl(\tfrac34\cdot 7 + \tfrac14\cdot 3,\ 5,\ \tfrac14\cdot 7 + \tfrac34\cdot 3,\ 1\bigr) = (6, 5, 4, 1) .
\]
Now \( \y' \) agrees with \( \x \) in positions \( 2 \) and \( 3 \), where before it agreed only in position \( 2 \).

*Second step.* \( \y' - \x = (1, 0, 0, -1) \), so \( j = 1 \) and \( k = 4 \), with \( \delta = \min\{1, 1\} = 1 \) and \( t = 1/(6 - 1) = \tfrac15 \). The T-transform \( \T_2 \) on \( \{1, 4\} \) gives
\[
\T_2\y' = \bigl(\tfrac45\cdot 6 + \tfrac15\cdot 1,\ 5,\ 4,\ \tfrac15\cdot 6 + \tfrac45\cdot 1\bigr) = (5, 5, 4, 2) = \x .
\]
Two transforms, and \( 2 \le n - 1 = 3 \).

*The matrix.* Multiplying \( \T_2\T_1 \) row by row,
\[
\D = \T_2\T_1 = \begin{pmatrix}
\tfrac35 & 0 & \tfrac15 & \tfrac15 \\[2pt]
0 & 1 & 0 & 0 \\[2pt]
\tfrac14 & 0 & \tfrac34 & 0 \\[2pt]
\tfrac3{20} & 0 & \tfrac1{20} & \tfrac45
\end{pmatrix} .
\]
Every row adds up to \( 1 \), and so does every column: the first is \( \tfrac35 + \tfrac14 + \tfrac3{20} = \tfrac{12 + 5 + 3}{20} = 1 \), the third is \( \tfrac15 + \tfrac34 + \tfrac1{20} = \tfrac{4 + 15 + 1}{20} = 1 \), and the second and fourth are visibly \( 1 \). Finally
\[
\D\y = \bigl(\tfrac{21 + 3 + 1}{5},\ 5,\ \tfrac{7 + 9}{4},\ \tfrac{21 + 3 + 16}{20}\bigr) = (5, 5, 4, 2) = \x .
\]
Note that \( \D \) is not a T-transform: it moves three of the four coordinates.
:::

::: {.warning}
**The matrix \( \D \) is far from unique, and "doubly stochastic" cannot be relaxed to "row-stochastic".** For \( \y = (2, 1, 0) \) and \( \x = (1, 1, 1) \), both
\[
\D_1 = \tfrac13\J , \qquad
\D_2 = \begin{pmatrix} 0 & 1 & 0 \\ \tfrac12 & 0 & \tfrac12 \\ \tfrac12 & 0 & \tfrac12 \end{pmatrix}
\]
are doubly stochastic with \( \D_i\y = \x \). And if only the **rows** are required to add up to \( 1 \), the conclusion fails: with \( \y = (1, 0) \) and the row-stochastic \( \S = \begin{psmallmatrix} 1 & 0 \\ 1 & 0 \end{psmallmatrix} \), \( \S\y = (1, 1) \), whose total is \( 2 \ne 1 \), so \( \S\y \not\prec \y \). The column condition is what enforces the equal totals.
:::

## Majorization as a polytope

Birkhoff's theorem turns the doubly stochastic matrix of @thm-hardy-littlewood-polya into an average of permutations, and the statement becomes geometric.

::: {#cor-majorization-convex-hull}
[Majorization Is Membership in a Permutation Polytope]

Let \( \x, \y \in \nR^n \). Then
\[
\x \prec \y \quad\Longleftrightarrow\quad \x \in \conv\{\P_\sigma\y : \sigma \in S_n\} .
\]
:::

::: {.proof}
\( (\Rightarrow) \) By @thm-hardy-littlewood-polya, \( \x = \D\y \) with \( \D \in \Omega_n \). By @thm-birkhoff, \( \D \in \conv\{\P_\sigma : \sigma \in S_n\} \), so by @thm-convex-hull-combinations, \( \D = \sum_{i=1}^{m}t_i\P_{\sigma_i} \) with \( t_i \ge 0 \) and \( \sum_i t_i = 1 \). Hence \( \x = \sum_i t_i\P_{\sigma_i}\y \), a convex combination of the vectors \( \P_\sigma\y \), which lies in their convex hull by @thm-convex-hull-combinations.

\( (\Leftarrow) \) By @thm-convex-hull-combinations, \( \x = \sum_i t_i\P_{\sigma_i}\y \) with \( (t_1, \dots, t_m) \) a list of non-negative weights adding up to \( 1 \). Put \( \D = \sum_i t_i\P_{\sigma_i} \). Its entries are non-negative, and \( \D\1 = \sum_i t_i\1 = \1 \), \( \1\tp\D = \1\tp \), so \( \D \in \Omega_n \) and \( \x = \D\y \). By @prp-doubly-stochastic-image-majorized, \( \x \prec \y \).
:::

The set \( \conv\{\P_\sigma\y\} \) is the **permutation polytope** of \( \y \): the convex hull of the \( n! \) rearrangements of \( \y \). It lies in the affine subspace where the coordinate sum equals \( \sum_i y_i \), so its dimension is at most \( n - 1 \). For \( n = 3 \) and distinct entries it is a hexagon.

\begin{center}
\begin{tikzpicture}[scale=1.5, lab/.style={font=\footnotesize},
                    dot/.style={circle, fill, inner sep=1.2pt}]
  \coordinate (a) at (1.414,0);
  \coordinate (b) at (0.707,1.2247);
  \coordinate (c) at (-0.707,1.2247);
  \coordinate (d) at (-1.414,0);
  \coordinate (e) at (-0.707,-1.2247);
  \coordinate (f) at (0.707,-1.2247);
  \fill[gray!14] (a) -- (b) -- (c) -- (d) -- (e) -- (f) -- cycle;
  \draw[very thick] (a) -- (b) -- (c) -- (d) -- (e) -- (f) -- cycle;
  \draw[thick, dashed] (0.3535,0.6124) -- (-0.3535,0.6124) -- (-0.707,0)
      -- (-0.3535,-0.6124) -- (0.3535,-0.6124) -- (0.707,0) -- cycle;
  \foreach \p in {(a),(b),(c),(d),(e),(f)} \node[dot] at \p {};
  \node[dot] at (0,0) {};
  \node[lab, right] at (1.45,0) {$(3,1,2)$};
  \node[lab, above right] at (0.72,1.25) {$(2,1,3)$};
  \node[lab, above left] at (-0.72,1.25) {$(1,2,3)$};
  \node[lab, left] at (-1.45,0) {$(1,3,2)$};
  \node[lab, below left] at (-0.72,-1.25) {$(2,3,1)$};
  \node[lab, below right] at (0.72,-1.25) {$(3,2,1)$};
  \node[lab, below right] at (0.03,-0.03) {$(2,2,2)$};
\end{tikzpicture}
\end{center}

The solid hexagon is the permutation polytope of \( \y = (3, 2, 1) \), drawn inside the plane \( x_1 + x_2 + x_3 = 6 \); the dashed one, at half the size, is the polytope of \( (\tfrac52, 2, \tfrac32) \). By @cor-majorization-convex-hull, \( \x \prec \y \) says that \( \x \) lies in the solid hexagon, and \( \x \prec (\tfrac52, 2, \tfrac32) \prec \y \) says that the dashed hexagon sits inside the solid one. *The majorization order is containment of permutation polytopes.* The center \( (2,2,2) \), the flat vector, lies in every one of them, which is @exm-majorization-first-examples (b) again.

::: {.check}
Use @cor-majorization-convex-hull to give a second proof that \( \{\x : \x \prec \y\} \) is convex, a fact Chapter 18 proved by hand in @exm-majorization-set-convex.
:::

::: {.solution}
By the corollary, \( \{\x : \x \prec \y\} = \conv\{\P_\sigma\y : \sigma \in S_n\} \). A convex hull is convex (@thm-convex-hull-combinations, or @def-convex-hull directly). So the set is convex.
:::

## Exercises

### A. Check your understanding

:::: {#exr-hardy-littlewood-polya-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define a T-transform, and say which coordinates of a vector it can change.
2. State the Hardy–Littlewood–Pólya theorem in full.
3. True or false: if \( \x = \S\y \) with \( \S \) row-stochastic (non-negative entries, every row adding up to \( 1 \)), then \( \x \prec \y \). Justify your answer.
4. True or false: if \( \x \prec \y \), the doubly stochastic \( \D \) with \( \x = \D\y \) is unique. Justify your answer.
5. In @lem-t-transform-step, why is \( j \) chosen as the **largest** index with \( y_j > x_j \) rather than the smallest?
6. Why can the number of coordinates in which two decreasing vectors \( \x \prec \y \) agree never be exactly \( n - 1 \)?
:::
::::

::: {.solution}
(a) For \( 1 \le j < k \le n \) and \( 0 \le t \le 1 \), it is \( \T = (1-t)\I + t\Q \) with \( \Q \) the permutation matrix of the transposition of \( j \) and \( k \) (@def-t-transform). It changes only the coordinates \( j \) and \( k \), replacing each by an average of the two old values.

(b) For \( \x, \y \in \nR^n \), \( \x \prec \y \) if and only if \( \x = \D\y \) for some doubly stochastic \( \D \); and when \( \x \) and \( \y \) are both decreasing, \( \D \) may be taken to be a product of at most \( n-1 \) T-transforms (@thm-hardy-littlewood-polya).

(c) False. With \( \y = (1,0) \) and \( \S = \begin{psmallmatrix} 1 & 0 \\ 1 & 0\end{psmallmatrix} \), \( \S\y = (1,1) \) has total \( 2 \) while \( \y \) has total \( 1 \), so (M2) fails. Row sums alone control nothing but the individual entries; the column sums are what preserve the total.

(d) False. For \( \y = (2,1,0) \) and \( \x = (1,1,1) \), both \( \tfrac13\J \) and the matrix \( \D_2 \) of the warning after @exm-hlp-four-vector send \( \y \) to \( \x \).

(e) Because it makes the entries strictly between \( j \) and \( k \) agree with \( \x \)'s, which is what Step 4 needs in order to keep \( \y' \) decreasing. The majorization would survive the other choice: with \( j \) smallest, the slack \( Y_m - X_m \) is non-decreasing on \( j \le m \le k - 1 \) rather than constant, hence still at least \( \delta \) throughout, and Step 5 goes through. The sorted order is what fails, and with it the possibility of applying the lemma again. For \( \x = (5,5,0) \) and \( \y = (6,6,-2) \), taking \( j \) smallest gives \( j = 1 \), \( k = 3 \), \( \delta = 1 \) and \( \y' = (5, 6, -1) \), which is not decreasing, while the rule of the lemma gives \( j = 2 \) and \( \y' = (6, 5, -1) \), which is.

(f) Suppose they agree in all indices but \( i_0 \). Subtracting the \( n - 1 \) equalities \( x_i = y_i \) from the equal totals of (M2) leaves \( x_{i_0} = y_{i_0} \), so in fact they agree everywhere.
:::

### B. Practice

:::: {#exr-hardy-littlewood-polya-b1}
[B1: Run the construction]

Let \( \y = (9, 5, 4) \) and \( \x = (6, 6, 6) \). Verify \( \x \prec \y \), produce T-transforms \( \T_1, \T_2 \) with \( \x = \T_2\T_1\y \) by the recipe of @lem-t-transform-step, and write out \( \D = \T_2\T_1 \). Hence check that \( \D \) is doubly stochastic.
::::

::: {.solution}
Both vectors are decreasing with total \( 18 \), and the running totals are \( 6, 12 \) against \( 9, 14 \). So (M1) and (M2) hold and \( \x \prec \y \).

*First step.* \( \y - \x = (3, -1, -2) \), so \( j = 1 \) and \( k = 2 \). Then \( \delta = \min\{3, 1\} = 1 \) and \( t = 1/(9-5) = \tfrac14 \), and \( \T_1 \) acts on \( \{1,2\} \):
\[
\y' = \bigl(\tfrac34\cdot 9 + \tfrac14\cdot 5,\ \tfrac14\cdot 9 + \tfrac34\cdot 5,\ 4\bigr) = (8, 6, 4) .
\]

*Second step.* \( \y' - \x = (2, 0, -2) \), so \( j = 1 \), \( k = 3 \), \( \delta = \min\{2,2\} = 2 \) and \( t = 2/(8-4) = \tfrac12 \). Then
\[
\T_2\y' = \bigl(\tfrac12\cdot 8 + \tfrac12\cdot 4,\ 6,\ \tfrac12\cdot 8 + \tfrac12\cdot 4\bigr) = (6, 6, 6) = \x .
\]

*The matrix.* \( \T_1 \) has rows \( (\tfrac34, \tfrac14, 0) \), \( (\tfrac14, \tfrac34, 0) \), \( (0,0,1) \), and \( \T_2 \) has rows \( (\tfrac12, 0, \tfrac12) \), \( (0,1,0) \), \( (\tfrac12, 0, \tfrac12) \). Multiplying,
\[
\D = \T_2\T_1 = \begin{pmatrix}
\tfrac38 & \tfrac18 & \tfrac12 \\[2pt]
\tfrac14 & \tfrac34 & 0 \\[2pt]
\tfrac38 & \tfrac18 & \tfrac12
\end{pmatrix} .
\]
Each row adds up to \( 1 \), and the columns add up to \( \tfrac38 + \tfrac14 + \tfrac38 = 1 \), \( \tfrac18 + \tfrac34 + \tfrac18 = 1 \) and \( \tfrac12 + 0 + \tfrac12 = 1 \). So \( \D \in \Omega_3 \), and \( \D\y = (\tfrac{27}{8} + \tfrac58 + 2,\ \tfrac94 + \tfrac{15}4,\ \tfrac{27}8 + \tfrac58 + 2) = (6,6,6) \).
:::

:::: {#exr-hardy-littlewood-polya-b2}
[B2: Determine which are majorizations]

For each pair, determine whether \( \x \prec \y \). Where it holds, exhibit a doubly stochastic \( \D \) with \( \x = \D\y \); where it fails, name the clause of @def-majorization and the value of \( k \) at which it fails. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \x = (2, 2, 2) \), \( \y = (4, 1, 1) \).
2. \( \x = (3, 1, 0) \), \( \y = (2, 2, 0) \).
3. \( \x = (1, 3, 0) \), \( \y = (2, 0, 2) \).
4. \( \x = (1, 1) \), \( \y = (2, 1) \).
:::
::::

::: {.solution}
(a) Both decreasing, totals \( 6 = 6 \); running totals \( 2, 4 \) against \( 4, 5 \). So \( \x \prec \y \). Here \( \x \) is the flat vector, and \( \D = \tfrac13\J \) works: every entry of \( \tfrac13\J\y \) is \( \tfrac13(4+1+1) = 2 \).

(b) Totals \( 4 = 4 \), but at \( k = 1 \) the sorted first entries are \( 3 > 2 \), so (M1) fails at \( k = 1 \) and \( \x \not\prec \y \).

(c) Sorted, \( \x^{\downarrow} = (3,1,0) \) and \( \y^{\downarrow} = (2,2,0) \); this is (b) again, so \( \x \not\prec \y \), with (M1) failing at \( k = 1 \).

(d) Totals \( 2 \ne 3 \), so (M2) fails and \( \x \not\prec \y \). (Both running totals do satisfy (M1), so \( \x \prec_w \y \).)
:::

:::: {#exr-hardy-littlewood-polya-b3}
[B3: Into the polytope]

Let \( \y = (4, 2, 0) \) and \( \x = (2, 2, 2) \). Using @cor-majorization-convex-hull, write \( \x \) explicitly as a convex combination of rearrangements of \( \y \), in two different ways.
::::

::: {.solution}
The six rearrangements of \( \y \) are the vectors with entries \( 4, 2, 0 \) in some order. Averaging the three cyclic shifts,
\[
\tfrac13\bigl[(4,2,0) + (0,4,2) + (2,0,4)\bigr] = \tfrac13(6,6,6) = (2,2,2) = \x .
\]
Alternatively, average a vector with its reversal:
\[
\tfrac12\bigl[(4,2,0) + (0,2,4)\bigr] = \tfrac12(4,4,4) = (2,2,2) = \x .
\]
Both are convex combinations, with weights \( (\tfrac13,\tfrac13,\tfrac13) \) and \( (\tfrac12,\tfrac12) \). This is the non-uniqueness of the warning after @exm-hlp-four-vector, seen on the polytope: \( \x \) is the center of the hexagon, lying strictly inside it rather than on an edge, and such a point has many representations. (The hexagon itself has empty interior in \( \nR^3 \), since it lies in the plane \( x_1 + x_2 + x_3 = 6 \); "inside" here means inside the hexagon, within that plane.)
:::

### C. Going deeper

:::: {#exr-hardy-littlewood-polya-c1}
[C1: Row-stochastic is not enough, twice over]

Let \( \S \in M_n(\nR) \) be **row-stochastic**: every entry is non-negative and every row adds up to \( 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Give such an \( \S \) and a \( \y \in \nR^2 \) with \( \S\y \not\prec \y \).
2. Prove that if \( \S\y \prec \y \) for **every** \( \y \in \nR^n \), then \( \S \) is doubly stochastic.
:::

*Hint for (b): test the hypothesis on the standard basis vectors.*
::::

::: {.solution}
(a) Take \( \S = \begin{psmallmatrix} 1 & 0 \\ 1 & 0\end{psmallmatrix} \) and \( \y = (1, 0) \). Then \( \S\y = (1,1) \), whose total is \( 2 \), while \( \y \) has total \( 1 \). So (M2) fails.

(b) Apply the hypothesis with \( \y = \e_j \). The vector \( \S\e_j \) is the \( j \)-th column of \( \S \), by @def-matrix-multiplication. From \( \S\e_j \prec \e_j \), clause (M2) gives
\[
\sum_{i=1}^{n}s_{ij} = \sum_{i=1}^{n}(\e_j)_i = 1 .
\]
So every column of \( \S \) adds up to \( 1 \). The entries are non-negative and the rows add up to \( 1 \) by hypothesis, so \( \S \) is doubly stochastic by @def-doubly-stochastic.
:::

:::: {#exr-hardy-littlewood-polya-c2}
[C2: Transitivity, a second time]

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( \A, \B \in \Omega_n \) then \( \A\B \in \Omega_n \).
2. Hence deduce that \( \x \prec \y \) and \( \y \prec \z \) imply \( \x \prec \z \), and compare this route with the proof of @prp-majorization-basic (b).
:::
::::

::: {.solution}
(a) The entries of \( \A\B \) are \( \sum_k a_{ik}b_{kj} \), sums of products of non-negative numbers, hence non-negative. Since \( \A\1 = \1 \) and \( \B\1 = \1 \), we get \( (\A\B)\1 = \A(\B\1) = \A\1 = \1 \), so every row of \( \A\B \) adds up to \( 1 \). Since \( \1\tp\A = \1\tp \) and \( \1\tp\B = \1\tp \), we get \( \1\tp(\A\B) = (\1\tp\A)\B = \1\tp\B = \1\tp \), so every column does too. By @def-doubly-stochastic, \( \A\B \in \Omega_n \).

(b) By @thm-hardy-littlewood-polya there are \( \D, \E \in \Omega_n \) with \( \x = \D\y \) and \( \y = \E\z \). Then \( \x = \D\E\z \), and \( \D\E \in \Omega_n \) by (a). By @thm-hardy-littlewood-polya again, \( \x \prec \z \).

@prp-majorization-basic (b) proved the same thing in one line, by chaining the inequalities \( X_k \le Y_k \le Z_k \) between running totals. That proof is shorter and uses nothing. The route here is longer, but it explains transitivity rather than verifying it: a majorization is an averaging, and averaging twice is averaging.
:::

:::: {#exr-hardy-littlewood-polya-c3}
[C3: The count \( n - 1 \) cannot be improved]

Let \( n \ge 2 \), \( \y = (n, 0, \dots, 0) \) and \( \x = (1, 1, \dots, 1) \) in \( \nR^n \). For \( \z \in \nR^n \), write \( \operatorname{supp}(\z) = \{i : z_i \ne 0\} \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \x \prec \y \).
2. Let \( \T \) be a T-transform. Prove that \( \lvert\operatorname{supp}(\T\z)\rvert \le \lvert\operatorname{supp}(\z)\rvert + 1 \) for every \( \z \in \nR^n \).
3. Deduce that no product of fewer than \( n - 1 \) T-transforms sends \( \y \) to \( \x \).
:::
::::

::: {.solution}
(a) Both vectors are decreasing with total \( n \). Every running total of \( \y \) is \( n \), and the \( k \)-th running total of \( \x \) is \( k \le n \). So (M1) and (M2) hold.

(b) Let \( \T \) act on \( \{j, k\} \) with parameter \( t \). By @eq-t-transform-action, \( (\T\z)_i = z_i \) for \( i \notin \{j, k\} \), so
\[
\operatorname{supp}(\T\z) \subseteq \operatorname{supp}(\z) \cup \{j, k\} .
\]
If both \( j, k \in \operatorname{supp}(\z) \), the right side is \( \operatorname{supp}(\z) \) and there is nothing to prove. If neither is, then \( z_j = z_k = 0 \), so \( (\T\z)_j = (\T\z)_k = 0 \) and again \( \operatorname{supp}(\T\z) \subseteq \operatorname{supp}(\z) \). In the remaining case exactly one of them, say \( j \), lies in \( \operatorname{supp}(\z) \), and then \( \operatorname{supp}(\T\z) \subseteq \operatorname{supp}(\z) \cup \{k\} \), a set with one more element. In all cases the bound holds.

(c) Suppose \( \x = \T_r\cdots\T_1\y \). Put \( \z^{(0)} = \y \) and \( \z^{(i)} = \T_i\z^{(i-1)} \). Then \( \lvert\operatorname{supp}(\z^{(0)})\rvert = 1 \) and \( \lvert\operatorname{supp}(\z^{(r)})\rvert = \lvert\operatorname{supp}(\x)\rvert = n \). By (b), the size of the support grows by at most \( 1 \) at each step, so
\[
n \le 1 + r , \qquad\text{that is,}\qquad r \ge n - 1 .
\]
Together with @thm-hardy-littlewood-polya, which gives such a product with \( r \le n-1 \), exactly \( n - 1 \) transforms are needed for this pair.
:::
