import constants
from scripting.action import Action
from shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)
        self._points = 0

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
            for i in range(1):
                snake = cast.get_first_actor("snakes")
                snake.grow_tail(i + 1)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
            for i in range(1):
                snake = cast.get_first_actor("snakes")
                snake.grow_tail(i + 1)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
            for i in range(1):
                snake = cast.get_first_actor("snakes")
                snake.grow_tail(i + 1)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
            for i in range(1):
                snake = cast.get_first_actor("snakes")
                snake.grow_tail(i + 1)
                
        # Other command
        if self._keyboard_service.is_key_down('j'):
            self._directions = Point(-constants.CELL_SIZE, 0)
            for i in range(1):
                snake2 = cast.get_first_actor("foods")
                snake2.grow_tail(i + 1)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._directions = Point(constants.CELL_SIZE, 0)
            for i in range(1):
                snake2 = cast.get_first_actor("foods")
                snake2.grow_tail(i + 1)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._directions = Point(0, -constants.CELL_SIZE)
            for i in range(1):
                snake2 = cast.get_first_actor("foods")
                snake2.grow_tail(i + 1)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._directions = Point(0, constants.CELL_SIZE) 
            for i in range(1):
                snake2 = cast.get_first_actor("foods")
                snake2.grow_tail(i + 1)    
                
        
        snake = cast.get_first_actor("snakes")
        snake.turn_head(self._direction)
        
        snake2 = cast.get_first_actor("foods")
        snake2.turn_head(self._directions)