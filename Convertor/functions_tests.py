from Convertor.functions import *
import pandas as pd

def test_transpose_of_column():

    data = [['a1', 10], 
            ['a2', 15], 
            ['a3', 14],
            ['a4', 10], 
            ['b1', 15], 
            ['b2', 14],
            ['b3', 10], 
            ['b4', 15], 
            ['c1', 14],]
    
    df = pd.DataFrame(data, columns=['Name', 'Number'])

    data_comparation=[
        ["a1","a2","a3","a4"],
        ["b1","b2","b3","b4"],
        ["c1","","",""]
    ]

    df_comparation = pd.DataFrame(data_comparation, columns=["L1","L2","L3","L4"])

    df_function = transpose_of_column(df,"Name",4,"L")

    #print(df_function)
    #print(df_comparation)

    assert pd.testing.assert_frame_equal(df_comparation,df_function) is None #Check for documentation of pd.testing.assert_frame_equal


def test_transpose_of_data():

    data = [['a1', 10], 
            ['a2', 15], 
            ['a3', 14],
            ['a4', 10], 
            ['b1', 15], 
            ['b2', 14],
            ['b3', 10], 
            ['b4', 15], 
            ['c1', 14],]
    
    df = pd.DataFrame(data, columns=['L', 'N'])

    data_comparation=[
        [1,"a1","a2","a3","a4",10,15,14,10],
        [2,"b1","b2","b3","b4",15,14,10,15],
        [3,"c1","","","",14,"","",""]
    ]

    df_comparation = pd.DataFrame(data_comparation, columns=["PL.","L1","L2","L3","L4","N1","N2","N3","N4"])

    df_function = transpose_of_data(df,4)

    #print(df_function)
    #print(df_comparation)

    assert pd.testing.assert_frame_equal(df_comparation,df_function) is None #Check for documentation of pd.testing.assert_frame_equal

def test_multiplying_columns():

    true_csv=pd.read_csv("Convertor\\sheet_tests\\test_multiplying_columns\\sheet_correct_multiplying_columns.csv",sep=";")
    true_csv = true_csv. dropna(axis=1)
    df=pd.read_excel("Convertor\\sheet_tests\\test_multiplying_columns\\sheet_test_multiplying_columns.xlsx",header=0)

    false_csv=multiplying_columns(df,"cantidad")

    try:
        assert pd.testing.assert_frame_equal(false_csv,true_csv) is None #Check for documentation of pd.testing.assert_frame_equal
    except AssertionError:
        print("Expected csv:")
        print(true_csv)
        print("You csv:")
        print(false_csv)

        raise

def test_extraction_data():

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
    
    true_csv=pd.read_csv("Convertor\\sheet_tests\\test_data_extraction\\correct.csv",sep=";",dtype=str,converters={"cantidad":int()})
    
    df=pd.read_csv("Convertor\\sheet_tests\\test_data_extraction\\dataframe_for_function.csv",sep=";")

    false_csv=data_extraction(df)

    true_csv["fecha_year"]=datetime.now().strftime('%Y')
    true_csv["fecha_mes"]=CONVERSION_MESES[datetime.now().strftime('%m')]
    true_csv["f_placa"] = true_csv["fecha_mes"] + " " + true_csv["fecha_year"]


    false_csv = false_csv.astype(str)
    true_csv = true_csv.astype(str)

    try:
        assert pd.testing.assert_frame_equal(false_csv,true_csv) is None #Check for documentation of pd.testing.assert_frame_equal
    except AssertionError:
        print("Expected csv:")
        print(true_csv)
        print("You csv:")
        print(false_csv)

        raise


def test_extraction_placa():
    
    true_csv=pd.read_csv("Convertor\\sheet_tests\\test_sheet_extraction_placa\\correct.csv",sep=";",dtype=str,converters={"cantidad":int()},na_values="")
    true_csv.fillna("",inplace=True)
    
    df=pd.read_excel("Convertor\\sheet_tests\\test_sheet_extraction_placa\\test.xlsx",header=0)

    false_csv=extraction_placa(df,8)

    false_csv = false_csv.astype(str)
    true_csv = true_csv.astype(str)

    try:
        assert pd.testing.assert_frame_equal(false_csv,true_csv) is None #Check for documentation of pd.testing.assert_frame_equal
    except AssertionError:
        print("Expected csv:")
        print(true_csv)
        print("You csv:")
        print(false_csv)

        raise


def test_from_number_columns_to_csv():

    true_csv=pd.read_csv("Convertor\\sheet_tests\\test_sheet_transpose\\sheet_correct_1.csv",sep=";",dtype=str,converters={"PL.":int()}, na_filter=False)
    sheet=pd.read_excel("Convertor\\sheet_tests\\test_sheet_transpose\\sheet_test_1.xlsx",header=0)

    false_csv=transpose_of_data(sheet,8)

    
    false_csv = false_csv.astype(str)
    true_csv = true_csv.astype(str)

    #assert pd.testing.assert_frame_equal(false_csv,true_csv) is None #Check for documentation of pd.testing.assert_frame_equal

    try:
        assert pd.testing.assert_frame_equal(false_csv,true_csv) is None #Check for documentation of pd.testing.assert_frame_equal
    except AssertionError:
        print("Expected csv:")
        print(true_csv)
        print("You csv:")
        print(false_csv)

        raise


def test_words_in_line_extraction():

    true_csv=pd.read_csv("Convertor\\sheet_tests\\test_words_in_line_extraction\\correct.csv",sep=";",dtype=str,converters={"cantidad":int()},na_values="")
    true_csv.fillna("",inplace=True)
    
    df=pd.read_excel("Convertor\\sheet_tests\\test_words_in_line_extraction\\test.xlsx",header=0)

    false_csv = words_in_line_extraction(df,8)

    false_csv = false_csv.astype(str)
    true_csv = true_csv.astype(str)

    #assert pd.testing.assert_frame_equal(false_csv,true_csv) is None #Check for documentation of pd.testing.assert_frame_equal

    try:
        assert pd.testing.assert_frame_equal(false_csv,true_csv) is None #Check for documentation of pd.testing.assert_frame_equal
    except AssertionError:
        print("Expected csv:")
        print(true_csv)
        print("You csv:")
        print(false_csv)

        raise


    


