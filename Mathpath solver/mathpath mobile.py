from kivymd.app import MDApp
from kivymd.uix.button import MDRoundFlatIconButton, MDFlatButton, MDIconButton, MDRoundFlatButton
from kivy.uix.button import Button
from kivymd.uix.list import OneLineAvatarListItem, OneLineIconListItem, IconLeftWidget, MDList
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.widget import Widget  
from kivy.uix.popup import Popup
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.gridlayout import MDGridLayout 
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen  #VERSION OF LIBRARIES: KivyMD = 1.1.1 , Kivy = 2.1.0 , SymPy = 1.10.1
from kivy.lang.builder import Builder      
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import TouchBehavior
from kivy.metrics import dp 
from kivymd.uix.navigationdrawer import (
    MDNavigationLayout,
    MDNavigationDrawer,
    MDNavigationDrawerMenu,
    MDNavigationDrawerHeader)
from kivy.uix.scrollview import ScrollView        
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image,CoreImage
from kivy.core.window import Window
from sympy import S, I, pi, gamma, zeta, jacobi, legendre, assoc_legendre, hermite, laguerre, assoc_laguerre
from sympy.plotting import plot, plot3d
import io #--> for display graphics without errors. Please look at below 'calc_graphs(self)'
from sympy import *
import matplotlib.pyplot as plt
import webbrowser
a, b, c, d, e, f, g, h, i, j, k, l, m, n, p, r, s, t, u, v, x, y, z, nu, rho, phi, theta = symbols("a b c d e f g h i j k l m n p r s t u v x y z nu rho phi theta")

init_printing(use_unicode=True) #for pretty mathematical symbols by Sympy

dataset_name_data=[] #dataset memory 
img_data=[] #--> 2d, 3d, dataset image graph memory to use delete or change.           
type_hint_text = [''] #--> data for hint text above on keyboard.                                                      here is main keyboard symbols  
mykeyboard_keys={'b1': ('∫ dx','#EEEEEE'), 'b2':('abc','#EEEEEE'), 'b3':('[size=32]trigo∆[/size]','#EEEEEE'), 'b4':('[size=72]←[/size]','#EEEEEE'), 
            'b5':('[size=72]→[/size]','#EEEEEE'), 'b6':('[size=76]⌫[/size]','#EEEEEE'), 'b7':('(','#DEDEDE'), 'b8':(')','#DEDEDE'),'b9':('7','F6F6F6'),
            'b10':('8','F6F6F6'),'b11':('9','F6F6F6'),'b12':('/','#DEDEDE'),'b13':('⬚[sup]⬚[/sup]','#DEDEDE'), 'b14':('√⬚','#DEDEDE'),
            'b15':('4','F6F6F6'),'b16':('5','F6F6F6'),'b17':('6','F6F6F6'), 'b18':('×','#DEDEDE'),'b19':('⬚[sup]2[/sup]','#DEDEDE'),'b20':('x','#DEDEDE'),
            'b21':('1','F6F6F6'), 'b22':('2','F6F6F6'),'b23':('3','F6F6F6'),'b24':('-','#DEDEDE'),'b25':('π','#DEDEDE'), 'b26':(',','#DEDEDE'),
            'b27':('0','F6F6F6'),'b28':('.','F6F6F6'),'b29':('=','#DEDEDE'), 'b30':('+','#DEDEDE')}
                                                                                                                      #after changes, turn back main keyboard
old_mykeyboard_keys={'b1': ('∫ dx','#EEEEEE'), 'b2':('abc','#EEEEEE'), 'b3':('[size=32]trigo∆[/size]','#EEEEEE'), 'b4':('[size=72]←[/size]','#EEEEEE'), 
            'b5':('[size=72]→[/size]','#EEEEEE'), 'b6':('[size=76]⌫[/size]','#EEEEEE'), 'b7':('(','#DEDEDE'), 'b8':(')','#DEDEDE'),'b9':('7','F6F6F6'),
            'b10':('8','F6F6F6'),'b11':('9','F6F6F6'),'b12':('/','#DEDEDE'),'b13':('⬚[sup]⬚[/sup]','#DEDEDE'), 'b14':('√⬚','#DEDEDE'),
            'b15':('4','F6F6F6'),'b16':('5','F6F6F6'),'b17':('6','F6F6F6'), 'b18':('×','#DEDEDE'),'b19':('⬚[sup]2[/sup]','#DEDEDE'),'b20':('x','#DEDEDE'),
            'b21':('1','F6F6F6'), 'b22':('2','F6F6F6'),'b23':('3','F6F6F6'),'b24':('-','#DEDEDE'),'b25':('π','#DEDEDE'), 'b26':(',','#DEDEDE'),
            'b27':('0','F6F6F6'),'b28':('.','F6F6F6'),'b29':('=','#DEDEDE'), 'b30':('+','#DEDEDE')}

pretty_symb=['sin(','cos(','tan(','cot(','sec(','csc(','sinc(','asin(','acos(','atan(','acot(','asec(','acsc(','asinc(','sinh(','cosh(',
        'atanh(','coth(','asinh(','acosh(','tanh','acoth(', 'a','b','c','d','e','f','g','h','y','i','j','k','o','m','n','p','q','r','t','x','z',
        'α','β','θ','φ','pi','oo','sqrt(','exp(','log(','ln(','Abs(','root(','0','1','2','3','4','5','6','7','8','9'] #look at below
                              
_keyboard_back = 0 #keyboard counter


class ContentNavigationDrawer(MDBoxLayout):
    pass

