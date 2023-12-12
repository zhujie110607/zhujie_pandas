# -*- 保税好件-原件更换 -*-
import pandas as pd
import datetime
from pyFile import common
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
import webbrowser
import os

pd.set_option('display.max_colwidth', None)
ddf = pd.DataFrame()


def BaseExcels() -> list:  # 读取基础数据表
    excelpath = common.select_excel_file('请选择基础数据表')
    # 如果文件路径为空，则退出程序
    dfList = []
    if excelpath is None:
        return dfList

    # 基础数据-子库对应表
    columns_Old0 = [x.strip() for x in ddf[ddf['ID'] == 0]['源字段名'].to_string(index=False).split(',')]
    dfList.append(pd.read_excel(excelpath, sheet_name=ddf[ddf['ID'] == 0]['源表名'].to_string(index=False),usecols=columns_Old0))
    dfList[0]=dfList[0].loc[:,columns_Old0]
    dfList[0].rename(columns=dict(zip(dfList[0].columns, ['iCare子库', 'ERP子库', 'ERP货位', '组织', '整改/维护'])), inplace=True)

    # 基础数据-原件维修
    columns_Old1 = [x.strip() for x in ddf[ddf['ID'] == 1]['源字段名'].to_string(index=False).split(',')]
    dfList.append(pd.read_excel(excelpath, sheet_name=ddf[ddf['ID'] == 1]['源表名'].to_string(index=False),usecols=columns_Old1))
    dfList[1] = dfList[1].loc[:, columns_Old1]
    dfList[1].rename(columns=dict(zip(dfList[1].columns, ['组织', '转入ERP子库', '转入ERP货位'])), inplace=True)

    # 基础数据-原件整改
    columns_Old2 = [x.strip() for x in ddf[ddf['ID'] == 2]['源字段名'].to_string(index=False).split(',')]
    dfList.append(pd.read_excel(excelpath, sheet_name=ddf[ddf['ID'] == 2]['源表名'].to_string(index=False),usecols=columns_Old2))
    dfList[2] = dfList[2].loc[:, columns_Old2]
    dfList[2].rename(columns=dict(zip(dfList[2].columns, ['组织', '转入ERP子库', '转入ERP货位'])), inplace=True)
    return dfList


def WriteExcels():
    global ddf
    ddf = common.json_text
    excelpath = common.select_excel_file('请选择原件更换数据源表')
    # 如果文件路径为空，则退出程序
    if excelpath is None:
        return
    try:
        columns_Old3 = [x.strip() for x in ddf[ddf['ID'] == 3]['源字段名'].to_string(index=False).split(',')]
        df = pd.read_excel(excelpath, sheet_name=ddf[ddf['ID'] == 3]['源表名'].to_string(index=False),usecols=columns_Old3)
        df = df.loc[:, columns_Old3]
        df.rename(columns=dict(zip(df.columns, ['物料编码', 'SN', '交易数量', '子库组代码', '需求单号', '派单号', '备注'])), inplace=True)

        dfList = BaseExcels()
        dfs = pd.merge(left=df, right=dfList[0], left_on='子库组代码', right_on='iCare子库', how='left')
        dfs1 = dfs.loc[dfs['整改/维护'].astype(str).str.contains('整改') == 0]  # 不包含整改的数据
        dfs2 = dfs.loc[dfs['整改/维护'].astype(str).str.contains('整改') > 0]  # 包含整改的数据

        dfs3 = dfs1.merge(dfList[1], on='组织', how='left')  # 不包含整改的数据去原件维修里面匹配
        dfs4 = dfs2.merge(dfList[2], on='组织', how='left')  # 包含整改的数据去原件整改里面匹配
        dfs5 = pd.concat([dfs3, dfs4])
        df_table = pd.pivot_table(dfs5, index=['组织', '物料编码', 'ERP子库', 'ERP货位', '转入ERP子库', '转入ERP货位',
                                               '需求单号'], values='交易数量', aggfunc="sum")
        df_table.reset_index(inplace=True)

        # 写入excel表格
        writes = pd.ExcelWriter(os.path.join(common.save_path[0], "原件更换.xlsx"))
        df_table.to_excel(writes, sheet_name='原件更换', index=False)
        writes.close()

        # 写入html表格并打开
        table = Table()
        table.add(df_table.columns.tolist(), df_table.values.tolist())

        table.set_global_opts(
            title_opts=ComponentTitleOpts(title="原件更换",
                                          subtitle=(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        )
        table.render(os.path.join(common.save_path[1], "原件更换.html"))
        webbrowser.open(os.path.join(common.save_path[1], "原件更换.html"))
        # common.show_message("结果文件已保存到\n{}\\保税好件".format(common.base_path), 1)
    except  Exception as e:
        common.show_message(e, 0)
