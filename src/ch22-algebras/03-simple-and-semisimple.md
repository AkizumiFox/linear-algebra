# Simple and Semisimple Algebras

Section 2 found that \( M_n(F) \) has no two-sided ideals except the two unavoidable ones: as an algebra it cannot be collapsed. This section is about a second kind of object that is indecomposable — not the algebra, but a space the algebra acts on — and about what happens when a space does break apart. The main theorem says that "every invariant subspace can be split off" and "the space is a sum of unbreakable pieces" are one condition wearing two faces, and that condition is what the rest of the chapter runs on. At the end we check the new vocabulary against the old: an operator is semisimple in Chapter 9's sense exactly when the algebra it generates acts semisimply.

Throughout, \( F \) is **any** field. Nothing in this section asks it to be algebraically closed or to have a particular characteristic; the hypotheses start biting in the next section. Algebras are associative, unital and finite-dimensional over \( F \), as agreed in Section 1.

## Two meanings of the word simple

Section 2 proved that \( M_n(F) \) has exactly two two-sided ideals (@thm-matrix-algebra-is-simple), while \( F[x] \) — the infinite-dimensional standing exception of Section 1 — has infinitely many. That difference deserves a name.

*A simple algebra is one that cannot be collapsed: forming the quotient by an ideal either changes nothing or destroys everything.*

