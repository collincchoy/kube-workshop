FROM python:3.8

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

# CMD ["--host 0.0.0.0"]
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]