# Week 6

## Weekly progress
Significant improvements in intelligence and gamesense of the Ai. Implemented iterative deepening and dynamic depth calculation. Added transposition table that caches moves during one move calculation. created first drafts of multiplier matrices for each piece. Improved piece development, openings and early game.


## Unclear and troubling things
Should i start focusing on user experience or keep improving heuristics?


## Next steps
Transition from multiplying piece values to adding fixed amount of points depending on locations. This way it is much easier to adjust relative values. Detect if checkmate exists before starting move calculation. This can be done by calling alphabeta with depth 2 on current game state. If returned value is ending value, the color who the alphabeta was called on has been checkmated.

### Hours used: 10
