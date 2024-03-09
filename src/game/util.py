from .models import Position


# Gets Information
def am_i_in_danger(bot, enemies):
    for enemy in enemies:
        if (
            abs(enemy.position.x - bot.position.x)
            + abs(enemy.position.y - bot.position.y)
            <= 2
        ):
            return True
    return False


def is_in_between(point1, point2, point3):
    return point1 <= point2 <= point3  # Check if point2 is between point1 and point3


def get_direction(current_x, current_y, dest_x, dest_y, board):
    teleports = get_teleport_info(board.game_objects)
    diamondButton = get_diamond_button(board.game_objects)
    horizontal = True
    isDestDiaButton = (
        dest_x == diamondButton.position.x and dest_y == diamondButton.position.y
    )

    # Edge case where the bot, the diamond button, and the destination are in the same line on the edge of the board
    if (
        (
            is_in_between(current_x, diamondButton.position.x, dest_x)
            or is_in_between(dest_x, diamondButton.position.x, current_x)
        )
        and current_y == dest_y
        and current_y == diamondButton.position.y
        and not isDestDiaButton
    ):
        print("masuk sini")
        if current_y != board.height - 1:
            return (0, 1)
        else:
            return (0, -1)
    elif (
        (
            is_in_between(current_y, diamondButton.position.y, dest_y)
            or is_in_between(dest_y, diamondButton.position.y, current_y)
        )
        and current_x == dest_x
        and current_x == diamondButton.position.x
        and not isDestDiaButton
    ):
        print("msuk pak eko")
        if current_x != board.width - 1:
            return (1, 0)
        else:
            return (-1, 0)

    # This will avoid any diamond button on the way to the destionation
    if (
        (
            is_in_between(current_y, diamondButton.position.y, dest_y)
            or is_in_between(dest_y, diamondButton.position.y, current_y)
        )
        and (
            dest_x == diamondButton.position.x or current_y == diamondButton.position.y
        )
        and not isDestDiaButton
    ):
        print("anjay pak eko")
        horizontal = False

    for teleport in teleports:
        # Edge case where the bot, the teleport, and the destination are in the same line on the edge of the board
        if (
            (
                is_in_between(current_x, teleport.position.x, dest_x)
                or is_in_between(dest_x, teleport.position.x, current_x)
            )
            and current_y == dest_y
            and current_y == teleport.position.y
        ):
            print("masuk sini")
            if current_y != board.height - 1:
                return (0, 1)
            else:
                return (0, -1)
        elif (
            (
                is_in_between(current_y, teleport.position.y, dest_y)
                or is_in_between(dest_y, teleport.position.y, current_y)
            )
            and current_x == dest_x
            and current_x == teleport.position.x
        ):
            print("msuk pak eko")
            if current_x != board.width - 1:
                return (1, 0)
            else:
                return (-1, 0)

        # This will avoid any teleport on the way to the destionation=
        if (
            is_in_between(current_y, teleport.position.y, dest_y)
            or is_in_between(dest_y, teleport.position.y, current_y)
        ) and (dest_x == teleport.position.x or current_y == teleport.position.y):
            print("kelas pak eko")
            horizontal = False

    delta_x = clamp(dest_x - current_x, -1, 1)
    delta_y = clamp(dest_y - current_y, -1, 1)

    if delta_x != 0 and horizontal:
        delta_y = 0
    elif delta_y != 0 and not horizontal:
        delta_x = 0
    return (delta_x, delta_y)


def get_diamonds_info(game_objects: list):
    return [obj for obj in game_objects if obj.type == "DiamondGameObject"]


def get_teleport_info(game_objects: list):
    return [obj for obj in game_objects if obj.type == "TeleportGameObject"]


def get_time_left(game_objects: list):
    for item in game_objects:
        if item.type == "BotGameObject":
            return item.properties.milliseconds_left


def get_closest_diamond(pos: Position, diamonds: list):
    return min(
        diamonds,
        key=lambda d: abs(d.position.x - pos.x) + abs(d.position.y - pos.y),
    )


def check_if_should_go_for_diamond_button(bot, game_objects, diamond_location):
    return (
        get_time_to_location(
            bot.position, get_closest_diamond_position(bot.position, diamonds)
        )
        - get_time_to_location(bot.position, get_diamond_button(game_objects).position)
        > 5000
    )


