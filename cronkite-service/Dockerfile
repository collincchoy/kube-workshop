FROM python:3.7-slim

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["uvicorn", "cronkite_service.app:app", "--host", "0.0.0.0"]