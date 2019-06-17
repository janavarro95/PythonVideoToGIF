'''
Python MP4 to GIF

This python program interfaces moviepy by using tkinter as a way to creat gifs from videos.
Version: 1.0.0
Author: Joshua Navarro

'''


import tkinter as tk;
import os;
import platform;
from tkinter.filedialog import askopenfilename
from moviepy.editor import *

#Open file in tkinter
#https://stackoverflow.com/questions/3579568/choosing-a-file-in-python-with-simple-dialog

#Const window size
#https://stackoverflow.com/questions/36575890/how-to-set-a-tkinter-window-to-a-constant-size


#Simple tkinter docs
#https://www.geeksforgeeks.org/python-gui-tkinter/

#fileLabel=tk.Label(); #THIS IS TERRIBLE CODING

system=platform.system();
window=tk.Tk(); #the main window for tkinter
selectedFileName=tk.StringVar();

startSecond=tk.StringVar();
startMinute=tk.StringVar();
endSecond=tk.StringVar();
endMinute=tk.StringVar();
outputName=tk.StringVar();


def cls():
    if system=="Windows":
        os.system("cls");
    else:
        os.system("clear")

def openCMD():
    if system=="Windows":
        os.system("start cmd");

def isStringEmpty(string):
    if not string:
        return True;
    else:
        return False;

def openFileExplorer():
    filename=askopenfilename(filetypes=[("Video Files", "*.mp4")]);
    if isStringEmpty(filename):
        print("No file selected.");
        changeLabelText(selectedFileName,"No File Selected");
    else:
        print(filename);
        changeLabelText(selectedFileName,filename);
    #return filename;

def getPath(fileName):
    return os.path.dirname(fileName);

def changeLabelText(labelText,text):
    labelText.set(text);
    return;

"""
Creates the actual gif file.
"""
def createGIF():
    if isStringEmpty(selectedFileName.get()) or selectedFileName.get()=="No File Selected":
        print("No file selected. Can't create GIF");
        return;

    if isStringEmpty(startSecond.get()):
        print("Start Second Not Set");
        return;

    if isStringEmpty(startMinute.get()):
        print("Start Minute Not Set");
        return;

    if isStringEmpty(endSecond.get()):
        print("End Second Not Set");
        return;

    if isStringEmpty(endMinute.get()):
        print("End Minute Not Set");
        return;

    if isStringEmpty(outputName.get()):
        print("Output Name not set!!");
        return;

    finalPath= os.path.join(getPath(selectedFileName.get()),outputName.get()+".gif");
    
    clip=(VideoFileClip(selectedFileName.get())
        .subclip( (int(startMinute.get()) , float(startSecond.get())) , (int(endMinute.get()) ,float(endSecond.get()))) 
        .resize(1));
    clip.write_gif(finalPath);
    print ("All done creating .gif "+finalPath);

def main():
    cls();

    
    window.title("Video To GIF GUI");

    #Set width and height
    window.geometry("500x500");
    
    mainFrame=tk.Frame(master=window); #Create a frame where we display everything.
    mainFrame.pack_propagate(0); #Don't let widgets control the app size
    mainFrame.pack(fill=tk.BOTH,expand=1);

    #Width and height for widgets is % based. I.E 100= full window

    button=tk.Button(master=mainFrame,text="Select File!", width=10,height=1,command=openFileExplorer); #Note command names MUST be the name of the commands with NO ()
    #Relative x, Relative y, anchor (c is center)
    button.place(relx=.15,rely=.15,anchor="c"); #Used to actually include the button.


    outputbutton=tk.Button(master=mainFrame,text="CreateGIF", width=10,height=1,command=createGIF); #Note command names MUST be the name of the commands with NO ()
    #Relative x, Relative y, anchor (c is center)
    outputbutton.place(relx=.15,rely=.70,anchor="c"); #Used to actually include the button.

    label=tk.Label(mainFrame,textvariable=selectedFileName);
    label.place(relx=.15,rely=.25,anchor="c");

    changeLabelText(selectedFileName,"No File Selected");


    fileNameLabel=tk.Label(mainFrame,text="Output Name");
    fileNameLabel.place(relx=.15,rely=.35,anchor="c");
    fileOutputEntry=tk.Entry(mainFrame,textvariable=outputName);
    fileOutputEntry.place(relx=.40,rely=.35,anchor="c");


    startMinuteLabel=tk.Label(mainFrame,text="StartMinute (int)");
    startMinuteLabel.place(relx=.15,rely=.45,anchor="c");
    startMinuteEntry=tk.Entry(mainFrame,textvariable=startMinute);
    startMinuteEntry.place(relx=.40,rely=.45,anchor="c");
    startSecondLabel=tk.Label(mainFrame,text="StartSecond (decimal)");
    startSecondLabel.place(relx=.15,rely=.50,anchor="c");
    startSecondEntry=tk.Entry(mainFrame,textvariable=startSecond);
    startSecondEntry.place(relx=.40,rely=.50,anchor="c");

    endMinuteLabel=tk.Label(mainFrame,text="EndMinute (int)");
    endMinuteLabel.place(relx=.15,rely=.55,anchor="c");
    endMinuteEntry=tk.Entry(mainFrame,textvariable=endMinute);
    endMinuteEntry.place(relx=.40,rely=.55,anchor="c");
    endSecondLabel=tk.Label(mainFrame,text="EndSecond (decimal)");
    endSecondLabel.place(relx=.15,rely=.60,anchor="c");
    endSecondEntry=tk.Entry(mainFrame,textvariable=endSecond);
    endSecondEntry.place(relx=.40,rely=.60,anchor="c");

    window.mainloop(); #Must go last!

main();
