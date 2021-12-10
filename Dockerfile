FROM python:3.10
ADD . /StockManager
RUN cd /StockManager && pip3 install -r requirements.txt
WORKDIR /StockManager/app
EXPOSE 8000
CMD [ "uvicorn", "main:app" ]