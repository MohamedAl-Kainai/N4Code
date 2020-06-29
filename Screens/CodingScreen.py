from modules import *
from Screens.tools.ToolsWidget import ToolsWidget ,ToolsWidget2

Builder.load_string('''
<CodeInputWidget>:
    background_color:.1,.1,.4,.1

<codingscreen>:
    canvas:
        Color:
            rgb:background_app
        Rectangle:
            #source: 'mylogo.png'
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation:'vertical'
        BoxLayout:
            size_hint:1,None
            size:1,dp(50)
            FloatLayout:
                ToolsWidget:
                    obj:code_input
                    pos_hint:{'top':1}

        BoxLayout:
            ScrollView:
                size_hint: 1, 1
                CodeInputWidget:
                    id:code_input
                    _run_code:_run_code
                    size_hint: 1, None
                    height: self.minimum_height
                    font_size:root.font_size

        BoxLayout:
            size_hint:1,None
            size:1,dp(50)
            FloatLayout:
                ToolsWidget2:
                    code_input:code_input
                    id:toolswidget2
                    code_input:code_input
                    pos_hint:{'bottom':1}

                    FloatLayout:
                        size_hint:None,None
                        size:dp(30),dp(50)
                        MDFloatingActionButton:
                            id:_run_code
                            icon:'play'
                            size_hint:None,None
                            size:dp(40),dp(40)
                            pos_hint:{'center_x':.3,'center_y':.32}
                            md_bg_color:hex('51cc0e')
                            on_release:
                                if root.ids.code_input.CheckErrors():toast(root.ids.code_input.CheckErrors())
                                else:app.RunCode(code_input.text)
                                app.get_permission()
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

    def on_text(self,obj,text):
        obj._run_code.md_bg_color = hex('ba1307') if self.CheckErrors() else hex('51cc0e')

    def CheckErrors(self):
        try:
            ast.parse(self.text)
            return False
        except:
            return 'SyntaxError'
