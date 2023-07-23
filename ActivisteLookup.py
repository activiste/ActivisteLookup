import tkinter as tk
import requests
#-----def fonctions-----
def exit():
    Activiste.destroy()
def lookup():
 ip = ip_tr.get()
 requestweb = requests.get(f"https://ipinfo.io/{ip}/json")
 data = requestweb.json()
 result_text.config(state=tk.NORMAL)
 result_text.delete("1.0", tk.END)
 result_text.insert(tk.END, f"IP: {data['ip']}\n")
 result_text.insert(tk.END, f"Hostname: {data['hostname']}\n")
 result_text.insert(tk.END, f"Ville: {data['city']}\n")
 result_text.insert(tk.END, f"Région: {data['region']}\n")
 result_text.insert(tk.END, f"Pays: {data['country']}\n")
 result_text.insert(tk.END, f"Code postal: {data['postal']}\n")
 result_text.insert(tk.END, f"Coordonnées: {data['loc']}\n")
 result_text.insert(tk.END, f"Organisation: {data['org']}\n")
 result_text.config(state=tk.DISABLED)
#-----Settings AIO-----
Activiste = tk.Tk()
Activiste.geometry("500x550")
Activiste.title("ACTIVISTE | IP LOOKUP")
#-----Interface graphique-----
titre = tk.Label(Activiste, text="✧ ACTIVISTE LOOKUP ✧", font=("Courier", 20))
titre.pack(side="top", pady=50)
devtag = tk.Label(Activiste, text="( dev by Activiste )", font=("Courier", 10))
devtag.pack(side="top")
ip_frame = tk.Frame(Activiste)
ip_frame.pack(pady=20)
ip_put = tk.Label(ip_frame, text="Adresse IP:")
ip_put.pack(side="left")
ip_tr = tk.Entry(ip_frame, width=20)
ip_tr.pack(side="left")
lookup_btn = tk.Button(Activiste, text="Lookup", command=lookup)
lookup_btn.pack(pady=10)
result_text = tk.Text(Activiste, height=10, width=40)
result_text.config(state=tk.DISABLED)
result_text.pack()
exitbtn = tk.Button(Activiste, text="Exit", font=("Courier", 12), borderwidth=2, relief="groove", padx=15, pady=10, command=exit)
exitbtn.pack(pady=20)
#-----config-----
for btn in [lookup_btn, exitbtn]:
    btn.config(highlightthickness=0, bd=0, highlightbackground="black", highlightcolor="black", borderwidth=0, relief="groove", padx=15, pady=10, font=("Courier", 12), bg="white", fg="black", activebackground="black", activeforeground="white", disabledforeground="grey")
Activiste.mainloop()
