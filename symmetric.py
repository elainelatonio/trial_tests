'''
Create a function named isSymmetric that takes an n×n integer matrix (two dimensional array/list)
as a parameter and returns true if the matrix is symmetric or false if it is not.
Symmetric means it has identical values along its diagonal axis from top-left to bottom-right, as in the first example.
'''

sample = [
  [7, 7, 7],
  [6, 5, 7],
  [1, 2, 1]
]

def isSymmetric(input):
  def check_if_2darray(input):
    if isinstance(input, list):
      result = [isinstance(item, list) for item in input]
      return all(result)
    return False

  def check_if_nxn(input):
    REQUIRED_LEN = len(input)
    return all([len(list) == REQUIRED_LEN for list in input])

  def check_if_symmetric(input):
    transposed_array = []
    for col in range(len(input)):
      transposed_array_row = []
      for row in range(len(input)):
        transposed_array_row.append(input[row][col])
      transposed_array.append(transposed_array_row)
    return(input == transposed_array)

  if not check_if_2darray(input):
    raise TypeError("input must be 2d array")

  if not check_if_nxn(input):
    raise ValueError("2d array must be nxn")

  return check_if_symmetric(input)

print(isSymmetric(sample))