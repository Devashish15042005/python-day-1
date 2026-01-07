import time
import sys

def print_lyrics():
    lyrics = [
        "Jaati nahi teri yaadein kasam se",
        "Ke dil ka bharam hai tu",
        "Baaki nahi ab koi sharam, jaana",
        "Ek dharam hai tu",
        "Jo kehti thi 'Mat piyo na'",
        "Meri jaan zeher hain yeh",
        "Usey dekhta hu koi gair chuye",
        "Ab aur zeher kya piyu?"
    ]
    delays = [0.5, 1.3, 1.0, 2.0, 0.8, 1.0, 0.5, 1.7]

    print("\nPaaroo - :\n")
    time.sleep(1.2)
    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.077)
        print()
        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(1.0)
    print("\n🎵 End of song — hope you felt the vibe! 🎵")
print_lyrics()