::: {#def-simple-algebra}
[Simple Algebra]

An \( F \)-algebra \( A \) is **simple** if \( A \ne \{0\} \) and the only two-sided ideals (@def-two-sided-ideal) of \( A \) are \( \{0\} \) and \( A \) itself.
:::

In words: two conditions, and the first is not decoration. The zero algebra has only one ideal, so without the clause \( A \ne \{0\} \) it would count as simple and every theorem below would need an exception for it.

**Examples.**

- **The field itself.** \( A = F \) is simple: a non-zero ideal contains some \( c \ne 0 \), hence contains \( c^{-1}c = 1 \), hence everything.
- **Matrix algebras.** \( M_n(F) \) is simple for every \( n \ge 1 \) (@thm-matrix-algebra-is-simple). This is the example the whole chapter is aimed at.
- **A degenerate case.** \( n = 1 \) recovers \( M_1(F) = F \), so the two examples above are one.

**Non-example by minimal change.** Replace \( M_n(F) \) by the algebra \( A \) of **upper triangular** \( 2 \times 2 \) matrices over \( F \). It is a subalgebra of \( M_2(F) \) of dimension \( 3 \), with basis \( \E_{11}, \E_{12}, \E_{22} \), and the set
\[
\cN = \left\{ \begin{pmatrix} 0 & b \\ 0 & 0\end{pmatrix} : b \in F \right\}
\]
is a two-sided ideal of \( A \): it is a subspace, and
\[
\begin{aligned}
\begin{pmatrix} a & c \\ 0 & d\end{pmatrix}\begin{pmatrix} 0 & b \\ 0 & 0\end{pmatrix}
  &= \begin{pmatrix} 0 & ab \\ 0 & 0\end{pmatrix}, \\
\begin{pmatrix} 0 & b \\ 0 & 0\end{pmatrix}\begin{pmatrix} a & c \\ 0 & d\end{pmatrix}
  &= \begin{pmatrix} 0 & bd \\ 0 & 0\end{pmatrix}.
\end{aligned}
\]
Since \( \{0\} \ne \cN \ne A \), the algebra \( A \) is not simple. The clause that fails is the second one; \( A \ne \{0\} \) is fine.

- **Another non-example, the infinite-dimensional one.** \( F[x] \) has the ideal \( \langle x \rangle \) (@prp-ideal-generated), the polynomials with zero constant term (@exm-ideals-polynomials (b)), which is neither \( \{0\} \) nor \( F[x] \).

**Why this definition.** Section 2 identified ideals with kernels: the kernel of an algebra homomorphism out of \( A \) is a two-sided ideal, and conversely every two-sided ideal is the kernel of the map onto the quotient algebra (@def-quotient-algebra, @thm-algebra-first-isomorphism). Simplicity therefore says that \( A \) admits no interesting image under a homomorphism, which is the following one-line consequence.

::: {#prp-map-out-of-simple-is-injective}
[Maps Out of a Simple Algebra]

Let \( A \) be a simple \( F \)-algebra, let \( B \ne \{0\} \) be an \( F \)-algebra, and let \( \varphi \colon A \to B \) be an algebra homomorphism (@def-algebra-homomorphism). Then \( \varphi \) is injective.
:::

::: {.proof}
Since \( B \ne \{0\} \) we have \( 1_B \ne 0 \): otherwise \( y = 1_By = 0 \) for every \( y \in B \). The kernel of \( \varphi \) is a two-sided ideal of \( A \), and it does not contain \( 1_A \), because \( \varphi(1_A) = 1_B \ne 0 \). So \( \ker\varphi \ne A \), and simplicity forces \( \ker\varphi = \{0\} \). A linear map with zero kernel is injective (@thm-injective-iff-trivial-kernel).
:::

Section 2 had already seen the case \( A = M_n(F) \), which is simple by @thm-matrix-algebra-is-simple: that is @cor-matrix-homomorphism-injective. So a simple algebra has only one image under a homomorphism worth the name: itself. Section 6 will turn this around and recognize the **semisimple** algebras, over an algebraically closed field, as products of matrix algebras; its Exercise C1 picks out the simple ones among them as the single matrix algebras.

## Algebras acting on spaces

An algebra is already a set of operators, by Section 1's embedding theorem (@thm-cayley-for-algebras). But the same abstract algebra acts on many different spaces — \( M_n(F) \) acts on \( F^n \), on itself, on \( M_n(F) \) by conjugation — and the differences between those actions are the subject. We need a word for one of them.

::: {#def-representation-of-an-algebra}
[Representation of an Algebra, and Invariant Subspaces]

Let \( A \) be an \( F \)-algebra. A **representation** of \( A \) on a finite-dimensional vector space \( V \) over \( F \) is an algebra homomorphism
\[
\rho \colon A \to \cL(V) ,
\]
so that \( \rho \) is linear, \( \rho(ab) = \rho(a)\rho(b) \), and \( \rho(1_A) = \id_V \). We then call \( V \) an **\( A \)-space** and abbreviate \( \rho(a)(\v) \) to \( a\v \). A subspace \( U \subseteq V \) is **\( A \)-invariant** if \( a\u \in U \) for every \( a \in A \) and every \( \u \in U \).
:::

In words: the multiplication of \( A \) is carried to composition of operators, and — the clause that is easy to overlook — **the identity of \( A \) must act as the identity of \( V \)**. Two standing examples:

- **The tautological representation.** If \( A \subseteq \cL(V) \) is a subalgebra containing \( \id_V \) (@def-subalgebra), the inclusion is a representation. This is the case we usually mean when we say "an algebra of operators on \( V \)".
- **The regular representation.** \( A \) acts on itself by left multiplication: \( \rho(a)(b) = ab \). Associativity gives \( \rho(ab) = \rho(a)\rho(b) \), bilinearity gives linearity, and \( \rho(1_A) = \id_A \). Here the \( A \)-invariant subspaces are precisely the **left ideals** of Section 2.

**Non-example by minimal change.** Take \( A = F \), \( V = F^2 \), and \( \rho(c) = \0 \) for every \( c \). This is linear and multiplicative, but \( \rho(1) = \0 \ne \id_V \), so it is not a representation. The clause that fails is unitality, and it is not a technicality: it is what makes \( \v = 1\v \) lie in \( A\v \), a step used twice below.

Now the indecomposable actions.

*An irreducible \( A \)-space is one with nothing inside it for \( A \) to see.*

::: {#def-simple-module}
[Irreducible, or Simple, \( A \)-space]

An \( A \)-space \( V \) is **irreducible** — equivalently, **simple** — if \( V \ne \{\0\} \) and the only \( A \)-invariant subspaces of \( V \) are \( \{\0\} \) and \( V \).
:::

Both words are standard and we use them interchangeably. Again two clauses, and again the first is needed: \( \{\0\} \) has only one subspace and must be excluded by hand, exactly as the zero algebra was.

**Examples.**

- **Lines.** Any \( A \)-space of dimension \( 1 \) is irreducible, whatever \( A \) is, since its only subspaces are \( \{\0\} \) and itself. These are the smallest possible pieces, and Section 4 will show that over an algebraically closed field a commutative algebra has no others.
- **The column space of a matrix algebra.** \( F^n \) is an irreducible \( M_n(F) \)-space. Indeed, let \( U \ne \{\0\} \) be invariant and pick \( \u \in U \) with \( \u \ne \0 \). Given any \( \w \in F^n \), extend \( \u \) to a basis of \( F^n \) (@thm-basis-extension) and let \( \X \) be the matrix of the linear map sending \( \u \) to \( \w \) and the other basis vectors to \( \0 \) (@thm-linear-map-from-any-basis). Then \( \w = \X\u \in U \). So \( U = F^n \).

**Non-example by minimal change.** Shrink \( M_2(F) \) to the upper triangular algebra \( A \) above, still acting on \( F^2 \). The line \( F\e_1 \) is \( A \)-invariant, because an upper triangular \( \X \) has \( \X\e_1 = x_{11}\e_1 \). So \( F^2 \) is not an irreducible \( A \)-space; the clause that fails is the second.

::: {.warning}
**Two different words are both spelled "simple".** An algebra is simple when it has no proper non-zero **two-sided ideal**; an \( A \)-space is simple when it has no proper non-zero **invariant subspace**. The first does not imply the second. For \( n \ge 2 \) the algebra \( M_n(F) \) is simple, yet \( M_n(F) \) as a space over itself is **not**: the matrices whose columns other than the first are zero form a left ideal that is neither \( \{0\} \) nor all of \( M_n(F) \), that is, a proper non-zero invariant subspace of the regular representation.
:::

::: {.check}
Let \( A \subseteq M_2(F) \) be the algebra of **diagonal** matrices and let \( V = F^2 \). Which subspaces of \( V \) are \( A \)-invariant? Is \( V \) irreducible?
:::

::: {.solution}
The invariant subspaces are \( \{\0\} \), \( F\e_1 \), \( F\e_2 \) and \( F^2 \). Each of these four is invariant because \( \diag(d_1, d_2) \) fixes each coordinate line. No other line \( F\v \) with \( \v = (x, y) \) is: \( \E_{11}\v = (x, 0) \) must be a multiple \( c(x, y) \) of \( \v \), and if both \( x \ne 0 \) and \( y \ne 0 \) then \( cy = 0 \) forces \( c = 0 \) and hence \( x = 0 \), a contradiction. So \( V \) is not irreducible: \( F\e_1 \) is a proper non-zero invariant subspace.
:::

## Splitting a space into pieces

Here is the phenomenon the section is built on. Take \( V = F^2 \) and the single operator \( \N = \J_2(0) \), that is, \( \N\e_1 = \0 \) and \( \N\e_2 = \e_1 \). The line \( F\e_1 \) is invariant. Is there an invariant complement? A complement of a line in \( F^2 \) is a line \( F\v \) with \( \v = (x, y) \) and \( y \ne 0 \), and \( \N\v = (y, 0) \) is a non-zero element of \( F\e_1 \), which meets \( F\v \) only in \( \0 \). So \( \N\v \notin F\v \): there is **no** invariant complement, and \( F^2 \) does not break into invariant lines.

Compare \( \D = \diag(1, 2) \), where \( F^2 = F\e_1 \oplus F\e_2 \) splits perfectly. The difference between these two pictures is the definition we want.

*An algebra acts semisimply when every invariant subspace can be split off.*

::: {#def-semisimple-algebra}
[Semisimple Action, Semisimple Algebra]

Let \( A \) be an \( F \)-algebra and \( V \) an \( A \)-space. We say \( A \) **acts semisimply on \( V \)** if **every** \( A \)-invariant subspace \( U \subseteq V \) has an \( A \)-invariant complement: a subspace \( W \subseteq V \) with
\[
V = U \oplus W \qquad\text{and}\qquad W \text{ is } A\text{-invariant.}
\]
The algebra \( A \) is **semisimple** if it acts semisimply on **itself** in the regular representation — that is, if every left ideal of \( A \) has a complementary left ideal.
:::

In words: the first notion is a property of an action, the second a property of the algebra alone, obtained by feeding the algebra its own most faithful space. The examples come after the theorem that makes the definition usable.

::: {.warning}
**Acting semisimply depends on the space, not only on the algebra.** The upper triangular algebra \( A \) does not act semisimply on \( F^2 \), as we check below. Yet it does act semisimply on the one-dimensional space \( F \) through \( \X \mapsto x_{11} \), for the silly reason that a one-dimensional space has no invariant subspace to split off. Always say **which space**. The unqualified phrase "\( A \) is semisimple" is reserved for the regular representation, and a proposition below shows that this is the right choice: a semisimple algebra acts semisimply on every space.
:::

The first thing to know is that the property passes to invariant subspaces. Without this, no induction on dimension gets started.

::: {#lem-invariant-complement-heredity}
[Splitting Is Inherited by Invariant Subspaces]

Let \( A \) act semisimply on a finite-dimensional \( A \)-space \( V \), and let \( W \subseteq V \) be \( A \)-invariant. Then \( W \), with the action \( a \mapsto \rho(a)|_W \), is an \( A \)-space, and \( A \) acts semisimply on \( W \).
:::

::: {.idea}
An invariant subspace \( U \) of \( W \) is also one of \( V \), so it has an invariant complement \( U' \) in \( V \). That complement is too big; cut it down to \( U' \cap W \) and check that nothing was lost.
:::

::: {.proof}
Since \( W \) is \( A \)-invariant, \( \rho(a)|_W \in \cL(W) \) for every \( a \in A \), and \( a \mapsto \rho(a)|_W \) is linear, multiplicative and sends \( 1_A \) to \( \id_W \); so it is a representation.

Let \( U \subseteq W \) be \( A \)-invariant. Then \( U \) is an \( A \)-invariant subspace of \( V \), so there is an \( A \)-invariant \( U' \) with \( V = U \oplus U' \). Put \( W' = U' \cap W \), which is \( A \)-invariant because \( U' \) and \( W \) are.

\( U + W' = W \): the inclusion \( \subseteq \) holds since \( U \subseteq W \) and \( W' \subseteq W \). Conversely, let \( \w \in W \) and write \( \w = \u + \u' \) with \( \u \in U \), \( \u' \in U' \). Then \( \u' = \w - \u \in W \), because both \( \w \) and \( \u \) lie in \( W \); hence \( \u' \in U' \cap W = W' \) and \( \w \in U + W' \).

The sum is direct: \( U \cap W' \subseteq U \cap U' = \{\0\} \).

Therefore \( W = U \oplus W' \) with \( W' \) an \( A \)-invariant complement, which is what semisimplicity of the action on \( W \) asks for.
:::

Now the theorem. It is the section's real content, and every later section uses it.

:::: {#thm-semisimple-iff-sum-of-simples}
[Complete Reducibility]

Let \( A \) be an \( F \)-algebra and let \( V \) be a finite-dimensional \( A \)-space. The following are equivalent:

::: {.enumerate options="label=(\alph*)"}
1. \( A \) acts semisimply on \( V \);
2. \( V \) is a sum of irreducible \( A \)-invariant subspaces;
3. \( V \) is a direct sum of finitely many irreducible \( A \)-invariant subspaces.
:::

Here a sum over the empty family is \( \{\0\} \), so all three hold when \( V = \{\0\} \). No hypothesis is placed on \( F \).
::::

::: {.idea}
For (a) \( \Rightarrow \) (c), induct on \( \dim V \). The smallest non-zero invariant subspace is automatically irreducible: it has no room for a proper one. Split it off using (a), and apply the inductive hypothesis to the complement — which is legitimate precisely because of @lem-invariant-complement-heredity. For (b) \( \Rightarrow \) (a), given an invariant \( U \), build a complement greedily out of the given irreducible pieces: add pieces to \( U \) as long as the sum stays direct, and then show that a piece left outside would have to meet the sum in \( \{\0\} \), so it could have been added too.
:::

::: {.proof}
(a) \( \Rightarrow \) (c). Induction on \( \dim V \). If \( \dim V = 0 \) then \( V \) is the empty direct sum and there is nothing to prove. Let \( \dim V \ge 1 \) and suppose the implication holds for every \( A \)-space of smaller dimension.

Among the non-zero \( A \)-invariant subspaces of \( V \) — there is at least one, namely \( V \) — choose \( W \) of smallest dimension. Then \( W \) is irreducible: it is non-zero, and if \( U \subseteq W \) is \( A \)-invariant with \( U \ne \{\0\} \), then \( U \) is a non-zero \( A \)-invariant subspace of \( V \), so \( \dim U \ge \dim W \) by the choice of \( W \), and \( U = W \) by @thm-dim-impl-eq.

By (a) there is an \( A \)-invariant \( W' \) with \( V = W \oplus W' \). By @lem-invariant-complement-heredity, \( W' \) is an \( A \)-space on which \( A \) acts semisimply, and \( \dim W' = \dim V - \dim W < \dim V \) because \( \dim W \ge 1 \). The inductive hypothesis writes \( W' = W_1 \oplus \dots \oplus W_r \) with each \( W_i \) an irreducible \( A \)-invariant subspace of \( W' \). Invariance and irreducibility refer only to the action of \( A \), not to the ambient space, so each \( W_i \) is an irreducible \( A \)-invariant subspace of \( V \) as well. Hence
\[
V = W \oplus W_1 \oplus \dots \oplus W_r ,
\]
a direct sum of finitely many irreducibles.

(c) \( \Rightarrow \) (b). A direct sum is in particular a sum.

(b) \( \Rightarrow \) (a). Write \( V = \sum_{i \in I} W_i \) with each \( W_i \) an irreducible \( A \)-invariant subspace, and let \( U \subseteq V \) be \( A \)-invariant. Call a finite subset \( J \subseteq I \) **good** if the sum \( U + \sum_{j \in J} W_j \) is direct. The empty set is good. Every good \( J \) satisfies
\[
\lvert J \rvert \le \dim U + \sum_{j \in J}\dim W_j = \dim\Bigl(U \oplus \bigoplus_{j \in J} W_j\Bigr) \le \dim V ,
\]
where the first inequality uses \( \dim W_j \ge 1 \) and the middle equality is @thm-direct-sum-k-criteria. So the sizes of good sets are bounded, and we may choose a good \( J \) with \( \lvert J \rvert \) as large as possible. Put
\[
W = \sum_{j \in J} W_j ,
\]
an \( A \)-invariant subspace, since a sum of \( A \)-invariant subspaces is \( A \)-invariant. Write \( S = U \oplus W \).

*Claim: \( W_i \subseteq S \) for every \( i \in I \).* Fix \( i \). The subspace \( W_i \cap S \) is \( A \)-invariant and contained in the irreducible \( W_i \), so it is \( \{\0\} \) or \( W_i \). Suppose it were \( \{\0\} \). Then \( i \notin J \), since \( j \in J \) gives \( W_j \subseteq S \) and \( W_j \ne \{\0\} \). We show \( J \cup \{i\} \) is good, contradicting maximality. Let
\[
\u + \sum_{j \in J}\w_j + \w_i = \0 , \qquad \u \in U,\ \w_j \in W_j,\ \w_i \in W_i .
\]
Then \( \w_i = -\bigl(\u + \sum_{j}\w_j\bigr) \in W_i \cap S = \{\0\} \), so \( \w_i = \0 \); and then \( \u + \sum_j \w_j = \0 \) forces \( \u = \0 \) and every \( \w_j = \0 \), because \( J \) is good (@thm-direct-sum-k-criteria (b)). So the sum over \( J \cup \{i\} \) is direct, which is the contradiction. Hence \( W_i \cap S = W_i \), that is, \( W_i \subseteq S \).

The claim gives \( V = \sum_{i}W_i \subseteq S \), so \( V = S = U \oplus W \) with \( W \) invariant. This proves (a).
:::

Two features of the proof are worth keeping. The complement produced in (b) \( \Rightarrow \) (a) is a sum of some of the given pieces, so nothing new has to be constructed. And the pieces in (c) are far from unique: \( F^2 \) under the scalar matrices is a direct sum of **any** two distinct lines.

::: {#exm-triangular-not-semisimple}
[Upper Triangular Matrices Are Not Semisimple]

Let \( A \subseteq M_2(F) \) be the algebra of upper triangular matrices, of dimension \( 3 \). Show that \( A \) does not act semisimply on \( F^2 \), and list the irreducible \( A \)-subspaces of \( F^2 \).
:::

::: {.solution}
The \( A \)-invariant subspaces of \( F^2 \) are \( \{\0\} \), \( F\e_1 \) and \( F^2 \), and no others. Certainly all three are invariant, the middle one because \( \X\e_1 = x_{11}\e_1 \) for upper triangular \( \X \). Conversely, let \( F\v \) be an invariant line with \( \v = (x, y) \). Since \( \E_{12} \in A \) and \( \E_{12}\v = (y, 0) \), invariance gives \( (y, 0) = c(x, y) \) for some \( c \in F \). If \( y \ne 0 \) then \( cy = 0 \) gives \( c = 0 \), hence \( y = 0 \) after all; so \( y = 0 \) and \( F\v = F\e_1 \).

Now \( F\e_1 \) is an invariant subspace with no invariant complement, since a complement of a line in \( F^2 \) is a line, and \( F\e_1 \) is the only invariant one. So \( A \) does not act semisimply on \( F^2 \). The only irreducible \( A \)-subspace is \( F\e_1 \); in particular \( F^2 \) is not a sum of irreducibles, in agreement with @thm-semisimple-iff-sum-of-simples.
:::

For contrast, here is an action that does split, and it is the one Section 6 will build on.

::: {#exm-matrix-algebra-semisimple}
[Matrix Algebras Are Semisimple]

Show that \( A = M_n(F) \) is a semisimple algebra for every \( n \ge 1 \).
:::

::: {.solution}
Section 2 did the work. For \( j = 1, \dots, n \) let \( C_j \subseteq A \) be the column ideal: the matrices all of whose columns except the \( j \)-th are zero. By @prp-left-ideals-of-matrix-algebra (d), each \( C_j \) is a left ideal and \( A = C_1 \oplus \dots \oplus C_n \). Moreover \( C_j = L_W \) for the one-dimensional space of row vectors \( W = \Span(\e_j\tp) \), so \( C_j \) is a **minimal** non-zero left ideal by part (c) of the same proposition.

The \( A \)-invariant subspaces of the regular representation are the left ideals of \( A \), so "minimal non-zero left ideal" says exactly "irreducible \( A \)-subspace". Hence the regular representation of \( A \) is a direct sum of irreducibles, and @thm-semisimple-iff-sum-of-simples makes \( A \) semisimple.
:::

The definition of a semisimple **algebra** only looked at one space. It controls all of them.

::: {#prp-semisimple-algebra-all-reps-semisimple}
[A Semisimple Algebra Has No Other Kind of Representation]

Let \( A \) be a semisimple \( F \)-algebra and let \( V \) be any finite-dimensional \( A \)-space. Then \( A \) acts semisimply on \( V \).
:::

::: {.idea}
Every vector \( \v \) lies in \( A\v \), because \( 1_A \) acts as the identity; so \( V \) is the sum of the subspaces \( A\v \). Chop \( A \) itself into irreducible left ideals \( L \) and show each \( L\v \) is either zero or irreducible. Then \( V \) is a sum of irreducibles and @thm-semisimple-iff-sum-of-simples finishes.
:::

::: {.proof}
If \( V = \{\0\} \) there is nothing to prove, so let \( \dim V \ge 1 \). Since \( A \) is semisimple, @thm-semisimple-iff-sum-of-simples applied to the regular representation gives \( A = L_1 \oplus \dots \oplus L_k \) with each \( L_m \) an irreducible left ideal.

*Claim: for a left ideal \( L \) that is irreducible and a vector \( \v \in V \), the subspace \( L\v = \{ a\v : a \in L \} \) is either \( \{\0\} \) or an irreducible \( A \)-invariant subspace of \( V \).* It is a subspace, being the image of the linear map \( a \mapsto a\v \) restricted to \( L \), and it is \( A \)-invariant because \( b(a\v) = (ba)\v \) with \( ba \in L \). Suppose \( L\v \ne \{\0\} \) and let \( U \subseteq L\v \) be \( A \)-invariant with \( U \ne \{\0\} \). Put
\[
L_0 = \{ a \in L : a\v \in U \} .
\]
This is a subspace of \( L \), and it is a left ideal: for \( b \in A \) and \( a \in L_0 \) we have \( ba \in L \) and \( (ba)\v = b(a\v) \in U \) since \( U \) is invariant. As \( L \) is irreducible, \( L_0 = \{0\} \) or \( L_0 = L \). If \( L_0 = \{0\} \), then every \( \u \in U \) has the form \( \u = a\v \) with \( a \in L \), whence \( a \in L_0 = \{0\} \) and \( \u = \0 \), contradicting \( U \ne \{\0\} \). So \( L_0 = L \), which says \( L\v \subseteq U \) and therefore \( U = L\v \). This proves the claim.

Now let \( \v \in V \). Since \( 1_A\v = \v \), we have \( \v \in A\v = L_1\v + \dots + L_k\v \). Hence
\[
V = \sum_{\v \in V} A\v = \sum_{\v \in V}\ \sum_{m = 1}^{k} L_m\v ,
\]
and discarding the summands that are \( \{\0\} \) exhibits \( V \) as a sum of irreducible \( A \)-invariant subspaces. By @thm-semisimple-iff-sum-of-simples, \( A \) acts semisimply on \( V \).
:::

## How far from semisimple: the radical

The upper triangular algebra failed to act semisimply on \( F^2 \), and the ideal \( \cN \) was visibly to blame: it is non-zero, yet it squares to zero, so no irreducible space can feel it. That suggests measuring the failure by collecting everything invisible.

We write \( \operatorname{rad} A \) for what follows. Chapter 13 §01 writes \( \operatorname{rad}(\beta) \) for the radical of a bilinear form; here the argument is an algebra and the two never meet.

::: {#def-algebra-radical}
[Radical of an Algebra]

Let \( A \) be an \( F \)-algebra. Its **radical** is
\[
\operatorname{rad} A \coloneqq \bigcap_{V} \{\, a \in A : aV = \{\0\} \,\} ,
\]
where \( V \) runs over all irreducible \( A \)-spaces and \( aV = \{ a\v : \v \in V \} \).
:::

In words: the elements that every irreducible representation sends to \( 0 \). The quantifier ranges over a manageable supply: if \( V \) is irreducible and \( \v \in V \) is non-zero, then \( A\v \) is a non-zero invariant subspace, so \( V = A\v \) is the image of the linear map \( a \mapsto a\v \), and \( \dim V \le \dim A \).

The radical is a two-sided ideal. It is a subspace, being an intersection of kernels of linear maps; and if \( a \in \operatorname{rad} A \), \( x, y \in A \) and \( V \) is irreducible, then \( (xay)\v = x\bigl(a(y\v)\bigr) = x\0 = \0 \) for every \( \v \in V \). Taking \( y = 1_A \) and \( x = 1_A \) in turn shows \( xa \) and \( ay \) lie in \( \operatorname{rad} A \).

The first fact we want is the one the triangular example suggested.

::: {#lem-nilpotent-ideal-acts-as-zero}
[A Nilpotent Ideal Is Invisible]

Let \( A \) be an \( F \)-algebra and let \( \cI \subseteq A \) be a two-sided ideal which is **nilpotent**: for some \( m \ge 1 \), every product \( a_1a_2\cdots a_m \) of \( m \) elements of \( \cI \) is \( 0 \). Then \( \cI \subseteq \operatorname{rad} A \).
:::

::: {.proof}
Let \( V \) be an irreducible \( A \)-space and write \( \cI V = \Span\{ a\v : a \in \cI,\ \v \in V \} \), and more generally \( \cI^{k}V = \Span\{ a_1\cdots a_k\v : a_i \in \cI,\ \v \in V \} \).

The subspace \( \cI V \) is \( A \)-invariant, since \( b(a\v) = (ba)\v \) with \( ba \in \cI \). By irreducibility, \( \cI V = \{\0\} \) or \( \cI V = V \).

Suppose \( \cI V = V \). Applying \( \cI \) to both sides, \( \cI^{2}V = \cI(\cI V) = \cI V = V \), and repeating gives \( \cI^{k}V = V \) for every \( k \ge 1 \). But \( \cI^{m}V = \{\0\} \) by nilpotency, so \( V = \{\0\} \), contradicting irreducibility.

Hence \( \cI V = \{\0\} \), that is, every \( a \in \cI \) acts as \( 0 \) on \( V \). Since \( V \) was an arbitrary irreducible \( A \)-space, \( \cI \subseteq \operatorname{rad} A \).
:::

And the radical really does obstruct semisimplicity.

::: {#prp-semisimple-has-zero-radical}
[A Semisimple Algebra Has Zero Radical]

Let \( A \) be a semisimple \( F \)-algebra. Then \( \operatorname{rad} A = \{0\} \).
:::

::: {.proof}
By @thm-semisimple-iff-sum-of-simples applied to the regular representation, \( A = L_1 \oplus \dots \oplus L_k \) with each \( L_m \) an irreducible \( A \)-space. Let \( a \in \operatorname{rad} A \). Then \( a \) acts as \( 0 \) on each \( L_m \), so \( aL_m = \{0\} \) for every \( m \), and therefore \( aA = \{0\} \). In particular \( a = a1_A = 0 \).
:::

::: {.remark}
The converse is also true for finite-dimensional algebras: \( \operatorname{rad} A = \{0\} \) forces \( A \) to be semisimple. We do not prove it, and nothing in this book uses it; whenever semisimplicity is needed later it is established directly, by Maschke's theorem in Section 7 or by exhibiting a decomposition.
:::

We can now finish the running example.

::: {.check}
Let \( A \) be the algebra of upper triangular \( 2 \times 2 \) matrices and \( \cN \) its ideal of strictly upper triangular matrices. Using the two results above, identify \( \operatorname{rad} A \) and decide whether \( A \) is a semisimple algebra. *Hint: the maps \( \X \mapsto x_{11} \) and \( \X \mapsto x_{22} \) go from \( A \) to \( F \).*
:::

::: {.solution}
\( \operatorname{rad} A = \cN \), and \( A \) is not semisimple.

\( (\supseteq) \) We saw that \( \cN \) is a two-sided ideal, and \( \cN^2 = \{0\} \) because \( \E_{12}\E_{12} = \0 \). By @lem-nilpotent-ideal-acts-as-zero, \( \cN \subseteq \operatorname{rad} A \).

\( (\subseteq) \) For upper triangular \( \X, \Y \) the product has \( (\X\Y)_{11} = x_{11}y_{11} \) and \( (\X\Y)_{22} = x_{22}y_{22} \). So \( \rho_1(\X) = x_{11} \) and \( \rho_2(\X) = x_{22} \) are algebra homomorphisms \( A \to F \), each sending \( \I_2 \) to \( 1 \); they make \( F \) an \( A \)-space in two ways, irreducible because \( \dim F = 1 \). An element of \( \operatorname{rad} A \) must be killed by both, so it has \( x_{11} = x_{22} = 0 \) and lies in \( \cN \).

Since \( \operatorname{rad} A = \cN \ne \{0\} \), @prp-semisimple-has-zero-radical shows \( A \) is not a semisimple algebra.
:::

## Back to a single operator

Chapter 9 §08 already used the word semisimple, for an operator: \( T \) is semisimple when \( m_T \) is a product of **distinct** monic irreducible polynomials (@def-semisimple-operator). That definition was about a polynomial. This section's is about invariant subspaces. They agree, and proving so is the best check that the new definition is the right one.

Fix a finite-dimensional \( V \ne \{\0\} \) over \( F \) and \( T \in \cL(V) \), and let
\[
F[T] \coloneqq \{\, p(T) : p \in F[x] \,\} \subseteq \cL(V) ,
\]
which is a commutative subalgebra of \( \cL(V) \) containing \( \id_V \) (@prp-polynomial-algebra-dimension). A subspace \( U \) is \( F[T] \)-invariant if and only if it is \( T \)-invariant: one direction is the case \( p = x \), and the other holds because \( TU \subseteq U \) gives \( T^kU \subseteq U \) for every \( k \), hence \( p(T)U \subseteq U \) for every \( p \).

:::: {#thm-semisimple-operator-iff-semisimple-action}
[The Two Meanings of Semisimple Agree]

Let \( V \ne \{\0\} \) be a finite-dimensional vector space over \( F \) and let \( T \in \cL(V) \). The following are equivalent:

::: {.enumerate options="label=(\alph*)"}
1. \( T \) is semisimple in the sense of @def-semisimple-operator, that is, \( m_T \) is a product of distinct monic irreducible polynomials;
2. \( F[T] \) acts semisimply on \( V \): every \( T \)-invariant subspace has a \( T \)-invariant complement;
3. \( V \) is a sum of irreducible \( F[T] \)-invariant subspaces.
:::

No hypothesis is placed on \( F \).
::::

::: {.idea}
(b) and (c) are @thm-semisimple-iff-sum-of-simples for the algebra \( F[T] \), so the work is the polynomial statement (a). Forwards: the primary decomposition splits \( V \) into pieces on which the minimal polynomial is a single irreducible \( p \), and inside such a piece **every** non-zero vector generates a cyclic subspace of dimension \( \deg p \) — which leaves no room for a proper invariant subspace. Backwards: an irreducible piece is cyclic, and a factorization of its minimal polynomial would manufacture a smaller invariant subspace inside it; so each piece contributes one irreducible polynomial, and their product, which is squarefree, kills \( T \).
:::

::: {.proof}
By the remark preceding the theorem, "\( T \)-invariant" and "\( F[T] \)-invariant" are the same condition, so (b) \( \Leftrightarrow \) (c) is @thm-semisimple-iff-sum-of-simples applied to \( A = F[T] \).

(a) \( \Rightarrow \) (c). Write \( m_T = p_1\cdots p_k \) with \( p_1, \dots, p_k \) distinct monic irreducibles, so that every exponent in the factorization is \( 1 \). By @thm-primary-decomposition, \( V = V_1 \oplus \dots \oplus V_k \) with \( V_i = \ker p_i(T) \) a non-zero \( T \)-invariant subspace on which \( m_{T|_{V_i}} = p_i \).

Fix \( i \) and let \( \v \in V_i \) with \( \v \ne \0 \). Then \( p_i(T)\v = \0 \), so the \( T \)-annihilator \( m_{T,\v} \) divides \( p_i \) (@def-t-annihilator); it is monic of degree at least \( 1 \) because \( \v \ne \0 \), and \( p_i \) is irreducible, so \( m_{T,\v} = p_i \). By @thm-cyclic-subspace-basis (a), the cyclic subspace \( Z(\v; T) \) has dimension \( \deg p_i \), and it is \( T \)-invariant (@prp-cyclic-subspace-smallest).

\( Z(\v; T) \) is irreducible. Let \( U \subseteq Z(\v; T) \) be \( T \)-invariant with \( U \ne \{\0\} \) and pick \( \u \in U \) with \( \u \ne \0 \). Since \( \u \in V_i \), the same argument gives \( m_{T,\u} = p_i \) and \( \dim Z(\u; T) = \deg p_i \). As \( Z(\u; T) \subseteq U \subseteq Z(\v; T) \) and the two ends have equal dimension, @thm-dim-impl-eq gives \( U = Z(\v; T) \).

Every non-zero \( \v \in V_i \) lies in \( Z(\v; T) \subseteq V_i \), so \( V_i \) is a sum of irreducible \( T \)-invariant subspaces, and hence so is \( V = V_1 + \dots + V_k \).

(c) \( \Rightarrow \) (a). Write \( V = \sum_{i \in I}W_i \) with each \( W_i \) irreducible.

*Each \( m_{T|_{W_i}} \) is irreducible.* Pick \( \w \in W_i \) with \( \w \ne \0 \). Then \( Z(\w; T) \) is a non-zero \( T \)-invariant subspace of \( W_i \), so \( Z(\w; T) = W_i \), and @thm-cyclic-subspace-basis (a), (c) give \( q \coloneqq m_{T|_{W_i}} = m_{T,\w} \) with \( \deg q = \dim W_i \ge 1 \). Suppose \( q \) were not irreducible. Since \( \deg q \ge 1 \), @def-irreducible-polynomial then gives \( q = fg \) with both \( f \) and \( g \) non-constant, and we may take them monic after dividing each by its leading coefficient. So \( 1 \le \deg f < \deg q \) and \( 1 \le \deg g < \deg q \). Put \( \u = g(T)\w \). Then \( \u \ne \0 \): otherwise \( g(T)\w = \0 \) would give \( m_{T,\w} \mid g \) (@def-t-annihilator), impossible since \( g \ne 0 \) has degree less than \( \deg m_{T,\w} \). Also \( f(T)\u = (fg)(T)\w = q(T)\w = \0 \), so \( m_{T,\u} \mid f \) and, by @thm-cyclic-subspace-basis (a), \( \dim Z(\u; T) \le \deg f < \dim W_i \). But \( Z(\u; T) \) is a non-zero \( T \)-invariant subspace of \( W_i \), hence equal to \( W_i \) by irreducibility — a contradiction. So no such factorization exists and \( q \) is irreducible.

*Finitely many pieces suffice.* Start with one \( W_{i_1} \); as long as the sum of the chosen pieces is not \( V \), some \( W_i \) is not contained in it, and adding that one strictly increases the dimension. The process stops, giving \( V = W_{i_1} + \dots + W_{i_r} \).

*Conclusion.* Let \( q_1, \dots, q_s \) be the distinct polynomials among \( m_{T|_{W_{i_1}}}, \dots, m_{T|_{W_{i_r}}} \) and put \( q = q_1\cdots q_s \), a product of distinct monic irreducibles. For each \( j \), the polynomial \( m_{T|_{W_{i_j}}} \) divides \( q \), so \( q(T) \) vanishes on \( W_{i_j} \); as these subspaces span \( V \), \( q(T) = 0 \) and therefore \( m_T \mid q \) (@thm-minimal-polynomial-divides). If some irreducible \( p \) had \( p^2 \mid m_T \), then \( p^2 \mid q \), which contradicts the uniqueness of the factorization of \( q \) into irreducibles (@thm-unique-factorization-polynomials), every exponent there being \( 1 \). So no irreducible square divides \( m_T \), which is (a).
:::

Two things follow at once. First, the operator case is nothing but the case \( A = F[T] \) of @thm-semisimple-iff-sum-of-simples, so Chapter 9's vocabulary was this chapter's all along. Second, over an algebraically closed field every irreducible polynomial is linear — a monic polynomial of degree at least \( 2 \) has a root \( \lambda \), hence the non-constant factor \( x - \lambda \) (@thm-remainder-theorem) — so "semisimple" there means "a product of distinct **linear** factors", which is diagonalizability (@thm-diagonalizable-iff-minimal-distinct-linear): over such a field, \( F[T] \) acts semisimply on \( V \) exactly when \( T \) is diagonalizable. The shear \( \J_2(0) \) fails on both counts, as it must. Chapter 9 §08 made a finer statement in the same direction, @prp-semisimple-iff-diagonalizable-over-extension: in characteristic zero, semisimple means diagonalizable after the field has been enlarged enough to split \( m_T \). That proposition needs its characteristic hypothesis; @thm-semisimple-operator-iff-semisimple-action does not, because it never leaves \( F \).

## Exercises

### A. Check your understanding

:::: {#exr-simple-and-semisimple-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State what it means for an algebra to be **simple** and what it means for an \( A \)-space to be **irreducible**, and give one object that is the first but whose regular representation is not the second.
2. True or false: if \( A \) acts semisimply on \( V \), then every \( A \)-invariant subspace of \( V \) is irreducible. Justify your answer.
3. Where exactly does the proof of @prp-semisimple-algebra-all-reps-semisimple use the requirement \( \rho(1_A) = \id_V \) built into @def-representation-of-an-algebra? And why is the step \( a = a1_A \) in the proof of @prp-semisimple-has-zero-radical **not** an instance of that requirement?
4. Name \( \operatorname{rad} A \) for the algebra \( A \) of upper triangular \( 2 \times 2 \) matrices, and say which two results identify it.
:::
:::

::: {.solution}
(a) \( A \) is simple if \( A \ne \{0\} \) and its only two-sided ideals are \( \{0\} \) and \( A \) (@def-simple-algebra); an \( A \)-space \( V \) is irreducible if \( V \ne \{\0\} \) and its only \( A \)-invariant subspaces are \( \{\0\} \) and \( V \) (@def-simple-module). For \( n \ge 2 \) the algebra \( M_n(F) \) is simple, but its regular representation is not irreducible, since the first column ideal \( C_1 \) of @exm-matrix-algebra-semisimple is a proper non-zero left ideal.

(b) False. Take \( A = F \) acting on \( V = F^2 \) by scalars. Every subspace is invariant and every subspace has a complement, so \( A \) acts semisimply; but \( V \) itself is an invariant subspace of dimension \( 2 \), and it is not irreducible.

(c) In the final paragraph, at the words "Since \( 1_A\v = \v \)": that is the requirement \( \rho(1_A) = \id_V \) and nothing else, and without it \( \v \) need not lie in \( A\v \), so \( V \) need not be the sum of the subspaces \( A\v \). The step \( a = a1_A \) in @prp-semisimple-has-zero-radical is a different statement: it is axiom (A3) of @def-algebra-over-field, which makes \( 1_A \) a two-sided identity of \( A \) itself, and it holds with no representation in sight.

(d) \( \operatorname{rad} A = \cN \), the strictly upper triangular matrices: the inclusion \( \supseteq \) is @lem-nilpotent-ideal-acts-as-zero applied to the nilpotent ideal \( \cN \), and \( \subseteq \) comes from the two one-dimensional representations \( \X \mapsto x_{11} \) and \( \X \mapsto x_{22} \).
:::

### B. Practice

:::: {#exr-simple-and-semisimple-b1}
[B1: Which actions split?]

Determine which of the following subalgebras of \( M_2(F) \), acting on \( V = F^2 \), act semisimply. Justify your answer in each case, and when the action is semisimple exhibit \( V \) as a direct sum of irreducibles.

::: {.enumerate options="label=(\alph*)"}
1. the scalar matrices \( \{c\I_2 : c \in F\} \);
2. the diagonal matrices;
3. \( F[\N] = \{a\I_2 + b\N : a, b \in F\} \), where \( \N = \J_2(0) \);
4. \( M_2(F) \) itself.
:::
:::

::: {.solution}
(a) Semisimple. Every subspace is invariant, and every subspace of a finite-dimensional space has a complement (@thm-complement-exists). \( V = F\e_1 \oplus F\e_2 \), and each line is irreducible because it has dimension \( 1 \).

(b) Semisimple. By the Quick check above, the invariant subspaces are \( \{\0\} \), \( F\e_1 \), \( F\e_2 \), \( F^2 \); the two lines are complements of each other and the two extreme cases are complements of each other. Again \( V = F\e_1 \oplus F\e_2 \) with both summands irreducible.

(c) Not semisimple. The invariant subspaces are the \( \N \)-invariant ones, and the only invariant line is \( F\e_1 \): if \( \v = (x, y) \) with \( y \ne 0 \) then \( \N\v = (y, 0) \) is a non-zero element of \( F\e_1 \), which is not a multiple of \( \v \). So \( F\e_1 \) has no invariant complement. (Alternatively: \( m_{\N} = x^2 \) is not squarefree, so @thm-semisimple-operator-iff-semisimple-action applies.)

(d) Semisimple, trivially: \( V \) is itself irreducible, as shown after @def-simple-module, so \( V \) is a one-term direct sum of irreducibles.
:::

:::: {#exr-simple-and-semisimple-b2}
[B2: A two-dimensional algebra]

Let \( \N = \J_2(0) \in M_2(F) \) and \( A = \{a\I_2 + b\N : a, b \in F\} \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( A \) is a commutative subalgebra of \( M_2(F) \) of dimension \( 2 \).
2. Prove that \( F\N \) is a two-sided ideal of \( A \) and compute \( \operatorname{rad} A \).
3. Is \( A \) a semisimple algebra? Justify your answer.
:::
:::

::: {.solution}
(a) \( A = \Span(\I_2, \N) \) is a subspace, and \( \I_2, \N \) are independent since \( \N \) is not a scalar. It contains \( \I_2 \), and
\[
(a\I_2 + b\N)(a'\I_2 + b'\N) = aa'\I_2 + (ab' + a'b)\N ,
\]
using \( \N^2 = \0 \); the right-hand side lies in \( A \) and is symmetric in the two factors, so \( A \) is a commutative subalgebra of dimension \( 2 \).

(b) The displayed product shows \( (a\I_2 + b\N)(c\N) = ac\N \in F\N \), and \( A \) is commutative, so \( F\N \) is a two-sided ideal; \( (F\N)^2 = \{0\} \) since \( \N^2 = \0 \). By @lem-nilpotent-ideal-acts-as-zero, \( F\N \subseteq \operatorname{rad} A \). Conversely \( \varphi(a\I_2 + b\N) = a \) is an algebra homomorphism \( A \to F \) by the same display, and \( \varphi(\I_2) = 1 \), so \( F \) is an irreducible \( A \)-space; an element of \( \operatorname{rad} A \) must have \( a = 0 \). Hence \( \operatorname{rad} A = F\N \).

(c) No: \( \operatorname{rad} A \ne \{0\} \), so @prp-semisimple-has-zero-radical rules it out.
:::

:::: {#exr-simple-and-semisimple-b3}
[B3: Semisimple operators]

For each of the following, decide whether \( F[T] \) acts semisimply on \( V \), using @thm-semisimple-operator-iff-semisimple-action.

::: {.enumerate options="label=(\alph*)"}
1. \( F = \nR \), \( V = \nR^2 \), \( T \) the rotation matrix \( \begin{pmatrix} 0 & -1 \\ 1 & 0\end{pmatrix} \);
2. \( F = \nQ \), \( V = \nQ^3 \), \( T = \diag(1, 1, 2) \);
3. \( F = \nQ \), \( V = \nQ^3 \), \( T = \J_3(0) \);
4. \( F = \nR \), \( V = \nR^4 \), \( T = \C\bigl((x^2+1)^2\bigr) \).
:::
:::

::: {.solution}
(a) Yes. \( m_T = x^2 + 1 \), irreducible over \( \nR \) and occurring once, so \( T \) is semisimple. Note that \( T \) is **not** diagonalizable over \( \nR \); semisimplicity is the weaker condition.

(b) Yes. \( m_T = (x-1)(x-2) \), two distinct irreducibles.

(c) No. \( m_T = x^3 \) repeats the irreducible \( x \).

(d) No. \( m_T = (x^2+1)^2 \) by @thm-companion-char-min, and \( x^2 + 1 \) is repeated.
:::

### C. Going deeper

:::: {#exr-simple-and-semisimple-c1}
[C1: The diagonal algebra]

Let \( A \subseteq M_n(F) \) be the algebra of all diagonal matrices, acting on \( V = F^n \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that every \( A \)-invariant subspace of \( V \) is the span of a subset of \( \{\e_1, \dots, \e_n\} \). *Hint: consider \( \E_{ii}\v \).*
2. Deduce that \( A \) acts semisimply on \( V \) and identify the irreducible \( A \)-subspaces.
:::
:::

::: {.solution}
(a) Let \( U \) be \( A \)-invariant and put \( S = \{ i : u_i \ne 0 \text{ for some } \u \in U \} \). For \( \u \in U \) and each \( i \), the matrix \( \E_{ii} \) is diagonal, so \( \E_{ii}\u = u_i\e_i \in U \); if \( i \in S \), choosing \( \u \) with \( u_i \ne 0 \) gives \( \e_i \in U \). Hence \( \Span\{\e_i : i \in S\} \subseteq U \). Conversely every \( \u \in U \) is \( \sum_{i \in S} u_i\e_i \), since \( u_i = 0 \) for \( i \notin S \) by the definition of \( S \). So \( U = \Span\{\e_i : i \in S\} \).

(b) By (a) the invariant subspaces are indexed by subsets \( S \subseteq \{1, \dots, n\} \), and the complement of \( \Span\{\e_i : i \in S\} \) inside \( V \) given by the complementary subset is again invariant. So \( A \) acts semisimply, and \( V = F\e_1 \oplus \dots \oplus F\e_n \). The irreducible \( A \)-subspaces are exactly the coordinate lines \( F\e_i \): they are irreducible because they have dimension \( 1 \), and by (a) no other subspace is both invariant and free of a proper non-zero invariant subspace.
:::

:::: {#exr-simple-and-semisimple-c2}
[C2: The radical is never everything]

Let \( A \ne \{0\} \) be a finite-dimensional \( F \)-algebra.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( A \) has at least one irreducible \( A \)-space. *Hint: among the non-zero left ideals, take one of smallest dimension.*
2. Prove that every irreducible \( A \)-space has dimension at most \( \dim A \).
3. Deduce that \( 1_A \notin \operatorname{rad} A \), so \( \operatorname{rad} A \ne A \).
:::
:::

::: {.solution}
(a) \( A \) itself is a non-zero left ideal, so among the non-zero left ideals there is one, \( L \), of smallest dimension. A non-zero left ideal contained in \( L \) is a non-zero left ideal of \( A \), hence has dimension at least \( \dim L \), hence equals \( L \) by @thm-dim-impl-eq. Since the \( A \)-invariant subspaces of the regular representation are the left ideals, \( L \) is an irreducible \( A \)-space.

(b) Let \( V \) be irreducible and \( \v \in V \) non-zero. The set \( A\v \) is an \( A \)-invariant subspace containing \( \v = 1_A\v \), so \( A\v = V \). It is the image of the linear map \( A \to V \), \( a \mapsto a\v \), so \( \dim V \le \dim A \) by @thm-rank-nullity.

(c) Let \( L \) be as in (a). Since \( L \ne \{0\} \), pick \( a \in L \) with \( a \ne 0 \); then \( 1_Aa = a \ne 0 \), so \( 1_A \) does not act as \( 0 \) on \( L \) and therefore \( 1_A \notin \operatorname{rad} A \). Hence \( \operatorname{rad} A \ne A \). (Note the contrast with @prp-semisimple-has-zero-radical: the radical is always a proper ideal, but it is \( \{0\} \) only in the semisimple case.)
:::
