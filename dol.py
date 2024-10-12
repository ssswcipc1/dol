from nicegui import ui,app,Client
import datetime
import requests
import re
import pymysql
import asyncio
import plotly.graph_objects as go
from flask import Flask, request
from django.http import HttpRequest
from fastapi import FastAPI, Request,WebSocket

@ui.page("/")
async def Mian(client: Client):
  
    
    print(client)
    szd=""
    cl=client
    
    def chaxun():
        handle_connection(cl)      
        
        conn = pymysql.connect(host="sql.wsfdb.cn", port=3306, user='ssswcip20240930', passwd='123123Aa', db='ssswcip20240930', charset='utf8mb4')    
        # 使用cursor()方法获取操作游标 
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        # 1. 执行SQL,返回受影响的行数
        chanpin=i.value
     
        print(chanpin)   
        effect_row1 = cursor.execute("SHOW TABLES like '%hangqing%'")
        result = cursor.fetchall()
        print(result)
        print (type(result) )        
        biao=result[-1]
        print(biao)
        print (type(biao) )
        biao=list(biao.values())[-1]  
        print(biao)
        print (type(biao) )
        if chanpin=="":
            effect_row1 = cursor.execute(f'select  * from   `{biao}` order by jiage  desc;;')
            print(f'select  * from   `{biao}` ;')
            myclick(szd+'     正在查询         所有产品')
        else:
            chanpin='%'+chanpin+"%"     
            effect_row1 = cursor.execute(f'select  * from   `{biao}` where `name` like \'{chanpin}\' order by jiage  desc; ')
            print(f'select  * from   `{biao}` where `name` like \'{chanpin}\'  ')        
            myclick(szd+'     正在查询       '+chanpin)   

        # 2. 执行SQL,返回受影响的行数,一次插入多行数据
        #effect_row2 = cursor.executemany("insert into USER (NAME) values(%s)", [("jack"), ("boom"), ("lucy")])  # 3
        # 查询所有数据,返回数据为元组格式
        result = cursor.fetchall()
        #my_dict = {"name": "Alice", "age": 25, "gender": "female"}
        #my_dict["new_name"] = my_dict.pop("name")
        # 创建新的键值对          
        # new_dict=[]    
        # new_dict= newdict(result,new_dict,'name','分类')
        # new_dict= newdict(result,new_dict,'shangpin','商品名')
        # new_dict= newdict(result,new_dict,'chengshi','地名')
        # new_dict= newdict(result,new_dict,'jiage','价格')
        # new_dict= newdict(result,new_dict,'qushi','趋势')
        # new_dict= newdict(result,new_dict,'date','时间')
        # print(new_dict)    
        print(result)
        # result["分类"] = result.pop('name')
        # result["商品名"] = result.pop('shangpin')
        # result["地名"] = result.pop('chengshi')
        # result["价格"] = result.pop('jiage')
        # result["趋势"] = result.pop('qushi')
        # result["时间"] = result.pop('date')
        # 增/删/改均需要进行commit提交,进行保存
        conn.commit()
        aggrid.clear()
        rows.clear()
        # 关闭游标
        cursor.close()
        for key in result:            
            key["分类"] = key.pop('name')
            key["商品名"] = key.pop('shangpin')
            key["城市"] = key.pop('chengshi')
            key["价格"] = key.pop('jiage')
            key["趋势"] = key.pop('qushi')
            key["时间"] = key.pop('date')
            rows.append(key)   
        #aggrid.options['columnDefs']=[{'field':'id'},{'field':'商品名'},{'field':'城市'},{'field':'价格'},{'field':'趋势'},{'field':'时间'}]
        aggrid.update()
        # 关闭连接
        conn.close()
    def chaxunsp():
    # 打开数据库连接
        handle_connection(ui.context.client)    
        conn = pymysql.connect(host="sql.wsfdb.cn", port=3306, user='ssswcip20240930', passwd='123123Aa', db='ssswcip20240930', charset='utf8mb4')
        # 使用cursor()方法获取操作游标 
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        # 1. 执行SQL,返回受影响的行数
        chanpin=i1.value
        i1.value=''
        print(chanpin)    
        if chanpin=="":
            effect_row1 = cursor.execute('select  * from  `svsangguan`  ;')        
            myclick(szd+'     正在查询所有商铺       ')  
        else:
            chanpin='%'+chanpin+"%"     
            ml=f"select  * from   `svsangguan` where `text` like '{chanpin}' ;"
            print(ml)
            effect_row1 = cursor.execute(ml)              
            myclick(szd+'     正在查询商铺       '+chanpin)
        # 2. 执行SQL,返回受影响的行数,一次插入多行数据
        #effect_row2 = cursor.executemany("insert into USER (NAME) values(%s)", [("jack"), ("boom"), ("lucy")])  # 3
        # 查询所有数据,返回数据为元组格式
        result = cursor.fetchall()
        #my_dict = {"name": "Alice", "age": 25, "gender": "female"}
        #my_dict["new_name"] = my_dict.pop("name")
        # 创建新的键值对          
        # new_dict=[]    
        # new_dict= newdict(result,new_dict,'name','分类')
        # new_dict= newdict(result,new_dict,'shangpin','商品名')
        # new_dict= newdict(result,new_dict,'chengshi','地名')
        # new_dict= newdict(result,new_dict,'jiage','价格')
        # new_dict= newdict(result,new_dict,'qushi','趋势')
        # new_dict= newdict(result,new_dict,'date','时间')
        # print(new_dict)    
        print(result)
        # result["分类"] = result.pop('name')
        # result["商品名"] = result.pop('shangpin')
        # result["地名"] = result.pop('chengshi')
        # result["价格"] = result.pop('jiage')
        # result["趋势"] = result.pop('qushi')
        # result["时间"] = result.pop('date')
        # 增/删/改均需要进行commit提交,进行保存
        conn.commit()
        aggrid1.clear()
        rows1.clear()
        # 关闭游标
        cursor.close()
        for key in result:            
            key["商铺名"] = key.pop('name')
            key["商品名"] = key.pop('text')
            key["价格"] = key.pop('date')
            rows1.append(key)   
        #aggrid.options['columnDefs']=[{'field':'id'},{'field':'商品名'},{'field':'城市'},{'field':'价格'},{'field':'趋势'},{'field':'时间'}]
        aggrid1.update()
        # 关闭连接
        conn.close()
    def chaxundt():
    # 打开数据库连接
        handle_connection(ui.context.client)    
        conn = pymysql.connect(host="sql.wsfdb.cn", port=3306, user='ssswcip20240930', passwd='123123Aa', db='ssswcip20240930', charset='utf8mb4')
        # 使用cursor()方法获取操作游标 
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        # 1. 执行SQL,返回受影响的行数
        chanpin=i1.value  
     
        print(chanpin)    
        if chanpin=="":
            effect_row1 = cursor.execute('select  * from  `svbaitan` ;')        
            myclick(szd+'     正在查询所有地毯       ')  
        else:
            chanpin='%'+chanpin+"%"     
            ml=f"select  * from   `svbaitan` where `text` like '{chanpin}' ;"
            print(ml)
            effect_row1 = cursor.execute(ml)       
            myclick(szd+'     正在查询地毯       '+chanpin)
        # 2. 执行SQL,返回受影响的行数,一次插入多行数据
        #effect_row2 = cursor.executemany("insert into USER (NAME) values(%s)", [("jack"), ("boom"), ("lucy")])  # 3
        # 查询所有数据,返回数据为元组格式
        result = cursor.fetchall()
        #my_dict = {"name": "Alice", "age": 25, "gender": "female"}
        #my_dict["new_name"] = my_dict.pop("name")
        # 创建新的键值对           
        # new_dict=[]    
        # new_dict= newdict(result,new_dict,'name','分类')
        # new_dict= newdict(result,new_dict,'shangpin','商品名')
        # new_dict= newdict(result,new_dict,'chengshi','地名')
        # new_dict= newdict(result,new_dict,'jiage','价格')
        # new_dict= newdict(result,new_dict,'qushi','趋势')
        # new_dict= newdict(result,new_dict,'date','时间')
        # print(new_dict)    
        print(result)
        # result["分类"] = result.pop('name')
        # result["商品名"] = result.pop('shangpin')
        # result["地名"] = result.pop('chengshi')
        # result["价格"] = result.pop('jiage')
        # result["趋势"] = result.pop('qushi')
        # result["时间"] = result.pop('date')
        # 增/删/改均需要进行commit提交,进行保存
        conn.commit()
        aggrid1.clear()
        rows1.clear()
        # 关闭游标
        cursor.close()
        for key in result:            
            key["商铺名"] = key.pop('name')
            key["商品名"] = key.pop('text')
            key["价格"] = key.pop('date')
            rows1.append(key)   
        #aggrid.options['columnDefs']=[{'field':'id'},{'field':'商品名'},{'field':'城市'},{'field':'价格'},{'field':'趋势'},{'field':'时间'}]
        aggrid1.update()
        # 关闭连接
        conn.close()
    def chaxunlt():
    # 打开数据库连接
        handle_connection(ui.context.client)    
        conn = pymysql.connect(host="sql.wsfdb.cn", port=3306, user='ssswcip20240930', passwd='123123Aa', db='ssswcip20240930', charset='utf8mb4')
        # 使用cursor()方法获取操作游标 
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        # 1. 执行SQL,返回受影响的行数
        chanpin=i1.value  
       
        print(chanpin)      
        effect_row1 = cursor.execute("SHOW TABLES like '%liaotian%'")
        result = cursor.fetchall()
        print(result)
        print (type(result) )           
        biao=result[-1]
        print(biao)
        print (type(biao) )
        biao=list(biao.values())[-1]
        if chanpin=="":
            effect_row1 = cursor.execute(f'select  * from  `{biao}` order by date desc ;')        
            myclick(szd+'     正在查询所有聊天记录       ')  
        else:
            chanpin='%'+chanpin+"%"     
            ml=f"select  * from   `{biao}` where `text` like '{chanpin}'  or `name` like '{chanpin}' order by date desc ;"
            print(ml)
            effect_row1 = cursor.execute(ml)      
            myclick(szd+'     正在查询聊天记录      '+chanpin)
        # 2. 执行SQL,返回受影响的行数,一次插入多行数据
        #effect_row2 = cursor.executemany("insert into USER (NAME) values(%s)", [("jack"), ("boom"), ("lucy")])  # 3
        # 查询所有数据,返回数据为元组格式
        result = cursor.fetchall()
        #my_dict = {"name": "Alice", "age": 25, "gender": "female"}
        #my_dict["new_name"] = my_dict.pop("name")
        # 创建新的键值对            
        #   # new_dict=[]    
        # new_dict= newdict(result,new_dict,'name','分类')
        # new_dict= newdict(result,new_dict,'shangpin','商品名')
        # new_dict= newdict(result,new_dict,'chengshi','地名')
        # new_dict= newdict(result,new_dict,'jiage','价格')
        # new_dict= newdict(result,new_dict,'qushi','趋势')
        # new_dict= newdict(result,new_dict,'date','时间')
        # print(new_dict)    
        print(result)
        # result["分类"] = result.pop('name')
        # result["商品名"] = result.pop('shangpin')
        # result["地名"] = result.pop('chengshi')
        # result["价格"] = result.pop('jiage')
        # result["趋势"] = result.pop('qushi')
        # result["时间"] = result.pop('date')
        # 增/删/改均需要进行commit提交,进行保存
        conn.commit()
        aggrid1.clear()
        rows1.clear()
        # 关闭游标
        cursor.close()
        for key in result:            
            key["商铺名"] = key.pop('name')
            key["商品名"] = key.pop('text')
            key["价格"] = key.pop('date')
            rows1.append(key)   
        #aggrid.options['columnDefs']=[{'field':'id'},{'field':'商品名'},{'field':'城市'},{'field':'价格'},{'field':'趋势'},{'field':'时间'}]
        aggrid1.update()
        # 关闭连接
        conn.close()
    def   chaxunltwj():
    # 打开数据库连接
        handle_connection(ui.context.client)    
        conn = pymysql.connect(host="sql.wsfdb.cn", port=3306, user='ssswcip20240930', passwd='123123Aa', db='ssswcip20240930', charset='utf8mb4')
        # 使用cursor()方法获取操作游标 
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        # 1. 执行SQL,返回受影响的行数
        chanpin=i1.value  
       
        print(chanpin)      
        effect_row1 = cursor.execute("SHOW TABLES like '%liaotian%'")
        result = cursor.fetchall()
        print(result)
        print (type(result) )        
        biao=result[-1]
        print(biao)
        print (type(biao) )


        biao=list(biao.values())[-1]        
        chanpin='%'+chanpin+"%"     
        ml=""
        y1=[]
        for person in reversed(result):    
            #在每个遍历的字典里再进行嵌套（内层循环）
            for k,v in person.items() :
                if ml=="":
                    ml =f'select  * from   `{v}` where `text` like \'{chanpin}\' or name like \'{chanpin}\'   ' 

                else:
                    ml +=f'union all select  * from   `{v}` where `text` like \'{chanpin}\' or name like \'{chanpin}\'     '         
                      
        print(ml)
        
        effect_row1 = cursor.execute(ml)
        
        # 2. 执行SQL,返回受影响的行数,一次插入多行数据
        #effect_row2 = cursor.executemany("insert into USER (NAME) values(%s)", [("jack"), ("boom"), ("lucy")])  # 3
        # 查询所有数据,返回数据为元组格式
        result = cursor.fetchall()
        #my_dict = {"name": "Alice", "age": 25, "gender": "female"}
        #my_dict["new_name"] = my_dict.pop("name")
        # 创建新的键值对            
        #   # new_dict=[]    
        # new_dict= newdict(result,new_dict,'name','分类')
        # new_dict= newdict(result,new_dict,'shangpin','商品名')
        # new_dict= newdict(result,new_dict,'chengshi','地名')
        # new_dict= newdict(result,new_dict,'jiage','价格')
        # new_dict= newdict(result,new_dict,'qushi','趋势')
        # new_dict= newdict(result,new_dict,'date','时间')
        # print(new_dict)    
        print(result)
        # result["分类"] = result.pop('name')
        # result["商品名"] = result.pop('shangpin')
        # result["地名"] = result.pop('chengshi')
        # result["价格"] = result.pop('jiage')
        # result["趋势"] = result.pop('qushi')
        # result["时间"] = result.pop('date')
        # 增/删/改均需要进行commit提交,进行保存
        conn.commit()
        aggrid1.clear()
        rows1.clear()
        # 关闭游标
        cursor.close()
        for key in result:            
            key["商铺名"] = key.pop('name')
            key["商品名"] = key.pop('text')
            key["价格"] = key.pop('date')
            rows1.append(key)   
        #aggrid.options['columnDefs']=[{'field':'id'},{'field':'商品名'},{'field':'城市'},{'field':'价格'},{'field':'趋势'},{'field':'时间'}]
        aggrid1.update()
        # 关闭连接
        conn.close()
    
    
    def add_trace(e):
        conn = pymysql.connect(host="sql.wsfdb.cn", port=3306, user='ssswcip20240930', passwd='123123Aa', db='ssswcip20240930', charset='utf8mb4')   
        # 使用cursor()方法获取操作游标 
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        # 1. 执行SQL,返回受影响的行数  
        effect_row1 = cursor.execute("SHOW TABLES like '%hangqing%'")
        result = cursor.fetchall()
        row =  e.args['data']
        print(result)
        print (type(result) )
        name=row['分类']
        ml=""
        y1=[]
        for person in result:    
            #在每个遍历的字典里再进行嵌套（内层循环）
            for k,v in person.items():             
                if ml=="":
                    ml =f'select  * from   `{v}` where `name` like \'{name}\' '  
                else:
                    ml +=f'union all select  * from   `{v}` where `name` like \'{name}\' '                  
        print(ml)
        effect_row1 = cursor.execute(ml)
        biao=result[-1]
        biao=list(biao.values())[-1]
        # 2. 执行SQL,返回受影响的行数,一次插入多行数据
        #effect_row2 = cursor.executemany("insert into USER (NAME) values(%s)", [("jack"), ("boom"), ("lucy")])  # 3
        # 查询所有数据,返回数据为元组格式
        result = cursor.fetchall()
        #my_dict = {"name": "Alice", "age": 25, "gender": "female"}
        #my_dict["new_name"] = my_dict.pop("name")
        # 创建新的键值对          
        # new_dict=[]    
        # new_dict= newdict(result,new_dict,'name','分类')
        # new_dict= newdict(result,new_dict,'shangpin','商品名')
        # new_dict= newdict(result,new_dict,'chengshi','地名')
        # new_dict= newdict(result,new_dict,'jiage','价格')
        # new_dict= newdict(result,new_dict,'qushi','趋势')
        # new_dict= newdict(result,new_dict,'date','时间')
        # print(new_dict)    
        print(result)
        # result["分类"] = result.pop('name')
        # result["商品名"] = result.pop('shangpin')
        # result["地名"] = result.pop('chengshi')
        # result["价格"] = result.pop('jiage')
        # result["趋势"] = result.pop('qushi')
        # result["时间"] = result.pop('date')
        # 增/删/改均需要进行commit提交,进行保存
        conn.commit()    
        # 关闭游标
        cursor.close()   
        # 关闭连接
        conn.close()
        x1=[]
        y1=[]
        for person in result:   
            print(f"{person['jiage']}'s age is {person['date']}")    
            y1.append(person['jiage'])     
            x1.append(person['date'])      
        #plot.update_figure()
        plot.clear()
        fig.data[0].x=x1
        fig.data[0].y=y1
        #fig.add_trace( go.Scatter(x=x1, y=y1))
        print(fig)
        #fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    # fig.add_trace(go.Scatter(x=x1, y=y1))
        #print(fig)
        plot.update()
    def hubi():
        i.value="湖笔"   
        chaxun()
    def gumo():
        i.value="古墨"   
        chaxun()
    def tideng():
        i.value="灯笼"   
        chaxun()
    def xiazhi():
        i.value="狭织"   
        chaxun()
    def qinghua():
        i.value="青花粗瓷"   
        chaxun()
    def quanbu():
        i.value=""   
        chaxun()
   
    def handle_connection(client):
        
        dt = client.environ           
        print(dt)   
        rule = r"b'fly-client-ip', b'(.*?)'"
        result = re.findall(rule,str(dt))
        chanpin=i.value      
     
        if len(result)>0:
            ip=result[0]      
            # 使用ipinfo.io的API
            url = f'https://whois.pconline.com.cn/ipJson.jsp?ip={ip}&json=true'        
            # 发送HTTP请求
            response = requests.get(url)        
            # 确保请求成功
            if response.status_code == 200:
                location = response.json()
                print(location)
                # 打印特定的位置信息
                print("城市:", location['addr'])    
                
                szd=location['addr'] 
            else:
                print("查询位置失败，状态码:", response.status_code)   
    #app.on_connect(handle_connection)
    columns=[{'checkboxSelection': True},{'field':'商品名'},{'field':'城市'},{'field':'价格'},{'field':'趋势'},{'field':'时间'}]
    columns1=[{'checkboxSelection': True},{'field':'商铺名'},{'field':'商品名'},{'field':'价格'}]
    #columns=[{'field':'id'},{'field':'shangpin'},{'field':'chengshi'},{'field':'jiage'},{'field':'qushi'},{'field':'date'}]   
    rows =[]
    rows1 =[]
    ui.query('body').style('background-image:url("https://imgsa.baidu.com/forum/pic/item/f68344086e061d95dbbeeb747bf40ad163d9ca01.jpg"); background-size: cover;  position: absolute;   top: 0;left: 0;  content: "";  z-index: -1;   -webkit-filter: opacity(90%);   filter: opacity(90%);')
    #ui.image('background.jpg').props("absolute-top text-center").tailwind('h-screen')
    #ui.button('Delete selected', on_click=delete_selected)
    aggrid = ui.aggrid({
        'columnDefs': columns, 'rowData': rows, 'rowSelection': 'multiple',
    }).on('cellDoubleClicked', add_trace).classes('max-w-100')#on('cellValueChanged', handle_cell_value_change).
    with ui.row():
        i = ui.input(placeholder='输入需要搜索的产品').props('dark dense standout input-class="font-mono" color="lime-11" bg-color="green" ')
        ui.button('查询指定产品或地名', on_click=chaxun)
        ui.button('狭织查询', on_click=xiazhi)
        ui.button('湖笔查询', on_click=hubi)
        ui.button('青花查询', on_click=qinghua)
        #ui.button('古墨查询', on_click=gumo)
        ui.button('提灯查询', on_click=tideng)
        ui.button('查询全部', on_click=quanbu)
        #a= ui.button('测试', on_click=index)
        #ui.label().bind_text_from(i, 'value')      
    aggrid1 = ui.aggrid({ 'columnDefs': columns1, 'rowData': rows1, 'rowSelection': 'multiple','suppressSizeToFit': True },auto_size_columns=True).on('cellDoubleClicked', add_trace).classes('max-w-100')#on('cellValueChanged', handle_cell_value_change).
        #ui.button('Delete selected', on_click=delete_selected)    
    with ui.row():
        i1 = ui.input(placeholder='输入需要搜索的产品').props('dark dense standout input-class="font-mono" color="lime-11" bg-color="green" ')
        ui.button('查询赛维商铺', on_click=chaxunsp)
        ui.button('查询赛维地毯', on_click=chaxundt)
        ui.button('查询聊天记录', on_click=chaxunlt)
        ui.button('查询近几天聊天记录', on_click=chaxunltwj)

    fig = go.Figure(go.Scatter(x=[0], y=[0]))
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
    plot = ui.plotly(fig).classes('w-full h-40')
    #启动界面        
    mylog = ui.log(max_lines=1000).classes('w-full h-30')
    label = ui.label()

    def myclick(text):           
        mylog.push(f'{datetime.datetime.now().strftime("%H:%M:%S")}  '+text)    
            # 最多显示15行，超过15行的会自动清除          

        


#ui.run(port=8080, reconnect_timeout=60, native=True)
ui.run(title='大航海时代OL国际服',port=8080, reconnect_timeout=60,on_air='RfEm7vbfAv15JLQG',)
#定时任务

