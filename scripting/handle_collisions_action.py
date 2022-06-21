import constants
from casting.actor import Actor
from scripting.action import Action
from shared.point import Point
from casting.game_over_message import GameOver

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            #self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    # def _handle_food_collision(self, cast):
    #     """Updates the score nd moves the food if the snake collides with the food.
        
    #     Args:
    #         cast (Cast): The cast of Actors in the game.
    #     """
    #     score = cast.get_first_actor("scores")
    #     food = cast.get_first_actor("foods")
    #     snake = cast.get_first_actor("snakes")
    #     head = snake.get_head()

    #     if head.get_position().equals(food.get_position()):
    #         points = food.get_points()
    #         snake.grow_tail(points)
    #         score.add_points(points)
    #         food.reset()
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle = cast.get_first_actor("cycle_one")
        head = cycle.get_segments()[0]
        segments_one = cycle.get_segments()[1:]
        
        cycle2 = cast.get_first_actor("cycle_two")
        head2 = cycle2.get_segments()[0]
        segments_two = cycle2.get_segments()[1:]
        
        for segment in segments_one:
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True

        for seg in segments_two:        
            if head.get_position().equals(seg.get_position()):  
                self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns both cycles white if the game is over.

        Args:
        ---
            cast (Cast): The cast of Actors in the game.
        """

        # Gets position for gameover message
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        position = Point(x, y)

        if self._is_game_over:
            cycle_one = cast.get_first_actor("cycle_one")
            cycle_two = cast.get_first_actor("cycle_two")
            
            # Gets segments for cycle one and two
            segments_one = cycle_one.get_segments()
            segments_two = cycle_two.get_segments()
            
            # Creates gameover message
            game_over = GameOver()
            game_over.set_position(position)
            game_over.set_text(self._game_over_message)
            game_over.set_font_size(50)
            cast.add_actor("messages", game_over)

            # Changes color of cycles to white after the game ends
            for segment in segments_one:
                segment.set_color(constants.WHITE)

            for segment in segments_two:
                segment.set_color(constants.WHITE)