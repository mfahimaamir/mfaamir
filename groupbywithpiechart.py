import numpy
import streamlit as st
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
from st_aggrid.shared import ColumnsAutoSizeMode
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')       #서버에서, 화면에 표시하기 위해서 필요
import seaborn as sns
import altair as alt               ##https://altair-viz.github.io/
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

labels2 = ['Frogs', 'Hogs', 'Dogs', 'Logs']
sizes2 = [15, 30, 45, 10]
#st.write(labels2)
#st.write(sizes2)
#def display_grid(df: pd.DataFrame):    
data = {
    'Region': ['North America', 'North America', 'North America', 'Europe', 'Europe', 'Asia', 'Asia'],
    'Country': ['USA', 'USA', 'Canada', 'Germany', 'France', 'Japan', 'China'],
    'City': ['New York', 'Los Angeles', 'Toronto', 'Berlin', 'Paris', 'Tokyo', 'Beijing'],
    'iTEM': ['TV', 'CAL', 'BUS', 'TRAIN', 'TANK', 'TABLE', 'DESK'],
    'Person': ['gggTV', 'dddCAL', 'ffffBUS', 'ssssTRAIN', 'ffffTANK', 'ssssTABLE', 'dddDESK'],
    'Sale': [76445, 45555, 73356, 54467, 65758, 544456, 75556],
     'Comm': [1726, 1425, 1725, 1527, 1628, 1426, 1276],
     'Qty': [765, 455, 756, 567, 678, 456, 756]
    
    }

df = pd.DataFrame(data)


gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_selection(
        selection_mode="multiple",
        #use_checkbox=True,
        pre_selected_rows=None,  # <-- Set to manually persist checkbox state
    )


        # Configure column filters for all columns
for column in df.columns:
        gb.configure_column(column, filter=True)

#gb.configure_grid_options(pivotMode= True)

gridOptions = gb.build()
mfa = AgGrid(
        df,
        gridOptions=gridOptions,
        update_mode=GridUpdateMode.GRID_CHANGED,
        columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
        data_return_mode=DataReturnMode.FILTERED   # <-- Gets filtered data, but not filters applied to columns
    )

if st.button('Check availability'):
    mfa4 =mfa['data']
    fild = pd.DataFrame(mfa['columns_state'])
    above_35= fild["hide"] 
    above_36= fild["colId"] 
    list_from_df = above_36.values.tolist()
    list_from_column = fild["colId"].tolist()
    fild["hide"] = fild["hide"].astype(int) 
    fild = fild[fild["hide"]==0 ]
    list_from_df2 = fild["colId"].values.tolist()
    mfa5 = mfa4[list_from_column]
    mfa6 = mfa4[list_from_df2]
    colt = int(len(mfa6.columns)) 
    #df12 = df.groupby('Region')['Sale'].sum().reset_index()
    df12 = df.groupby(mfa6.columns[0])[mfa6.columns[colt-1]].sum().reset_index()
    st.write(df12)
    df12["expl"] = 0.1
    
    #s = df.groupby('text').agg({'word': list, 'num': 'count'}).reset_index()
   ## item= mfa6.iloc[:,[0]].values.tolist()
    
    colt2 = int(len(mfa6.columns))
    st.write(colt2)
    #item= mfa6.iloc[:,[0]].values.tolist()
    item = df12.columns[0]
    itemvalue  = df12[item].values.tolist()
    last2 = df12.columns[1]
    cost  = df12[last2].values.tolist()
    last1 = df12.columns[2]
    expl  = df12[last1].values.tolist()

    #cost= df.iloc[:,[colt-2]].values.tolist()
    #expl= df.iloc[:,[colt-1]].values.tolist()
    
    #st.write(mfa6)
    #st.write(colt)
    #st.write(item)
    #st.write(cost)
    #st.write(expl)








    fig1, ax1 = plt.subplots()
    ax1.pie(cost, explode=expl, labels=itemvalue, autopct='%1.1f%%',        shadow=True, startangle=90)
    #ax1.pie(sizes, explode=explode, labels=item, autopct='%1.1f%%',        shadow=True, startangle=90)
    #ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)

    
    fig1 = px.pie(df12, values=last2, names=item, title='Pie Chart of Languages')      #plotly pie차트
    st.plotly_chart(fig1)

    fig2 = px.bar( df12, x=item, y=last2)        #plotly bar차트
    st.plotly_chart(fig2)
    
    counts = pd.Series(cost, 
                   index=itemvalue)
    colors = ['#191970', '#001CF0', '#0038E2', '#0055D4', '#0071C6', '#008DB8', '#00AAAA',
          '#00C69C', '#00E28E', '#00FF80', ]
    explode = expl

    counts.plot(kind='pie', fontsize=17, colors=colors, explode=explode)
 #   plt.axis('equal')
    plt.ylabel('Muhammad is the best')
    #plt.legend(labels=itemvalue, loc="best")
    #plt.show()
    st.pyplot(plt)    
#counts.index
    
    #cost  = df['cost'].values.tolist()
    #expl  = df['expl'].values.tolist()
#listxx= mfa6.iloc[:,[colt-1]].values.tolist()


    #listyy= mfa6.iloc[:,[0]].values.tolist()
    #listyy= mfa6.iloc[:,[0]].T.values.tolist()
    
    #Third_Column=DF.iloc[:,2]
    #colname = df.columns[2]
    #listyy0= (df.to_string(index=False))
 #   listyy=listyy0.values.tolist()
 #   colt = int(len(mfa6.columns))
    #listxx= mfa6.iloc[:,[colt-1]].values.tolist()
#    listxx= mfa6.iloc[:,[colt-1]].astype('int').T.values.tolist()
    
    
    #test.to_numpy('int').tolist()
    #test.T.values.tolist()
  #  st.write(listyy)
    

    
#    plt.barh(itemvalue,cost)
    #plt.show()
    
    #plt.bar(cost,itemvalue , color='skyblue')
 #   plt.xlabel('Visualization Library')
  #  plt.ylabel('Number of Enthusiasts')
   # plt.title('Which Visualization Library Do People Prefer?')
    #plt.show()
    #st.pyplot(plt)
    
    