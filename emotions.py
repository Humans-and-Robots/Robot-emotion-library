import sys, os, time
import api
import time
import threading
import sound
import emotionDisplay

class emotion():
    def emotion_ready(self):
        if api.Initialize():
            print("Initialized")
            api.PlayAction(3)
            time.sleep(3)
        else:
            print("Initialization failed")
            sys.exit(1)

    def show_emotion(self, emotion_class, emotion_level):
        api_map = {'happy1': 3, 'sad1': 3, 'fear1': 3, 'anger1': 3, 'surprise1': 3, 'happy3': 4, 'happy2': 5, 'anger2': 6, 'anger3': 7, 'fear3': 11,
                   'fear2': 12, 'surprise2': 13, 'surprise3': 14, 'sad2': 17, 'sad3': 18}


        emotionDisplay.main(emotion_class, emotion_level)
	if emotion_level > 1:
            sound.sound_activate(emotion_class, emotion_level)
	api.PlayAction(api_map[emotion_class + repr(emotion_level)])

    def sound_emotion(self, emotion_class, emotion_level):
	emotion_level = emotion_level+1
	if emotion_level > 1:
	    sound.sound_activate(emotion_class, emotion_level)
	else:
	    print("There are only two levels, use 1, or 2")

    def facial_emotion(self, emotion_class, emotion_level):
	emotionDisplay.main(emotion_class, emotion_level)

    def posture_emotion(self, emotion_class, emotion_level):
	api_map = {'happy1': 3, 'sad1': 3, 'fear1': 3, 'anger1': 3, 'surprise1': 3, 'happy3': 4, 'happy2': 5, 'anger2': 6, 'anger3': 7, 'fear3': 11,
                   'fear2': 12, 'surprise2': 13, 'surprise3': 14, 'sad2': 17, 'sad3': 18}

	emotion_level = emotion_level+1
        if emotion_level > 1:
	    api.PlayAction(api_map[emotion_class + repr(emotion_level)])
	else:
            print("There are only two levels, use 1, or 2")    
    def emotion_finished(self):
        api.ServoShutdown()


