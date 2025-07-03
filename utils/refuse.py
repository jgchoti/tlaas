from random import random, choice

def api_refuse():
    if random() < 0.7:
        lazy_messages = [
            "Nah. Too lazy to do that right now.",
            "Hmm... no thanks.",
            "Sounds like work. Pass.",
            "Not in the mood.",
            "Not today, human.",
        ]
        return {"excuse": choice(lazy_messages), "status": "the API is refusing to work. Try again later (or don’t)"}
    return None
