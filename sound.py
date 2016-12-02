import pygame
import os.path
import sys

"""
Project 3, Team A: Emotion Audio Library

This plays emotion sound files contained in "wav" folder. This folder must be
present in current working directory.

Usage:

    1. To play emotion:
    
    >> sound_activate('happy',1)

        This would play happy level 1 sound file.

        Note that this is a non-blocking function, so the next command would
        execute immediately.
    
    2. To stop any playback abd to release file and device handles:
    
    >> sound_stop()
        
       stops any sound being played
        
    3. To know when a sound is being played
    
    >> sound_is_active()
        
        This would return True only if playback is active. Useful if you'd like
        to wait for playback to finish before performing the next task.

"""


def __playFile__(waveFile):
    '''Helper function for wave file playback'''
    global channel
    
    waveFile
    sound = pygame.mixer.Sound(waveFile)
    channel = sound.play()
    
def sound_is_active():
    '''Check if a sound is being played'''
    try:
        return channel.get_busy()
    except:
        return False
        
def sound_stop():
    '''Stops any sound being played'''
    channel.stop()

def sound_activate(emotion,level):
    '''Plays sound corresponding to emotion and level/intensity.
    This is a non-blocking function'''
    
    # generate emotion sound file name to be expected based on naming convention
    emotionFileName = "./wav/" + emotion + "_" + str(level) + ".wav"
    if not os.path.isfile(emotionFileName):
        raise ValueError('Could not find corresponding emotion sound file:', emotionFileName)

    # open and play
    __playFile__(emotionFileName)

pygame.init()
pygame.mixer.init()
if __name__ == "__main__":
    # open and play
    fileName = sys.argv[1]
    __playFile__(fileName)
    while channel.get_busy():
        pass
    
