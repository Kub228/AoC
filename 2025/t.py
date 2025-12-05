# import time

# # Example calculation: 2 + 2
# start = time.perf_counter()
# result = 2 + 2
# end = time.perf_counter()

# execution_time = end - start
# print(f"Time for one calculation: {execution_time:.9f} seconds")


a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
res = list(set(a).union(set(b)))
print(res)