from functions import *
from files_manager import *

import pandas as pd

def test_from_number_columns_to_csv():

    true_csv=pd.read_csv("sheet_tests\\test_sheet_transpose\\sheet_correct_1.csv",sep=";",dtype=str,converters={"PL.":int()}, na_filter=False)
    sheet=pd.read_excel("sheet_tests\\test_sheet_transpose\\sheet_test_1.xlsx",header=0)

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