class MenuScreen(Screen,TouchBehavior):  #we take touchBehaviour from kivymd
    duration_long_touch = 0.58 #long touch on 'remove symbol'
    from shrink_function import oto_width_main, oto_height_main  #--> call the height and width of math symbols on label.       

    def checktouch(self):
        try:
            touch=self.ids.txt1.cursor_pos
            if Window.mouse_pos[1]<touch[1]-27 and self.ids.txt1.keyboard_mode=='managed':
                self.ids.txt1.focus=False
                if (self.ids.txt1.text.count('diff(')==1 or self.ids.txt1.text.count('integrate(')==1) and (self.ids.txt1.text[-1]==')' and img_data.count('2')==0 and '=' not in self.ids.txt1.text):
                    step_layout=MDFloatLayout(size_hint_y=None, pos_hint={'top':0})
                    step_button=MDRoundFlatButton(text='Show Steps', size_hint=(None,None), pos_hint={'center_x':0.5, 'top':0.2})
                    self.ids["button_steps"]=step_layout #for delete widget
                    web_text=self.ids.txt1.text.replace('(','%28')
                    web_text1=web_text.replace(')','%29')
                    web_text2=web_text1.replace('^','%5E') #step-by-step solution transformation look at below '/input/?i={}'
                    web_text3=web_text2.replace('+','%2B')
                    web_text4=web_text3.replace(',','%2C')
                    web_text5=web_text4.replace('/','%2F')
                    web_text6=web_text5.replace('×','*')
                    if "diff(" in self.ids.txt1.text:
                        web_text7=web_text6+'#diffsteps'
                    else:
                        web_text7=web_text6+'#intsteps'       #for step-by-step solution
                    step_button.bind(on_release=lambda _:webbrowser.open('https://gamma.sympy.org/input/?i={}'.format(web_text7))) 
                    step_layout.add_widget(step_button)
                    self.ids.box_layout.add_widget(step_layout)
                    img_data.append('2')
            else:
                pass
        except(Exception):
            self.ids.lbl0.text='StepButton ConnectionError'

    def checkfocus(self):
        check_focus=self.ids.txt1.focus
        global artifical_keyboard #for remove mykeyboard widget!
        current_opacity = 0.4
        if self.ids.bulb_icon.icon=='lightbulb-off': 
            current_opacity = 0
        if check_focus==True and self.ids.txt1.keyboard_mode=='managed': #call our created keyboard
                                                          
            artifical_keyboard=MDFloatLayout(size_hint_y=0.5) #floatlayout good choice!
            mykeyboard=MDGridLayout(cols=6, rows=5, height='283dp',md_bg_color='#EEEEEE', spacing='0.50dp', size_hint_y=None)
            ahint_text=MDLabel(text=type_hint_text[-1], font_size='9dp',color='black' ,size_hint_y=None, y=mykeyboard.top + dp(5), halign='center', 
                adaptive_height=True, markup=True, opacity=current_opacity)
            for n,m in mykeyboard_keys.items():
                but=Button(text=str(m[0]), color='black', font_size='20sp' ,markup=True, font_name='dejavusansmono.ttf', background_normal=m[1], background_color=m[1],size_hint_y=None, height='56dp')
                mykeyboard.add_widget(but)  
                but.bind(on_press= lambda _,z=str(m[0]):self.mykeyborad_click(z))
                if n=='b6':
                    self.ids['key_delete']=but #for check state of delete button.

            self.ids['keyboard_hint']=ahint_text #for hint!
            artifical_keyboard.add_widget(ahint_text)
            artifical_keyboard.add_widget(mykeyboard)   
            self.ids.box_layout.add_widget(artifical_keyboard)
                                  
        elif check_focus==False and self.ids.txt1.keyboard_mode=='managed':
            self.ids.box_layout.remove_widget(artifical_keyboard)
            mykeyboard_keys.update(old_mykeyboard_keys)
        
    def on_long_touch(self, *args): #delete textbox with long-touch
        try:
            l=self.ids.txt1.cursor_index()                                    
            if self.ids.key_delete.state=='down' and l != 0 :
                self.ids.txt1.focus=True
                self.ids.txt1.text=''
                if self.ids.txt1.text=='':
                    if len(img_data)>0: 
                        if (img_data.count('2'))>0:
                            self.ids.box_layout.remove_widget(self.ids.button_steps)
                        else:
                            self.ids.box_layout.remove_widget(self.ids.img_box)
                        img_data.clear() 
                
                    self.ids.txt1.text=""
                    self.ids.lbl0.text=""
                    self.ids.lbl1.text=""
                    self.ids.lbl_blue.text="[Out]"
                    self.ids.lbl1.font_size="18dp"
                    self.ids.lbl0.font_size="14dp"
                    self.ids.lblcol.background_color=(0,0,0,0) 
                    _keyboard_back = 0
                    type_hint_text.clear()
                    type_hint_text.append('')
                    self.ids.keyboard_hint.text=''
        except(Exception):
            pass

    def mykeyborad_click(self, z): 
        try:
            first_text_check_for_pretty=self.ids.txt1.text
            trigo_add_bra=['sin','cos','tan','cot','sec','csc','sinc','asin','acos','atan','acot','asec','acsc','asinc','sinh','cosh',
            'tanh','coth','[size=30]asinh[/size]','[size=30]acosh[/size]','[size=30]atanh[/size]','[size=30]acoth[/size]',
            'det','[size=20]transpose[/size]','[size=22]inverse[/size]','[size=16]eigenvalues[/size]','[size=16]eigenvectors[/size]',
            '[size=22]cofactor[/size]','[size=22]echolon[/size]','rank']
                                                      
            if z=='[size=72]←[/size]':
                self.ids.txt1.focus=True
                self.ids.txt1.do_cursor_movement('cursor_left',control=False, alt=False)

            elif z=="[size=72]→[/size]":
                self.ids.txt1.focus=True
                self.ids.txt1.do_cursor_movement('cursor_right',control=False, alt=False)
               
            elif z=='[size=76]⌫[/size]': 
                self.ids.txt1.focus=True
                l=self.ids.txt1.cursor_index() 
                if l !=0:

                    for d in reversed(pretty_symb[:22]):
                        if (d == self.ids.txt1.text[self.ids.txt1.cursor_index()-4 : self.ids.txt1.cursor_index()] or d == self.ids.txt1.text[self.ids.txt1.cursor_index()-5 : self.ids.txt1.cursor_index()]
                         or d == self.ids.txt1.text[self.ids.txt1.cursor_index()-6 : self.ids.txt1.cursor_index()]):
                            lx = len(d)
                            self.ids.txt1.text = self.ids.txt1.text[:l-lx]+''+self.ids.txt1.text[l:]
                            self.ids.txt1.cursor=self.ids.txt1.get_cursor_from_index(l-lx)
                            return lx
 
                    for d in pretty_symb[47:55]:
                        if (d == self.ids.txt1.text[self.ids.txt1.cursor_index()-4 : self.ids.txt1.cursor_index()] or d == self.ids.txt1.text[self.ids.txt1.cursor_index()-5 : self.ids.txt1.cursor_index()]
                         or d == self.ids.txt1.text[self.ids.txt1.cursor_index()-6 : self.ids.txt1.cursor_index()]):
                            lx = len(d)
                            self.ids.txt1.text = self.ids.txt1.text[:l-lx]+''+self.ids.txt1.text[l:]
                            self.ids.txt1.cursor=self.ids.txt1.get_cursor_from_index(l-lx)
                            if len(self.ids.txt1.text)==0:
                                self.ids.keyboard_hint.text=''
                                type_hint_text.clear()
                                type_hint_text.append('')

                            return lx

                    else:
                        lx = 1
                        self.ids.txt1.text = self.ids.txt1.text[:l-1]+''+self.ids.txt1.text[l:]
                        self.ids.txt1.cursor=self.ids.txt1.get_cursor_from_index(l-lx) 
                
                if len(self.ids.txt1.text)<=0: 
                    type_hint_text.clear()
                    type_hint_text.append('')
                    self.ids.keyboard_hint.text=''

            elif z=="⬚[sup]2[/sup]":
                if self.ids.txt1.text !='':
                    l=self.ids.txt1.cursor_index()  #l+2 is len(^2) therefore!
                    self.ids.txt1.text = self.ids.txt1.text[:l]+'^2'+self.ids.txt1.text[l:]
                    self.ids.txt1.cursor=self.ids.txt1.get_cursor_from_index(l+2)
                elif self.ids.txt1.text=="":
                    self.ids.txt1.text = 'a^2'

            elif z=="⬚[sup]⬚[/sup]":
                if self.ids.txt1.text !='':
                    l=self.ids.txt1.cursor_index()
                    self.ids.txt1.text = self.ids.txt1.text[:l]+'^'+self.ids.txt1.text[l:]
                    self.ids.txt1.cursor=self.ids.txt1.get_cursor_from_index(l+1)
                elif self.ids.txt1.text =='':
                    self.ids.txt1.text = 'a^n'
            elif z=="√⬚":
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'sqrt('+self.ids.txt1.text[l:]
                self.ids.txt1.cursor=self.ids.txt1.get_cursor_from_index(l+5)

            elif z=='π':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'pi'+self.ids.txt1.text[l:]
                self.ids.txt1.cursor=self.ids.txt1.get_cursor_from_index(l+2)

            elif z in trigo_add_bra[:22]:
                add_bra=z+'('
                add_bra1=add_bra.replace('[/size]','')
                add_bra2=add_bra1.replace('[size=28]','')
                k=len(add_bra2)
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+add_bra2+self.ids.txt1.text[l:]
                self.ids.txt1.cursor=self.ids.txt1.get_cursor_from_index(l+k)
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty, b=self.ids.txt1.text)
            elif z in trigo_add_bra[22:]:
                my_matrix=z
                my_matrix1=my_matrix.replace('[size=20]transpose[/size]','.T')
                my_matrix2=my_matrix1.replace('[size=22]inverse[/size]','.inv()')
                my_matrix3=my_matrix2.replace('[size=16]eigenvalues[/size]','.eigenvals()')
                my_matrix4=my_matrix3.replace('[size=16]eigenvectors[/size]','.eigenvects()')
                now_matrix=my_matrix4.replace('[size=22]echolon[/size]','.echelon_form()')
                now_matrix1=now_matrix.replace('rank','.rank()')
                now_matrix2=now_matrix1.replace('det','.det()')
                now_matrix3=now_matrix2.replace('[size=22]cofactor[/size]','.cofactor_matrix()')
                k=len(now_matrix3)
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+now_matrix3+self.ids.txt1.text[l:]
                self.ids.txt1.cursor=self.ids.txt1.get_cursor_from_index(l+k)
                
            elif z=='≤' or z=='≥': 
                l=self.ids.txt1.cursor_index()
                if z=='≤':
                    self.ids.txt1.text = self.ids.txt1.text[:l]+'<='+self.ids.txt1.text[l:] 
                elif z=='≥':
                    self.ids.txt1.text = self.ids.txt1.text[:l]+'>='+self.ids.txt1.text[l:]
                self.ids.txt1.cursor=self.ids.txt1.get_cursor_from_index(l+2) 
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)
            elif z=='&bl;':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'['+self.ids.txt1.text[l:]
                self.ids.txt1.cursor=self.ids.txt1.get_cursor_from_index(l+1)

            elif z=='∫⬚dx':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'integrate(f, x'+self.ids.txt1.text[l:]
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]integrate[/color](cos(x), x) || [color=#4F49FF]integrate[/color](cos(y), (y,0,pi))')
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]integrate[/color](cos(x), x) || [color=#4F49FF]integrate[/color](cos(y), (y,0,pi))'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)
            elif z=='[u] d⬚[/u] \n dx':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'diff(f, x'+self.ids.txt1.text[l:]
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]diff[/color](x+2, x) || [color=#4F49FF]diff[/color](cos(x), x, 2)')
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]diff[/color](x+2, x) || [color=#4F49FF]diff[/color](cos(x), x, 2)'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)
            elif z=='lim\n[sup] x → ⬚[/sup]':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+"limit(f, x, 0, '+'"+self.ids.txt1.text[l:]
                type_hint_text.clear()
                type_hint_text.append("Sample: [color=#4F49FF]limit[/color](sin(x), x, 1) || [color=#4F49FF]limit[/color](y+2, y, 2, '+')")
                self.ids.keyboard_hint.text="Sample: [color=#4F49FF]limit[/color](sin(x), x, 1) || [color=#4F49FF]limit[/color](y+2, y, 2, '+')"
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)
            elif z=='[size=54]∑[/size]⬚':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'sum(i, (i,0,5)'+self.ids.txt1.text[l:]
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]sum[/color](i×sin(x), (i, 0, 5))')
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]sum[/color](i×sin(x), (i, 0, 5))'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)
            elif z=='[sup]⎡1 0 0⎤\n⎢0 1 0⎟\n⎣0 0 1⎦[/sup]':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'Matrix([ [a,b], [c,d] ]'+self.ids.txt1.text[l:]
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]Matrix[/color]([ [1,2], [2,3] ])[color=#4F49FF].det()[/color]')
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]Matrix[/color]([ [1,2], [2,3] ])[color=#4F49FF].det()[/color]'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)
            elif z=='∇[i]f[/i]':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'grad(x×y×z'+self.ids.txt1.text[l:]
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]grad[/color](4×x - y×z^3)')
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]grad[/color](4×x - y×z^3)'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)
            elif z=='∇•[i]f[/i]':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'div(x×i + y×j + z×k'+self.ids.txt1.text[l:]
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]div[/color](x×i + y×j + z×k)')
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]grad[/color](4×x - y×z^3)'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)
            elif z=='∇×[i]f[/i]':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'curl(x×i + y×j + z×k'+self.ids.txt1.text[l:]
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]curl[/color](x×i + y×j + z×k)')
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]grad[/color](4×x - y×z^3)'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)

            elif z=='∞':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'oo'+self.ids.txt1.text[l:]
                self.ids.txt1.cursor=self.ids.txt1.get_cursor_from_index(l+2)
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)

            elif z=='[size=51]∑[/size][size=29]f(⬚)[/size]':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'series(f, x, a, b'+self.ids.txt1.text[l:]
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]series[/color](sin(x), x, -pi, pi)') 
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]series[/color](sin(x), x, -pi, pi)'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)
            elif z=='[size=30]exp(⬚)[/size]':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'exp('+self.ids.txt1.text[l:]
                self.ids.txt1.cursor=self.ids.txt1.get_cursor_from_index(l+4)
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]exp[/color](x)') 
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]exp[/color](x)'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)
            elif z=='⎛n⎞\n⎝k⎠':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'binomial('+self.ids.txt1.text[l:]
                self.ids.txt1.cursor=self.ids.txt1.get_cursor_from_index(l+9)
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]binomial[/color](n, k) || [color=#4F49FF]binomial[/color](5, 3)')
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]binomial[/color](n, k) || [color=#4F49FF]binomial[/color](5, 3)'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)
            elif z=='log[sub]⬚[/sub]⬚':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'log('+self.ids.txt1.text[l:]
                self.ids.txt1.cursor=self.ids.txt1.get_cursor_from_index(l+4)
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]log[/color](x, base) || [color=#4F49FF]log[/color](16, 2)')
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]log[/color](x, base) || [color=#4F49FF]log[/color](16, 2)'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)
            elif z=='ln⬚':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'ln('+self.ids.txt1.text[l:]
                self.ids.txt1.cursor=self.ids.txt1.get_cursor_from_index(l+3)
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]log[/color](x, base=e) || [color=#4F49FF]ln[/color](2) or [color=#4F49FF]log[/color](2)')
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]log[/color](x, base=e) || [color=#4F49FF]ln[/color](2) or [color=#4F49FF]log[/color](2)'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)

            elif z=='|⬚|':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'Abs('+self.ids.txt1.text[l:]
                self.ids.txt1.cursor=self.ids.txt1.get_cursor_from_index(l+4)
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]Abs[/color](-5)')
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]Abs[/color](-5)'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)
            elif z=='[sup]⬚[/sup]√⬚':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'root('+self.ids.txt1.text[l:]
                self.ids.txt1.cursor=self.ids.txt1.get_cursor_from_index(l+5)
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]root[/color](x, rank) || [color=#4F49FF]root[/color](8, 3)')
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]root[/color](x, rank) || [color=#4F49FF]root[/color](8, 3)'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)
            elif z=='Z[sup] *[/sup]':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'conjugate('+self.ids.txt1.text[l:]
                self.ids.txt1.cursor=self.ids.txt1.get_cursor_from_index(l+10)
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]conjugate[/color](a + bi) || [color=#4F49FF]conjugate[/color](3 + 2×i)')
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]conjugate[/color](a + bi) || [color=#4F49FF]conjugate[/color](3 + 2×i)'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)
            elif z=='i':
                l=self.ids.txt1.cursor_index()
                if 'conjugate(' in self.ids.txt1.text:
                    self.ids.txt1.text = self.ids.txt1.text[:l]+'I'+self.ids.txt1.text[l:]
                else:
                    self.ids.txt1.text = self.ids.txt1.text[:l]+z+self.ids.txt1.text[l:]
                self.ids.txt1.cursor=self.ids.txt1.get_cursor_from_index(l+1)
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)

            elif z=='[size=23]polydiv[/size]':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'pdiv(x, x'+self.ids.txt1.text[l:]
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]pdiv[/color](dividend, divisor) | [color=#4F49FF][Out][/color](multiply, remainder)')
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]pdiv[/color](dividend, divisor) | [color=#4F49FF][Out][/color](multiply, remainder)'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)
            elif z=='[size=21]fourier\n trans.[/size]':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'fourier_transform(F, x, k'+self.ids.txt1.text[l:]
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]fourier_transform[/color](exp(-x^2), x, k)')
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]fourier_transform[/color](exp(-x^2), x, k)'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)
            elif z=='[size=21]fourier\n series[/size]':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'fourier_series(F, (x, a, b'+self.ids.txt1.text[l:]
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]fourier_series[/color](x^2, (x, -pi, -2pi))')
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]fourier_series[/color](x^2, (x, -pi, -2pi))'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)
            elif z=='gamma':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'gamma(x'+self.ids.txt1.text[l:]
                self.ids.txt1.cursor=self.ids.txt1.get_cursor_from_index(l+7)
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]gamma[/color](3)')
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]gamma[/color](3)'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)
            elif z=='zeta':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'zeta(x'+self.ids.txt1.text[l:]
                self.ids.txt1.cursor=self.ids.txt1.get_cursor_from_index(l+6)
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]zeta[/color](2)')
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]zeta[/color](2)'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)
            elif z=='[size=26]jacobi[/size]':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'jacobi(n, a, b, x'+self.ids.txt1.text[l:]
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]jacobi[/color](0, a, b, x)')
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]jacobi[/color](0, a, b, x)'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)
            elif z=='[size=24]legendre[/size]':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'legendre(n, x'+self.ids.txt1.text[l:]
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]legendre[/color](2, x)')
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]legendre[/color](2, x)'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)
            elif z=='[size=16]ass.legendre[/size]':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'assoc_legendre(n, m, x'+self.ids.txt1.text[l:]
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]assoc_legendre[/color](0, 0, x)')
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]assoc_legendre[/color](0, 0, x)'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)
            elif z=='[size=24]hermite[/size]':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'hermite(n, x'+self.ids.txt1.text[l:]
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]hermite[/color](3, x)')
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]hermite[/color](3, x)'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)
            elif z=='[size=22]laguerre[/size]':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'laguerre(n, x'+self.ids.txt1.text[l:]
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]laguerre[/color](2, x)')
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]laguerre[/color](2, x)'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)
            elif z=='[size=16]ass.laguerre[/size]':
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+'assoc_laguerre(n, a, x'+self.ids.txt1.text[l:]
                type_hint_text.clear()
                type_hint_text.append('Sample: [color=#4F49FF]assoc_laguerre[/color](0, a, x)')
                self.ids.keyboard_hint.text='Sample: [color=#4F49FF]assoc_laguerre[/color](0, a, x)'
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)

            elif z=='[size=21][color=#173EFF]specaial\n func.[/color][/size]':
                specialfunc_keyboard={'b1': ('[color=#5A75FF]∫ dx[/color]','#FFFFFF'), 'b2':('abc','#EEEEEE'), 'b3':('[size=32]trigo∆[/size]','#EEEEEE'), 'b4':('[size=72]←[/size]','#EEEEEE'), 
                'b5':('[size=72]→[/size]','#EEEEEE'), 'b6':('[size=76]⌫[/size]','#EEEEEE'), 'b7':('gamma','#DEDEDE'), 'b8':('zeta','#DEDEDE'),'b9':('[size=26]jacobi[/size]','#DEDEDE'),
                'b10':('[size=24]legendre[/size]','#DEDEDE'),'b11':('[size=16]ass.legendre[/size]','#DEDEDE'),'b12':('[size=24]hermite[/size]','#DEDEDE'),'b13':('[size=22]laguerre[/size]','#DEDEDE'), 'b14':('[size=16]ass.laguerre[/size]','#DEDEDE'),
                'b15':('','F6F6F6'),'b16':('','F6F6F6'),'b17':('','F6F6F6'), 'b18':('','F6F6F6'),'b19':('','F6F6F6'),'b20':('','F6F6F6'),
                'b21':('','F6F6F6'), 'b22':('','F6F6F6'),'b23':('','F6F6F6'),'b24':('','F6F6F6'),'b25':('','F6F6F6'), 'b26':('','F6F6F6'),
                'b27':('','F6F6F6'),'b28':('','F6F6F6'),'b29':('','F6F6F6'), 'b30':('','F6F6F6')}

                mykeyboard_keys.update(specialfunc_keyboard)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus()

            elif z=='[size=19][color=#173EFF]Matrix\n operators[/color][/size]':
                matrix_keyboard={'b1': ('[color=#5A75FF]∫ dx[/color]','#FFFFFF'), 'b2':('abc','#EEEEEE'), 'b3':('[size=32]trigo∆[/size]','#EEEEEE'), 'b4':('[size=72]←[/size]','#EEEEEE'), 
                'b5':('[size=72]→[/size]','#EEEEEE'), 'b6':('[size=76]⌫[/size]','#EEEEEE'), 'b7':('det','#DEDEDE'), 'b8':('[size=20]transpose[/size]','#DEDEDE'),'b9':('[size=22]inverse[/size]','#DEDEDE'),
                'b10':('[size=16]eigenvalues[/size]','#DEDEDE'),'b11':('[size=16]eigenvectors[/size]','#DEDEDE'),'b12':('[size=22]cofactor[/size]','#DEDEDE'),'b13':('[size=22]echolon[/size]','#DEDEDE'), 'b14':('rank','#DEDEDE'),
                'b15':('','F6F6F6'),'b16':('','F6F6F6'),'b17':('','F6F6F6'), 'b18':('','F6F6F6'),'b19':('','F6F6F6'),'b20':('','F6F6F6'),
                'b21':('','F6F6F6'), 'b22':('','F6F6F6'),'b23':('','F6F6F6'),'b24':('','F6F6F6'),'b25':('','F6F6F6'), 'b26':('','F6F6F6'),
                'b27':('','F6F6F6'),'b28':('','F6F6F6'),'b29':('','F6F6F6'), 'b30':('','F6F6F6')}

                mykeyboard_keys.update(matrix_keyboard)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus()

            elif z=='[color=#173EFF]< >[/color]': 
                bigger_keyboard={'b1': ('[color=#5A75FF]∫ dx[/color]','#FFFFFF'), 'b2':('abc','#EEEEEE'), 'b3':('[size=32]trigo∆[/size]','#EEEEEE'), 'b4':('[size=72]←[/size]','#EEEEEE'), 
                'b5':('[size=72]→[/size]','#EEEEEE'), 'b6':('[size=76]⌫[/size]','#EEEEEE'), 'b7':('>','#DEDEDE'), 'b8':('<','#DEDEDE'),'b9':('≥','#DEDEDE'),
                'b10':('≤','#DEDEDE'),'b11':('','F6F6F6'),'b12':('','F6F6F6'),'b13':('','F6F6F6'), 'b14':('','F6F6F6'),
                'b15':('','F6F6F6'),'b16':('','F6F6F6'),'b17':('','F6F6F6'), 'b18':('','F6F6F6'),'b19':('','F6F6F6'),'b20':('','F6F6F6'),
                'b21':('','F6F6F6'), 'b22':('','F6F6F6'),'b23':('','F6F6F6'),'b24':('','F6F6F6'),'b25':('','F6F6F6'), 'b26':('','F6F6F6'),
                'b27':('','F6F6F6'),'b28':('','F6F6F6'),'b29':('','F6F6F6'), 'b30':('','F6F6F6')}

                mykeyboard_keys.update(bigger_keyboard)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus()

            elif z=='[color=#173EFF]∇×[i]f[/i][/color]':
                lambda_keyboard={'b1': ('[color=#5A75FF]∫ dx[/color]','#FFFFFF'), 'b2':('abc','#EEEEEE'), 'b3':('[size=32]trigo∆[/size]','#EEEEEE'), 'b4':('[size=72]←[/size]','#EEEEEE'), 
                'b5':('[size=72]→[/size]','#EEEEEE'), 'b6':('[size=76]⌫[/size]','#EEEEEE'), 'b7':('∇[i]f[/i]','#DEDEDE'), 'b8':('∇•[i]f[/i]','#DEDEDE'),'b9':('∇×[i]f[/i]','#DEDEDE'),
                'b10':('','F6F6F6'),'b11':('','F6F6F6'),'b12':('','F6F6F6'),'b13':('','F6F6F6'), 'b14':('','F6F6F6'),
                'b15':('','F6F6F6'),'b16':('','F6F6F6'),'b17':('','F6F6F6'), 'b18':('','F6F6F6'),'b19':('','F6F6F6'),'b20':('','F6F6F6'),
                'b21':('','F6F6F6'), 'b22':('','F6F6F6'),'b23':('','F6F6F6'),'b24':('','F6F6F6'),'b25':('','F6F6F6'), 'b26':('','F6F6F6'),
                'b27':('','F6F6F6'),'b28':('','F6F6F6'),'b29':('','F6F6F6'), 'b30':('','F6F6F6')}

                mykeyboard_keys.update(lambda_keyboard)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus()

            elif z=='abc' or z=='[color=#5A75FF]abc[/color]':
                global _keyboard_back
                _keyboard_back += 1
                abc_keyboard={'b1': ('∫ dx','#EEEEEE'), 'b2':('[color=#5A75FF]abc[/color]','#FFFFFF'), 'b3':('[size=32]trigo∆[/size]','#EEEEEE'), 'b4':('[size=72]←[/size]','#EEEEEE'), 
                'b5':('[size=72]→[/size]','#EEEEEE'), 'b6':('[size=76]⌫[/size]','#EEEEEE'), 'b7':('a','#DEDEDE'), 'b8':('b','#DEDEDE'),'b9':('c','#DEDEDE'),
                'b10':('d','#DEDEDE'),'b11':('e','#DEDEDE'),'b12':('f','#DEDEDE'),'b13':('g','#DEDEDE'), 'b14':('h','#DEDEDE'),
                'b15':('i','#DEDEDE'),'b16':('j','#DEDEDE'),'b17':('k','#DEDEDE'), 'b18':('m','#DEDEDE'),'b19':('n','#DEDEDE'),'b20':('p','#DEDEDE'),
                'b21':('q','#DEDEDE'), 'b22':('r','#DEDEDE'),'b23':('t','#DEDEDE'),'b24':('x','#DEDEDE'),'b25':('y','#DEDEDE'), 'b26':('z','#DEDEDE'),
                'b27':('α','#DEDEDE'),'b28':('β','#DEDEDE'),'b29':('θ','#DEDEDE'), 'b30':('φ','#DEDEDE')}

                mykeyboard_keys.update(abc_keyboard)
                if _keyboard_back >= 2 and z=='[color=#5A75FF]abc[/color]':
                    mykeyboard_keys.update(old_mykeyboard_keys)
                    _keyboard_back = 0

                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus()

            elif z=='∫ dx' or z=='[color=#5A75FF]∫ dx[/color]':  
                _keyboard_back += 1 
                calculus_keyboard={'b1': ('[color=#5A75FF]∫ dx[/color]','#FFFFFF'), 'b2':('abc','#EEEEEE'), 'b3':('[size=32]trigo∆[/size]','#EEEEEE'), 'b4':('[size=72]←[/size]','#EEEEEE'), 
                'b5':('[size=72]→[/size]','#EEEEEE'), 'b6':('[size=76]⌫[/size]','#EEEEEE'), 'b7':('∫⬚dx','#DEDEDE'), 'b8':('[u] d⬚[/u] \n dx','#DEDEDE'),'b9':('lim\n[sup] x → ⬚[/sup]','#DEDEDE'),
                'b10':('[size=54]∑[/size]⬚','#DEDEDE'),'b11':('[sup]⎡1 0 0⎤\n⎢0 1 0⎟\n⎣0 0 1⎦[/sup]','#DEDEDE'),'b12':('[color=#173EFF]∇×[i]f[/i][/color]','#DEDEDE'),'b13':('[color=#173EFF]< >[/color]','#DEDEDE'), 'b14':('∞','#DEDEDE'),
                'b15':('[size=51]∑[/size][size=29]f(⬚)[/size]','#DEDEDE'),'b16':('[size=30]exp(⬚)[/size]','#DEDEDE'),'b17':('ln⬚','#DEDEDE'), 'b18':('log[sub]⬚[/sub]⬚','#DEDEDE'),'b19':('!','#DEDEDE'),'b20':('|⬚|','#DEDEDE'),
                'b21':('[sup]⬚[/sup]√⬚','#DEDEDE'), 'b22':('⎛n⎞\n⎝k⎠','#DEDEDE'),'b23':('&bl;','#DEDEDE'),'b24':(']','#DEDEDE'),'b25':('Z[sup] *[/sup]','#DEDEDE'), 'b26':('[size=19][color=#173EFF]Matrix\n operators[/color][/size]','#DEDEDE'),
                'b27':('[size=23]polydiv[/size]','#DEDEDE'),'b28':('[size=21]fourier\n series[/size]','#DEDEDE'),'b29':('[size=21]fourier\n trans.[/size]','#DEDEDE'), 'b30':('[size=21][color=#173EFF]specaial\n func.[/color][/size]','#DEDEDE')}
     
                mykeyboard_keys.update(calculus_keyboard)
                if _keyboard_back >= 2 and z=='[color=#5A75FF]∫ dx[/color]':
                    mykeyboard_keys.update(old_mykeyboard_keys)
                    _keyboard_back = 0

                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus()

            elif z=='[size=32]trigo∆[/size]' or z=='[color=#5A75FF][size=32]trigo∆[/size][/color]':
                _keyboard_back += 1
                trygonometry_keyboard={'b1': ('∫ dx','#EEEEEE'), 'b2':('abc','#EEEEEE'), 'b3':('[color=#5A75FF][size=32]trigo∆[/size][/color]','#FFFFFF'), 'b4':('[size=72]←[/size]','#EEEEEE'), 
                'b5':('[size=72]→[/size]','#EEEEEE'), 'b6':('[size=76]⌫[/size]','#EEEEEE'), 'b7':('sin','#DEDEDE'), 'b8':('cos','#DEDEDE'),'b9':('tan','#DEDEDE'),
                'b10':('cot','#DEDEDE'),'b11':('sec','#DEDEDE'),'b12':('csc','#DEDEDE'),'b13':('sinc','#DEDEDE'), 'b14':('asin','#DEDEDE'),
                'b15':('acos','#DEDEDE'),'b16':('atan','#DEDEDE'),'b17':('acot','#DEDEDE'), 'b18':('asec','#DEDEDE'),'b19':('acsc','#DEDEDE'),'b20':('asinc','#DEDEDE'),
                'b21':('sinh','#DEDEDE'), 'b22':('cosh','#DEDEDE'),'b23':('tanh','#DEDEDE'),'b24':('coth','#DEDEDE'),'b25':('[size=30]asinh[/size]','#DEDEDE'), 'b26':('[size=30]acosh[/size]','#DEDEDE'),
                'b27':('[size=30]atanh[/size]','#DEDEDE'),'b28':('[size=30]acoth[/size]','#DEDEDE'),'b29':('','F6F6F6'), 'b30':('','F6F6F6')}

                mykeyboard_keys.update(trygonometry_keyboard)
                if _keyboard_back >= 2 and z=='[color=#5A75FF][size=32]trigo∆[/size][/color]':
                    mykeyboard_keys.update(old_mykeyboard_keys)
                    _keyboard_back = 0
                                                
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus()

            elif mykeyboard_keys['b2']==('[color=#5A75FF]abc[/color]','#FFFFFF'):
              #re-back normal keyboard to type anything!
                l=self.ids.txt1.cursor_index()
                self.ids.txt1.text = self.ids.txt1.text[:l]+z+self.ids.txt1.text[l:]
                self.ids.txt1.cursor=self.ids.txt1.get_cursor_from_index(l+1)
                mykeyboard_keys.update(old_mykeyboard_keys)
                return self.ids.box_layout.remove_widget(artifical_keyboard), self.checkfocus(), self.pretty_symbols(a=first_text_check_for_pretty,b=self.ids.txt1.text)

            else: 
                l=self.ids.txt1.cursor_index()  
                self.ids.txt1.text = self.ids.txt1.text[:l]+z+self.ids.txt1.text[l:]
                self.ids.txt1.cursor = self.ids.txt1.get_cursor_from_index(l+1)          

            end_text_check_for_pretty=self.ids.txt1.text

            return self.pretty_symbols(a=first_text_check_for_pretty, b=end_text_check_for_pretty)
        except(Exception):
            self.ids.lbl0.text='Accurred unknown vMath keyboard error'
            self.ids.lbl1.text=''       

    def pretty_symbols(self, a, b):
        try:
            j=self.ids.txt1.cursor_index()                                          
            le1=len(a)
            le2=len(b)                                               
            le=le2-le1
            if le>0 and (self.ids.txt1.text[le1-1] in pretty_symb[55:] and self.ids.txt1.text[le1:] in pretty_symb[:55] and j>1 #xcos()..falan olmuyor!
                or (self.ids.txt1.text[j-le-1] in pretty_symb[22:46] and (self.ids.txt1.text[j-le:] in pretty_symb[:22] or self.ids.txt1.text[j-le:] in pretty_symb[47:55]))
                or (self.ids.txt1.text[le1-1]==')' and (self.ids.txt1.text[le1:] in pretty_symb or self.ids.txt1.text[le1:]=='('))
                or (self.ids.txt1.text[le1-1] in pretty_symb and self.ids.txt1.text[le1:]=='(')) and le2 == j:
                self.ids.txt1.text = self.ids.txt1.text[:le1]+'×'+self.ids.txt1.text[le1:]
            
            elif le2 != j and j>1:          
                if (self.ids.txt1.text[j-le-1] in pretty_symb[55:] and self.ids.txt1.text[j-le] in pretty_symb[:55] 
                or (self.ids.txt1.text[j-le-1] in pretty_symb[22:46] and (self.ids.txt1.text[j-le:j] in pretty_symb[:22] or self.ids.txt1.text[j-le:j] in pretty_symb[47:55])) #arg x sqrt(...
                or (self.ids.txt1.text[j-2]==')' and (self.ids.txt1.text[j-1] in pretty_symb or self.ids.txt1.text[j-1]=='(')) 
                or (self.ids.txt1.text[j-2] in pretty_symb and self.ids.txt1.text[j-1]=='(' 
                    and ((self.ids.txt1.text[j-3] not in pretty_symb[22:46] and self.ids.txt1.text[j-3] !='u') and self.ids.txt1.text[j-2] not in pretty_symb[22:31]))):
                    self.ids.txt1.text = self.ids.txt1.text[:j-le]+'×'+self.ids.txt1.text[j-le:]
                    l=self.ids.txt1.cursor_index()
                    k=len(self.ids.txt1.text[j-1:])
                    self.ids.txt1.cursor = self.ids.txt1.get_cursor_from_index(l-k+2)
            else:
                pass
        except(Exception):
            self.ids.lbl0.text='Unknown vMath checking notation error'

    def setting_keyboard(self, p):
        try:
            global artifical_keyboard
            if self.ids.keyboard_icon.icon=='keyboard' and p==1:
                self.ids.txt1.keyboard_mode='auto'
                self.ids.keyboard_icon.icon='keyboard-off' 
                self.ids.change_keyboard.secondary_text='Current: System keyboard' 
                self.ids.bulb_icon.icon='lightbulb-off' #if you use system keyboard no hint!
                self.ids.change_hint.secondary_text='Hints non-active' 
                self.ids.box_layout.remove_widget(artifical_keyboard) #delete vMath keyboard
                mykeyboard_keys.update(old_mykeyboard_keys)
            elif self.ids.keyboard_icon.icon=='keyboard-off' and p==1:
                self.ids.txt1.keyboard_mode='managed'
                self.ids.keyboard_icon.icon='keyboard' 
                self.ids.change_keyboard.secondary_text='Current: vMath keyboard'  
                self.ids.bulb_icon.icon='lightbulb' #if you use vMath keyboard call default hint
                self.ids.change_hint.secondary_text='Hints active'
            elif self.ids.bulb_icon.icon=='lightbulb' and p==2:
                self.ids.bulb_icon.icon='lightbulb-off'
                self.ids.change_hint.secondary_text='Hints non-active'
                type_hint_text.clear()
                type_hint_text.append('')
            elif self.ids.bulb_icon.icon=='lightbulb-off' and p==2:
                self.ids.bulb_icon.icon='lightbulb'
                self.ids.change_hint.secondary_text='Hints active'
            elif p==3:
                webbrowser.open('https://www.buymeacoffee.com/mathconsole')
        except(Exception):
            self.ids.txt1.keyboard_mode='auto'

    def fallow_text(self):    
        main_sign1=self.ids.txt1.text.replace("×","*")
        main_sign2=main_sign1.replace("÷","/")
        try:
            self.ids.lblcol.text=" "
            self.ids.lbl_blue.text="[Out]"  
                            
            if len(img_data)>0: 
                if (img_data.count('2'))>0:
                    self.ids.box_layout.remove_widget(self.ids.button_steps)
                else:
                    self.ids.box_layout.remove_widget(self.ids.img_box)
                img_data.clear()       
                
            data=main_sign2
            sign0=sympify(data)
            sign_str=pretty(simplify(str(sign0)))    
            sign_exp=sign_str.replace("ℯ","e") 
            self.ids.lbl1.text=sign_exp
            sign1=main_sign2.replace("diff","Derivative")
            sign2=sign1.replace("integrate","Integral")
            sign3=sign2.replace("limit","Limit")                
            sign4=sign3.replace("factor","")
            sign5=sign4.replace("expand","")
            sign6=sign5.replace("simplify","")
            sign7=sign6.replace("LC","")
            sign8=sign7.replace("discriminant","")
            sign9=sign8.replace("degree","")
            sign10=sign9.replace("degree_list","")
            sign11=sign10.replace("im(","(")
            sign12=sign11.replace("re(","(")
            sign13=sign12.replace(".evalf()","")
             
            signs=pretty(sympify(sign13,evaluate=False)) 
            sign_exp_expr=signs.replace("ℯ","e")
            self.ids.lbl0.text=sign_exp_expr
                                   
        except(SympifyError,Exception):
            if self.ids.txt1.text!="":
                self.ids.lbl0.text="typing..."
                self.ids.lbl1.text="waiting..."
                self.ids.lblcol.text=""
            elif self.ids.txt1.text=="":
                self.ids.lbl0.text=""
                self.ids.lbl1.text=""
                self.ids.lblcol.text=""
                self.ids.lblcol.background_color=(0,0,0,0)
                      
        def other_mathematics(self):
            try:
                
                if "gamma(" in self.ids.txt1.text and self.ids.txt1.text[-1]==")":
                    status=main_sign2.replace("gamma","Gamma")
                    expr_gamma=sympify(status,evaluate=False)
                    data=sympify(main_sign2)

                    self.ids.lbl1.text=pretty(data)
                    self.ids.lbl0.text=pretty(expr_gamma)

                elif "zeta(" in self.ids.txt1.text and self.ids.txt1.text[-1]==")":
                    status=main_sign2.replace("zeta","Zeta")
                    expr_zeta=sympify(status,evaluate=False)
                    data=sympify(main_sign2)

                    self.ids.lbl1.text=pretty(data)
                    self.ids.lbl0.text=pretty(expr_zeta)

                elif "jacobi(" in self.ids.txt1.text and self.ids.txt1.text[-1]==")":
                    status=main_sign2.replace("jacobi","Jacobi")
                    expr_jacobi=sympify(status,evaluate=False)
                    data=sympify(main_sign2)

                    self.ids.lbl1.text=pretty(data)
                    self.ids.lbl0.text=pretty(expr_jacobi)

                elif "legendre(" in self.ids.txt1.text and "assoc_legendre" not in self.ids.txt1.text and self.ids.txt1.text[-1]==")":
                    status=main_sign2.replace("legendre","Legendre")
                    expr_legendre=sympify(status,evaluate=False)
                    data=sympify(main_sign2)

                    self.ids.lbl1.text=pretty(data)
                    self.ids.lbl0.text=pretty(expr_legendre)

                elif "assoc_legendre(" in self.ids.txt1.text and self.ids.txt1.text[-1]==")":
                    status=main_sign2.replace("assoc_legendre","As_Legendre")
                    expr_aslegendre=sympify(status,evaluate=False)
                    data=sympify(main_sign2)

                    self.ids.lbl1.text=pretty(data)
                    self.ids.lbl0.text=pretty(expr_aslegendre)

                elif "hermite(" in self.ids.txt1.text and self.ids.txt1.text[-1]==")":
                    status=main_sign2.replace("hermite","H")
                    expr_hermite=sympify(status,evaluate=False)
                    data=sympify(main_sign2)

                    self.ids.lbl1.text=pretty(data)
                    self.ids.lbl0.text=pretty(expr_hermite)

                elif "laguerre(" in self.ids.txt1.text and "assoc_laguerre(" not in self.ids.txt1.text and self.ids.txt1.text[-1]==")":
                    status=main_sign2.replace("laguerre","L")
                    expr_laguerre=sympify(status,evaluate=False)
                    data=sympify(main_sign2)

                    self.ids.lbl1.text=pretty(data)
                    self.ids.lbl0.text=pretty(expr_laguerre)

                elif "assoc_laguerre(" in self.ids.txt1.text and self.ids.txt1.text[-1]==")": 
                    status=main_sign2.replace("assoc_laguerre","As_L")
                    expr_aslaguerre=sympify(status,evaluate=False)
                    data=sympify(main_sign2)

                    self.ids.lbl1.text=pretty(data)
                    self.ids.lbl0.text=pretty(expr_aslaguerre)

                elif "fourier_series(" in self.ids.txt1.text and self.ids.txt1.text[-1]==")":
                    self.ids.lblcol.text=" "
                    fourier_expr=sympify(main_sign2)
                    exp_sign=pretty(fourier_expr).replace("ℯ","e")
                    self.ids.lbl1.text=exp_sign
                    
                    apart_dot=main_sign2.split(",")
                    expr_apart=apart_dot[0].replace("fourier_series(","") 
                    expr_out1=sympify(expr_apart,evaluate=False)
                    expr_out2=pretty(expr_out1).replace("ℯ","e")
                    
                    self.ids.lbl0.text=expr_out2+"  Fourierseries"

                elif "fourier_transform(" in self.ids.txt1.text  and self.ids.txt1.text[-1]==")":
                    fourier_expr=sympify(main_sign2)
                    exp_sign=pretty(fourier_expr).replace("ℯ","e") #here --add help
                    self.ids.lbl1.text=exp_sign
                    
                    apart_dot=main_sign2.split(",")
                    expr_apart=apart_dot[0].replace("fourier_transform(","")
                    expr_out1=sympify(expr_apart,evaluate=False)
                    expr_out2=pretty(expr_out1).replace("ℯ","e")
                    
                    self.ids.lbl0.text=expr_out2+"  Fouriertransform"

                elif "series(" in self.ids.txt1.text and self.ids.txt1.text[-1]==")":
                    series_expr=sympify(main_sign2)
                    exp_sign=pretty(series_expr).replace("ℯ","e")
                    self.ids.lbl1.text=exp_sign
                    
                    apart_dot=main_sign2.split(",")
                    expr_apart=apart_dot[0].replace("series(","")
                    expr_out1=sympify(expr_apart,evaluate=False)
                    expr_out2=pretty(expr_out1).replace("ℯ","e")
                    
                    self.ids.lbl0.text=expr_out2+"  Series"

                elif "Matrix([" in self.ids.txt1.text and ".eigenvects()" in self.ids.txt1.text: 
                    data=main_sign2
                    sign0=sympify(data)
                    self.ids.lblcol.text=" "
                    sign1=str(sign0).replace("1, [","λ, [")
                    sign2=sign1.replace("2, [","λ_12, [") 
                    sign3=sign2.replace("3, [","λ_123, [") 
                    sign4=sign3.replace("4, [","λ_1234, [")
                    sign5=sign4.replace("5, [","λ_12345, [")

                    exp_sign_matrix=pretty(sympify(sign5)).replace("ℯ","e")
                    
                    sign_str=exp_sign_matrix
                    self.ids.lbl1.text=sign_str
                        
                    expr_vals=data.replace(".eigenvects()","")
                    exp_sign_matrix_expr=pretty(sympify(expr_vals,evaluate=False)).replace("ℯ","e")
                    pre_expr=exp_sign_matrix_expr
                    self.ids.lbl0.text=pre_expr

                elif "Matrix([" in self.ids.txt1.text and ".eigenvals()" in self.ids.txt1.text:  
                    data=main_sign2
                    sign0=sympify(data)
        
                    sign1=str(sign0).replace(": 1",": λ")
                    sign2=sign1.replace(": 2",": λ_12") 
                    sign3=sign2.replace(": 3",": λ_123")
                    sign4=sign3.replace(": 4",": λ_1234")
                    sign5=sign4.replace(": 5",": λ_12345")
                    
                    exp_sign_matrix=pretty(sympify(sign5)).replace("ℯ","e")
                    self.ids.lbl1.text=exp_sign_matrix
                        
                    expr_vals=data.replace(".eigenvals()","")
                    
                    exp_sign_matrix_expr=pretty(sympify(expr_vals,evaluate=False)).replace("ℯ","e")
                    pre_expr=exp_sign_matrix_expr
                    self.ids.lbl0.text=pre_expr

                elif "Matrix([" in self.ids.txt1.text and ".eigenvects()" not in self.ids.txt1.text and ".eigenvals()" not in self.ids.txt1.text:
                    expr1=main_sign2.replace(".det()","") 
                    expr2=expr1.replace(".T","")
                    expr3=expr2.replace(".cofactor()","")
                    expr4=expr3.replace(".cofactor_matrix()","")
                    expr5=expr4.replace(".minor()","")
                    expr6=expr5.replace(".echelon_form()","")
                    expr7=expr6.replace(".rank()","")
                    expr8=expr7.replace("diff","Derivative")
                    expr9=expr8.replace("integrate","Integral")
                    expr10=expr9.replace("limit","Limit")
                    expr11=expr10.replace(".inv()","")

                    data=sympify(main_sign2)
                    pre_expr=pretty(data).replace("ℯ","e")
                    self.ids.lbl1.text=pre_expr

                    expr_in=sympify(expr11,evaluate=False)
                    expr_sign_matrix=pretty(expr_in).replace("ℯ","e")
                    self.ids.lbl0.text=expr_sign_matrix
                
                elif "sum(" in self.ids.txt1.text and self.ids.txt1.text[-1]==")":
                    self.ids.lblcol.text=" "
                    expr_out1=main_sign2.replace("sum","Sum")
                    sum_expr=sympify(expr_out1).doit()
                    exp_sign=pretty(sum_expr).replace("ℯ","e") 
                    self.ids.lbl1.text=exp_sign
                    
                    expr_out2=pretty(sympify(expr_out1)).replace("ℯ","e")
                    self.ids.lbl0.text=expr_out2

                elif ">=" in self.ids.txt1.text or "<=" in self.ids.txt1.text:
                
                    solve_expr=sympify(main_sign2)
                    data=solve(solve_expr)
                    
                    out_display=pretty(simplify(str(data)))

                    fix_sign1=out_display.replace("∧","∩")  
                    fix_sign2=fix_sign1.replace("∨","∪")
                    fix_sign3=fix_sign2.replace("ℯ","e")
                    self.ids.lbl1.text=fix_sign3      
                    eq_exp=pretty(sympify(main_sign2,evaluate=False)).replace("ℯ","e")
                    self.ids.lbl0.text=pretty(eq_exp)         
                
                elif "=" in self.ids.txt1.text and (">" not in self.ids.txt1.text or "<" not in self.ids.txt1.text):
                    self.ids.lblcol.text=" "
                    apart=main_sign2.split("=")
                    expr1=sympify(apart[0])
                    expr2=sympify(apart[1])
                    solve_expr=sympify(expr1-expr2)
                    if 'diff(' in self.ids.txt1.text:
                        for b in solve_expr.atoms(Function):
                            count_b = str(b).count(',')
                        if count_b>0:
                            data=pdsolve(solve_expr)
                        else:
                            data=dsolve(solve_expr)
                    else:
                        data=solve(solve_expr)
                    
                    out_display=pretty(data)
                    out_exp=out_display.replace("ℯ","e")
                    self.ids.lbl1.text=out_exp
                    
                    in_display1=sympify(apart[0],evaluate=False)
                    in_display2=sympify(apart[1],evaluate=False)
                    
                    find_pow=apart[1].count("^")
                    find_divide=apart[1].count("/") 
                    find_exp=apart[1].count("exp(")
                
                    if find_pow>0 or find_divide>0 or find_exp>0:
                        fix_equ=sympify((apart[0]+"-"+apart[1]),evaluate=False)
                        fix_exp=pretty(fix_equ).replace("ℯ","e")
                        self.ids.lbl0.text=pretty(fix_exp)+" = 0"
                    
                    else:
                        fix_exp=pretty(in_display1).replace("ℯ","e")
                        fix_exp1=pretty(in_display2).replace("ℯ","e")
                        self.ids.lbl0.text=pretty(fix_exp)+" = "+pretty(fix_exp1)
       
                elif ("<" in self.ids.txt1.text or '>' in self.ids.txt1.text) and '=' not in self.ids.txt1.text:
                    solve_expr=sympify(main_sign2)
                    data=solve(solve_expr)
                    
                    out_display=pretty(simplify(str(data)))

                    fix_sign1=out_display.replace("∧","∩") 
                    fix_sign2=fix_sign1.replace("∨","∪")
                    fix_sign3=fix_sign2.replace("ℯ","e")
                    self.ids.lbl1.text=fix_sign3   
                    eq_exp=pretty(sympify(main_sign2,evaluate=False)).replace("ℯ","e")
                    self.ids.lbl0.text=pretty(eq_exp)
                    
                elif "curl(" in self.ids.txt1.text and ("i" in self.ids.txt1.text or "j" in self.ids.txt1.text or "k" in self.ids.txt1.text) and self.ids.txt1.text[-1]==")":
                        
                    div_del=main_sign2.replace("curl","")
                    div_expr=collect(sympify(div_del),(i,j,k))
                    div_x=diff(div_expr*i,x)
                    div_y=diff(div_expr*j,y) 
                    div_z=diff(div_expr*k,z)

                    divx_expand=expand(div_x)
                    divx_step1=str(divx_expand).replace("i*k","-j")
                    divx_step2=divx_step1.replace("i**2","0")
                    divx_step3=divx_step2.replace("i*j","k") 
                    divx_step4=divx_step3.replace("i","0")
                    div_sin=divx_step4.replace("s0n","sin")
                    div_phi=div_sin.replace("ph0","phi")
                    Div_x=sympify(div_phi)

                    div_expand=expand(div_y)
                    divy_step1=str(div_expand).replace("i*j","-k")
                    divy_step2=divy_step1.replace("j**2","0")
                    divy_step3=divy_step2.replace("j*k","i") 
                    divy_step4=divy_step3.replace("j","0") 
                    Div_y=sympify(divy_step4)

                    divz_expand=expand(div_z)
                    divz_step1=str(divz_expand).replace("i*k","j")
                    divz_step2=divz_step1.replace("k**2","0")
                    divz_step3=divz_step2.replace("j*k","-i") 
                    divz_step4=divz_step3.replace("k","0") 
                    Div_z=sympify(divz_step4)

                    rdiv=collect(sympify(Div_x+Div_y+Div_z),(i,j,k))  

                    editx1=pretty(rdiv)
                    editx2=editx1.replace("i","[color=#000000]i[/color]")
                    editx3=editx2.replace("j","[color=#000000]j[/color]")
                    editx4=editx3.replace("k","[color=#000000]k[/color]")
                    editx5=editx4.replace("s[color=#000000]i[/color]n","[color=#0000FF]sin[/color]")
                    editx6=editx5.replace("ℯ","e")

                    expr_print=sympify(div_del,evaluate=False)
                    edit1=pretty(expr_print)
                    edit2=edit1.replace("i","[color=#002BFF]i[/color]")
                    edit3=edit2.replace("j","[color=#002BFF]j[/color]")
                    edit4=edit3.replace("k","[color=#002BFF]k[/color]")
                    edit5=edit4.replace("s[color=#002BFF]i[/color]n","[color=#000000]sin[/color]")
                    edit6=edit5.replace("ℯ","e")
            
                    pre_expr=edit6+" × [color=#002BFF]∇[/color]" 
                
                    self.ids.lbl0.text=pre_expr
                    self.ids.lbl1.text=editx6
                    
                elif "pdiv" in self.ids.txt1.text and self.ids.txt1.text[-1]==")":
                    pol_div=main_sign2.replace("pdiv","")   
                    pol_div1=pol_div.split(",")
                    pol_div2=sympify(pol_div1[0]+")")
                    pol_div3=sympify("("+pol_div1[-1])
                    pol_expr=sympify((pol_div2/pol_div3),evaluate=False)
                    pol_data=sympify(main_sign2)
                    
                    fix_sign_exp=pretty(pol_data).replace("ℯ","e")
                    fix_sign_exp1=pretty(pol_expr).replace("ℯ","e")
                    
                    self.ids.lbl0.text=fix_sign_exp1
                    self.ids.lbl1.text=pretty(fix_sign_exp)

                elif "div(" in self.ids.txt1.text and (self.ids.txt1.text.count("i")>1 or "j" in self.ids.txt1.text or "k" in self.ids.txt1.text) and (self.ids.txt1.text[-1]==")" and "pdiv" not in self.ids.txt1.text):
                    self.ids.lblcol.text=" "
                    div_del=main_sign2.replace("div","")
                    div_expr=collect(sympify(div_del),(i,j,k)) 
                    div_x=diff(div_expr*i,x)
                    div_y=diff(div_expr*j,y) 
                    div_z=diff(div_expr*k,z)

                    divx_expand=expand(div_x)
                    divx_step1=str(divx_expand).replace("i**2","1")
                    divx_step2=divx_step1.replace("i*j","0")
                    divx_step3=divx_step2.replace("i*k","0") 
                    divx_step4=divx_step3.replace("i","0")
                    div_sin=divx_step4.replace("s0n","sin")
                    div_phi=div_sin.replace("ph0","phi")
                    Div_x=sympify(div_phi)
    
                    div_expand=expand(div_y)
                    divy_step1=str(div_expand).replace("j**2","1")
                    divy_step2=divy_step1.replace("i*j","0")
                    divy_step3=divy_step2.replace("j*k","0")
                    divy_step4=divy_step3.replace("j","0") 
                    Div_y=sympify(divy_step4)

                    divz_expand=expand(div_z)
                    divz_step1=str(divz_expand).replace("k**2","1")
                    divz_step2=divz_step1.replace("i*k","0")
                    divz_step3=divz_step2.replace("j*k","0")
                    divz_step4=divz_step3.replace("k","0") 
                    Div_z=sympify(divz_step4)

                    rdiv=sympify(Div_x+Div_y+Div_z)  

                    editx1=pretty(rdiv)
                    editx2=editx1.replace("i","[color=#000000]i[/color]")
                    editx3=editx2.replace("j","[color=#000000]j[/color]")
                    editx4=editx3.replace("k","[color=#000000]k[/color]")
                    editx5=editx4.replace("s[color=#000000]i[/color]n","[color=#0000FF]sin[/color]")
                    editx6=editx5.replace("ℯ","e")
                    
                    expr_print=sympify(div_del,evaluate=False)
                    edit1=pretty(expr_print)
                    edit2=edit1.replace("i","[color=#002BFF]i[/color]")                  
                    edit3=edit2.replace("j","[color=#002BFF]j[/color]")
                    edit4=edit3.replace("k","[color=#002BFF]k[/color]")
                    edit5=edit4.replace("s[color=#002BFF]i[/color]n","[color=#000000]sin[/color]")
                    edit6=edit5.replace("ℯ","e")
            
                    pre_expr=edit6+" • [color=#002BFF]∇[/color]"
                  
                    self.ids.lbl0.text=pre_expr
                    self.ids.lbl1.text=editx6
                    
                elif "grad(" in self.ids.txt1.text and (("i" not in self.ids.txt1.text or ("sin" in self.ids.txt1.text and self.ids.txt1.text.count("i")==self.ids.txt1.text.count("sin"))) and "j" not in self.ids.txt1.text and "k" not in self.ids.txt1.text):
                    grad_del=main_sign2.replace("grad","")
                    grad_expr=sympify(grad_del)
                    grad_x=diff(grad_expr,x)
                    grad_y=diff(grad_expr,y)
                    grad_z=diff(grad_expr,z)

                    Grad=(grad_x)*i+(grad_y)*j+(grad_z)*k
                    rgrad=collect(sympify(Grad),(i,j,k))

                    editx1=pretty(rgrad)
                    editx2=editx1.replace("i","[color=#000000]i[/color]")
                    editx3=editx2.replace("j","[color=#000000]j[/color]")
                    editx4=editx3.replace("k","[color=#000000]k[/color]")
                    editx5=editx4.replace("s[color=#000000]i[/color]n","[color=#0000FF]sin[/color]")
                    editx6=editx5.replace("ℯ","e")

                    expr_print=sympify(grad_del,evaluate=False)
                    expr_sign_exp=pretty(expr_print).replace("ℯ","e")
                    pre_expr=pretty(expr_sign_exp)+" [color=#002BFF]∇[/color]"
            
                    self.ids.lbl0.text=pre_expr
                    self.ids.lbl1.text=editx6

                elif "binomial(" in self.ids.txt1.text and self.ids.txt1.text[-1]==")":
                    status=main_sign2.replace("binomial(","") 
                    status1 = status.split(',') 
                    expr_text="factorial({},evaluate=False)/(factorial({},evaluate=False)*({}-{})!)".format(status1[0],status1[1][:-1],status1[0],status1[1][:-1])      
                    expr_binomial=sympify(expr_text,evaluate=False)
                    data=sympify(main_sign2)

                    self.ids.lbl1.text=pretty(data)
                    self.ids.lbl0.text=pretty(expr_binomial)
                                                                                 #section for outo .evalf()
                elif (len(sympify(main_sign2).atoms(Number)) != 0 and len(sympify(main_sign2).atoms(Symbol)) == 0 and("exp(" in main_sign2 or 'log(' in main_sign2 or 'ln(' in main_sign2
                    or 'sqrt(' in main_sign2 or 'root(' in main_sign2 or 'pi' in main_sign2 or '/' in main_sign2) and ("integrate(" not in main_sign2 and "limit(" not in main_sign2 and "diff(" not in main_sign2)):
                    sign_str = pretty(simplify(str(main_sign2)).evalf())  
                    sign_exp=sign_str.replace("ℯ","e") 
                    self.ids.lbl1.text=sign_exp

                    signs=pretty(sympify(main_sign2,evaluate=False)) 
                    sign_exp_expr=signs.replace("ℯ","e")
                    self.ids.lbl0.text=sign_exp_expr
                                                                                        #section for auto factor-expand
                elif len(sympify(main_sign2).atoms(Symbol)) != 0 and ("integrate(" not in main_sign2 and "limit(" not in main_sign2 and "diff(" not in main_sign2):
                    
                    if ((str(sympify(main_sign2)).replace('**','^'))).replace(' ','')== ((str(sympify(factor(main_sign2))).replace('**','^'))).replace(' ',''):
                        sign_str=pretty(simplify(str('expand('+main_sign2+')'))) 
                    else:
                        sign_str=pretty(simplify(str('factor('+main_sign2+')'))) 
                    sign_exp=sign_str.replace("ℯ","e")
                    self.ids.lbl1.text=sign_exp

                    signs=pretty(sympify(main_sign2,evaluate=False)) 
                    sign_exp_expr=signs.replace("ℯ","e")
                    self.ids.lbl0.text=sign_exp_expr
                
            except(SympifyError,Exception):
                pass
        
        other_mathematics(self)

        def count_bra_and_error_debug(self):  
            try:
                bra_left=self.ids.txt1.text.count("(")
                bra_right=self.ids.txt1.text.count(")")
                use_text="Do not forget brackets '"
        
                if bra_left>bra_right:
                    bra_l=bra_left-bra_right
                    self.ids.txt1.helper_text=use_text+bra_l*")'"
                elif bra_left<bra_right:
                    bra_r=bra_right-bra_left
                    self.ids.txt1.helper_text=use_text+bra_r*"('"
                    
                elif "<" in self.ids.lbl0.text and ">" in self.ids.lbl1.text and ("<" not in self.ids.txt1.text or ">" not in self.ids.txt1.text):
                    self.ids.lbl0.text="typing..."
                    self.ids.lbl1.text="waiting..."
                    self.ids.lblcol.text=""
                    self.ids.lblcol.background_color=(0,0,0,0)
                
                else:
                    self.ids.txt1.helper_text=""
            except(Exception):
                pass
        count_bra_and_error_debug(self)

        self.ids.lbl1.texture_update()
        self.ids.lbl0.texture_update()
        self.ids.lblcol.texture_update()

        self.oto_width_main()
        self.oto_height_main()
                          
    def gohelp(self):
        self.manager.current='help'

        self.manager.get_screen('help').ids.helptoolbar.right_action_items=[["timeline-question"]]
        self.manager.get_screen('help').ids.helptoolbar.left_action_items=[["arrow-left",lambda x: self.manager.get_screen('help').back_menu()]]
    
    def calc_matrices(self):
        if len(img_data)>0: 
            if (img_data.count('2'))>0:
                self.ids.box_layout.remove_widget(self.ids.button_steps)
            else:
                self.ids.box_layout.remove_widget(self.ids.img_box)
            img_data.clear()
            self.ids.lbl_blue.text="[Out]"
                
        ctnt=BoxLayout(orientation='vertical',spacing='1dp')
        b1=Button(text='Create a 2x2 matrices',background_normal='#F0F0F0',background_color='#F0F0F0',color='black')
        b2=Button(text='Create a 3x3 matrices',background_normal='#F0F0F0',background_color='#F0F0F0',color='black')
        b3=Button(text='Create a 4x4 matrices',background_normal='#F0F0F0',background_color='#F0F0F0',color='black')
        
        b1.bind(on_press=self.matrices_two)
        b2.bind(on_press=self.matrices_three) 
        b3.bind(on_press=self.matrices_four)
        
        ctnt.add_widget(b1)
        ctnt.add_widget(b2)
        ctnt.add_widget(b3)
        
        popmat_x=Window.size[0]/1.35
        popmat_y=Window.size[1]/2.4 
        popup = Popup(title='Create any Matrice',title_color='black',content=ctnt,size_hint=(None,None),size=(popmat_x,popmat_y),auto_dismiss=True,
                      background_color = (255,255,255,1),separator_color='grey')
        b1.bind(on_press=popup.dismiss)
        b2.bind(on_press=popup.dismiss)
        b3.bind(on_press=popup.dismiss)
        popup.open()
        self.ids.lbl0.font_size="14dp"
        self.ids.lbl1.font_size="18dp"
        self.ids.lbl0.texture_update()
        self.ids.lbl1.texture_update()
        
    def matrices_two(self, instance):
        ctnt=BoxLayout(orientation='vertical')
        ctntx=BoxLayout(orientation='horizontal')
        ctntx1=BoxLayout(orientation='horizontal')
        ctntx2=BoxLayout(orientation='horizontal')
        b1=TextInput(text='',hint_text="a11")
        b2=TextInput(text='',hint_text="a12")
        b3=TextInput(text='',hint_text="a21")
        b4=TextInput(text='',hint_text="a22")
        b5=Button(text='Determinant',background_normal='#F0F0F0',background_color='#F0F0F0',color='black')
        b6=Button(text='Transpose',background_normal='#F0F0F0',background_color='#F0F0F0',color='black')
        b7=Button(text='Invserse',background_normal='#F0F0F0',background_color='#F0F0F0',color='black')

        b5.bind(on_press=self.matrices_two_det)
        b6.bind(on_press=self.matrices_two_trans)
        b7.bind(on_press=self.matrices_two_invers)

        self.ids["matricestwo_one"]=b1
        self.ids["matricestwo_two"]=b2
        self.ids["matricestwo_three"]=b3
        self.ids["matricestwo_four"]=b4

        ctntx.add_widget(b1)
        ctntx.add_widget(b2)
        ctntx1.add_widget(b3)
        ctntx1.add_widget(b4)
        ctntx2.add_widget(b5)
        ctntx2.add_widget(b6)
        ctntx2.add_widget(b7)
        
        ctnt.add_widget(ctntx)
        ctnt.add_widget(ctntx1)
        ctnt.add_widget(ctntx2)

        popint_x=Window.size[0]/1.35
        popint_y=Window.size[1]/2.4
        self.popup = Popup(title='2x2 Marix', title_color='black',content=ctnt,size_hint=(None,None),size=(popint_x,popint_y),separator_color='grey',
                      auto_dismiss=True, background_color = (255,255,255,1),pos_hint={'top':0.88})
        b5.bind(on_press=self.popup.dismiss)
        b6.bind(on_press=self.popup.dismiss)
        b7.bind(on_press=self.popup.dismiss)
        self.popup.open()

    def matrices_two_det(self,instance):
        try:
            iexpr=sympify(self.ids.matricestwo_one.text)
            i2expr=sympify(self.ids.matricestwo_two.text)
            i3expr=sympify(self.ids.matricestwo_three.text)
            i4expr=sympify(self.ids.matricestwo_four.text)
            self.ids.txt1.text='Matrix([[{},{}],[{},{}]]).det()'.format(iexpr,i2expr,i3expr,i4expr)
            
        except(SympifyError,Exception):
            self.matrices_two(instance)
            self.popup.title="Matrices error"

    def matrices_two_trans(self, instance):
        try:
            iexpr=sympify(self.ids.matricestwo_one.text)
            i2expr=sympify(self.ids.matricestwo_two.text)
            i3expr=sympify(self.ids.matricestwo_three.text)
            i4expr=sympify(self.ids.matricestwo_four.text)
            self.ids.txt1.text='Matrix([[{},{}],[{},{}]]).T'.format(iexpr,i2expr,i3expr,i4expr)


        except(SympifyError,Exception):
            self.matrices_two(instance)
            self.popup.title="Matrices error"

    def matrices_two_invers(self, instance):
        try:
            iexpr=sympify(self.ids.matricestwo_one.text)
            i2expr=sympify(self.ids.matricestwo_two.text)
            i3expr=sympify(self.ids.matricestwo_three.text)
            i4expr=sympify(self.ids.matricestwo_four.text)
            self.ids.txt1.text='Matrix([[{},{}],[{},{}]]).inv()'.format(iexpr,i2expr,i3expr,i4expr)
            
        except(SympifyError,Exception):
            self.matrices_two(instance)
            self.popup.title="Matrices error"

    def matrices_three(self, instance):
        ctnt=BoxLayout(orientation='vertical')
        ctntx=BoxLayout(orientation='horizontal')
        ctntx1=BoxLayout(orientation='horizontal')
        ctntx2=BoxLayout(orientation='horizontal')
        ctntx3=BoxLayout(orientation='horizontal')
        b1=TextInput(text='',hint_text="a11")
        b2=TextInput(text='',hint_text="a12")
        b3=TextInput(text='',hint_text="a13")
        b4=TextInput(text='',hint_text="a21")
        b5=TextInput(text='',hint_text="a22")
        b6=TextInput(text='',hint_text="a23")
        b7=TextInput(text='',hint_text="a31")
        b8=TextInput(text='',hint_text="a32")
        b9=TextInput(text='',hint_text="a33")
        b10=Button(text='Determinant',background_normal='#F0F0F0',background_color='#F0F0F0',color='black')
        b11=Button(text='Transpose',background_normal='#F0F0F0',background_color='#F0F0F0',color='black')
        b12=Button(text='Invserse',background_normal='#F0F0F0',background_color='#F0F0F0',color='black')

        b10.bind(on_press=self.matrices_three_det)
        b11.bind(on_press=self.matrices_three_trans)
        b12.bind(on_press=self.matrices_three_invers)

        self.ids["matricesthree_one"]=b1
        self.ids["matricesthree_two"]=b2
        self.ids["matricesthree_three"]=b3
        self.ids["matricesthree_four"]=b4
        self.ids["matricesthree_five"]=b5
        self.ids["matricesthree_six"]=b6
        self.ids["matricesthree_seven"]=b7
        self.ids["matricesthree_eight"]=b8
        self.ids["matricesthree_nine"]=b9

        ctntx.add_widget(b1)
        ctntx.add_widget(b2)
        ctntx.add_widget(b3)
        ctntx1.add_widget(b4)
        ctntx1.add_widget(b5)
        ctntx1.add_widget(b6)
        ctntx2.add_widget(b7)
        ctntx2.add_widget(b8)
        ctntx2.add_widget(b9)
        ctntx3.add_widget(b10)
        ctntx3.add_widget(b11)
        ctntx3.add_widget(b12)
        
        ctnt.add_widget(ctntx)
        ctnt.add_widget(ctntx1)
        ctnt.add_widget(ctntx2)
        ctnt.add_widget(ctntx3)

        popint_x=Window.size[0]/1.35
        popint_y=Window.size[1]/2.4
        self.popup = Popup(title='3x3 Matrix', title_color='black',content=ctnt,size_hint=(None,None),size=(popint_x,popint_y),separator_color='grey',
                      auto_dismiss=True, background_color = (255,255,255,1),pos_hint={'top':0.88}) 
        b10.bind(on_press=self.popup.dismiss)
        b11.bind(on_press=self.popup.dismiss)
        b12.bind(on_press=self.popup.dismiss)
        self.popup.open()

    def matrices_three_det(self, instance):
        try:
            iexpr=sympify(self.ids.matricesthree_one.text)
            i2expr=sympify(self.ids.matricesthree_two.text)
            i3expr=sympify(self.ids.matricesthree_three.text)
            i4expr=sympify(self.ids.matricesthree_four.text)
            i5expr=sympify(self.ids.matricesthree_five.text)
            i6expr=sympify(self.ids.matricesthree_six.text)
            i7expr=sympify(self.ids.matricesthree_seven.text)
            i8expr=sympify(self.ids.matricesthree_eight.text)
            i9expr=sympify(self.ids.matricesthree_nine.text)
            self.ids.txt1.text='Matrix([[{},{},{}],[{},{},{}],[{},{},{}]]).det()'.format(iexpr,i2expr,i3expr,i4expr,i5expr,i6expr,i7expr,i8expr,i9expr)

        except(SympifyError,Exception):
            self.matrices_three(instance)
            self.popup.title="Matrices error"

    def matrices_three_trans(self, instance):  
        try:
            iexpr=sympify(self.ids.matricesthree_one.text)
            i2expr=sympify(self.ids.matricesthree_two.text)
            i3expr=sympify(self.ids.matricesthree_three.text)
            i4expr=sympify(self.ids.matricesthree_four.text)
            i5expr=sympify(self.ids.matricesthree_five.text)
            i6expr=sympify(self.ids.matricesthree_six.text)
            i7expr=sympify(self.ids.matricesthree_seven.text)
            i8expr=sympify(self.ids.matricesthree_eight.text)
            i9expr=sympify(self.ids.matricesthree_nine.text)
            self.ids.txt1.text='Matrix([[{},{},{}],[{},{},{}],[{},{},{}]]).T'.format(iexpr,i2expr,i3expr,i4expr,i5expr,i6expr,i7expr,i8expr,i9expr)

        except(SympifyError,Exception):
            self.matrices_three(instance)
            self.popup.title="Matrices error"
            
    def matrices_three_invers(self, instance):
        try:
            iexpr=sympify(self.ids.matricesthree_one.text)
            i2expr=sympify(self.ids.matricesthree_two.text)
            i3expr=sympify(self.ids.matricesthree_three.text)
            i4expr=sympify(self.ids.matricesthree_four.text)
            i5expr=sympify(self.ids.matricesthree_five.text)
            i6expr=sympify(self.ids.matricesthree_six.text)
            i7expr=sympify(self.ids.matricesthree_seven.text)
            i8expr=sympify(self.ids.matricesthree_eight.text)
            i9expr=sympify(self.ids.matricesthree_nine.text)
            self.ids.txt1.text='Matrix([[{},{},{}],[{},{},{}],[{},{},{}]]).inv()'.format(iexpr,i2expr,i3expr,i4expr,i5expr,i6expr,i7expr,i8expr,i9expr)

        except(SympifyError,Exception):
            self.matrices_three(instance)
            self.popup.title="Matrices error"

    def matrices_four(self, instance):
        ctnt=BoxLayout(orientation='vertical')
        ctntx=BoxLayout(orientation='horizontal')
        ctntx1=BoxLayout(orientation='horizontal')
        ctntx2=BoxLayout(orientation='horizontal')
        ctntx3=BoxLayout(orientation='horizontal')
        ctntx4=BoxLayout(orientation='horizontal')
        b1=TextInput(text='',hint_text="a11")
        b2=TextInput(text='',hint_text="a12")
        b3=TextInput(text='',hint_text="a13")
        b4=TextInput(text='',hint_text="a14")
        b5=TextInput(text='',hint_text="a21")
        b6=TextInput(text='',hint_text="a22")
        b7=TextInput(text='',hint_text="a23")
        b8=TextInput(text='',hint_text="a24")
        b9=TextInput(text='',hint_text="a31")
        b10=TextInput(text='',hint_text="a32")
        b11=TextInput(text='',hint_text="a33")
        b12=TextInput(text='',hint_text="a34")
        b13=TextInput(text='',hint_text="a41")
        b14=TextInput(text='',hint_text="a42")
        b15=TextInput(text='',hint_text="a43")
        b16=TextInput(text='',hint_text="a44")
        b17=Button(text='Determinant',background_normal='#F0F0F0',background_color='#F0F0F0',color='black')
        b18=Button(text='Transpose',background_normal='#F0F0F0',background_color='#F0F0F0',color='black')
        b19=Button(text='Invserse',background_normal='#F0F0F0',background_color='#F0F0F0',color='black')

        b17.bind(on_press=self.matrices_four_det)
        b18.bind(on_press=self.matrices_four_trans)
        b19.bind(on_press=self.matrices_four_invers)

        self.ids["matricesfour_one"]=b1
        self.ids["matricesfour_two"]=b2
        self.ids["matricesfour_three"]=b3
        self.ids["matricesfour_four"]=b4
        self.ids["matricesfour_five"]=b5
        self.ids["matricesfour_six"]=b6
        self.ids["matricesfour_seven"]=b7
        self.ids["matricesfour_eight"]=b8
        self.ids["matricesfour_nine"]=b9
        self.ids["matricesfour_ten"]=b10
        self.ids["matricesfour_eleven"]=b11
        self.ids["matricesfour_twelve"]=b12
        self.ids["matricesfour_threeten"]=b3
        self.ids["matricesfour_fourteen"]=b14
        self.ids["matricesfour_fiveteen"]=b15
        self.ids["matricesfour_sixteen"]=b16

        ctntx.add_widget(b1)
        ctntx.add_widget(b2)
        ctntx.add_widget(b3)
        ctntx.add_widget(b4)
        ctntx1.add_widget(b5)
        ctntx1.add_widget(b6)
        ctntx1.add_widget(b7)
        ctntx1.add_widget(b8)
        ctntx2.add_widget(b9)
        ctntx2.add_widget(b10)
        ctntx2.add_widget(b11)
        ctntx2.add_widget(b12)
        ctntx3.add_widget(b13)
        ctntx3.add_widget(b14)
        ctntx3.add_widget(b15)
        ctntx3.add_widget(b16)
        ctntx4.add_widget(b17)
        ctntx4.add_widget(b18)
        ctntx4.add_widget(b19)
        
        ctnt.add_widget(ctntx)
        ctnt.add_widget(ctntx1)
        ctnt.add_widget(ctntx2)
        ctnt.add_widget(ctntx3)
        ctnt.add_widget(ctntx4)

        popint_x=Window.size[0]/1.35
        popint_y=Window.size[1]/2.4
        self.popup = Popup(title='4x4 Matrix', title_color='black',content=ctnt,size_hint=(None,None),size=(popint_x,popint_y),separator_color='grey',
                      auto_dismiss=True, background_color = (255,255,255,1),pos_hint={'top':0.88})
        b17.bind(on_press=self.popup.dismiss)
        b18.bind(on_press=self.popup.dismiss)
        b19.bind(on_press=self.popup.dismiss)
        self.popup.open()

    def matrices_four_det(self, instance):
        try:
            iexpr=sympify(self.ids.matricesfour_one.text)
            i2expr=sympify(self.ids.matricesfour_two.text)
            i3expr=sympify(self.ids.matricesfour_three.text)
            i4expr=sympify(self.ids.matricesfour_four.text)
            i5expr=sympify(self.ids.matricesfour_five.text)
            i6expr=sympify(self.ids.matricesfour_six.text)
            i7expr=sympify(self.ids.matricesfour_seven.text)
            i8expr=sympify(self.ids.matricesfour_eight.text)
            i9expr=sympify(self.ids.matricesfour_nine.text)
            i10expr=sympify(self.ids.matricesfour_ten.text)
            i11expr=sympify(self.ids.matricesfour_eleven.text)
            i12expr=sympify(self.ids.matricesfour_twelve.text)
            i13expr=sympify(self.ids.matricesfour_threeten.text)
            i14expr=sympify(self.ids.matricesfour_fourteen.text)
            i15expr=sympify(self.ids.matricesfour_fiveteen.text)
            i16expr=sympify(self.ids.matricesfour_sixteen.text)
            self.ids.txt1.text='Matrix([[{},{},{},{}],[{},{},{},{}],[{},{},{},{}],[{},{},{},{}]]).det()'.format(iexpr,i2expr,i3expr,i4expr,i5expr,i6expr,i7expr,i8expr,i9expr,
                                                                                   i10expr,i11expr,i12expr,i13expr,i14expr,i15expr,i16expr)
        except(SympifyError,Exception):
            self.matrices_four(instance)
            self.popup.title="Matrices error"

    def matrices_four_trans(self, instance):
        try:
            iexpr=sympify(self.ids.matricesfour_one.text)
            i2expr=sympify(self.ids.matricesfour_two.text)
            i3expr=sympify(self.ids.matricesfour_three.text)
            i4expr=sympify(self.ids.matricesfour_four.text)
            i5expr=sympify(self.ids.matricesfour_five.text)
            i6expr=sympify(self.ids.matricesfour_six.text)
            i7expr=sympify(self.ids.matricesfour_seven.text)
            i8expr=sympify(self.ids.matricesfour_eight.text)
            i9expr=sympify(self.ids.matricesfour_nine.text)
            i10expr=sympify(self.ids.matricesfour_ten.text)
            i11expr=sympify(self.ids.matricesfour_eleven.text)
            i12expr=sympify(self.ids.matricesfour_twelve.text)
            i13expr=sympify(self.ids.matricesfour_threeten.text)
            i14expr=sympify(self.ids.matricesfour_fourteen.text)
            i15expr=sympify(self.ids.matricesfour_fiveteen.text)
            i16expr=sympify(self.ids.matricesfour_sixteen.text)
            self.ids.txt1.text='Matrix([[{},{},{},{}],[{},{},{},{}],[{},{},{},{}],[{},{},{},{}]]).T'.format(iexpr,i2expr,i3expr,i4expr,i5expr,i6expr,i7expr,i8expr,i9expr,
                                                                                   i10expr,i11expr,i12expr,i13expr,i14expr,i15expr,i16expr)
        except(SympifyError,Exception):
            self.matrices_four(instance)
            self.popup.title="Matrices error"

    def matrices_four_invers(self, instance):
        try:
            iexpr=sympify(self.ids.matricesfour_one.text)
            i2expr=sympify(self.ids.matricesfour_two.text)
            i3expr=sympify(self.ids.matricesfour_three.text)
            i4expr=sympify(self.ids.matricesfour_four.text)
            i5expr=sympify(self.ids.matricesfour_five.text)
            i6expr=sympify(self.ids.matricesfour_six.text)
            i7expr=sympify(self.ids.matricesfour_seven.text)
            i8expr=sympify(self.ids.matricesfour_eight.text)
            i9expr=sympify(self.ids.matricesfour_nine.text)
            i10expr=sympify(self.ids.matricesfour_ten.text)
            i11expr=sympify(self.ids.matricesfour_eleven.text)
            i12expr=sympify(self.ids.matricesfour_twelve.text)
            i13expr=sympify(self.ids.matricesfour_threeten.text)
            i14expr=sympify(self.ids.matricesfour_fourteen.text)
            i15expr=sympify(self.ids.matricesfour_fiveteen.text)
            i16expr=sympify(self.ids.matricesfour_sixteen.text)
            self.ids.txt1.text='Matrix([[{},{},{},{}],[{},{},{},{}],[{},{},{},{}],[{},{},{},{}]]).inv()'.format(iexpr,i2expr,i3expr,i4expr,i5expr,i6expr,i7expr,i8expr,i9expr,
                                                                                   i10expr,i11expr,i12expr,i13expr,i14expr,i15expr,i16expr)     
        except(SympifyError,Exception):
            self.matrices_four(instance)
            self.popup.title="Matrices error"

    def add_graphs(self,mul):
        self.ids.txt1.focus=False
        if len(img_data)>0: 
            if (img_data.count('2'))>0:
                self.ids.box_layout.remove_widget(self.ids.button_steps)
            else:
                self.ids.box_layout.remove_widget(self.ids.img_box)
            img_data.clear()

        if mul==1:
            img_data.append('1')
            
        elif mul==2:
            img_data.append('0')
            img_data.append('1')
            
        return self.calc_graphs() 
       
    def calc_graphs(self):
        try:
            main_sign1=self.ids.txt1.text.replace("×","*")
            main_sign2=main_sign1.replace("÷","/")
            if ',' in self.ids.txt1.text and len(img_data)==1: 
                splt=main_sign2.split(",")
                graph_one=splt[0]
                graph_two=splt[1]
                state1=sympify(graph_one)
                state2=sympify(graph_two)
                self.ids.lbl_blue.text="" 
                self.ids.lbl1.text=""
                T=plot((state1),(state2),show=False,legend=True)
                T[0].line_color=(0,0,0)
                T[0].label=graph_one
                T[1].label=graph_two
                buf = io.BytesIO()
                T.save(buf)
                buf.seek(0)
                create_box=MDBoxLayout(adaptive_height=True) 
                create_img=Image(source='')
                self.ids["img"]=create_img
                self.ids["img_box"]=create_box
                create_img.size_hint=(None,None)
                self.ids.box_layout.add_widget(create_box) 
                create_box.add_widget(create_img) 
                create_img.texture=CoreImage(buf, ext="png").texture
                create_img.reload()
                create_img.width=self.width
                create_img.pos_hint={'top':1.3}
                create_img.height=Window.size[1]/2.74   
                create_img.allow_stretch=True
                create_img.keep_ratio=True
                del buf
                
            else:    
                state=sympify(main_sign2)
                self.ids.lbl_blue.text=""
                self.ids.lbl1.text=""
                fix_sign_exp_img=pretty(sympify(main_sign2,evaluate=False)).replace("ℯ","e")
                self.ids.lbl0.text=fix_sign_exp_img
                
                if len(img_data)==1: 
                    T=plot(state,show=False)
                    
                elif len(img_data)==2:
                    T=plot3d(state,show=False)
                    
                buf = io.BytesIO()
                T.save(buf)
                buf.seek(0)
                create_box=MDBoxLayout(adaptive_height=True) 
                create_img=Image(source='')
                self.ids["img"]=create_img
                self.ids["img_box"]=create_box
                create_img.size_hint=(None,None)
                self.ids.box_layout.add_widget(create_box) 
                create_box.add_widget(create_img) 
                create_img.texture=CoreImage(buf, ext="png").texture
                create_img.reload()
                create_img.width=self.width
                create_img.pos_hint={'top':1.3}
                create_img.height=Window.size[1]/2.74   
                create_img.allow_stretch=True
                create_img.keep_ratio=True
                del buf

            self.ids.lblcol.text=""
                
        except(SympifyError,Exception):
            img_data.clear()
            self.ids.lbl0.text="Graph error"
            self.ids.lbl1.text=""
            
    def calc_graphdata(self):
        ctnt=BoxLayout(orientation='vertical',spacing='1dp')
        self.b1=Button(text='Create a line data',background_normal='#F0F0F0',background_color='#F0F0F0',color='black')
        self.b2=Button(text='Create a dot data',background_normal='#F0F0F0',background_color='#F0F0F0',color='black')   
        self.b3=Button(text='Create a column data',background_normal='#F0F0F0',background_color='#F0F0F0',color='black')
        
        self.b1.bind(on_press=self.set_data)
        self.b2.bind(on_press=self.set_data) 
        self.b3.bind(on_press=self.set_data)
        
        ctnt.add_widget(self.b1)
        ctnt.add_widget(self.b2)
        ctnt.add_widget(self.b3)
        
        popint_x=Window.size[0]/1.35
        popint_y=Window.size[1]/2.4
        popup = Popup(title='Choose a dataset', title_color='black',content=ctnt,size_hint=(None,None),size=(popint_x,popint_y),separator_color='grey',
                      auto_dismiss=True, background_color = (255,255,255,1),pos_hint={'top':0.88}) 
        self.b1.bind(on_press=popup.dismiss)
        self.b2.bind(on_press=popup.dismiss)
        self.b3.bind(on_press=popup.dismiss)
        popup.open()

    def set_data(self,instance):
        try:
            if self.b1.state=='down':
                dataset_name_data.append("Line Dataset")
            elif self.b2.state=='down':
                dataset_name_data.append("Dot Dataset")
            elif self.b3.state=='down':
                dataset_name_data.append("Column Dataset")
                
            ctnt=BoxLayout(orientation='vertical')
            ctntx=BoxLayout(orientation='horizontal')
            ctnty=BoxLayout(orientation='horizontal')
            b1=TextInput(text='',hint_text="X-axis values e.g 1,2,3,4,5")
            bx=TextInput(text='',hint_text="x-axis title")
            b2=TextInput(text='',hint_text="Y-axis values e.g 1,2,3,4,5")
            by=TextInput(text='',hint_text="y-axis title")
            b3=Button(text="Draw",background_normal='#F0F0F0',background_color='#F0F0F0',color='black')
            b4=TextInput(text='',hint_text="Graph title")
            
            self.ids['xaxis'] = b1 
            self.ids['yaxis']= b2
            self.ids['title']= b4
            self.ids['xaxistitle']= bx
            self.ids['yaxistitle']= by
            ctntx.add_widget(b1)
            ctntx.add_widget(bx)
            ctnty.add_widget(b2)
            ctnty.add_widget(by)

            ctnt.add_widget(ctntx)
            ctnt.add_widget(ctnty)
            ctnt.add_widget(b4)
            ctnt.add_widget(b3)

            b3.bind(on_press=self.show_dataset)
            b2.bind(text=self.line_check)
            
            popint_x=Window.size[0]/1.35
            popint_y=Window.size[1]/2.4
            self.popup = Popup(title=dataset_name_data[-1],title_color='black', content=ctnt,size_hint=(None,None),size=(popint_x,popint_y),separator_color='grey',
                      auto_dismiss=True,background_color = (255,255,255,1) ,pos_hint={'top':0.88}) 
            
            self.popup.open()

        except(SympifyError,Exception):
            pass

    def line_check(self,*args):
        len_x=self.ids.xaxis.text.count(",")
        len_y=self.ids.yaxis.text.count(",")
        len_sub=len_x-len_y
        
        if len_sub==0:
            self.popup.title_color="black"
            self.popup.title=dataset_name_data[0]
        elif len_sub>0:
            self.popup.title_color="black"
            self.popup.title=" "+str(len_sub)
        elif len_sub<0:
            self.popup.title_color="red"
            self.popup.title=" "+str(len_sub)
            
    def show_dataset(self,instance):
        try:
            self.ids.txt1.focus=False
            X=sympify(self.ids.xaxis.text) 
            Y=sympify(self.ids.yaxis.text)
            len_x=self.ids.xaxis.text.count(",")
            len_y=self.ids.yaxis.text.count(",")
            
            if len(img_data)>0: 
                if (img_data.count('2'))>0:
                    self.ids.box_layout.remove_widget(self.ids.button_steps)
                else:
                    self.ids.box_layout.remove_widget(self.ids.img_box)
                img_data.clear()
                
            if len_x==len_y and len(img_data)==0:
                
                self.popup.dismiss() 
                img_data.append("1")
                
                self.ids.lbl_blue.text=""
                self.ids.lbl1.text=""
                self.ids.lbl0.text="Dataset graph;"
                
                plt.clf()
                
                if dataset_name_data[-1]=='Line Dataset':
                    plt.plot(X,Y)
                    
                elif dataset_name_data[-1]=='Column Dataset':
                    plt.bar(X,Y)
                    
                elif dataset_name_data[-1]=='Dot Dataset':
                    plt.plot(X,Y,'ro')
                    
                plt.title(self.ids.title.text)
                plt.xlabel(self.ids.xaxistitle.text)
                plt.ylabel(self.ids.yaxistitle.text)
                buf=io.BytesIO()
                plt.savefig(buf)
                buf.seek(0)
                create_box=MDBoxLayout(adaptive_height=True) 
                create_img=Image(source='')
                self.ids["img"]=create_img
                self.ids["img_box"]=create_box
                create_img.size_hint=(None,None)
                self.ids.box_layout.add_widget(create_box)
                create_box.add_widget(create_img) 
                create_img.texture=CoreImage(buf, ext="png").texture
                create_img.reload()
                create_img.width=self.width
                create_img.pos_hint={'top':1.3}
                create_img.height=Window.size[1]/2.74   
                create_img.allow_stretch=True
                create_img.keep_ratio=True
                del buf
                plt.clf()

                dataset_name_data.clear()
                self.ids.lblcol.text=""               
                
            elif len_x>len_y:
                self.ids.xaxis.foreground_color="red"
                self.popup.title="No equal content with y-axis"
            elif len_x<len_y:
                self.ids.yaxis.foreground_color="red"
                self.popup.title="No equal content with x-axis"
                        
        except(SympifyError,Exception):
            img_data.clear()
        
