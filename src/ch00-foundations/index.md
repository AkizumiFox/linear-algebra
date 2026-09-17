# Preliminaries

Most people meet linear algebra as a way of computing: row reduction, determinants, maybe eigenvalues. This book treats it as a subject you **prove**. Every statement comes with a reason, and those reasons are built from a small set of ideas: sets, functions, equivalence relations, fields, polynomials and matrices. This chapter collects that toolkit in one place.

You have probably seen some of this before. Some of it, such as negating a statement with several quantifiers, or checking that a rule on equivalence classes is well defined, is exactly where careful readers later stumble. So each section spends its time on the delicate points and moves quickly past the rest.

**How to use this chapter.** Skim the sections you know, but try the *A. Check your understanding* exercises at the end of each one. If you can do them without looking back, move on. If not, that section is worth a slower read.

**What you need.** Nothing from this book. School algebra is enough, plus some familiarity with numbers such as \( \nZ \), \( \nQ \) and \( \nR \). One convention to note now: in this book the natural numbers \( \nN \) start at \( 0 \).

## Roadmap

- **Statements, implications and quantifiers.** How mathematical statements are built, and how to negate them correctly.
- **How proofs are built.** Direct proof, contrapositive, contradiction, cases, uniqueness, counterexamples and induction, and the conventions this book's proofs follow.
- **Sets.** Subsets, operations, indexed families, and the habit of proving two sets equal by double inclusion.
- **Functions.** Injective, surjective and bijective maps; composition; left, right and two-sided inverses.
- **Relations, equivalence classes and quotients.** Sorting a set into classes, and defining functions on classes without ambiguity.
- **Complex numbers.** Arithmetic, conjugates, the modulus, polar form and roots of unity.
- **Fields.** The number systems in which linear algebra works, from \( \nQ \), \( \nR \) and \( \nC \) to the finite fields \( \nF_p \).
- **Polynomials.** Degree, evaluation, and why a polynomial is not the same thing as a function.
- **Matrices.** Addition, the three ways to read a matrix product, transpose, trace and inverses.
- **Groups and permutations.** One structure shared by invertible matrices, the non-zero elements of a field, and rearrangements of a set.

## Named moves

These proof techniques appear throughout the book. Each is introduced in this chapter.

- **Contrapositive.** To prove "if \( P \) then \( Q \)", prove "if not \( Q \) then not \( P \)".
- **Assume two.** To prove something is unique, suppose two objects have the property and show they are equal.
- **Double inclusion.** To prove \( A = B \), prove \( A \subseteq B \) and \( B \subseteq A \).
- **Suppose \( f(a) = f(b) \).** The standard first line when proving that a function is injective.
- **Check well-definedness.** A rule given through a representative must not depend on which representative is chosen.
- **Induction on \( n \).** Find a smaller instance of the problem inside the larger one.
