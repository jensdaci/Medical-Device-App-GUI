import tkinter as tk
#import canvas as ck
import arduino_graphing_3sensors as gr
from PIL import Image, ImageTk

def startCommand():
    fn = entry1.get()
    ln = entry2.get()
    date = entry3.get()
    entry1.delete(0, "end")
    entry2.delete(0, "end")
    entry3.delete(0, "end")
    print ("================================")
    print ("First Name:\t" + str(fn))
    print ("Last Name:\t" + str(ln))
    print ("Date:\t\t" + str(date))
    print ("================================")
    gr.startGraph()

def main ():
    root = tk.Tk()
    root.title("Welcome")
    root.minsize(width = 500, height = 700)
    root.maxsize(width = 500, height = 700)

    global entry1
    global entry2
    global entry3

    # Title Frame
    title_frame = tk.Frame(root, bg = "white")
    title1 = tk.Label(title_frame, text = "THE PENCIL GRIP", font=("Segoe UI", 18, 'bold'), width = 150, height = 1, relief=tk.RIDGE, fg='black', bg='white')
    title1.pack(padx = 5, pady = 5)
    title2 = tk.Label(title_frame, text = "Home Page", font=(8), width = 150, height = 1, fg='black', bg='white')
    title2.pack(padx = 5, pady = 10)
    title_frame.pack(padx = 5, pady = 5)
    
    # Logo (no frame)
    canvas = tk.Canvas(root, width = 275, height = 245)
    canvas.pack()      
    img = ImageTk.PhotoImage(Image.open("grip.png")) 
    canvas.create_image(135,130,image=img)
    
    # Info Entry Frames
    entry0_frame = tk.Frame(root, bg = 'white')
    label0 = tk.Label(entry0_frame, text="Please enter the following information: ", bg="white")
    label0.pack()
    entry0_frame.pack(padx = 10, pady = 10 )
    
    entry1_frame = tk.Frame(root, bg = 'white')
    label1 = tk.Label(entry1_frame, text="First Name:  ", bg="white")
    label1.pack(side=tk.LEFT)
    entry1 = tk.Entry(entry1_frame, width = 30)
    entry1.pack(side=tk.LEFT)
    entry1_frame.pack(padx = 10, pady = 10)
    
    entry2_frame = tk.Frame(root, bg = 'white')
    label2 = tk.Label(entry2_frame, text="Last Name:  ", bg="white")
    label2.pack(side=tk.LEFT)
    entry2 = tk.Entry(entry2_frame, width = 30)
    entry2.pack(side=tk.LEFT)
    entry2_frame.pack(padx = 10, pady = 10)

    entry3_frame = tk.Frame(root, bg = 'white')
    label3 = tk.Label(entry3_frame, text="Date (mm/dd/yy):", bg="white")
    label3.pack(side=tk.LEFT)
    entry3 = tk.Entry(entry3_frame, width = 24)
    entry3.pack(side=tk.LEFT)
    entry3_frame.pack(padx = 10, pady = 10)

    # Start Button (no frame)
    button1 = tk.Button(root, text = "START TEST", font=(15), width = 12, height = 1, fg='white', bg='black', command = startCommand)
    button1.pack(padx = 10, pady= 10 )


    # Project Information Frame
    information_frame = tk.Frame(root)
    info = "Pencil Grip" + u"\u2122" + "\nJens Daci, Kehinde Williams, Elis Cucka, Mariam Gabriel, Jonathan Coskuner \nIn association with Dr. Artan and Dr. Lopez"
    label2 = tk.Label(information_frame, bg = "white", text = info, justify = 'left')
    label2.pack()
    information_frame.pack(padx = 1, pady = 35)
    
    root.configure(background = 'white')
    root.mainloop()


if __name__ == "__main__":
    main()
