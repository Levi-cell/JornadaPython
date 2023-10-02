# Example 1
print("Example 1")
print("-" * 35)

# Local Variables - What are they?
# Every variable created inside a function

def variables():  # function variables
    var = 5        # process
    print(var)     # process

# Using the function outside the function declaration indentation
print("The value of the local variable is:")
variables()  # process return

# Global Variables - What are they?
# Every variable created outside a function
var = "Some value"
print("The value of the global variable is:\n", var)

# Note that local and global variables can have the same name but are not the same
# and therefore can have different values