from starlette.requests import Request


def get_db(request: Request):
    return request.state.db


def add_entity(database, entity):
    database.add(entity)
    database.commit()
    database.refresh(entity)