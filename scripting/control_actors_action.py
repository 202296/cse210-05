
import constants
from scripting.action import Action
from shared.point import Point
from scripting.handle_collisions_action import HandleCollisionsAction


class ControlActorsAction(Action):
    """
    An input action that controls the cycle.
    
    The responsibility of ControlActorsAction is to get the direction and move the cycle's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._cycle_one_direction = Point(0, -constants.CELL_SIZE)
        self._cycle_two_direction = Point(0, -constants.CELL_SIZE)
        self._is_game_over = True

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
        ---
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        # Cycle one keyboard Inputs
        self.cycle_one = cast.get_first_actor("cycle_one")
        self.cycle_one.turn_cycle(self._cycle_one_direction)

        # left
        if self._keyboard_service.is_key_down('a'):
            self._cycle_one_direction = Point(-constants.CELL_SIZE, 0)            
            self.cycle_one.grow_tail(1)

        # right
        if self._keyboard_service.is_key_down('d'):
            self._cycle_one_direction = Point(constants.CELL_SIZE, 0)            
            self.cycle_one.grow_tail(1)

        # up
        if self._keyboard_service.is_key_down('w'):
            self._cycle_one_direction = Point(0, -constants.CELL_SIZE)            
            self.cycle_one.grow_tail(1)

        # down
        if self._keyboard_service.is_key_down('s'):
            self._cycle_one_direction = Point(0, constants.CELL_SIZE)            
            self.cycle_one.grow_tail(1)        

        # Cycle two keyboard Inputs
        self.cycle_two = cast.get_first_actor("cycle_two")
        self.cycle_two.turn_cycle(self._cycle_two_direction)
        
        # left
        if self._keyboard_service.is_key_down('j'):
            self._cycle_two_direction = Point(-constants.CELL_SIZE, 0)            
            self.cycle_two.grow_tail(1)
        # right
        if self._keyboard_service.is_key_down('l'):
            self._cycle_two_direction = Point(constants.CELL_SIZE, 0)            
            self.cycle_two.grow_tail(1)
        # up
        if self._keyboard_service.is_key_down('i'):
            self._cycle_two_direction = Point(0, -constants.CELL_SIZE)            
            self.cycle_two.grow_tail(1)
        # down
        if self._keyboard_service.is_key_down('k'):
            self._cycle_two_direction = Point(0, constants.CELL_SIZE)            
            self.cycle_two.grow_tail(1)

        