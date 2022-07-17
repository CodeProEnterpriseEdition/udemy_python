# FIRST EXAMPLE:
import pdb
first = "First"
second = "Second"
pdb.set_trace()
result = first + second
third = "Third"
# pdb.set_trace()
result += third
print(result)


# import pdb
# pdb.set_trace()

# Also commonly on oneline:
# import pdb; pdb.set_trace()

# Common PDB Commands:
# l (list)
# n (next line)
# p (print)     = p muuttujan_nimi esim. p first
# c (continue - finishes debugging)
