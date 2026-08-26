from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from fastapi_zero.schemas import (
    Message,
    UserDB,
    UserList,
    UserPublic,
    UserSchemas,
)

app = FastAPI()

database = []

# CRUD x HTTP
# Create x POST
# Read x GET
# Update x PUT
# Delete x DELETE


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}


# response model é a forma de retornar para vc
# Como esta retornando a classe UserPublic para mim
# Create
@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchemas):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    # precisamos criar um modelo para nosso banco
    # precisamos de um id para cada registro

    database.append(user_with_id)
    return user_with_id


# read, sem filtro
@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': database}


# update
# put altera todos os dados
# essas "{}" são variaveis, nesse caso vamos usar o id,
# para achar o user que queremos alterar


@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def update_user(user_id: int, user: UserSchemas):
    user_with_id = UserDB(**user.model_dump(), id=user_id)

    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='NOT FOUND!'
        )

    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='NOT FOUND!'
        )

    return database.pop(user_id - 1)
