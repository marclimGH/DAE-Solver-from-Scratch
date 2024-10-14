## **Gaussian Elimination**

### **Idea:**

Gaussian Elimination is a method for solving systems of linear equations. It systematically transforms the system's augmented matrix into an upper triangular form using elementary row operations. Once in upper triangular form, the solutions are found through back-substitution.

### **Basic Steps:**

1. **Form the Augmented Matrix:**

   For a system \( A\mathbf{x} = \mathbf{b} \), create the augmented matrix \([A | \mathbf{b}]\).

2. **Forward Elimination:**

   - Use **elementary row operations** to create zeros below the leading coefficients (pivots) in each column.
   - The goal is to convert the matrix into an **upper triangular matrix**.

3. **Back-Substitution:**

   - Starting from the last equation, solve for each variable by substituting known values from previous steps.






## **LU Decomposition**

### **Idea:**

LU Decomposition factors a square matrix \( A \) into the product of a **lower triangular matrix** \( L \) and an **upper triangular matrix** \( U \):

\[
A = L \cdot U
\]

This decomposition simplifies solving \( A\mathbf{x} = \mathbf{b} \) by breaking it into two steps:

1. Solve \( L\mathbf{y} = \mathbf{b} \) for \( \mathbf{y} \) (forward substitution).
2. Solve \( U\mathbf{x} = \mathbf{y} \) for \( \mathbf{x} \) (backward substitution).





### **Usage:**

- **Efficient for Multiple Right-Hand Sides:**

  Once \( A \) is decomposed into \( L \) and \( U \), you can solve \( A\mathbf{x} = \mathbf{b} \) for different \( \mathbf{b} \) vectors without recomputing \( L \) and \( U \).

- **Conditions:**

  - \( A \) must be a square matrix.
  - Pivoting may be necessary if zeros appear on the diagonal during decomposition.

---

## **Key Differences**

- **Gaussian Elimination:**

  - Focuses on transforming the augmented matrix directly into upper triangular form.
  - Suitable for solving a single system.

- **LU Decomposition:**

  - Factors the matrix \( A \) into \( L \) and \( U \) matrices.
  - More efficient when solving multiple systems with the same coefficient matrix but different right-hand sides.

---

