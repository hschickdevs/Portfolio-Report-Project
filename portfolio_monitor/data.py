from os.path import splitext

import pandas as pd


def load_portfolio(path: str) -> list[tuple[str, pd.DataFrame]]:
    """
    Attempts to load the portfolio input and checks that all required parameters are satisfied.

    :param path: The path to the portfolio data  spreadsheet
    :return: List containing tuple pairs of sheetname (portfolio name), and portfolio dataframe
    """
    output = []
    if splitext(path)[-1] == ".csv":
        output.append(("Portfolio", pd.read_csv(path)))
    else:
        xls = pd.ExcelFile(path)
        for sheet in xls.sheet_names:
            output.append((sheet, pd.read_excel(path, sheet_name=sheet)))

    # Assert mandatory columns are set
    MANDATORY_COLS = ["Symbol", "Entry Price", "Shares"]
    for sheet in output:
        assert all(col in sheet[1].columns for col in MANDATORY_COLS), f"Sheet '{sheet[0]}' missing mandatory column. " \
                                                                       f"({MANDATORY_COLS})"
    return output

