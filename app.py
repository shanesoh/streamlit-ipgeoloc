import streamlit as st
import pandas as pd
import requests
import json
import os

API_KEY = os.environ.get('IPDATA_API_KEY')
API_URL = 'https://api.ipdata.co/'


def query_ip(ips):
    df = pd.DataFrame()
    for ip in ips.split(','):
        ip = ip.strip()
        response = requests.get(f'{API_URL}{ip}?api-key={API_KEY}')
        if response.status_code == 200:
            data = json.loads(response.content)
            df = df.append(pd.DataFrame(pd.io.json.json_normalize(data)))
    return df


st.title('IP Geolocation')
ips = st.text_area('IP addresses separated by comma', '8.8.8.8, 1.1.1.1')

df = query_ip(ips)
st.table(df[['ip', 'emoji_flag', 'country_name', 'city', 'asn.name', 'asn.type']].reset_index())

st.deck_gl_chart(
    layers=[
        {
            'data': df,
            'type': 'TextLayer',
            'getText': 'ip',
        },
        {
            'data': df,
            'type': 'ScatterplotLayer',
            'getRadius': 1e2,
        }
    ]
)
