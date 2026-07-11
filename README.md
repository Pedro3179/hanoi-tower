# Tower of Hanoi Algorithm

This project solves the mathematical puzzle known as the *Tower of Hanoi*. The algorithm takes a number as input and generates a list sorted in descending order. The goal is then to move these numbers to the rightmost list (or rod).

This is part of the *certification project* and one of the requirements for earning the *Python Certification*. The lab project is called "Implement the Tower of Hanoi Algorithm."

---

## What I learned

1. How to solve algorithmic challenges
2. How to work with recursion
3. Break problems down into smaller challenges and solve them one step at a time
4. How to write clear comments for each part of the script
5. How to write readable code
6. Anticipate edge cases that could cause the program to crash and handle them

Below are the instructions to pass the lab.

---

## Implement the Tower of Hanoi Algorithm

In this lab, you will solve the mathematical puzzle known as the *Tower of Hanoi*.
The puzzle consists of three rods and a number of disks of different diameters.

The puzzle starts with the disks piled up on the first rod, in decreasing size, with the smallest disk on top and the largest disk on the bottom.

The goal of the *Tower of Hanoi* puzzle is moving all the disks to the last rod. To do that, you must follow three simple rules:

1. You can move only top-most disks.
2. You can move only one disk at a time.
3. You cannot place larger disks on top of smaller ones.
**Objective**: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

1. You should have a function named hanoi_solver that takes an integer representing the total number of disks of the puzzle as the argument.
2. The hanoi_solver function should solve the puzzle following the given rules in 2n - 1 moves, where n is the total number of disks.
3. The hanoi_solver function should return a string with all the moves taken to solve the puzzle, including the starting arrangement, with each move on a new line. Rods should be represented as lists of integers, (the smallest disk is represented by the number 1) with each rod separated by a space. 
