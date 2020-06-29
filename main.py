from modules import *
from Screens.CodingScreen import codingscreen
from Screens.OutputScreen import outputscreen

Window.keyboard_anim_args = {'t': 'in_out_expo', 'd': 0.3}
Window.softinput_mode = 'below_target'

if kivy.utils.platform == 'android':
    Color = autoclass("android.graphics.Color")
    WindowManager = autoclass('android.view.WindowManager$LayoutParams')
    activity = autoclass('org.kivy.android.PythonActivity').mActivity

Builder.load_string('''
#:import hex kivy.utils.get_color_from_hex
#:import Window kivy.core.window.Window
#:import toast kivymd.toast.toast

# app colors...
#:set background_app hex('adadad')
#:set background_bar hex('2b2b2b')
#:set buttons_color hex('FFFFFF')
#:set output_text_color hex('FFFFFF')
''')

class N4Coding(MDApp):
    sm = ScreenManager()
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        self.outputscreen = outputscreen(name='result')
        self.codingscreen = codingscreen(name='menu')
        self.sm.add_widget(self.codingscreen)
        self.sm.add_widget(self.outputscreen)

        return self.sm

    @run_on_ui_thread
    def statusbar(self,color):
        window = activity.getWindow()
        window.clearFlags(WindowManager.FLAG_TRANSLUCENT_STATUS)
        window.addFlags(WindowManager.FLAG_DRAWS_SYSTEM_BAR_BACKGROUNDS)
        window.setStatusBarColor(Color.parseColor(color))
        window.setNavigationBarColor(Color.parseColor(color))

    def RunCode(self,text):
        self.sm.transition.direction = 'left'
        self.sm.current = 'result'
        threading.Thread(target=self.outputscreen.output,args=[text]).start()

    def on_start(self):
        if kivy.utils.platform == 'android':
            self.statusbar('#2b2b2b') # statusbar color

    def get_permission(self):
        if kivy.utils.platform == 'android':
            if (status:=check_permission(Permission.WRITE_EXTERNAL_STORAGE)):
                pass
            else:
                request_permission(Permission.WRITE_EXTERNAL_STORAGE)

if __name__ == "__main__":
    N4Coding().run()
