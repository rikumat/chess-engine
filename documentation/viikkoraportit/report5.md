# Week 1

## Weekly progress
This week I created the initial github-project, and planned how the project will be implemented. I studied minimax-algorithm and alpha-beta pruning by watching videos on youtube. I also watched an instructional video about how to create a chess engine in python. I created a plan for how legal moves will be calculated (moves updated after every move).

## Unclear and troubling things
Perhaps the most troublesome thing as of yet is how to store legal moves such that they can be removed efficiently when they are no longer legal. The initial plan for keeping track of legal moves is to start with initial state (pawns and knights can move) and update them every time a piece is moved for all affected pieces.

## Next steps
The next step in the project is to create the ability to keep track of legal moves when the game progresses. After this, initial heuristic function will be created to calculate how favorable a position is for the player. Then, minimax algorithm will be implemented. Finally, the focus will be moved to improving the heuristic function.

### Hours used: 3
