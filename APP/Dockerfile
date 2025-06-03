FROM python:3.12-slim

WORKDIR /app

COPY . /app
 
RUN pip install --upgrade -r /app/requirements.txt

EXPOSE 8080

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080",  "--server.address=0.0.0.0"]



