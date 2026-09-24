# Preface

This is a book about linear algebra, written for someone reading it alone, with no lecture to fill the gaps and nobody to ask.

It has twenty-five chapters and two hundred and thirty-six sections, in six parts. It begins at Chapter 0 with statements, proofs, sets, functions, equivalence relations, fields, polynomials and matrices: the tools everything else is built from, and where careful readers first stumble. It ends with representation theory and with numerical computation.

## What is in the book

**Part I, Spaces and Maps.** Vector spaces and dimension; linear systems and elimination, proved rather than recited; linear maps, rank and nullity; and duality, where a subspace is traded for the measurements that vanish on it.

**Part II, Determinants and the Structure of Operators.** Polynomial arithmetic first, because the structure of an operator is read off polynomials. Then determinants, built from what a signed volume must do and not from a formula; block matrices; eigenvalues; and the canonical forms that finally decide when two matrices are similar.

**Part III, Inner Products and Spectral Theory.** Length and angle arrive, ten chapters in. Orthonormal bases, projections and least squares; the spectral theorems; positive matrices and the singular value decomposition.

**Part IV, Forms and Multilinear Algebra.** The measuring is taken away again and the pairing kept: bilinear and quadratic forms, congruence, inertia, the classical groups. Then tensor, symmetric and exterior powers, where the determinant reappears as an induced map on a line.

**Part V, Matrix Analysis.** Six chapters on how big things are and how far they move: norms, variational principles and interlacing, convexity, non-negative matrices, perturbation theory, matrix inequalities.

**Part VI, Geometry, Algebra, Computation.** Affine and projective geometry; algebras and their representations; and a last chapter on how any of this is computed, and what a computed answer means.

## What we promise about proof

This is the part worth reading before the rest, because it is unusual and because we keep it.

Every result in this book is in one of two states, and we always say which. Either it is **proved here**, from material that came earlier — never from a later section, and never from an exercise — or it is **stated with credit and marked plainly as not proved here**, in which case nothing in the book depends on it. There is no third state. We never leave a gap and then build on it.

Keeping that promise costs something, and we would rather the cost were visible. Chapter 7 defines the volume of a parallelepiped by the determinant, proves that no other definition obeys the rules volume must obey, and then states without proof that this agrees with Lebesgue measure, and that nothing depends on it. Chapter 24 lists section by section every classical result it quotes and does not prove, and then says that no theorem in the book rests on any of them.

From Part V on, each chapter opens by listing what it borrows. The clearest instance is Chapter 16. It leans on analysis harder than anything before it, so its opening page numbers the analytic facts it quotes — completeness, monotone convergence, compactness of closed bounded sets, the extreme value theorem, the intermediate value theorem and the mean value theorem — as (A1) to (A6), and every later use names the fact again by its number. Chapters 17 to 20 and 22 to 24 add nothing to that list and say so. Chapter 21 adds exactly one item, (A7), a theorem about functions of a complex variable that linear algebra cannot produce; it states it once and then sets out which of its own results rest on it and which do not.

That accounting matters to us more than any single theorem in the book.

## What a section looks like

Sections are all built the same way.

A section opens with two to four sentences: where we are, what question is open, what this section does. A new idea then arrives through a hook — a naive notion shown failing, an expression that keeps recurring and deserves a name, or a theorem we want and cannot yet state. There is a one-line slogan in plain words, then the definition, with the small words that carry the weight set in bold, then the definition read back clause by clause, because a definition is to be parsed and not memorized.

Examples follow, simplest first, each checked against the definition one clause at a time, spread across the families the book cares about — tuples, polynomials, functions, matrices — with one degenerate case among them. Then a non-example, made by changing an example as little as possible, so that the exact clause that fails can be named. Where there is a trap, a warning names it with a concrete failing case, before you can fall into it.

Theorems come with a sentence saying what need they fill. Most come with an Idea: a few lines of plain prose on how the proof was found. That is where "why would anyone try that" is answered. The proof is kept separate and does mathematics from its first sentence.

Scattered through the text are Quick checks, about three hundred and fifty of them: one short question, with the answer folded away just below. Take them. They are the cheapest way to find out whether reading felt like understanding.

Every section ends with exercises in three groups. **A** is one question in several parts, to be answered before moving on. **B** is practice like the worked examples. **C** goes deeper: a prove-and-deduce pair, a counterexample, a change of field. There are more than fifteen hundred exercises, each with a complete written solution, folded away until you ask for it.

## What we assume

The book is algebraic. For most of its length the scalars are an arbitrary field, and the arguments use the field axioms and what is built from them. Chapters 11 to 13 and much of Part V restrict to the real and complex numbers, and say why each time: a length needs an order so that it can be positive, and a conjugation so that it can be real.

Analysis does enter, because it must — the Fundamental Theorem of Algebra is not a theorem of algebra — but it never enters silently. Chapter 6 isolates the two analytic facts its proof of that theorem uses and proves everything else. Chapter 10 names five facts from analysis before building the matrix exponential. Chapter 14 names the two results its second-derivative test assumes. Chapter 16 gives the standing list, and every chapter after it cites that list by number.

So we do not ask you to know calculus. We ask you to accept, where the book says so, a short list of named facts about the real numbers. If you have met continuity, compactness and the mean value theorem before, Part V will read faster. If you have not, you can still follow every proof, because each one says which fact it uses and states it.

What we do assume is some comfort with proof: reading one, and writing one. Chapter 0 supplies the vocabulary and the standard moves — contrapositive, contradiction, induction, double inclusion, checking that something is well defined — and it is a chapter rather than an appendix because those are where readers stumble. We assume no previous linear algebra: matrices, elimination and determinants are built here from nothing. A reader who has taken a first course will move quickly through the early chapters, and should still not skip them, since the vocabulary of the whole book is fixed there.

## How to read it

Read Parts I, II and III in order. They are the spine, and nothing later stands without them. Chapters 0 to 5 fix the language; Chapters 6 to 10 answer one question, how simple the matrix of an operator can be made; Chapters 11 to 13 answer it again with lengths and angles present.

After that the book branches, and every chapter's opening page tells you what it needs. Spend a minute on it first. It gives the chapter's story, the earlier results it uses with a link to each, a roadmap of one sentence per section, and the named moves the chapter introduces.

Part IV can be deferred, though not skipped. Chapter 17 uses its law of inertia; Chapter 22 uses its quadratic forms and, for one section, its exterior powers; Chapter 23 needs its definition of an algebra and its free vector space. Chapter 24 uses neither chapter at all. Part V is best read in order, with Chapter 16 as its gate. Part VI's three chapters are independent of one another, and each names on its opening page the earlier chapters it never cites.

If you came for one theorem, do not take a chapter list from us. The one that stood here was wrong in every entry, and wrong in the same direction each time: it named fewer chapters than the proofs need. The build now follows the proofs backwards instead, section by section, and works out what a given theorem actually rests on. Ten of those paths, one for each kind of reader, are on the [reading paths](paths.html) page. Each gives its sections in reading order, says how many of the two hundred and thirty-six they are, and says how many more the exercises cost; and each is checked, every time the book is built, to contain everything its own proofs use. The [dependency graph](graph.html) will do the same for any one section you name.

The proofs are written to be read with a pen. Where a move is not visible, a clause says why we make it; where a clause of a definition is delicate, a non-example fails on that clause and no other. None of that replaces closing the book and trying to state the theorem yourself. When something will not come, the chapter's opening page usually names the earlier result you are missing.
