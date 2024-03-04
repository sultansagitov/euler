FROM python

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY pg_hba.conf /etc/postgresql/$PG_MAJOR/main/pg_hba.conf
RUN chmod 0600 /etc/postgresql/$PG_MAJOR/main/pg_hba.conf

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
