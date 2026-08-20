import tkinter as tk

def window_popup(
    root: tk.Tk,
    title: str,
    text: str,
    x_position: int,
    y_position: int,
) -> tk.Toplevel:
    window = tk.Toplevel(root)
    window.title(title)
    window.geometry(f"400x400+{x_position}+{y_position}")

    def close_window() -> None:
        window.destroy()
        if not root.winfo_children():
            root.destroy()

    window.protocol("WM_DELETE_WINDOW", close_window)

    title_label = tk.Label(
        window,
        text=title,
        font=("Segoe UI", 20, "bold"),
        justify="center",
    )
    title_label.pack(fill="x", padx=20, pady=(20, 10))

    fixtures_label = tk.Label(
        window,
        text=text,
        font=("Segoe UI", 14),
        justify="center",
        anchor="center",
    )
    fixtures_label.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    return window