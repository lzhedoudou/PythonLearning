# 查询茅台股价
import tushare as ts
df = ts.get_hist_data('600519',start='2019-01-01',end='2020-01-01').sort_index(ascending=True) # sort_index按照时间进行排序
df.low.plot()