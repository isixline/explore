import akshare as ak
import pandas as pd
from datetime import datetime

# 使用 AKShare 获取上证指数的日交易数据
stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()


# 用当前日期和股票代码构建文件名
filename = f"stock_zh_a_spot_em_{datetime.today().strftime('%Y%m%d')}.csv"

# 将数据存储为 CSV 文件
stock_zh_a_spot_em_df.to_csv(filename, index=False)
