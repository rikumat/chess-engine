# Week 1

## Weekly progress
This week my main focus was fixing the main problem of the previous build - always losing by repetition. Last week the only heuristic the bot used was material balance. This week, i added a new heuristic, which gives more points the closer the player's pieces are to the opponents king. This forces the Ai to attack the king.

## Unclear and troubling things
Perhaps the most troublesome thing as of yet is how to store legal moves such that they can be removed efficiently when they are no longer legal. The initial plan for keeping track of legal moves is to start with initial state (pawns and knights can move) and update them every time a piece is moved for all affected pieces.

## Next steps
The next step in the project is to create the ability to keep track of legal moves when the game progresses. After this, initial heuristic function will be created to calculate how favorable a position is for the player. Then, minimax algorithm will be implemented. Finally, the focus will be moved to improving the heuristic function.

### Hours used: 3
