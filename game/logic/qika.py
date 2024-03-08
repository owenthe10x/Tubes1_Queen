import math
from game.models import Board, GameObject
from ..util import clamp


def get_direction(current_x, current_y, dest_x, dest_y):
    delta_x = clamp(dest_x - current_x, -1, 1)
    delta_y = clamp(dest_y - current_y, -1, 1)
    if delta_x != 0:
        delta_y = 0
    return (delta_x, delta_y)


class Heuristik(object):
    def __init__(self):
        self.goal_position = None
        self.previous_position = (None, None)
        self.turn_direction = 1

    def next_move(self, board_bot: GameObject, board: Board):
        props = board_bot.properties

        teleporter = [
            obj for obj in board.game_objects if obj.type == "TeleportGameObject"
        ]

        if props.diamonds == 5:
            base = props.base
            self.goal_position = base

        else:
            max_score = -1
            target = None
            for diamond in board.diamonds:
                if board_bot.properties.diamonds + diamond.properties.points > 5:
                    continue
                xDist = abs(board_bot.position.x - diamond.position.x)
                yDist = abs(board_bot.position.y - diamond.position.y)
                distance = math.sqrt(xDist * xDist + yDist * yDist)
                score = diamond.properties.points / distance

                if score > max_score:
                    max_score = score
                    target = diamond

            for other_bot in board.bots:
                if other_bot.id == board_bot.id:
                    continue

                xDist = abs(board_bot.position.x - other_bot.position.x)
                yDist = abs(board_bot.position.y - other_bot.position.y)
                distance = math.sqrt(xDist * xDist + yDist * yDist)
                score = other_bot.properties.diamonds / distance

                if other_bot.properties.diamonds > board_bot.properties.diamonds:
                    score = -score

                if score > max_score:
                    max_score = score
                    target = other_bot

            if target is not None:
                self.goal_position = target.position

        if self.goal_position:
            current_position = board_bot.position
            cur_x = current_position.x
            cur_y = current_position.y
            delta_x, delta_y = get_direction(
                cur_x,
                cur_y,
                self.goal_position.x,
                self.goal_position.y,
            )

            if (cur_x, cur_y) == self.previous_position:
                if delta_x != 0:
                    delta_y = delta_x * self.turn_direction
                    delta_x = 0
                elif delta_y != 0:
                    delta_x = delta_y * self.turn_direction
                    delta_y = 0
                self.turn_direction = -self.turn_direction

            self.previous_position = (cur_x, cur_y)
            return delta_x, delta_y

        return 0, 0
