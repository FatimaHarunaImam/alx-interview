
# Pascal's Triangle

## Description
This project implements a function to generate Pascal's Triangle up to a given number of rows. Pascal's Triangle is a triangular array of binomial coefficients. Each number in the triangle is the sum of the two numbers directly above it.

The function returns a list of lists of integers representing Pascal’s triangle of a given number of rows, `n`.

## Repository
- **GitHub Repository:** alx-interview
- **Directory:** `0x00-pascal_triangle`
- **File:** `0-pascal_triangle.py`

## Function

```python
def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle up to n rows
    """
```

### Parameters:
- `n`: an integer representing the number of rows of Pascal’s Triangle to generate.
  - Returns an empty list if `n <= 0`.

### Example Usage:
```python
>>> from 0-pascal_triangle import pascal_triangle
>>> print(pascal_triangle(5))
[
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]
```

## Files
- **0-main.py:** Example of how to test and print the Pascal's Triangle.
- **0-pascal_triangle.py:** Contains the function that generates the triangle.

## Installation and Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/alx-interview.git
   ```
2. Navigate to the project directory:
   ```bash
   cd alx-interview/0x00-pascal_triangle
   ```
3. Run the script:
   ```bash
   ./0-main.py
   ```

## Requirements
- Python 3.x
- The code must follow PEP 8 style guidelines.

## Author
- **Fatima Haruna Imam** - [GitHub Profile](https://github.com/your-username)
```

You can replace `yourusername` with your actual GitHub username and make sure the file paths match your project structure.
