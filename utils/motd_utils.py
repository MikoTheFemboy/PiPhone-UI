import random

def get_motd():
    motd = [
        "Software is like sex; it's better when\nit's free.\n-Linux Torvalds",
        "A computer is like air conditioning -- it\nbecomes useless when you open Windows.\n-Linux Torvalds",
        "Trains usually aren't tasty.\n-Miko",
        "Linux for femboys, call that TransNux.\n-Miko"
    ]

    return random.choice(motd)