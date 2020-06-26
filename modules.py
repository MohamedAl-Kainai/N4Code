import kivy
from kivmob import KivMob, TestIds

if kivy.utils.platform == 'android':
    from android.permissions import (
    Permission,
    request_permission,
    check_permission
    )
    from android.runnable import run_on_ui_thread
    from jnius import autoclass
else:
    run_on_ui_thread = lambda x:x

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.codeinput import CodeInput

from kivy.properties import ListProperty ,NumericProperty ,StringProperty
from kivy.animation import Animation

from kivy.utils import get_color_from_hex as hex
from kivy.metrics import sp,dp
from kivy.lang import Builder

from kivymd.toast import toast

from io import StringIO
import sys, threading, os
import ast, traceback
