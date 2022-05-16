import pyspark.ml.stat
from pyspark.sql import DataFrame
from pyspark import StorageLevel
from types import MethodType

def ChiSquareTestForString(self, data, col1, col2):
    
    if isinstance(data, DataFrame):
        data_rdd = data.rdd
    else:
        raise Exception("data must be of type : 'pyspark DataFrame'.")
    
    if (col1 not in data.schema.names):
        raise Exception("Can not find {} in DataFrame columns.".format(col1))
    
    if (col2 not in data.schema.names):
        raise Exception("Can not find {} in DataFrame columns.".format(col2))
        
    data_ones = data_rdd.map(lambda row: ((row[col1], row[col2]), 1))
    observed_data = data_ones.reduceByKey(lambda x, y: x + y).map(lambda row: ((row[0][0], row[0][1]), row[1]))
    observed_data.persist(StorageLevel.MEMORY_AND_DISK)
    row_total = observed_data.map(lambda row: (row[0][0], row[1])).reduceByKey(lambda x, y: x + y)
    col_total = observed_data.map(lambda row: (row[0][1], row[1])).reduceByKey(lambda x, y: x + y)
    row_counts = row_total.count()
    col_counts = col_total.count()
    degree_of_freedom = (row_counts - 1) * (col_counts - 1)
    grand_data = row_total.map(lambda row: row[1]).sum()
    expected_data = row_total.cartesian(col_total).map(lambda row: ((row[0][0], row[1][0]), (row[0][1] * row[1][1])/ grand_data))
    expected_data.persist(StorageLevel.MEMORY_AND_DISK)
    chi_squared_table = observed_data.join(expected_data).map(lambda row: (row[0], ((row[1][0]-row[1][1])*(row[1][0]-row[1][1]))/row[1][1]))
    chi_squared_table.persist(StorageLevel.MEMORY_AND_DISK)
    chi_squared = chi_squared_table.map(lambda row: row[1]).sum()
    
    return chi_squared, degree_of_freedom

pyspark.ml.stat.ChiSquareTestForString = MethodType(ChiSquareTestForString, pyspark.ml.stat)