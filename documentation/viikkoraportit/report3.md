# Week 3

## Weekly progress
This week my main focus was fixing the main problem of the previous build - always losing by repetition. Last week the only heuristic the bot used was material balance. Consequently, if the bot didn't see an assured advantage in material within the next 5 moves, it considered all moves equally good. This caused it to move a rook back and forth until the game ends in a draw by repetition, or the opponent manages to win the game.

This week, i added a new heuristic, which gives more points the closer the player's pieces are to the opponents king. This forces the Ai to develop its pieces. I attempted removing the for loop from the evaluation function by saving the material balance in a dictionary which was passed as an argument in the alphabeta method (with move a2b3 add the value of the piece in b3 to the material balance), but this didn't work properly. Consequently, i reverted the project back to the previous version. Had this worked, it would have improved efficiency greatly, since dict access and assignment is O(1) time. This will be reattempted in the future.

## Unclear and troubling things
Prevailing problem with the build is that the Ai looks forward x moves and values the position by material advantage and piece development. However, if this sequence ends in a state where the Ai's queen is threatened by a less valued piece, it doesn't affect the evaluation, because it's effect is only seen on the x+1 move. This causes occasional blunders.

**Will i lose signinificantly performance if in the alphabeta function i go through each piece and calculate legal moves for that piece from a 2-dimensional list that represents the chessboard? My idea is to go through each existing piece, calculate legal moves (methods in Board class), and iterate through those moves recursively.**

## Next steps
The highest priority task for next week is transferring board functionality to a custom class (Board), and pruning the python-chess dependency. After this is done, tested and ensured to work properly, the focus will be moved to improving the heuristic function. The next step to improve the heuristics is to add value to threats.

### Hours used: 7
