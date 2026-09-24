# Floating Point and Backward Error

Chapter 16 ended with a number and a warning. The number was \( \kappa(\A) \), which bounds how much a relative error in the data can be magnified on the way to the answer. The warning was that \( \kappa \) says nothing about arithmetic: it "describes a problem", and an error bound of its shape "only becomes a statement about a computation once one knows how large a perturbation the computation itself introduces". That chapter closed the door with a sentence we now have to walk through: "Conditioning bounds what *any* method can promise; whether a given method keeps that promise is stability, and it is Chapter 24's subject."

This section builds the two things that were missing. First a **model** of machine arithmetic — an assumption, stated plainly as one, because floating-point arithmetic is not a theorem of linear algebra. Then the vocabulary that turns the model into verdicts about algorithms: forward error, backward error, and stability.

## Two answers to one question

Chapter 16 §08 left a small experiment on the reader's desk. The system was
\[
\begin{aligned}
10^{-15}x_1 + x_2 &= 1, \\
x_1 + x_2 &= 2 ,
\end{aligned}
\]
whose coefficient matrix has \( \kappa_{\infty} < 5 \): by every measure of Chapter 16 this problem is as well behaved as a problem can be, and its exact solution is \( (1, 1) \) to fourteen places. Eliminating \( x_1 \) with the first equation as the pivot row, and rounding to twelve significant decimal digits at every step, returns \( (0, 1) \). Exchanging the two equations first, and rounding in exactly the same way, returns \( (1, 1) \).

Two algorithms, one problem, one arithmetic, and one of the two answers has no correct digit in it. Nothing in Chapter 16 can tell the two apart, because \( \kappa \) never mentions a method. Section 2 works that example in the model below and says exactly what the exchange achieved. This section builds the language it will be said in.

## A model of machine arithmetic

A machine holds finitely many numbers. It cannot hold \( 1/3 \), it cannot hold \( \sqrt2 \), and between any two numbers it does hold there are infinitely many it does not. So the result of an arithmetic operation on two stored numbers is usually not a stored number, and the machine must replace it by a neighbor.

We could try to describe which numbers a particular machine stores and exactly how it rounds. That would be a description of a machine, not mathematics, and it would be obsolete before the ink dried. What is wanted instead is the *one property* of rounding that every later argument uses, elevated into an assumption.

*Every operation is performed exactly and then moved to the nearest stored number, so each operation multiplies its exact answer by something within \( u \) of \( 1 \).*

