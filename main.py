from dragon_core.engine import (
    Engine,
    EngineStore,
    EngineScene,
    InputHandler
)
from dragon_core.scenes import HomeScene

game_scene = EngineScene(HomeScene())
game_store = EngineStore()
game_input_handler = InputHandler()
game_engine = Engine(
    store=game_store,
    scene=game_scene,
    input_handler=game_input_handler
)

game_engine.run()