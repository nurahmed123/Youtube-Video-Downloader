from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

root = Tk()
root.geometry("520x500+350+100")
root.configure(bg = "gray3")
root.title("BongVideo-PLR")
root.resizable(0,0)
root.wm_iconbitmap("u_donload.ico")

direct = ""
def set_path():
    global direct
    # download_out.config(root , text = "Wait If System Show No Responding During Download" , bg = "gray3" , fg = "dark orange" , font = ("lucida 13"))
    download_name.config(text = "")
    download_size.config(text = "")
    download_loc.config(text = "")
    direct = filedialog.askdirectory()
    path_holder.config(text = direct)

def start_download():
    global direct
    url = link_entry.get()
    selected = types.get()
    print(f"url is : {url} and selected item is : {selected} and dir is : {direct}")
    if len(url)<1:
        link_error.config(text = "Please insert URL")
    if len(direct) <1:
        path_error.config(text = "Please insert path")
    else:
        link_error.config(text = "")
        path_error.config(text = "")
        yt = YouTube(url)
        print(yt)
        try:
            try:
                if selected == options[0]:
                    typ = yt.streams.get_highest_resolution()
                    print("lol1")
                elif selected == options[1]:
                    print("lol2")
                    typ = yt.streams.filter(progressive=True , file_extension="MP4").first()
                elif selected ==options[2]:
                    print("lol3")
                    typ = yt.streams.filter(only_audio=True).first()
                try:
                    print("lol dir is  : ",direct)
                    typ.download(direct)
                    link_entry.delete(0,"end")
                    path_holder.config(text = "Download" , font = (12))
                    # download_out.config(text = "Downloaded" , font = (12))

                    name = typ.title
                    size = typ.filesize/1024000
                    size = round(size,1)
                    download_name.config(text = "Name : "+name)
                    download_size.config(text = "Size : "+str(size)+"MB")
                    download_loc.config(text = "Path : "+direct)
                except:
                    download_out(text = "Download Faild" , font =(12))
            except:
                download_out(text="Having Error", font=(12))
        except:
            path_error.config(text = "Please insert valid path")



#TODO : HEADING OF APPLICATION
heading = Label(root,text = "Youtube Video Downloader" , bg = "gray3",fg = "dark orange" , font = ("lucida 20 bold"))
heading.pack(anchor = CENTER , pady = 10)

#TODO : video url
link = Label(root,text = "Video URL" , bg = "gray3",fg = "dark orange" , font = ("lucida 13 "))
link.pack(anchor = "nw" , padx = 30 , pady = 25)

#TODO : VIDEO LINK ENTRY
entry_url = StringVar()
link_entry = Entry(root , textvariable = entry_url , width = 52 , font = ("lucida 10"))
link_entry.place(x = 120 , y = 83)
link_entry.focus()

#TODO : LINK ERROR
link_error = Label(root,text = "", bg = "gray3" , fg = "dark orange", font = ("luciuda 11"))
link_error.place(x = 300 , y = 105)

#TODO : SET PATH
path =  Label(root,text = "Path", bg = "gray3" , fg = "dark orange", font = ("luciuda 13"))
path.pack(anchor = "nw" , padx = 30 , pady = 1)

#TODO : PATH HOLDER
path_holder = Label(root,text = "\t\t\t\t", bg = "white" , fg = "black", width = 29 ,font = ("luciuda 11"))
path_holder.place(x = 120 , y = 130)

#TODO : PATH BUTTON
path_btn = Button(root , text = "Select Path" , width = 10 , bg = "yellow" , activebackground = "red" , activeforeground = "white" , font = ("lucida 11 bold") , command = set_path)
path_btn.place(x = 400, y = 126)

#TODO : PATH ERRROR
path_error = Label(root , bg = "gray3" , fg = "orange" , font = ("lucida 11"))
path_error.place(x = 300 , y = 158)

#TODO : DOWNLOAD TYPE
download_type = Label(root , text = "Download Types" , bg = "gray3" , fg = "dark orange" , font = ("lucida 13"))
download_type.pack(anchor = "w" , padx = 30, pady = 25)

options = ["High Quality" , "Low Quality" , "Audio"]

#TODO : CHOOSE TYPE FOR DOWNLOAD
types = ttk.Combobox(root, values = options,width = 15, state = "r" , font = ("lucida 13"))
types.current(0)
types.place(x = 166 , y = 187)

#TODO : NORMAL TEXT
choose_type = Label(root , text = "Choose Type" , bg = "gray3" , fg = "dark orange" , font = ("lucida 13"))
choose_type.place(x = 340 , y = 187)

#TODO : BUTTGON FOR START DOWNLOAD
Button(root , text = "Start Download" , font = "lucida 13 bold" , width = 40 , bg = "yellow" , activebackground = "red" , activeforeground = "white" , command = start_download).pack()

#TODO : DOWNLOAD START NOTICE
download_out = Label(root , text = "Wait If System Show No Responding During Download" , bg = "gray3" , fg = "dark orange" , font = ("lucida 13"))
download_out.pack(anchor = CENTER , pady = 10)

#TODO : SHOW THE PROJECT NAME
download_name = Label(root , bg = "gray3" , fg = "dark orange" , font = ("lucida 13"))
download_name.pack(anchor = "nw" , pady = 10 , padx = 30)

#TODO : SHOW THE DOWNLOAD LOCATION
download_loc = Label(root , bg = "gray3" , fg = "dark orange" , font = ("lucida 13"))
download_loc.pack(anchor = "nw" , padx = 30 , pady = 10)

#TODO : SHOW SIZE OF DOWNLOAD
download_size = Label(root , text = "" , bg = "gray3" , fg = "dark orange" , font = ("lucida 13"))
download_size.pack(anchor = "nw" , padx = 30 , pady = 10)
root.mainloop()
