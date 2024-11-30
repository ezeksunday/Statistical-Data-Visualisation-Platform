# pip install customtkinter
# pip install PIL
# pip install tkinter-tooltip
# pip install numpy,pandas,matplotlib,seaborn
# pip install tkkthemes
# pip install BeautifulSoup4
# pip install lxml
# pip install html5lib
import pathlib
import datetime
import os
import sqlite3
import matplotlib.tri as tri
import random
from tkinter import font
from tkinter.colorchooser import askcolor
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import *
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox,filedialog 
from tkinter import ttk
import tkinter as tk
import pandas as pd
from customtkinter import *
import customtkinter
from mpl_toolkits import mplot3d
from PIL import Image,ImageTk
from ttkthemes import ThemedStyle
from tktooltip import ToolTip 
import seaborn as sns   
import matplotlib.patches

class App(customtkinter.CTk):
        def __init__(self):
            super().__init__()
            customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
            customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
            self.width=self.winfo_screenwidth()
            self.height=self.winfo_screenheight()
            
            self.style=ThemedStyle()
            self.protocol('WM_DELETE_WINDOW',self.close_app) 
            self.style.theme_use('breeze')
            self.st=ttk.Style()
            
            self.st.configure("TCombobox", fieldbackground= "blue", background= "white")
            self.st.configure('Treeview',font='cambria 10 ')
            self.st.configure('Treeview.Heading',font='cambria 11 bold')
            self.photo=PhotoImage(file='images/data.png')
            self.iconphoto(False,self.photo)
            self.resizable(True,True)
        
            self.geometry(f"{self.width}x{self.height}+0+0")
            self.title("STATISTICAL DATA VISUALIZATION PLATFORM")
            self.output = None
            self.fig = None
            sns.set_theme(style='white')
            

            self.conn=sqlite3.connect('database_for_recent_files.db',detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
            self.cur=self.conn.cursor()
            sql='''CREATE TABLE IF NOT EXISTS file_holder(file_name VARCHAR(500),file_path VARCHAR(900),uploadtime TIMESTAMP, file_size VARCHAR(300))'''
            self.cur.execute(sql)
          
            
         
             
            # Images Used in App
            self.project_image=Image.open('images/project.png')
            self.project_image=self.project_image.resize((30,30))
            self.project_image=ImageTk.PhotoImage(self.project_image)
            
            self.search_image=Image.open('images/search.png')
            self.search_image=self.search_image.resize((30,30))
            self.search_image=ImageTk.PhotoImage(self.search_image)
            
            self.tk_img=Image.open('images/bg.jpg')
            self.tk_img=self.tk_img.resize((self.width-40,self.height-200))
            self.tk_img=ImageTk.PhotoImage(self.tk_img)
            
            self.import_image=Image.open('images/import.png')
            self.import_image=self.import_image.resize((20,20))
            self.import_image=ImageTk.PhotoImage(self.import_image)

            
            
            self.open_image=Image.open('images/open2.png')
            self.open_image=self.open_image.resize((30,30))
            self.open_image=ImageTk.PhotoImage(self.open_image)

            self.open_image_2=Image.open('images/open.png')
            self.open_image_2=self.open_image_2.resize((30,30))
            self.open_image_2=ImageTk.PhotoImage(self.open_image_2)
            
            self.recent_image=Image.open('images/recent.png')
            self.recent_image=self.recent_image.resize((30,30))
            self.recent_image=ImageTk.PhotoImage(self.recent_image)
            
            self.exit_image=Image.open('images/exit_app.png')
            self.exit_image=self.exit_image.resize((30,30))
            self.exit_image=ImageTk.PhotoImage(self.exit_image)

            self.help_image=Image.open('images/help.png')
            self.help_image=self.help_image.resize((30,30))
            self.help_image=ImageTk.PhotoImage(self.help_image)
            
            self.school=Image.open('images/bradford.png')
            self.school=self.school.resize((170,70))
            self.school=ImageTk.PhotoImage(self.school)
            
            
            
            #Colors used
            self.entry_color='#EAF6FA'
            self.button_bg ='#ffffff'# button color effects in the title bar (Hex color)
            self.left_bg='#000000'
            self.btn_for_cv='#000000'
            self.title_bar_bg ='gray'
            self.online_btn_color='#6596F2'



            #Top Menu Frameand Items
            self.top_frame=CTkFrame(self,fg_color=self.button_bg,height=50,corner_radius=0,border_width=5,border_color=self.button_bg,relief=RAISED)
            self.top_frame.pack(fill=X)
            
            self.logo_f=CTkLabel(self.top_frame,text='',image=self.school,fg_color='white',text_font=('cambria','14'),text_color='black',)
            self.logo_f.pack(side=LEFT,padx=1,pady=5)
            
            # File Menus
            self.menu_btn=CTkButton(self.top_frame,corner_radius=5,cursor='hand2',text='Files',fg_color='white',hover_color='lightgray',text_font=('cambria','10'),width=10,text_color='black',command=self.file_menu)
            #self.menu_btn.bind('<Enter>',self.file_menu)   
            self.menu_btn.pack(side=LEFT,padx=1,pady=5)
            
            # Statistics Menu
            self.stat_btn=CTkButton(self.top_frame,corner_radius=5,cursor='hand2',text='Statistical Data',fg_color='white',hover_color='lightgray',text_font=('cambria','10'),width=10,text_color='black',command=self.stat_menu)
            self.stat_btn.pack(side=LEFT,padx=1,pady=5)
           
           
            
            # 2 Dimensional Charts
            self.two_d_btn=CTkButton(self.top_frame,corner_radius=5,cursor='hand2',text='Select 2D Chart',fg_color='white',hover_color='lightgray',text_font=('cambria','10'),width=10,text_color='black',command=self.two_d_menu)
            self.two_d_btn.pack(side=LEFT,padx=1,pady=5)
            
            
            # 3 Dimensional Charts
            self.three_d_btn=CTkButton(self.top_frame,corner_radius=5,cursor='hand2',text='Select 3D Chart',fg_color='white',hover_color='lightgray',text_font=('cambria','10'),width=10,text_color='black',command=self.three_d_menu)
            self.three_d_btn.pack(side=LEFT,padx=1,pady=5)
            #self.three_d_btn.bind('<Enter>',self.three_d_menu)


            self.pre_processing_btn=CTkButton(self.top_frame,corner_radius=5,cursor='hand2',text='Preprocess data',fg_color='white',hover_color='lightgray',text_font=('cambria','10'),width=10,text_color='black',command=self.pre_processing_menu)
            self.pre_processing_btn.pack(side=LEFT,padx=1,pady=5)
            
           
       
            
            
            
            self.lab2=CTkLabel(self.top_frame,text='Online Dataset:',text_color='black',text_font=('cambria','10'),corner_radius=0).place(relx=0.59,rely=.18)
            
            # Download Dataset online
            self.online_entry=CTkEntry(self.top_frame,width=300,height=25,fg_color=self.entry_color,corner_radius=1,text_color='lightgray')
            self.online_entry.insert(0,'enter url for dataset')
            self.online_entry.bind('<FocusIn>',self.click)
            self.online_entry.bind('<Leave>',self.leave_fc)
            self.online_entry.place(relx=.687,rely=.2)
            self.online_download_button=CTkButton(self.top_frame,corner_radius=1,text='',image=self.search_image,width=25,height=6,fg_color=self.online_btn_color,hover_color='#000000',cursor='hand2',command=self.search_online_fnc)
            ToolTip(self.online_download_button,msg='click to download',parent_kwargs={'bg':'#0b0b0b','padx':5,'pady':1},fg='white',bg='#0b0b0b')
            self.online_download_button.place(relx=.9,rely=.2)

            self.help_btn=CTkButton(self.top_frame,corner_radius=1,text='',image=self.help_image,width=25,height=6,fg_color='#ffffff',hover_color='#ffffff',cursor='hand2',command=self.read_me)
            
            self.help_btn.place(relx=.94,rely=.2)
            
            
            
            
            #Left side Menus
            self.left_frame=CTkFrame(self,fg_color=self.left_bg,width=40,corner_radius=0,border_width=5,border_color=self.left_bg,)
            self.left_frame.pack(fill=Y,side=LEFT)
            # frame to hold dataset details
            self.detail_holder=CTkFrame(self,fg_color='white',corner_radius=0,width=400,height=self.height)
            self.detail_holder.pack(fill=Y,side=LEFT)
            
            
            
            
            self.spacer=CTkButton(self.left_frame,text='',width=40,height=30,fg_color=self.left_bg,hover_color=self.left_bg)
            self.spacer.pack(pady=9)
            self.recent_btn=CTkButton(self.left_frame,text='',image=self.recent_image,width=32,height=30,fg_color=self.left_bg,hover_color=self.title_bar_bg,corner_radius=5,command=self.recent_window)
            ToolTip(self.recent_btn,msg='See Recent Files Opened',parent_kwargs={'bg':'#0b0b0b','padx':5,'pady':1},fg='white',bg='#0b0b0b')
            self.recent_btn.pack(pady=5)
            
            self.new_btn=CTkButton(self.left_frame,text='',image=self.project_image,width=32,height=30,fg_color=self.left_bg,hover_color=self.title_bar_bg,corner_radius=5,command=self.new_pro)
            ToolTip(self.new_btn,msg='Open New Workbook',parent_kwargs={'bg':'#0b0b0b','padx':5,'pady':1},fg='white',bg='#0b0b0b')
            self.new_btn.pack(pady=5)
            self.open_btn=CTkButton(self.left_frame,text='',image=self.open_image,width=32,height=30,fg_color=self.left_bg,hover_color=self.title_bar_bg,corner_radius=5,command=self.open)
            ToolTip(self.open_btn,msg='Open Downloaded Dataset',parent_kwargs={'bg':'#0b0b0b','padx':5,'pady':1},fg='white',bg='#0b0b0b')
            self.open_btn.pack(pady=5)
            
            self.save_btn=CTkButton(self.left_frame,text='',image=self.exit_image,width=32,height=30,fg_color=self.left_bg,hover_color=self.title_bar_bg,corner_radius=5,command=self.close_app)
            ToolTip(self.save_btn,msg='Exit',parent_kwargs={'bg':'#0b0b0b','padx':5,'pady':1},fg='white',bg='#0b0b0b')
            self.save_btn.pack(pady=5)
            
                
            
            
           
            
            #Notebook Details
            self.note=ttk.Notebook(self.detail_holder,height=500,width=380)
            self.note.place(relx=0,rely=0)
            self.s_info_frame=CTkFrame(self.note,fg_color='white',corner_radius=0,height=400)
            self.s_info_frame.pack()
            self.attribute_frame=CTkFrame(self.note,fg_color='white',corner_radius=0)
            self.attribute_frame.pack(fill=BOTH,expand=1)
            self.note.add(self.attribute_frame,text='Data Attributes')
            self.note.add(self.s_info_frame,text='Statistical details')
            self.ls = Listbox(self.attribute_frame,bg='white',bd=0,font='cambria 12 bold',highlightbackground='white',
                              highlightcolor='white',selectborderwidth=0,selectbackground='white',selectforeground='black',
                              activestyle='none')
            self.ls.pack(side = LEFT, fill = BOTH,expand=1)
            self.scrol_info = ttk.Scrollbar(self.attribute_frame)
            self.scrol_info.pack(side = RIGHT, fill = Y)
            self.ls.config(yscrollcommand = self.scrol_info.set)
            self.scrol_info.config(command=self.ls.yview)
            
            self.down=CTkFrame(self.detail_holder,fg_color='white',corner_radius=10)
            self.down.place(relx=0,rely=.589,height=30,width=380)
            
            self.sec_frame = Listbox(self.s_info_frame,bg='white',bd=0,font='cambria 12 bold',highlightbackground='white',
                              highlightcolor='white',selectborderwidth=0,selectbackground='white',selectforeground='black',
                              activestyle='none')
            self.sec_frame.pack(side = LEFT, fill = BOTH,expand=1)
            self.scrol_info_y = ttk.Scrollbar(self.s_info_frame)
            self.scrol_info_y.pack(side = RIGHT, fill = Y)
            self.scrol_info_x_al = ttk.Scrollbar(self.down,orient=HORIZONTAL)
            self.scrol_info_x_al.pack(side = BOTTOM, fill = X)
            self.sec_frame.config(xscrollcommand = self.scrol_info_x_al.set,yscrollcommand = self.scrol_info_y.set)
            self.scrol_info_x_al.config(command=self.sec_frame.xview)
            self.scrol_info_y.config(command=self.sec_frame.yview)
            
            
            

            # Main items holder
            self.main=CTkFrame(self)
            self.main.pack(fill=BOTH,expand=1)

            
            self.main_app=Canvas(self.main,highlightbackground='white',highlightcolor='white',borderwidth=2)
            self.main_app.create_image(0, 0, image=self.tk_img, anchor="nw")
            self.main_app.pack(side=LEFT,expand=True,fill=BOTH)
            self.scrollty=ttk.Scrollbar(self.main,orient=VERTICAL,command=self.main_app.yview)
            self.scrollty.pack(fill=Y,side=RIGHT)
            self.main_app.bind('<Configure>',lambda e: self.main_app.configure(scrollregion=self.main_app.bbox('all')))
            
            
            self.graph_l=CTkLabel(self.main_app,text='GRAPH DISPLAY',text_font='Cambria 15 bold',fg_color='white',corner_radius=0)
            self.mapp=CTkFrame(self.main_app,width=800,height=300,fg_color='white',corner_radius=0,border_width=2,border_color='lightgray')
            self.data_h=CTkFrame(self.main_app,width=self.width,height=400,fg_color='white',corner_radius=0,)
            
            
            #Seperators
            self.sep=CTkFrame(self.main_app,width=self.width,fg_color='lightgray',height=5,border_color='lightgray',relief=GROOVE)
            self.sep2=CTkFrame(self.main_app,width=self.width-800,fg_color='#E8E8E8',height=2,border_color='lightgray',relief=GROOVE)
            self.sep3=CTkFrame(self.main_app,width=self.width,fg_color='lightgray',height=5,border_color='lightgray',relief=GROOVE)
            
            
            self.x_column=StringVar()
            self.y_column=StringVar()
            self.z_column=StringVar()
            #PLot Entry Boxes
            self.x_entry_val=CTkEntry(self.main_app,width=100,fg_color=self.entry_color,text_font="cambria 9",corner_radius=0)
            self.x_chooser=ttk.Combobox(self.main_app,state='readonly',width=17,font='arial 9 bold',textvariable=self.x_column)
            self.x_chooser['values']=(['Choose x column'])
            self.x_chooser.current(0)
            self.y_entry_val=CTkEntry(self.main_app,width=100,fg_color=self.entry_color,text_font="cambria 9",corner_radius=0)
            self.y_chooser=ttk.Combobox(self.main_app,state='readonly',width=17,font='arial 9 bold',textvariable=self.y_column)
            self.y_chooser['values']=(['Choose y column'])
            self.y_chooser.current(0)
            self.z_entry_val=CTkEntry(self.main_app,width=100,fg_color=self.entry_color,text_font="cambria 9",corner_radius=0)
            self.hue=ttk.Combobox(self.main_app,state='readonly',width=17,font='arial 9 bold',textvariable=self.z_column)
            self.hue['values']=(['Choose hue column'])
            self.hue.current(0)
            self.graph_type=CTkButton(self.main_app,text_font=('cambria','10'),text_color='white',text='GRAPH TYPE')
            
            self.x_entry_val.bind('<FocusIn>',self.color_x)
            self.y_entry_val.bind('<FocusIn>',self.color_y)
            self.z_entry_val.bind('<FocusIn>',self.color_z)
            self.x_entry_val.bind('<Leave>',self.leave_x)
            self.y_entry_val.bind('<Leave>',self.leave_y)
            self.z_entry_val.bind('<Leave>',self.leave_z)
            self.x_chooser.bind('<<ComboboxSelected>>', self.on_x_select) 
            self.y_chooser.bind('<<ComboboxSelected>>', self.on_y_select)
            self.hue.bind('<<ComboboxSelected>>', self.on_z_select)          
            
            self.optional_label=CTkLabel(self.main_app,corner_radius=0,text='Optional',fg_color='white',text_font=('cambria','10'),text_color='black')
            self.row_start_label=CTkLabel(self.main_app,corner_radius=0,text='Row start:',fg_color='white',text_font=('cambria','10'),text_color='black')
            self.row_end_label=CTkLabel(self.main_app,corner_radius=0,text='Row End:',fg_color='white',text_font=('cambria','10'),text_color='black')
            self.start_entry=CTkEntry(self.main_app,corner_radius=5,fg_color='white',text_font=('cambria','10'),text_color='black',width=90)
            self.end_entry=CTkEntry(self.main_app,corner_radius=5,fg_color='white',text_font=('cambria','10'),text_color='black',width=90)
            
            self.x_entry_label=CTkLabel(self.main_app,corner_radius=0,text='Select X values to plot:',fg_color='white',text_font=('cambria','11'),text_color='black')
            self.y_entry_label=CTkLabel(self.main_app,corner_radius=0,text='Select Y values to plot:',fg_color='white',text_font=('cambria','11'),text_color='black')
            self.z_entry_label=CTkLabel(self.main_app,corner_radius=0,text='Select Hue column:',fg_color='white',text_font=('cambria','11'),text_color='black')
            self.selected_graph_type=CTkLabel(self.main_app,corner_radius=0,text='Selected Graph',fg_color='white',text_font=('cambria','11'),text_color='black')
            
            self.plot_button=CTkButton(self.main_app,text='PLOT', text_font=('cambria','10'),fg_color=self.btn_for_cv,hover_color='#2DC703',text_color='white',command=self.main_plot)
            
            self.main_app.create_window((270,10),window=self.x_entry_val,anchor=NW)
            self.main_app.create_window((470,10),window=self.x_chooser,anchor=NW)
            self.main_app.create_window((270,60),window=self.y_entry_val,anchor=NW)
            self.main_app.create_window((470,60),window=self.y_chooser,anchor=NW)
            self.main_app.create_window((470,110),window=self.hue,anchor=NW)
            self.main_app.create_window((270,110),window=self.z_entry_val,anchor=NW)
            self.main_app.create_window((500,155),window=self.plot_button,anchor=NW)
            self.main_app.create_window((270,155),window=self.graph_type,anchor=NW)
            self.main_app.create_window((750,15),window=self.optional_label,anchor=NW)
            self.main_app.create_window((667,60),window=self.row_start_label,anchor=NW)
            self.main_app.create_window((825,60),window=self.row_end_label,anchor=NW)
            self.main_app.create_window((710,100),window=self.start_entry,anchor=NW)
            self.main_app.create_window((865,100),window=self.end_entry,anchor=NW)
            self.main_app.create_window((30,10),window=self.x_entry_label,anchor=NW)
            self.main_app.create_window((30,60),window=self.y_entry_label,anchor=NW)
            self.main_app.create_window((30,110),window=self.z_entry_label,anchor=NW)
            self.main_app.create_window((35,155),window=self.selected_graph_type,anchor=NW)
            self.main_app.create_window((10,200),window=self.sep,anchor=NW)
            self.main_app.create_window((10,750),window=self.sep3,anchor=NW)
            #self.main_app.create_window((300,180),window=self.sep2,anchor=NW)
            self.main_app.create_window((22,200),window=self.graph_l,anchor=NW)
            self.main_app.create_window((10,240),window=self.mapp,anchor=NW)
            self.main_app.create_window((2,750),window=self.data_h,anchor=NW)
            
           
            self.data_label=CTkLabel(self.data_h,text='IMPORTED DATA ',text_font='Cambria 15 bold',corner_radius=0).place(relx=0.005,rely=0)
            self.hold=CTkFrame(self.data_h,corner_radius=0)
            self.hold.place(rely=.1,height=250,width=1250)
            self.data_name=Label(self.data_h,text='',font='Cambria 10',bg='white')
            self.data_name.place(relx=0.18,rely=0.018)

            self.data_reupload=CTkButton(self.data_h,text='SEE ALL DATA',text_font='Cambria 10',text_color='white',corner_radius=2,command=self.open_reupload)
            self.data_reupload.place(relx=0.35,rely=.018)
            self.data_items=ttk.Treeview(self.hold)
            self.data_items.place(relheight=1,relwidth=1)
            treescrolly=ttk.Scrollbar(self.hold,orient='vertical',command=self.data_items.yview)
            treescrollx=ttk.Scrollbar(self.hold,orient='horizontal',command=self.data_items.xview)
            self.data_items.config(xscrollcommand=treescrollx.set,yscrollcommand=treescrolly.set)
            treescrolly.pack(side=RIGHT,fill=Y)
            treescrollx.pack(side=BOTTOM,fill=X)
            
          

           
        
        ###########Other functions###########
        

        def color_x(self,event):
            self.x_entry_val.config(fg_color='white')
        def color_y(self,event):
            self.y_entry_val.config(fg_color='white')
        def color_z(self,event):
            self.z_entry_val.config(fg_color='white')
        def leave_fc(self,event):
            if self.online_entry.get()=='':
                self.online_entry.config(fg_color=self.entry_color,text_color='black')
                self.online_entry.focus()
                self.online_download_button.config(fg_color=self.online_btn_color)
        
        def click(self,event) :
            if self.online_entry.get()=='enter url for dataset':
                self.online_entry.config(fg_color='white',text_color='black')
                self.online_download_button.config(fg_color=self.online_btn_color)
                self.online_entry.delete(0,END)
            elif self.online_entry.get()!='enter url for dataset':
                self.online_entry.config(fg_color='white',text_color='black')
                
            else:
                self.leave_fc
               
        def sum_up(self) :
            self.df.sum()       
        def file_menu(self):
            popup=Menu(self.top_frame,tearoff=False,font=('cambria','10'),bd=0,activebackground='#000000',activeforeground='#ffffff',bg='white')
            try:
                popup.add_command(label="New Project",command=self.new_pro)
                popup.add_command(label="Upload dataset",command=self.open)
                popup.tk_popup(70,73)
            finally:
                popup.grab_release()
        def stat_menu(self):
            popup=Menu(self.top_frame,tearoff=False,font=('cambria','10'),bd=0,activebackground='#000000',activeforeground='#ffffff',bg='white')
            try:
                
                
                popup.add_command(label="Dataset Information",command=self.dataset_info)
                popup.add_command(label="Dataset Description",command=self.descript)
                popup.add_command(label="Dataset Variance",command=self.var)
                popup.add_command(label="Dataset correlation",command=self.data_cor)
                popup.add_separator()
                sum_menu = Menu(popup, tearoff=0,font=('cambria','10'),bd=0,activebackground='#000000',activeforeground='#ffffff',bg='white')
                sum_menu.add_command(label='sum by row',command=self.dataset_sum_by_row)
                sum_menu.add_command(label='sum by column',command=self.dataset_sum_by_column)
                popup.add_cascade(label="Dataset Sum",menu=sum_menu)
                popup.add_command(label="dataset standard Deviation",command=self.dataset_std)
                popup.add_separator()
                # add a submenu
                other_menu = Menu(popup, tearoff=0,font=('cambria','10'),bd=0,activebackground='#000000',activeforeground='#ffffff',bg='white')
                other_menu.add_command(label='Mean Value by Column',command=self.dataset_mean)
                other_menu.add_command(label='Mean Value by Row',command=self.dataset_mean_2)
                other_menu.add_command(label='Median Value by Column',command=self.dataset_median)
                other_menu.add_command(label='Median Value by Row',command=self.dataset_median_2)
                other_menu.add_command(label='Mode Value',command=self.dataset_mode)
                other_menu.add_command(label='product of values',command=self.dataset_prod)
                other_menu.add_separator()
                other_menu.add_command(label='Minimum Value by row',command=self.dataset_min_by_row)
                other_menu.add_command(label='Minimum Value by column',command=self.dataset_min_by_column)
                other_menu.add_command(label='Maximium Value by row',command=self.dataset_max_by_row)
                other_menu.add_command(label='Maximum Value by column',command=self.dataset_max_by_column)
                other_menu.add_command(label='Unique values in each column',command=self.dataset_count)
                popup.add_cascade(label="Mean and others of Dataset",menu=other_menu)
                
                
                popup.tk_popup(190,73)
            finally:
                popup.grab_release()
          
        def two_d_menu(self):
            popup=Menu(self.top_frame,tearoff=False,font=('cambria','10'),bd=0,activebackground='#000000',activeforeground='#ffffff',bg='white')
            try:
                # Basic plots
                basic_menu = Menu(popup, tearoff=0,font=('cambria','10'),bd=0,activebackground='#000000',activeforeground='#ffffff',bg='white')
                popup.add_cascade(label="Basic Charts",menu=basic_menu)
                def l():
                    self.graph_type.config(text='line plot')
                   
                def sc():
                    self.graph_type.config(text='Scatter plot')
                    
                def st():
                    self.graph_type.config(text='Stem plot')
                    
                def sp():
                    self.graph_type.config(text='Step plot')
                    
                def sk():
                    self.graph_type.config(text='Stack plot')
          
                basic_menu.add_command(label='Line Plot',command=l)
                basic_menu.add_command(label='Scatter Plot',command=sc)
                basic_menu.add_command(label='Stem plot',command=st)
                basic_menu.add_command(label='Step plot',command=sp)
                basic_menu.add_command(label='Stack plot',command=sk)
                
                # Stat plots
                stat_menu = Menu(popup, tearoff=0,font=('cambria','10'),bd=0,activebackground='#000000',activeforeground='#ffffff',bg='white')
                
                pie_menu = Menu(popup, tearoff=0,font=('cambria','10'),bd=0,activebackground='#000000',activeforeground='#ffffff',bg='white')
                def p():
                    self.graph_type.config(text='pie plot')
                    
                def don():
                    self.graph_type.config(text='Doughnut plot')
                def bar():
                    self.graph_type.config(text='Bar chart')
                def his():
                    self.graph_type.config(text='Histogram')
                def diis():
                    self.graph_type.config(text='EC Distribution plot')
                def bx():
                    self.graph_type.config(text='Box plot')
                def cx():
                    self.graph_type.config(text='point plot')
                def cxd():
                    self.graph_type.config(text='Count plot')
                def dis():
                    self.graph_type.config(text='Density plot')
                def bub():
                    self.graph_type.config(text='Bubble chart')
                def err():
                    self.graph_type.config(text='Error plot')
                def ev():
                    self.graph_type.config(text='Event plot')
                def hx():
                    self.graph_type.config(text='Hexbin plot')
                def hp():
                    self.graph_type.config(text='Heatmap')
                def vl():
                    self.graph_type.config(text='Violin plot')
                def strp():
                    self.graph_type.config(text='Strip plot')
                def lm():
                    self.graph_type.config(text='Linear model plot')
                def sp():
                    self.graph_type.config(text='Swarm plot')
                def bp():
                    self.graph_type.config(text='Boxen plot')
                def rp():
                    self.graph_type.config(text='Residual plot')
                def cxd1():
                    self.graph_type.config(text='Contour plot')
                def dis1():
                    self.graph_type.config(text='Quiver plot')
                
                pie_menu.add_command(label='Pie Plot',command=p)
                pie_menu.add_command(label='Doughnut Plot',command=don)
                stat_menu.add_cascade(label='Pie Charts',menu=pie_menu)
                stat_menu.add_command(label='Bar plot',command=bar)
                stat_menu.add_command(label='Histogram',command=his)
                stat_menu.add_command(label='EC Distribution plot',command=diis)
                stat_menu.add_command(label='Count plot',command=cxd)
                stat_menu.add_command(label='Density plot',command=dis)
                stat_menu.add_command(label='point plot',command=cx)
                stat_menu.add_command(label='Box plot',command=bx)
                stat_menu.add_command(label='Bubble chart',command=bub)
                stat_menu.add_command(label='Error plot',command=err)
                stat_menu.add_command(label='Event plot',command=ev)
                stat_menu.add_command(label='Hexbin plot',command=hx)
                stat_menu.add_command(label='Heatmap',command=hp)
                stat_menu.add_command(label='Violin plot',command=vl)
                stat_menu.add_command(label='Strip plot',command=strp)
                stat_menu.add_command(label='Linear model plot',command=lm)
                stat_menu.add_command(label='Swarm plot',command=sp)
                stat_menu.add_command(label='Boxen plot',command=bp)
                stat_menu.add_command(label='residual plot',command=rp)
                popup.add_cascade(label="Statistical Plots",menu=stat_menu)
                
                # Array plots
                array_menu = Menu(popup, tearoff=0,font=('cambria','10'),bd=0,activebackground='#000000',activeforeground='#ffffff',bg='white')
                array_menu.add_command(label='Contour plot',command=cxd1)
                array_menu.add_command(label='Quiver plot',command=dis1)
                popup.add_cascade(label="Array Plots",menu=array_menu)
                popup.tk_popup(300,73)
            finally:
                popup.grab_release()
                
            
            
        def three_d_menu(self):
            popup=Menu(self.top_frame,tearoff=False,font=('cambria','10'),bd=0,activebackground='#000000',activeforeground='#ffffff',bg='white')
            try:
                def l3d():
                    self.graph_type.config(text='3D Scatter plot')
                def bar3d():
                    self.graph_type.config(text='3D Bar chart')
                def line3d():
                    self.graph_type.config(text='3D Line plot')
                def surface3d():
                    self.graph_type.config(text='3D Surface plot')
                def contour3d():
                    self.graph_type.config(text='3D contour plot')
                def stem3d():
                    self.graph_type.config(text='3D stem plot')
                def quiver3d():
                    self.graph_type.config(text='3D Quiver plot') 
                def tri3d():
                    self.graph_type.config(text='Triangular 3D plot')
                def tric3d():
                    self.graph_type.config(text='Triangular Contour 3D plot')
                def wire3d():
                    self.graph_type.config(text='3D Wireframe plot')
                def pc3d():
                    self.graph_type.config(text='Parametric curve')  
                popup.add_command(label="3D Bar plot",command=bar3d)
                popup.add_command(label="3D Line plot",command=line3d)
                popup.add_command(label="3D Surface plot",command=surface3d)
                popup.add_command(label="3D contour plot",command=contour3d)
                popup.add_separator()
                popup.add_command(label="3D Scatter plot",command=l3d)
                popup.add_command(label="3D stem plot",command=stem3d)
                popup.add_command(label="3D Quiver plot",command=quiver3d)
                popup.add_separator()
                popup.add_command(label='3D Wireframe plot',command=wire3d)
                popup.add_command(label='Parametric curve',command=pc3d)
                popup.add_command(label='Triangular 3D plot',command=tri3d)
                popup.add_command(label='Triangular contour 3D plot',command=tric3d)
                popup.tk_popup(410,73)
            finally:
                popup.grab_release()
        def pre_processing_menu(self) :
            popup=Menu(self.top_frame,tearoff=False,font=('cambria','10'),bd=0,activebackground='#000000',activeforeground='#ffffff',bg='white')
            try:
                popup.add_command(label='Drop empty rows',command=self.drop_empty_row)
                popup.add_command(label='Remove columns will empty values',command=self.drop_empty)
                popup.add_command(label='Fill empty values Automatically',command=self.fill_na)
                popup.add_command(label='Fill empty values manually',command=self.fill_na_1)
                popup.add_command(label='Drop irrelevant rows',command=self.drop_row)
                popup.add_command(label='Drop irrelevant rows by range',command=self.drop_row_index)
                popup.add_command(label='Remove irrelevant columns',command=self.drop_column)
                
                popup.tk_popup(500,73)
            finally:
                popup.grab_release() 

         



    #############================================OPEN FILE FUNCTION=============###############
        def search_online_fnc(self):
            try:
                self.clearonline_data()
                self.clear_plot()
                self.online_url=self.online_entry.get()
                messagebox.showinfo('downloading file','be patatient file is downloading click ok')
                
                name=str(self.online_url)
                self.data_items['columns']=''
                self.x_chooser['values']=(['Choose x column'])
                self.x_chooser.current(0)
                self.y_chooser['values']=(['Choose y column'])
                self.y_chooser.current(0)
                self.hue['values']=(['Choose hue column'])
                self.hue.current(0)
                self.graph_type.config(text='selected graph')
                self.df=''
                s=str(self.online_url)
                s=s.split('/')
                s=s[-1]
                s=str(s)
                s=s[7:]
               
                self.data_name.config(text=s)
                name=str(s)
                if name.endswith('.csv'):
                    self.df=pd.read_csv(self.online_url)
                    head=list(self.df.columns)
                    
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    
                        
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])

                if name.endswith('.arff'):
                    self.df=pd.loadarff(self.online_url)
                    self.df=pd.DataFrame(self.df[0])
                    head=list(self.df.columns)
                    
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    
                        
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])


                if name.endswith('.data') or name.endswith('.dat'):
                    self.df=pd.read_csv(self.filename,names=['col1','col2'])
                    head=list(self.df.columns)
                    
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    
                
                            
                            
        ########Opening different file formats###########
                if name.endswith('.txt'):
                    self.df=pd.read_csv(self.online_url)
                    head=list(self.df.columns)
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])
                if name.endswith('.html') or name.endswith(''):
                    self.df=pd.read_html(self.online_url)
                    self.df=self.df[0]
                    head=list(self.df.columns)
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])
                              
                if name.endswith('.json'):
                    self.df=pd.read_json(self.online_url, orient=None, typ='frame',convert_axes=None, convert_dates=True)
                    
                    head=list(self.df.columns)
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])
                             
                if name.endswith('.xlsx'):
                    self.df=pd.read_excel(self.online_url)
                    head=list(self.df.columns)
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])
                    return None
                 

                
                
            except FileNotFoundError:
                pass
            except ValueError:
                pass
            except Exception as e:
                messagebox.showerror('An error has occured','An error has occured check your internet or it could be from the dataset')
        
        #open file
        def open(self):
            self.filename=filedialog.askopenfilename(initialdir=os.path.expanduser('~/Documents'),title='Upload File',filetypes=(('All Files','*.*'),('xlsx files','*.xlsx'),('csv files','*.csv'),('Text files','*.txt'),('Html files','*.html'),('JSON Files','*.json')))
            self.add_data() 


            
            try:
                self.clear_data()
                self.clear_plot()
                self.data_items['columns']=''
                self.x_chooser['values']=(['Choose x column'])
                self.x_chooser.current(0)
                self.y_chooser['values']=(['Choose y column'])
                self.y_chooser.current(0)
                self.hue['values']=(['Choose hue column'])
                self.hue.current(0)
                self.graph_type.config(text='selected graph')
                self.df=''
                s=str(self.filename)
                s=s.split('/')
                s=s[-1]
               
                self.data_name.config(text=s)
                name=str(s)
                
                

                if name.endswith('.csv'):
                    self.df=pd.read_csv(self.filename)
                    head=list(self.df.columns)
                    
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    
                        
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])
                            

                if name.endswith('.data') or name.endswith('.dat'):
                    self.df=pd.read_csv(self.filename,names=['col1','col2'])
                    head=list(self.df.columns)
                    
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    
                        
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])
                            
                if name.endswith('.html'):
                    self.df=pd.read_csv(self.filename)
                    self.df=self.df[0]
                    head=list(self.df.columns)
                    
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    
                        
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])
                                       
        ########Opening different file formats###########
                if name.endswith('.txt'):
                    self.df=pd.read_fwf(self.filename)
                    head=list(self.df.columns)
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])
                              
                if name.endswith('.json'):
                    self.df=pd.read_json(self.filename, orient=None, typ='frame',convert_axes=None, convert_dates=True)
                    
                    head=list(self.df.columns)
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])
                             
                if name.endswith('.xlsx'):
                    self.df=pd.read_excel(self.filename)
                    head=list(self.df.columns)
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])
                     
                     
                    return None
                  
            except FileNotFoundError:
                messagebox.showerror('Invalid','File Cannnot be loaded due to error')
            except ValueError:
                messagebox.showerror('Invalid Dataset','Invalid file format')






        ################================DATABASE CONNECTION=========================########################
        def add_data(self):
          try:
              self.name=str(self.filename)
              self.name=self.name.split('/')
              self.name=self.name[-1]
              si=os.path.getsize(self.filename)
              self.size=round(float(si)/1024,2)
              self.filename=str(self.filename)
              s=datetime.datetime.now()
              self.upt=pd.to_datetime(s)
              self.upt=self.upt.round('S')
              self.uploadtime=str(self.upt)
              self.filesize=str(self.size)+'KB'
              sql="INSERT INTO file_holder VALUES (?,?,?,?)"
              self.cur.execute(sql,(self.name,self.filename,self.uploadtime,self.filesize))
              self.conn.commit()
          except Exception:
              pass 

          


        def open_2(self):


            
            try:
                self.data_items['columns']=''
                self.x_chooser['values']=(['Choose x column'])
                self.x_chooser.current(0)
                self.y_chooser['values']=(['Choose y column'])
                self.y_chooser.current(0)
                self.hue['values']=(['Choose hue column'])
                self.hue.current(0)
                self.graph_type.config(text='selected graph')
                self.df=''
                s=str(self.filename)
                s=s.split('/')
                s=s[-1]
               
                self.data_name.config(text=s)
                name=str(s)
                
                

                if name.endswith('.csv'):
                    self.df=pd.read_csv(self.filename)
                    head=list(self.df.columns)

                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    
                        
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])
                            

                if name.endswith('.data') or name.endswith('.dat'):
                    self.df=pd.read_csv(self.filename,names=['col1','col2'])
                    head=list(self.df.columns)
                    
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    
                        
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])
                            
                if name.endswith('.html'):
                    self.df=pd.read_csv(self.filename)
                    self.df=self.df[0]
                    head=list(self.df.columns)
                    
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    
                        
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])
                                       
        ########Opening different file formats###########
                if name.endswith('.txt'):
                    self.df=pd.read_fwf(self.filename)
                    head=list(self.df.columns)
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])
                              
                if name.endswith('.json'):
                    self.df=pd.read_json(self.filename, orient=None, typ='frame',convert_axes=None, convert_dates=True)
                    
                    head=list(self.df.columns)
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])
                             
                if name.endswith('.xlsx'):
                    self.df=pd.read_excel(self.filename)
                    head=list(self.df.columns)
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])
                     
                     
                    return None
                  
            except FileNotFoundError:
                messagebox.showerror('Invalid','File Cannnot be loaded due to error')
            except ValueError:
                messagebox.showerror('Invalid Dataset','Invalid file format')





        ################================DATABASE CONNECTION=========================########################
        def add_data(self):
          try:
              self.name=str(self.filename)
              self.name=self.name.split('/')
              self.name=self.name[-1]
              si=os.path.getsize(self.filename)
              self.size=round(float(si)/1024,2)
              self.filename=str(self.filename)
              s=datetime.datetime.now()
              self.upt=pd.to_datetime(s)
              self.upt=self.upt.round('S')
              self.uploadtime=str(self.upt)
              self.filesize=str(self.size)+'KB'
              sql="INSERT INTO file_holder VALUES (?,?,?,?)"
              self.cur.execute(sql,(self.name,self.filename,self.uploadtime,self.filesize))
              self.conn.commit()
          except Exception:
              pass 
          

        def fetch_data(self):
          try:
              self.cur.execute('SELECT * FROM file_holder ORDER BY uploadtime DESC')
              rows=self.cur.fetchall()
              rows=rows[:10]
              for x in rows:
                
                self.dt_holder=CTkFrame(self.hdr,width=350,height=50,corner_radius=0,fg_color='white')
                self.dt_holder.pack(pady=3)
                self.bt_file=CTkButton(self.dt_holder,image=self.open_image_2,text='',width=5,corner_radius=0,fg_color='white',hover_color='lightgray')
                self.bt_file.place(relx=0.2)
                d='    '+str(x[0])+'   '+str(x[2])
                self.file_d=CTkButton(self.dt_holder,text=d,text_font='cambria 10 bold',corner_radius=0,fg_color='white',hover_color='#e7e3e2',command=self.open,width=250)
                self.file_d.place(relx=0.3)
              self.conn.commit()
              
          except Exception as e:
        
            messagebox.showerror('invalid request','You made an invalid selection')
        

        


     ######################STATISTICAL INFORMATION ON EACH UPLOADED DATASET###########
        def clear_stat_info(self):
            try:
              self.sec_frame.delete(0,END)
            except Exception:
              pass

        def dataset_info(self) :
            try:
                self.clear_stat_info()
                self.sec_frame.insert(END,'DATA SET INFROMATION')
                self.sec_frame.insert(END,'RangeIndex:'+str(self.df.shape[0])+' Entries,'+'0 to '+str(self.df.shape[0]-1))
                self.sec_frame.insert(END,'Data Columns (total '+str(self.df.shape[1])+' columns)')
                self.sec_frame.insert(END,'#'+'   Column    '+'  Non-null Count       '+'    Dtype')
                self.sec_frame.insert(END,'--------------------------------------------------------------')
                data_types=list(self.df.dtypes)
                columns_info=list(self.df.columns)

                for x in range(len(data_types)):
                    row_num=self.df.shape[0]-self.df[columns_info[x]].isna().sum()
                    self.sec_frame.insert(END,str(x)+'   '+str(columns_info[x])+':'+str(row_num)+' Non-null Values   '+str(data_types[x]))
                
                self.sec_frame.insert(END,'File shape:'+str(self.df.shape[0])+' rows,'+str(self.df.shape[1])+' columns')
            except Exception as e:
                messagebox.showerror('invalid dataset','Pleas a valid datset is needed!')



        def col_select(self,event):
            try:
              self.col_selected=self.col_names.get()
              if self.col_selected=='Choose x column':
                  pass
              else:
                  self.column_entry.delete('0', 'end') 
                  self.column_entry.insert('end', self.col_selected)
            except Exception:
              pass
        def column_chooser(self):
            try:
                self.frame_1=Toplevel(app)
                self.frame_1.resizable(False,False)
                self.frame_1.geometry('390x170+300+200')
                self.frame_1.config(background='white')
                self.frame_1.title('COLUMN CHOOSER')
                self.photo=PhotoImage(file='images/data.png')
                self.frame_1.iconphoto(False,self.photo)
                Label(self.frame_1,text='Select column to check its correlation with others.',font='cambria 11 bold',bg='white').pack(pady=2)
                Label(self.frame_1,text='To correlate all columns, Just click ok without selecting a column',font='cambria 10',bg='white').pack(padx=2)
                self.column_entry=CTkEntry(self.frame_1,corner_radius=5)
                self.column_entry.pack()
                self.col_n=StringVar()
                head=list(self.df.columns)
                self.col_names=ttk.Combobox(self.frame_1,state='readonly',width=15,font='arial 10 bold',textvariable=self.col_n)
                self.col_names['values']=(head)
                self.col_names.current(0)
                self.col_names.bind('<<ComboboxSelected>>', self.col_select)
                self.col_names.pack(pady=3)
                self.column_btn=CTkButton(self.frame_1,text='OK',command=self.corr_val,corner_radius=0)
                self.column_btn.pack(pady=3)
            except Exception:
                messagebox.showerror('Error','invalid selection')
        
        def corr_val(self):
            try:
                self.clear_stat_info()
                
                self.sec_frame.insert(END,'DATA SET CORRELATION')
                y=self.column_entry.get()
                if self.column_entry.get()=='':
                    
                    self.sec_frame.insert(END,self.df.corr())

                else:
                    head=list(self.df.columns)
                    

                    if self.df.dtypes[y]==np.int64 or self.df.dtypes[y]==np.float64:
                        self.sec_frame.insert(END,'CORRELATION BETWEEN '+str(y)+' AND OTHER COLUMNS')
                        for x in head:
                            if self.df.dtypes[x]==np.int64 or self.df.dtypes[x]==np.float64:
                                self.sec_frame.insert(END,'correlation with '+str(x)+'='+str(round(self.df[y].corr(self.df[x]),4)))

                            else:
                                pass
                    
                    else:
                        messagebox.showerror('Invalid column','selected column must contain integers or float')

                self.frame_1.destroy()
            except Exception as e:
                messagebox.showerror('Invalid selection','check selected column or error from dataset')
            
        def data_cor(self):
            try:
                columns_info=list(self.df.columns)
                self.column_chooser()
            except Exception:
                messagebox.showerror('Invalid request','Valid dataset is required')

        def var(self):
            try:
                self.clear_stat_info()
                x=dict(self.df.var())
                self.sec_frame.insert(END,'DATA SET VARIENCE')
                for u,v in x.items():
                    self.sec_frame.insert(END,str(u)+':'+str(round(v,4)))
            except Exception:
                messagebox.showerror('Invalid Dataset','Valid dataset is required')

        def dataset_std(self):
            try:
                self.clear_stat_info()
                self.sec_frame.insert(END,'DATA SET STANDARD DIVIATION')
                x=dict(self.df.std())
                for u,v in x.items():
                    self.sec_frame.insert(END,str(u)+':'+str(round(v,4)))
            except Exception:
                messagebox.showerror('Invalid Dataset','Valid dataset is required')

        def dataset_sum_by_row(self):
            try: 
                self.clear_stat_info()
                x=dict(self.df.sum(axis=1))
                self.sec_frame.insert(END,'DATA SET SUM BY ROW')
                for k,v in x.items():
                    self.sec_frame.insert(END,str(k)+':'+str(v))
            except Exception:
                messagebox.showerror('Invalid Dataset','Valid dataset is required')

        def dataset_sum_by_column(self):
            try: 
                self.clear_stat_info()
                x=dict(self.df.sum())
                self.sec_frame.insert(END,'DATA SET SUM BY COLUMN')
                for k,v in x.items():
                    self.sec_frame.insert(END,str(k)+':'+str(v))
            except Exception:
                messagebox.showerror('Invalid Dataset','Valid dataset is required')
        
        def descript(self):
            try:
                self.clear_stat_info()
                df_head=list(self.df.columns)
                self.sec_frame.insert(END,'DATA SET DESCRIPTION')
                for x in df_head:
                    self.sec_frame.insert(END,str(x)+' column')
                    for u,j in dict(self.df[x].describe(include='all')).items():
                        self.sec_frame.insert(END,str(u)+':'+str(j))
                    self.sec_frame.insert(END,' ')   
            except Exception as e:
                
                messagebox.showerror('Invalid Dataset','Valid dataset is required')

        def dataset_count(self):
            try:
                self.clear_stat_info()
                self.sec_frame.insert(END,'DATA SET UNIQUE VALUES IN COLUMNS')
                for x in self.df.columns:
                  self.sec_frame.insert(END,str(x)+' column')
                  for u,j in dict(self.df[x].value_counts()).items():
                    self.sec_frame.insert(END,str(u)+':'+str(j)+' Times')
                  self.sec_frame.insert(END,' ')
            except Exception as e:
            
              messagebox.showerror('Invalid Dataset','Valid dataset is required')
      
        def dataset_mean(self):
            try:
                self.clear_stat_info()
                self.sec_frame.insert(END,'DATA SET MEAN')
                for k,v in dict(self.df.mean()).items():
                    self.sec_frame.insert(END,str(k)+':'+str(round(v,4)))
            except Exception as e:
                messagebox.showerror('Invalid Dataset','Valid dataset is required')
        def dataset_median(self):
            try:
                self.clear_stat_info()
                self.sec_frame.insert(END,'DATA SET MEDIAN')
                for k,v in dict(self.df.median()).items():
                    self.sec_frame.insert(END,str(k)+':'+str(round(v,4)))
            except Exception as e:
                messagebox.showerror('Invalid Dataset','Valid dataset is required')
        def dataset_mean_2(self):
            try:
                self.clear_stat_info()
                self.sec_frame.insert(END,'DATA SET MEAN BY ROW')
                for k,v in dict(self.df.mean(axis=1)).items():
                    self.sec_frame.insert(END,str(k)+':'+str(round(v,4)))
            except Exception as e:
                messagebox.showerror('Invalid Dataset','Valid dataset is required')
        def dataset_median_2(self):
            try:
                self.clear_stat_info()
                self.sec_frame.insert(END,'DATA SET MEDIAN BY ROW')
                for k,v in dict(self.df.median(axis=1)).items():
                    self.sec_frame.insert(END,str(k)+':'+str(round(v,4)))
            except Exception as e:
                messagebox.showerror('Invalid Dataset','Valid dataset is required')
        def dataset_mode(self):
            try:
                self.clear_stat_info()
                
                df_head=list(self.df.columns)
                self.sec_frame.insert(END,'DATA SET MODE')
                for x in df_head:
                    self.sec_frame.insert(END,str(x)+' column\n')
                    self.sec_frame.insert(END,str(self.df[x].mode()[0]))
            except Exception as e:
                messagebox.showerror('Invalid Dataset','Valid dataset is required')
        def dataset_prod(self):
            try:
                self.clear_stat_info()
                
                df_head=list(self.df.columns)
                self.sec_frame.insert(END,'DATA SET PRODUCT BY COLUMN')
                s=dict(self.df.prod())
                for u,v in s.items():
                    self.sec_frame.insert(END,str(u)+':'+str(round(v,4)))
            except Exception as e:
                messagebox.showerror('Invalid Dataset','Valid dataset is required')

        def dataset_max_by_column(self):
            try:
                self.clear_stat_info()
                self.sec_frame.insert(END,'DATA SET MAXIMUM VALUES IN EACH COLUMN')
                x=dict(self.df.max())
                for u,v in x.items():
                    self.sec_frame.insert(END,str(u)+':'+str(v))
            except Exception as e:
                messagebox.showerror('Invalid Dataset','An error has occured from your selection check again')
        def dataset_max_by_row(self):
            try:
                self.clear_stat_info()
                self.sec_frame.insert(END,'DATA SET MAXIMUM VALUES IN EACH ROW')
                x=dict(self.df.max(axis=1))
                for u,v in x.items():
                    self.sec_frame.insert(END,str(u)+':'+str(v))
            except Exception as e:
                messagebox.showerror('Invalid Dataset','Valid dataset is required')

        def dataset_min_by_column(self):
            try:
                self.clear_stat_info()
                self.sec_frame.insert(END,'DATA SET MINIMUM VALUES IN EACH COLUMN')
                x=dict(self.df.min())
                for u,v in x.items():
                    self.sec_frame.insert(END,str(u)+':'+str(v))
            except Exception as e:
                messagebox.showerror('Invalid Dataset','Valid dataset is required')
        def dataset_min_by_row(self):
            try:
                self.clear_stat_info()
                self.sec_frame.insert(END,'DATA SET MINIMUM VALUES IN EACH ROW')
                x=dict(self.df.min(axis=1))
                for u,v in x.items():
                    self.sec_frame.insert(END,str(u)+':'+str(v))
            except Exception as e:
                messagebox.showerror('Invalid Dataset','Valid dataset is required')
                    
    ################selecting Values to be plotted#######
        def leave_x(self,event):
            self.x_entry_val.focus()
        def leave_y(self,event):
            self.y_entry_val.focus()
        def leave_z(self,event):
            self.z_entry_val.focus()

        def on_x_select(self,event):
            self.x_selected=self.x_chooser.get()
            if self.x_selected=='Choose x column':
                pass
            else:
                self.x_entry_val.delete('0', 'end') 
                self.x_entry_val.insert('end', self.x_selected)
                self.x_entry_val.config(fg_color='white') 
        def on_y_select(self,event):
            self.y_selected=self.y_chooser.get()
            if self.y_selected=='Choose y column':
                pass
            else:
                self.y_entry_val.delete('0', 'end')  # remove previous content
                self.y_entry_val.insert('end', self.y_selected)
                self.y_entry_val.config(fg_color='white')
        def on_z_select(self,event):
            self.z_selected=self.hue.get()
            if self.z_selected=='Choose z column':
                pass
            else:
                self.z_entry_val.delete('0', 'end')  # remove previous content
                self.z_entry_val.insert('end', self.z_selected)
                self.z_entry_val.config(fg_color='white')                       
    ######################################All plots in the app##########
    ####-----------------------line plot-------------------######
        def line_plot(self):
            try:
                self.clear_plot()
                self.z_entry_val.config(state='normal')
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
               
                
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)

                if self.z_entry_val.get()=='':
                    sns.lineplot(data=self.df,x=x,y=y,ax=self.plot1)
                    #plt.xticks(rotation='vertical')
                    #self.plot1.locator_params(axis='y',nbins=10)
                else:
                    z=self.df.loc[:,self.z_entry_val.get()]
                    sns.lineplot(data=self.df,x=x,y=y,ax=self.plot1,hue=z)
                self.plot1.set_xlabel(self.x_selected)
                self.plot1.set_ylabel(self.y_selected)

                if type(self.x_selected[1])=='int' or type(self.y_selected[1])=='int':
                    self.plot1.set_xlim(left=self.df.iloc[1,self.df.columns.get_loc(self.x_entry_val.get())], right=self.df.iloc[-1,self.df.columns.get_loc(self.x_entry_val.get())])
                    self.plot1.set_ylim(self.df.iloc[1,self.df.columns.get_loc(self.x_entry_val.get())],self.df.iloc[-1,self.df.columns.get_loc(self.x_entry_val.get())])
                self.plot1.set_title('A GRAPH OF '+str(self.x_selected).upper() +' AGAINST '+ str(self.y_selected).upper())

                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()
                
            except Exception as e:
                messagebox.showerror('Invalid format provided','Errors from parameters selection'+str(e))            
    #--------------------------------------scatter plot-----------#           
        def scatter_plot(self):
            try:
                self.clear_plot()
                self.z_entry_val.config(state='normal')
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                if self.z_entry_val.get()=='':
                    sns.scatterplot(data=self.df,x=x,y=y,ax=self.plot1)
                else:
                    z=self.df.loc[:,self.z_entry_val.get()]
                    sns.scatterplot(data=self.df,x=x,y=y,ax=self.plot1,marker='o',palette='viridis',hue=z)
                self.plot1.set_xlabel(self.x_selected)
                self.plot1.set_ylabel(self.y_selected)
                self.plot1.set_title('A GRAPH OF '+str(self.x_selected).upper() +' AGAINST '+ str(self.y_selected).upper())
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()    
            except Exception as e:
                messagebox.showerror('Invalid format provided','Errors from parameters selection'+str(e))
                          
    #--------------------------------------stem plot-----------#           
        def stem_plot(self):
            try:
                self.clear_plot()
                self.z_entry_val.config(state='disabled')
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                self.plot1.plot(x,y,color='green')
                self.plot1.set_xlabel(self.x_selected)
                self.plot1.set_ylabel(self.y_selected)
                self.plot1.set_title('A GRAPH OF '+str(self.x_selected).upper() +' AGAINST '+ str(self.y_selected).upper())
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()   
            except Exception as e:
                messagebox.showerror('Invalid format provided','Errors from parameters selection'+str(e))
                
                    
    #--------------------------------------step plot-----------#           
        def step_plot(self):
            try:
                self.clear_plot()
                self.z_entry_val.config(state='disabled')
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                self.plot1.step(x,y, marker='o')
                self.plot1.set_xlabel(self.x_selected)
                self.plot1.set_ylabel(self.y_selected)
                self.plot1.set_title('A GRAPH OF '+str(self.x_selected).upper() +' AGAINST '+ str(self.y_selected).upper())
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()
            except Exception as e:
                messagebox.showerror('Invalid format provided','Errors from parameters selection'+str(e))
                
                    
    #--------------------------------------stack plot-----------#           
        def stack_plot(self):
            try:
                self.clear_plot()
                self.z_entry_val.config(state='disabled')
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                x=list(x)
                y=list(y)
                y=np.vstack([y,y])
                self.plot1.stackplot(x,y)
                self.plot1.set_xlabel(self.x_selected)
                self.plot1.set_ylabel(self.y_selected)
                self.plot1.set_title('A GRAPH OF '+str(self.x_selected).upper() +' AGAINST '+ str(self.y_selected).upper())
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()
            except Exception as e:
                messagebox.showerror('Invalid format provided','X and Y must be Numbers')
                
    ############ statistical Plots #####           
    #--------------------------------------Bar plot-----------#             
        def point_plot(self):
            try:
                self.clear_plot()
                self.z_entry_val.config(state='normal')
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                if self.z_entry_val.get()=="":
                    sns.pointplot(data=self.df,x=x,y=y,ax=self.plot1)
                else:
                    z=self.df.loc[:,self.z_entry_val.get()]
                    sns.pointplot(data=self.df,x=x,y=y,ax=self.plot1,dodge=True,hue=z)
                self.plot1.set_title('A GRAPH OF '+str(self.x_selected).upper() +' AGAINST '+ str(self.y_selected).upper())
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()
            except Exception as e:
                messagebox.showerror('Invalid format provided','Invalid Columns selected or Missing values from dataset')
                


        def bar_plot(self):
            try:
                self.clear_plot()
                self.z_entry_val.config(state='normal')
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                if self.z_entry_val.get()=='': 
                    sns.barplot(data=self.df,x=x,y=y,ax=self.plot1)
                else:
                    z=self.df.loc[:,self.z_entry_val.get()] 
                    sns.barplot(data=self.df,x=x,y=y,ax=self.plot1,hue=z)
                self.plot1.set_xlabel(self.x_selected)
                self.plot1.set_ylabel(self.y_selected)
                self.plot1.set_title('A GRAPH OF '+str(self.x_selected).upper() +' AGAINST '+ str(self.y_selected).upper())
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()
            except Exception as e:
                messagebox.showerror('Invalid format provided','one of the columns must contain Numbers')
                
        def density_plot(self):
            try:
                self.clear_plot()
                self.z_entry_val.config(state='normal')
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                if self.z_entry_val.get()=='':
                    sns.kdeplot(data=self.df,x=x,y=y,ax=self.plot1,fill=True)
                else:
                    z=self.df.loc[:,self.z_entry_val.get()]
                    sns.kdeplot(data=self.df,x=x,y=y,ax=self.plot1, multiple="stack",fill=True,hue=z)
                self.plot1.set_title('A graph of '+self.x_selected +' against '+ self.y_selected)
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()
                
            except Exception as e:
                messagebox.showerror('Invalid format provided','Choose columns with Numbers for X and Y and Non ambigoius column for Hue!')
                
        def count_plot(self):
            try:
                self.clear_plot()
                self.z_entry_val.config(state='normal')
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                
                if self.z_entry_val.get()=='': 
                    sns.countplot(data=self.df,x=x,ax=self.plot1)
                else:
                    z=self.df.loc[:,self.z_entry_val.get()]
                    sns.countplot(data=self.df,x=x,ax=self.plot1,hue=z)

                self.plot1.set_title('A graph of '+self.x_selected+' showing its count')
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()           
            except Exception as e:
                messagebox.showerror('Invalid format provided','Please recheck selections!(Yis not needed when making selections)')
                
        def dist_plot(self):
            try:
                self.clear_plot()
                self.z_entry_val.config(state='normal')
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                if self.z_entry_val.get()=='': 
                    sns.ecdfplot(data=self.df,x=x,ax=self.plot1)
                else:
                    z=self.df.loc[:,self.z_entry_val.get()]
                    sns.ecdfplot(data=self.df,x=x,ax=self.plot1,hue=z)
                
                self.plot1.set_title('A graph showing distribution of '+self.x_selected )
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()           
            except Exception as e:
                messagebox.showerror('Invalid format provided','please select valid columns')
                
        def hist_plot(self):
            try:
                self.z_entry_val.config(state='normal')
                self.clear_plot()
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                if self.z_entry_val.get()=='':
                    sns.histplot(data=self.df,x=x,ax=self.plot1,kde=True)
                    self.plot1.set_title('Graph showing the distribution of '+self.x_selected)
                    if self.y_entry_val.get()!='' and self.x_entry_val.get()!='':
                        y=self.df.loc[:,self.y_entry_val.get()]
                        sns.histplot(data=self.df,x=x,y=y,ax=self.plot1,kde=True)
                        self.plot1.set_title('Graph showing the distribution of '+self.x_selected+' against '+self.y_selected)

                else:
                    z=self.df.loc[:,self.z_entry_val.get()]
                    sns.histplot(data=self.df,x=x,ax=self.plot1,hue=z)
                    self.plot1.set_title('Graph showing the distribution of '+self.x_selected)
                    if self.y_entry_val.get()!='' and self.x_entry_val.get()!='':
                        y=self.df.loc[:,self.y_entry_val.get()]
                        z=self.df.loc[:,self.z_entry_val.get()]
                        sns.histplot(data=self.df,x=x,y=y,ax=self.plot1,hue=z)
                        self.plot1.set_title('Graph showing the distribution of '+self.x_selected+' against '+self.y_selected)
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()
                           
            except Exception as e:
                messagebox.showerror('Invalid format provided','check selected columns!')
                
        def pie_plot(self):
            try:
                self.clear_plot()
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                vr=0.05
                
                self.plot1.pie(y,labels=x,autopct='%.1f%%',textprops = dict(fontsize=8,color ="black"))
                self.plot1.set_title('A graph of showing the distribution of '+self.y_selected +' in terms of '+ self.x_selected)
                
                
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()           
            except Exception as e:
                messagebox.showerror('Invalid format provided','X must be labels Y must be data')
                
        def box_plot(self):
            try:
                self.clear_plot()
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                self.z_entry_val.config(state='normal')
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                
                if self.z_entry_val.get()=='':
                    sns.boxplot(data=self.df,x=x,y=y,ax=self.plot1)
                else:
                    z=self.df.loc[:,self.z_entry_val.get()]
                    sns.boxplot(data=self.df,x=x,y=y,ax=self.plot1,hue=z)
                self.plot1.set_title('A graph of '+self.x_selected +' against '+ self.y_selected)
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()           
            except Exception as e:
                messagebox.showerror('Invalid format provided','please select x and  y column')
                
        def dou_plot(self):
            try:
                self.clear_plot()
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                self.z_entry_val.config(state='disabled')
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                vr=0.1
                explodes=[vr for i in range(len(x))]
                self.plot1.pie(y,labels=x,autopct='%1.1f%%', pctdistance=0.85,explode=explodes,textprops = dict(fontsize=8,color ="black"))
                circle=matplotlib.patches.Circle((0,0), 0.7, color='white')
                self.plot1.add_artist(circle)
                
                self.plot1.set_title('A graph of '+self.x_selected +' against '+ self.y_selected)
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()           
            except Exception as e:
                messagebox.showerror('Invalid format provided','please select x and  y column')
                
        def bubble_plot(self):
            try:
                self.clear_plot()
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                self.z_entry_val.config(state='normal')
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                vrs=[random.random() for i in range(len(x))]
                if self.z_entry_val.get()=='':
                    sns.scatterplot(data=self.df,x=x,y=y,ax=self.plot1,size=vrs,alpha=0.5, sizes=(20, 800)) 
                else:
                    z=self.df.loc[:,self.z_entry_val.get()]
                    sns.scatterplot(data=self.df,x=x,y=y,ax=self.plot1,size=vrs,alpha=0.5, sizes=(20, 800),hue=z)
                self.plot1.set_title('A graph of '+self.x_selected +' against '+ self.y_selected)
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()         
            except Exception as e:
                messagebox.showerror('Invalid format provided','please select x and  y column')
                
        def strip_plot(self):
            try:
                self.clear_plot()
                self.z_entry_val.config(state='normal')
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                if self.z_entry_val.get()=='':

                    sns.stripplot(data=self.df,x=x,y=y,ax=self.plot1,orient='v')
                else:
                    z=self.df.loc[:,self.z_entry_val.get()]
                    sns.stripplot(data=self.df,x=x,y=y,ax=self.plot1,orient='v',hue=z)
                self.plot1.set_title('A graph of '+self.x_selected +' against '+ self.y_selected)
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()           
            except Exception as e:
                messagebox.showerror('Invalid format provided','please select x and  y column')
                
        def lm_plot(self):
            try:
                self.clear_plot()
                # x=self.x_entry_val.get()
                # y=self.y_entry_val.get()

                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                self.z_entry_val.config(state='disabled')
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                sns.regplot(data=self.df,x=x,y=y,ax=self.plot1)
                self.plot1.set_title('A graph of '+self.x_selected +' against '+ self.y_selected)
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()          
            except Exception as e:
                messagebox.showerror('Invalid format provided','please select x and  y column')
                
        def swarm_plot(self):
            try:
                self.clear_plot()
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                self.z_entry_val.config(state='disabled')
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                vrs=[random.random() for i in range(len(x))]
                sns.swarmplot(data=self.df,x=x,y=y,ax=self.plot1,palette="deep",orient='v')
                self.plot1.set_title('A graph of '+self.x_selected +' against '+ self.y_selected)
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()          
            except Exception as e:
                messagebox.showerror('Invalid format provided','please select x and  y column')
                
        def boxen_plot(self):
            try:
                self.clear_plot()
                
                self.z_entry_val.config(state='normal')
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                if self.z_entry_val.get()=='':
                    sns.boxenplot(data=self.df,x=x,y=y,ax=self.plot1,orient='v',scale='linear')
                else:
                    z=self.df.loc[:,self.z_entry_val.get()]
                    sns.boxenplot(data=self.df,x=x,y=y,ax=self.plot1,orient='v',scale='linear',hue=z)
                self.plot1.set_title('A graph of '+self.x_selected +' against '+ self.y_selected)
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()
                           
            except Exception as e:
                messagebox.showerror('Invalid format provided','please select x and  y column')
                
        def residual_plot(self):
            try:
                self.clear_plot()
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                self.z_entry_val.config(state='disabled')
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                vrs=[random.random() for i in range(len(x))]
                sns.residplot(data=self.df,x=x,y=y,ax=self.plot1)
                self.plot1.set_title('A graph of '+self.x_selected +' against '+ self.y_selected)
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()          
            except Exception as e:
                messagebox.showerror('Invalid format provided','please select x and  y column')
                
        def error_plot(self):
            try:
                self.clear_plot()
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                self.z_entry_val.config(state='disabled')
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                self.plot1.errorbar(x, y, xerr = x.mean(), yerr = y.mean())
                self.plot1.set_title('A graph of '+self.x_selected +' against '+ self.y_selected)
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()
                           
            except Exception as e:
                messagebox.showerror('Invalid format provided','please select x and  y column')
                 
        
        def event_plot(self):
            try:
                self.clear_plot()
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                self.z_entry_val.config(state='disabled')
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                limx=[random.randint(-5,5) for i in range(len(x))]
                limy=[random.randint(1,3) for i in range(len(x))]
                self.plot1.eventplot(x, orientation='vertical')
                self.plot1.set_title('A graph of '+self.x_selected +' against '+ self.y_selected)
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()
                           
            except Exception as e:
                messagebox.showerror('Invalid format provided','please select x and  y column')
                 
        def violin_plot(self):
            try:
                self.clear_plot()
                self.z_entry_val.config(state='normal')
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                vrs=[random.random() for i in range(len(x))]
                if self.z_entry_val.get()=='':
                    sns.violinplot(data=self.df,x=x,y=y,ax=self.plot1)
                else:
                    z=self.df.loc[:,self.z_entry_val.get()]
                    sns.violinplot(data=self.df,x=x,y=y,ax=self.plot1,hue=z)
                self.plot1.set_title('A graph of '+self.x_selected +' against '+ self.y_selected)
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()
                           
            except Exception as e:
                messagebox.showerror('Invalid format provided','please select x and  y column')
                         

        def heatmap_plot(self):
            try:
                self.clear_plot()
                self.clear_plot()
                self.z_entry_val.config(state='disabled')
                self.fig = Figure(figsize=(8.4,4.3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                
                g=sns.heatmap(data=self.df.corr(),annot=True,ax=self.plot1,fmt='.1f',xticklabels='auto',yticklabels='auto')
                g.set_xticklabels(g.get_xticklabels(),rotation=90,fontsize=11)
                g.set_yticklabels(g.get_yticklabels(),rotation=0,fontsize=11)

                self.plot1.set_title('Heatmap for entire Dataset')
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()
                           
            except Exception as e:
                messagebox.showerror('Invalid format provided','Please select valid column or check dataset for error')
                 
        def hexbin_plot(self):
            try:
                self.clear_plot()
                a=self.start_entry.get()
                b=self.end_entry.get()
                self.z_entry_val.config(state='disabled')
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                self.plot1.hexbin(x,y, gridsize = 50, cmap ='BuGn') 
                self.plot1.set_title('A graph of '+self.x_selected +' against '+ self.y_selected)
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()
                           
            except Exception as e:
                messagebox.showerror('Invalid format provided','please select x and  y column')
                
        def contour_plot(self):
            try:
                self.clear_plot()
                self.z_entry_val.config(state='disabled')
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                self.z_entry_val.config(state='disabled')
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                [X, Y] = np.meshgrid(x,y)
                Z = X ** 2 + Y ** 2
                self.plot1.contourf(X,Y,Z) 
                self.plot1.set_title('A graph of '+self.x_selected +' against '+ self.y_selected)
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()
                           
            except Exception as e:
                messagebox.showerror('Invalid format provided','X and Y must be Numbers')
                
        def quiver_plot(self):
            try:
                self.clear_plot()
                a=self.start_entry.get()
                b=self.end_entry.get()
                self.z_entry_val.config(state='disabled')
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                X, Y = np.meshgrid(x, y)
                z = X * np.exp(-X**2-Y**2)
                dx, dy = np.gradient(z)
                self.plot1.quiver(X, Y, dx, dy) 
                self.plot1.set_title('A graph of '+self.x_selected +' against '+ self.y_selected)
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()
                           
            except Exception as e:
                messagebox.showerror('Invalid format provided','X and Y must be Numbers')
                
        def tripcolor_plot(self):
            try:
                self.clear_plot()
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                self.z_entry_val.config(state='disabled')
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                X, Y = np.meshgrid(x, y)
                u = np.ones((10, 10))
                v = np.zeros((10, 10))
                self.plot1.streamplot(X, Y, u, v, density = 0.5) 
                self.plot1.set_title('A graph of '+self.x_selected +' against '+ self.y_selected)
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()
                           
            except Exception as e:
                messagebox.showerror('Invalid format provided','X and Y must be Numbers')
                
        def tri_plot(self):
            try:
                self.clear_plot()
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                self.z_entry_val.config(state='disabled')
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1)
                X, Y = np.meshgrid(x, y)
                u = np.ones((10, 10))
                v = np.zeros((10, 10))
                self.plot1.streamplot(X, Y, u, v, density = 0.5) 
                self.plot1.set_title('A graph of '+self.x_selected +' against '+ self.y_selected)
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()
                           
            except Exception as e:
                messagebox.showerror('Invalid format provided','X and Y must be Numbers')
                
        


    ################ 3 DIMENSIONAL PLOTS######### 
        def bar3d_plot(self):
            try:
                
                self.clear_plot()
                self.z_entry_val.config(state='normal')
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                    z=self.df.loc[:,self.z_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                    z=self.df.loc[:b,self.z_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                    z=self.df.loc[a:,self.z_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                    z=self.df.loc[a:b+1,self.z_entry_val.get()]
                xs=list(x)
                ys=list(y)
                zs=np.zeros(len(xs))
                dx =np.ones(len(xs))
                dy =np.ones(len(xs))
                dz = list(z)

                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1,projection='3d')
                self.plot1.bar3d(xs, ys,zs,dx,dy,dz,color='blue')
                self.plot1.set_title('A graph of '+str(self.x_selected).upper() +' against '+ str(self.y_selected).upper() +' against '+ str(self.z_selected).upper())
                self.plot1.set_xlabel(self.x_selected)
                self.plot1.set_ylabel(self.y_selected)
                self.plot1.set_zlabel(self.z_selected)
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()
                           
            except Exception as e:
                messagebox.showerror('Invalid format provided','All 3 columns must be Numerical....')
                
        def line3d_plot(self):
            try:
                self.z_entry_val.config(state='normal')
                self.clear_plot()
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                    z=self.df.loc[:,self.z_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                    z=self.df.loc[:b,self.z_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                    z=self.df.loc[a:,self.z_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                    z=self.df.loc[a:b+1,self.z_entry_val.get()]
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1,projection='3d')
                self.plot1.plot(x,y,z,color='orange',marker='o')
                self.plot1.set_title('A graph of '+str(self.x_selected).upper() +' against '+ str(self.y_selected).upper()+' against '+ str(self.z_selected).upper())
                self.plot1.set_xlabel(self.x_selected)
                self.plot1.set_ylabel(self.y_selected)
                self.plot1.set_zlabel(self.z_selected)
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()               
            except Exception as e:
                messagebox.showerror('Invalid format provided','please select all three perameters(x,y and hue and all must be numerical...)')
                
        def scatter3d_plot(self):
            try:
                self.z_entry_val.config(state='normal')
                self.clear_plot()
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                    z=self.df.loc[:,self.z_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                    z=self.df.loc[:b,self.z_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                    z=self.df.loc[a:,self.z_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                    z=self.df.loc[a:b+1,self.z_entry_val.get()]
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1,projection='3d')
                self.plot1.scatter(x,y,z)
                self.plot1.set_title('A graph of '+str(self.x_selected).upper() +' against '+ str(self.y_selected).upper()+' against '+ str(self.z_selected).upper())
                self.plot1.set_xlabel(self.x_selected)
                self.plot1.set_ylabel(self.y_selected)
                self.plot1.set_zlabel(self.z_selected)
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()
                           
            except Exception as e:
                messagebox.showerror('Invalid format provided','please select all three perameters(x,y and hue and all must be numerical...)')
                
        def surface3d_plot(self):
            try:
                self.z_entry_val.config(state='normal')
                self.clear_plot()
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]

                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]   
                X,Y = np.meshgrid(x,y)
                Z = (Y*X)*np.exp(-X**2 - Y**2)
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1,projection='3d')
                mycmap = plt.get_cmap('gist_earth')
                surf1 = self.plot1.plot_surface(X, Y,Z, cmap=mycmap,linewidth=0, antialiased=False)
                self.plot1.set_title('A graph of '+str(self.x_selected).upper() +' against '+ str(self.y_selected).upper())
                self.plot1.set_xlabel(self.x_selected)
                self.plot1.set_ylabel(self.y_selected)
                self.plot1.set_zlabel('Function of '+str(self.x_selected)+' and '+str(self.y_selected))
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()
                           
            except Exception as e:
                messagebox.showerror('Invalid format provided','x and y must be numerical...')
                
        def contour3d_plot(self):
            try:
                self.z_entry_val.config(state='normal')
                self.clear_plot()
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                X,Y = np.meshgrid(x,y)
                def f(x, y):
                    return x*np.sqrt(x**2 + y**2)   
                zs=f(X,Y)
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1,projection='3d')
                surf = self.plot1.contour3D(X,Y,zs, cmap='coolwarm')
                self.plot1.set_title('A graph of '+str(self.x_selected).upper() +' against '+ str(self.y_selected).upper())
                self.plot1.set_xlabel(self.x_selected)
                self.plot1.set_ylabel(self.y_selected)
                self.plot1.set_zlabel('Function of '+str(self.x_selected)+' and '+str(self.y_selected))
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()
                           
            except Exception as e:
                messagebox.showerror('Invalid format provided','please x and y must be Numerical (Numbers)')
                
        
                
        def stem3d_plot(self):
            try:
                self.z_entry_val.config(state='normal')
                self.clear_plot()
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                X=np.array(list(x))
                Y=np.array(list(y))
                Z=list((2*X))
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1,projection='3d')
                self.plot1.stem(X,Y,Z)
                self.plot1.set_title('A graph of '+str(self.x_selected).upper() +' against '+ str(self.y_selected).upper())
                self.plot1.set_xlabel(self.x_selected)
                self.plot1.set_ylabel(self.y_selected)
                self.plot1.set_zlabel('Function of '+str(self.x_selected)+' and '+str(self.y_selected))
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()               
            except Exception as e:
                messagebox.showerror('Invalid format provided','x and y must be numerical...')
                
                
        def quiver3d_plot(self):
            try:
                self.z_entry_val.config(state='normal')
                self.clear_plot()
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1,projection='3d')
                x=list(x);y=list(y);
                x=np.array(x).flatten()
                y=np.array(y).flatten()
                z=x*y
                x, y, z = np.meshgrid(x,y,z)
                u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
                v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
                w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) * np.sin(np.pi * z))
                self.plot1.quiver(x, y, z,u,v,w, length=0.1, normalize=True)
                self.plot1.set_title('A graph of '+str(self.x_selected).upper() +' against '+ str(self.y_selected).upper())
                self.plot1.set_xlabel(self.x_selected)
                self.plot1.set_ylabel(self.y_selected)
                self.plot1.set_zlabel('Function of '+str(self.x_selected)+' and '+str(self.y_selected))
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()               
            except Exception as e:
                messagebox.showerror('Invalid format provided','x and y must be numerical...')
                
                
        def tri3d_plot(self):
            try:
                self.z_entry_val.config(state='normal')
                self.clear_plot()
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1,projection='3d')
                x=list(x);y=list(y)
                x=np.array(x);y=np.array(y)
                z = np.sin(-x*y)
                self.plot1.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)
                self.plot1.set_title('A graph of '+str(self.x_selected).upper() +' against '+ str(self.y_selected).upper())
                self.plot1.set_xlabel(self.x_selected)
                self.plot1.set_ylabel(self.y_selected)
                self.plot1.set_zlabel('Function of '+str(self.x_selected)+' and '+str(self.y_selected))
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()               
            except Exception as e:
                messagebox.showerror('Invalid format provided','please x and y must be Numerical (Numbers)')
                
                
        def tric3d_plot(self):
            try:
                self.z_entry_val.config(state='normal')
                self.clear_plot()
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                x=list(x);y=list(y)
                x=np.array(x);y=np.array(y)
                z = np.cos(-x*y)+np.sin(-x*y)
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1,projection='3d')
                self.plot1.tricontour(x,y, z, cmap=plt.cm.CMRmap)
                self.plot1.set_title('A graph of '+str(self.x_selected).upper() +' against '+ str(self.y_selected).upper())
                self.plot1.set_xlabel(self.x_selected)
                self.plot1.set_ylabel(self.y_selected)
                self.plot1.set_zlabel('Function of '+str(self.x_selected)+' and '+str(self.y_selected))
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()               
            except Exception as e:
                messagebox.showerror('Invalid format provided','x and y must be numerical...')
                
                
        def wire3d_plot(self):
            try:
                self.z_entry_val.config(state='normal')
                self.clear_plot()
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                x=list(x);y=list(y)
                x=np.array(x);y=np.array(y)
                def f(a,b):
                    return np.sin(np.sqrt(a ** 2 + b ** 2))
                X, Y = np.meshgrid(x, y)
                Z = f(X, Y)
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1,projection='3d')
                self.plot1.plot_wireframe(X, Y, Z)
                self.plot1.set_title('A graph of '+str(self.x_selected).upper() +' against '+ str(self.y_selected).upper())
                self.plot1.set_xlabel(self.x_selected)
                self.plot1.set_ylabel(self.y_selected)
                self.plot1.set_zlabel('Function of '+str(self.x_selected)+' and '+str(self.y_selected))
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()               
            except Exception as e:
                messagebox.showerror('Invalid format provided','x and y must be numerical...')
                
        
                
        def pc3d_plot(self):
            try:
                self.z_entry_val.config(state='normal')
                self.clear_plot()
                a=self.start_entry.get()
                b=self.end_entry.get()
                if self.start_entry.get()=='' and self.end_entry.get()=='':
                    x=self.df.loc[:,self.x_entry_val.get()]
                    y=self.df.loc[:,self.y_entry_val.get()]
                elif self.start_entry.get()=='' and self.end_entry.get()!='':
                    b=int(b)
                    x=self.df.loc[:b,self.x_entry_val.get()]
                    y=self.df.loc[:b,self.y_entry_val.get()]
                elif self.end_entry.get()=='' and self.start_entry.get()!='':
                    a=int(a)
                    x=self.df.loc[a:,self.x_entry_val.get()]
                    y=self.df.loc[a:,self.y_entry_val.get()]
                else:
                    a=int(a)
                    b=int(b)
                    x=self.df.loc[a:b+1,self.x_entry_val.get()]
                    y=self.df.loc[a:b+1,self.y_entry_val.get()]
                self.fig = Figure(figsize=(7.3,3), dpi=105,layout='tight')
                self.plot1 = self.fig.add_subplot(1,1,1,projection='3d')
                theta =x
                z = y
                r = z**2 + 1
                x = r * np.sin(theta)
                y = r * np.cos(theta)

                self.plot1.plot(x, y, z, label='parametric curve')
                self.plot1.set_title('A graph of '+str(self.x_selected).upper() +' against '+ str(self.y_selected).upper())
                self.plot1.set_xlabel(self.x_selected)
                self.plot1.set_ylabel(self.y_selected)
                self.plot1.set_zlabel('Function of '+str(self.x_selected)+' and '+str(self.y_selected))
                self.output = FigureCanvasTkAgg(self.fig,master = self.mapp)
                self.output.draw()
                self.output.get_tk_widget().pack()
                toolbar = NavigationToolbar2Tk(self.output,self.mapp)
                toolbar.update()
                self.output.get_tk_widget().pack()               
            except Exception as e:
                messagebox.showerror('Invalid format provided','x and y must be numerical...')
                 
                
        
             
     
     
            
            
    ############----------------Clearing Functions-------------###########
        def clear_title(self):
            self.data_name.config(text='')

        def clear_data(self):
            if self.filename=='':
                pass
            else:
                self.x_entry_val.delete('0', 'end') 
                self.online_entry.delete('0','end')
                self.y_entry_val.delete('0', 'end')
                 
                self.z_entry_val.delete('0', 'end')
                self.start_entry.delete('0','end')
                self.end_entry.delete('0','end')
                self.clear_stat_info()
                self.ls.delete(0,END) 
                self.data_items.delete(*self.data_items.get_children())
        def clearonline_data(self):
            self.online_url=self.online_entry.get()
            if self.online_url=='':
                pass
            else:
                self.x_entry_val.delete('0', 'end') 
                self.y_entry_val.delete('0', 'end')
                self.data_name.config(text='') 
                self.z_entry_val.delete('0', 'end')
                self.start_entry.delete('0','end')
                self.end_entry.delete('0','end')
                self.clear_stat_info()
                self.ls.delete(0,END) 
                self.data_items.delete(*self.data_items.get_children())

        def close_app(self):
            rsp=messagebox.askyesno('CLOSE APPLICATION','Do you want to exit App?')
            if rsp>0:
                self.destroy()
                self.conn.close()
            else:
                pass
        def new_pro(self):
            try:
                if self.filename!='' or self.online_url!='':
                    self.clear_data()
                    self.clear_title()
                    self.clear_plot()
                    self.clearonline_data()
                    self.clear_stat_info()
                    self.data_name.config(text='')
                    
                    self.data_items['columns']=''
                    self.x_chooser['values']=(['Choose x column'])
                    self.x_chooser.current(0)
                    self.y_chooser['values']=(['Choose y column'])
                    self.y_chooser.current(0)
                    self.hue['values']=(['Choose hue column'])
                    self.hue.current(0)
                    self.df=''
                    self.graph_type.config(text='selected graph')
                else:
                    pass
            except Exception as e:
                
                messagebox.showerror('Error','No work on going as no dataset was found')
        
        def toggle_destroy(self):
          self.toggle_menu.destroy()
        def clear_plot(self):
            if self.output:
                for child in self.mapp.winfo_children():
                    child.destroy()
            self.output = None 
        def recent_window(self):
            self.toggle_menu=Frame(self,bg='#d3d2d1')
            self.toggle_menu.place(x=60,y=57,height=self.height,width=400)
            self.des_btn=CTkButton(self.toggle_menu,text=' X ',text_font='cambria 10 bold',width=5,corner_radius=0,fg_color='white',text_color='red',command=self.toggle_destroy)
            self.des_btn.place(x=10,y=2)
            self.recent_label=Label(self.toggle_menu,text='RECENT FILES OPENED BY TIME',fg='black',font='cambria 10 bold',bg='#d3d2d1')
            self.recent_label.pack(padx=3,pady=10)
            self.recent_files_holder=Frame(self.toggle_menu,bg='white')
            self.recent_files_holder.place(relx=.0,rely=.05,width=400,height=500)
            self.cv=Canvas(self.recent_files_holder,bg='white',width=380)
            self.cv.pack(fill=BOTH,side=LEFT)
            self.scroll_it_y=ttk.Scrollbar(self.recent_files_holder,orient=VERTICAL,command=self.cv.yview)
            self.scroll_it_y.pack(fill=Y,side=RIGHT)
            self.hdr=Frame(self.cv,bg='white',width=380)
            self.cv.create_window((0,0),window=self.hdr,anchor=CENTER)
            self.cv.configure(yscrollcommand= self.scroll_it_y.set)
            self.cv.bind('<Configure>',lambda e: self.cv.configure(scrollregion=self.cv.bbox('all')))
            self.fetch_data()



        def drop_empty(self):
          self.df=self.df.dropna(axis=1)
          self.clear_data()
          head=list(self.df.columns)          
          if head[0]=='Unnamed: 0':
              head=head[1:]
              self.x_chooser['values']=(head)
              self.y_chooser['values']=(head)
              self.hue['values']=(head)
              self.data_items['columns']=head
              self.data_items['show']='headings'
              for column in self.data_items['columns']:
                  self.data_items.heading(column,text=column)
                  self.ls.insert(END,column)
                  
              self.df_rows=self.df.to_numpy().tolist()
              for row in self.df_rows:
                  self.data_items.insert('','end',values=row[1:])
          else:
            head=head[:]
            self.x_chooser['values']=(head)
            self.y_chooser['values']=(head)
            self.hue['values']=(head)
            self.data_items['columns']=head
            self.data_items['show']='headings'
            for column in self.data_items['columns']:
                self.data_items.heading(column,text=column)
                self.ls.insert(END,column)
                
            self.df_rows=self.df.to_numpy().tolist()
            for row in self.df_rows:
                self.data_items.insert('','end',values=row[:])
          
        def drop_empty_row(self):
          self.df=self.df.dropna(axis=0)
          self.clear_data()
          head=list(self.df.columns)          
          if head[0]=='Unnamed: 0':
              head=head[1:]
              self.x_chooser['values']=(head)
              self.y_chooser['values']=(head)
              self.hue['values']=(head)
              self.data_items['columns']=head
              self.data_items['show']='headings'
              for column in self.data_items['columns']:
                  self.data_items.heading(column,text=column)
                  self.ls.insert(END,column)
                  
              self.df_rows=self.df.to_numpy().tolist()
              for row in self.df_rows:
                  self.data_items.insert('','end',values=row[1:])
          else:
            head=head[:]
            self.x_chooser['values']=(head)
            self.y_chooser['values']=(head)
            self.hue['values']=(head)
            self.data_items['columns']=head
            self.data_items['show']='headings'
            for column in self.data_items['columns']:
                self.data_items.heading(column,text=column)
                self.ls.insert(END,column)
                
            self.df_rows=self.df.to_numpy().tolist()
            for row in self.df_rows:
                self.data_items.insert('','end',values=row[:])

        def fill_na(self):
          self.df=self.df.fillna(self.df.mean())
          self.clear_data()
          head=list(self.df.columns)          
          if head[0]=='Unnamed: 0':
              head=head[1:]
              self.x_chooser['values']=(head)
              self.y_chooser['values']=(head)
              self.hue['values']=(head)
              self.data_items['columns']=head
              self.data_items['show']='headings'
              for column in self.data_items['columns']:
                  self.data_items.heading(column,text=column)
                  self.ls.insert(END,column)
                  
              self.df_rows=self.df.to_numpy().tolist()
              for row in self.df_rows:
                  self.data_items.insert('','end',values=row[1:])
          else:
            head=head[:]
            self.x_chooser['values']=(head)
            self.y_chooser['values']=(head)
            self.hue['values']=(head)
            self.data_items['columns']=head
            self.data_items['show']='headings'
            for column in self.data_items['columns']:
                self.data_items.heading(column,text=column)
                self.ls.insert(END,column)
                
            self.df_rows=self.df.to_numpy().tolist()
            for row in self.df_rows:
                self.data_items.insert('','end',values=row[:])

        def fill_na_1(self):
          self.fill_na_val()

        def fill_na_2(self):
          self.fill_x_val=self.fill_entry.get()
          self.fill_hd.destroy()
          self.df=self.df.fillna(self.fill_x_val)
          self.clear_data()
          head=list(self.df.columns)          
          if head[0]=='Unnamed: 0':
              head=head[1:]
              self.x_chooser['values']=(head)
              self.y_chooser['values']=(head)
              self.hue['values']=(head)
              self.data_items['columns']=head
              self.data_items['show']='headings'
              for column in self.data_items['columns']:
                  self.data_items.heading(column,text=column)
                  self.ls.insert(END,column)
                  
              self.df_rows=self.df.to_numpy().tolist()
              for row in self.df_rows:
                  self.data_items.insert('','end',values=row[1:])
          else:
            head=head[:]
            self.x_chooser['values']=(head)
            self.y_chooser['values']=(head)
            self.hue['values']=(head)
            self.data_items['columns']=head
            self.data_items['show']='headings'
            for column in self.data_items['columns']:
                self.data_items.heading(column,text=column)
                self.ls.insert(END,column)
                
            self.df_rows=self.df.to_numpy().tolist()
            for row in self.df_rows:
                self.data_items.insert('','end',values=row[:])
          
        def drop_empty_row(self):
          self.df=self.df.dropna(axis=0)
          self.clear_data()
          head=list(self.df.columns)          
          if head[0]=='Unnamed: 0':
              head=head[1:]
              self.x_chooser['values']=(head)
              self.y_chooser['values']=(head)
              self.hue['values']=(head)
              self.data_items['columns']=head
              self.data_items['show']='headings'
              for column in self.data_items['columns']:
                  self.data_items.heading(column,text=column)
                  self.ls.insert(END,column)
                  
              self.df_rows=self.df.to_numpy().tolist()
              for row in self.df_rows:
                  self.data_items.insert('','end',values=row[1:])
          else:
            head=head[:]
            self.x_chooser['values']=(head)
            self.y_chooser['values']=(head)
            self.hue['values']=(head)
            self.data_items['columns']=head
            self.data_items['show']='headings'
            for column in self.data_items['columns']:
                self.data_items.heading(column,text=column)
                self.ls.insert(END,column)
                
            self.df_rows=self.df.to_numpy().tolist()
            for row in self.df_rows:
                self.data_items.insert('','end',values=row[:])

        def fill_na(self):
          try:
              self.df=self.df.fillna(self.df.mean())
              self.clear_data()
              head=list(self.df.columns)          
              if head[0]=='Unnamed: 0':
                  head=head[1:]
                  self.x_chooser['values']=(head)
                  self.y_chooser['values']=(head)
                  self.hue['values']=(head)
                  self.data_items['columns']=head
                  self.data_items['show']='headings'
                  for column in self.data_items['columns']:
                      self.data_items.heading(column,text=column)
                      self.ls.insert(END,column)
                      
                  self.df_rows=self.df.to_numpy().tolist()
                  for row in self.df_rows:
                      self.data_items.insert('','end',values=row[1:])
              else:
                head=head[:]
                self.x_chooser['values']=(head)
                self.y_chooser['values']=(head)
                self.hue['values']=(head)
                self.data_items['columns']=head
                self.data_items['show']='headings'
                for column in self.data_items['columns']:
                    self.data_items.heading(column,text=column)
                    self.ls.insert(END,column)
                    
                self.df_rows=self.df.to_numpy().tolist()
                for row in self.df_rows:
                    self.data_items.insert('','end',values=row[:])
          except Exception:
            messagebox.showerror('Error','check dataset for error')

        

        

        def fill_na_val(self):
            try:
                self.fill_hd=Toplevel(app)
                self.fill_hd.resizable(False,False)
                self.fill_hd.geometry('200x100+300+200')
                self.fill_hd.config(background='white')
                self.fill_hd.title('FILL EMPTY VALUE')
                self.photo=PhotoImage(file='images/data.png')
                self.fill_hd.iconphoto(False,self.photo)
                Label(self.fill_hd,text='Enter value to fill all empty',font='cambria 11 bold',bg='white').pack(pady=2)
                self.fill_entry=CTkEntry(self.fill_hd,corner_radius=5)
                self.fill_entry.pack()
                self.fill_ac=CTkButton(self.fill_hd,text='OK',command=self.fill_na_2,corner_radius=0)
                self.fill_ac.pack(pady=3)
            except Exception as e:
            
                messagebox.showerror('Error','invalid selection')
        def drop_column(self):
          try:  
            self.column_to_drop()
          except Exception:
            pass

        def drop_cols(self):
          try:
            s=str(self.col_t.get())
            s=s.split(',')
            s=s[:-1]
            self.df=self.df.drop(s,axis=1)

            self.clear_data()
            self.drop_c.destroy()
            head=list(self.df.columns)          
            if head[0]=='Unnamed: 0':
                head=head[1:]
                self.x_chooser['values']=(head)
                self.y_chooser['values']=(head)
                self.hue['values']=(head)
                self.data_items['columns']=head
                self.data_items['show']='headings'
                for column in self.data_items['columns']:
                    self.data_items.heading(column,text=column)
                    self.ls.insert(END,column)
                    
                self.df_rows=self.df.to_numpy().tolist()
                for row in self.df_rows:
                    self.data_items.insert('','end',values=row[1:])
            else:
              head=head[:]
              self.x_chooser['values']=(head)
              self.y_chooser['values']=(head)
              self.hue['values']=(head)
              self.data_items['columns']=head
              self.data_items['show']='headings'
              for column in self.data_items['columns']:
                  self.data_items.heading(column,text=column)
                  self.ls.insert(END,column)
                  
              self.df_rows=self.df.to_numpy().tolist()
              for row in self.df_rows:
                  self.data_items.insert('','end',values=row[:])
          except Exception as e:
            messagebox.showerror('An error has occured','check dataset for error')

        def col_drop(self,event):
            try:
              self.col_droped=self.s_cols.get()
              if self.col_droped=='Choose x column':
                  pass
              else:
                  #self.column_entry.delete('0', 'end') 
                  self.col_t.insert('end',self.col_droped+',')
            except Exception:
              pass
        def column_to_drop(self):
            try:
                self.drop_c=Toplevel(app)
                self.drop_c.resizable(False,False)
                self.drop_c.geometry('390x170+300+200')
                self.drop_c.config(background='white')
                self.drop_c.title('CHOOSE COLUMN TO DROP')
                self.photo=PhotoImage(file='images/data.png')
                self.drop_c.iconphoto(False,self.photo)
                Label(self.drop_c,text='Select columns to drop',font='cambria 11 bold',bg='white').pack(pady=2)
               
                self.col_t=CTkEntry(self.drop_c,corner_radius=0,fg_color='white',width=150)
                self.col_t.pack()
                self.col_n=StringVar()
                head=list(self.df.columns)
                self.s_cols=ttk.Combobox(self.drop_c,state='readonly',width=15,font='arial 10 bold',textvariable=self.col_n)
                self.s_cols['values']=(head)
                self.s_cols.current(0)
                self.s_cols.bind('<<ComboboxSelected>>', self.col_drop)
                self.s_cols.pack(pady=3)
                self.close_sec=CTkButton(self.drop_c,text='OK',command=self.drop_cols,corner_radius=0)
                self.close_sec.pack(pady=3)
            except Exception as e:
            
                messagebox.showerror('Error','invalid selection')



        def drop_row(self):
          try:  
            self.row_to_drop()
          except Exception:
            pass

        def drop_rows(self):
          s=str(self.row_t.get())
          if ',' in s:
            s=s.split(',')
            s=s[:]
            s=[int(x) for x in s]
          else:
            s=int(s)
          self.df=self.df.drop(s)
          self.drop_r.destroy()
          self.clear_data()
          head=list(self.df.columns)          
          if head[0]=='Unnamed: 0':
              head=head[1:]
              self.x_chooser['values']=(head)
              self.y_chooser['values']=(head)
              self.hue['values']=(head)
              self.data_items['columns']=head
              self.data_items['show']='headings'
              for column in self.data_items['columns']:
                  self.data_items.heading(column,text=column)
                  self.ls.insert(END,column)
                  
              self.df_rows=self.df.to_numpy().tolist()
              for row in self.df_rows:
                  self.data_items.insert('','end',values=row[1:])
          else:
            head=head[:]
            self.x_chooser['values']=(head)
            self.y_chooser['values']=(head)
            self.hue['values']=(head)
            self.data_items['columns']=head
            self.data_items['show']='headings'
            for column in self.data_items['columns']:
                self.data_items.heading(column,text=column)
                self.ls.insert(END,column)
                
            self.df_rows=self.df.to_numpy().tolist()
            for row in self.df_rows:
                self.data_items.insert('','end',values=row[:])
        def row_to_drop(self):
            try:
                self.drop_r=Toplevel(app)
                self.drop_r.resizable(False,False)
                self.drop_r.geometry('390x170+300+200')
                self.drop_r.config(background='white')
                self.drop_r.title('ENTER ROWS TO DROP')
                self.photo=PhotoImage(file='images/data.png')
                self.drop_r.iconphoto(False,self.photo)
                Label(self.drop_r,text='ENTER ROWS TO DROP',font='cambria 11 bold',bg='white').pack(pady=2)
                Label(self.drop_r,text='Separate rows with ,',font='cambria 11 bold',bg='white').pack(pady=2)
               
                self.row_t=CTkEntry(self.drop_r,corner_radius=0,fg_color='white',width=150)
                self.row_t.pack()
                self.row_n=StringVar()
                head=list(self.df.columns)
                self.s_rows=ttk.Combobox(self.drop_r,state='readonly',width=15,font='arial 10 bold',textvariable=self.row_n)
                self.close_sec=CTkButton(self.drop_r,text='OK',command=self.drop_rows,corner_radius=0)
                self.close_sec.pack(pady=3)
            except Exception as e:
            
                messagebox.showerror('Error','invalid selection')
        

        def drop_row_index(self):
            try:  
              self.row_index_to_drop()
            except Exception:
              pass

        def drop_row_indexs(self):
          a=self.row_index_s.get()
          b=self.row_index_e.get()
          self.drop_r_i.destroy()
          if a=='' and b=='':
              pass
          elif a=='' and b!='':
              b=int(b)
              self.df=self.df.iloc[:b+1]
          elif b=='' and a!='':
              a=int(a)
              self.df=self.df.iloc[a:]
          else:
              a=int(a)
              b=int(b)
              self.df=self.df.iloc[a:b+1]
          self.clear_data()
          head=list(self.df.columns)          
          if head[0]=='Unnamed: 0':
              head=head[1:]
              self.x_chooser['values']=(head)
              self.y_chooser['values']=(head)
              self.hue['values']=(head)
              self.data_items['columns']=head
              self.data_items['show']='headings'
              for column in self.data_items['columns']:
                  self.data_items.heading(column,text=column)
                  self.ls.insert(END,column)
                  
              self.df_rows=self.df.to_numpy().tolist()
              for row in self.df_rows:
                  self.data_items.insert('','end',values=row[1:])
          else:
            head=head[:]
            self.x_chooser['values']=(head)
            self.y_chooser['values']=(head)
            self.hue['values']=(head)
            self.data_items['columns']=head
            self.data_items['show']='headings'
            for column in self.data_items['columns']:
                self.data_items.heading(column,text=column)
                self.ls.insert(END,column)
                
            self.df_rows=self.df.to_numpy().tolist()
            for row in self.df_rows:
                self.data_items.insert('','end',values=row[:])
        def row_index_to_drop(self):
            try:
                self.drop_r_i=Toplevel(app)
                self.drop_r_i.resizable(False,False)
                self.drop_r_i.geometry('390x170+300+200')
                self.drop_r_i.config(background='white')
                self.drop_r_i.title('ENTER ROWS TO DROP')
                self.photo=PhotoImage(file='images/data.png')
                self.drop_r_i.iconphoto(False,self.photo)
                Label(self.drop_r_i,text='ENTER ROW RANGE',font='cambria 11 bold',bg='white').grid(row=0,column=1)
                
                Label(self.drop_r_i,text='ROW START:',font='cambria 11 bold',bg='white').grid(row=1,column=0,padx=2,pady=3)
                self.row_index_s=CTkEntry(self.drop_r_i,corner_radius=0,fg_color='white',width=70)
                self.row_index_s.grid(row=1,column=1,padx=4,pady=3)

                Label(self.drop_r_i,text='ROW END:',font='cambria 11 bold',bg='white').grid(row=2,column=0,padx=2,pady=3)
                self.row_index_e=CTkEntry(self.drop_r_i,corner_radius=0,fg_color='white',width=70)
                self.row_index_e.grid(row=2,column=1,padx=4,pady=3)
                self.close_sec=CTkButton(self.drop_r_i,text='OK',command=self.drop_row_indexs,corner_radius=0)
                self.close_sec.grid(row=3,column=1,columnspan=2,pady=5)
            except Exception as e:
            
                messagebox.showerror('Error','invalid selection')
        

        def open_reupload(self):

            self.cur.execute('SELECT * FROM file_holder ORDER BY uploadtime DESC')
            rows=self.cur.fetchall()
            w=dict()
            r=self.data_name.cget('text')
            print(w)
            print(r)
            for y in rows:
              w[y[0]]=y[1]
            
            self.filename=w[r] 
            try:
                self.clear_data()
                self.clear_plot()
                self.data_items['columns']=''
                self.x_chooser['values']=(['Choose x column'])
                self.x_chooser.current(0)
                self.y_chooser['values']=(['Choose y column'])
                self.y_chooser.current(0)
                self.hue['values']=(['Choose hue column'])
                self.hue.current(0)
                self.graph_type.config(text='selected graph')
                self.df=''
                s=str(self.filename)
                s=s.split('/')
                s=s[-1]
               
                self.data_name.config(text=s)
                name=str(s)
                
                 
                if name.endswith('.arff'):
                    self.df=pd.loadarff(self.filename)
                    self.df=pd.DataFrame(self.df[0])
                    head=list(self.df.columns)
                    
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    
                        
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])

                if name.endswith('.csv'):
                    self.df=pd.read_csv(self.filename)
                    head=list(self.df.columns)
                    
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    
                        
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])

                if name.endswith('.arff'):
                    self.df=pd.loadarff(self.filename)
                    self.df=pd.DataFrame(self.df[0])
                    head=list(self.df.columns)
                    
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    
                        
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])

                            

                if name.endswith('.data') or name.endswith('.dat'):
                    self.df=pd.read_csv(self.filename,names=['col1','col2'])
                    head=list(self.df.columns)
                    
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    
                        
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])
                            
                if name.endswith('.html'):
                    self.df=pd.read_csv(self.filename)
                    self.df=self.df[0]
                    head=list(self.df.columns)
                    
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    
                        
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])
                                       
        ########Opening different file formats###########
                if name.endswith('.txt'):
                    self.df=pd.read_fwf(self.filename)
                    head=list(self.df.columns)
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])
                              
                if name.endswith('.json'):
                    self.df=pd.read_json(self.filename, orient=None, typ='frame',convert_axes=None, convert_dates=True)
                    
                    head=list(self.df.columns)
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])
                             
                if name.endswith('.xlsx'):
                    self.df=pd.read_excel(self.filename)
                    head=list(self.df.columns)
                    if head[0]=='Unnamed: 0':
                        head=head[1:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[1:])
                    else:
                        head=head[:]
                        self.x_chooser['values']=(head)
                        self.y_chooser['values']=(head)
                        self.hue['values']=(head)
                        self.data_items['columns']=head
                        self.data_items['show']='headings'
                        for column in self.data_items['columns']:
                            self.data_items.heading(column,text=column)
                            self.ls.insert(END,column)
                            
                        self.df_rows=self.df.to_numpy().tolist()
                        for row in self.df_rows:
                            self.data_items.insert('','end',values=row[:])
                     
                     
                    return None
                  
            except FileNotFoundError:
                messagebox.showerror('Invalid','File Cannnot be loaded due to error')
            except ValueError:
                messagebox.showerror('Invalid Dataset','Invalid file format')

    ####################==============All graphs  Visualizations==================######################### 
        def main_plot(self):
            x=self.graph_type
            if x.text=='line plot':
                self.line_plot()
            elif x.text=='Bar chart':
                self.bar_plot()
            elif x.text=='pie plot':
                self.pie_plot()
            elif x.text=='Scatter plot':
                self.scatter_plot()
            elif x.text=='Stem plot':
                self.stem_plot()
            elif x.text=='Step plot':
                self.step_plot()
            elif x.text=='Stack plot':
                self.stack_plot()
            elif x.text=='point plot':
                self.point_plot()
            elif x.text=='Density plot':
                self.density_plot()
            elif x.text=='Count plot':
                self.count_plot()
            elif x.text=='Histogram':
                self.hist_plot()
            elif x.text=='EC Distribution plot':
                self.dist_plot()
            elif x.text=='Heatmap':
                self.heatmap_plot()
            elif x.text=='Hexbin plot':
                self.hexbin_plot()
            elif x.text=='Contour plot':
                self.contour_plot()
            elif x.text=='Box plot':
                self.box_plot()
            elif x.text=='Doughnut plot':
                self.dou_plot()
            elif x.text=='Bubble chart':
                self.bubble_plot()  
            elif x.text=='Error plot':
                self.error_plot()  
            elif x.text=='Event plot':
                self.event_plot()
            elif x.text=='Violin plot':
                self.violin_plot() 
            elif x.text=='Strip plot':
                self.strip_plot()
            elif x.text=='Linear model plot':
                self.lm_plot()  
            elif x.text=='Swarm plot':
                self.swarm_plot()  
            elif x.text=='Boxen plot':
                self.boxen_plot()
            elif x.text=='Residual plot':
                self.residual_plot() 
            elif x.text=='Quiver plot':
                self.quiver_plot()
            
            ##################3d plots #############
            elif x.text=='3D Bar chart':
                self.bar3d_plot()
            elif x.text=='3D Scatter plot':
                self.scatter3d_plot()
            elif x.text=='3D Line plot':
                self.line3d_plot()
            elif x.text=='3D Surface plot':
                self.surface3d_plot()
            elif x.text=='3D contour plot':
                self.contour3d_plot()
            elif x.text=='3D stem plot':
                self.stem3d_plot()
            elif x.text=='3D Quiver plot':
                self.quiver3d_plot()
            elif x.text=='Triangular Contour 3D plot':
                self.tric3d_plot()
            elif x.text=='3D Wireframe plot':
                self.wire3d_plot()
            elif x.text=='Triangular 3D plot':
                self.tri3d_plot()
            elif x.text=='Parametric curve':
                self.pc3d_plot()

        def read_me(self):
            os.startfile('readme.txt')


                    
if __name__=="__main__":  
    app = App()
    app.mainloop()









