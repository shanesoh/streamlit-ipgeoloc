FROM python:3.7.4-slim-buster

RUN pip install streamlit==0.47.3

COPY . /app

# Streamlit workaround
# https://discuss.streamlit.io/t/running-streamlit-in-docker/103/5
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'

# https://discuss.streamlit.io/t/connection-error-when-deploying-using-docker-on-k8s/148
RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'

WORKDIR /app
CMD streamlit run /app/app.py

