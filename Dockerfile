FROM python:3.10
ADD . /StockManager
RUN cd /StockManager && pip3 install -r requirements.txt
WORKDIR /StockManager/app
CMD [ "uvicorn", "main:app" ]