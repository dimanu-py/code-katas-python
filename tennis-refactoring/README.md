# Resources

These requirements and the initial state of the code are extracted from the original GitHub repository

[![Web](https://img.shields.io/badge/GitHub-emilybache-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/emilybache/Tennis-Refactoring-Kata/tree/main)

# 🎾 Tennis Refactoring Kata 🎾

## Description

Imagine you work for a consultancy company, and one of your colleagues has been doing some work for the Tennis Society. The contract is for 
10 hours billable work, and your colleague has spent 8.5 hours working on it. Unfortunately he has now fallen ill. He says he has completed 
the work, and the tests all pass. Your boss has asked you to take over from him. She wants you to spend an hour or so on the code, so she can
bill the client for the full 10 hours. She instructs you to tidy up the code a little and perhaps make some notes, so you can give your 
colleague some feedback on his chosen design. You should also prepare to talk to your boss about the value of this refactoring work, over 
and above the extra billable hours.

> [!NOTE]
> There are several versions of this refactoring kata, each with their own design smells and challenges. The recommended entry point is the
> tennis 1 file.

To understand the logic of the code you may need to know how the tennis scoring system works. Here is a quick summary:

- A game is won by the first player to have won at least four points in total and at least two points more than the opponent.
- Scores from zero to three points are described as "Love", "Fifteen", "Thirty", and "Forty" respectively.
- If at least three points have been scored by each player, and the scores are equal, the score is "Deuce".
- If the players are in "Deuce" situation and a player wins a point, the score of the game is "Advantage" for the player in the lead.

## Objective

The main objective of this kata is to refactor the code to make it more readable and maintainable. The code should be easy to understand and
extend.

We will be focused on baby steps refactor and code smells.
