import pickle
import subprocess
from skimage.io import imread
from skimage.transform import resize
import matplotlib.pyplot as plt
import os
import tkinter as tk
from PIL import ImageTk,Image



	
	
def predict_FMD():
    model = pickle.load(open('img_model.p','rb'))
    Categories = ["Healthy", "Diseased"]
    label.destroy()
    button1.destroy()
    button2.destroy()
    # datain = int(input("enter 1 to give camera captured image"))
    def fmd_path():
        labelpath.destroy()
        btconfirm.destroy()
        # btconfirm1.destroy()
        bt.destroy()
        lab.destroy()
        bt0.destroy()
        path = entry.get(1.0, "end-1c")
        labelpath1.config(text = "YOUR PATH: "+path)
        entry.destroy()
        model = pickle.load(open('img_model.p','rb'))
        Categories = ["Healthy", "Diseased"]
        dir = path
        img = imread(dir)

        img_resize=resize(img,(150,150,3))
        l=[img_resize.flatten()]
        probability=model.predict_proba(l)
        def disp():
                        labelpath.destroy()
                        btconfirm.destroy()
                        # btconfirm1.destroy()
                        bt.destroy()
                        # lab.destroy()
                        bt0.destroy()
                        entry.destroy()
                   
                    
                        pro1=(probability[0][0]*100)
                        pro2=(probability[0][1]*100)
                        bt1.destroy()
                    
                        last.destroy()
                    
                        lab=tk.Label(root,text="PREDICTION RESULTS",font=50)
                        lab.pack(fill="both",expand="true") 
                        lab1=tk.Label(root,text="Healthy ="" %s percentage "%(pro1),font=50)
                        lab2=tk.Label(root,text="Diseased ="" %s percentage "%(pro2),font=50)
                        lab3=tk.Label(root,text="\nThe predicted image is : "+Categories[model.predict(l)[0]],font=50)
                        image=Image.open(path)
                        res_img=image.resize((150,150))
                        img=ImageTk.PhotoImage(res_img)
                    
                        xx=tk.Label(root,image=img)
                        xx.image=img
                        xx.pack(expand="yes",fill="both",side="top",)
                    
                    
                   
                        lab1.pack(fill="both",expand="true")
                        lab2.pack(fill="both",expand="true")
                        lab3.pack(fill="both",expand="true")
        last=tk.Label(text="CLICK TO VIEW RESULT",font=20) 
        last.pack()
        bt1=tk.Button(text="result",command=disp,fg="white",height=2,width=20,bg='#0f4b6e')
        bt1.pack(expand=2,side="top")
        bt2=tk.Button(text="exit",command=root.destroy,fg="white",height=2,width=20,bg='#0f4b6e')
        bt2.pack(expand=2,side="bottom")
    def onbutton():
        subprocess.call(["g++","camerain.cpp"])
        tmp=subprocess.call("./camerain")
        f=open("count.txt","r")

        count=f.read()
	#path0=path
        pathoffile='/home/root/subprocess'
	#for i in os.listdir(pathoffile):
        # lab.destroy()
        bt.destroy()
        lab.destroy()
        bt0.destroy()
        entry.destroy()
        
        labelpath.destroy()
        btconfirm.destroy()
        f1=open("path.txt","r")
	
        path =f1.read()
        path1=os.path.join(pathoffile,path)
        img = imread(path1)
        img_resize=resize(img,(150,150,3))
        plt.imshow(img_resize)
        plt.show()
        l=[img_resize.flatten()]
        probability=model.predict_proba(l)
        print(probability)
        def display_out():
                    pro1=(probability[0][0]*100)
                    pro2=(probability[0][1]*100)
                    lt.destroy()
                    bt1.destroy()
                    entry.destroy()
                    
                    
                    
                    
                    lab=tk.Label(root,text="PREDICTION RESULTS",font=50)
                    lab.pack(fill="both",expand="true")
                    lab1=tk.Label(root,text="Healthy ="" %s percentage "%(pro1),font=50)
                    lab2=tk.Label(root,text="Diseased ="" %s percentage "%(pro2),font=50)
                    lab3=tk.Label(root,text="\nThe predicted image is : "+Categories[model.predict(l)[0]],font=50)
                    image=Image.open(path)
                    res_img=image.resize((150,150))
                    img=ImageTk.PhotoImage(res_img)
                    
                    xx=tk.Label(root,image=img)
                    xx.image=img
                    xx.pack(expand="yes",fill="both",side="top",)
                    
                    
                   
                    lab1.pack(fill="both",expand="true")
                    lab2.pack(fill="both",expand="true")
                    lab3.pack(fill="both",expand="true")
        lt=tk.Label(text="CLICK TO VIEW RESULT",font=20) 
        lt.pack()
        bt1=tk.Button(text="result",command=display_out,fg="white",height=2,width=20,bg='#0f4b6e')
        bt1.pack(expand=2,side="top")
        bt2=tk.Button(text="exit",command=root.destroy,fg="white",height=2,width=20,bg='#0f4b6e')
        bt2.pack(expand=2,side="bottom")
    labelpath=tk.Label(root,text="ENTER THE DESIRED PATH OF THE IMAGE",font=20)
    labelpath.pack(expand=1)
    labelpath1=tk.Label(root,text=" ")
    labelpath1.pack(expand=1)
    entry=tk.Text(root,height=2,width=40,bg="light blue")
    entry.pack(side="top")
    btconfirm=tk.Button(root,text="CONFIRM PATH",fg="white",bg="#0f4b6e",height=2,width=20,command=fmd_path)
    btconfirm.pack(expand=2)
    
    lab=tk.Label(text="CLICK TO CAPTURE AN IMAGE",font=20)
    lab.pack()
    

    bt=tk.Button(text="capture image",command=onbutton,fg="white",bg="#0f4b6e",height=2,width=20)
    bt.pack(expand=1)
    
    
    bt0=tk.Button(text="exit",command=root.destroy,fg="white",bg="#0f4b6e",height=2,width=20)
    bt0.pack(expand=2,side="left")
    
root=tk.Tk()
root.minsize(height=250,width=500)
root.title("FMD PREDICTION")
root.config()
frame=tk.Frame(root)
frame.pack()
label=tk.Label(root, text="DO YOU WANT TO PREDICT FMD?",font=20)
label.pack()


button1 = tk.Button(root,text="YES",command=predict_FMD,fg="white",height=2,width=20,bg='#0f4b6e')
button1.pack(expand=2,side="left")

button2 = tk.Button(root,text="NO",command=root.destroy,fg="white",bg='#0f4b6e',height=2,width=20)
button2.pack(expand=2,side="right")

root.mainloop()




