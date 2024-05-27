# flake8: noqa
import pygame
from pygame.locals import *
from pygame import mixer
from const import *
from game import *

pygame.init()
mixer.init()
mixer.music.set_volume(20)

def bgm():
    mixer.music.load('music/chickenbgm.wav')
    mixer.music.play()

def ji():
    mixer.music.load('music/audios/ji.wav')
    mixer.music.play()

def ni():
    mixer.music.load('music/audios/ni.wav')
    mixer.music.play()

def tai():
    mixer.music.load('music/audios/tai.wav')
    mixer.music.play()

def mei():
    mixer.music.load('music/audios/mei.wav')
    mixer.music.play()

def kun():
    mixer.music.load('music/audios/kun.wav')
    mixer.music.play()

def ctrl():
    mixer.music.load('music/audios/ctrl.wav')
    mixer.music.play()

def music():
    mixer.music.load('music/audios/music.wav')
    mixer.music.play()

def niganma():
    mixer.music.load('music/audios/niganma.wav')
    mixer.music.play()

def a():
    mixer.music.load('music/audios/a.wav')
    mixer.music.play()

def wahaha():
    mixer.music.load('music/audios/wahaha.wav')
    mixer.music.play()

def aiyo():
    mixer.music.load('music/audios/aiyo.wav')
    mixer.music.play()

