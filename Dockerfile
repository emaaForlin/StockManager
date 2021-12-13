FROM python:3.10-slim
ADD . /StockManager
RUN cd /StockManager && pip install -r requirements.txt
WORKDIR /StockManager/app
EXPOSE 8000:8000
CMD [ "python", "main.py" ]