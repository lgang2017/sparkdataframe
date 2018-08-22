def start():
    print("import successful")
def spark_concat(_list):
    spark_df = _list[0]
    for i in range(len(_list)-1)
        spark_df = spark_df.unionByName(_list[i+1])
    return spark_df
