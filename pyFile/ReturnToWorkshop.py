# -*- 保税好件-车间返仓 -*-

import pandas as pd
import datetime
from pyFile import common
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
import webbrowser
import os
from pyecharts.charts import Page

pd.set_option('display.max_colwidth', None)
ddf = pd.DataFrame()


def WriteExcels():
    global ddf
    ddf = common.json_text
    excelpath = common.select_excel_file('请选择车间返仓数据源表')
    # 如果文件路径为空，则退出程序
    if excelpath is None:
        return

    try:
        columns_Old5 = [x.strip() for x in ddf[ddf['ID'] == 5]['源字段名'].to_string(index=False).split(',')]
        df = pd.read_excel(excelpath, sheet_name=ddf[ddf['ID'] == 5]['源表名'].to_string(index=False),usecols=columns_Old5)
        df=df.loc[:,columns_Old5]
        df.rename(columns=dict(zip(df.columns,['销售编码', '条码', '数量', '打折', '转入ICARE子库', '转出ERP子库', '转出ERP货位', '转入ERP子库', '转入ERP货位', '子库组织', 'Icare接收子库', '入库类型'])), inplace=True)

        # 筛选“打折”为非空白值的，只要“销售编码”“Icare接收子库”“转入ICARE子库”“条码”“数量”。
        df1 = df[df['打折'].notnull()][['销售编码', 'Icare接收子库', '转入ICARE子库', '条码', '数量']]
        # 筛选“打折”为空白值的，“子库组织”“销售编码”“转出ERP子库”“转出ERP货位”“转入ERP子库”“转入ERP货位”“入库类型”。对“数量”求和汇总。
        df2 = df[df['打折'].isnull()][
            ['子库组织', '销售编码', '转出ERP子库', '转出ERP货位', '转入ERP子库', '转入ERP货位', '入库类型', '数量']]
        df_table = pd.pivot_table(df2,
                                  index=['子库组织', '销售编码', '转出ERP子库', '转出ERP货位', '转入ERP子库',
                                         '转入ERP货位',
                                         '入库类型'],
                                  values='数量', aggfunc="sum")
        df_table.reset_index(inplace=True)

        # 写入excel表格
        writes = pd.ExcelWriter(os.path.join(common.save_path[0], "车间返仓.xlsx"))
        df1.to_excel(writes, sheet_name='打折', index=False)
        df_table.to_excel(writes, sheet_name='不打折', index=False)
        writes.close()

        # 写入html表格并打开
        page = Page(layout=Page.SimplePageLayout)  # 网页中各子图可拖动。默认的SimplePageLayout不可拖动
        table1 = Table()
        table1.add(df1.columns.tolist(), df1.values.tolist())
        table1.set_global_opts(
            title_opts=ComponentTitleOpts(title="车间返仓_打折",
                                          subtitle=(datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S')))

        table2 = Table()
        table2.add(df_table.columns.tolist(), df_table.values.tolist())
        table2.set_global_opts(
            title_opts=ComponentTitleOpts(title="车间返仓_不打折",
                                          subtitle=(datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S')))

        page.add(table1, table2)
        page.render(os.path.join(common.save_path[1], "车间返仓.html"))

        webbrowser.open(os.path.join(common.save_path[1], "车间返仓.html"))
        # common.show_message("结果文件已保存到\n{}\\保税好件".format(common.base_path), 1)
    except  Exception as e:
        common.show_message(e, 0)
