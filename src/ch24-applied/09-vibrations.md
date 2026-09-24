# Vibrations

Chapter 13 §04 diagonalized two forms at once and then said, in one sentence, what the theorem was for: for a vibrating structure one matrix is the mass matrix, the other the stiffness matrix, the generalized eigenvalues are the squared natural frequencies, and the eigenvectors are the normal modes. This section turns that sentence into a theorem and reads off its consequences. Everything in it is linear algebra already proved, applied to one physical model; the model is the only new ingredient, and it is stated as a model, not derived.

Throughout, the field is \( \nR \), and \( n \ge 1 \) is the number of moving masses.

**A note on the letter \( \K \).** In this section \( \K \) is the stiffness matrix. Chapter 19 §09's second-difference matrix always carries its size as a subscript, \( \K_n \), and it will appear below as exactly that; the two never collide.

## A chain of masses and springs

Picture \( n \) carts on a line, joined to each other and to two fixed walls by springs. Each cart is at rest in some position, and we track only its **displacement** from that position, so that the rest state is the zero vector. The question is what the system does when it is pushed and released.

\begin{center}
\begin{tikzpicture}[scale=0.9, lab/.style={font=\small}]
  \fill[pattern=north east lines] (-0.25,-0.5) rectangle (0,0.85);
  \draw[very thick] (0,-0.5) -- (0,0.85);
  \fill[pattern=north east lines] (8,-0.5) rectangle (8.25,0.85);
  \draw[very thick] (8,-0.5) -- (8,0.85);
  \draw[thick] (0,-0.5) -- (8,-0.5);
  \foreach \i/\xc in {1/2, 2/4, 3/6}{
    \draw[thick, fill=black!12] (\xc-0.5,-0.2) rectangle (\xc+0.5,0.6);
    \node[lab] at (\xc,0.2) {$m_\i$};
  }
  \draw[thick] (0,0.2) -- (0.3,0.2) -- (0.45,0.45) -- (0.75,-0.05) -- (1.05,0.45) -- (1.2,0.2) -- (1.5,0.2);
  \draw[thick] (2.5,0.2) -- (2.65,0.2) -- (2.78,0.45) -- (3,-0.05) -- (3.22,0.45) -- (3.35,0.2) -- (3.5,0.2);
  \draw[thick] (4.5,0.2) -- (4.65,0.2) -- (4.78,0.45) -- (5,-0.05) -- (5.22,0.45) -- (5.35,0.2) -- (5.5,0.2);
  \draw[thick] (6.5,0.2) -- (6.8,0.2) -- (6.95,0.45) -- (7.25,-0.05) -- (7.55,0.45) -- (7.7,0.2) -- (8,0.2);
  \node[lab] at (0.75,0.85) {$k_1$};
  \node[lab] at (3,0.85) {$k_2$};
  \node[lab] at (5,0.85) {$k_3$};
  \node[lab] at (7.25,0.85) {$k_4$};
  \draw[-latex] (2,-0.38) -- (2.7,-0.38);
  \node[lab] at (2.95,-0.38) {$x_1$};
\end{tikzpicture}
\end{center}

Two physical laws describe what happens, and both are assumptions, not theorems of this book. We give them a name and numbered clauses, so that the steps below can say which one they are using.

