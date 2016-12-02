import sys, os, time
from emotions import emotion


if __name__ == '__main__':
    new_emotion = emotion()
    new_emotion.emotion_ready()
    emotion_class ='happy'
    emotion_level = 3
    new_emotion.show_emotion(emotion_class, emotion_level)

    new_emotion.emotion_finished()

