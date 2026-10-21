num = [1,2,3,4,5,6,7,8,90,12,14,15,167,678,98,78]
def count_even(num):
    count = 0
    for n in num:
        if n % 2 == 0:
            print(f"Even number found: {n}")
            count += 1
    print(f"Total even numbers found: {count}")
    return count

count_even(num)