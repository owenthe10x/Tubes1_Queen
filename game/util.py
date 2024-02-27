from .models import Position


# Gets Information
def get_direction(current_x, current_y, dest_x, dest_y):
    delta_x = clamp(dest_x - current_x, -1, 1)
    delta_y = clamp(dest_y - current_y, -1, 1)
    if delta_x != 0:
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
            return item.properties.milliseconds_left


def get_closest_diamond_position(pos: Position, diamonds: list):
    return min(
        diamonds,
        key=lambda d: abs(d.position.x - pos.x) + abs(d.position.y - pos.y),
    ).position


def get_second_closest_diamond_position(diamonds, pos):
    closest_diamond = min(
        diamonds, key=lambda d: abs(d.position.x - pos.x) + abs(d.position.y - pos.y)
    )
    # Remove the closest diamond from the list
    remaining_diamonds = [d for d in diamonds if d != closest_diamond]

    if remaining_diamonds:  # Check if there are remaining diamonds
        second_closest_diamond = min(
            remaining_diamonds,
            key=lambda d: abs(d.position.x - pos.x) + abs(d.position.y - pos.y),
        )
        return second_closest_diamond
    else:
        return None  # If there are no remaining diamonds


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
    return 1000 * ((dest.x - current.x) + (dest.y - current.y))


# Comparisons
def position_equals(a: Position, b: Position):
    return a.x == b.x and a.y == b.y


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


# Actions
# def kill_bot(diamond_loc:Position, enemy_loc:Position):


# python main.py --logic Greedy --email=your_email@example.com --name=your_name --password=your_password --team etimo
