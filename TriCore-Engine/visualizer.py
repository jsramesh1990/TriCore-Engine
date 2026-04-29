import tkinter as tk

root = tk.Tk()
root.title("TriCore Terminal Engine")
root.geometry("700x500")

calc = tk.LabelFrame(root, text="Calculator", padx=10, pady=10)
calc.pack(fill="x", padx=10, pady=5)

server = tk.LabelFrame(root, text="Server Connection Display", padx=10, pady=10)
server.pack(fill="x", padx=10, pady=5)
tk.Label(server, text="Server: Connected").pack()

client = tk.LabelFrame(root, text="Client Connection Display", padx=10, pady=10)
client.pack(fill="x", padx=10, pady=5)
tk.Label(client, text="Client: Connected").pack()

close_btn = tk.Button(root, text="Close Windows", command=root.destroy)
close_btn.pack(pady=20)

root.mainloop()
