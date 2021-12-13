FROM python:3.10-alpine
ADD . /StockManager
RUN cd /StockManager && pip install -r requirements.txt
WORKDIR /StockManager/app
CMD [ "python", "main.py" ]