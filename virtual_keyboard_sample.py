                                    #Current ver== KivyMD version = 1.1.1 , Kivy version = 2.1.0 , SymPy version = 1.10.1
from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder      
from kivymd.uix.behaviors import TouchBehavior
from kivymd.uix.gridlayout import MDGridLayout 
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivy.metrics import dp 
from kivy.uix.button import Button
from kivymd.uix.navigationdrawer import (
    MDNavigationLayout,
    MDNavigationDrawer,
    MDNavigationDrawerMenu,
    MDNavigationDrawerHeader)
from kivy.uix.scrollview import ScrollView        
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image,CoreImage
from kivy.core.window import Window

from sympy import S, I, pi, gamma, zeta, jacobi, legendre, assoc_legendre, hermite, laguerre, assoc_laguerre
from sympy.plotting import plot, plot3d
from sympy import *
a, b, c, d, e, f, g, h, i, j, k, l, m, n, p, r, s, t, u, v, x, y, z, nu, rho, phi, theta = symbols("a b c d e f g h i j k l m n p r s t u v x y z nu rho phi theta")
init_printing(use_unicode=True)

                                                 #this keyboard keys for 1st open and it's changeable
mykeyboard_keys={'b1': ('∫ dx','#EEEEEE'), 'b2':('abc','#EEEEEE'), 'b3':('[size=30]trigo∆[/size]','#EEEEEE'), 'b4':('[size=68]←[/size]','#EEEEEE'), 
            'b5':('[size=68]→[/size]','#EEEEEE'), 'b6':('[size=74]⌫[/size]','#EEEEEE'), 'b7':('(','#DEDEDE'), 'b8':(')','#DEDEDE'),'b9':('7','F6F6F6'),
            'b10':('8','F6F6F6'),'b11':('9','F6F6F6'),'b12':('/','#DEDEDE'),'b13':('[u] ⬚ [/u]\n ⬚','#DEDEDE'), 'b14':('√⬚','#DEDEDE'),
            'b15':('4','F6F6F6'),'b16':('5','F6F6F6'),'b17':('6','F6F6F6'), 'b18':('×','#DEDEDE'),'b19':('⬚[sup]⬚[/sup]','#DEDEDE'),'b20':('x','#DEDEDE'),
            'b21':('1','F6F6F6'), 'b22':('2','F6F6F6'),'b23':('3','F6F6F6'),'b24':('-','#DEDEDE'),'b25':('π','#DEDEDE'), 'b26':('⬚[sup]2[/sup]','#DEDEDE'),
            'b27':('0','F6F6F6'),'b28':('.','F6F6F6'),'b29':('=','#DEDEDE'), 'b30':('+','#DEDEDE')}

                                                #this keyboard is constant and use for turn back 1st keys.
old_mykeyboard_keys={'b1': ('∫ dx','#EEEEEE'), 'b2':('abc','#EEEEEE'), 'b3':('[size=30]trigo∆[/size]','#EEEEEE'), 'b4':('[size=68]←[/size]','#EEEEEE'), 
            'b5':('[size=68]→[/size]','#EEEEEE'), 'b6':('[size=74]⌫[/size]','#EEEEEE'), 'b7':('(','#DEDEDE'), 'b8':(')','#DEDEDE'),'b9':('7','F6F6F6'),
            'b10':('8','F6F6F6'),'b11':('9','F6F6F6'),'b12':('/','#DEDEDE'),'b13':('[u] ⬚ [/u]\n ⬚','#DEDEDE'), 'b14':('√⬚','#DEDEDE'),
            'b15':('4','F6F6F6'),'b16':('5','F6F6F6'),'b17':('6','F6F6F6'), 'b18':('×','#DEDEDE'),'b19':('⬚[sup]⬚[/sup]','#DEDEDE'),'b20':('x','#DEDEDE'),
            'b21':('1','F6F6F6'), 'b22':('2','F6F6F6'),'b23':('3','F6F6F6'),'b24':('-','#DEDEDE'),'b25':('π','#DEDEDE'), 'b26':('⬚[sup]2[/sup]','#DEDEDE'),
            'b27':('0','F6F6F6'),'b28':('.','F6F6F6'),'b29':('=','#DEDEDE'), 'b30':('+','#DEDEDE')}

type_hint_text=['']

_keyboard_back = 0 

class ContentNavigationDrawer(MDBoxLayout):
    pass

