from .models import Position


# Gets Information
def is_in_between(point1, point2, point3):
    return point1 <= point2 <= point3  # Check if point2 is between point1 and point3


def get_direction(current_x, current_y, dest_x, dest_y, game_objects):
    teleports = get_teleport_info(game_objects)
    diamondButton = get_diamond_button(game_objects)
    horizontal = True
    # This will avoid any diamond button and teleports on the way by going around it
    if (
        is_in_between(current_x, diamondButton.position.x, dest_x)
        and current_y == diamondButton.position.y
    ) or (
        is_in_between(dest_x, diamondButton.position.x, current_x)
        and current_y == diamondButton.position.y
    ):
        horizontal = False

    for teleport in teleports:
        if (
            is_in_between(current_x, teleport.position.x, dest_x)
            and current_y == teleport.position.y
        ) or (
            is_in_between(dest_x, teleport.position.x, current_x)
            and current_y == teleport.position.y
        ):
            horizontal = False

    delta_x = clamp(dest_x - current_x, -1, 1)
    delta_y = clamp(dest_y - current_y, -1, 1)

    if delta_x != 0 and horizontal:
        delta_y = 0
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


# Gets Location
def get_diamond_button(game_objects: list):
    for item in game_objects:
        if item.type == "DiamondButtonGameObject":
            return item


def get_closest_diamond_position(pos: Position, diamonds: list):
    return min(
        diamonds,
        key=lambda d: abs(d.position.x - pos.x) + abs(d.position.y - pos.y),
    ).position


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
    return 1000 * abs((dest.x - current.x) + (dest.y - current.y))


# Comparisons
def position_equals(a: Position, b: Position):
    return a.x == b.x and a.y == b.y


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


def killable(my_bot: any, enemy: any, diamond_pos: Position) -> bool:
    # Check if the enemy is in a killable position which is a position which has the same distance to the diamond as my_bot
    return (
        abs(my_bot.position.x - diamond_pos.x) + abs(my_bot.position.y - diamond_pos.y)
        == abs(enemy.position.x - diamond_pos.x) + abs(enemy.position.y - diamond_pos.y)
        and my_bot.properties.diamonds
        == 5  # wont kill the enemy if my_bot already has 5 diamonds
    )


# section paling banyak poin bukan diamond karna red diamond lebih worth it
def find_diamond_mine(diamonds: list):
    # return closest diamond to bot which is located in the 5x5 area with the most number of diamonds
    pass


# jalan pulang ada teleport yang ngebuat dia muter disitu situ aja

# python main.py --logic Greedy --email=your_email@example.com --name=your_name --password=your_password --team etimo
