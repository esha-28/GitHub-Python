from pytube import YouTube
import urllib.request
import urllib.parse
import pyttsx3 as pt
import webbrowser as wb
from tkinter import *
from pynotifier import Notification

root=Tk()
root.title('YouTube Downloader')
root.config(bg='gray20')
root.iconbitmap('iconfinder_Rounded-05_2024668.ico')
root.geometry('525x350')


def download():
    try:
        path = i2.get()
        yt = YouTube(url)
        stream = yt.streams.first()
        stream.download(path) # choose path for save download video
        Notification(title='Download status',
                 description='Download is complete',
                 icon_path=r'bell_sign_twitter_icon_127116.ico',
                 duration=15).send()
    except:
        Notification(title='download error',
                     description='Download path error. Check the path',
                     icon_path=r'bell_sign_twitter_icon_127116.ico',
                     duration=15).send()

def play():
    wb.open_new(url)

def send():
    global url
    song = i.get()
    query_string = urllib.parse.urlencode({"search_query": song})
    html_cont = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_res = re.findall(r'href=\"\/watch\?v=(.{11})', html_cont.read().decode())
    url = "http://www.youtube.com/watch?v=" + search_res[0]
    d3 = pt.init()
    d3.say("for playing the music, press the play button, and, for download, choose the path for save download video")
    voices2 = d3.getProperty('voices')
    d3.setProperty('voice', voices2[0].id)
    d3.setProperty('rate', 1.5)
    d3.setProperty('volume', 2.0)
    d3.runAndWait()
    d3.stop()
    
def func_keyboard(event):
    send()
    
l1=Label(root,text='YouTube Downloader',font=('arial',15,'bold'),bg='red3',fg='white')
l1.grid(row=0,columnspan=2,pady=15,ipady=5,padx=10,ipadx=5)
l1.config(anchor=CENTER)

l2=Label(root,text='Search in YouTube:',bg='red3',fg='white',font=('arial',10,'bold'))
l2.grid(row=1,column=0,pady=10,ipady=5,padx=5,ipadx=5)

i=StringVar()
e1=Entry(root,textvariable=i,width=40,border=2)
e1.grid(row=1,column=1,sticky='w',ipady=3)
e1.bind("<Return>", func_keyboard)

l4 = Label(root, text='Choose Path for Save Download Video:',bg='red3',fg='white')
l4.grid(row=2,column=0,pady=10,ipady=5,padx=5)

i2 = StringVar()
e2 = Entry(root, textvariable=i2,width=40,border=2)
e2.grid(row=2, column=1,pady=5,ipady=5,sticky='w')
e2.insert(END, 'EX:--' + r'C:\Users\Esha\Desktop\project\project-2')

b1=Button(root,text='Play',command=play)
b1.grid(row=1,column=3)

photo_send=PhotoImage(file='arrow_entrance_in_internet_log_login_security_icon_127060.png')
b2=Button(root,image=photo_send,command=send)
b2.grid(row=1,column=2)

b3=Button(root,text='Download',command=download,bd=2)
b3.grid(row=4,columnspan=2)


root.mainloop()
