from modules import *
from Screens.CodingScreen import codingscreen
from Screens.OutputScreen import outputscreen

Window.keyboard_anim_args = {'t': 'in_out_expo', 'd': 0.3}
Window.softinput_mode = 'pan'

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

    def build(self):
        self.ads = KivMob("ca-app-pub-8577364383694171~6132993772")
        self.ads.new_interstitial("ca-app-pub-8577364383694171/2513197368")
        self.ads.request_interstitial()

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

    # def zeig_ads(self):
    #     if (status:=check_permission(Permission.ACCESS_NETWORK_STATE)):
    #         toast(str(f'permission {status}'))
    #         if (check:=self.ads.is_interstitial_loaded()):
    #             self.ads.show_interstitial()
    #         else:
    #             #toast(str(check))
    #             self.ads.request_interstitial()
    #     else:
    #         request_permission(Permission.ACCESS_NETWORK_STATE)
    #         toast(str(f'permission {status}'))

if __name__ == "__main__":
    N4Coding().run()
