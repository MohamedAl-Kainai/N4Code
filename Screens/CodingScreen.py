from modules import *
from Screens.tools.ToolsWidget import ToolsWidget ,ToolsWidget2

Builder.load_string('''

<CodeInputWidget>:
    background_color:0,0,0,0

<codingscreen>:
    BoxLayout:
        size_hint:1,None
        height:Window.height-Window.keyboard_height
        orientation:'vertical'
        canvas:
            Color:
                rgb:background_app
            Rectangle:
                #source: 'mylogo.png'
                pos: self.pos
                size: self.size

        BoxLayout:
            size_hint:1,None
            size:1,dp(50)
            FloatLayout:
                ToolsWidget:
                    obj:code_input
                    pos_hint:{'top':1}

        BoxLayout:
            ScrollView:
                CodeInputWidget:
                    id:code_input
                    size_hint: 1, None
                    height: self.minimum_height
                    font_size:root.font_size
                    on_text:
                        _run_code.md_bg_color = hex('51cc0e') if self.CheckErrors() else hex('ba1307')

        BoxLayout:
            size_hint:1,None
            size:1,dp(50)
            FloatLayout:
                ToolsWidget2:
                    code_input:code_input
                    pos_hint:{'bottom':1}

                MDFloatingActionButton:
                    id:_run_code
                    icon:'play'
                    pos_hint:{'right':1}
                    md_bg_color:hex('51cc0e')
                    on_release:
                        if root.ids.code_input.CheckErrors():app.RunCode(code_input.text)
                        else:toast('Error')

''')
class codingscreen(Screen):
    font_size = NumericProperty(sp(15))
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

class CodeInputWidget(CodeInput):
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)

    def Idee(self,idee,pos):
        text = ''
        for index,value in enumerate(self.text.split('\n')):
            if index == pos[1]:
                text += value[0:pos[0]]+idee+'()'+value[pos[0]::]+'\n'
            else:
                text += value+'\n'

        self.text = text[0:-1]
        self.cursor = (pos[0]+len(idee+'()')-1,pos[1])
        self.focus = True

    def CheckErrors(self):
        try:
            ast.parse(self.text)
            return True
        except:return False
            #traceback.print_exc()
