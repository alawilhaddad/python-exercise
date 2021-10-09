# https://www.hackerrank.com/challenges/30-data-types/problem

i = 4
d = 4.0
s = 'HackerRank '

if __name__ == "___main__":
    # Declare second integer, double, and String variables.
    x, y, z = int(input()), float(input()), input()
    # Print the sum of both integer variables on a new line.
    print(int(i+x))
    # Print the sum of the double variables on a new line.
    print(d+y)
    # Concatenate and print the String variables on a new line
    print(f'{s}{z}')
    # The 's' variable above should be printed first.
