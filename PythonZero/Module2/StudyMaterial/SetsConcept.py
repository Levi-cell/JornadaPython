# DECLARING SETS
setExample = {'banana', 'apple', 'orange', 'grape'}

### We use braces or the set() function to declare sets
### Be careful when creating empty sets!! Use set() instead of {}

################################# MATHEMATICAL OPERATIONS ON SETS

print("""
PYTHON OPERATOR ///// DESCRIPTION
      in               element is a member of S
      <=               A is a subset of B
      <                A is a proper subset of B
      |                A union with B
      &                A intersection with B
      -                Difference between A and B
""")

# Example 1
print("-" * 35)
print('Example 1:')

setA = {0, 1, 3, 5, 7, 9}
setB = {0, 2, 4, 6, 8}

setC = setA.union(setB)  # or more concise way: setC = setA | setB
print(setC)