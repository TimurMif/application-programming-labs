import pandas


def graph_histogram(table: pandas.core.frame.DataFrame) -> list:
    """Graphic of count pixels and steps of highlights"""
    counter = []
    for row in range(0,table.shape[0]):
        counter.append(table.iat[row, table.columns.get_loc("Площадь изображения")])
    return counter