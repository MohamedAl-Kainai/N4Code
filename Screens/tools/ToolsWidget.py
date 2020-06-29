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
    code_input = ObjectProperty()

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

    def tab(self,pos):
        self.add_idee(pos,'\t')

    def _text(self,pos):
        self.add_idee(pos,'""')

    def _dict(self,pos):
        self.add_idee(pos,'{}')

    def _list(self,pos):
        self.add_idee(pos,'[]')

    def _grup(self,pos):
        self.add_idee(pos,'()')

    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            self.t = time.time()

        return super(ToolsWidget2,self).on_touch_down(touch)

    def on_touch_move(self,touch):
        if touch.grab_current is self and time.time()-self.t > 0.7:
            self.opacity = .5
            if Window.height-100 > self.pos[1]:
                self.pos[1] = touch.y
            else:
                if self.pos[1] > touch.y:
                    self.pos[1] = touch.y

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            self.opacity = 1

class ToolsWidget3(BoxLayout):
    buttons_color = ListProperty([1,1,1,1])

    def font_size_plus(self):
        if self.output.font_size >= sp(30):
            toast('max')
        else:
            self.output.font_size += sp(3)

    def font_size_minus(self):
        if self.output.font_size <= sp(12):
            toast('max')
        else:
            self.output.font_size -= sp(3)
