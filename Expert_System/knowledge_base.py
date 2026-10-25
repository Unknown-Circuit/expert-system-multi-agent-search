# Expert_System/knowledge_base.py
RULES = [
    ("traffic_heavy", "choose_alternative_route"),
    ("flood_risk", "avoid_lowland_path"),
    ("battery_low", "reduce_speed_and_limit_distance"),
    ("weather_rainy", "use_wider_road"),
]

FACTS = {
    "traffic_heavy": True,
    "flood_risk": False,
    "battery_low": True,
    "weather_rainy": True,
}
