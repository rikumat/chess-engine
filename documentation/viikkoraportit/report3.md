# Week 1

## Weekly progress
This week my main focus was fixing the main problem of the previous build - always losing by repetition. Last week the only heuristic the bot used was material balance. Consequently, if the bot didn't see an assured advantage in material within the next 5 moves, it considered all moves equally good. This caused it to move a rook back and forth until the game ends in a draw by repetition, or the opponent manages to win the game.

This week, i added a new heuristic, which gives more points the closer the player's pieces are to the opponents king. This forces the Ai to develop its pieces.

## Unclear and troubling things
Prevailing problem with the build is that the Ai looks forward x moves and values the position by material advantage and piece development. However, if this sequence ends in a state where the Ai's queen is threatened by a less valued piece, it doesn't affect the evaluation, because it is only seen on the sixth move. This causes occasional blunders.

## Next steps
The next step in the project is to create the ability to keep track of legal moves when the game progresses. After this, initial heuristic function will be created to calculate how favorable a position is for the player. Then, minimax algorithm will be implemented. Finally, the focus will be moved to improving the heuristic function.

### Hours used: 3