class MenuScreen(Screen, TouchBehavior): #take TouchBehavior from kivymd for long-touch *we'll use this in key-delete while pressed long

    def checktouch(self): #virtual keyboard-close
        touch=self.ids.txt1.cursor_pos
        if Window.mouse_pos[1]<touch[1]-27 and self.ids.txt1.keyboard_mode=='managed': 
            self.ids.txt1.focus=False
        else:
            pass

    def checkfocus(self):
        check_focus=self.ids.txt1.focus
        global artifical_keyboard 
        current_opacity = 0.4
        if self.ids.bulb_icon.icon=='lightbulb-off': #change hint_text visibility
            current_opacity = 0
        if check_focus==True and self.ids.txt1.keyboard_mode=='managed': #create our keyboard when focus on textbox
                                                         
            artifical_keyboard=MDFloatLayout(size_hint_y=0.5) 
            mykeyboard=MDGridLayout(cols=6, rows=5, height='283dp',md_bg_color='#EEEEEE', spacing='0.50dp', size_hint_y=None)
            ahint_text=MDLabel(text=type_hint_text[-1], font_size='9dp',color='black' ,size_hint_y=None, y=mykeyboard.top + dp(5), halign='center', 
                adaptive_height=True, markup=True, opacity=current_opacity)
            for n,m in mykeyboard_keys.items():
                but=Button(text=str(m[0]), color='black', font_size='20sp', markup=True, font_name='dejavusansmono.ttf', background_normal=m[1], background_color=m[1],size_hint_y=None, height='56dp')
                mykeyboard.add_widget(but)  
                but.bind(on_press= lambda _,z=str(m[0]):self.mykeyborad_click(z))
                if n=='b6':
                    self.ids['key_delete']=but #for delete button
                    
            self.ids['keyboard_hint']=ahint_text 
            artifical_keyboard.add_widget(ahint_text)
            artifical_keyboard.add_widget(mykeyboard)   
            self.ids.box_layout.add_widget(artifical_keyboard)
                                  
        elif check_focus==False and self.ids.txt1.keyboard_mode=='managed':
            self.ids.box_layout.remove_widget(artifical_keyboard)
            mykeyboard_keys.update(old_mykeyboard_keys) #turn back our 1st keyboard
        
    def mykeyborad_click(self, z): #keyboard-on press
        try:
            if z=='[size=68]←[/size]':

                self.ids.txt1.focus=True
                self.ids.txt1.do_cursor_movement('cursor_left',control=False, alt=False)

            elif z=="[size=68]→[/size]":
                self.ids.txt1.focus=True
                self.ids.txt1.do_cursor_movement('cursor_right',control=False, alt=False)
                   
            elif z=='[size=74]⌫[/size]':
                self.ids.txt1.focus=True
                l=self.ids.txt1.cursor_index() 
                if l !=0:
                    self.ids.txt1.text = self.ids.txt1.text[:l-1]+''+self.ids.txt1.text[l:]
                    self.ids.txt1.cursor=self.ids.txt1.get_cursor_from_index(l-1) 
           
            else:
                l=self.ids.txt1.cursor_index()  
                length_z=len(z)
                self.ids.txt1.text = self.ids.txt1.text[:l]+z+self.ids.txt1.text[l:]
                self.ids.txt1.cursor = self.ids.txt1.get_cursor_from_index(l+length_z)
        except(Exception):
            pass

    def on_long_touch(self, *args): #delete textbox with long-touch
        try:
            l=self.ids.txt1.cursor_index()                                    
            if self.ids.key_delete.state=='down' and l != 0 :
                self.ids.txt1.focus=True
                self.ids.txt1.text=''
                if self.ids.txt1.text=='':
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

    def gohelp(self):
        self.manager.current='help'
        self.manager.get_screen('help').ids.helptoolbar.right_action_items=[["timeline-question"]]
        self.manager.get_screen('help').ids.helptoolbar.left_action_items=[["arrow-left",lambda x: self.manager.get_screen('help').back_menu()]]

    def follow(self): #type textbox like x^2+3*x, diff(x+2,x)...
        main_sign1=self.ids.txt1.text.replace("×","*")
        main_sign2=main_sign1.replace("÷","/")
        try:
            self.ids.lblcol.text=" "
            self.ids.lbl_blue.text="[Out]"   
                                            
            data=main_sign2
            sign0=sympify(data)
            sign_str=pretty(simplify(str(sign0)))  #pretty write **init_printing()***  
            sign_exp=sign_str.replace("ℯ","e") 
            self.ids.lbl1.text=sign_exp
             
            signs=pretty(sympify(main_sign2,evaluate=False)) 
            sign_exp_expr=signs.replace("ℯ","e")
            self.ids.lbl0.text=sign_exp_expr

            self.ids.lbl0.texture_update() #update texture
            self.ids.lbl1.texture_update()

            self.ids.lblcol.size_hint_y=self.ids.lbl1.texture_size[1]*0.0105 #red line set
            self.ids.lblcol.background_color=(176/255,3/255,3/255,0.8)
            self.ids.lblcol.texture_update()
            
                                   
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

class HelpScreen(Screen):
    def back_menu(self):
        self.manager.current='menu'

    

class sampleApp(MDApp):
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

kv=sampleApp().run()
