import time
import sys

def type_lyric(line, char_delay=0.055):  # balanced speed
    for char in line:
        print(char, end='', flush=True)
        time.sleep(char_delay)
    print()

def print_lyrics():
    lyrics = [
        "I shouldn't have fallen in love",
        "Look what it made me become",
        "I let you get too close ",
         "Just to wake up alone",
        "And I know you think you can run",
        "You're scared to believe I'm the one",
        "But I just can't let you go........",
        "I'd let the world burn",
        "Let the world burn for you",
        "This is how it always had to end",
        "If I can't have you then no one can",
        "I'd let it burn",
        "I'd let the world burn",
        "           by @dev.Frosty"
    ]

    delays = [1.1, 1.0, 1.3, 1.3 ,1.1, 1.1, 1.1, 1.2, 1.1, 1.2, 1.1, 1.0, 0.9, 0.8]
    print("\n")

    print("LET THE WORLD BURN 🔥:\n")
    time.sleep(1.0)

    for i, line in enumerate(lyrics):
        type_lyric(line)
        time.sleep(delays[i])

print_lyrics()
time.sleep(0.02)
