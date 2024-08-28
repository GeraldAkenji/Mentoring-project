FROM python:3.7

LABEL maintainer="Idris Fagbemi"

WORKDIR /app


COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

# HEALTHCHECK CMD curl --fail http://localhost:5000/ || exit 1

CMD ["python", "-m", "pytest"]

EXPOSE 5000

ENTRYPOINT ["python", "app.py"]