::: {#def-floating-point-model}
[The floating-point model]

A **floating-point model** consists of a finite set \( \cR \subseteq \nR \) of **representable numbers** with \( 0, 1 \in \cR \) and \( -\cR = \cR \), a map \( \fl \colon \nR \to \cR \) sending each real number to **a nearest** element of \( \cR \), and a real number \( u > 0 \) called the **unit roundoff**, subject to the following.

::: {.enumerate options="label=(FP\arabic*)"}
1. **(Rounding.)** For every \( t \in \nR \) in range, \( \fl(t) = t(1 + \delta) \) for some \( \delta \) with \( \lvert\delta\rvert \le u \).
2. **(Arithmetic.)** For \( x, y \in \cR \) and \( \odot \in \{+, -, \times, \div\} \) with \( y \ne 0 \) when \( \odot \) is \( \div \), the computed value of \( x \odot y \) is \( \fl(x \odot y) \); the computed value of \( \sqrt{x} \) for \( x \in \cR \), \( x \ge 0 \), is \( \fl(\sqrt{x}\,) \). Hence
   \[
   \fl(x \odot y) = (x \odot y)(1 + \delta),
   \qquad
   \lvert\delta\rvert \le u ,
   \]
   and likewise \( \fl(\sqrt x) = \sqrt x\,(1 + \delta) \) with \( \lvert\delta\rvert \le u \).
3. **(No overflow or underflow.)** Every quantity occurring in a computation we analyze is assumed to be **in range**, so that (FP1) applies to it.
:::
:::

Clause by clause. "A nearest element" is a mild requirement, and the only use we make of it is the observation that \( \lvert t\rvert \le 1 \) forces \( \lvert\fl(t)\rvert \le 1 \), because \( 1 \in \cR \). (FP1) is the whole content of the word *roundoff*: the error made in storing a real number is **relative**, of size at most \( u \), and that is essentially the only thing we will ever know about \( \fl \). (FP2) says an operation is as accurate as storing its answer would be — the machine does not do anything stupid in between. The displayed identity is what every proof in this chapter actually uses, and it is worth reading aloud: *the computed product is the exact product times \( 1 + \delta \)*. (FP3) is an honest exclusion. Numbers too large or too small for \( \cR \) break (FP1) completely, and analyzing them is a separate subject; we assume the problem away and say so each time it matters.

**This is a definition, not a theorem.** Nothing in Chapters 1 to 21 implies it, and nothing in this chapter proves it. It is an idealization of a machine, in the way that a frictionless plane is an idealization of a table. The arithmetic in common use satisfies it for the four operations and the square root, with \( u \) a little over \( 10^{-16} \); a decimal machine carrying \( t \) significant digits satisfies it with \( u = \tfrac12 \cdot 10^{1-t} \). Every statement in this chapter that mentions rounding is a theorem **about the model**, and carries exactly as much authority as the model does.

::: {#exm-six-digit-model}
[The model we compute in]

Throughout this chapter, a worked number comes from the **six-digit decimal model**: \( \cR \) is the set of numbers \( \pm d_1.d_2d_3d_4d_5d_6 \times 10^{e} \) with digits \( d_i \), \( d_1 \ne 0 \) and \( e \) in some fixed finite range, together with \( 0 \); and \( \fl \) rounds to the nearest such number. (The range of \( e \) is what (FP3) lets us stop thinking about.) What is \( u \), and what is \( \fl(99999996) \)?
:::

::: {.solution}
Two consecutive representable numbers of the same exponent \( e \) differ by \( 10^{e-5} \), and a number \( t \) with that exponent has \( \lvert t\rvert \ge 10^{e} \). Rounding to the nearest moves \( t \) by at most half the gap, so
\[
\lvert\fl(t) - t\rvert \le \tfrac12 \cdot 10^{e-5} \le \tfrac12 \cdot 10^{-5}\lvert t\rvert ,
\]
which is (FP1) with \( u = \tfrac12 \cdot 10^{-5} = 5 \times 10^{-6} \).

For \( \fl(99999996) \): the number is \( 9.9999996 \times 10^{7} \), and the two neighbors with six digits are \( 9.99999 \times 10^{7} \) and \( 1.00000 \times 10^{8} \). The second is nearer, so \( \fl(99999996) = 10^{8} \). Note what happened: eight digits went in, six came out, and the two digits that were lost were the only two that distinguished \( 99999996 \) from \( 10^8 \).
:::

::: {.warning}
**A model with an absolute error bound would be a different, and false, model.** Suppose we had written \( \fl(x + y) = (x + y) + \delta \) with \( \lvert\delta\rvert \le u \). Then \( \fl(10^{6} + 1) \) would have to be within \( u = 5\times10^{-6} \) of \( 10^{6} + 1 \), whereas a six-digit machine returns \( 10^{6} \), an absolute error of \( 1 \). The error a machine makes is proportional to the size of the number it is storing; a machine is accurate in *ratio*, never in *amount*. Confusing the two is the commonest mistake in the subject, and (FP1) exists to prevent it.
:::

::: {.check}
In the six-digit model, is \( \fl(x + y) = x + y \) possible when \( x \) and \( y \) are representable and both non-zero? Is \( \fl(x - y) = x - y \) possible when \( x \ne y \)?
:::

::: {.solution}
Yes to both, and easily. \( 1 + 2 = 3 \) is representable, so the first addition is exact. For the second, \( 10^{8} - 99999.9 = 99900000.1 \), which is *not* representable, so that particular subtraction is inexact; but \( 1.00001 - 1.00000 = 10^{-5} \) is representable exactly, so that subtraction is exact. The model never claims an operation *is* inexact. It claims only a bound on how inexact it can be. That both extremes occur is what makes the subject interesting: the second subtraction is performed exactly, and it is nevertheless the shape of subtraction that destroys answers, as the last example of this section will show.
:::

## Accumulated rounding: the constant \( \gamma_k \)

A single operation costs a factor \( 1 + \delta \). An algorithm performs many, and the factors pile up: an answer typically carries a product like \( (1 + \delta_1)(1 + \delta_2)\cdots(1 + \delta_k) \), sometimes with an inverted factor where a division occurred. Carrying such products around is unbearable, so we bound them once and for all. The constant that results is used in every remaining section of this chapter.

::: {#lem-gamma-bound}
[Accumulated rounding]

Let \( k \ge 1 \) and let \( \delta_1, \dots, \delta_k \) satisfy \( \lvert\delta_i\rvert \le u \), and let \( \rho_1, \dots, \rho_k \in \{+1, -1\} \). If \( ku < 1 \), then
\[
\prod_{i=1}^{k}(1 + \delta_i)^{\rho_i} = 1 + \theta
\qquad\text{with}\qquad
\lvert\theta\rvert \le \gamma_k \coloneqq \frac{ku}{1 - ku} .
\]
:::

::: {.idea}
Induction on \( k \), with the two signs treated as two cases. The only thing to watch is that the recursion for \( \gamma_k \) survives division, where the denominator \( 1 - u \) costs something; the definition \( \gamma_k = ku/(1-ku) \) is exactly the bound that absorbs that cost.
:::

::: {.proof}
Note first that \( ku < 1 \) forces \( ju < 1 \) for \( j \le k \), so every \( \gamma_j \) with \( j \le k \) is defined and positive, and \( \gamma_1 \le \gamma_2 \le \dots \le \gamma_k \).

*Base case \( k = 1 \).* If \( \rho_1 = +1 \), then \( \theta = \delta_1 \) and \( \lvert\theta\rvert \le u \le u/(1-u) = \gamma_1 \). If \( \rho_1 = -1 \), then
\[
\theta = \frac{1}{1 + \delta_1} - 1 = \frac{-\delta_1}{1 + \delta_1},
\qquad
\lvert\theta\rvert \le \frac{u}{1 - u} = \gamma_1 ,
\]
where \( 1 + \delta_1 \ge 1 - u > 0 \) because \( u < 1 \).

*Inductive step.* Suppose the product of the first \( k-1 \) factors is \( 1 + \theta' \) with \( \lvert\theta'\rvert \le \gamma_{k-1} \), and write \( \delta = \delta_k \).

If \( \rho_k = +1 \), then \( 1 + \theta = (1 + \theta')(1 + \delta) \), so \( \theta = \theta' + \delta + \theta'\delta \) and
\[
\begin{aligned}
\lvert\theta\rvert
&\le \gamma_{k-1} + u + \gamma_{k-1}u\\
&= \frac{(k-1)u + u\bigl(1 - (k-1)u\bigr) + (k-1)u^2}{1 - (k-1)u}
= \frac{ku}{1 - (k-1)u} ,
\end{aligned}
\]
and \( 1 - (k-1)u \ge 1 - ku > 0 \), so this is at most \( ku/(1-ku) = \gamma_k \).

If \( \rho_k = -1 \), then \( 1 + \theta = (1 + \theta')/(1 + \delta) \), so \( \theta = (\theta' - \delta)/(1 + \delta) \) and \( \lvert\theta\rvert \le (\gamma_{k-1} + u)/(1 - u) \). It remains to check that this is at most \( \gamma_k \). Clearing the positive denominators \( 1 - (k-1)u \), \( 1 - u \) and \( 1 - ku \), the inequality \( (\gamma_{k-1}+u)/(1-u) \le \gamma_k \) is equivalent to
\[
u\bigl(k - (k-1)u\bigr)(1 - ku) \le ku\bigl(1 - ku + (k-1)u^2\bigr) ,
\]
and expanding both sides gives \( k - k^2u - (k-1)u + k(k-1)u^2 \) on the left against \( k - k^2u + k(k-1)u^2 \) on the right, after dividing by \( u > 0 \). The left side is the right side minus \( (k-1)u \), which is at least \( 0 \), so the left side is at most the right side and the inequality holds. This proves the lemma.
:::

::: {.remark}
Read \( \gamma_k \) as "about \( ku \)". Indeed if \( ku \le 0.01 \) then \( \gamma_k \le ku/0.99 < 1.02\,ku \). The denominator is there only so that the induction above closes; it is never the point of a bound. We will also use, without further comment, that \( \gamma_j \le \gamma_k \) for \( j \le k \), and we set \( \gamma_0 = 0 \), which is what the formula gives and what the empty product deserves.
:::

## The first backward error analysis

Here is the simplest algorithm in the book: add up \( n \) products. What comes out is not \( \x\tp\y \). But it is *exactly* \( \x\tp\y \) for a slightly different \( \x \) — and that turns out to be the useful thing to say.

::: {#thm-inner-product-backward-error}
[Backward Error of an Inner Product]

Let \( \x, \y \in \nR^{n} \) have representable entries, let \( nu < 1 \), and let the inner product be computed in the model of @def-floating-point-model in the natural order,
\[
s_1 = \fl(x_1y_1),
\qquad
s_k = \fl\bigl(s_{k-1} + \fl(x_ky_k)\bigr)
\quad (k = 2, \dots, n).
\]
Then there is a vector \( \Delta\x \in \nR^n \) with
\[
s_n = (\x + \Delta\x)\tp\y
\qquad\text{and}\qquad
\lvert\Delta x_i\rvert \le \gamma_n \lvert x_i\rvert \ \text{ for every } i .
\]
:::

::: {.idea}
Unroll the recursion and see which rounding factors touch which term. The term \( x_ky_k \) picks up one factor from its own multiplication and one from each addition it takes part in afterwards, so no term collects more than \( n \) factors. @lem-gamma-bound converts "at most \( n \) factors" into "\( 1 + \theta \) with \( \lvert\theta\rvert \le \gamma_n \)", and a factor attached to \( x_ky_k \) can be blamed on \( x_k \) alone.
:::

::: {.proof}
By (FP2) there are numbers \( \delta_k \) and \( \varepsilon_k \), all of modulus at most \( u \), with
\[
\begin{aligned}
\fl(x_ky_k) &= x_ky_k(1 + \delta_k)
\quad (1 \le k \le n),\\
s_k &= \bigl(s_{k-1} + \fl(x_ky_k)\bigr)(1 + \varepsilon_k)
\quad (2 \le k \le n).
\end{aligned}
\]
An induction on \( m \) gives
\[
s_m = \sum_{k=1}^{m} x_ky_k(1 + \delta_k)\prod_{j = \max(k,2)}^{m}(1 + \varepsilon_j) ,
\]
the empty product being \( 1 \): for \( m = 1 \) this is \( s_1 = x_1y_1(1+\delta_1) \), and the step from \( m-1 \) to \( m \) multiplies every existing term by \( 1 + \varepsilon_m \) and adds the new term \( x_my_m(1+\delta_m)(1+\varepsilon_m) \), which is what the formula says.

Take \( m = n \) and count factors in the \( k \)-th term. For \( k = 1 \) there are \( 1 + (n-1) = n \) of them; for \( k \ge 2 \) there are \( 1 + (n - k + 1) = n - k + 2 \le n \). Every factor has the form \( 1 + \delta \) with \( \lvert\delta\rvert \le u \), and \( nu < 1 \), so @lem-gamma-bound (with all \( \rho_i = +1 \)) gives numbers \( \theta_k \) with
\[
s_n = \sum_{k=1}^{n} x_ky_k(1 + \theta_k),
\qquad
\lvert\theta_k\rvert \le \gamma_n .
\]
Put \( \Delta x_k = x_k\theta_k \). Then \( \lvert\Delta x_k\rvert \le \gamma_n\lvert x_k\rvert \) and \( s_n = \sum_k (x_k + \Delta x_k)y_k = (\x + \Delta\x)\tp\y \). This proves the theorem.
:::

The conclusion is worth staring at. The computed number is not close to \( \x\tp\y \) — if \( \x\tp\y \) happens to be tiny compared with \( \sum_k \lvert x_ky_k\rvert \), it can be wrong in every digit. What the theorem says is different and stronger in kind: *the computed number is an inner product, exactly, of data within a relative \( \gamma_n \) of the given data.* The algorithm has not solved a nearby problem approximately; it has solved a nearby problem exactly.

::: {.remark}
The same proof, with the roles of \( \x \) and \( \y \) exchanged, gives \( s_n = \x\tp(\y + \Delta\y) \) with \( \lvert\Delta\y\rvert \le \gamma_n\lvert\y\rvert \) entrywise. What it does **not** give is a perturbation of both at once with half the constant, and it does not give a bound on \( \lvert s_n - \x\tp\y\rvert \) relative to \( \lvert\x\tp\y\rvert \). @exr-floating-point-and-backward-error-c1 makes the last point precise. For complex \( \x, \y \) the operations \( + \), \( \times \) are themselves built from several real operations, so the model must be applied to those; the resulting bound has the same shape with a modestly larger constant, and we do not prove it here or use it.
:::

## Forward error, backward error, stability

We can now name what @thm-inner-product-backward-error did, and the alternative it declined to do. Fix a **problem**: a map \( f \colon D \to \nR^{m} \) from data to answers, where \( D \) is a set of admissible data in some \( \nR^{N} \). The set \( D \) always consists of **real** data and is never cut down to the representable ones: for the problems of this chapter it is all of \( \nR^{N} \), or all invertible matrices, and it has to be, because the perturbed datum \( \a + \Delta\a \) below must lie in it. An **algorithm** for \( f \) is a map \( \widehat f \) — defined at the representable data, and sending each of them to whatever the computation actually returns in the model, rounding and all. Two numbers measure how the second differs from the first.

::: {#def-forward-error}
[Forward and backward error]

Let \( f \) be a problem, \( \widehat f \) an algorithm for it, and \( \a \in D \) a representable datum with \( f(\a) \ne \0 \). The **forward error** of \( \widehat f \) at \( \a \) is the relative error in the answer,
\[
\frac{\norm{\widehat f(\a) - f(\a)}}{\norm{f(\a)}} .
\]
The **backward error** of \( \widehat f \) at \( \a \) is the smallest relative perturbation of the data that accounts for the computed answer exactly,
\[
\inf\Bigl\{\frac{\norm{\Delta\a}}{\norm{\a}} \;:\; \a + \Delta\a \in D \text{ and } f(\a + \Delta\a) = \widehat f(\a)\Bigr\} ,
\]
with the convention that it is \( \infty \) when no such \( \Delta\a \) exists.
:::

The forward error is what a user wants to know and can almost never compute, since it needs \( f(\a) \). The backward error is what an analyst can bound, because bounding it only requires *exhibiting* one \( \Delta\a \), which a proof like the one above hands over for free. An algorithm whose backward error is always as small as the arithmetic allows is the best one can hope for.

*A backward stable algorithm returns the exact answer to a question you might as well have asked.*

::: {#def-backward-stable}
[Backward stability]

Let \( f \colon D \to \nR^m \) be a problem. An algorithm \( \widehat f \) for \( f \), running in a floating-point model with unit roundoff \( u \), is **backward stable** if there is a constant \( c \), depending only on the dimensions of the data and **not** on the data itself or on \( u \), such that for every representable \( \a \in D \) there exists \( \Delta\a \in \nR^{N} \) with
\[
\a + \Delta\a \in D,
\qquad
\widehat f(\a) = f(\a + \Delta\a),
\qquad
\norm{\Delta\a} \le c\,u\,\norm{\a} .
\]
:::

The small words carry the weight. **For every \( \a \)**: one lucky datum proves nothing. **\( c \) independent of the data**: a "constant" allowed to grow with \( \norm{\a} \) or with \( \kappa \) would make the definition vacuous. **\( c \) independent of \( u \)**: the bound must improve when the arithmetic does. The constant is allowed to depend on \( n \), and in practice always does — \( \gamma_n \) is about \( nu \), not \( u \) — which is why "backward stable" is a statement about a *family* of algorithms indexed by size, and why nobody worries much about a factor of \( n \).

By @thm-inner-product-backward-error, the natural inner product algorithm is backward stable as an algorithm in \( \x \) for the problem \( \x \mapsto \x\tp\y \) with \( \y \) fixed, on the domain \( D = \nR^n \). Take \( c = 1.02\,n \), which depends on the dimension alone. Indeed the entrywise bound \( \lvert\Delta\x\rvert \le \gamma_n\lvert\x\rvert \) implies \( \norm{\Delta\x} \le \gamma_n\norm{\x} \) in each of the norms \( \norm{\cdot}_1 \), \( \norm{\cdot}_2 \), \( \norm{\cdot}_{\infty} \), and \( \gamma_n \le 1.02\,nu \) in every model with \( nu \le 0.01 \), by the remark after @lem-gamma-bound. (Restricting to such models is how a bound stated with \( \gamma_n \) is turned into one with a constant independent of \( u \), and we do it silently from here on.)

Some algorithms are not backward stable and are not bad either: they perturb the data a little *and* the answer a little, and neither perturbation alone accounts for the result. The weaker notion that covers them is worth naming, so that we never have to claim more than we have proved.

::: {#def-mixed-stability}
[Mixed forward-backward stability]

An algorithm \( \widehat f \) for \( f \colon D \to \nR^m \) is **mixed forward-backward stable** if there is a constant \( c \), depending only on the dimensions, such that for every representable \( \a \in D \) there are \( \Delta\a \) and \( \Delta\y \) with \( \a + \Delta\a \in D \) and
\[
\widehat f(\a) = f(\a + \Delta\a) + \Delta\y,
\qquad
\norm{\Delta\a} \le cu\norm{\a},
\qquad
\norm{\Delta\y} \le cu\norm{f(\a + \Delta\a)} .
\]
:::

Backward stability is the special case \( \Delta\y = \0 \), so it is the stronger statement of the two. A mixed stable algorithm does **not** satisfy the hypothesis of the next theorem: its \( \Delta\y \) contributes a further term to the forward error, and we do not estimate that term anywhere in this chapter. Where a method in this chapter is only mixed stable, we say so, and we claim nothing more about it than the definition gives.

::: {.warning}
**Backward stable does not mean accurate, and inaccurate does not mean unstable.** A backward stable algorithm commits to nothing about the forward error except what the *problem* allows, and for an ill-conditioned problem that is very little. Conversely, an algorithm can return an accurate answer on one datum by luck while being backward unstable. The two words describe different objects: conditioning belongs to \( f \), stability belongs to \( \widehat f \). Chapter 16 §08 promised exactly this: "Chapter 24 draws the distinction properly, defines backward stability, and proves which of the algorithms in this book have it." @def-backward-stable is the definition; the proofs occupy Sections 2 and 3, and the next theorem is the only bridge between the two sides.
:::

## Multiplying the two together

The rule of thumb everyone quotes is *forward error \( \lesssim \) condition number \( \times \) backward error*. For linear systems it is not a rule of thumb at all. It is @thm-relative-error-bound with a different reading of the same symbols.

::: {#thm-forward-from-backward}
[Forward Error from Backward Error]

Let \( \A \in M_n(\nC) \) be invertible, \( \b \ne \0 \), and \( \A\x = \b \). Let \( \widehat\x \) be any vector which is the exact solution of a perturbed system,
\[
(\A + \Delta\A)\widehat\x = \b,
\qquad
\frac{\norm{\Delta\A}}{\norm{\A}} \le \eta ,
\]
and suppose \( r \coloneqq \kappa(\A)\,\eta < 1 \). Then \( \A + \Delta\A \) is invertible and
\[
\frac{\norm{\widehat\x - \x}}{\norm{\x}} \;\le\; \frac{r}{1 - r} \;=\; \frac{\kappa(\A)\eta}{1 - \kappa(\A)\eta} .
\]
In particular, if \( \eta = cu \) is admissible — as it is when the algorithm producing \( \widehat\x \) is backward stable with constant \( c \) **for the problem \( \A \mapsto \A^{-1}\b \) with \( \b \) held fixed**, so that only \( \A \) is perturbed — and if \( \kappa(\A)cu \le \tfrac12 \), then the forward relative error is at most \( 2\kappa(\A)cu \).
:::

::: {.idea}
There is nothing to do: backward stability says the computed answer solves a perturbed system exactly, and Chapter 16 already bounded the effect of perturbing \( \A \). The content of the theorem is the *translation*, not the estimate.
:::

::: {.proof}
Since \( \norm{\Delta\A}/\norm{\A} \le \eta \), we have \( \kappa(\A)\norm{\Delta\A}/\norm{\A} \le r < 1 \), so @thm-relative-error-bound (b), applied with \( \E = \Delta\A \), says that \( \A + \Delta\A \) is invertible and that
\[
\frac{\norm{\widehat\x - \x}}{\norm{\x}} \le \frac{r'}{1 - r'},
\qquad
r' \coloneqq \kappa(\A)\frac{\norm{\Delta\A}}{\norm{\A}} \le r .
\]
The function \( s \mapsto s/(1-s) \) is increasing on \( [0, 1) \), since its derivative \( (1-s)^{-2} \) is positive there, so \( r'/(1-r') \le r/(1-r) \). For the last claim put \( \eta = cu \); then \( r = \kappa(\A)cu \le \tfrac12 \) gives \( 1 - r \ge \tfrac12 \) and \( r/(1-r) \le 2r \). This proves the theorem.
:::

::: {.remark}
**When the right-hand side is perturbed too.** A solver for \( \A\x = \b \) normally perturbs the pair \( (\A, \b) \), returning \( \widehat\x \ne \0 \) with
\[
(\A + \Delta\A)\widehat\x = \b + \Delta\b,
\qquad
\norm{\Delta\A}_2 \le cu\norm{\A}_2,
\qquad
\norm{\Delta\b}_2 \le cu\norm{\b}_2 ,
\]
which is not literally the hypothesis above. One absorption repairs that. Put \( \Delta\A' = \Delta\A - \Delta\b\,\widehat\x^{*}/\norm{\widehat\x}_2^2 \); then \( (\A + \Delta\A')\widehat\x = \b + \Delta\b - \Delta\b = \b \), and the subtracted matrix is an outer product, of \( 2 \)-norm \( \norm{\Delta\b}_2/\norm{\widehat\x}_2 \). So @thm-forward-from-backward applies in the \( 2 \)-norm with
\[
\eta = cu\Bigl(1 + \frac{\norm{\b}_2}{\norm{\A}_2\norm{\widehat\x}_2}\Bigr)
\;\le\; cu\Bigl(1 + \frac{\norm{\x}_2}{\norm{\widehat\x}_2}\Bigr) ,
\]
the last step because \( \norm{\b}_2 = \norm{\A\x}_2 \le \norm{\A}_2\norm{\x}_2 \). That is a small multiple of \( cu \) as soon as the computed \( \widehat\x \) is not much shorter than \( \x \), and it is how every later appeal to the theorem for a linear solver is to be read.
:::

**Reading the bound in digits.** Suppose the arithmetic has \( u \approx 10^{-16} \) and the algorithm is backward stable with a modest \( c \). The bound then reads: relative forward error at most about \( \kappa(\A) \cdot 10^{-16} \). Taking logarithms, the computed answer may be wrong from about the \( \bigl(16 - \log_{10}\kappa(\A)\bigr) \)-th significant digit onward. This is the origin of the sentence "a stable solve loses about \( \log_{10}\kappa \) decimal digits". Two cautions, both real. It is an upper bound, so the loss may be smaller — Chapter 16 §08's warning that "the condition number bounds the error; it does not produce it" applies verbatim. And it is a statement about \( \kappa(\A) \) for the *problem as posed*: an algorithm that quietly poses a different problem pays that problem's condition number instead.

That last point is the whole of Chapter 16 §08's remaining ledger. Its third unpaid item read: "**Hence the comparison of the two algorithms** — that a stable implementation of the QR route loses about \( \log_{10}\kappa_2(\A) \) decimal digits while forming and solving the normal equations loses about \( 2\log_{10}\kappa_2(\A) \) — is still Chapter 24's to prove." The theorem above supplies the first half of the sentence for any backward stable method. Section 3 supplies the second half and the two algorithms, using Chapter 16's own @thm-normal-equations-squares-conditioning for the square.

::: {.check}
An algorithm for \( \A\x = \b \) is backward stable, \( \kappa(\A) = 10^{8} \), and \( u = 10^{-16} \). A user reports that the computed \( \widehat\x \) has only eight correct digits and concludes that the algorithm is broken. What is wrong with the conclusion?
:::

::: {.solution}
Nothing at all is wrong with the algorithm: @thm-forward-from-backward — applied after absorbing any perturbation of \( \b \) into \( \Delta\A \), as in the remark following it — predicts a relative forward error of about \( \kappa(\A)u = 10^{-8} \), up to the modest constant \( c \), which is exactly eight correct digits. The loss is charged to the problem, not to the method. Chapter 16 §08 put it as sharply as it can be put: with data of limited accuracy, an ill-conditioned answer *is not determined* to more digits than that, whatever anybody computes with.
:::

## Cancellation, and where the damage really happens

Backward stability is a property of a whole algorithm, and algorithms are usually wrecked in one place. That place is almost always a subtraction of two nearly equal numbers. The following example is the standard one, and it repays being done digit by digit.

::: {#exm-cancellation}
[Two ways to solve a quadratic]

In the six-digit decimal model of @exm-six-digit-model, find the two roots of
\[
x^2 - 10^{4}x + 1 = 0
\]
by the quadratic formula \( x_{\pm} = \tfrac12\bigl(10^4 \pm \sqrt{10^8 - 4}\bigr) \), and then again with the smaller root computed as \( x_- = 1/x_+ \). Compare with the exact roots.
:::

::: {.solution}
*The exact roots.* Their sum is \( 10^4 \) and their product is \( 1 \). Now \( 9999.9998^2 = 10^{8} - 4 + 4\times10^{-8} \), which is just above \( 10^8 - 4 \), so \( \sqrt{10^8 - 4} = 9999.99979999\ldots \) and
\[
x_+ = 9999.99989999\ldots,
\qquad
x_- = \frac{1}{x_+} = 1.0000000100\ldots \times 10^{-4} .
\]

*The formula, step by step.* Each line is one operation of the model.

- \( \fl(10^4 \times 10^4) = 10^{8} \), exactly representable, no error.
- \( \fl(10^{8} - 4) = \fl(99999996) = 1.00000 \times 10^{8} \), by @exm-six-digit-model. **Here the two informative digits are lost**, and the relative error committed is about \( 4 \times 10^{-8} \), comfortably inside \( u = 5 \times 10^{-6} \). The model is behaving perfectly.
- \( \fl(\sqrt{10^{8}}) = 10^{4} \), exactly.
- \( \fl(10^4 + 10^4) = 2 \times 10^4 \) and \( \fl(2\times10^4 \div 2) = 10^4 \): the computed \( x_+ \) is \( 10^{4} \), with relative error \( 10^{-8} \). Excellent.
- \( \fl(10^4 - 10^4) = 0 \), exactly, and \( \fl(0 \div 2) = 0 \): the computed \( x_- \) is \( \mathbf{0} \).

*The repair.* Compute \( x_+ = 10^4 \) as above, then \( \fl(1 \div 10^4) = 10^{-4} \), whose relative error against \( 1.00000001 \times 10^{-4} \) is \( 10^{-8} \).

*What to conclude.* The second route loses nothing; the first returns a root with no correct digit, indeed with no digits at all. And notice **where** the damage was done. The fatal subtraction \( 10^4 - 10^4 \) was performed **exactly**: both operands were representable and so was their difference. The error was already present, manufactured four lines earlier when \( 99999996 \) was rounded to \( 10^8 \), and the subtraction merely deleted the digits the two operands had in common, which was all of them. Cancellation does not create error. It *exposes* error, by deleting the digits that were correct and promoting the ones that were not.
:::

::: {.warning}
**A small residual is not a small error, and a small error is not a small residual.** For a computed solution \( \widehat\x \) of \( \A\x = \b \) with \( \widehat\x \ne \0 \), put \( \r = \b - \A\widehat\x \) and
\[
\Delta\A = \frac{\r\,\widehat\x^{*}}{\norm{\widehat\x}_2^2},
\qquad\text{so that}\qquad
(\A + \Delta\A)\widehat\x = \A\widehat\x + \r = \b ,
\]
and \( \norm{\Delta\A}_2 = \norm{\r}_2/\norm{\widehat\x}_2 \): Cauchy–Schwarz gives \( \le \), and \( \Delta\A\widehat\x = \r \) attains it — the computation is the one in the proof of @thm-residual-bound, with \( \b \) in place of \( \mu\widehat\x \). So a small relative residual *is* a small backward error, and nothing more: by @thm-forward-from-backward the forward error may still be \( \kappa(\A) \) times as large. In the other direction, an accurate \( \widehat\x \) for a badly scaled \( \A \) can have a residual far larger than one expects. Chapter 20 §04's @thm-residual-bound is the eigenvalue version of exactly this move, and that section named the technique: "An error analysis of this kind, which measures an answer by a change in the data that makes it exact, is a **backward error analysis**. Chapter 24 builds on it."
:::

## Exercises

### A. Check your understanding

:::: {#exr-floating-point-and-backward-error-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the three clauses of @def-floating-point-model, and say which one is an exclusion rather than an assumption about accuracy.
2. Define the unit roundoff, and give its value for a decimal model carrying \( t \) significant digits.
3. Define the forward error and the backward error of an algorithm at a datum, and say which of the two a user can usually measure.
4. Decide whether each statement is correct, with a reason: (i) "a backward stable algorithm returns an answer with small forward error"; (ii) "if the computed \( \widehat\x \) has a tiny residual, then \( \widehat\x \) is close to \( \x \)".
5. Why is @def-floating-point-model called a model rather than a theorem?
:::
::::

::: {.solution}
(a) (FP1) rounding is relative, with error at most \( u \); (FP2) each operation returns the rounding of its exact result, so \( \fl(x \odot y) = (x\odot y)(1+\delta) \) with \( \lvert\delta\rvert \le u \); (FP3) no overflow or underflow. (FP3) is the exclusion: it does not say the arithmetic is good, it says we decline to analyze the case where it is not.

(b) \( u \) is the bound in (FP1): \( \lvert \fl(t) - t\rvert \le u\lvert t\rvert \) for every in-range \( t \). For a decimal model with \( t \) significant digits, \( u = \tfrac12 \cdot 10^{1-t} \) (@exm-six-digit-model does the case \( t = 6 \)).

(c) See @def-forward-error. The forward error is \( \norm{\widehat f(\a) - f(\a)}/\norm{f(\a)} \), the backward error the smallest \( \norm{\Delta\a}/\norm{\a} \) with \( f(\a + \Delta\a) = \widehat f(\a) \). A user can usually measure neither directly, but the backward error is the one an analyst can *bound*, because a bound needs only one exhibited \( \Delta\a \); computing the forward error needs the exact answer, which is what the computation was for.

(d) (i) Incorrect. It returns an answer with small *backward* error; the forward error is then at most about \( \kappa \) times that, by @thm-forward-from-backward (after absorbing any perturbation of \( \b \), as the remark after that theorem does), and for large \( \kappa \) that is no guarantee at all. (ii) Incorrect, for the same reason: a small residual is a small backward error (see the warning above), which bounds the forward error only after multiplication by \( \kappa(\A) \).

(e) Because it is an assumption about a physical machine, not a consequence of anything proved earlier in the book. Nothing in Chapters 1 to 21 mentions rounding. Everything this chapter proves about arithmetic is a theorem *about the model*, true of any machine that satisfies it and silent about one that does not.
:::

### B. Practice

:::: {#exr-floating-point-and-backward-error-b1}
[B1: The \( \gamma \) calculus]

Assume \( (j + k)u < 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( 1 + \gamma_k = 1/(1 - ku) \).
2. Hence prove that \( \gamma_j + \gamma_k + \gamma_j\gamma_k \le \gamma_{j+k} \).
3. Explain in one sentence why (b) is the statement one needs when two separately analyzed computations are performed one after the other.
:::
::::

::: {.solution}
(a) \( 1 + \gamma_k = 1 + ku/(1-ku) = \bigl((1-ku) + ku\bigr)/(1-ku) = 1/(1-ku) \).

(b) Using (a) twice,
\[
1 + \gamma_j + \gamma_k + \gamma_j\gamma_k = (1+\gamma_j)(1+\gamma_k) = \frac{1}{(1-ju)(1-ku)} .
\]
Now \( (1-ju)(1-ku) = 1 - (j+k)u + jku^2 \ge 1 - (j+k)u > 0 \), and inverting reverses the inequality between positive numbers, so the right-hand side is at most \( 1/\bigl(1-(j+k)u\bigr) = 1 + \gamma_{j+k} \). Subtracting \( 1 \) gives the claim.

(c) If one stage multiplies the exact answer by \( 1 + \theta_1 \) with \( \lvert\theta_1\rvert \le \gamma_j \) and the next by \( 1 + \theta_2 \) with \( \lvert\theta_2\rvert \le \gamma_k \), the combined factor is \( 1 + \theta_1 + \theta_2 + \theta_1\theta_2 \), and (b) says the total is still of the form \( 1 + \theta \) with \( \lvert\theta\rvert \le \gamma_{j+k} \) — the counts simply add.
:::

:::: {#exr-floating-point-and-backward-error-b2}
[B2: Summation]

Let \( x_1, \dots, x_n \) be representable, let \( nu < 1 \), and let \( s_n \) be computed by \( s_1 = x_1 \), \( s_k = \fl(s_{k-1} + x_k) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( s_n = \sum_{k=1}^n x_k(1 + \theta_k) \) with \( \lvert\theta_k\rvert \le \gamma_{n-1} \).
2. Deduce \( \lvert s_n - \sum_k x_k\rvert \le \gamma_{n-1}\sum_k\lvert x_k\rvert \), and explain why this is **not** a bound on the relative error of \( s_n \).
3. Give three representable numbers in the six-digit model for which the computed sum has relative error larger than \( u \).
:::
::::

::: {.solution}
(a) By (FP2), \( s_k = (s_{k-1} + x_k)(1 + \varepsilon_k) \) for \( 2 \le k \le n \), with \( \lvert\varepsilon_k\rvert \le u \). Unrolling as in the proof of @thm-inner-product-backward-error,
\[
s_n = \sum_{k=1}^{n} x_k \prod_{j = \max(k,2)}^{n}(1 + \varepsilon_j) .
\]
The \( k = 1 \) and \( k = 2 \) terms carry \( n - 1 \) factors and the rest carry fewer, so @lem-gamma-bound gives \( \lvert\theta_k\rvert \le \gamma_{n-1} \).

(b) Subtract \( \sum_k x_k \) and use the triangle inequality: \( \lvert s_n - \sum_k x_k\rvert = \lvert\sum_k x_k\theta_k\rvert \le \gamma_{n-1}\sum_k\lvert x_k\rvert \). It is not a relative error bound because the right-hand side involves \( \sum_k\lvert x_k\rvert \), not \( \lvert\sum_k x_k\rvert \), and the two differ by an arbitrarily large factor when the \( x_k \) have mixed signs and cancel.

(c) Take \( x_1 = 1 \), \( x_2 = 10^{-7} \), \( x_3 = -1 \), summed in that order. Then \( \fl(1 + 10^{-7}) = 1 \), since \( 1 + 10^{-7} \) lies strictly between the representable neighbors \( 1 \) and \( 1.00001 \) and is nearer the first; and \( \fl(1 - 1) = 0 \). The computed sum is \( 0 \), the true sum is \( 10^{-7} \), and the relative error is \( 1 \). This is (b) at work: \( \sum\lvert x_k\rvert = 2 \) while \( \lvert\sum x_k\rvert = 10^{-7} \).
:::

:::: {#exr-floating-point-and-backward-error-b3}
[B3: The model by hand]

Work in the six-digit decimal model.

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \fl(1/3) \) and verify (FP1) for it.
2. Compute the two sides of \( \fl\bigl(\fl(a + b) + c\bigr) \) and \( \fl\bigl(a + \fl(b + c)\bigr) \) for \( a = 10^{5} \), \( b = 1 \), \( c = 1 \), and say what this shows about the model.
:::
::::

::: {.solution}
(a) \( 1/3 = 3.33333\overline{3} \times 10^{-1} \), so \( \fl(1/3) = 0.333333 \) and \( \lvert\fl(1/3) - 1/3\rvert = \tfrac13 \times 10^{-6} \). Dividing by \( 1/3 \) gives a relative error of \( 10^{-6} \), which is at most \( u = 5 \times 10^{-6} \).

(b) Left: \( \fl(10^5 + 1) = 100001 \) exactly (six digits), and \( \fl(100001 + 1) = 100002 \). Right: \( \fl(1 + 1) = 2 \), and \( \fl(10^5 + 2) = 100002 \). Here the two agree. Change \( a \) to \( 10^{6} \): left gives \( \fl(10^6 + 1) = 10^6 \), then \( \fl(10^6 + 1) = 10^{6} \); right gives \( \fl(1+1) = 2 \), then \( \fl(10^6 + 2) = 10^{6} \) as well, since \( 1000002 \) rounds to \( 1.00000 \times 10^6 \). Try \( a = 10^{6} \), \( b = c = 3 \): left is \( 10^6 \) then \( 10^{6} \); right is \( 6 \) then \( \fl(1000006) = 1.00001 \times 10^{6} \). The two differ. **Floating-point addition is commutative but not associative**, so the *order* of a summation is part of the algorithm, not an irrelevance — which is why @thm-inner-product-backward-error names the order it analyzes.
:::

### C. Going deeper

:::: {#exr-floating-point-and-backward-error-c1}
[C1: When backward stability says nothing]

Let \( \x, \y \in \nR^n \) and let \( s_n \) be the computed inner product of @thm-inner-product-backward-error.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \lvert s_n - \x\tp\y\rvert \le \gamma_n \lvert\x\rvert\tp\lvert\y\rvert \), where \( \lvert\cdot\rvert \) is entrywise.
2. Deduce that if all \( x_iy_i \ge 0 \) then the *relative* error of \( s_n \) is at most \( \gamma_n \).
3. Give \( \x, \y \in \nR^3 \) with representable entries, in the six-digit model, for which the relative error of \( s_n \) is at least \( 1 \). Explain why this does not contradict @thm-inner-product-backward-error.
:::
::::

::: {.solution}
(a) By the theorem's proof, \( s_n = \sum_k x_ky_k(1+\theta_k) \) with \( \lvert\theta_k\rvert \le \gamma_n \), so
\[
\lvert s_n - \x\tp\y\rvert = \Bigl\lvert\sum_k x_ky_k\theta_k\Bigr\rvert \le \gamma_n\sum_k\lvert x_k\rvert\lvert y_k\rvert = \gamma_n\lvert\x\rvert\tp\lvert\y\rvert .
\]

(b) If every \( x_ky_k \ge 0 \) then \( \lvert\x\rvert\tp\lvert\y\rvert = \sum_k x_ky_k = \x\tp\y \), so (a) reads \( \lvert s_n - \x\tp\y\rvert \le \gamma_n\,\x\tp\y \), which is the relative bound (and \( \x\tp\y > 0 \) unless every term vanishes, in which case \( s_n = 0 \) too).

(c) Take \( \x = (1, 10^{-7}, -1) \) and \( \y = (1, 1, 1) \), all representable. Each product \( x_ky_k \) is computed exactly, so \( \delta_1 = \delta_2 = \delta_3 = 0 \). Then \( s_1 = 1 \); next \( s_2 = \fl(1 + 10^{-7}) = 1 \), which is \( (1 + 10^{-7})(1 + \varepsilon_2) \) with
\[
\varepsilon_2 = \frac{-10^{-7}}{1 + 10^{-7}},
\qquad
\lvert\varepsilon_2\rvert < 10^{-7} < u ;
\]
finally \( s_3 = \fl(1 - 1) = 0 \), exactly, so \( \varepsilon_3 = 0 \) serves. The true value is \( \x\tp\y = 10^{-7} \), so the forward relative error is \( 1 \).

There is no contradiction. Following the proof, \( \theta_1 = \theta_2 = \varepsilon_2 \) and \( \theta_3 = 0 \), all of modulus below \( u \le \gamma_3 \), and indeed
\[
(1 + \varepsilon_2) + 10^{-7}(1 + \varepsilon_2) - 1 = (1 + 10^{-7})(1 + \varepsilon_2) - 1 = 0 = s_3 .
\]
So the backward perturbation \( \Delta\x = (\varepsilon_2, 10^{-7}\varepsilon_2, 0) \) is of relative size about \( 10^{-7} \) in every coordinate: the algorithm solved a neighboring problem exactly. What made the answer worthless is the *problem*, not the method: here \( \lvert\x\rvert\tp\lvert\y\rvert = 2 + 10^{-7} \) while \( \x\tp\y = 10^{-7} \), so part (a)'s bound is twenty million times the quantity being computed. This is the same phenomenon as @exm-cancellation, seen through the backward error.
:::

:::: {#exr-floating-point-and-backward-error-c2}
[C2: An unstable way to compute a variance]

Given \( x_1, \dots, x_N \) with mean \( \overline x = \tfrac1N\sum_i x_i \), the quantity \( S = \sum_i (x_i - \overline x)^2 \) can be computed in one pass as \( S = \sum_i x_i^2 - \tfrac1N\bigl(\sum_i x_i\bigr)^2 \), or in two passes by forming \( \overline x \) first.

::: {.enumerate options="label=(\alph*)"}
1. Verify the identity \( \sum_i (x_i - \overline x)^2 = \sum_i x_i^2 - \tfrac1N(\sum_i x_i)^2 \).
2. In the six-digit model, run both routes on \( x = (10000, 10001, 10002) \), showing every operation, and compare with the exact value \( S = 2 \).
3. Say which route is to be preferred and why, in the vocabulary of this section.
:::
::::

::: {.solution}
(a) Expand: \( \sum_i(x_i - \overline x)^2 = \sum_i x_i^2 - 2\overline x\sum_i x_i + N\overline x^2 \). Since \( \sum_i x_i = N\overline x \), the last two terms are \( -2N\overline x^2 + N\overline x^2 = -N\overline x^2 = -\tfrac1N(\sum_i x_i)^2 \).

(b) *One pass.* The squares are \( 10^{8} \), \( 100020001 \), \( 100040004 \); rounding each to six digits gives \( 1.00000\times10^{8} \), \( 1.00020 \times 10^{8} \) and \( 1.00040 \times 10^{8} \), and accumulating gives \( \fl(1.00000\times10^8 + 1.00020\times10^8) = 2.00020\times10^{8} \) and then \( 3.00060 \times 10^{8} \). The sum \( \sum_i x_i = 30003 \) is exact, its square is \( 900180009 \), which rounds to \( 9.00180 \times 10^{8} \), and dividing by \( 3 \) gives \( 3.00060 \times 10^{8} \). Subtracting: \( \fl(3.00060\times10^8 - 3.00060\times10^8) = \mathbf{0} \).

*Two passes.* \( \overline x = \fl(30003/3) = 10001 \), exactly. The deviations \( -1, 0, 1 \) are computed exactly, their squares are \( 1, 0, 1 \), and the sum is \( \mathbf{2} \), the exact answer.

(c) The two-pass route. The one-pass route subtracts two nine-digit numbers that agree in their first six digits, so in a six-digit model it commits catastrophic cancellation and returns \( 0 \); worse, \( 0 \) is not the value of \( S \) for *any* small relative perturbation of the data. Indeed \( S(\x + \Delta\x) = 0 \) forces the three perturbed entries to be equal, say to \( v \); and for \( \x = (10000, 10001, 10002) \) the largest of \( \lvert x_i - v\rvert \) is at least \( 1 \), whatever \( v \) is, because \( x_3 - x_1 = 2 \). So every \( \Delta\x \) that accounts for the computed answer has
\[
\frac{\norm{\Delta\x}_{\infty}}{\norm{\x}_{\infty}} \ge \frac{1}{10002} > 19\,u ,
\]
whereas @def-backward-stable allows \( cu \). One datum bounds the constant rather than disposing of it — what this shows exactly is that no \( c \le 19 \) will serve for the one-pass route — but the mechanism is general, and it is the one @exm-cancellation identified. The two-pass route performs the subtraction \( x_i - \overline x \) *first*, while the operands are still exactly representable, and nothing is ever lost. Same identity, same arithmetic, different algorithm — which is precisely the distinction between a problem and a method.
:::
