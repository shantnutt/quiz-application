'''Nmae: Shantnu
Enrollement: 0103AL231190
Batch: Python-5
Batch_time: 10:30 to 12:10'''
print("Hello World")


# Q1. Write a program to check whether a number is positive, negative, or zero.
print("--- Solution 1 ---")
num = float(input("Q1: Enter a number: "))
if num > 0:
   print(str(num) + " is Positive")
elif num == 0:
   print("It's Zero")
else:
   print(str(num) + " is Negative")


# Q2. Write a program to check whether a number is even or odd.
print("\n--- Solution 2 ---")
number = int(input("Q2: Enter a number: "))
if (number % 2) == 0:
   print(str(number) + " is an Even number")
else:
   print(str(number) + " is an Odd number")
print("="*25)


# Q3. Write a program to check if a given year is a leap year or not.
print("\n--- Solution 3 ---")
year = int(input("Q3: Enter a year to check: "))
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(str(year) + " is a leap year.")
else:
    print(str(year) + " is not a leap year.")
print("="*25)


# Q4. Write a program to find the greatest of two numbers.
print("\n--- Solution 4 ---")
x = float(input("Q4: Enter the first number: "))
y = float(input("Q4: Enter the second number: "))
if x > y:
    print("The greater number is: " + str(x))
elif y > x:
    print("The greater number is: " + str(y))
else:
    print("Both numbers are the same.")


# Q5. Write a program to check whether a person is eligible to vote (age >= 18).
print("\n--- Solution 5 ---")
age = int(input("Q5: Please enter your age: "))
if age >= 18:
    print("Congratulations! You are eligible to vote.")
else:
    print("Sorry, you are not yet eligible to vote.")
print("="*25)


# Q6. Write a program to check whether a given character is a vowel or consonant.
print("\n--- Solution 6 ---")
my_char = input("Q6: Enter a single character: ").lower()
if my_char == 'a' or my_char == 'e' or my_char == 'i' or my_char == 'o' or my_char == 'u':
    print("The character '" + my_char + "' is a vowel.")
else:
    print("The character '" + my_char + "' is a consonant.")


# Q7. Write a program to check if a number is divisible by 5.
print("\n--- Solution 7 ---")
val = int(input("Q7: Enter a number: "))
if (val % 5) == 0:
    print(str(val) + " is divisible by 5.")
else:
    print(str(val) + " is not divisible by 5.")
print("="*25)


# Q8. Write a program to determine whether a given number is a single-digit, two-digit, or more than two-digit number.
print("\n--- Solution 8 ---")
num8 = int(input("Q8: Enter an integer: "))
abs_num = abs(num8)
if abs_num < 10:
    print(str(num8) + " is a single-digit number.")
elif abs_num < 100:
    print(str(num8) + " is a two-digit number.")
else:
    print(str(num8) + " has more than two digits.")


# Q9. Write a program to check whether a student has passed or failed (passing marks = 40).
print("\n--- Solution 9 ---")
score = float(input("Q9: Enter the student's marks: "))
if score >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
print("="*25)


# Q10. Write a program to find whether the entered number is a multiple of both 3 and 7.
print("\n--- Solution 10 ---")
check_num = int(input("Q10: Enter a number: "))
if (check_num % 3 == 0) and (check_num % 7 == 0):
    print(str(check_num) + " is a multiple of 3 and 7.")
else:
    print(str(check_num) + " isn't a multiple of both 3 and 7.")

#-------------------------------------------------
# Ladder If & Nested If
#-------------------------------------------------

# Q1. Write a program to find the greatest among three numbers.
print("\n--- Solution 11 ---")
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
if n1 >= n2 and n1 >= n3:
    largest = n1
elif n2 >= n1 and n2 >= n3:
    largest = n2
else:
    largest = n3
print("The largest number is", largest)


# Q2. Write a program to classify a person based on age: Child (<13), Teenager (13-19), Adult (20-59), Senior (60+).
print("\n--- Solution 12 ---")
person_age = int(input("Enter age: "))
if person_age < 13:
    print("Classification: Child")
