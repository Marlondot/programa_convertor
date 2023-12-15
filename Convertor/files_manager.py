import tkinter
from tkinter import filedialog
import pandas as pd

def sheet_to_dataframe():
    """
    Uses get_file_path() to get a path and then read that file with pandas

    :methods: file_manager.get_file_path()

    :return: return reference for dataframe generated
    """

    sheet_path=get_file_path()
    
    excel_archivo=pd.read_excel(sheet_path,header=0)

    return excel_archivo

def get_file_path():
    """
    Uses the tkinter library to return a folders path

    :return: Returns folder path
    """
    tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing

    file_path = filedialog.askopenfilename(filetypes=(("xlsx", "*.xlsx"), ("all files", "*.*"))) #===assigns the path to filepath

    return file_path

def save_file_in_path(dataframe_by_reference):
    """
    Uses tkinter library to save a csv, given a tkinter given path and filenames

    :param dataframe_by_reference: uses the reference (python doc) of a dataframe

    :return: True if completed
    """
    filename = filedialog.asksaveasfilename(filetype=[('CSV files', '*.csv')])

    dataframe_by_reference.to_csv(filename,sep=';')
    
    return True