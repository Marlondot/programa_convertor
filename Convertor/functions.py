import pandas as pd
from datetime import datetime

def transpose_of_column(data,column_name,k,assigned_name):
  """
  Transforms a data vector [a_1, ..., a_n]^{T} into a dataframe [ [a_1, ... , a_k ], [a_{k+1}, ... , ] , ..., [] ] for a given K
  
  :param data: It's the dataframe from which we are getting de data vector
  :param column_name: It's the name of the column in the dataframe data which is our data vector
  :param k: It's our number of columns in our transformed dataframe
  :param assigned_name: It's the name given to the columns in the transformed dataframe
  
  :return: The transformed column into a datagrame with k columns
  """
  en_csv= pd.DataFrame()

  # Creating the dataframe with given <k> columns each of them with a given name <name>
  for i in range(k):
    nombre_columna=assigned_name+str(i+1)
    en_csv[nombre_columna]=""


  numero_index= data.shape[0]
  cuenta_uno_por_uno=0

  #Passing through data each pack of data
  for i in range( (numero_index//k) + 1):
    
    llenado=list()
    
    for _ in range(k):
      if cuenta_uno_por_uno>=numero_index:
        llenado.append("")
        continue
      llenado.append(data.loc[cuenta_uno_por_uno][column_name])
      cuenta_uno_por_uno+=1
    
    en_csv.loc[i]=llenado

  return en_csv


def transpose_of_data(data:pd.DataFrame,number_columns:int):
  """
  Apply the function transpose_of_column over each of the columns

  :methods: functions.transpose_of_column()

  :param data: It's the dataframe from which we are getting all the data vectors
  :param number_columns: It's our number of columns in our transformed columns

  :return: The transformed dataframe in (K*number_columns + 1)  columns
  """

  data_transformed=pd.DataFrame()
  data_transformed["PL."]=list(range(1, (data.shape[0]//number_columns) + 2))


  for column in list(data.columns):
    column_transposed=transpose_of_column(data,column,number_columns,column)
    data_transformed = pd.concat([data_transformed, column_transposed], axis=1, join='inner')

    
  #data_transformed["PL."] = data_transformed["PL."] + 1
  return data_transformed


def multiplying_columns(dataframe_by_reference:pd.DataFrame,column_quantity:str):
  """
  Muliply rows by the number of times it's indicated in the column column_quantity

  :param dataframe_by_reference: It's the dataframe where the function wants to be applied
  :param column_quantity: It's the name of the column in the dataframe that have the number by which the row will multiply

  :return: A new dataframe
  """

  data_transformed=pd.DataFrame()
  reference_columns=list(dataframe_by_reference.columns)
  reference_columns.remove(column_quantity)


  for column_e in reference_columns: # Creating the columns for the transformed dataframe
    data_transformed[column_e]=""

  index_in_data_transformed=0

  #Dataframe add of values
  for i in range(len(dataframe_by_reference.index)):
    quantity=dataframe_by_reference.loc[i][column_quantity]
    for _ in range(quantity):

      data_transformed.loc[index_in_data_transformed]=[dataframe_by_reference.loc[i][column_e] for column_e in reference_columns]
      
      index_in_data_transformed+=1
      
  return data_transformed

  
def data_extraction(dataframe_by_reference:pd.DataFrame):
  """
  
  """
  #[(numero_ot,ot),(sp_placa,placa),(),()]

  CONVERSION_MESES={"01":"ENERO",
                  "02":"FEBRERO",
                  "03":"MARZO",
                  "04":"ABRIL",
                  "05":"MAYO",
                  "06":"JUNIO",
                  "07":"JULIO",
                  "08":"AGOSTO",
                  "09":"SEPTIEMBRE",
                  "10":"OCTUBRE",
                  "11":"NOVIEMBRE",
                  "12":"DICIEMBRE",}
  
  datafame_transformed=dataframe_by_reference.copy()
  
  datafame_transformed["cantidad"] = datafame_transformed["cantidad"].astype(int)

  # Extrayendo el valor numerico de df.ot

  datafame_transformed["numero_ot"] = datafame_transformed["ot"].str.extract("(\d{5,})")

  # Extrayendo SP de df.placa

  datafame_transformed["sp_placa"] = datafame_transformed["placa"].str.extract("SP(\d{1,})")

  # Extrayendo CA de df.placa

  datafame_transformed["ca_placa"] = datafame_transformed["placa"].str.extract("CA(\d{1,})")

  # Extrayendo fecha de df.fecha

  datafame_transformed["fecha_year"] = datafame_transformed["fecha"].fillna(datetime.now().strftime('%Y')) # Si la fecha no está llenada se reemplaza por fecha actual
  datafame_transformed["fecha_mes"] = datafame_transformed["fecha"].fillna(datetime.now().strftime('%m'))
  datafame_transformed = datafame_transformed.replace({"fecha_mes":CONVERSION_MESES})

  datafame_transformed["f_placa"] = datafame_transformed["fecha_mes"] + " " + datafame_transformed["fecha_year"]


  return datafame_transformed

def extraction_placa(dataframe_by_reference:pd.DataFrame,number_columns:int):

  dataframe_data_extracted=data_extraction(dataframe_by_reference)

  dataframe_data_extracted_multiplication=multiplying_columns(dataframe_data_extracted,"cantidad")
  
  dataframe_data_extracted_multiplication.drop(columns=["fecha_mes","fecha_year","fecha","ot"],inplace=True)
  
  dataframe_data_extracted_multiplication.rename(
    columns={
      "placa":'No',
      "numero_ot":"ot",
      "sp_placa":"sp",
      "ca_placa":"ca",
      "f_placa":'f',
    },
    inplace=True
  )

  dataframe_transposed=transpose_of_data(dataframe_data_extracted_multiplication, number_columns)

  return dataframe_transposed