elif person_age <= 19:
    print("Classification: Teenager")
elif person_age <= 59:
    print("Classification: Adult")
else:
    print("Classification: Senior")


# Q3. Write a program to assign grades based on marks: 90-100: A, 75-89: B, 50-74: C, 35-49: D, <35: Fail.
print("\n--- Solution 13 ---")
marks = float(input("Enter marks: "))
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
elif marks >= 35:
    grade = "D"
else:
    grade = "Fail"
print("Grade:", grade)


# Q4. Write a program to check the type of triangle (equilateral, isosceles, or scalene) based on sides.
print("\n--- Solution 14 ---")
side1 = float(input("Enter length of side 1: "))
side2 = float(input("Enter length of side 2: "))
side3 = float(input("Enter length of side 3: "))
if side1 == side2 and side2 == side3:
    print("It is an Equilateral triangle.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("It is an Isosceles triangle.")
else:
    print("It is a Scalene triangle.")


# Q5. Write a program to check if a character is uppercase, lowercase, digit, or special symbol.
print("\n--- Solution 15 ---")
char_input = input("Enter a character: ")
if 'a' <= char_input <= 'z':
    print("The character is a lowercase letter.")
elif 'A' <= char_input <= 'Z':
    print("The character is an uppercase letter.")
elif '0' <= char_input <= '9':
    print("The character is a digit.")
else:
    print("The character is a special symbol.")


# Q6. Write a program to calculate electricity bill based on units.
print("\n--- Solution 16 ---")
units = float(input("Enter number of units: "))
bill = 0
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
print("Total electricity bill: Rs.", bill)


# Q7. Write a program to determine the largest of four numbers using nested if.
print("\n--- Solution 17 ---")
num_a = int(input("Enter first number: "))
num_b = int(input("Enter second number: "))
num_c = int(input("Enter third number: "))
num_d = int(input("Enter fourth number: "))
if num_a > num_b:
    if num_a > num_c:
        if num_a > num_d:
            greatest = num_a
        else:
            greatest = num_d
    else:
        if num_c > num_d:
            greatest = num_c
        else:
            greatest = num_d
else:
    if num_b > num_c:
        if num_b > num_d:
            greatest = num_b
        else:
            greatest = num_d
    else:
        if num_c > num_d:
            greatest = num_c
        else:
            greatest = num_d
print("The largest number is:", greatest)


# Q8. Write a program to check if a given year is a century year and also a leap year.
print("\n--- Solution 18 ---")
input_year = int(input("Enter a year: "))
if input_year % 100 == 0:
    print(input_year, "is a century year.")
    if input_year % 400 == 0:
        print("It is also a leap year.")
    else:
        print("But it is not a leap year.")
else:
    print(input_year, "is not a century year.")


# Q9. Write a program to classify BMI value.
print("\n--- Solution 19 ---")
weight_kg = float(input("Enter weight in kg: "))
height_m = float(input("Enter height in meters: "))
bmi = weight_kg / (height_m * height_m)
print("Your BMI is:", bmi)
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")


# Q10. Write a program to display the smallest number among three using nested if.
print("\n--- Solution 20 ---")
val1 = int(input("Enter first number: "))
val2 = int(input("Enter second number: "))
val3 = int(input("Enter third number: "))
if val1 < val2:
    if val1 < val3:
        smallest = val1
    else:
        smallest = val3
else:
    if val2 < val3:
        smallest = val2
    else:
        smallest = val3
print("The smallest number is:", smallest)


#-------------------------------------------------
# For Loop Problems
#-------------------------------------------------

# Q1. Write a program using a for loop to print all Armstrong numbers between 100 and 999.
print("\n--- Solution 21 ---")
print("Armstrong numbers between 100 and 999 are:")
for number in range(100, 1000):
    sum_of_cubes = 0
    temp_num = number
    for digit in str(temp_num):
        sum_of_cubes += int(digit) ** 3
    if sum_of_cubes == number:
        print(number)


# Q2. Write a program to generate and display the first n prime numbers using a for loop.
print("\n--- Solution 22 ---")
n_primes = int(input("Enter how many prime numbers to display: "))
count = 0
num_to_check = 2
while count < n_primes:
    is_prime = True
    for i in range(2, int(num_to_check**0.5) + 1):
        if num_to_check % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num_to_check, end=" ")
        count += 1
    num_to_check += 1
