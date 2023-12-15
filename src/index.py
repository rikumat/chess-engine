from services.engine import Engine
from services.ai import Ai
from services.move_generator import MoveGenerator

move_generator = MoveGenerator()
ai = Ai(move_generator)
chess_engine = Engine(ai, move_generator)

chess_engine.run()
