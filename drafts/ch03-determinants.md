<!--
Draft carried over from the retired LaTeX edition (chapters/chapter03-determinants, removed 2026-09-14).
Not built: the build only reads chapters listed in config/config.json. To publish, move this
file into src/ch03-determinants/ (as index.md plus section files), and add "src/ch03-determinants"
to "chapters" in config/config.json. The chapter title comes from index.md's "# " heading.
-->

# Determinants

Determinants are scalars associated with square matrices that provide important information about the matrix.

## Properties of Determinants

We discuss the properties and computation of determinants.

::: {#thm-det-properties}
[Properties of Determinants]

Let \( \A \) and \( \B \) be \( n \times n \) matrices. Then:

1. \( \det(\A\B) = \det(\A)\det(\B) \);
2. \( \det(\A^\top) = \det(\A) \).
:::

::: {.remark}
TODO: define \( \det \) and prove both properties before publishing.
:::