print()


# Q3. Write a program to display all numbers from 1 to 500 that are divisible by 3, but the sum of their digits should not exceed 10.
print("\n--- Solution 23 ---")
for i in range(1, 501):
    if i % 3 == 0:
        digit_sum = 0
        for digit in str(i):
            digit_sum += int(digit)
        if digit_sum <= 10:
            print(i, end=" ")
print()


# Q4. Write a program using a for loop to print a pyramid of stars (*) of height n.
print("\n--- Solution 24 ---")
height = int(input("Enter the height of the pyramid: "))
for i in range(height):
    for j in range(height - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()


# Q5. Write a program to accept a string and check whether it is a pangram.
print("\n--- Solution 25 ---")
input_string = input("Enter a string: ").lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
is_pangram = True
for char in alphabet:
    if char not in input_string:
        is_pangram = False
        break
if is_pangram:
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")


# Q6. Write a program using a for loop to print all twin primes between 1 and 100.
print("\n--- Solution 26 ---")
def check_prime(num_to_check):
    if num_to_check < 2:
        return False
    for i in range(2, num_to_check):
        if num_to_check % i == 0:
            return False
    return True

print("Twin primes between 1 and 100:")
for num in range(1, 99):
    if check_prime(num) and check_prime(num + 2):
        print("(" + str(num) + ", " + str(num + 2) + ")")


# Q7. Write a program that accepts a number and prints whether it is a Harshad number.
print("\n--- Solution 27 ---")
harshad_num = int(input("Enter a number: "))
s_digits = 0
for d in str(harshad_num):
    s_digits += int(d)
if harshad_num % s_digits == 0:
    print(harshad_num, "is a Harshad number.")
else:
    print(harshad_num, "is not a Harshad number.")


# Q8. Write a program to generate Pascal’s Triangle up to n rows.
print("\n--- Solution 28 ---")
rows = int(input("Enter number of rows for Pascal's Triangle: "))
triangle = []
for i in range(rows):
    row = [1] * (i + 1)
    if i > 1:
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
    triangle.append(row)
    print(row)

# Q9. Write a program using a for loop to display the sum of the series: 1^2 + 2^2 + 3^2 + ... + n^2
print("\n--- Solution 29 ---")
n_series = int(input("Enter the value of n: "))
total_sum = 0
for i in range(1, n_series + 1):
    total_sum += i * i
print("Sum of the series is:", total_sum)


# Q10. Write a program that accepts a number and prints whether it is a Strong number.
print("\n--- Solution 30 ---")
strong_num_input = int(input("Enter a number to check for Strong number: "))
sum_of_factorials = 0
for digit in str(strong_num_input):
    fact = 1
    for i in range(1, int(digit) + 1):
        fact = fact * i
    sum_of_factorials += fact

if sum_of_factorials == strong_num_input:
    print(strong_num_input, "is a Strong number.")
else:
    print(strong_num_input, "is not a Strong number.")


#-------------------------------------------------
# While Loop Problems
#-------------------------------------------------

# Q11. Write a program using a while loop to find the reverse of a number and check if the reversed number is prime.
print("\n--- Solution 31 ---")
num_to_rev = int(input("Enter a number: "))
rev_num = 0
temp = num_to_rev
while temp > 0:
    digit = temp % 10
    rev_num = rev_num * 10 + digit
    temp = temp // 10
print("Reverse is:", rev_num)
is_rev_prime = True
if rev_num < 2:
    is_rev_prime = False
else:
    i = 2
    while i*i <= rev_num:
        if rev_num % i == 0:
            is_rev_prime = False
            break
        i += 1
if is_rev_prime:
    print(rev_num, "is a prime number.")
else:
    print(rev_num, "is not a prime number.")


# Q12. Write a program that continues to accept numbers from the user until the sum of digits of all numbers entered becomes greater than 100.
print("\n--- Solution 32 ---")
total_digit_sum = 0
while total_digit_sum <= 100:
    print("Current total sum of digits:", total_digit_sum)
    user_num = input("Enter a number: ")
    for digit in user_num:
        total_digit_sum += int(digit)
print("Final sum of digits", total_digit_sum, "is greater than 100. Halting.")


# Q13. Write a program using a while loop to check whether a number is a Duck number.
print("\n--- Solution 33 ---")
duck_input = input("Enter a number: ")
if duck_input.startswith('0'):
    print(duck_input, "is not a Duck number (starts with 0).")
else:
    has_zero = False
    for digit in duck_input:
        if digit == '0':
            has_zero = True
            break
    if has_zero:
        print(duck_input, "is a Duck number.")
    else:
        print(duck_input, "is not a Duck number.")


# Q14. Write a program using a while loop to check if it is a Happy number.
print("\n--- Solution 34 ---")
happy_input = int(input("Enter a number: "))
seen_numbers = []
current_num = happy_input
while current_num != 1 and current_num not in seen_numbers:
    seen_numbers.append(current_num)
    sum_sq = 0
    temp = current_num
    while temp > 0:
        d = temp % 10
        sum_sq += d * d
        temp //= 10
    current_num = sum_sq
if current_num == 1:
    print(happy_input, "is a Happy number.")
else:
    print(happy_input, "is not a Happy number.")


# Q15. Write a program using a while loop to find the largest prime factor of a given number.
print("\n--- Solution 35 ---")
n = int(input("Enter a number to find its largest prime factor: "))
factor = 2
while factor * factor <= n:
    if n % factor:
        factor += 1
    else:
        n //= factor
print("Largest prime factor is:", n)


# Q16. Write a program to repeatedly accept a string from the user until the string entered is a palindrome.
print("\n--- Solution 36 ---")
while True:
    user_string = input("Enter a string: ")
    if user_string == user_string[::-1]:
        print("This is a palindrome! Thank you.")
        break
    else:
        print("Not a palindrome. Please try again.")


# Q17. Write a program using a while loop to compute the digital root of a number.
print("\n--- Solution 37 ---")
digital_root_num = int(input("Enter a number: "))
while digital_root_num >= 10:
    sum_digits = 0
    temp = digital_root_num
    while temp > 0:
        sum_digits += temp % 10
        temp //= 10
    digital_root_num = sum_digits
print("The digital root is:", digital_root_num)


# Q18. Write a program using a while loop to generate the Collatz sequence for a given number.
print("\n--- Solution 38 ---")
collatz_num = int(input("Enter a starting number for the Collatz sequence: "))
while collatz_num != 1:
    print(collatz_num, end=" -> ")
    if collatz_num % 2 == 0:
        collatz_num = collatz_num // 2
    else:
        collatz_num = 3 * collatz_num + 1
print(1)


# Q19. Write a program using a while loop to accept a number and check whether it is a Kaprekar number.
print("\n--- Solution 39 ---")
kap_num = int(input("Enter a number: "))
sq_num = kap_num * kap_num
sq_str = str(sq_num)
is_kaprekar = False
i = 1
while i < len(sq_str):
    part1_str = sq_str[:i]
    part2_str = sq_str[i:]
    if int(part1_str) > 0 and int(part2_str) > 0:
        if int(part1_str) + int(part2_str) == kap_num:
            is_kaprekar = True
            break
    i += 1
if is_kaprekar:
    print(kap_num, "is a Kaprekar number.")
else:
    print(kap_num, "is not a Kaprekar number.")


# Q20. Write a program to simulate an ATM machine using a while loop.
print("\n--- Solution 40 ---")
balance = 10000.00
while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        print("Your current balance is: Rs.", balance)
    elif choice == '2':
        deposit_amount = float(input("Enter amount to deposit: "))
        balance += deposit_amount
        print("Deposit successful. New balance: Rs.", balance)
    elif choice == '3':
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount > balance:
            print("Insufficient balance.")
        else:
            balance -= withdraw_amount
            print("Withdrawal successful. New balance: Rs.", balance)
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")