::: {#def-mass-spring-model}
[The mass–spring model]

::: {.enumerate options="label=(P\arabic*)"}
1. **(Newton's second law.)** A mass \( m_i > 0 \) whose displacement is \( x_i(t) \) obeys \( m_i x_i''(t) = f_i(t) \), where \( f_i \) is the total force on it.
2. **(Hooke's law.)** A spring of **stiffness** \( k \ge 0 \) whose two ends have moved by \( a \) and \( b \) pulls its ends together with force \( k(b - a) \) acting on the end at \( a \), and \( -k(b-a) \) on the end at \( b \). A wall is an end whose displacement is \( 0 \). A spring of stiffness \( 0 \) exerts no force whatever, so it is the same thing as no spring at all.
:::
:::

Hooke's law is an idealization: real springs obey it only for small displacements, and every real system also loses energy. We assume both laws exactly, and everything below is a theorem about that idealization; the energy loss reappears as the non-example below.

Take the chain in the picture: three masses \( m_1, m_2, m_3 \) and four springs \( k_1, \dots, k_4 \), with \( k_1 \) joining the left wall to mass \( 1 \) and \( k_4 \) joining mass \( 3 \) to the right wall. The force on mass \( 1 \) comes from the springs on either side of it, so by (P1) and (P2) of @def-mass-spring-model,
\[
\begin{aligned}
m_1x_1'' &= -k_1x_1 + k_2(x_2 - x_1) , \\
m_2x_2'' &= -k_2(x_2 - x_1) + k_3(x_3 - x_2) , \\
m_3x_3'' &= -k_3(x_3 - x_2) - k_4x_3 .
\end{aligned}
\]
Collecting the coefficients of \( x_1, x_2, x_3 \) on the right and moving the sign out front, this is \( \M\x'' = -\K\x \) with
\[
\M = \begin{pmatrix} m_1 & & \\ & m_2 & \\ & & m_3\end{pmatrix},
\quad
\K = \begin{pmatrix}
k_1 {+} k_2 & -k_2 & 0 \\
-k_2 & k_2 {+} k_3 & -k_3 \\
0 & -k_3 & k_3 {+} k_4
\end{pmatrix} .
\]
The matrix \( \M \) is diagonal with positive entries, hence positive definite. The matrix \( \K \) is symmetric, and it is positive semidefinite for a reason worth isolating, so we record the general shape first.

*A mass–spring system is a pair of forms: one that measures inertia and one that measures the price of a deformation.*

::: {#def-mass-spring-system}
[Mass–spring system]

A **mass–spring system** with \( n \) degrees of freedom is a pair of real symmetric matrices \( \M, \K \in M_n(\nR) \) with **\( \M \succ 0 \)** and **\( \K \succeq 0 \)**, called the **mass matrix** and the **stiffness matrix**. A **motion** of the system is a twice-differentiable function \( \x \colon \nR \to \nR^n \) with
\[
\M\x''(t) = -\K\x(t) \qquad \text{for every } t \in \nR .
\]{#eq-mass-spring}
The same equation is read for a function \( \x \colon \nR \to \nC^n \) whenever a complex trial solution is convenient; a **motion** without qualification is real.
:::

In words: \( \M \succ 0 \) says every direction of motion costs some inertia, so no coordinate is massless; \( \K \succeq 0 \) says no deformation releases energy, so the rest state \( \x = \0 \) is not a hilltop. The quantities \( \tfrac12(\x')\tp\M\x' \) and \( \tfrac12\x\tp\K\x \) are what the model calls the kinetic and potential energy of the state \( (\x, \x') \) — a third physical identification, on the same footing as (P1) and (P2) of @def-mass-spring-model and used nowhere in a proof — and the two definiteness hypotheses say exactly that the first is positive and the second non-negative away from rest.

For the chain, positive semidefiniteness of \( \K \) is a factorization. Number the springs \( 1, \dots, n+1 \) from left to right and let \( \B \in M_{(n+1) \times n}(\nR) \) be the matrix whose row \( e \) records how much spring \( e \) is stretched: for the chain above,
\[
\B = \begin{pmatrix}
1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \\ 0 & 0 & -1
\end{pmatrix},
\qquad
\K = \B\tp\D_k\B ,
\]
where \( \D_k = \diag(k_1, \dots, k_{n+1}) \). Multiplying out confirms the second identity entry by entry. Consequently
\[
\x\tp\K\x = (\B\x)\tp\D_k(\B\x) = \sum_{e} k_e\,(\B\x)_e^2 \ \ge\ 0 ,
\]
a sum of squares weighted by the stiffnesses: the potential energy stored in the springs. Together with \( \K\tp = \K \) this is @def-positive-semidefinite, so \( \K \succeq 0 \) with no computation of eigenvalues. (The matrix \( \B \) is, up to a transpose and the deletion of the two wall rows, the incidence matrix of Chapter 3 §07, @def-incidence-matrix, of the chain together with a choice of orientation for each spring: the orientation is what fixes the sign pattern of the rows, and it is what @def-incidence-matrix records as the head and the tail of an edge. The last section of this chapter takes that observation seriously.)

Three instances, simplest first.

::: {#exm-mass-spring-examples}
[Three systems]

::: {.enumerate options="label=(\alph*)"}
1. \( n = 1 \): one mass \( m \) between two walls with springs \( k_1, k_2 \). Then \( \M = (m) \) and \( \K = (k_1 + k_2) \), both \( 1 \times 1 \).
2. \( n = 3 \) with all masses equal to \( m \) and all four stiffnesses equal to \( k \). Then \( \M = m\I_3 \) and \( \K = k\K_3 \), where \( \K_3 \) is the second-difference matrix met in @prp-second-difference-inverse.
3. The **free** chain: the same three masses joined to each other by \( k_2, k_3 \) but with **no walls**, so \( k_1 = k_4 = 0 \). Then \( \K \) is still symmetric and still \( \B\tp\D_k\B \), hence \( \succeq 0 \), but now \( \K\1 = \0 \): sliding the whole chain sideways stretches nothing.
:::
:::

Case (c) is the degenerate one, and it is not a pathology to be excluded: it is why the definition asks only for \( \K \succeq 0 \). A system with a direction of zero stiffness has a motion that is not a vibration at all, and the theorem below will produce it.

Change one clause and the definition stops describing this situation. If a cart also feels friction proportional to its velocity, the equation becomes \( \M\x'' = -\K\x - \C\x' \) with \( \C \succeq 0 \) the damping matrix; the right-hand side is no longer a function of \( \x \) alone, @eq-mass-spring fails, and the analysis of this section does not apply to it. The models differ in exactly one term, and everything below uses the absence of that term.

::: {.warning}
**The natural frequencies are not the eigenvalues of \( \K \) divided by the eigenvalues of \( \M \).** Take \( \M = \diag(1, 4) \) and \( \K = \begin{psmallmatrix} 2 & -1 \\ -1 & 2\end{psmallmatrix} \). The eigenvalues of \( \K \) are \( 3 \) and \( 1 \), those of \( \M \) are \( 4 \) and \( 1 \), so the four available quotients are \( 3, 3/4, 1 \) and \( 1/4 \). The squared natural frequencies, computed from \( \det(\K - \lambda\M) = 4\lambda^2 - 10\lambda + 3 \), are
\[
\lambda = \tfrac{5 \pm \sqrt{13}}{4} \approx 2.151,\ 0.349 ,
\]
and neither is on the list. Mass and stiffness interact through their eigenvectors, not only through their eigenvalues; only when \( \M \) is a scalar multiple of \( \I \) does the naive rule hold.
:::

## Normal modes

A motion of one mass on one spring is a single oscillation. The hope is that a motion of \( n \) masses is a superposition of \( n \) such oscillations, each with its own frequency and its own shape. That hope is exactly @thm-simultaneous-congruence, and the only thing needed before it is the one-dimensional case.

::: {#lem-scalar-oscillator}
[The scalar oscillator]

Let \( \omega \ge 0 \) and let \( y \colon \nR \to \nC \) be twice differentiable with \( y'' = -\omega^2 y \). If \( \omega > 0 \), then
\[
y(t) = y(0)\cos\omega t + \frac{y'(0)}{\omega}\sin\omega t
\]
for every \( t \); if \( \omega = 0 \), then \( y(t) = y(0) + y'(0)t \). Conversely every function of these two shapes satisfies \( y'' = -\omega^2y \).
:::

::: {.idea}
A second-order scalar equation is a first-order system in the variable \( (y, y') \), which is the translation of @exm-second-order-scalar-ode. Once it is a system, @thm-linear-ode-solution supplies both existence and, what we actually want, uniqueness: two solutions with the same value and the same derivative at \( 0 \) are the same function.
:::

::: {.proof}
Put \( \N = \begin{psmallmatrix} 0 & 1 \\ -\omega^2 & 0\end{psmallmatrix} \) and \( \u = (y, y') \). Then \( \u' = (y', y'') = (y', -\omega^2 y) = \N\u \), and conversely a differentiable \( \u = (u_1, u_2) \) with \( \u' = \N\u \) has \( u_2 = u_1' \) and \( u_1'' = -\omega^2u_1 \). By @thm-linear-ode-solution there is exactly one differentiable \( \u \colon \nR \to \nC^2 \) with \( \u' = \N\u \) and a given value at \( 0 \).

For the converse half, \( (e^{zt})' = z e^{zt} \) for \( z \in \nC \), which is the \( 1 \times 1 \) case of @thm-exponential-properties (b); applying it twice, \( e^{\pm i\omega t} \) satisfies \( y'' = -\omega^2y \). Euler's formula — fact (A1) of Chapter 10 §09 — writes \( \cos\omega t \) and \( \sin\omega t \) as the combinations \( \tfrac12(e^{i\omega t} + e^{-i\omega t}) \) and \( \tfrac1{2i}(e^{i\omega t} - e^{-i\omega t}) \), so both satisfy it too, as does every linear combination of them; and for \( \omega = 0 \) the functions \( 1 \) and \( t \) satisfy \( y'' = 0 \).

Now let \( y \) be any solution and let \( z \) be the function displayed in the statement. By the previous paragraph \( z \) is a solution. Differentiating, \( z(0) = y(0) \) and \( z'(0) = y'(0) \) in both cases, the case \( \omega > 0 \) using \( (\sin\omega t)' = \omega\cos\omega t \) at \( t = 0 \). So \( (y, y') \) and \( (z, z') \) solve \( \u' = \N\u \) with the same value at \( 0 \), and uniqueness gives \( y = z \). This proves the lemma.
:::

Now the main theorem. Read the substitution in part (a) as a question: is there a motion in which every mass moves with the *same* time dependence, so that the shape of the deformation never changes and only its amplitude does?

::: {#thm-normal-modes}
[Normal Modes]

Let \( (\M, \K) \) be a mass–spring system with \( n \) degrees of freedom (@def-mass-spring-system).

::: {.enumerate options="label=(\alph*)"}
1. For \( \omega \in \nR \) and \( \v \in \nR^n \) with \( \v \ne \0 \), the complex-valued function \( \x(t) = e^{i\omega t}\v \) satisfies @eq-mass-spring if and only if
\[
\K\v = \omega^2\M\v .
\]
2. There are real numbers \( 0 \le \omega_1 \le \dots \le \omega_n \) and vectors \( \v_1, \dots, \v_n \in \nR^n \) with
\[
\K\v_j = \omega_j^2\M\v_j
\quad\text{and}\quad
\v_i\tp\M\v_j = \delta_{ij} ,
\]
and \( (\v_1, \dots, \v_n) \) is a basis of \( \nR^n \).
3. Every motion of the system is
\[
\x(t) = \sum_{j=1}^{n} c_j(t)\,\v_j ,
\]
where
\[
c_j(t) = \begin{cases}
a_j\cos\omega_jt + b_j\sin\omega_jt, & \omega_j > 0, \\
a_j + b_jt, & \omega_j = 0,
\end{cases}
\]
for uniquely determined real \( a_j, b_j \); conversely every such function is a motion. The coefficients are \( a_j = \v_j\tp\M\x(0) \), and \( b_j = \v_j\tp\M\x'(0)/\omega_j \) when \( \omega_j > 0 \), \( b_j = \v_j\tp\M\x'(0) \) when \( \omega_j = 0 \).
:::

The numbers \( \omega_j \) do not depend on the construction in (b): by @thm-generalized-eigenvalues-real (b) the \( \omega_j^2 \) are exactly the roots of \( \det(\K - \lambda\M) \), with multiplicity. They are the **natural frequencies**, and the pairs \( (\omega_j, \v_j) \) are the **normal modes** of the system.
:::

::: {.idea}
Part (a) is one differentiation. Part (b) is Chapter 13 §04 verbatim: \( \M \succ 0 \) is the hypothesis of @thm-simultaneous-congruence, and the columns of the congruence it produces are \( \M \)-orthonormal generalized eigenvectors by @thm-generalized-eigenvalues-real; all that has to be added is that the generalized eigenvalues are \( \ge 0 \), which is where \( \K \succeq 0 \) is spent. Part (c) then costs nothing: expanding \( \x \) in the basis \( (\v_j) \) turns @eq-mass-spring into \( n \) *separate* scalar equations, one per mode, and @lem-scalar-oscillator solves each.
:::

::: {.proof}
(a) Differentiating twice, \( \x''(t) = -\omega^2e^{i\omega t}\v \), so
\[
\M\x''(t) + \K\x(t) = e^{i\omega t}\bigl(\K\v - \omega^2\M\v\bigr) .
\]
Since \( e^{i\omega t} \ne 0 \) for every \( t \), the left side vanishes for every \( t \) if and only if \( \K\v = \omega^2\M\v \).

(b) The matrices \( \M \) and \( \K \) are real symmetric and \( \M \succ 0 \), so @thm-simultaneous-congruence gives a real invertible \( \S \) with \( \S\tp\M\S = \I_n \) and \( \S\tp\K\S = \D = \diag(d_1, \dots, d_n) \), the \( d_j \) real. Let \( \s_1, \dots, \s_n \) be the columns of \( \S \). By @thm-generalized-eigenvalues-real (a), \( \K\s_j = d_j\M\s_j \) and \( \s_i\tp\M\s_j = \delta_{ij} \). Each \( d_j \) is non-negative: the \( (j,j) \) entry of \( \S\tp\K\S \) is \( d_j = \s_j\tp\K\s_j \ge 0 \), because \( \K \succeq 0 \). Put \( \omega_j = \sqrt{d_j} \ge 0 \), and relabel the columns so that \( \omega_1 \le \dots \le \omega_n \); relabeling preserves both displayed properties. The list \( (\v_1, \dots, \v_n) \) obtained is the list of columns of an invertible matrix, hence a basis of \( \nR^n \).

(c) *Every such function is a motion.* Let \( c_j \) be as displayed. By @lem-scalar-oscillator, \( c_j'' = -\omega_j^2c_j \). Hence, differentiating the sum termwise,
\[
\M\x'' = \sum_j c_j''\,\M\v_j
 = -\sum_j \omega_j^2 c_j\,\M\v_j
 = -\sum_j c_j\,\K\v_j = -\K\x ,
\]
where the third equality is (b).

*Every motion is such a function.* Let \( \x \) be a motion. Since \( (\v_j) \) is a basis, write \( \x(t) = \sum_j u_j(t)\v_j \). Pairing with \( \M\v_j \) and using (b) gives \( u_j(t) = \v_j\tp\M\x(t) \), a fixed linear combination of the entries of \( \x \), so each \( u_j \) is twice differentiable. Substituting into @eq-mass-spring and using (b),
\[
\sum_j \bigl(u_j'' + \omega_j^2u_j\bigr)\M\v_j = \0 .
\]
The vectors \( \M\v_1, \dots, \M\v_n \) are independent, since \( \M \) is invertible and the \( \v_j \) are independent, so every coefficient vanishes: \( u_j'' = -\omega_j^2u_j \) for each \( j \). By @lem-scalar-oscillator each \( u_j \) has the displayed shape, with \( a_j = u_j(0) \) and \( b_j = u_j'(0)/\omega_j \) or \( u_j'(0) \).

*The coefficients.* Pairing \( \x(0) = \sum_i a_i\v_i \) with \( \M\v_j \) and using \( \v_j\tp\M\v_i = \delta_{ij} \) gives \( \v_j\tp\M\x(0) = a_j \); the same computation on \( \x'(0) = \sum_i u_i'(0)\v_i \) gives \( \v_j\tp\M\x'(0) = u_j'(0) \). Uniqueness of \( a_j, b_j \) follows, since they are determined by \( \x(0) \) and \( \x'(0) \). This proves the theorem.
:::

So the general motion has \( 2n \) real parameters, and the modes evolve independently. Mode \( j \) is a motion in which every mass oscillates at the single frequency \( \omega_j \), with relative displacements fixed by \( \v_j \); the sign pattern of \( \v_j \) says which masses move together and which move against each other.

::: {.check}
Why is the normalization \( \v_i\tp\M\v_j = \delta_{ij} \), and not \( \v_i\tp\v_j = \delta_{ij} \)? Which step of the proof would fail?
:::

::: {.solution}
The step reading off the coefficients. What is available is \( \S\tp\M\S = \I \), which says the \( \v_j \) are orthonormal for the inner product \( \inner{\x}{\y}_{\M} = \y\tp\M\x \) of @thm-generalized-eigenvalues-real (a), not for the standard one. Generalized eigenvectors for *different* \( \omega_j \) need not be orthogonal in the standard sense, and a genuine mass–spring system already shows it: for \( \M = \diag(2,1) \) and \( \K = \begin{psmallmatrix} 3 & -1 \\ -1 & 1\end{psmallmatrix} \) the modes are the multiples of \( (1,2) \), for \( \omega^2 = \tfrac12 \), and of \( (1,-1) \), for \( \omega^2 = 2 \); and \( (1,2)\tp\M(1,-1) = 0 \) while \( (1,2)\cdot(1,-1) = -1 \ne 0 \). So here the two normalizations cannot both be imposed: rescaling the \( \v_j \) to standard unit length keeps them generalized eigenvectors but destroys \( \v_i\tp\M\v_j = \delta_{ij} \), and the pairing step then has no \( \delta_{ij} \) to use. (When \( \M = c\I \) the two conditions differ by a constant only, and both can be met at once.)
:::

::: {#exm-three-mass-chain}
[Three equal masses, four equal springs]

Take \( n = 3 \) with every mass \( m \) and every stiffness \( k \), so that \( \M = m\I_3 \) and \( \K = k\K_3 \) as in @exm-mass-spring-examples (b). Find the natural frequencies and the normal modes of @thm-normal-modes.
:::

::: {.solution}
*The pencil.* Here \( \K\v = \omega^2\M\v \) reads \( k\K_3\v = m\omega^2\v \), an ordinary eigenvalue problem for the symmetric matrix
\[
\K_3 = \begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2\end{pmatrix},
\]
with \( \omega^2 = (k/m)\mu \) for \( \mu \) an eigenvalue of \( \K_3 \).

*Eigenvalues.* Expanding along the first row, \( \det(\K_3 - \mu\I) = (2-\mu)^3 - 2(2-\mu) = (2-\mu)\bigl((2-\mu)^2 - 2\bigr) \), so
\[
\mu = 2 - \sqrt2, \qquad \mu = 2, \qquad \mu = 2 + \sqrt2 .
\]

*Eigenvectors.* For \( \mu = 2 \) the first row of \( \K_3 - 2\I \) gives \( -v_2 = 0 \) and the second gives \( -v_1 - v_3 = 0 \), so \( \v \propto (1, 0, -1) \). For \( \mu = 2 \mp \sqrt2 \), so that \( 2 - \mu = \pm\sqrt2 \), the first row reads \( (2-\mu)v_1 - v_2 = 0 \) and the third reads \( -v_2 + (2-\mu)v_3 = 0 \), giving \( v_2 = \pm\sqrt2\,v_1 \) and \( v_2 = \pm\sqrt2\,v_3 \), so \( \v \propto (1, \pm\sqrt2, 1) \). The middle row is then automatic: it reads \( -1 + (2-\mu)(\pm\sqrt2) - 1 = -2 + 2 = 0 \). Direct substitution confirms all three.

*Normalizing.* Since \( \M = m\I_3 \), the condition \( \v\tp\M\v = 1 \) is \( m\norm{\v}^2 = 1 \). The squared lengths are \( 4, 2, 4 \), so
\[
\v_1 = \tfrac{1}{2\sqrt m}\begin{pmatrix} 1 \\ \sqrt2 \\ 1\end{pmatrix},
\quad
\v_2 = \tfrac{1}{\sqrt{2m}}\begin{pmatrix} 1 \\ 0 \\ -1\end{pmatrix},
\quad
\v_3 = \tfrac{1}{2\sqrt m}\begin{pmatrix} 1 \\ -\sqrt2 \\ 1\end{pmatrix},
\]
and the natural frequencies are
\[
\omega_1 = \sqrt{\tfrac km}\sqrt{2 - \sqrt2},
\quad
\omega_2 = \sqrt{\tfrac km}\sqrt2,
\quad
\omega_3 = \sqrt{\tfrac km}\sqrt{2 + \sqrt2} ,
\]
approximately \( 0.765, 1.414 \) and \( 1.848 \) times \( \sqrt{k/m} \).

*Reading the modes.* In mode \( 1 \) all three masses move the same way, the middle one furthest: the slowest and softest motion. In mode \( 2 \) the middle mass stands still and the outer two move oppositely. In mode \( 3 \) neighbors always move oppositely, which stretches every spring at once and costs the most: the fastest motion. The number of sign changes along the chain increases with the frequency. That is a general phenomenon for such chains, an oscillation theorem for tridiagonal stiffness matrices; nothing in this section uses it, and this book does not prove it.
:::

## Frequencies as a minimum

@thm-normal-modes computes the frequencies exactly, at the price of solving an \( n \)-th degree equation. Often one wants instead a cheap estimate of the lowest frequency, and a way to say how it responds to a change in the design. Both come from a quotient.

::: {#def-generalized-rayleigh-quotient}
[Generalized Rayleigh quotient]

Let \( (\M, \K) \) be a mass–spring system. Its **generalized Rayleigh quotient** is
\[
\rho(\v) \coloneqq \frac{\v\tp\K\v}{\v\tp\M\v} ,
\]
defined for every \( \v \in \nR^n \) with **\( \v \ne \0 \)**, and at no other vector.
:::

The denominator is non-zero exactly because \( \M \succ 0 \), which is the role definiteness played in @def-rayleigh-quotient; for \( \M = \I \) the two definitions agree. Physically \( \rho(\v) \) is the potential energy of the deformation \( \v \) divided by the kinetic energy of the velocity \( \v \): the stiffness-to-inertia ratio of the shape \( \v \). It is unchanged by scaling, since both numerator and denominator pick up \( c^2 \).

::: {#cor-rayleigh-frequency-bounds}
[Frequencies from the Rayleigh Quotient]

Let \( (\M, \K) \) be a mass–spring system with natural frequencies \( \omega_1 \le \dots \le \omega_n \). Then for every \( j \),
\[
\begin{aligned}
\omega_j^2 &= \min_{\dim W = j}\ \ \max_{\0 \ne \v \in W}\ \rho(\v) \\
&= \max_{\dim W = n-j+1}\ \ \min_{\0 \ne \v \in W}\ \rho(\v) ,
\end{aligned}
\]
\( W \) running over all subspaces of \( \nR^n \) of the stated dimension. In particular
\[
\omega_1^2 = \min_{\v \ne \0}\rho(\v),
\qquad
\omega_n^2 = \max_{\v \ne \0}\rho(\v) ,
\]
and every \( \v \ne \0 \) gives the upper bound \( \omega_1^2 \le \rho(\v) \), with equality exactly when \( \v \) is a generalized eigenvector for \( \omega_1 \).
:::

::: {.idea}
The congruence \( \S \) of @thm-normal-modes turns \( \rho \) into the ordinary Rayleigh quotient of the diagonal matrix \( \D \): substituting \( \v = \S\y \) replaces the numerator by \( \y\tp\D\y \) and the denominator by \( \y\tp\y \). Since \( \S \) is invertible it matches subspaces of dimension \( j \) with subspaces of dimension \( j \), so an optimization over subspaces is carried across unchanged, and @thm-courant-fischer applies. The only care needed is the index: Chapter 17 orders eigenvalues **decreasingly** and frequencies are ordered **increasingly**, so \( \omega_j^2 = \lambda_{n-j+1}(\D) \).
:::

::: {.proof}
Let \( \S \) and \( \D = \diag(d_1, \dots, d_n) \) be as in the proof of @thm-normal-modes, so \( \S\tp\M\S = \I_n \), \( \S\tp\K\S = \D \), and the multiset \( \{d_1, \dots, d_n\} \) is \( \{\omega_1^2, \dots, \omega_n^2\} \). For \( \y \ne \0 \) put \( \v = \S\y \), which is non-zero because \( \S \) is invertible. Then
\[
\rho(\S\y) = \frac{\y\tp\S\tp\K\S\y}{\y\tp\S\tp\M\S\y}
= \frac{\y\tp\D\y}{\y\tp\y} = R_{\D}(\y) ,
\]
the last step by @def-rayleigh-quotient, \( \D \) being real diagonal and hence Hermitian.

Fix \( j \) and put \( k = n - j + 1 \). Sorting \( d_1, \dots, d_n \) decreasingly as in Chapter 17 makes \( \lambda_k(\D) \) the \( j \)-th smallest of them, that is \( \lambda_k(\D) = \omega_j^2 \). By @thm-courant-fischer,
\[
\omega_j^2 = \lambda_k(\D) = \min_{\dim W' = n-k+1}\ \max_{\0 \ne \y \in W'} R_{\D}(\y) ,
\]
and \( n - k + 1 = j \). The map \( W' \mapsto \S W' \) is a bijection from the \( j \)-dimensional subspaces of \( \nR^n \) to themselves, since \( \S \) is invertible, and it carries the non-zero vectors of \( W' \) onto those of \( \S W' \); combined with the displayed identity \( \rho(\S\y) = R_{\D}(\y) \), the inner maximum over \( W' \) for \( R_{\D} \) equals the inner maximum over \( \S W' \) for \( \rho \). Hence the two outer minima agree, which is the first line. The second line is the second equality of @thm-courant-fischer transported in the same way, with \( n - k + 1 \) replaced by \( k = n-j+1 \).

For the particular cases, take \( j = 1 \) and \( j = n \) in the second and the first line respectively, where the only admissible \( W \) is \( \nR^n \) itself. Equality in \( \omega_1^2 \le \rho(\v) \) holds exactly when \( \y = \S^{-1}\v \) attains the minimum of \( R_{\D} \), and that happens exactly at the eigenvectors of \( \D \) for its smallest eigenvalue. In one direction, such an eigenvector attains the minimum by @prp-rayleigh-basic. Conversely, suppose \( \y \ne \0 \) attains it; replacing \( \y \) by \( \y/\norm{\y} \) changes nothing, since \( R_{\D}(c\y) = R_{\D}(\y) \) for \( c \ne 0 \) directly from @def-rayleigh-quotient, so we may take \( \y \) to be a unit vector. Then @prp-rayleigh-critical-points (b) applies in its minimum form and gives the condition of its part (a), whence \( \D\y = R_{\D}(\y)\y \) by that part, and \( R_{\D}(\y) = \lambda_n(\D) \) is the smallest eigenvalue by @prp-rayleigh-basic. Multiplying by \( \S \) turns these into the generalized eigenvectors for \( \omega_1 \), by @thm-generalized-eigenvalues-real (a). This proves the corollary.
:::

The practical content is the last sentence: **any** shape you can guess gives an upper bound for the lowest squared frequency, and the bound is good even when the guess is mediocre, because the quotient is flat at a minimum.

::: {#exm-rayleigh-estimate-lowest-mode}
[Guessing the lowest mode of the chain]

For the chain of @exm-three-mass-chain with \( k = m = 1 \), estimate \( \omega_1^2 \) by guessing a shape, without computing any eigenvalue.
:::

::: {.solution}
The lowest mode should have all three masses moving together, so try \( \g = (1,1,1) \). Then \( \K_3\g = (1, 0, 1) \), so
\[
\rho(\g) = \frac{\g\tp\K_3\g}{\g\tp\g} = \frac{2}{3} \approx 0.6667 .
\]
The true value is \( 2 - \sqrt2 \approx 0.5858 \), so the guess overestimates by about \( 14\% \) — and, by @cor-rayleigh-frequency-bounds, it is certainly an overestimate.

Refine it: the middle mass should swing furthest, so try \( \g = (2, 3, 2) \). Now \( \K_3\g = (1, 2, 1) \), and
\[
\rho(\g) = \frac{2 + 6 + 2}{4 + 9 + 4} = \frac{10}{17} \approx 0.5882 .
\]
The error has fallen to about \( 0.4\% \). The exact mode is \( (1, \sqrt2, 1) \propto (2, 2\sqrt2, 2) \) and \( 2\sqrt2 \approx 2.83 \), so the guess \( (2,3,2) \) is still off by about \( 6\% \) in its middle entry: the *shape* is wrong by \( 6\% \) and the *frequency* by \( 0.4\% \). Squaring the error in the shape is exactly what @prp-rayleigh-critical-points predicts near a critical point of the quotient.
:::

::: {.check}
The guess \( \g = (1, 2, 1) \) also gives \( \rho(\g) = 2/3 \), the same as \( (1,1,1) \), although \( (1,2,1) \) is much closer to the true mode \( (1,\sqrt2,1) \). Is that a contradiction?
:::

::: {.solution}
No. \( \K_3(1,2,1) = (0, 2, 0) \), so \( \rho = 4/6 = 2/3 \). Both guesses lie on the same level set of \( \rho \), and a level set is not a sphere around the minimizer: the quotient measures a ratio of energies, not a distance to \( \v_1 \). Being closer to the true mode in the Euclidean sense does not force a smaller value, only being closer *in the right directions* does. What @cor-rayleigh-frequency-bounds guarantees is one-sided, that both values are \( \ge 2 - \sqrt2 \), and both are.
:::

## Stiffer, heavier, pinned

The min–max description compares two systems, because the family of subspaces it runs over does not depend on the matrices. Three design changes can now be read off.

::: {#prp-frequency-monotonicity}
[Stiffening Raises, Loading Lowers]

Let \( (\M, \K) \) and \( (\M', \K') \) be mass–spring systems with \( n \) degrees of freedom, with natural frequencies \( \omega_j \) and \( \omega_j' \).

::: {.enumerate options="label=(\alph*)"}
1. If \( \M' = \M \) and \( \K' \succeq \K \), then \( \omega_j' \ge \omega_j \) for every \( j \).
2. If \( \K' = \K \) and \( \M' \succeq \M \), then \( \omega_j' \le \omega_j \) for every \( j \).
:::
:::

::: {.idea}
Both are the same one-line observation: the hypothesis makes \( \rho' \) compare with \( \rho \) at **every** vector, and a min–max of a larger function is larger. In (b) the numerator must be non-negative before enlarging the denominator helps, and that is exactly the hypothesis \( \K \succeq 0 \) from @def-mass-spring-system.
:::

::: {.proof}
(a) Let \( \v \ne \0 \). By @def-loewner-order, \( \v\tp\K'\v \ge \v\tp\K\v \), and the two quotients have the same positive denominator \( \v\tp\M\v \), so \( \rho'(\v) \ge \rho(\v) \). Fix \( j \) and a subspace \( W \) of dimension \( j \). Then \( \max_{\0\ne\v\in W}\rho'(\v) \ge \max_{\0\ne\v\in W}\rho(\v) \), since the maximum of the larger function over the same set is larger; taking the minimum over all such \( W \) preserves the inequality. By @cor-rayleigh-frequency-bounds applied to each system, the two sides are \( (\omega_j')^2 \) and \( \omega_j^2 \). Both frequencies are \( \ge 0 \), so \( \omega_j' \ge \omega_j \).

(b) Let \( \v \ne \0 \). Now \( \v\tp\M'\v \ge \v\tp\M\v > 0 \) by @def-loewner-order and \( \M \succ 0 \), while the common numerator satisfies \( \v\tp\K\v \ge 0 \) because \( \K \succeq 0 \). Increasing a positive denominator does not increase a non-negative fraction, so \( \rho'(\v) \le \rho(\v) \), and the argument of (a) runs in reverse. This proves the proposition.
:::

Part (b) needs \( \K \succeq 0 \) and not merely \( \K = \K\tp \): for a \( 1 \times 1 \) system with \( \K = (-1) \), replacing \( \M = (1) \) by \( \M' = (4) \) moves the quotient from \( -1 \) up to \( -1/4 \). Such a \( \K \) is not a stiffness matrix, and the definition excludes it for this reason among others.

The third change is to hold one mass still — to **pin** it. Constraining \( x_p = 0 \) leaves a system with \( n - 1 \) degrees of freedom whose matrices are obtained by deleting row and column \( p \).

::: {#prp-pinning-interlaces .optional}
[Pinning Interlaces the Frequencies]

Let \( (\M, \K) \) be a mass–spring system with \( n \ge 2 \) degrees of freedom and natural frequencies \( \omega_1 \le \dots \le \omega_n \). Fix \( p \), let \( I = \{1, \dots, n\}\setminus\{p\} \), and let \( \M' = \M_{I,I} \) and \( \K' = \K_{I,I} \) be the principal submatrices on \( I \). Then \( (\M', \K') \) is a mass–spring system with \( n-1 \) degrees of freedom, and its natural frequencies \( \mu_1 \le \dots \le \mu_{n-1} \) satisfy
\[
\omega_j \ \le\ \mu_j \ \le\ \omega_{j+1}
\qquad (1 \le j \le n-1) .
\]
:::

::: {.idea}
Pinning restricts the competition to the hyperplane \( H = \{\v : v_p = 0\} \). A subspace of \( H \) is a subspace of \( \nR^n \), so the min–max for the pinned system runs over *fewer* competitors than the one for the full system; that gives the left inequality at index \( j \) and, after the dimension count that makes @thm-cauchy-interlacing work, the right one at index \( j+1 \).
:::

::: {.proof}
Let \( H = \{\v \in \nR^n : v_p = 0\} \) and let \( \varphi \colon H \to \nR^{n-1} \) delete the \( p \)-th coordinate, a linear isomorphism. For \( \v \in H \) with coordinates \( \y = \varphi(\v) \), the terms of \( \v\tp\M\v \) involving index \( p \) all vanish, so
\[
\v\tp\M\v = \y\tp\M'\y,
\qquad
\v\tp\K\v = \y\tp\K'\y ,
\]
Both \( \M' \) and \( \K' \) are symmetric, being principal submatrices of symmetric matrices, and the displays give \( \y\tp\M'\y > 0 \) for \( \y \ne \0 \) and \( \y\tp\K'\y \ge 0 \) for all \( \y \), since \( \varphi \) is onto and \( \varphi^{-1}(\y) \ne \0 \) for \( \y \ne \0 \); so \( \M' \succ 0 \) and \( \K' \succeq 0 \) by @def-positive-semidefinite, and \( (\M', \K') \) is a mass–spring system. Writing \( \rho \) and \( \rho' \) for the two generalized Rayleigh quotients, the two displays give
\[
\rho(\v) = \rho'(\varphi(\v)) \qquad \text{for } \0 \ne \v \in H .
\]

Fix \( j \) with \( 1 \le j \le n-1 \).

\( (\omega_j \le \mu_j) \) By @cor-rayleigh-frequency-bounds for the pinned system there is a subspace \( W' \le \nR^{n-1} \) with \( \dim W' = j \) and \( \mu_j^2 = \max_{\0\ne\y\in W'}\rho'(\y) \). Put \( W = \varphi^{-1}(W') \le H \le \nR^n \), of dimension \( j \). Then \( \max_{\0\ne\v\in W}\rho(\v) = \mu_j^2 \), and \( W \) is one of the competitors in the min–max for \( \omega_j^2 \), so \( \omega_j^2 \le \mu_j^2 \).

\( (\mu_j \le \omega_{j+1}) \) By the max–min line of @cor-rayleigh-frequency-bounds for the pinned system there is a subspace \( W' \le \nR^{n-1} \) with \( \dim W' = (n-1) - j + 1 = n-j \) and \( \mu_j^2 = \min_{\0\ne\y\in W'}\rho'(\y) \). Put \( W = \varphi^{-1}(W') \le \nR^n \), of dimension \( n - j = n - (j+1) + 1 \), which is the dimension the max–min line for \( \omega_{j+1}^2 \) asks for. Hence
\[
\omega_{j+1}^2 \ \ge\ \min_{\0\ne\v\in W}\rho(\v) = \mu_j^2 .
\]
All frequencies being \( \ge 0 \), taking square roots preserves both inequalities. This proves the proposition.
:::

::: {#exm-pinning-the-chain}
[Pinning the middle mass]

In @exm-three-mass-chain with \( k = m = 1 \), hold mass \( 2 \) fixed. Deleting row and column \( 2 \) from \( \K_3 \) and from \( \I_3 \) gives \( \K' = \diag(2, 2) \) and \( \M' = \I_2 \), so the pinned frequencies are \( \mu_1 = \mu_2 = \sqrt2 \). The unpinned ones are \( \sqrt{2-\sqrt2} \approx 0.765 \), \( \sqrt2 \approx 1.414 \) and \( \sqrt{2+\sqrt2} \approx 1.848 \), and indeed
\[
0.765 \le 1.414 \le 1.414 \le 1.414 \le 1.848 ,
\]
which is @prp-pinning-interlaces, here with two of the four inequalities equalities. The answer is also visible: with the middle mass pinned, the two outer masses no longer interact, and each is a single mass between two unit springs, of frequency \( \sqrt2 \).
:::

Three sentences summarize the section. A structure's frequencies are the generalized eigenvalues of a definite pencil, and its modes are an \( \M \)-orthonormal basis, so its motion decouples completely. Each frequency is a min–max of one explicit quotient, so a guessed shape bounds the lowest one from above. And because the min–max runs over a family of subspaces that does not mention the matrices, making a structure stiffer raises every frequency, making it heavier lowers every frequency, and pinning a point interlaces them.

## Exercises

### A. Check your understanding

:::: {#exr-vibrations-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the two hypotheses on \( \M \) and \( \K \) in @def-mass-spring-system, and say which one guarantees that \( \rho(\v) \) is defined for every \( \v \ne \0 \).
2. State @thm-normal-modes (b), including the normalization of the eigenvectors.
3. A system has \( \K \) invertible. What does @thm-normal-modes say about \( \omega_1 \)? What if \( \K \) is singular?
4. True or false: if every stiffness \( k_e \) of a chain is doubled and every mass is left alone, every natural frequency is multiplied by \( \sqrt2 \). Justify your answer.
5. True or false: for \( \M = \diag(1,4) \) the squared natural frequencies are the eigenvalues of \( \K \) divided by \( 1 \) and by \( 4 \) in some order. Justify your answer.
:::
::::

::: {.solution}
(a) \( \M \succ 0 \) and \( \K \succeq 0 \), both symmetric. It is \( \M \succ 0 \) that makes the denominator \( \v\tp\M\v \) non-zero, hence positive, for every \( \v \ne \0 \).

(b) There are \( 0 \le \omega_1 \le \dots \le \omega_n \) and a basis \( \v_1, \dots, \v_n \) of \( \nR^n \) with \( \K\v_j = \omega_j^2\M\v_j \) and \( \v_i\tp\M\v_j = \delta_{ij} \): the eigenvectors are orthonormal for the \( \M \)-inner product, not for the standard one.

(c) If \( \K \) is invertible then no \( \omega_j \) is \( 0 \): \( \omega_j = 0 \) would give \( \K\v_j = \0 \) with \( \v_j \ne \0 \). So \( \omega_1 > 0 \) and every motion is a genuine oscillation. If \( \K \) is singular then some \( \omega_j = 0 \), and by @thm-normal-modes (c) there are motions containing a term \( b_jt\,\v_j \), which grow without bound: a drift, not a vibration.

(d) True. Replacing \( \K \) by \( 2\K \) multiplies \( \rho \) by \( 2 \) at every vector, hence multiplies every min–max by \( 2 \) (@cor-rayleigh-frequency-bounds), hence every \( \omega_j^2 \) by \( 2 \) and every \( \omega_j \) by \( \sqrt2 \).

(e) False; the warning above gives \( \K = \begin{psmallmatrix} 2 & -1 \\ -1 & 2\end{psmallmatrix} \) with \( \M = \diag(1,4) \), whose squared frequencies are \( (5 \pm \sqrt{13})/4 \), irrational, while the four candidate quotients \( 3, 3/4, 1, 1/4 \) are rational.
:::

### B. Practice

:::: {#exr-vibrations-b1}
[B1: Two masses, two springs]

A cart of mass \( 2 \) is joined to a wall by a spring of stiffness \( 2 \), and a cart of mass \( 1 \) is joined to the first cart by a spring of stiffness \( 1 \); the second cart is free on the right.

::: {.enumerate options="label=(\alph*)"}
1. Write down \( \M \) and \( \K \).
2. Find the natural frequencies and an \( \M \)-orthonormal basis of normal modes.
3. Verify directly that the two modes are \( \M \)-orthogonal but **not** orthogonal for the standard inner product.
:::
::::

::: {.solution}
(a) With \( x_1, x_2 \) the displacements, Newton and Hooke give \( 2x_1'' = -2x_1 + (x_2 - x_1) \) and \( x_2'' = -(x_2 - x_1) \), so
\[
\M = \begin{pmatrix} 2 & 0 \\ 0 & 1\end{pmatrix},
\qquad
\K = \begin{pmatrix} 3 & -1 \\ -1 & 1\end{pmatrix} .
\]
Both are symmetric, \( \M \succ 0 \), and \( \K \succ 0 \) since its leading minors are \( 3 \) and \( 2 \) (@thm-pd-characterizations).

(b) Expanding the determinant of the pencil,
\[
\begin{aligned}
\det(\K - \lambda\M) &= (3 - 2\lambda)(1 - \lambda) - 1 \\
&= 2\lambda^2 - 5\lambda + 2 = (2\lambda - 1)(\lambda - 2) ,
\end{aligned}
\]
so \( \omega_1^2 = \tfrac12 \) and \( \omega_2^2 = 2 \), that is \( \omega_1 = 1/\sqrt2 \) and \( \omega_2 = \sqrt2 \). For \( \lambda = \tfrac12 \), \( \K - \tfrac12\M = \begin{psmallmatrix} 2 & -1 \\ -1 & 1/2\end{psmallmatrix} \) has kernel spanned by \( (1, 2) \); for \( \lambda = 2 \), \( \K - 2\M = \begin{psmallmatrix} -1 & -1 \\ -1 & -1\end{psmallmatrix} \) has kernel spanned by \( (1, -1) \). Since \( (1,2)\tp\M(1,2) = 2 + 4 = 6 \) and \( (1,-1)\tp\M(1,-1) = 2 + 1 = 3 \),
\[
\v_1 = \tfrac{1}{\sqrt6}(1, 2), \qquad \v_2 = \tfrac{1}{\sqrt3}(1, -1) .
\]
In the slow mode the two carts move together, the light one further; in the fast mode they move against each other.

(c) \( (1,2)\tp\M(1,-1) = 2\cdot1\cdot1 + 1\cdot2\cdot(-1) = 0 \), so they are \( \M \)-orthogonal, as @thm-normal-modes (b) requires. But \( (1,2)\cdot(1,-1) = 1 - 2 = -1 \ne 0 \): the standard inner product does not see the modes.
:::

:::: {#exr-vibrations-b2}
[B2: Bounding the slowest mode]

For the system of Exercise B1, estimate \( \omega_1^2 \) from above using the guesses \( \g = (1,1) \) and \( \g = (2,3) \), and compare with the exact value.
::::

::: {.solution}
For \( \g = (1,1) \): \( \g\tp\K\g = 3 - 1 - 1 + 1 = 2 \) and \( \g\tp\M\g = 2 + 1 = 3 \), so \( \rho(\g) = 2/3 \approx 0.667 \).

For \( \g = (2,3) \): \( \K\g = (6-3, -2+3) = (3, 1) \), so \( \g\tp\K\g = 6 + 3 = 9 \); and \( \g\tp\M\g = 8 + 9 = 17 \), so \( \rho(\g) = 9/17 \approx 0.529 \).

The exact value is \( \omega_1^2 = 1/2 \). Both estimates exceed it, as @cor-rayleigh-frequency-bounds requires, and the second guess, being nearer the true mode \( (1,2) \propto (2,4) \), is much nearer the true value.
:::

:::: {#exr-vibrations-b3}
[B3: Stiffening a chain]

In the system of Exercise B1, the stiffness of the second spring is increased from \( 1 \) to \( 2 \), so that \( \K \) becomes \( \K' = \begin{psmallmatrix} 4 & -2 \\ -2 & 2\end{psmallmatrix} \).

::: {.enumerate options="label=(\alph*)"}
1. Verify that \( \K' \succeq \K \).
2. Compute the new squared frequencies and check @prp-frequency-monotonicity (a).
:::
::::

::: {.solution}
(a) \( \K' - \K = \begin{psmallmatrix} 1 & -1 \\ -1 & 1\end{psmallmatrix} \), whose trace is \( 2 \) and determinant \( 0 \), so its eigenvalues are \( 2 \) and \( 0 \) and it is positive semidefinite (@thm-psd-characterizations). Hence \( \K' \succeq \K \) by @def-loewner-order. Directly: \( \v\tp(\K'-\K)\v = (v_1 - v_2)^2 \ge 0 \), which is the extra spring energy.

(b) \( \det(\K' - \lambda\M) = (4 - 2\lambda)(2 - \lambda) - 4 = 2\lambda^2 - 8\lambda + 4 \), so the squared frequencies are \( 2 \pm \sqrt2 \), about \( 0.586 \) and \( 3.414 \). The old ones were \( 0.5 \) and \( 2 \), and \( 0.586 \ge 0.5 \), \( 3.414 \ge 2 \), as @prp-frequency-monotonicity (a) requires. Note the two increases are quite different in size: the proposition orders the frequencies, it does not move them by a common amount.
:::

### C. Going deeper

:::: {#exr-vibrations-c1}
[C1: The free chain drifts]

Let \( (\M, \K) \) be a mass–spring system.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \omega_1 = 0 \) if and only if \( \K \) is singular, and that in that case the generalized eigenvectors for \( \omega = 0 \) are exactly the non-zero vectors of \( \ker\K \).
2. Hence describe all motions of the free chain of @exm-mass-spring-examples (c) with three equal masses \( m \) and equal inner stiffnesses \( k \), given that \( \ker\K \) is spanned by \( \1 \).
3. Deduce that the total momentum \( \sum_i m_ix_i'(t) \) of the free chain is constant in time.
:::
::::

::: {.solution}
(a) By @thm-normal-modes (b), \( \omega_1 = 0 \) if and only if some \( \v \ne \0 \) has \( \K\v = 0\cdot\M\v = \0 \), that is if and only if \( \ker\K \ne \{\0\} \), that is if and only if \( \K \) is singular (@thm-invertible-tfae). For such an \( \omega \) the equation \( \K\v = \omega^2\M\v \) reads \( \K\v = \0 \), so its non-zero solutions are exactly the non-zero vectors of \( \ker\K \).

(b) Here \( \M = m\I_3 \) and \( \K = k\begin{psmallmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1\end{psmallmatrix} \), whose kernel is \( \Span(\1) \), one-dimensional. So \( \omega_1 = 0 \) with mode \( \v_1 = \1/\sqrt{3m} \), and the other two frequencies are positive. By @thm-normal-modes (c) every motion is
\[
\x(t) = (a_1 + b_1t)\v_1 + \sum_{j=2}^{3}\bigl(a_j\cos\omega_jt + b_j\sin\omega_jt\bigr)\v_j :
\]
an oscillation superposed on a uniform drift of the whole chain. The drift is the motion @thm-normal-modes produces for a singular \( \K \), and physically it is the chain floating away at constant speed.

(c) The total momentum is \( \1\tp\M\x'(t) \). Differentiating and using @eq-mass-spring, \( \1\tp\M\x''(t) = -\1\tp\K\x(t) = -(\K\1)\tp\x(t) = 0 \), where \( \K\tp = \K \) and \( \K\1 = \0 \) were used. A differentiable function with vanishing derivative is constant, so \( \1\tp\M\x'(t) \) does not depend on \( t \).
:::

:::: {#exr-vibrations-c2}
[C2: Adding a mass cannot raise a frequency, and can lower it a lot]

::: {.enumerate options="label=(\alph*)"}
1. Let \( (\M, \K) \) be a mass–spring system and let \( t > 0 \). Prove that the system \( (\M + t\e_p\e_p\tp, \K) \), obtained by adding mass \( t \) to the \( p \)-th degree of freedom, has \( \omega_j'(t) \le \omega_j \) for every \( j \), and that \( t \mapsto \omega_j'(t) \) is non-increasing.
2. For the single mass of @exm-mass-spring-examples (a) with \( m = k_1 = k_2 = 1 \), compute \( \omega_1'(t) \) exactly and find \( \lim_{t\to\infty}\omega_1'(t) \).
3. Give an example of a mass–spring system and a \( p \) for which adding mass at \( p \) leaves the **largest** frequency unchanged. *Hint: look for a mode that does not move the \( p \)-th mass.*
:::
::::

::: {.solution}
(a) The matrix \( t\e_p\e_p\tp \) is symmetric with \( \v\tp(t\e_p\e_p\tp)\v = tv_p^2 \ge 0 \), so it is positive semidefinite and \( \M + t\e_p\e_p\tp \succeq \M \). By @prp-frequency-monotonicity (b), \( \omega_j'(t) \le \omega_j \) for every \( j \). For monotonicity in \( t \), if \( 0 < s \le t \) then \( \M + t\e_p\e_p\tp \succeq \M + s\e_p\e_p\tp \), because the difference is \( (t-s)\e_p\e_p\tp \succeq 0 \), and applying (b) again to these two systems gives \( \omega_j'(t) \le \omega_j'(s) \).

(b) Here \( n = 1 \), \( \M = (1 + t) \) and \( \K = (2) \), so the single squared frequency is \( \rho(1) = 2/(1+t) \) and \( \omega_1'(t) = \sqrt{2/(1+t)} \). It is decreasing in \( t \) and tends to \( 0 \): an infinitely heavy cart does not move.

(c) Let \( n = 2 \), \( \M = \I_2 \) and \( \K = \diag(1, 4) \), so \( \omega_1^2 = 1 \), \( \omega_2^2 = 4 \) with modes \( \e_1, \e_2 \). Adding mass at \( p = 1 \) gives \( \M' = \diag(1+t, 1) \), and \( \det(\K - \lambda\M') = (1 - \lambda(1+t))(4 - \lambda) \), whose roots are \( 1/(1+t) \) and \( 4 \). The largest squared frequency is still \( 4 \), because its mode \( \e_2 \) has no component at \( p = 1 \) and the added mass therefore never moves in that mode. This also shows the inequalities of @prp-frequency-monotonicity (b) can be equalities.
:::
