import requests
from Utils.http_methods import Http_method

base_url="https://petstore.swagger.io"

class Swagger_petshop_api():

      @staticmethod
      def add_new_pet():
          json_for_add_new_pet = {
              "id": 5,
              "category": {
                  "id": 5,
                  "name": "string"
              },
              "name": "doggie",
              "photoUrls": [
                  "string"
              ],
              "tags": [
                  {
                      "id": 5,
                      "name": "string"
                  }
              ],
              "status": "available"
          }
          post_resource="/v2/pet"
          post_url=base_url+post_resource
          print(post_url)
          result_post=Http_method.post(post_url,json_for_add_new_pet)
          print(result_post.text)
          return result_post

      @staticmethod
      def get_add_pet(id):
          get_resource = "/v2/pet/"
          get_url = base_url+get_resource+str(id)
          result_get=Http_method.get(get_url)
          print(result_get.text)
          return result_get

      @staticmethod
      def put_add_pet(id):
          put_resource = "/v2/pet"
          put_url = base_url + put_resource
          json_for_update_put={
              "id": id,
              "category": {
                  "id": id,
                  "name": "string"
              },
              "name": "doggie",
              "photoUrls": [
                  "string"
              ],
              "tags": [
                  {
                      "id": id,
                      "name": "string"
                  }
              ],
              "status": "pending"
          }
          result_put = Http_method.put(put_url,json_for_update_put)
          print(result_put.text)
          return result_put

      @staticmethod
      def delete_new_pet(id):
          delete_resource = "/v2/pet/"
          delete_url = base_url + delete_resource + str(id)
          result_delete = Http_method.delete(delete_url)
          print(result_delete.text)
          return result_delete

