# Function to calculate mean
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

# calculate median
def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        middle1 = sorted_numbers[n // 2 - 1]
        middle2 = sorted_numbers[n // 2]
        median = (middle1 + middle2) / 2
    else:
        median = sorted_numbers[n // 2]
    return median

#  calculate average
def calculate_average(numbers):
    return calculate_mean(numbers)

# Main function
if __name__ == "__main__":
    # Input numbers from the user
    numbers = []
    n = int(input("Enter the number of elements: "))
    for _ in range(n):
        num = float(input("Enter a number: "))
        numbers.append(num)

    # Calculate mean, median, and average
    mean = calculate_mean(numbers)
    median = calculate_median(numbers)
    average = calculate_average(numbers)

    # Display the results
    print("Mean: {:.2f}".format(mean))
    print("Median: {:.2f}".format(median))
    print("Average: {:.2f}".format(average))
