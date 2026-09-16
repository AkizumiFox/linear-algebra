<!--
Draft carried over from the retired LaTeX edition (chapters/chapter04-diagonalization, removed 2026-09-14).
Not built: the build only reads src/. To publish, move this file into src/ch04-diagonalization/,
add "src/ch04-diagonalization" to "chapters" in config/config.json, and add the chapter name in
build/manifest.py (chapter_names).
-->

# Diagonalization

This chapter focuses on the diagonalization of matrices and its applications.

## Eigenvalues and Eigenvectors

::: {#def-eigenvalue}
[Eigenvalue and Eigenvector]

Let \( \A \) be an \( n \times n \) matrix. A scalar \( \lambda \in \nC \) is called an **eigenvalue** of \( \A \) if there exists a non-zero vector \( \v \in \nC^n \) such that
\[
\A\v = \lambda\v.
\]
The vector \( \v \) is called an **eigenvector** corresponding to \( \lambda \).
:::

::: {#thm-spectral-symmetric}
[Spectral Theorem for Symmetric Matrices]

Every real symmetric matrix \( \A \) can be diagonalized by an orthogonal matrix \( \Q \):
\[
\A = \Q \vLambda \Q^\top,
\]
where \( \vLambda = \diag(\lambda_1, \lambda_2, \ldots, \lambda_n) \) is a diagonal matrix containing the eigenvalues of \( \A \), and the columns of \( \Q \) are the corresponding orthonormal eigenvectors.
:::

::: {.proof}
We proceed by induction on the dimension \( n \).

**Base case (\( n = 1 \)).** Any \( 1 \times 1 \) matrix is already diagonal.

**Inductive step.** Assume the theorem holds for all \( (n-1) \times (n-1) \) symmetric matrices.

Let \( \A \) be an \( n \times n \) real symmetric matrix. Since \( \A \) is symmetric, it has a real eigenvalue \( \lambda_1 \) with corresponding unit eigenvector \( \v_1 \).

Let \( \Q_1 \) be an orthogonal matrix with \( \v_1 \) as its first column. Then
\[
\Q_1^\top \A \Q_1 = \begin{pmatrix} \lambda_1 & \mathbf{0}^\top \\ \mathbf{0} & \B \end{pmatrix},
\]
where \( \B \) is an \( (n-1) \times (n-1) \) symmetric matrix (symmetry is preserved under orthogonal transformations).

By the inductive hypothesis, there exists an orthogonal \( (n-1) \times (n-1) \) matrix \( \P \) such that \( \B = \P \vLambda' \P^\top \) where \( \vLambda' \) is diagonal.

Setting \( \Q = \Q_1 \begin{pmatrix} 1 & \mathbf{0}^\top \\ \mathbf{0} & \P \end{pmatrix} \) gives the desired decomposition.
:::

::: {.remark}
TODO before publishing: the proof uses two facts this book has not proved yet — that a real symmetric matrix has a real eigenvalue, and that \( \Q_1^\top \A \Q_1 \) has the block form above (the first column follows from \( \A\v_1 = \lambda_1\v_1 \), the zero first row from symmetry). Orthogonal matrices and inner products also need to be introduced first.
:::
