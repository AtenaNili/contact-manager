import tkinter as tk
import sqlite3
from tkinter import messagebox
import customtkinter as ctk

root = tk.Tk()
root.title("my contact")
root.geometry("600x470")
root.configure(bg="#F1F1F1")
font_style = ("Montserrat", 12)

con = sqlite3.connect("contact.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS contact(
    Id INTEGER PRIMARY KEY,
    name TEXT,
    phone TEXT
)
""")
con.commit()

def add_contact():
    try:
        name = entry_name.get()
        phone = entry_phone.get()
        
        if name == "" or phone == "":
            messagebox.showerror("Error 101", "Please enter name and phone number")
            return

        cur.execute("INSERT INTO contact(name,phone) VALUES(?,?)", (name,phone))
        con.commit()
        listbox.insert(tk.END, f"{name}->{phone}")
        entry_name.delete(0,tk.END)
        entry_phone.delete(0,tk.END)
    except Exception as e:
        messagebox.showerror("error 101",f"wrong data enter your information again!:{e}",)


def search():

    sname = entry_sname.get()

    if sname=="":
        messagebox.showerror("error202","please enter a name!")
        return

    cur.execute("SELECT* FROM contact WHERE name LIKE ?",(f'%{sname}%',))
    result = cur.fetchall()

    if len(result)==0:
        messagebox.showinfo("result!","nothing found!")
        return
     
    listname= ""
    for contact in result:
        listname+= f"{contact[1]}->{contact[2]}"

    messagebox.showinfo("result",listname)


def delete_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("please select a row","nothing is selected!")
        return
    selected_data = listbox.get(selected[0])
    name, phone = selected_data.split("->")
    cur.execute("DELETE FROM contact WHERE name=? AND phone=?", (name.strip(), phone.strip()))
    con.commit()
    listbox.delete(selected[0])
    messagebox.showinfo("deleted!","contact deleted successfully!")

def edit_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("please select a row","nothing is selected!")
        return
    old_data = listbox.get(selected[0])
    old_name,old_phone = old_data.split("->")
    old_name = old_name.strip()
    old_phone = old_phone.strip()
    
    new_name = entry_name.get().strip()
    new_phone = entry_phone.get().strip()

    if new_name == "" or new_phone == "":
        messagebox.showerror("error303!","name or phone feild is empty!")
        return
    cur.execute("UPDATE contact SET name=?, phone=? WHERE name=? AND phone=?",(new_name, new_phone, old_name, old_phone))
    con.commit()

    listbox.delete(selected[0])
    listbox.insert(selected[0], f"{new_name}->{new_phone}")

    messagebox.showinfo("success", "contact edited successfully!")

tk.Label(
    root,
    text="Name",
    font=font_style,
    bg=root["bg"]
).grid(row=0, column=1, padx=(20,5), pady=5)
entry_name = ctk.CTkEntry(
    master=root,
    width=240,
    height=38,
    corner_radius=18,             
    placeholder_text="Enter name",
    font=font_style,
    fg_color="#FFFFFF",        
    text_color="#333333",      
    border_color="#68A3D6" )  
entry_name.grid(row=0, column=2, padx=(5,20), pady=5, sticky="W")

tk.Label(
    root,
    text="Phone Number",
    font=font_style,
    bg=root["bg"]
).grid(row=1, column=1, padx=(20,5), pady=5, sticky="E")
entry_phone = ctk.CTkEntry(
    master=root,
    width=240,
    height=38,
    corner_radius=18,
    placeholder_text="Enter phone",
    font=font_style,
    fg_color="#FFFFFF",        
    text_color="#333333",      
    border_color="#68A3D6")
entry_phone.grid(row=1, column=2, padx=(5,20), pady=5, sticky="W")


tk.Label(
    root,
    text="Search name",
    font=font_style,
    bg=root["bg"]
    ).grid(row=5, column=1, padx=5, pady=5)
entry_sname = ctk.CTkEntry(
    master=root,
    width=240,
    height=38,
    corner_radius=18,
    placeholder_text="Search...",
    font=font_style,
    fg_color="#FFFFFF",        
    text_color="#333333",      
    border_color="#68A3D6")
entry_sname.grid(row=5, column=2, padx=5, pady=5)



ctk.CTkButton(
    master=root,
    text="Add Contact",
    command=add_contact,
    width=140,
    height=38,
    corner_radius=18,
    fg_color="#4A90E2",
    hover_color="#357ABD",
    text_color="white",
    font=font_style
).grid(row=3, column=1, padx=5, pady=5)


ctk.CTkButton(
    master=root,
    text="Delete Contact",
    command=delete_contact,
    width=140,
    height=38,
    corner_radius=18,
    fg_color="#4A90E2",
    hover_color="#357ABD",
    text_color="white",
    font=font_style
).grid(row=3, column=2, padx=5, pady=5)


ctk.CTkButton(
    master=root,
    text="Edit Contact",
    command=edit_contact,
    width=140,
    height=38,
    corner_radius=18,
    fg_color="#4A90E2",
    hover_color="#357ABD",
    text_color="white",
    font=font_style
).grid(row=3, column=3, padx=5, pady=5)


ctk.CTkButton(
    master=root,
    text="Search Name",
    command=search,
    width=140,
    height=38,
    corner_radius=18,
    fg_color="#4A90E2",
    hover_color="#357ABD",
    text_color="white",
    font=font_style
).grid(row=5, column=3, padx=5, pady=5)




list_frame = tk.Frame(
    root,
    bg="#4A90E2",      
    padx=6,            
    pady=6             
)

list_frame.grid(
    row=4,
    column=0,
    columnspan=4,
    padx=(30, 10),     
    pady=10,
    sticky="w"
)

listbox = tk.Listbox(
    list_frame,
    width=48,
    height=8,
    font=font_style,
    bg="#FFFFFF",
    fg="#333333",
    selectbackground="#E3F2FD",
    selectforeground="#0D47A1",
    highlightthickness=0,   
    bd=0,
    activestyle="none"
)

listbox.pack(side="left", fill="both")


scroll = tk.Scrollbar(
    list_frame,
    bd=0
)
scroll.pack(side="right", fill="y")

listbox.config(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)
cur.execute("SELECT* FROM contact")
for contact in cur.fetchall():
    listbox.insert(tk.END, f"{contact[1]}->{contact[2]}")

root.mainloop()
con.close()
