def sum_of_n_numbers(n):
    if n < 0:
        return "n must be a positive integer."
    else:
        total = 0
        for i in range(1, n + 1):
            total += i
        return total

# Example usage
n = int(input("Enter a positive integer: "))
result = sum_of_n_numbers(n)
print(f"The sum of the first {n} numbers is {result}.")
