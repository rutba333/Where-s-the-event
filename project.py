import tkinter as tk
def convert_to_cm():
    try:
        inches=float(entry.get())
        centimeters=inches * 2.54
        result_label.config(text=f"{centimeters:2f} cm")
    except ValueError:
        result_label.config(text="Please enter a valid number!")

#create a window
root=tk.Tk()
root.title("Inches to centimeters converter")

#create and place widgets
tk.Label(root,text="Enter lenth in inches:").grid(row=0,column=0,padx=10,pady=10)
entry=tk.Entry(root)
entry.grid(row=0,column=1,padx=0,pady=0)

convert_button=tk.Button(root,text="Convert",command=convert_to_cm)
convert_button.grid(row=1,column=0,columnspan=2,pady=10)

result_label=tk.Label(root,text="")
convert_button.grid(row=2,column=0,columnspan=2,pady=10)

root.mainloop()
