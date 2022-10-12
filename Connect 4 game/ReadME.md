# Connect-4
Connect 4 is a token game created with Python and module Numpy. 

## What is connect 4?
It is a two-player connection game in which the players first choose a color and then take turns dropping one colored disc from the top into a seven-column, six-row vertically suspended grid. The pieces fall straight down, occupying the lowest available space within the column, user wins by forming row of four of same color

## How to play:
Place 4 tokens in a row (vertically, horizontally, or diagonally) before your opponent wins. <br>Single-player against Artificial Intelligence.

The game will be playable in the iPython console.<br>
The flow of the game is as follows:
- Make the player select a colour of the token.
- Create a (m x n) matrix and ask the user where he/she wants to enter the token. 
- Next make the computer select a position for the opposition token.
- After every turn check the matrix for consecutive 4 tokens of the same colour either vertically, horizontally or diagonally and if found declare the winner.

In the below example, notice how player 1 won by connecting 4 diagonal pieces!

![player 1 victory](https://i.gyazo.com/45d2f1ab497c285dd75a2491377eb564.png)