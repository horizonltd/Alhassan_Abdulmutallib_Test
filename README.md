# TECHNICAL PROJECT REQUIREMENTS


Question A
Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
 
Question B
The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.
 
Question C
At Ormuco, we want to optimize every bits of software we write. Your goal is to write a new
library that can be integrated to the Ormuco stack. Dealing with network issues everyday, latency is our biggest problem. Thus, your challenge is to write a new Geo Distributed LRU (Least Recently Used) cache with time expiration. This library will be used extensively by many of our services so it needs to meet the following criteria


## SOLUTION

The Project was handled using python programming language

1. First Question was solved using simple functions (Method), using intercepter algorithms. 
2. While Question two was handled using if else statement.
3. Question Three was mainly a library which uses LRU Cache for a recursive execution of the script
   
   a. The solution simulated  normal network environment, whereby a lot of nods are connected to a network server
        either locally, or remotely. The solution determined the latency and number of nods in each network

## How to run the programs

1. Question A and B can be executed with their normal python file in the respective solution folders.
2. While Question C has two modules which are dependant of each other, to test the flow of the program,
    mainProgram.py should be run either using terminal or any IDE like VSCODE.

#### Note: While testing Question C, the project folder most be imported separately in any IDE, unlike the A and B questions,

    that to say:
        Question C folder only.



