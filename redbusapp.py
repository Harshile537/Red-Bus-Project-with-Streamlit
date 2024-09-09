#  AND Start_time>='{TIME}'
# importing libraries
import pandas as pd
import mysql.connector
import streamlit as slt
from streamlit_option_menu import option_menu
import plotly.express as px
import time

# kerala bus
lists_k=[]
df_k=pd.read_csv("df_k.csv")
for i,r in df_k.iterrows():
    lists_k.append(r["Route_name"])

#Andhra bus
lists_A=[]
df_A=pd.read_csv("df_A.csv")
for i,r in df_A.iterrows():
    lists_A.append(r["Route_name"])

#Telungana bus
lists_T=[]
df_T=pd.read_csv("df_T.csv")
for i,r in df_T.iterrows():
    lists_T.append(r["Route_name"])

# Goa bus
lists_g=[]
df_G=pd.read_csv("df_G.csv")
for i,r in df_G.iterrows():
    lists_g.append(r["Route_name"])

#Rajastan bus
lists_R=[]
df_R=pd.read_csv("df_R.csv")
for i,r in df_R.iterrows():
    lists_R.append(r["Route_name"])


# South bengal bus 
lists_SB=[]
df_SB=pd.read_csv("df_SB.csv")
for i,r in df_SB.iterrows():
    lists_SB.append(r["Route_name"])

# Haryana bus
lists_H=[]
df_H=pd.read_csv("df_H.csv")
for i,r in df_H.iterrows():
    lists_H.append(r["Route_name"])

#Assam bus
lists_AS=[]
df_AS=pd.read_csv("df_AS.csv")
for i,r in df_AS.iterrows():
    lists_AS.append(r["Route_name"])

#UP bus
lists_UP=[]
df_UP=pd.read_csv("df_UP.csv")
for i,r in df_UP.iterrows():
    lists_UP.append(r["Route_name"])

#West bengal bus
lists_WB=[]
df_WB=pd.read_csv("df_WB.csv")
for i,r in df_WB.iterrows():
    lists_WB.append(r["Route_name"])

#setting up streamlit page
slt.set_page_config(layout="wide")

web=option_menu(menu_title="RedBut",
                options=["Home","Find your Bus"],
                icons=["house","info-circle"],
                orientation="horizontal"
                )
# Home page setting
if web=="Home":
    # slt.image("t_500x300.jpg",width=200)
    slt.title("Redbus Data Scraping with Filtering using Streamlit")
    slt.subheader(":blue[Ojective:] ")
    slt.markdown("The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.")
    slt.subheader(":blue[Overview:]") 
    slt.markdown("Selenium: Selenium is a tool used for automating web browsers. It is commonly used for web scraping, which involves extracting data from websites. Selenium allows you to simulate human interactions with a web page, such as clicking buttons, filling out forms, and navigating through pages, to collect the desired data...")
    slt.markdown('''Pandas: Use the powerful Pandas library to transform the dataset from CSV format into a structured dataframe.
                    Pandas helps data manipulation, cleaning, and preprocessing, ensuring that data was ready for analysis.''')
    slt.markdown('''MySQL: With help of SQL to establish a connection to a SQL database, enabling seamless integration of the transformed dataset
                    and the data was efficiently inserted into relevant tables for storage and retrieval.''')
    slt.markdown("Streamlit: Developed an interactive web application using Streamlit, a user-friendly framework for data visualization and analysis.")
    slt.subheader(":blue[Tech Stack:]")
    slt.markdown("Selenium, Python, Pandas, MySQL,mysql-connector-python, Streamlit.")