class HelpScreen(Screen):
    
    def write(self): 
        self.ids.helplabel.text="""[b]What is Mathpath console?[/b]

[i]Mathpath console is an advanced mathematical solver. This application started to develop by [color=407EA8]Reşat Berk[/color] during studying physics. \
Then a few group members called [color=407EA8]Stars of the Sky[/color]. Our mission is, developing scientific easy-tools(useful) for all students or education field and with students do this. Mathpath is a just starter that way. \
Also Stars of The sky still continue to developing scientific tools if enough support.[/i]

[b]How to use Mathpath console[/b]

Just type your mathematical expression. While you're typing, you'll see 3 sections on screen. [b]1st[/b] section is textbox, [b]2nd[/b] section is [color=407EA8]'[In]'[/color] label and [b]last[/b] section is [color=407EA8]'[Out]'[/color] label. \
Textbox just takes symbols and words convert to mathematical notation in '[In]' section. Then quickly solution appeir in '[Out]' section. \


Also there is [b]Step-by-step[/b] solution for calculus. This solution need internet connection and linked you new tab in Google to open Sympy Gamma. \
These solution source is Sympy Gamma.


Also have [color=407EA8][b]Dataset, 2D, 3D and Matrices[/b][/color] segment on screen. 'Dataset, 2D and 3D' sections for display graphics. For example, you typed [color=407EA8][b]'x+3'[/b][/color] and press on '2D' button. You'll see graphic! \
And matrices section uses prepared matrices structure to do quick process like Det, Inverse, Transpose.[/i] \


[b]Currently supporting these subject (and their examples)[/b]:

[b]• [color=#D26200]Algebra[/color][/b]
[color=#777777]x^2 + 3×x + 5 = 0
(x+3)×(x+2) > 5
(a+b)^4[/color]
...

[b]• [color=#D26200]Calculus[/color][/b]
  [b][i]#Definitions[/i][/b]
    i) diff(expr, variable, rank) [color=#777777]If rank is 1 (so like d/dx not d[sup]n[/sup]/dx[sup]n[/sup]), do not need to type. Also same way for variable. Look samples below.[/color] \


    ii) integrate(expr, variable) [color=#777777]for [b]Indefinite integrals[/b]. Do not forget, this calculator returns C = 0.[/color] \


    iii) integrate(expr, (variable, a, b)) [color=#777777]for [b]Definite integrals[/b]. a and b is limits down and up.(a to b)[/color] \


[color=#777777]diff(cos(x), x)
diff(cos(x), x, 2)
integrate(x+2, x)
integrate(x+2, (x, 0, 5))[/color] 
...

[b]• [color=#D26200]Differentiation Equations[/color][/b]
  [b][i]#Definitions[/i][/b]
    i) f''(x) = y'' = d[sup]2[/sup]/dx[sup]2[/sup] = [b]diff(y(x), x,2)[/b] [color=#777777]Please use diff(...) definition for create differantiation equation. For example, \

[b]y'' + y = sin(x) == diff(y(x), x,2) + y(x) = sin(x)[/b][/color]


[color=#777777]diff(f(x), x,2) + f(x) = sin(x)
diff(f(x,y), x) + diff(f(x,y), y) + f(x,y) = 0[/color]
...

[b]• [color=#D26200]Matrices[/color][/b]
  [b][i]#Definitions[/i][/b]
    i) Create any matrices like [b]Matrix( [[a1,a2],[a3,a4]] )[/b] [color=#777777]follows these structure
|a1 a2|
|a3 a4|
You can create any matrix that any size like this process. Then choose matrix operators.[/color] \


[color=#777777]Matrix([[1,2], [2,2]]) + Matrix([[1,1], [2,3]]) 
Matrix([[1,2], [2,2]]).det()[/color]
...

[b]• [color=#D26200]2D, 3D, Dataset graphs[/color][/b]
[color=#777777]x^2 + 3 [b]||[/b] Choose 2D[/color]
[color=#777777]x+3[/color],[color=#777777] x-5 [b]||[/b][/color] -Two graphs- [color=#777777]Choose 2D[/color]
[color=#777777]x×y [b]||[/b] Choose 3D[/color]
...

[b]• [color=#D26200]Series[/color][/b]
[color=#777777]series(exp(sin(x)), x, 0, 4)
fourier_series(x^2, (x, -pi, -2×pi))
fourier_transform(exp(-x^2), x, k)[/color]
...

[b]• [color=#D26200]Vector Fields[/color][/b]
[color=#777777]div(18×x^2×y×i + 3×x×y×j)
grad(x^2×y×z + 3×y^2×z^2)[/color]
...

[b]• [color=#D26200]Special Functions[/color][/b]
[color=#777777]gamma(1)
hermite(3, x)
legendre(2,x)[/color]
...

[b][Errors information][/b]
If something didn't well and you got some error, probably their reasons like: \
If you complete your math problem and you still don't any answer, just you see on screen; [b]Typing... and Waiting...[/b],  \
[b]Graph error[/b], [b]Matrices error[/b], [b]vMathkeyboard error[/b], [b]Notation error[/b]. These means you got operator error \
[color=407EA8]{+, -, ×, /, (, )}[/color] or math structure error like [color=407EA8]diff(f(x), x)[/color]. \


Normally, vMath keyboard following by checking mathematical notation algorithm. If you press button [b]'3y+2'[/b] to type on textbox; vMath automatically edits like [b]'3×y+2'[/b]. \
Other reason is math structure. If you fill wrong math structure like [color=407EA8]limit(f(x), (x, 0))[/color] instead of [color=407EA8]limit(f(x), x, 0)[/color] get this error. [/i][/color]  
Please pay attention to use true operators and use math structures.(These rules display in hints)


Also Mathpath console can download for Windows system and now its wide sample is [b]open source in Github[/b]. Check out our web-site in below. If you have feedback or you found a bug please contact us. \
And if you want to join us to contribute scientific tools, don't hesitate to send any mail. You know this is pretty experience programming to useful things in little dorm room. \


• Use [b]Sympy Gamma[/b] (free) for [b]step-by-step[/b] solution on Web
[i]help.starsofthesky@gmail.com[/i]
[color=#777777]Update tag: [/color] [color=#D26200]#Weasleys[/color] 
"""                                                        
    def back_menu(self):
        self.manager.current='menu'
       
class MathPathApp(MDApp):

    def on_start(self):
        self.root.get_screen('menu').ids.change_tools.icon="matrix"
        self.root.get_screen('menu').ids.change_2d.icon="chart-bell-curve-cumulative"
        self.root.get_screen('menu').ids.change_3d.icon="cube-outline"
        self.root.get_screen('menu').ids.dataset.icon="chart-bar"        
                                                                    
    def build(self):
        self.theme_cls.material_style = "M3"
        Builder.load_file("menu_screen.kv")
        Builder.load_file("help_screen.kv")
        self.screenm = ScreenManager()
        self.screenm.add_widget(MenuScreen(name='menu'))
        self.screenm.add_widget(HelpScreen(name='help'))
        return self.screenm

kv=MathPathApp().run()

