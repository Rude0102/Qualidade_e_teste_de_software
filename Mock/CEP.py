import unittest
import requests
from unittest.mock import MagicMock,patch

cep='000000'

def validaCep(cep):
    if len(cep)==8:
        link=f'https://viacep.com.br/ws/{cep}/json/'

        response= requests.get(link)
        response_json= response.json()

        if response_json['uf'] =='SP':
            return True
        else:
            return False
    else:
        return False

funcao= validaCep(cep)



class TestMock(unittest.TestCase):

    @patch('requests.get')
    def test_api_call(self,response_mock):
        response_mock.return_value= MagicMock(status_code=200)
        response_mock.return_value.json.return_value= {"uf":"SP"}
        
        testeCep=validaCep("00000000")

        self.assertEqual(testeCep,True)
        response_mock.assert_called_once_with("https://viacep.com.br/ws/00000000/json")



if __name__ == '__main__':
    unittest()