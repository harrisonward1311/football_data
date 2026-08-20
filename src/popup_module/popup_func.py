import tkinter as tk

def window_popup(text: str):
    window = tk.Tk()
    window.title("Football Fixtures")
    window.geometry("400x400")

    fixtures_label = tk.Label(
        window,
        text=text,
        justify="left",
        anchor="w",
    )
    fixtures_label.pack(fill="both", expand=True, padx=20, pady=20)

    window.mainloop()