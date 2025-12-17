import tkinter as tk

# 1. Créez la fenêtre principale
root = tk.Tk()
root.title("Image de fond avec Canvas")

# 2. Créez un Canvas
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack(fill="both", expand=True)

# 3. Chargez et affichez l'image sur le Canvas
image = tk.PhotoImage(file="pictures/plateau_menu.png")
canvas.create_image(-600, -500, image=image, anchor="nw")

# 4. Ajoutez le titre "OTHELLO"
canvas.create_text(
    300, 50,               # position (x, y)
    text="OTHELLO",
    font=("Arial", 32, "bold"),
    fill="black"           # change la couleur si besoin
)

# 5. Ajoutez des widgets sur le Canvas
button = tk.Button(root, text="JOUER")
canvas.create_window(300, 100, window=button)

# 6. Lancez la boucle principale
root.mainloop()
