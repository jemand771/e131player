FROM python:3

RUN mkdir /config
ADD *.py /
ADD requirements.txt /
RUN pip install -r requirements.txt

CMD ["python", "main.py"]