import numpy as np
import pandas as pd

indexdatas = pd.date_range("20191127", periods=6)
data = pd.DataFrame(np.arange(24).reshape((6, 4)), index=indexdatas, columns=['A', 'B', 'C', 'D'])
print(data)
"""
             A   B   C   D
2019-11-27   0   1   2   3
2019-11-28   4   5   6   7
2019-11-29   8   9  10  11
2019-11-30  12  13  14  15
2019-12-01  16  17  18  19
2019-12-02  20  21  22  23
"""
print(data[0:3])  # 输出0列-第2列的数据(从0开始计数) 等于print(data[20191127:20191130]) 行索引只能切片不能指定某一行
                  # 后者包含两端，而前者切片操作只包含前界不包含后界
print(data.loc["20191129"])  # 输出某一行的数据不能直接用【】而是loc 注意引号
"""  输出时安装Series的形式输出
A     8
B     9
C    10
D    11
Name: 2019-11-29 00:00:00, dtype: int32
"""

print(data.loc[:, ['A', 'B']])  # loc就是下标的意思， ：表示所有行或者是所有列
"""
             A   B
2019-11-27   0   1
2019-11-28   4   5
2019-11-29   8   9
2019-11-30  12  13
2019-12-01  16  17
2019-12-02  20  21
"""

print(data.loc['20191130', ['A', 'B']])
"""     若行只有一行，则会输出Series 并在下面标注行名
A    12
B    13
Name: 2019-11-30 00:00:00, dtype: int32
"""
print(data.iloc[3:5, [1, 3]])  # iloc可以使得像二维数组那样访问表格/ 行列下标都是从0开始数 2*2=4个元素
print(data.ix[:3, ['A', 'C']])  # loc只能用行列名访问/iloc只能用数组下标访问/ix可以混合两种
print(data[data.A > 8])  # 可在索引中对某一列的所有元素做判断 输出满足条件的整行数据
"""
             A   B   C   D
2019-11-30  12  13  14  15
2019-12-01  16  17  18  19
2019-12-02  20  21  22  23
"""