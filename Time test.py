import time

start_time = time.time()
user_input = input("Enter something:")
end_time = time.time()

elapsed_time = end_time - start_time
print("Elapsed time:", elapsed_time)