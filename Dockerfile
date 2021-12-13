FROM python:3.10-alpine
ADD . /StockManager
RUN cd /StockManager && pip3 install -r requirements.txt
WORKDIR /StockManager/app
CMD [ "python", "main.py" ]