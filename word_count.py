"""Taller evaluable"""
 
import glob

import pandas as pd


def load_input(input_directory):
    
    """Load text files in 'input_directory/'"""
    #
    # Lea los archivos de texto en la carpeta input/ y almacene el contenido en
    # un DataFrame de Pandas. Cada línea del archivo de texto debe ser una
    # entrada en el DataFrame.
    #
    filenames = glob.glob(f"{input_directory}/*.txt")
    #Dataframes =[]
    #for filename in filenames:
    #dataframe =[]
    #df = pd.read.csv(filenames[0], sep="t", header=None, names=["text"]))
    dataframes = [
        pd.read_csv(filename, sep="\t" , header=None, names=["text"])
        for filename in filenames
    ]
    
    concatenated_df = pd.concat(dataframes, ignore_index=True)
    return concatenated_df

# df = load_input("input")
# print(df)

# load_input("input")
#tarea limpiar archivos palabras que tienen mayusculas y minusculas, eliminar puntuacion y acentos, como ñ
def clean_text(dataframe):
    """Text cleaning"""
    #
    # Elimine la puntuación y convierta el texto a minúsculas.
    #siempre hacer copia del data frame que entra por si se daña
    dataframe = dataframe.copy() #función del data frame que devuelve copia del dataframe
    dataframe["text"] = dataframe ["text"].str.lower() #Convertir todo a minusculas
    dataframe["text"] = dataframe ["text"].str.replace(".","")
    dataframe["text"] = dataframe ["text"].str.replace(",","")
    return dataframe

# df = load_input("input")
# df = clean_text(df)
# print (df)

def count_words(dataframe):
    """Word count"""
    # dataframe = dataframe.copy()
    # dataframe["text"] = dataframe["text"].str.split() #split comando para partir un linea en palabras que lo conforman separados por comas
    # dataframe = dataframe.explode("text") #cambia lineas a columnas
    # dataframe["count"] = 1 #agrega una columna cpunt y la llena de 1
    # dataframe = dataframe.groupby("text").agg({"count": "sum"}) # agg recibe como argumento un diccionario donde las claves son las columnas y 
    
    return dataframe

def count_words(dataframe):
    """Word count"""
    dataframe = dataframe.copy()
    dataframe["text"] = dataframe["text"].str.split() #split comando para partir un linea en palabras que lo conforman separados por comas
    dataframe = dataframe.explode("text") #cambia lineas a columnas
    dataframe = dataframe["text"].value_counts()
    
    
    return  dataframe

# df = load_input("input")
# df = clean_text(df)
# df = count_words(df)
# print (df)

def save_output(dataframe, output_filename):
    """Save output to a file."""

    dataframe.to_csv(output_filename, sep="\t" , index=True, header=False) 

# df = load_input("input")
# df = clean_text(df)
# df = count_words(df)
# save_output(df, "output.txt")
# print (df)

#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run(input_directory, output_filename):
    """Call all functions."""


    df = load_input("input")
    df = clean_text(df)
    df = count_words(df)
    save_output(df, output_filename)
    print (df)

if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )
