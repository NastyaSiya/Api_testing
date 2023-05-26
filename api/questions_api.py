import json
from api.client import Client


class Api(Client):
    USERS = '/users'
    REGISER = '/register'
    BASE_URL = 'https://reqres.in/api'

    def list_users(self):
        """
        :method:    get
        :rout:  /users?page=2
        :status:    200
        """
        url = self.BASE_URL + self.USERS + '?page=2'
        return self.get(url)

    def single_user_not_found(self):
        """
        :method:    get
        :rout:      /api/users/23
        :status:    404
        """
        url = self.BASE_URL + self.USERS + '/23'
        return self.get(url)

    def single_user(self):
        """
        :method:    get
        :rout:      /api/users/2
        :status:    200
        """

        url = self.BASE_URL + self.USERS + '/2'
        return self.get(url)

    def create(self, name: str, job: str):
        """
        :method:    post
        :routs:     /api/users
        :status:    201
        :body:      {
                            "name": "",
                            "job": ""
                        }
        """
        url = self.BASE_URL + self.USERS
        payload = json.dumps({
            "name": F"{name}",
            "job": F"{job}"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        return self.post(url, headers, payload)

    def delete_user(self, id: int):
        """
        :method:    delete
        :routs:     /api/users/id
        :status:    204
        """
        url = self.BASE_URL + self.USERS + F"/{id}"
        return self.delete(url)

    def createpassword(self, email: str, password: str):
        """
        :method:    post
        :routs:     /api/users
        :status:    200
        :body:      {
                            "email": "eve.holt@reqres.in",
                            "password": "12345"
                        }
        """
        url = self.BASE_URL + self.REGISER
        payload = json.dumps({
            "email": F"{email}",
            "password": F"{password}"
        })
        headers = {
            "Content-Type": "application/json"
        }
        return self.post(url, headers, payload)

    def createuncorrect(self, email: str):
        """
        :method:    post
        :routs:     /api/users
        :status:    400
        :body:      {
                            "email": "eve.holt@reqres.in",
                         }
        """
        url = self.BASE_URL + self.REGISER
        payload = json.dumps({
            "email": F"{email}",
        })
        headers = {
            "Content-Type": "application/json"
        }
        return self.post(url, headers, payload)


api = Api()
