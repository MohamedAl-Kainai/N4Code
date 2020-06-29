from modules import *
from Screens.tools.Capturing import capturing
from Screens.tools.ToolsWidget import ToolsWidget3

Builder.load_string('''
<outputscreen>:
    id:outputscreen
    canvas:
        Color:
            rgb:background_app
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        BoxLayout:
            padding:dp(1),dp(20),0,dp(60)
            ScrollView:
                TextInput:
                    size_hint:1,None
                    height:self.minimum_height
                    id:output
                    text:''
                    background_color:0,0,0,0
                    foreground_color:output_text_color

        ToolsWidget3:
            pos_hint:{'bottom':1}
            output:output

''')
class outputscreen(Screen):
    text = StringProperty('')
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_line(self,line):
        self.ids.output.text = open('logout.txt','r').read()

    def output(self,text):
        out = capturing('logout.txt',self.on_line)
        out.start()
        try:
            exec(text)
        except BaseException as ex:
            ex_type, ex_value, ex_traceback = sys.exc_info()
            trace_back = traceback.extract_tb(ex_traceback)
            print(ex_type.__name__+': ',end='')
            print(ex_value,end='')
            temp = False
            for trace in trace_back:
                if temp:
                    print(f' < line {trace[1]} >')
                temp = True
        time.sleep(0.1)
        self.ids.output.text = open('logout.txt','r').read()
        out.stop()

        self.ids.output.text += '\n[Program finished]'
