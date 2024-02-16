# Sequences
Cryptography (400 points)
## Description 

I wrote this linear recurrence function, can you figure out how to make it run fast enough and get the flag?
Download the code here [sequences.py](./sequences.py)
Note that even an efficient solution might take several seconds to run. If your solution is taking several minutes, then you may need to reconsider your approach.
## Solution
The problematic part of the Python script is
```python
# This will overflow the stack, it will need to be significantly optimized in order to get the answer :)
@functools.cache
def m_func(i):
    if i == 0: return 1
    if i == 1: return 2
    if i == 2: return 3
    if i == 3: return 4

    return 55692*m_func(i-4) - 9549*m_func(i-3) + 301*m_func(i-2) + 21*m_func(i-1)
```
A quick fix would be to compute the return value iteraitely, not recursively:
```python
def m_func_1(i):
    v = [1, 2, 3, 4]

    if i < 4:
        return v[i]

    for j in range(i - 3):
      v[0], v[1], v[2], v[3] =  v[1], v[2], v[3], 55692*v[0] - 9549*v[1] + 301*v[2] + 21*v[3]

    return v[3]
```
However this is still too slow. Notice that the new values of $v_0, v_1, v_2, v_3$ are actually computed by a matrix multiplication:
```math
\begin{bmatrix}v_0^1\\v_1^1\\v_2^1\\v_3^1\end{bmatrix} = \begin{bmatrix}0 & 1 & 0 & 0\\0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1\\ 55692 & - 9549 & 301 & 21\end{bmatrix} \cdot \begin{bmatrix}v_0^0\\v_1^0\\v_2^0\\v_3^0\end{bmatrix}
```
or more concisely
```math
v^1 = A \cdot v^0
```
What we are looking for is 
```math
v^{i - 3}_3
```
We get this by calculating
```math
v^{i - 3} =  A \cdot v^{i - 4} = A \cdot (A \cdot v^{i - 5}) = A^2 \cdot v^{i - 5} = \dots = A^{i - 3} v^0
```
and extract the last coordinate of this vector. To calculate $A^{i - 3}$ efficiently, we diagonalize $A$, i.e. write $A$ as
```math
A = S \cdot D \cdot S^{-1},
```
where $D$ is a diagonal matrix i. e. a matrix of the form
```math
D = \begin{bmatrix}\lambda_0 & 0 & 0 & 0\\0 & \lambda_1 & 0 & 0 \\ 0 & 0 & \lambda_2 & 0\\ 0 & 0 & 0 & \lambda_3\end{bmatrix}
```
This is useful, since then
```math
A^{i - 3} = A \cdot A \cdot A \cdot \dots \cdot A =  S \cdot D \cdot S^{-1} \cdot S \cdot D \cdot S^{-1} \cdot S \cdot D \cdot S^{-1} \cdot \dots \cdot S \cdot D \cdot S^{-1} = S \cdot D^{i - 3} \cdot S^{-1}
```
and powers of diagonal matrices are easily computable:
```math
D^{i - 3} = \begin{bmatrix}\lambda^{i -3}_0 & 0 & 0 & 0\\0 & \lambda^{i -3}_1 & 0 & 0 \\ 0 & 0 & \lambda^{i -3}_2 & 0\\ 0 & 0 & 0 & \lambda^{i -3}_3\end{bmatrix}
```
While it is possible to compute $D, S, S^{-1}$ with ```numpy```, I computed them with [WolframAlpha](https://www.wolframalpha.com/), to be able to control the representation, and ultimately, precision of matrix elements. This gave me
```math
D = \begin{bmatrix}-21 & 0 & 0 & 0\\0 & 12 & 0 & 0 \\ 0 & 0 & 13 & 0\\ 0 & 0 & 0 & 17\end{bmatrix}, \text{ } S = \begin{bmatrix}-1 & 1 & 1 & 1\\21 & 12 & 13 & 17 \\ -441 & 144 & 169 & 289\\ 9261 & 1728 & 2197 & 4913\end{bmatrix},
\text{ } S^{-1} = \begin{bmatrix} \frac{-13}{209} & \frac{581}{42636} & \frac{-7}{7106} & \frac{1}{42636} \\ \frac{1547}{55} & \frac{-409}{165} & \frac{-3}{55} & \frac{1}{165} \\
\frac{-63}{2} & \frac{405}{136} & \frac{1}{17} & \frac{-1}{136} \\ \frac{819}{190} & \frac{-369}{760} & \frac{-1}{190} & \frac{1}{760} \end{bmatrix}
```
To control precision, I used the ```gmpy2``` library, in particular ```mpz``` type for the representation of the elements of $D^{i - 3}$ and ```mpq``` for the elements of $S^{-1}$:
```python
def m_func(i):
    v_0 = np.array([1, 2, 3, 4])

    if i < 4:
        return v_0[i]

    eigenvalues = [mpz(-21), mpz(12), mpz(13), mpz(17)] 
    eigenvalues_imin3 = np.array([pow(eigenvalue, i - 3) for eigenvalue in eigenvalues])

    D_imin3 = np.diag(eigenvalues_imin3)

    S = np.array([[-1, 1, 1, 1],
              [21, 12, 13, 17],
              [-441, 144, 169, 289],
              [9261, 1728, 2197, 4913]])

    S_inv = np.array([[mpq(-13, 209), mpq(581, 42636), mpq(-7, 7106), mpq(1, 42636)],
              [mpq(1547, 55), mpq(-409, 165), mpq(-3, 55), mpq(1, 165)],
              [mpq(-63, 2), mpq(405, 136), mpq(1, 17), mpq(-1, 136)],
              [mpq(819, 190), mpq(-369, 760), mpq(-1, 190), mpq(1, 760)]])

    A_imin3 = np.dot(np.dot(S, D_imin3), S_inv)

    v_imin3 = np.dot(A_imin3, v_0)

    return v_imin3[3]
```
The function call ```m_func(ITERS)``` took ```2.878s``` for me.


