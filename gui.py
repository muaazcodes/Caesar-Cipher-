import dearpygui.dearpygui as dpg
import solver
import io, sys

# ----------------- Callback -----------------
def process_text():
    mode = dpg.get_value("Mode")
    text = dpg.get_value("input_text").upper().strip()
    shift_value = dpg.get_value("shift_key").strip()

    if not text:
        dpg.set_value("output_text", " Please enter a message.")
        return

    try:
        shift = int(shift_value)
    except ValueError:
        dpg.set_value("output_text", "⚠️ Shift key must be a number.")
        return

    buffer = io.StringIO()
    sys.stdout = buffer

    if mode == "Encrypt":
        solver.encryption(plain_text=text, shift_key=shift)
    else:
        solver.decryption(cipher_text=text, shift_key=shift)

    sys.stdout = sys.__stdout__
    result = buffer.getvalue().strip()

    if not result:
        result = "No output generated."
    dpg.set_value("output_text", result)

# ----------------- GUI Setup -----------------
dpg.create_context()
dpg.create_viewport(title="Caesar Cipher", width=550, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()

# Apply dark theme
with dpg.theme() as dark_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (100, 100, 100))
        dpg.add_theme_color(dpg.mvThemeCol_Text, (230, 230, 230))
        dpg.add_theme_color(dpg.mvThemeCol_Button, (60, 120, 200))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (80, 140, 220))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (100, 160, 240))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (45, 45, 45))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (65, 65, 65))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (85, 85, 85))

# ----------------- Layout -----------------
with dpg.window(label="Caesar Cipher Text", width=530, height=370, pos=(10, 10)):
    dpg.add_text(" Caesar Cipher Encryption & Decryption", color=(0, 170, 255))
    dpg.add_separator()

    dpg.add_spacing(count=5)
    dpg.add_combo(["Encrypt", "Decrypt"], default_value="Encrypt", label="Mode", tag="mode", width=150)

    # Message input
    dpg.add_text("Enter Message:")
    dpg.add_input_text(tag="input_text", width=480)
    dpg.add_spacing(count=5)

    # Shift Key input
    dpg.add_text("Enter Shift Key:")
    dpg.add_input_text(tag="shift_key", width=100)
    dpg.add_spacing(count=3)

    dpg.add_spacing(count=3)
    dpg.add_button(label="Process", width=120, height=50, callback=process_text)
    dpg.add_separator()

    dpg.add_text("Output:", color=(0, 255, 128))
    dpg.add_input_text(tag="output_text", width=480, multiline=True, readonly=True, height=120)

dpg.bind_theme(dark_theme)
dpg.start_dearpygui()
dpg.destroy_context()
