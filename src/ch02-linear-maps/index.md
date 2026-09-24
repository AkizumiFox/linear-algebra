# Linear Maps

Chapter 1 studied vector spaces one at a time. This chapter studies the functions between them that respect the structure: **linear maps**, the functions that send sums to sums and scalar multiples to scalar multiples. Differentiation of polynomials, the trace of a matrix, a rotation of the plane, a shift of a sequence and multiplication by a matrix are all linear maps, and one theory covers them all.

The theory is built without coordinates, and that is the point of putting it here. Two subspaces measure how far a linear map is from being injective and from being surjective: its kernel and its image. The Rank–Nullity Theorem ties their dimensions to the dimension of the domain, and turns questions that look as though they need a computation into questions of counting — often it is enough to check one of injectivity and surjectivity and let the count supply the other. By the end we can say when two spaces are "the same": finite-dimensional spaces are classified by a single number, their dimension. No basis is chosen anywhere in this chapter; Chapter 4 chooses one and turns all of this into matrices.

**What you need.** From Chapter 0, functions and what injective, surjective and bijective mean, composition and inverses (@def-injective-surjective-bijective, @def-composition, @thm-composition-preserves), and the counting fact this chapter has a linear version of: between finite sets of equal size, injective and surjective agree (@thm-finite-injective-iff-surjective). Also field arithmetic (@thm-field-basic-properties), polynomials with their degree and evaluation (@def-polynomial, @thm-degree-of-product, @thm-evaluation-respects-operations), which supply half the examples, and, for §04 alone, polynomials of a matrix (@thm-polynomial-of-matrix-properties). From Chapter 1, essentially all of it: vector spaces and the subspace test (@def-vector-space, @thm-subspace-test), span (@def-span, @thm-span-subspace), independence (@def-linear-independence), bases and coordinates (@def-basis, @exm-standard-bases, @thm-coordinates-linear, @cor-basis-existence), dimension with basis extension and the two counting theorems that replace a check (@def-dimension, @thm-basis-extension, @thm-right-size-basis, @thm-size-bounds, @thm-dim-impl-eq), and sums and direct sums with the dimension formula (@thm-direct-sum-criteria, @thm-dimension-formula-subspace-dim), whose proof pattern is the one Rank–Nullity reuses.

Nothing in this chapter needs Chapter 3. Linear systems, row reduction and the rank of a matrix come after it, and every proof here is written so that they can.

## Roadmap

- **Linear maps.** The definition, a gallery of examples and non-examples drawn from geometry, matrices, calculus and algebra, and the fact that makes linear maps manageable: a linear map is determined by, and may be freely prescribed on, a basis.
- **Kernel and image.** The two subspaces attached to every linear map, how to compute an image from a spanning list, and the kernel test that makes injectivity cheap to check.
- **The Rank–Nullity Theorem.** \( \nullity T + \rank T = \dim V \), proved by taking a basis of the kernel and extending it, and the corollaries that let a count replace a check.
- **The algebra of linear maps.** Adding, scaling and composing maps; \( \cL(V, W) \) as a vector space and \( \cL(V) \) as an algebra; polynomials in an operator, and the relations they satisfy.
- **Invertible maps and isomorphisms.** When two spaces are "the same", why dimension alone decides it in finite dimension, and the Invertible Operator Theorem, which collects nine ways to recognize an invertible operator.

## Named moves

- **Injective via the kernel.** To show \( T \) is injective, show that \( T\v = \0 \) forces \( \v = \0 \). One quantifier instead of two.
- **Count instead of check.** When \( \dim V = \dim W \) is finite, injective, surjective and bijective are the same property; check whichever is easier, usually the kernel.
- **Basis of the kernel, then extend.** Take a basis of the smaller space, extend it to the whole, claim the added vectors do the remaining work, and count. This proves Rank–Nullity, and it proved the dimension formula for sums before it.
- **One equation is enough.** Between spaces of equal finite dimension, \( ST = \id \) alone makes both maps invertible — the counting move again, in disguise.
- **Transport along an isomorphism.** An isomorphism carries bases to bases and preserves every statement written in terms of sums and scalar multiples, so a question about \( V \) may be asked in any space isomorphic to it.
