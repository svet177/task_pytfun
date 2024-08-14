def calculate_average(*args):
    """Calculate and print the average of the given arguments."""
    if not args:
        print("Arguments missing")
        return
    #workout the average value of arguments
    total = sum(args)
    count = len(args)
    average = total / count

    print(f"Passed arguments average: {average:.10f}")

#Examples:
calculate_average(10, 20, 30)
calculate_average(1, 2, 3, 4, 5)
calculate_average(5.5, 10.1, 7.3, 100, 200 , 4654878, 4, 0.0000005, 0.000003,0.0000004,0.00000007)
