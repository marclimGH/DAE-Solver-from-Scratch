## **Iterative Methods for Solving Linear Systems**

### **Introduction**

Iterative methods solve linear systems of equations of the form:

\[
A\mathbf{x} = \mathbf{b}
\]

by starting with an initial guess \(\mathbf{x}^{(0)}\) and iteratively refining it to approach the exact solution. These methods are particularly useful for large, sparse, or structured systems where direct methods (like Gaussian elimination) are computationally expensive.

### **Key Characteristics**

- **Scalability:** Suitable for large-scale problems.
- **Memory Efficiency:** Exploit sparsity to reduce memory usage.
- **Approximate Solutions:** Provide progressively better approximations.

---

## **The Most Basic Iterative Method: Jacobi Method**

### **Idea**

The **Jacobi Method** updates each component of the solution vector independently using values from the previous iteration. It's one of the simplest iterative techniques for solving linear systems.

### **Algorithm**

Given a system \(A\mathbf{x} = \mathbf{b}\), where \(A\) is a square matrix with non-zero diagonal elements, the Jacobi method updates each component \(x_i\) as follows:

\[
x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{\substack{j=1 \\ j \neq i}}^{n} a_{ij} x_j^{(k)} \right)
\]

- **\(x_i^{(k+1)}\):** The updated value of \(x_i\) at iteration \(k+1\).
- **\(x_j^{(k)}\):** The value of \(x_j\) from the previous iteration \(k\).
- **\(a_{ij}\):** Elements of matrix \(A\).
- **\(b_i\):** Elements of vector \(\mathbf{b}\).

### **Convergence Criteria**

- **Diagonal Dominance:** The method converges if \(A\) is strictly diagonally dominant, i.e.,

  \[
  |a_{ii}| > \sum_{\substack{j=1 \\ j \neq i}}^{n} |a_{ij}| \quad \text{for all } i
  \]

- **Symmetric Positive Definite Matrices:** Convergence is also guaranteed if \(A\) is symmetric positive definite.

### **Example**

Consider the system:

\[
\begin{cases}
10x_1 - x_2 + 2x_3 = 6 \\
 -x_1 + 11x_2 - x_3 = 25 \\
2x_1 - x_2 + 10x_3 = -11 \\
\end{cases}
\]

**Iteration Formulae:**

\[
\begin{aligned}
x_1^{(k+1)} &= \frac{1}{10} \left( 6 + x_2^{(k)} - 2x_3^{(k)} \right) \\
x_2^{(k+1)} &= \frac{1}{11} \left( 25 + x_1^{(k)} + x_3^{(k)} \right) \\
x_3^{(k+1)} &= \frac{1}{10} \left( -11 - 2x_1^{(k)} + x_2^{(k)} \right) \\
\end{aligned}
\]

**Procedure:**

1. **Initial Guess:** Start with \( x^{(0)} = [0, 0, 0]^T \).
2. **Iterate:** Apply the iteration formulae to compute \( x^{(1)}, x^{(2)}, \ldots \).
3. **Convergence:** Continue until \( \| x^{(k+1)} - x^{(k)} \| < \text{tolerance} \).

---

## **Sparse Linear Solvers**

### **Introduction**

Sparse linear solvers are specialized algorithms designed to efficiently solve linear systems where the matrix \(A\) is sparse—meaning most of its elements are zero.

### **Why Use Sparse Solvers?**

- **Memory Efficiency:** Store only non-zero elements, reducing memory requirements.
- **Computational Efficiency:** Exploit sparsity to minimize arithmetic operations.

### **Common Sparse Iterative Methods**

1. **Conjugate Gradient (CG) Method:**
   - Used for symmetric positive definite matrices.
   - Minimizes the quadratic form associated with \( A \).

2. **Bi-Conjugate Gradient Stabilized (BiCGSTAB) Method:**
   - Handles nonsymmetric and indefinite matrices.
   - Improves convergence over standard Bi-Conjugate Gradient methods.

3. **Generalized Minimal Residual (GMRES) Method:**
   - Suitable for nonsymmetric matrices.
   - Builds an orthonormal basis to minimize the residual over a Krylov subspace.

### **Example: Conjugate Gradient Method**

**Algorithm Steps:**

1. **Initialization:**
   - Choose \( x^{(0)} \) (initial guess).
   - Compute residual \( r^{(0)} = b - A x^{(0)} \).
   - Set \( p^{(0)} = r^{(0)} \).

2. **Iterative Process:**
   - For \( k = 0, 1, 2, \ldots \):
     \[
     \begin{aligned}
     \alpha_k &= \frac{(r^{(k)})^T r^{(k)}}{(p^{(k)})^T A p^{(k)}} \\
     x^{(k+1)} &= x^{(k)} + \alpha_k p^{(k)} \\
     r^{(k+1)} &= r^{(k)} - \alpha_k A p^{(k)} \\
     \beta_k &= \frac{(r^{(k+1)})^T r^{(k+1)}}{(r^{(k)})^T r^{(k)}} \\
     p^{(k+1)} &= r^{(k+1)} + \beta_k p^{(k)} \\
     \end{aligned}
     \]

3. **Convergence Check:**
   - Stop when \( \| r^{(k+1)} \| < \text{tolerance} \).


---

## **Summary**

- **Iterative Methods:** Provide approximate solutions through successive refinements; essential for large-scale systems.
- **Jacobi Method:** Simplest iterative method; updates variables independently using previous iteration values.
- **Sparse Linear Solvers:** Exploit matrix sparsity to reduce computational and memory demands; crucial for handling large, sparse systems efficiently.
- **Advanced Iterative Methods:** Conjugate Gradient, BiCGSTAB, and GMRES offer better convergence properties for specific types of matrices.

---

**Note:** When choosing an iterative method or sparse solver, consider the properties of the matrix \( A \) (e.g., symmetry, positive definiteness, sparsity pattern) and the requirements of the problem (e.g., accuracy, computational resources).

