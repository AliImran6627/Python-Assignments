# Input and Setup

Starting off, we prompt the user to enter their name as well as any 3 numbers of their choice using the **input** method. We store the numbers in 3 seperate variables and we store these variables in a list.

# Even/Odd Check

Next up, we make a list in which we will store tuples. We use a for loop to loop through our initial number list, using conditions to check if the numbers are even or odd *(divide by 2 and check remainder)* and storing them in our list of tuples *(using append method)* with a string mentioning if they're even or odd.

# Finding squares

We then create another list of tuples and use a for loop to loop through our previous list of tuples, squaring the numbers, storing them in the new list of tuples, and finally printing them by, again, using a for loop to loop through our latest list of squared tuples.

# Sum of Numbers

We create a variable and using the **sum()** method to simply add the numbers in our first number list, and then we print the sum.

# Prime Number Check

In order to check if the sum of numbers was a prime number, we first create a boolean variable and set it to True. We use an if statement to make sure that the sum is greater than 1 *(since 1 is not classified as a prime number)*, then we run a for loop starting from 2 and just before the number itself *(using range)*. We check if the sum is completely divisible by any number other than itself *(using modulus remainder)*, if it is, we set our initial boolean variable to False and break the loop. Otherwise it remains True. Outside the loop, we check if the boolean is True or False, and we print the status of the sum *(if it is a prime number or not)*.
