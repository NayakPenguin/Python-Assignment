import time

def geometric_progression(a, q):
    start_time = time.time()
    term_count = 0

    while True:
        term = a * q ** term_count
        term_count += 1

        if term > 100000:
            total_time = time.time() - start_time
            print("Total time:", total_time)
            print("Time within loop:", time.time() - start_time - total_time)
            return

        yield term

# Example usage
progression_generator = geometric_progression(2, 3)

for term in progression_generator:
    print(term)
