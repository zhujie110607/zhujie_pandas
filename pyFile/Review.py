# -*- 复核 -*-

import pandas as pd
import datetime
from pyFile import common
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
import webbrowser
import os
pd.set_option('display.max_colwidth', None)
ddf = pd.DataFrame()


def WriteExcels():
    global ddf
    ddf = common.json_text
    excelpath = common.select_excel_file('请选择复核数据源表')
    # 如果文件路径为空，则退出程序
    if excelpath is None:
        return
    try:
        # 复核-返仓清单数据
        columns_Old6 = [x.strip() for x in ddf[ddf['ID'] == 6]['源字段名'].to_string(index=False).split(',')]
        df1 = pd.read_excel(excelpath, sheet_name=ddf[ddf['ID'] == 6]['源表名'].to_string(index=False),usecols=columns_Old6)
        df1=df1.loc[:,columns_Old6]
        df1.rename(columns=dict(zip(df1.columns, ['物料编码', '货位', '数量'])), inplace=True)
        df1['物料编码_货位'] = df1['物料编码'].str.cat(df1['货位'], sep=',')

        # 复核-ERP清单数据
        columns_Old7 = [x.strip() for x in ddf[ddf['ID'] == 7]['源字段名'].to_string(index=False).split(',')]
        df2 = pd.read_excel(excelpath, sheet_name=ddf[ddf['ID'] == 7]['源表名'].to_string(index=False),usecols=columns_Old7)
        df2 = df2.loc[:, columns_Old7]
        df2.rename(columns=dict(zip(df2.columns, ['物料编码', '转入ERP货位', '数量'])), inplace=True)
        df2['物料编码_货位'] = df2['物料编码'].str.cat(df2['转入ERP货位'], sep=',')

        s1 = pd.pivot_table(df1, index='物料编码_货位', values='数量', aggfunc="sum")
        s2 = pd.pivot_table(df2, index='物料编码_货位', values='数量', aggfunc="sum")

        s12 = s1.merge(s2, on='物料编码_货位', how='outer', suffixes=('_返仓清单', '_ERP清单'))
        df_table = s12.loc[s12['数量_返仓清单'] != s12['数量_ERP清单']]
        df_table.reset_index(inplace=True)

        # 写入excel表格
        writes = pd.ExcelWriter(os.path.join(common.save_path[0], "复核结果.xlsx"))
        df_table.to_excel(writes, sheet_name='复核结果', index=False)
        writes.close()

        # 写入html表格并打开
        table = Table()
        table.add(df_table.columns.tolist(), df_table.values.tolist())
        table.set_global_opts(
            title_opts=ComponentTitleOpts(title="复核结果",
                                          subtitle=(datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S'))
        )
        table.render(os.path.join(common.save_path[1], "复核结果.html"))
        webbrowser.open(os.path.join(common.save_path[1], "复核结果.html"))
        # common.show_message("结果文件已保存到\n{}\\保税好件".format(common.base_path), 1)
    except  Exception as e:
        common.show_message(e, 0)
