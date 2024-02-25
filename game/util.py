from .models import Position


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


def get_direction(current_x, current_y, dest_x, dest_y):
    delta_x = clamp(dest_x - current_x, -1, 1)
    delta_y = clamp(dest_y - current_y, -1, 1)
    if delta_x != 0:
        delta_y = 0
    return (delta_x, delta_y)


def position_equals(a: Position, b: Position):
    return a.x == b.x and a.y == b.y


def get_rank(bots: list, bot_id: int):
    sorted_bots = sorted(bots, key=lambda b: b.properties.diamonds, reverse=True)
    for i, bot in enumerate(sorted_bots):
        if bot.id == bot_id:
            return i + 1


def get_time_left(game_objects: list):
    for item in game_objects:
        if item.type == "BotGameObject":
            return item.properties.milliseconds_left


def closest_diamond(pos: Position, diamonds: list):
    print(
        "anjay",
        min(
            diamonds,
            key=lambda d: abs(d.position.x - pos.x) + abs(d.position.y - pos.y),
        ).position,
    )
    return min(
        diamonds,
        key=lambda d: abs(d.position.x - pos.x) + abs(d.position.y - pos.y),
    ).position
