# Chess Engine

## Overview
Chess engine written in python. This engine will have a commandline interface, where the player can input a move, and the engine will print a move in response. To calculate moves, minimax algorithm and alpha-beta pruning will be used.

## Usage
This project uses poetry. You need to have poetry installed in order to run the tests. However, you can still play the game by running the index.py file in the src directory without poetry.
Once you have installed poetry, use the following commands to play the game:

To install dependencies, run the following command in the project's root folder:
~~~
poetry install
~~~

To run the game, run the following command:
~~~
poetry run invoke start
~~~

To run tests for the project, run the following command:
~~~
poetry run invoke test
~~~
For instructios on how to play the game, see [Manual](./documentation/manual.md)

### [Weekly reports](./documentation/viikkoraportit)

![example workflow](https://github.com/rikumat/chess-engine/workflows/CI/badge.svg)

[![codecov](https://codecov.io/gh/rikumat/chess-engine/graph/badge.svg?token=79OMT6GWXF)](https://codecov.io/gh/rikumat/chess-engine)

