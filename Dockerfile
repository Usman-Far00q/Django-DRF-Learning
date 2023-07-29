# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.9

LABEL authors="usman"
# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY . code
WORKDIR /code

EXPOSE 8000

# runs the production server
#ENTRYPOINT ["python", "manage.py"]
#CMD ["echo", "Starting development server at %(protocol)s://%(addr)s:%(port)s/\n"]
#CMD ["runserver", "0.0.0.0:8000"]
