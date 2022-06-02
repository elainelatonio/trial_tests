'''
Create a function named isSymmetric that takes an n×n integer matrix (two dimensional array/list)
as a parameter and returns true if the matrix is symmetric or false if it is not.
Symmetric means it has identical values along its diagonal axis from top-left to bottom-right, as in the first example.
'''

sample = [
  [1, 0, 1, 8],
  [0, 2, 2, 1],
  [1, 2, 5, 6],
[8, 1, 6, 0]
]

def isSymmetric(input):
  def check_if_2darray(input):
    if isinstance(input, list):
      result = [isinstance(item, list) for item in input]
      return all(result)
    return False

  def check_if_nxn(input):
    required_len = len(input)
    return all([len(list) == required_len for list in input])

  if not check_if_2darray(input):
    raise TypeError("input must be 2d array")

  if not check_if_nxn(input):
    raise ValueError("2d array must be nxn")

  for row in range(len(input)):
    for column in range(len(input)):
      if input[row][column] != input[column][row]:
        return False
  return True

print(isSymmetric(sample))