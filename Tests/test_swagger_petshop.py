import json
import allure
from requests import Response
from Utils.Cheking import Checking
from Utils.api import Swagger_petshop_api
"""Создание, изменение и удаление нового пета"""
@allure.epic("Test petstore")
class Test_create_pet():
    @allure.description("Test create, update, delete new pet")
    def test_add_new_pet(self):

        print("              Метод POST")
        result_post: Response = Swagger_petshop_api.add_new_pet()
        check_post = result_post.json()
        id = check_post.get("id")
        token=json.loads(result_post.text)
        print(list(token))
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['id', 'category', 'name', 'photoUrls', 'tags', 'status'])
        Checking.check_json_value(result_post, 'status', 'available')

        print("              Метод GET POST")
        result_get: Response = Swagger_petshop_api.get_add_pet(id)
        Checking.check_status_code(result_get, 200)
        token = json.loads(result_get.text)
        print(list(token))
        Checking.check_json_token(result_get, ['id', 'category', 'name', 'photoUrls', 'tags', 'status'])
        Checking.check_json_value(result_get, 'status', 'available')
        Checking.check_json_value(result_get, 'name', 'doggie')

        print("              Метод PUT")
        result_put: Response = Swagger_petshop_api.put_add_pet(id)
        token = json.loads(result_put.text)
        print(list(token))
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['id', 'category', 'name', 'photoUrls', 'tags', 'status'])
        Checking.check_json_value(result_put, 'name', 'doggie')
        Checking.check_json_value(result_put, 'status', 'pending')

        print("              Метод GET PUT")
        result_get: Response = Swagger_petshop_api.get_add_pet(id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['id', 'category', 'name', 'photoUrls', 'tags', 'status'])
        Checking.check_json_value(result_get, 'status', 'pending')

        print("              Метод DELETE")
        result_delete: Response = Swagger_petshop_api.delete_new_pet(id)
        Checking.check_status_code(result_delete, 200)
        token = json.loads(result_delete.text)
        print(list(token))
        Checking.check_json_token(result_delete, ['code', 'type', 'message'])
        Checking.check_json_value(result_delete, 'type', 'unknown')

        print("              Метод GET DELETE")
        result_get: Response = Swagger_petshop_api.get_add_pet(id)
        Checking.check_status_code(result_get, 404)
        token = json.loads(result_get.text)
        print(list(token))
        Checking.check_json_token(result_get, ['code', 'type', 'message'])
        Checking.check_json_search_word_in_value(result_get, 'message', 'Pet not found')

        print("Тестирование создания, изменения и удаления нового пета прошло успешно")