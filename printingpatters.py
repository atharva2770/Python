# printing '#' in this pattern

# print("# # # #")
# print("# # # #")
# print("# # # #")
# print("# # # #")

# another method

# for i in range(4):
#     for j in range(4):
#         print("# ", end="")

#     print()

# '***************************************
#next [pattern]

# for i in range(4):
#     for j in range(i+1):
#         print("# ", end="")

#     print()

# '***************************************
#next [pattern]

for i in range(4):
    for j in range(4-i):
        print("# ", end="")

    print()
