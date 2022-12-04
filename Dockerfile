FROM python:3

LABEL author="anoop600"
ENV port=5001
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE ${port}
CMD ["python","app.py"]