import random
from typing import Optional

from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction
from ..util import get_closest_diamond_position
from ..util import get_closest_diamond

from ..util import get_rank
from ..util import get_time_left
from ..util import get_closest_blue_diamond_position
from ..util import get_time_to_location
from ..util import check_if_should_go_for_diamond_button
from ..util import get_diamond_button
from ..util import am_i_in_danger
from ..util import find_diamond_mine


class Greedy(BaseLogic):
    def __init__(self):
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # Optional[Position] is a way to say that the value can be None
        self.goal_position: Optional[Position] = None
        self.current_direction = 0

    def next_move(self, board_bot: GameObject, board: Board):
        # store all robot objects
        other_robots = board.bots
        # store all diamond objects
        diamonds = board.diamonds
        # store the properties of our bot
        props = board_bot.properties

        print(
            "waktu ke lokasi",
            get_time_to_location(board_bot.position, board_bot.properties.base),
        )
        print("waktu sisa", get_time_left(board.game_objects))
        print(
            "total",
            abs(
                get_time_to_location(board_bot.position, board_bot.properties.base)
                - get_time_left(board.game_objects)
            ),
        )
        print(
            "moiney money money: ",
            find_diamond_mine(diamonds, board_bot.position),
        )

        # Check if inventory is empty and if diamond button is closer than the closest diamond
        if props.diamonds == 0:
            if check_if_should_go_for_diamond_button(
                board_bot, board.game_objects, diamonds
            ):
                print("Finishing")
                # Go to diamond button to reset board so that enemies who are close to their base will have to change direction because their base changed
                self.goal_position = get_diamond_button(board.game_objects).position
            else:
                self.goal_position = find_diamond_mine(diamonds, board_bot.position)

        elif (
            # Check if the inventory is full or there is not enough time to get back to the base. We do this so that in the last seconds, if our bot carries some diamonds and still looking for the closest diamond but dont have enough time to take those diamonds back to the base, it will go straigth to the base
            props.diamonds >= 5
            or (
                props.diamonds > 0
                and (
                    abs(
                        get_time_to_location(
                            board_bot.position, board_bot.properties.base
                        )
                        - get_time_left(board.game_objects)
                    )
                    <= 2000
                )
            )
        ):
            print("Play it safe")
            # Move to base
            base = board_bot.properties.base
            self.goal_position = base
        elif (
            # Check if the closest diamond is red diamond and our bot carries 4 diamonds already
            get_closest_diamond(board_bot.position, diamonds).properties.points == 2
            and props.diamonds == 4
        ):
            print("Going for blue diamond")
            # It will go to the closest blue diamond to fill the inventory
            self.goal_position = get_closest_blue_diamond_position(
                board_bot.position, diamonds
            )

        else:
            print("Going for the closest diamond")
            # Go to the closest diamond
            self.goal_position = get_closest_diamond_position(
                board_bot.position, diamonds
            )
        # store the current position of our robot
        current_position = board_bot.position

        # if goal position exists, calculate the direction to go to the goal position
        if self.goal_position:
            # We are aiming for a specific position, calculate delta
            delta_x, delta_y = get_direction(
                current_position.x,
                current_position.y,
                self.goal_position.x,
                self.goal_position.y,
                board,
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
        print("goal", self.goal_position)
        return delta_x, delta_y
