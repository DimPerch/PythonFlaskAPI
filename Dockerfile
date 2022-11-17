FROM python:rc-alpine

ADD . .

RUN pip install -r/requirements.txt

WORKDIR /
EXPOSE 5000
COPY . .

CMD ["python","-u", "main.py"]