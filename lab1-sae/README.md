# Lab - The Silver Dollar Game 

## Learning Goals

* Practice some of your new Java programming skills.
* Play with using the `ArrayList` class.
* Gain experience testing for errors and writing code that handles edge cases.

## Key Terms and Concepts
* `ArrayList` - An ArrayList is a resizable array-like data structure, where items can be added and removed regardless of the initialized size (See 1.3 pg. 136 in the textbook and the lecture notes). In this lab, we will use the default java.util.ArrayList class. Please look into its [documentation](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html) for more details about its methods.
* Edge cases - A possible scenario of user input which requires a specific or non-standard response from the code, such as a user clicking out of bounds or attempting an illegal move.


## Silver Dollar Game

Clone and import this project as you did with the introductory lab. Your program for lab today is to write a text-based version of the Silver Dollar Game. You are a given a strip of coins and your objective is to move all the coins to the left side. Coins can be moved multiple squares at a time, and only to the left. Coins cannot "jump" over each other, nor can they occupy the same square as another coin. The coins start in random positions along the strip. The game is over when all the coins are next to each other starting in the far left square.

Make sure you understand how the game is played before coding it up! This is a time for discussion in the lab; do not hesitate to ask questions or share
your thoughts with your classmates and the staff.

The behavior, in the console, will look like this:

```
_o____oo_oo_ Next move? 6 4
_oo____o_oo_ Next move? 2 2
Illegal move!
_oo____o_oo_ Next move? 1 1
o_o____o_oo_ Next move?
...
ooooo_______ You win!!
```
The pair of numbers after `Next move?` signifies the starting location of a coin and the number of squares
that the coin is to move to the left. To be consistent with how we do indexing in Java the leftmost square is in location 0, not 1.

For this lab, we have given you a start on the code for the class `TextCoinStrip`. Take some time to understand the code (we promise you’ll be much better off spending 5-10 minutes
looking at the code before doing any coding yourself), then fill in the four missing methods.

1. `toString` which returns the string representation of the strip,
2. `isLegalMove` which determines if a move is legal,
3. `makeMove` which makes a (legal) move, and
4. `gameIsOver` which determines if the game is completed.

Note that the program will not execute at all until `gameIsOver` compiles successfully.
We suggest that you change it to return `false` until you get the other functions working.

## Hints/Advice

* Develop incrementally.  Write one method and test that it works by writing static test methods (either in the class or in a separate class).  Make sure that method is working as you expect before moving on to the next method.  To get in good habits, you should also be pushing your changes to github once you have one method working.
* Think about all of the possible ways that your methods could be called and make sure that you are handling all of the cases appropriately.  One of the goals of this class is to get used to testing your own code in more realistic settings, i.e., where the inputs might not always be "proper" inputs.
* There are many constraints on whether or not a move (starting point and distance) is
legal.  You should think about these and enumerate them (in the pre-method comment) before
trying to write the code for the `isLegalMove` method.


## Submitting your work

Make sure that you change the `@author` comment at the start of each file to include your own name.

Although we will not get into the details of Github in this lab, it is important to know that you have on your side a powerful tool that keep track of your work along the way and save you from a lot of trouble.

Every time you feel that you have completed a substantial or logical part of your program, you should consider committing and pushing your work. This will also allow us to monitor your progress. **AVOID** one big push at the end of your work. For example, after writing the `toString` method in this lab you might want to commit your work. 

Write a meaningful message. For example, since I returned default values for the methods you have to fill so that VS Code would stop complaining:

Go to the Source Control icon on left, click + for all the files you want to commit and push.
Then click the expand arrow to the right of the Commit button. Choose `Commit and Push`.


<!-- Right click on the repository and then click `Commit`. -->

![Commit](images/commit_vscode.png "Commit")

<!-- Transfer all your files from `Unstaged Changes` to `Staged Changes`. If you don't see options for `Unstaged Changes` and `Staged Changes`, click `Open Git Staging View` in the bottom left-hand corner. -->



<!-- ![Push](images/push.png "Push") -->

<!-- Click `Commit and Push` -->

Want to confirm that we can see your work? Go to the URL that you were given. You can see the latest commit you pushed. Submitting correctly is your responsibility! Make sure you commit and push regularly so that we can see your progress and you avoid losing your work. 

**Important:** The last commit you push by the due date is the one we will look at and grade.

## Grading

This lab will directly lead into the assignment, so we'd strongly encourage you to complete the lab.  For grading purposes, you need to:

1. Participate in lab discussions.
2. Get checked off by TA or Professor.
3. Push code by the end of lab (or end of the day) that compiles and is close to completion.

