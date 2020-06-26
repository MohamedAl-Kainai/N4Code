from modules import *

Builder.load_file('Screens/tools/ToolsWidget.kv')

class ToolsWidget(BoxLayout):
    buttons_color = ListProperty([1,1,1,1])

    def font_size_plus(self):
        if self.obj.font_size >= sp(30):
            toast('max')
        else:
            self.obj.font_size += sp(3)

    def font_size_minus(self):
        if self.obj.font_size <= sp(12):
            toast('max')
        else:
            self.obj.font_size -= sp(3)

class ToolsWidget2(BoxLayout):
    buttons_color = ListProperty([1,1,1,1])

    def add_idee(self,pos,idee):
        text = ''
        for index,value in enumerate(self.code_input.text.split('\n')):
            if index == pos[1]:
                text += value[0:pos[0]]+idee+value[pos[0]::]+'\n'
            else:
                text += value+'\n'

        self.code_input.text = text[0:-1]
        self.code_input.cursor = (pos[0]+1,pos[1])
        self.code_input.focus = True

    def tab(self):
        self.code_input.text += '\t'
        self.code_input.focus = True

    def _text(self,pos):
        self.add_idee(pos,'""')

    def _dict(self,pos):
        self.add_idee(pos,'{}')

    def _list(self,pos):
        self.add_idee(pos,'[]')

    def _grup(self,pos):
        self.add_idee(pos,'()')
