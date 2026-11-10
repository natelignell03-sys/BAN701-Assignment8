# Basketball Score Tracker

## Project Description
This Python program tracks basketball game scores
and calculates the average points scored.

## Initial Version
The initial program allows users to enter scores
from multiple games, stores those scores in a list,
and calculates the average score.

## Feature Development Comparison
For Assignment 9, I used my existing Basketball Score Tracker program to add new features using two different development approaches. The goal was to compare the process of implementing a feature manually versus using generative AI.

On the manual-feature branch, I added a feature that displays the highest basketball score entered. This feature uses Python's max() function to identify the highest value from the list of scores. The feature was simple to integrate because the program already stored scores in a list. I tested the program with multiple scores to verify the correct result appeared.

On the ai-feature branch, I used generative AI to add a feature that displays the lowest basketball score and calculates the difference between the highest and lowest scores. AI suggested using the min() and max() functions, which worked with the existing program.

The AI-generated code worked on the first attempt. I was able to enter the code that AI generated at the end of my already published code, tested it, and it worked with no problems. When first trying to merge the code in GitHub, there was an error saying that it was not able to be performed, but after modifying the code, it worked with no problems.

I felt more confident adding the code myself because I was able to make it simple, which then led to a simple outcome. With the AI version, there were some changes that had to be made because there was more code. But after making the necessary changes, the AI code worked. This assignment helped me understand the importance of testing, reviewing code, and managing different branches in GitHub.
