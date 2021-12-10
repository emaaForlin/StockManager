# StockManager

This is an API for stock management, you can create your own client and use this API as backend.

## How to use
First you need to clone this repo with `git clone https://github.com/emaaForlin/StockManager.git`

Next install the requirements `cd ./StockManager && pip3 install -r requirements.txt`

Then go to `app` directory and run `uvicorn main:app`. Now open your browser in `http://localhost:8000` and you'll see welcome message.

In `http://localhost:8000/docs` are all the using documentation and you can test the API

If you prefer, you can run `docker run emaaforlin/StockManager`
**Don't use this at production because this has not file persistence.**

## Next moves
- [ ] CI/CD Workflow.
- [ ] Workflow to create a docker image.
- [ ] Edit the README.md when a new docker image is uploaded to the registry.
- [ ] Create the `Dockerfile`.
- [x] Logging feature.
- [x] Error handling in functions.
- [x] Edit items.
- [x] Add quantity field.
- [x] Use old IDs with new items.
- [x] Delete item.
- [x] Get item or items by name or id.
- [x] Get all items.
- [x] Add items.
