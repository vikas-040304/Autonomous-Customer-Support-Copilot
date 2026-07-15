import pandas as pd


def export_csv(df):

    file = "tickets.csv"

    df.to_csv(
        file,
        index=False
    )

    return file


def export_excel(df):

    file = "tickets.xlsx"

    df.to_excel(
        file,
        index=False
    )

    return file