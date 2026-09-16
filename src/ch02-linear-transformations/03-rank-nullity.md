

# Rank-Nullity Theorem

## Nullity and Rank

::: {#def-nullity}
[Nullity]
Let \( f : V \to W \) be a linear transformation. The **nullity** of \( f \) is defined by
\[
\nullity(f) \coloneqq \dim (\ker (f)).
\]
:::

::: {#def-rank}
[Rank]
Let \( f : V \to W \) be a linear transformation. The **rank** of \( f \) is defined by
\[
\rank(f) \coloneqq \dim (\im (f)).
\]
:::

::: {#exm-nullity-rank-diff}
Recall that for \( D : \nR[x]_{\leq 3} \to \nR[x]_{\leq 2} \) defined by
\[
D(f(x)) = f'(x),
\]
we have \( \ker(D) = \nR \) and \( \im (D) = \nR[x]_{\leq 2} \). Compute the nullity and image of \( D \).
:::

::: {.solution}
\( \nullity (D) \coloneqq \dim_{\nR} (\ker (D)) = \dim_{\nR} (\nR) = 1 \).

\( \rank (D) \coloneqq \dim_{\nR} (\im (D)) = \dim_{\nR} (\nR[x]_{\leq 2}) = 3 \).
:::

::: {.remark}
For other examples of nullity and rank, review the examples in the last section, which we have it covered.
:::

## The Theorem

::: {#thm-rank-nullity}
[Rank-Nullity Theorem]
Let \( V \) be a finite dimensional vector space and \( f : V \to W \) be a linear transformation. Then we have
\[
\nullity(f) + \rank(f) = \dim (V).
\]
:::

::: {.proof}
Let \( S = \left\{ \v_1, \v_2, \dots, \v_n \right\} \) be a basis of \( \ker (f) \), having \( \nullity(f) = \dim (\ker f) = n \). Since \( \ker (f) \subseteq V \), by Basis Extension Theorem, we can extend \( S \) to \( S' = \left\{ \v_1, \dots, \v_n, \s_1, \dots, \s_k \right\} \), a basis of \( V \), having \( \dim (V) = n + k \).

::: {.claim}
\( S'' = \left\{ f(\s_1), f(\s_2), \dots, f(\s_k) \right\} \) is a basis of \( \im (f) \).
:::

::: {.proof}
We verify two properties.

*Spanning.* Let \( \w \in \im (f) \), we have \( \w = f(\v) \) for some \( \v \in V \) by definition. As \( S' \) is a basis of \( V \), we can write \( \v = \sum_{i = 1}^n \alpha_i \v_i + \sum_{i = 1}^k \beta_i \s_i \). Then we apply \( f \) to both sides:
\[
\w = f(\v) = f \left( \sum \alpha_i \v_i + \sum \beta_i \s_i \right) = \sum \alpha_i f(\v_i) + \sum \beta_i f(\s_i) = \sum \beta_i f(\s_i),
\]
where the last equality holds since \( \v_i \in \ker (f) \). Since \( \w \) can be expressed by \( f(\s_i) \)'s, therefore \( S'' \) spans \( \im (f) \).

*Linear independence.* Suppose that \( \alpha_1 f(\s_1) + \cdots + \lambda_k f(\s_k) = \mathbf{0} \). By linearity of \( f \), it becomes \( f(\alpha_1 \s_1 + \cdots + \alpha_k \s_k) = \mathbf{0} \). Therefore we have \( \alpha_1 \s_1 + \cdots + \alpha_k \s_k \in \ker (f) \). Moreover, as \( S \) is a basis of \( \ker (f) \), we know that \( \sum \alpha_i \s_i = \sum \beta_i \v_i \) for some \( \beta_i \in F \). Reordering gives \( \sum \alpha_i \s_i - \sum \beta_i \v_i = \mathbf{0} \). As \( S' \) is linearly independent, this forces all \( \alpha_i \)'s and \( \beta_i \)'s to be \( 0 \). This completes the proof of the claim.
:::

Hence, we have
\[
\rank (f) = \dim (\im (f)) = k = (n + k) - n = \dim (V) - \nullity (f).
\]
:::

For the map \( f_\A : \nR^4 \to \nR^3 \), \( f_\A(\v) = \A\v \), the rank and nullity can be computed exactly with SymPy. In the online version the code can be edited and run; for any matrix, the sum is the number of columns, \( \dim (\nR^4) = 4 \).

```{.python .run #cell-rank-nullity}
from sympy import Matrix

A = Matrix([
    [1, 2, 3, 4],
    [2, 4, 6, 8],
    [1, 0, 1, 0],
])
rank = A.rank()                  # dim(im f_A)
nullity = len(A.nullspace())     # dim(ker f_A): size of a basis of the kernel
print("rank =", rank, " nullity =", nullity, " columns =", A.cols)
rank + nullity == A.cols
```
