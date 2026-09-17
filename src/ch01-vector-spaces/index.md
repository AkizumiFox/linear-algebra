# Vector Spaces

Arrows in the plane can be added and stretched. So can solutions of a homogeneous system of equations, polynomials, matrices, and real-valued functions. In each case the same handful of rules governs the arithmetic, and none of the arguments we care about uses anything beyond those rules. This chapter names the structure, a **vector space**, so that every theorem proved once holds for all of these examples at the same time.

The second half of the chapter answers a question that sounds innocent: how big is a vector space? The spaces \( \nR^3 \), \( \nR[x]_{\le 2} \) and the symmetric \( 2 \times 2 \) matrices are all infinite sets, yet each is "three-dimensional" in a precise sense. Making that sense precise, and proving that it does not depend on any choices, takes the Exchange Theorem, the most important proof in the chapter. Everything later in the book measures with the dimension defined here.

**What you need.** From Chapter 0: fields (@def-field) and their basic arithmetic (@thm-field-basic-properties), sets and double inclusion (@thm-double-inclusion), functions, and induction (@thm-induction). Polynomials (@def-polynomial) and matrices (@def-matrix) supply many of the examples.

## Roadmap

- **Vector spaces.** The eight axioms, a gallery of examples and non-examples, and the first consequences of the axioms.
- **Subspaces.** A subset that is a vector space in its own right, recognized by three checks.
- **Linear combinations and span.** Everything that can be built from a list of vectors, and the smallest subspace containing them.
- **Linear independence.** When a list contains no redundant vector, and the Linear Dependence Lemma that finds the redundant one when it does.
- **Bases and coordinates.** Lists that span without waste; every vector gets unique coordinates, and every finite spanning list can be trimmed to a basis.
- **The Exchange Theorem and dimension.** Independent lists are never longer than spanning lists, so all bases have the same length; extending bases and counting instead of checking.
- **Sums and direct sums.** Combining subspaces, the dimension formula, and splitting a space into independent pieces.
- **Infinite-dimensional spaces.** Every vector space has a basis (via Zorn's lemma), and which finite-dimensional facts fail without finiteness.
- **Changing the field.** The same set viewed over a smaller or larger field: restriction of scalars, the tower law, and complexification.

## Named moves

- **The three-check subspace test.** Zero vector, closed under addition, closed under scaling, each check ending with its own sentence.
- **"Let \( a_1\v_1 + \dots + a_k\v_k = \0 \)."** The first line of every independence proof; the goal is then to show every \( a_i \) is zero.
- **Exchange one vector at a time.** Swap a vector of an independent list into a spanning list without losing the span.
- **Count instead of check.** In a space of dimension \( n \), an independent list of length \( n \) is automatically a basis, and so is a spanning list of length \( n \).
- **Basis of the smallest space, then extend.** For any dimension formula, start from a basis of the smallest subspace in sight, extend it, and count.
