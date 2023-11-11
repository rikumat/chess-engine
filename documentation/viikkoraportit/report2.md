# Week 2

## Weekly progress
As a change to the initial plan, legal moves and chess rules will be implemented with a python module, python-chess. This allows me to focus on building the minimax algorithm, and improving heuristics and efficiency.

This week i created the game loop in index.py file, Engine class which keeps the state of the game, and Ai class, which is responsible for generating moves. I created alpha-beta pruning algorithm, and initial heuristics, which evaluates a game state only by the balance of material.

## Unclear and troubling things
One bug i noticed is playing a normal opening e2e4, to which the Ai responds with a reasonable g8f6. However, after move a2a3 the Ai doesn't capture the free pawn at e4, instead moving h8e8. The Ai can defend relatively well, and was able to win material upto +20 against chess.com's emir. However, in the end the Ai doesn't do anything, resulting in an eventual draw. My suspicion is that it doesn't see improvement in state in the move limit, thus selecting the last move in the tree. This, however, doesn't explain the bug mentioned earlier.


## Next steps
Next step is to improve heuristics for move generation. The plan is to include the following heuristics in the evaluation process:
- piece development
- pawn structure
- controlled squares
- weak squares

### Hours used: 10

