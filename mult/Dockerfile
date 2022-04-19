FROM python:alpine

ENV PYTHONUNBUFFERED 1

# exposing our app port in docker internal network
EXPOSE 8000

# creates a dir for our application
WORKDIR /mult

# copy our requirements.txt file and install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy the rest of our application
COPY . .
# run the application
CMD python manage.py runserver 0.0.0.0:8000
