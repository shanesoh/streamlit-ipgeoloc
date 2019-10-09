# IP Geolocation using Streamlit
This simple app queries IPs for their geolocation and plots them on a map. Deploys on Heroku.

Demo: https://streamlit-ipgeoloc.herokuapp.com/

## How to Use

### Get a free API key from [ipdata.co](https://ipdata.co)
Then store it in a `.env` file

```bash
cat "IPDATA_API_KEY=xxxxx > .env"
```

### Run locally with Pipenv

```bash
pipenv run streamlit run app.py
```

### Run locally without Pipenv
```bash
pip install streamlit==0.47.3

IPDATA_API_KEY=xxxxx streamlit run app.py
``

### Deploy on Heroku
Create Heroku project and push to Heroku as  usual with `git push heroku master`. There's a fair amount of fussing around with deploying Streamlit on Heroku at this moment. See `setup.sh` and the following for more details:
* https://discuss.streamlit.io/t/hosting-streamlit-on-heroku/132/2
* https://discuss.streamlit.io/t/connection-error-when-deploying-using-docker-on-k8s/148
