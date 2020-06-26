from modules import *

Builder.load_string('''
<outputscreen>:
    id:outputscreen
    canvas:
        Color:
            rgb:background_app
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        TextInput:
            id:output
            text:''
            background_color:0,0,0,0
            foreground_color:output_text_color

    MDFloatingActionButton:
        icon:'close'
        on_release:
            root.manager.transition.direction = 'right'
            app.root.current = 'menu'
            output.text = ''
''')

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

class outputscreen(Screen):
    text = StringProperty('')
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_read(self,line):
        # do something with the line
        print(capturing.print(line))

    def output(self,text):
        with Capturing() as out:
            exec(text)
        for i in out:
            self.ids.output.text += i+'\n'
        self.ids.output.text += '\n[Program finished]'
