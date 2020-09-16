# simple 8-ball module
# shuffle entries and return a random choice from
# the list of entries

from random import shuffle, choice

responses = [
    "All sings point to yes!",
    "Reply hazy, ask again.",
    "It is certainly so.",
    "Wouldn't count on it.",
    "Ask again later.",
    "It will surely happen.",
    "I'm not sure.",
    "Count on it.",
    "Ask again tomorrow.",
    "Maybe.",
    "It is possible.",
    "Does anyone really know?",
    "Ask a friend instead.",
    "You are on the right track, research further.",
    "Try asking Google.",
    "You broke the eight-ball with this question."
]

def eight_ball(**kwargs):
    shuffle(responses)
    return choice(responses)