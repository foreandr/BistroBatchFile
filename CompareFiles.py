import sys
import csv
import operator
from subprocess import call
import pandas as pd


def grab_format_sort_bistro_csv():

    df = pd.read_csv('\\\\smb\Bistro\data_imports\Bistro_Current_Records_20220802.csv')  # GRAB FILE
    # df.to_csv('OROGINAL ALL NAMES.csv')
    df = df[0:563]  # CUT OFF EXTRA

    df = df.sort_values(by=["firstName", "lastName"], ascending=True)  # SORT
    df.to_csv('bistro.csv')

    bistro_array = []
    reader = csv.reader(open("bistro.csv"), delimiter=",")
    for i in reader:
        i.pop(0)
        bistro_array.append(i)
    bistro_array.pop(-2)

    return bistro_array


def grab_format_sort_andre_csv():
    df = pd.read_csv('\\\\smb\Bistro\!NEW-BISTRO\CURRENT_RECORD\Bistro_Current_Records_2022-08-02.csv')  # GRAB FILE
    df = df.sort_values(by=["firstName", "lastName"], ascending=True)  #
    df.to_csv('andre.csv')

    andre_array = []
    reader = csv.reader(open("andre.csv"), delimiter=",")
    for i in reader:
        i.pop(0)
        andre_array.append(i)

    return andre_array


bistro_array = grab_format_sort_bistro_csv()
andre_array = grab_format_sort_andre_csv()


for i in range(len(andre_array)):
    for j in range(len(andre_array[i])):
        if j == 0:
            continue
        if andre_array[i][j] != bistro_array[i][j]:
            print("NAME:", andre_array[i][0], andre_array[i][1], bistro_array[i][0], bistro_array[i][1], "[",
            andre_array[i][j], "!=", bistro_array[i][j], "]")
