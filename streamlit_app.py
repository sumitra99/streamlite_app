import streamlit
#streamlit.title('conversation')
#streamlit.text('how r u ?')
#streamlit.text('had ur breakfast')
#streamlit.text('yeah, soup 🥣')

with streamlit.form(key="form1")
name=streamlit.text_input(label= "enter name")

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt") 
fruits_selected=streamlit.multiselect("pick some fruits:",list(my_fruit_list.index))#,['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


fruit_choice=streamlit.text_input('what fruit would you like information about?','kiwi')
streamlit.write('the user entered',fruit_choice)

import requests
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#streamlit.text(fruityvice_response.json())
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)




