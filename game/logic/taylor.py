import random
from typing import Optional

from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction
from ..util import get_closest_diamond_position
from ..util import get_closest_diamond

from ..util import get_rank
from ..util import get_time_left
from ..util import get_second_closest_diamond_position


class Taylor(BaseLogic):
    def __init__(self):
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # Optional[Position] is a way to say that the value can be None
        self.goal_position: Optional[Position] = None
        self.current_direction = 0
        self.mode = "safe"

    def next_move(self, board_bot: GameObject, board: Board):
        other_robots = board.bots
        diamonds = board.diamonds
        props = board_bot.properties
        print("waktu", get_time_left(board.game_objects))

        # Check if we need to play safe by checking diamonds in inventory
        if props.diamonds >= 4:
            self.mode = "safe"
        else:
            self.mode = "normal"

        # Check if inventory is full
        if props.diamonds >= 4:
            # Move to base
            base = board_bot.properties.base
            self.goal_position = base
        elif (
            get_closest_diamond(board_bot.position, diamonds).properties.points == 2
            and props.diamonds >= 4
        ):
            self.goal_position = get_second_closest_diamond_position(
                board_bot.position, diamonds
            )
        else:
            self.goal_position = get_closest_diamond_position(board_bot.position, diamonds)

        current_position = board_bot.position
        if self.goal_position:
            # We are aiming for a specific position, calculate delta
            delta_x, delta_y = get_direction(
                current_position.x,
                current_position.y,
                self.goal_position.x,
                self.goal_position.y,
            )
        else:
            # Roam around
            delta = self.directions[self.current_direction]
            delta_x = delta[0]
            delta_y = delta[1]
            if random.random() > 0.6:
                self.current_direction = (self.current_direction + 1) % len(
                    self.directions
                )
        print(f"delta_x: {delta_x}, delta_y: {delta_y}")
        return delta_x, delta_y