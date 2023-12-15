from Convertor.files_manager import get_file_path,save_file_in_path,sheet_to_dataframe
from Convertor.functions import transpose_of_data,extraction_placa

if __name__ == "__main__":
    mensaje="""
            Ingresar número de operación a realizar:
            (1) Extracción de valores de placa con archivo tipo [placa,ot,cantidad,fecha]
            (2) Transposición de datos tipo [n,L,m]
            """
    print(mensaje)

    case=int(input())

    if case==1:

        sheet_dataframe = sheet_to_dataframe()
        
        number_columns=int(input("Ingrese el número de páginas: "))

        transposed_dataframe=extraction_placa(sheet_dataframe,number_columns)

        save_file_in_path(transposed_dataframe)

    elif case==2:
        
        sheet_dataframe = sheet_to_dataframe()

        number_columns=int(input("Ingrese el número de páginas: "))

        transposed_dataframe=transpose_of_data(sheet_dataframe,number_columns)

        save_file_in_path(transposed_dataframe)




