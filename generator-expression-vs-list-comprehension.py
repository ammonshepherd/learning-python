# shows the difference between list comprehension
#   [x*x for x in range(11)]
# and generator expressions
#   (x*x for x in range(11))

# Sytactically, the only difference is list comprehensions are enclosed in
# square brackets, and generator expressions are enclosed in parenthesis.

# Under the hood, list comprehensions are created all at once, the whole list
# is created at once and stored in memory. While generator expressions are
# created as needed, each item created as it comes up.

# This uses the memory_profiler package which is installed with:
#   pip install -U memory_profiler
# and called with
#   python -m memory_profiler generator-expression-vs-list-comprehension.py


# Results when range is range(1000000):
# Filename: generator-expression-vs-list-comprehension.py
# 
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     21   11.469 MiB   11.469 MiB   @profile
#     22                             def ge():
#     23   11.969 MiB    0.004 MiB       ge = (x*x for x in range(1000000))
#     24   11.969 MiB    0.000 MiB       for g in ge:
#     25   11.969 MiB    0.219 MiB           print(g, end="")
#
#
# Filename: generator-expression-vs-list-comprehension.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     31   11.969 MiB   11.969 MiB   @profile
#     32                             def lc():
#     33   58.152 MiB    1.586 MiB       lc = [x*x for x in range(1000000)]
#     34   65.137 MiB    0.004 MiB       for l in lc:
#     35   65.137 MiB    0.012 MiB           print(l, end="")

print()
print("Running generator expression")
@profile
def ge():
    ge = (x*x for x in range(100000))
    for g in ge:
        print(g, end=" ")

ge()

print()
print("Running list comprehension")
@profile
def lc():
    lc = [x*x for x in range(100000)]
    for l in lc:
        print(l, end=" ")
lc()

print()
print("Done")
