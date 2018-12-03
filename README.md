# turner townsend technical assessment

welcome to the turner & townsend technical assessment. thank you so much for your interest in joining our team and for taking the time to apply to this role. the purpose of this assessment is for us to get a good idea of how you approach solving problems. the next stage after submitting a solution is for you to pair with us on extending it in some way.

the purpose of this is not to trick you or catch you out. although the problems are often deliberately ambiguous, we are much more interested in how you arrive at a solution rather than the solution itself.

please make yourself comfortable before attempting any of these. there is no time limit, although if you find yourself spending more than a couple of hours on these, you might be taking the solution too far. we value your time and don't want to waste it.

the problems are divided on complexity, from low to spicy. please choose a problem which you feel you will have time to properly solve and which gives most opportunity to demonstrate your programming skills. consider the seniority of the role in the decision of which problem to tackle.

at turner & townsend, we prefer solutions which are explicit over implicit, discoverable over performant, and which are correctly tested given their size. all of these require python as it is the language we use most often here.

to submit a solution, fork this repository and push your solution there. we will try to get back to you with feedback as soon as possible.

thanks!

## the collatz conjecture - low

the collatz, or 3n + 1 conjecture, is a mathematical sequence defined as follows:

* start with a number, n
* if n is even:
  * produce n / 2
* otherwise, n is odd:
  * produce 3 * n + 1
* repeat until n is 1

write a python program which takes a numeric input and shows how many steps it takes until the collatz sequence reaches 1.

## roman numerals - medium

roman numerals are a sequence of characters used for counting, and for recording what number sequel a movie is. valid roman numerals are:

| numeral | value |
| ------- | ----- |
| I | 1    |
| V | 5    |
| X | 10   |
| C | 100  |
| M | 1000 |

roman numerals are written by expressing each digit separately starting with the left most digit:

```
X = 10
VI = 5 + 1 = 6
MXVII = 1000 + 10 + 5 + 1 + 1 = 1017
```

there are some other rules around roman numerals which we don't currently care about.

write a python program which takes a series of roman numerals as input and which outputs their value as a number.

## stack - spicy 🌶

fifth is a new stack-based language. a stack is a data structure which can only have elements added to the top. fifth stores a stack of integers and supports commands to manipulate that stack. operations always apply to the top of the stack.

fifth supports the following arithmetic operators:

```
+ - * /
```

each of these applies the operator to the two values on the top of the stack and pushes the result to the top of the stack. if division results in a non-integer, round down.

fifth also supports the following commands:

* `PUSH x` - push x onto the top of the stack, where x is a valid integer
* `POP` - remove the top element of the stack
* `SWAP` - swap the top two elements of the stack
* `DUP` - duplicate the top element of the stack

write a python program which works as a fifth interpreter. each line of input to the program should represent a single fifth command. output the result of each command to the terminal. handle errors sensibly.

example:
```
stack is []
PUSH 3
stack is [3]
PUSH 11
stack is [3, 11]
+
stack is [14]
DUP
stack is [14, 14]
PUSH 2
stack is [14, 14, 2]
*
stack is [14, 28]
SWAP
stack is [28, 14]
/
stack is [2]
+
ERROR
```
