import constants

from casting.cast import Cast
from casting.score import Score
from casting.cycle import Cycle
from scripting.script import Script
from scripting.control_actors_action import ControlActorsAction
from scripting.move_actors_action import MoveActorsAction
from scripting.handle_collisions_action import HandleCollisionsAction
from scripting.draw_actors_action import DrawActorsAction
from directing.director import Director
from services.keyboard_service import KeyboardService
from services.video_service import VideoService
from shared.color import Color
from shared.point import Point


def main():
    
      # Creates two cycles, gets their position and color
    cycle_one = Cycle(Point(int(constants.MAX_X - 600), int(constants.MAX_Y / 2)))
    cycle_two = Cycle(Point(int(constants.MAX_X - 300), int(constants.MAX_Y / 2)))
    cycle_one.set_cycle_color(constants.GREEN)
    cycle_two.set_cycle_color(constants.RED)
    cycle_one_name = "Player 1"
    cycle_two_name = "Player 2"
    cycle_one.set_name(cycle_one_name)
    cycle_two.set_name(cycle_two_name)

    # Create the cast
    cast = Cast()
    score1 = Score()
    score2 = Score()
    score1.set_position(Point(constants.MAX_X - 850, 7))
    score2.set_position(Point(constants.MAX_X - 200, 7))
    score1.add_points(0)
    score2.add_points(0)
    score1.set_player_name(cycle_one_name)
    score2.set_player_name(cycle_two_name)
    cast.add_actor("cycle_one", cycle_one)
    cast.add_actor("cycle_two", cycle_two)
    cast.add_actor("score1", score1)
    cast.add_actor("score2", score2)
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()