# States and Routes page setting
if web == "Find your Bus":
    S = slt.selectbox("Lists of States", ["Kerala", "Adhra Pradesh", "Telugana", "Goa", "Rajastan", 
                                          "South Bengal", "Haryana", "Assam", "Uttar Pradesh", "West Bengal"])
    
    slt.subheader(":blue[Filters :]")
    col1,col2,col3=slt.columns(3)
    with col1:
        select_rating = slt.radio("Choose bus ratings", ("Clear ","1","2","3","4","5"))
    with col2:
        select_fare = slt.radio("Choose bus fare range", ("Clear ","50-1000", "1000-2000", "2000 and above"))
    with col3:
        select_seat = slt.radio("Choose seat availity",("Clear ", "1-10","11-20","21-30","31-40","41-50"))
        

    slt.title("Select From and to Place")
    # Kerala bus fare filtering
    if S == "Kerala":
        K = slt.selectbox("List of routes",lists_k)

        def type_and_fare(bus_rating, fare_range, seat):
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="red_bus_details")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            elif fare_range == "2000 and above":
                fare_min, fare_max = 2000, 100000
            else:
                fare_min, fare_max = 50, 100000



            if seat == "1-10":
                s_seat, e_seat = 1, 10
            elif seat == "11-20":
                s_seat, e_seat = 11, 20
            elif seat == "21-30":
                s_seat, e_seat = 21, 30
            elif seat == "31-40":
                s_seat, e_seat = 31, 40
            elif seat == "41-50":
                s_seat, e_seat = 41, 50
            else:
                s_seat, e_seat = 1, 50


            if bus_rating == "1":
                s_r,e_r = 1.0, 1.9
            elif bus_rating == "2":
                s_r,e_r = 2.0, 2.9
            elif bus_rating == "3":
                s_r,e_r = 3.0, 3.9
            elif bus_rating == "4":
                s_r,e_r = 4.0, 4.9
            elif bus_rating == "5":
                s_r,e_r = 5.0, 5.0
            else:
                s_r,e_r = 1, 5
                



            # Define bus type condition
            # if bus_type == "sleeper":
            #     bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            # elif bus_type == "semi-sleeper":
            #     bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            # else:
            #     bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM bus_details_edit
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                 AND Seats_Available BETWEEN {s_seat} AND {e_seat}  AND Ratings BETWEEN {s_r} AND {e_r}
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()
            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_rating, select_fare, select_seat)
        slt.subheader(":blue[Result]")
        slt.dataframe(df_result)

    # Adhra Pradesh bus fare filtering
    if S=="Adhra Pradesh":
        A=slt.selectbox("list of routes",lists_A)

        def type_and_fare_A(bus_rating, fare_range, seat):
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="red_bus_details")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            elif fare_range == "2000 and above":
                fare_min, fare_max = 2000, 100000
            else:
                fare_min, fare_max = 50, 100000



            if seat == "1-10":
                s_seat, e_seat = 1, 10
            elif seat == "11-20":
                s_seat, e_seat = 11, 20
            elif seat == "21-30":
                s_seat, e_seat = 21, 30
            elif seat == "31-40":
                s_seat, e_seat = 31, 40
            elif seat == "41-50":
                s_seat, e_seat = 41, 50
            else:
                s_seat, e_seat = 1, 50


            if bus_rating == "1":
                s_r,e_r = 1.0, 1.9
            elif bus_rating == "2":
                s_r,e_r = 2.0, 2.9
            elif bus_rating == "3":
                s_r,e_r = 3.0, 3.9
            elif bus_rating == "4":
                s_r,e_r = 4.0, 4.9
            elif bus_rating == "5":
                s_r,e_r = 5.0, 5.0
            else:
                s_r,e_r = 1, 5
                
            query = f'''
                SELECT * FROM bus_details_edit
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{A}"
                 AND Seats_Available BETWEEN {s_seat} AND {e_seat}  AND Ratings BETWEEN {s_r} AND {e_r}
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_A(select_rating, select_fare, select_seat)
        slt.dataframe(df_result)
          

    # Telugana bus fare filtering
    if S=="Telugana":
        T=slt.selectbox("list of routes",lists_T)

        def type_and_fare_T(bus_rating, fare_range, seat):
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="red_bus_details")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            elif fare_range == "2000 and above":
                fare_min, fare_max = 2000, 100000
            else:
                fare_min, fare_max = 50, 100000



            if seat == "1-10":
                s_seat, e_seat = 1, 10
            elif seat == "11-20":
                s_seat, e_seat = 11, 20
            elif seat == "21-30":
                s_seat, e_seat = 21, 30
            elif seat == "31-40":
                s_seat, e_seat = 31, 40
            elif seat == "41-50":
                s_seat, e_seat = 41, 50
            else:
                s_seat, e_seat = 1, 50


            if bus_rating == "1":
                s_r,e_r = 1.0, 1.9
            elif bus_rating == "2":
                s_r,e_r = 2.0, 2.9
            elif bus_rating == "3":
                s_r,e_r = 3.0, 3.9
            elif bus_rating == "4":
                s_r,e_r = 4.0, 4.9
            elif bus_rating == "5":
                s_r,e_r = 5.0, 5.0
            else:
                s_r,e_r = 1, 5
            query = f'''
                SELECT * FROM bus_details_edit
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{T}"
                 AND Seats_Available BETWEEN {s_seat} AND {e_seat}  AND Ratings BETWEEN {s_r} AND {e_r}
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_T(select_rating, select_fare, select_seat)
        slt.dataframe(df_result)

    # Goa bus fare filtering
    if S=="Goa":
        G=slt.selectbox("list of routes",lists_g)

        def type_and_fare_G(bus_rating, fare_range, seat):
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="red_bus_details")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            elif fare_range == "2000 and above":
                fare_min, fare_max = 2000, 100000
            else:
                fare_min, fare_max = 50, 100000



            if seat == "1-10":
                s_seat, e_seat = 1, 10
            elif seat == "11-20":
                s_seat, e_seat = 11, 20
            elif seat == "21-30":
                s_seat, e_seat = 21, 30
            elif seat == "31-40":
                s_seat, e_seat = 31, 40
            elif seat == "41-50":
                s_seat, e_seat = 41, 50
            else:
                s_seat, e_seat = 1, 50


            if bus_rating == "1":
                s_r,e_r = 1.0, 1.9
            elif bus_rating == "2":
                s_r,e_r = 2.0, 2.9
            elif bus_rating == "3":
                s_r,e_r = 3.0, 3.9
            elif bus_rating == "4":
                s_r,e_r = 4.0, 4.9
            elif bus_rating == "5":
                s_r,e_r = 5.0, 5.0
            else:
                s_r,e_r = 1, 5
            query = f'''
                SELECT * FROM bus_details_edit
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{G}"
                 AND Seats_Available BETWEEN {s_seat} AND {e_seat}  AND Ratings BETWEEN {s_r} AND {e_r} 
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_G(select_rating, select_fare, select_seat)
        slt.dataframe(df_result)

    # Rajastan bus fare filtering
    if S=="Rajastan":
        R=slt.selectbox("list of routes",lists_R)

        def type_and_fare_R(bus_rating, fare_range, seat):
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="red_bus_details")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            elif fare_range == "2000 and above":
                fare_min, fare_max = 2000, 100000
            else:
                fare_min, fare_max = 50, 100000



            if seat == "1-10":
                s_seat, e_seat = 1, 10
            elif seat == "11-20":
                s_seat, e_seat = 11, 20
            elif seat == "21-30":
                s_seat, e_seat = 21, 30
            elif seat == "31-40":
                s_seat, e_seat = 31, 40
            elif seat == "41-50":
                s_seat, e_seat = 41, 50
            else:
                s_seat, e_seat = 1, 50


            if bus_rating == "1":
                s_r,e_r = 1.0, 1.9
            elif bus_rating == "2":
                s_r,e_r = 2.0, 2.9
            elif bus_rating == "3":
                s_r,e_r = 3.0, 3.9
            elif bus_rating == "4":
                s_r,e_r = 4.0, 4.9
            elif bus_rating == "5":
                s_r,e_r = 5.0, 5.0
            else:
                s_r,e_r = 1, 5
            query = f'''
                SELECT * FROM bus_details_edit
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{R}"
                 AND Seats_Available BETWEEN {s_seat} AND {e_seat}  AND Ratings BETWEEN {s_r} AND {e_r} 
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_R(select_rating, select_fare, select_seat)
        slt.dataframe(df_result)
          

    # South Bengal bus fare filtering       
    if S=="South Bengal":
        SB=slt.selectbox("list of rotes",lists_SB)

        def type_and_fare_SB(bus_rating, fare_range, seat):
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="red_bus_details")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            elif fare_range == "2000 and above":
                fare_min, fare_max = 2000, 100000
            else:
                fare_min, fare_max = 50, 100000



            if seat == "1-10":
                s_seat, e_seat = 1, 10
            elif seat == "11-20":
                s_seat, e_seat = 11, 20
            elif seat == "21-30":
                s_seat, e_seat = 21, 30
            elif seat == "31-40":
                s_seat, e_seat = 31, 40
            elif seat == "41-50":
                s_seat, e_seat = 41, 50
            else:
                s_seat, e_seat = 1, 50


            if bus_rating == "1":
                s_r,e_r = 1.0, 1.9
            elif bus_rating == "2":
                s_r,e_r = 2.0, 2.9
            elif bus_rating == "3":
                s_r,e_r = 3.0, 3.9
            elif bus_rating == "4":
                s_r,e_r = 4.0, 4.9
            elif bus_rating == "5":
                s_r,e_r = 5.0, 5.0
            else:
                s_r,e_r = 1, 5
            query = f'''
                SELECT * FROM bus_details_edit
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{SB}"
                 AND Seats_Available BETWEEN {s_seat} AND {e_seat}  AND Ratings BETWEEN {s_r} AND {e_r} 
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_SB(select_rating, select_fare, select_seat)
        slt.dataframe(df_result)
    
    # Haryana bus fare filtering
    if S=="Haryana":
        H=slt.selectbox("list of rotes",lists_H)

        def type_and_fare_H(bus_rating, fare_range, seat):
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="red_bus_details")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            elif fare_range == "2000 and above":
                fare_min, fare_max = 2000, 100000
            else:
                fare_min, fare_max = 50, 100000



            if seat == "1-10":
                s_seat, e_seat = 1, 10
            elif seat == "11-20":
                s_seat, e_seat = 11, 20
            elif seat == "21-30":
                s_seat, e_seat = 21, 30
            elif seat == "31-40":
                s_seat, e_seat = 31, 40
            elif seat == "41-50":
                s_seat, e_seat = 41, 50
            else:
                s_seat, e_seat = 1, 50


            if bus_rating == "1":
                s_r,e_r = 1.0, 1.9
            elif bus_rating == "2":
                s_r,e_r = 2.0, 2.9
            elif bus_rating == "3":
                s_r,e_r = 3.0, 3.9
            elif bus_rating == "4":
                s_r,e_r = 4.0, 4.9
            elif bus_rating == "5":
                s_r,e_r = 5.0, 5.0
            else:
                s_r,e_r = 1, 5
            query = f'''
                SELECT * FROM bus_details_edit
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{A}"
                 AND Seats_Available BETWEEN {s_seat} AND {e_seat}  AND Ratings BETWEEN {s_r} AND {e_r} 
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_H(select_rating, select_fare, select_seat)
        slt.dataframe(df_result)


    # Assam bus fare filtering
    if S=="Assam":
        AS=slt.selectbox("list of rotes",lists_AS)

        def type_and_fare_AS(bus_rating, fare_range, seat):
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="red_bus_details")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            elif fare_range == "2000 and above":
                fare_min, fare_max = 2000, 100000
            else:
                fare_min, fare_max = 50, 100000



            if seat == "1-10":
                s_seat, e_seat = 1, 10
            elif seat == "11-20":
                s_seat, e_seat = 11, 20
            elif seat == "21-30":
                s_seat, e_seat = 21, 30
            elif seat == "31-40":
                s_seat, e_seat = 31, 40
            elif seat == "41-50":
                s_seat, e_seat = 41, 50
            else:
                s_seat, e_seat = 1, 50


            if bus_rating == "1":
                s_r,e_r = 1.0, 1.9
            elif bus_rating == "2":
                s_r,e_r = 2.0, 2.9
            elif bus_rating == "3":
                s_r,e_r = 3.0, 3.9
            elif bus_rating == "4":
                s_r,e_r = 4.0, 4.9
            elif bus_rating == "5":
                s_r,e_r = 5.0, 5.0
            else:
                s_r,e_r = 1, 5
            query = f'''
                SELECT * FROM bus_details_edit
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{AS}"
                 AND Seats_Available BETWEEN {s_seat} AND {e_seat}  AND Ratings BETWEEN {s_r} AND {e_r} 
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_AS(select_rating, select_fare, select_seat)
        slt.dataframe(df_result)

    # Utrra Pradesh bus fare filtering
    if S=="Utrra Pradesh":
        UP=slt.selectbox("list of rotes",lists_UP)

        def type_and_fare_UP(bus_rating, fare_range, seat):
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="red_bus_details")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            elif fare_range == "2000 and above":
                fare_min, fare_max = 2000, 100000
            else:
                fare_min, fare_max = 50, 100000



            if seat == "1-10":
                s_seat, e_seat = 1, 10
            elif seat == "11-20":
                s_seat, e_seat = 11, 20
            elif seat == "21-30":
                s_seat, e_seat = 21, 30
            elif seat == "31-40":
                s_seat, e_seat = 31, 40
            elif seat == "41-50":
                s_seat, e_seat = 41, 50
            else:
                s_seat, e_seat = 1, 50


            if bus_rating == "1":
                s_r,e_r = 1.0, 1.9
            elif bus_rating == "2":
                s_r,e_r = 2.0, 2.9
            elif bus_rating == "3":
                s_r,e_r = 3.0, 3.9
            elif bus_rating == "4":
                s_r,e_r = 4.0, 4.9
            elif bus_rating == "5":
                s_r,e_r = 5.0, 5.0
            else:
                s_r,e_r = 1, 5
            query = f'''
                SELECT * FROM bus_details_edit
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{UP}"
                 AND Seats_Available BETWEEN {s_seat} AND {e_seat}  AND Ratings BETWEEN {s_r} AND {e_r} 
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_UP(select_rating, select_fare, select_seat)
        slt.dataframe(df_result)

    # West Bengal bus fare filtering
    if S=="West Bengal":
        WB=slt.selectbox("list of rotes",lists_WB)

        def type_and_fare_WB(bus_rating, fare_range, seat):
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="red_bus_details")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            elif fare_range == "2000 and above":
                fare_min, fare_max = 2000, 100000
            else:
                fare_min, fare_max = 50, 100000



            if seat == "1-10":
                s_seat, e_seat = 1, 10
            elif seat == "11-20":
                s_seat, e_seat = 11, 20
            elif seat == "21-30":
                s_seat, e_seat = 21, 30
            elif seat == "31-40":
                s_seat, e_seat = 31, 40
            elif seat == "41-50":
                s_seat, e_seat = 41, 50
            else:
                s_seat, e_seat = 1, 50


            if bus_rating == "1":
                s_r,e_r = 1.0, 1.9
            elif bus_rating == "2":
                s_r,e_r = 2.0, 2.9
            elif bus_rating == "3":
                s_r,e_r = 3.0, 3.9
            elif bus_rating == "4":
                s_r,e_r = 4.0, 4.9
            elif bus_rating == "5":
                s_r,e_r = 5.0, 5.0
            else:
                s_r,e_r = 1, 5
            query = f'''
                SELECT * FROM bus_details_edit
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{WB}"
                 AND Seats_Available BETWEEN {s_seat} AND {e_seat}  AND Ratings BETWEEN {s_r} AND {e_r} 
                ORDER BY Price and Start_time  DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_WB(select_rating, select_fare, select_seat)
        slt.dataframe(df_result)



