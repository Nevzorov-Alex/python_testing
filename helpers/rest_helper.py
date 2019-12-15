import logging
from abc import ABC
import requests
import pprint
from json import JSONDecodeError
from http import HTTPStatus
import time


class RESTService(ABC):
    __version__ = 1

    def __init__(self, api_url: str, resource_name: str, headers: dict = None) -> None:
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)

        formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        sh.setFormatter(formater)
        self.logger.addHandler(sh)

        self._url = f"{api_url}/{resource_name}"
        if headers:
            self._headers = headers
        else:
            self._headers = {}

        self.logger.debug(f"RESTServis init.{self.__repr__()}")

    def get(self, url: str = None, params: dict = None, headers: dict = None) -> dict:
        if not url:
            url = self._url
        if headers:
            headers = {**self._headers, **headers}.copy()
        else:
            headers = self._headers.copy()
        try:
            req = requests.get(url=url, params=params, headers=headers)
        except requests.exceptions.ConnectionError as e:
            raise Exception

        if not str(req.status_code).startswith("2"):
            "bad situation"
            pass

        if not req.status_code == HTTPStatus.MOVED_PERMANENTLY:
            "moved logic"
            pass

        req_json = {}
        try:
            req_json = req.json()
        except JSONDecodeError as e:
            pass

        return {"code": req.status_code, "json": req_json, "headers": headers}

    def _post(self, url: str = None, params: dict = None, headers: dict = None) -> dict:
        if not url:
            url = self._url
        if headers:
            headers = {**self._headers, **headers}.copy()
        else:
            headers = self._headers.copy()
        req_json = {}
        try:
            req_json = requests.post(url=url, params=params, headers=headers)
        except req_json.exceptions.ConnectionError as e:
            exit(100)
        return {"code": req_json.status_code, "json": req_json, "headers": headers}

    def _put(self, url: str = None, params: dict = None, headers: dict = None) -> dict:
        if not url:
            url = self._url
        if headers:
            headers = {**self._headers, **headers}.copy()
        else:
            headers = self._headers.copy()
        req_json = {}
        try:
            req_json = requests.put(url=url, params=params, headers=headers)
        except req_json.exceptions.ConnectionError as e:
            exit(100)
        return {"code": req_json.status_code, "json": req_json, "headers": headers}

    def _delete(self, url: str = None, params: dict = None, headers: dict = None) -> dict:
        if not url:
            url = self._url
        if headers:
            headers = {**self._headers, **headers}.copy()
        else:
            headers = self._headers.copy()
        req_json = {}
        try:
            req_json = requests.delete(url=url, params=params, headers=headers)
        except req_json.exceptions.ConnectionError as e:
            exit(100)
        return {"code": req_json.status_code, "json": req_json, "headers": headers}

    def __repr__(self):
        return self.__dict__


class CatFactService(RESTService):
    def __init__(self, api_url: str, resource_name: str):
        super().__init__(api_url, resource_name)

    def get_random_fact(self, animal_type: str = 'cat', amount: int = 1):
        params = {
            "animal_type": animal_type,
            "amount": amount
        }

        response = self.get(url=f"{self._url}/random", params=params)
        self.logger.debug(response)

        return response

    def get_fact_by_id(self, sid: str):
        response = self.get(url=f"{self._url}/{sid}")
        self.logger.debug(response)
        return response

    def post_fact_by_id(self, animal_type: str = 'cat',  text: str = 'text'):
        params = {
            "animal_type": animal_type,
            "text": text
        }
        response = self._post(url=f"{self._url}", params=params)
        self.logger.debug(response)
        return response

    def put_fact_id(self, sid: str, animal_type: str = 'cat', text: str = "   "):
        params = {
            "animal_type": animal_type,
            "text": text
        }
        response = self._put(url=f"{self._url}", params=params)

        self.logger.debug(response)
        return response

    def delete_fact_by_id(self, sid: str):
        response = self._delete(url=f"{self._url}/{sid}")
        self.logger.debug(response)
        return response


if __name__ == '__main__':
    api_url = "https://cat-fact.herokuapp.com"
    resource_name = "facts"
    cfs = CatFactService(api_url=api_url, resource_name=resource_name)

    fact_json = cfs.get_random_fact(amount=100, animal_type="dog")
    fact_list = fact_json.get("json")

    for fact in fact_list:
        print(fact.get("_id"), fact.get("text"))
        sid = fact.get("_id")
        time.sleep(0.5)


    print(cfs.delete_fact_by_id(sid),sid)

    print(cfs.post_fact_by_id( animal_type="dog", text="dog is barking,caravan is going"))

    print(cfs.put_fact_id(sid,animal_type="dog", text="dog is barking,caravan is going"))

