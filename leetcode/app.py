import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
class childApp(GridLayout):
 def __init__(self, **kwargs):
  super(childApp, self).__init__()
  self.cols = 2
  self.add_widget(Image(source = 'C:/Users/Admin/Downloads/img2.jpg'))
  self.add_widget(Image(source = 'C:/Users/Admin/Downloads/img2.jpg'))
  self.add_widget(Label(text='Student name'))
  self.s_name = TextInput()
  self.add_widget(self.s_name)
  self.add_widget(Label(text='Reg No'))
  self.emp = TextInput()
  self.add_widget(self.emp)
  self.add_widget(Label(text='Branch'))
  self.com = TextInput()
  self.add_widget(self.com)
  self.add_widget(Label(text='Location'))
  self.loc = TextInput()
  self.add_widget(self.loc)
  self.press = Button(text='click')
  self.press.bind(on_press = self.click)
  self.add_widget(self.press)
 def click(self,instance):
  f = open("out1.txt", 'w')
  print("Student name:"+self.s_name.text, file = f)
  print("Reg No:"+self.emp.text, file = f)
  print("Branch:"+self.com.text, file = f)
  print("Location:"+self.loc.text, file = f)
  f.close()  
class parentApp(App):
 def build(self):
  return childApp()
if __name__ =="__main__":
 app = parentApp()
 app.run()