# Gets Location
def get_diamond_button(game_objects: list):
    for item in game_objects:
        if item.type == "DiamondButtonGameObject":
            return item


def get_closest_diamond_position(pos: Position, diamonds: list):
    return get_closest_diamond(pos, diamonds).position


def get_closest_blue_diamond_position(pos: Position, diamonds: list):
    return min(
        [d for d in diamonds if d.properties.points == 1],
        key=lambda d: abs(d.position.x - pos.x) + abs(d.position.y - pos.y),
    ).position


def get_closest_bot(pos: Position, bots: list):
    return min(
        bots,
        key=lambda b: abs(b.position.x - pos.x) + abs(b.position.y - pos.y),
    )


def get_closest_bot_to_diamond(diamond_pos: Position, bots: list):
    return min(
        bots,
        key=lambda b: abs(b.position.x - diamond_pos.x)
        + abs(b.position.y - diamond_pos.y),
    )


def get_ranked_robots(bots: list):
    return sorted(bots, key=lambda b: b.properties.diamonds, reverse=True)


def get_rank(bots: list, bot_id: int):
    sorted_bots = sorted(bots, key=lambda b: b.properties.diamonds, reverse=True)
    for i, bot in enumerate(sorted_bots):
        if bot.id == bot_id:
            return i + 1


def get_time_to_location(current: Position, dest: Position):
    return 1000 * (abs(dest.x - current.x) + abs(dest.y - current.y))


# Comparisons
def position_equals(a: Position, b: Position):
    return a.x == b.x and a.y == b.y


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


def killable(my_bot: any, enemies: any, diamonds: any) -> bool:
    # Check if other bot is killable which is in a position where the closest diamond is the same as my bot and the other bot is exactly 1 tile closer to the diamond than our bot
    for enemy in enemies:
        my_bot_closest_diamond = get_closest_diamond_position(my_bot.position, diamonds)
        enemy_closest_diamond = get_closest_diamond_position(enemy.position, diamonds)
        if not position_equals(my_bot_closest_diamond, enemy_closest_diamond):
            continue
        elif (
            get_time_to_location(my_bot.position, my_bot_closest_diamond)
            - get_time_to_location(enemy.position, enemy_closest_diamond)
            == 1000
        ):
            return True
    return False


def suicide(my_bot: any, enemies: any, diamonds: any) -> bool:
    # Check if my bot is in an unsafe position which is in a position where the closest diamond is the same as some bots and my bot is exactly 1 tile closer to the diamond than the other bot
    for enemy in enemies:
        my_bot_closest_diamond = get_closest_diamond_position(my_bot.position, diamonds)
        enemy_closest_diamond = get_closest_diamond_position(enemy.position, diamonds)
        if not position_equals(my_bot_closest_diamond, enemy_closest_diamond):
            continue
        elif (
            get_time_to_location(my_bot.position, enemy_closest_diamond)
            - get_time_to_location(enemy.position, my_bot_closest_diamond)
            == 1000
        ):
            return True
    return False


# 5x5 section yang paling banyak poin bukan diamond karna red diamond lebih worth it
def find_diamond_mine(diamonds: list, bot_position: Position):
    max_tile_diamonds = 0
    section = []
    for y in range(11):
        for x in range(11):
            tile_diamonds = sum(
                diamond.properties.points
                for diamond in diamonds
                if y <= diamond.position.y < y + 5 and x <= diamond.position.x < x + 5
            )
            if tile_diamonds > max_tile_diamonds:
                section = []
                max_tile_diamonds = tile_diamonds
                for diamond in diamonds:
                    if (
                        y <= diamond.position.y < y + 5
                        and x <= diamond.position.x < x + 5
                    ):
                        section.append(diamond)

    print("Ini total diamond points", max_tile_diamonds)
    print("Ini section", section)
    return get_closest_diamond_position(bot_position, section)


# jalan pulang ada teleport yang ngebuat dia muter disitu situ aja

# python main.py --logic Greedy --email=your_email@example.com --name=your_name --password=your_password --team etimo
