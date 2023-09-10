import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def process_demucs(input_path, output_folder):
    # Checking if the provided input path is a directory
    if not os.path.isdir(input_path):
        messagebox.showerror("Error", f"'{input_path}' is not a valid directory.")
        return

    # Iterating over all directories inside the main input directory
    for subfolder in os.listdir(input_path):
        full_subfolder_path = os.path.join(input_path, subfolder)
        if not os.path.isdir(full_subfolder_path):  # Skipping if it's not a directory
            continue

        # Creating corresponding output subfolder with "_stem" appended
        output_subfolder_path = os.path.join(output_folder, f"{subfolder}_stems")
        if not os.path.exists(output_subfolder_path):
            os.makedirs(output_subfolder_path)

        # Iterating over all audio files in the subfolder
        for audio_file in os.listdir(full_subfolder_path):
            full_audio_path = os.path.join(full_subfolder_path, audio_file)
            if not os.path.isfile(full_audio_path):
                continue

            base_name, _ = os.path.splitext(audio_file)
            subprocess.run(["demucs", full_audio_path])

            # Creating directory for stems corresponding to the audio file
            stems_folder_path = os.path.join(output_subfolder_path, base_name)
            if not os.path.exists(stems_folder_path):
                os.makedirs(stems_folder_path)

            default_output_path = os.path.join("separated", "htdemucs", base_name)
            stems = ["drums", "bass", "vocals", "other"]
            for stem in stems:
                original_path = os.path.join(default_output_path, f"{stem}.wav")
                new_path = os.path.join(stems_folder_path, f"{base_name}_{stem}.wav")
                if os.path.exists(original_path):
                    os.rename(original_path, new_path)

            if os.path.exists(default_output_path):
                os.rmdir(default_output_path)

    messagebox.showinfo("Success", "Processing completed!")

def select_input_folder():
    path = filedialog.askdirectory(title="Select input folder")
    if path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, path)

def select_output():
    path = filedialog.askdirectory(title="Select output folder")
    if path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, path)

def start_processing():
    input_path = input_entry.get()
    output_path = output_entry.get()
    process_demucs(input_path, output_path)

app = tk.Tk()
app.title("Demucs Processor")

input_label = tk.Label(app, text="Input Folder:")
input_label.pack(padx=10, pady=5)

input_entry = tk.Entry(app, width=50)
input_entry.pack(padx=10, pady=5)

input_folder_button = tk.Button(app, text="I folder", command=select_input_folder)
input_folder_button.pack(padx=10, pady=5)

output_label = tk.Label(app, text="Output Folder:")
output_label.pack(padx=10, pady=5)

output_entry = tk.Entry(app, width=50)
output_entry.pack(padx=10, pady=5)

output_button = tk.Button(app, text="O folder", command=select_output)
output_button.pack(padx=10, pady=5)

start_button = tk.Button(app, text="Start Processing", command=start_processing)
start_button.pack(padx=10, pady=20)

app.mainloop()
