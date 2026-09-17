

# Kernel and Image

## Definition

::: {#def-kernel}
[Kernel]

Let \( f: V \to W \) be a linear transformation. Define the **kernel** of \( f \) by
\[
\ker (f) \coloneqq \left\{ \v \in V : f(\v) = \mathbf{0}_W \right\}.
\]

i.e. The kernel contains everything in the domain that becomes the zero vector under \( f \).
:::

::: {#def-image}
[Image]

Let \( f: V \to W \) be a linear transformation. Define the **image** of \( f \) by
\[
\im (f) \coloneqq \left\{ \w \in W : \w = f(\v) \text{ for some } \v \in V \right\}.
\]

i.e. The image contains all the possible outputs of the function \( f \).
:::

::: {.remark}
The kernel is also known as the nullspace, which you might be familiar from Gilbert Strang's book. And the image is also called the range. Also, we sometimes denote the image as \( f(V) \).
:::

## Examples {#sec-kernel-image-examples}

::: {#exm-differentiation-kernel-image}
[Differentiation]

Let \( D : \nR[x]_{\leq 3} \to \nR[x]_{\leq 2} \) be defined by \( D(f(x)) = f'(x) \). Find the kernel and image of \( D \).
:::

::: {.solution}
**Kernel:** We seek all polynomials \( f(x) \in \nR[x]_{\leq 3} \) such that \( D(f(x)) = f'(x) = 0 \).

A polynomial has derivative zero if and only if it is a constant. Thus:
\[
    \ker(D) = \{ c : c \in \nR \} = \Span\{1\}.
\]
So \( \dim(\ker(D)) = 1 \).

**Image:** We need to determine which polynomials in \( \nR[x]_{\leq 2} \) can be obtained as derivatives.

Let \( f(x) = a_0 + a_1 x + a_2 x^2 + a_3 x^3 \in \nR[x]_{\leq 3} \). Then:
\[
    D(f(x)) = f'(x) = a_1 + 2a_2 x + 3a_3 x^2.
\]
As \( a_1, a_2, a_3 \) range over all real numbers, we can obtain any polynomial of degree at most 2. Therefore:
\[
    \im(D) = \nR[x]_{\leq 2}.
\]
So \( \dim(\im(D)) = 3 \).

Note that \( \dim(\ker(D)) + \dim(\im(D)) = 1 + 3 = 4 = \dim(\nR[x]_{\leq 3}) \).
:::

::: {#exm-trace-kernel-image}
[Trace]

Let \( \tr : M_2(\nR) \to \nR \) be defined by \( \tr(\A) = a_{11} + a_{22} \). Find the kernel and image of \( \tr \).
:::

::: {.solution}
**Kernel:** We seek all matrices \( \A \in M_2(\nR) \) such that \( \tr(\A) = 0 \).

Let \( \A = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \). Then \( \tr(\A) = a + d = 0 \), which means \( d = -a \).

So the kernel consists of all matrices of the form:
\[
    \A = \begin{bmatrix} a & b \\ c & -a \end{bmatrix} = a\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} + b\begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix} + c\begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}.
\]
Therefore:
\[
    \ker(\tr) = \Span\left\{ \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}, \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix} \right\}.
\]
So \( \dim(\ker(\tr)) = 3 \).

**Image:** For any \( r \in \nR \), we can find a matrix with trace \( r \), for example \( \begin{bmatrix} r & 0 \\ 0 & 0 \end{bmatrix} \).

Therefore:
\[
    \im(\tr) = \nR.
\]
So \( \dim(\im(\tr)) = 1 \).

Note that \( \dim(\ker(\tr)) + \dim(\im(\tr)) = 3 + 1 = 4 = \dim(M_2(\nR)) \).
:::

## Basic Theorems

::: {#thm-prop-kernel}
[Properties of Kernel]

Let \( f: V \to W \) be a linear transformation. Then:

1. \( \ker (f) \) is a subspace of \( V \);

2. \( f \) is injective iff \( \ker (f) = \left\{ \mathbf{0}_V \right\} \).
:::

::: {.proof}
1. - Non-emptiness: As \( f \) is linear, \( f(\mathbf{0}_V) = \mathbf{0}_W \), therefore \( \mathbf{0}_V \in \ker (f) \).
   - Closure under addition: Let \( \v_1, \v_2 \in \ker(f) \), it implies that \( f(\v_1) = \mathbf{0}_W \) and \( f(\v_2) = \mathbf{0}_W \). We have
     \[ f(\v_1 + \v_2) = f (\v_1) + f(\v_2) = \mathbf{0}_W + \mathbf{0}_W = \mathbf{0}_W. \]
     Therefore \( \v_1 + \v_2 \in \ker(f) \).
   - Closure under scalar multiplication: Let \( \v \in \ker(f) \), it implies that \( f(\v) = \mathbf{0}_W \). We have
\[
    f(\lambda \v) = \lambda f(\v) = \lambda \mathbf{0}_W = \mathbf{0}_W.
\]
    Therefore \( \lambda \v \in \ker(f) \).

2. - (\( \Rightarrow \)) Suppose \( f \) is injective. Let \( \v \in \ker (f) \), we have
\begin{align*}
   f(\v) &= \mathbf{0}_W \\
    &= f(\mathbf{0}_V) && \text{(linearity)}
\end{align*}
  By having \( f(\v) = f(\mathbf{0}_V) \) and \( f \) is injective, it implies that \( \v = \mathbf{0}_V \), so \( \ker (f) = \left\{ \mathbf{0}_V \right\} \).
    - (\( \Leftarrow \)) Suppose \( \ker (f) = \left\{ \mathbf{0}_V \right\} \), and we consider \( f(\v) = f(\w) \). Reordering the terms we get \( f(\v) - f(\w) = \mathbf{0}_W \), and since \( f \) is linear we have \( f (\v - \w) = \mathbf{0}_W \). Therefore \( \v - \w \in \ker (f) = \left\{ \mathbf{0}_V \right\} \), implying that \( \v - \w = \mathbf{0}_V \), hence \( \v = \w \). So \( f \) is injective.
:::

::: {#thm-prop-image}
[Properties of Image]

Let \( f: V \to W \) be a linear transformation. Then:

1. \( \im (f) \) is a subspace of \( W \);

2. \( f \) is surjective iff \( \im (f) = W \).
:::

::: {.proof}
1.  - Non-emptiness: Since \( f \) is linear, \( \mathbf{0}_W = f(\mathbf{0}_V) \), therefore \( \mathbf{0}_W \in \im (f) \).
    - Closure under addition: Let \( \w_1, \w_2 \in im (f) \). So \( \w_1 = f(\v_1) \), and \( \w_2 = f(\v_2) \) for some \( \v_1, \v_2 \in V \). Notice that
\[
\w_1 + \w_2 = f(\v_1) + f(\v_2) = f(\v_1 + \v_2).
\]
      Therefore \( \w_1 + \w_2 \in \im (f) \).
    - Closure under scalar multiplication: Let \( \w \in \im (f) \). So \( \w = \f(\v) \) for some \( \v \in V \). Notice that
\[
\lambda \w = \lambda f(\v) = f(\lambda \v).
\]
    Therefore \( \lambda \w \in \im (f) \).

2. \( f \) is surjective \( \Leftrightarrow \) \( \forall\w \in W \), we have \( \w \in f(\v) \) for some \( \v \in V \), that is equivalent to say \( W \subseteq \im (f) \), and by the first condition we know that \( \im (f) \subseteq  W \) is always true. Hence we have \( f \) is surjective \( \Leftrightarrow \) \( W = \im (f) \).
:::
