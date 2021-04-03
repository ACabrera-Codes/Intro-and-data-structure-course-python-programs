def main():
    print('This program tests if the sequence of positive numbers you input are unique')
    print (" ")
    print('Enter -1 to quit')
    print (" ")
    firstNum = int(input("Enter the first number : "))
    numbers = []
    s = set()
    while firstNum!=-1:
        numbers.append(firstNum)
        s.add(firstNum)
        firstNum = int(input("Next : "))
    if len(s) != len(numbers):
        print("The sequence {} is NOT unique.".format(numbers))
    else:
        print("The sequence {} is unique.".format(numbers))
main()

