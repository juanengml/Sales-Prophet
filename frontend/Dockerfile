FROM python:3.10

RUN apt-get update 

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD streamlit run app.py
