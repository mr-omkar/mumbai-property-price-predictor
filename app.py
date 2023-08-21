import pandas as pd
import numpy as np
import streamlit as st
import dill

st.set_page_config(
    page_title="Mumbai Property Price",
    page_icon="₹"
)


data = pd.read_csv("Properties.csv")
df = pd.DataFrame(data)
regions = df['Region'].unique()
Property_Age = df['Property_Age'].unique()
Availability = df['Availability'].unique()
Area_Tpye = df['Area_Tpye'].unique()
Floor_No = df['Floor_No'].unique()
Bedroom = df['Bedroom'].unique()
Bathroom = df['Bathroom'].unique()



# print(regions,Property_Age,Availability,Area_Tpye,Floor_No,Bedroom,Bathroom)


# print(Floor_No)
st.title("Mumbai's Property Price Predector")

def load_data():
    data = pd.DataFrame([[inp_reg,inp_age,inp_aval,inp_area,inp_areasqft,inp_flr,inp_bed,inp_bath]],
                        columns=['Region','Property_Age','Availability','Area_Tpye','Area_SqFt','Floor_No','Bedroom','Bathroom'])


    prediction(data)

def prediction(inp):
    with open("pipelineRfr.pkl","rb") as f:
        m = dill.load(f)
    res = m.predict(inp)[0]
    out = round(res,4) * 100000
    out = round(out,2)
    out = f"{out:,}"
    print(out)
    # print(f"{out:,}")
    c2.success("Predicted Price : ₹ {}".format(out))

min_area = int(df["Area_SqFt"].min())
max_area = int(df["Area_SqFt"].max())

# min_rate = int(df["Rate_SqFt"].min())
# max_rate = int(df["Rate_SqFt"].max())

min_floor = int(df["Floor_No"].min())
max_floor = int(df["Floor_No"].max())

min_bed = int(df["Bedroom"].min())
max_bed = int(df["Bathroom"].max())

min_bath = int(df["Bathroom"].min())
max_bath = int(df["Bathroom"].max())

c1 = st.container()
c1.subheader("Enter Property Details")
col1, col2 = c1.columns(2)
with col1:
    inp_reg = col1.selectbox("Region",regions)
    col1.divider()
    inp_aval = col1.radio("Availability",Availability)


with col2:
    inp_age = col2.selectbox("Property Age",Property_Age)
    col2.divider()
    inp_area = col2.radio("Area Type",Area_Tpye)

c1.divider()
inp_flr = c1.number_input("Floor No",min_floor,max_floor)
c1.divider()

col11, col12 = c1.columns(2)

with col11:
        inp_areasqft = col11.number_input("Area SqFt",min_area,max_area)
        col11.divider()
        inp_bed = col11.number_input("Bedroom",min_bed,max_bed)


with col12:
        # inp_ratesqft = col12.number_input("Rate SqFt",min_rate,max_rate)
        col12.divider()
        inp_bath = col12.number_input("Bathroom",min_bath,max_bath)

c1.divider()


c2 = st.container()




# inp_flr = st.select_slider("Floor No",np.sort(Floor_No))
# inp_bed = st.select_slider("Bedroom",np.sort(Bedroom))
# inp_bath = st.select_slider("Bathroom",np.sort(Bathroom))





c2.button("Calculate",on_click=load_data)

c2.divider()

