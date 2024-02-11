FROM python:3.11.4

WORKDIR .

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "__main__.py"]