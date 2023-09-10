Demucs Processor: Audio Stems Extraction GUI
Overview
Demucs Processor is a graphical user interface (GUI) application designed to simplify the process of extracting stems from audio files. This application is built using Python and utilizes the Demucs model for source separation. It's perfect for both computer science enthusiasts and music aficionados who want to process multiple audio files and folders quickly and efficiently.

Features
Select multiple audio folders for processing.
Automatic creation of output folders with _stems suffix.
GUI built with Tkinter for ease of use.
File and folder selection dialogs.
Process completion notifications.
Dependencies
Python 3.x
Tkinter
Demucs
os and subprocess Python modules
Installation
Make sure you have Python 3.x installed.
Clone this repository.
Navigate to the directory containing the script.
Run pip install -r requirements.txt to install the dependencies (Assuming that Demucs and Tkinter are listed in a requirements.txt file).
Usage
Run the script: python demucs_processor.py
Use the "I folder" button to select the input folder containing audio files.
Use the "O folder" button to select the output folder where the processed stems will be saved.
Click "Start Processing" to begin the extraction process.
License
MIT License

