import pyarrow.parquet as pq
import pandas as pd

# 读取 parquet 文件
file_path = "/Users/zhulinyu/Desktop/TraceGra/dataset/aiopschallengedata2025/sample/abnormal/case1/trace_jaeger-span_2025-04-27_03-59-00.parquet"
table = pq.read_table(file_path)

# 转换为 pandas DataFrame
df = table.to_pandas()

# 保存前3行数据到CSV文件
df.iloc[:3].to_csv('first_3_rows_abnormal.csv', index=False)
print("前3行数据已保存到 first_3_rows_abnormal.csv 文件")

