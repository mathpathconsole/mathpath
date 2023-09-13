                                    #Current ver== KivyMD version = 1.1.1 , Kivy version = 2.1.0 , SymPy version = 1.10.1
from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder      
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

class ContentNavigationDrawer(MDBoxLayout):
    pass

class MenuScreen(Screen):
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
