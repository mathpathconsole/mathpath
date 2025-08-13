from sympy import *
from kivy.core.window import Window
height_data0=[]
height_data1=[]
width_data0=[]
width_data1=[]
#here is shrinking or setting input and output labels.
def oto_width_main(self):  
    try:
        self.ids.lbl0.texture_update()
        self.ids.lbl1.texture_update()
        lbl0_width=Window.size[0]-56 
        lbl1_width=Window.size[0]-66                 
        if self.ids.lbl0.texture_size[0]>lbl0_width:
            width_data0.append(len(self.ids.lbl0.text))
            while self.ids.lbl0.texture_size[0]>lbl0_width:
                self.ids.lbl0.font_size -=0.2
                self.ids.lbl0.texture_update()
                if self.ids.lbl0.font_size<=0 or self.ids.lbl0.texture_size[0]<=lbl0_width:
                    self.ids.lbl0.texture_update()
                    break

        elif len(width_data0)!=0 and self.ids.lbl0.texture_size[0]<=lbl0_width: 
            if width_data0[0]>len(self.ids.lbl0.text):
                self.ids.lbl0.font_size="14dp"
                self.ids.lbl0.texture_update()
                width_data0.clear()

        if self.ids.lbl1.texture_size[0]>lbl1_width:
            width_data1.append(len(self.ids.lbl1.text))
            while self.ids.lbl1.texture_size[0]>lbl1_width:
                self.ids.lbl1.font_size -=0.2
                self.ids.lbl1.texture_update()
                if self.ids.lbl1.font_size<=0 or self.ids.lbl1.texture_size[0]<=lbl1_width:
                    self.ids.lbl1.texture_update()
                    break
         
        elif len(width_data1)!=0 and self.ids.lbl1.texture_size[0]<=lbl1_width: 
            if width_data1[0]>len(self.ids.lbl1.text):
                self.ids.lbl1.font_size="18dp"
                self.ids.lbl1.texture_update()
                width_data1.clear()

        if self.ids.txt1.text=="":
            self.ids.lbl_black.text="[In]"
            self.ids.lbl_blue.text="[Out]" 
        else:                               #for in-out and copy-paste
            self.ids.lbl_black.text=""
            self.ids.lbl_blue.text=""
                
        self.ids.lbl1.texture_update()
        self.ids.lbl0.texture_update()
                            
                    
    except(SympifyError,Exception):
        pass

    return

def oto_height_main(self):  
    try:
        self.ids.lbl0.texture_update()
        self.ids.lbl1.texture_update()
        h0=self.ids.lbl0.pos[1]-(0.5*self.ids.lbl0.texture_size[1])
        h1=self.ids.lbl1.pos[1]-(0.5*self.ids.lbl1.texture_size[1])
        h=h0-h1-self.ids.lbl1.texture_size[1]
        
        if h<=8: 
            height_data0.append(len(self.ids.lbl0.text))
            height_data1.append(len(self.ids.lbl1.text))
            while h<=8:
                self.ids.lbl0.font_size -=0.25
                self.ids.lbl1.font_size -= 0.2
                self.ids.lbl0.texture_update()
                self.ids.lbl1.texture_update()
                h=h0-h1-self.ids.lbl1.texture_size[1]
                if h>8:
                    self.ids.lbl0.texture_update()
                    self.ids.lbl1.texture_update()
                    break
                        
        elif h>8 and (len(height_data0)!=0 or len(height_data1)!=0):
            if height_data1[0]>len(self.ids.lbl1.text) and height_data0[0]>len(self.ids.lbl0.text):
                self.ids.lbl0.font_size="14dp"
                self.ids.lbl1.font_size="18dp"
                self.ids.lbl0.texture_update()
                self.ids.lbl1.texture_update()
                height_data0.clear()
                height_data1.clear()
            elif height_data1[0]>len(self.ids.lbl1.text) and height_data0[0]<len(self.ids.lbl0.text):
                self.ids.lbl1.font_size="18dp"
                self.ids.lbl1.texture_update()
                height_data1.clear()

            elif height_data1[0]<len(self.ids.lbl1.text) and height_data0[0]>len(self.ids.lbl0.text):
                self.ids.lbl0.font_size="14dp"
                self.ids.lbl0.texture_update()
                height_data0.clear()

        self.ids.lbl1.texture_update()
        self.ids.lbl0.texture_update()

        self.ids.lblcol.size_hint_y=self.ids.lbl1.texture_size[1]*0.0105 
        self.ids.lblcol.background_color=(176/255,3/255,3/255,0.8)
        self.ids.lblcol.texture_update()
                
                
    except(SympifyError,Exception):
        pass

    return
