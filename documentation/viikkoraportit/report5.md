# Week 5

## Weekly progress
Significant improvements in both memory- and computation-efficiency. This week i integrated custom move generator with my Ai, removed looping in evaluation function, and transitioned from copying previous game state to undoing changes after recursive call. I added move ordering (order by eating most valuable piece first). Now it is feasible to calculate 7 moves forward (10-15 seconds) as opposed to last week's 5.

## Unclear and troubling things
What should happen when the Ai notices it's losing in mate in 7? How is the best move selected when all moves result in a checkmate?

***does always preferring mate in least moves fix this problem automatically?*** If the winning party always prefers mate in least moves, wouldn't the losing party always choose mate in most moves as a side effect? This would result in making illegal move only when checkmate has already occured.

How can i gain slightly efficiency to make the game comfortable with depth 7 minimax?

## Next steps
The next step is to consider endgames. Ensure the game ends without a crash, based on the earlier problem. After this, allow castling and pawn promotion initialy to queen only. Finally, consider improvements to user experience.

### Hours used: 10
