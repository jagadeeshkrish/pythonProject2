#Request module-
#module-> Package or libraries contains functions which  you can use easily
#math,OS,csv,allure,pytest
#TO make the HTTP-Methods
#Request-Module
#GET,POST,PUT,PATCH,DELETE,POTIONS..HTTP METHODS
#URL.AUTH,COOKIES,VERIFICATION with pytest

#Get Request- Booking ID (Client-Server)
#URL
#AUTH ->X
#PAYLOAD ->X
#CONTENT TYPE- or HEADER->X
#QUERY PARAM->X
#PATH PARAM-Yes

#Response
#BOdy -> Verify -Assert ., #Key,Values
#Status code -> Verify
#Time
#JSON Schema ,XML Schema

import pytest #pip install pytest
import allure #pip install allure-pytest
import requests

@allure.title("Test GET Request-RestFUL BOOKER Project#1")
@allure.description("TC#1-> Verify the GET Request with ID works")
#@allure.tag(*tags:"Regression", "p0","Smoke")
#@allure.label(label_type:"owner", *labels:"JK")
@allure.testcase("TC#4")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url="https://restful-booker.herokuapp.com/booking/1"
    responseData=requests.get(url)
    print(responseData.text)
    print(responseData.headers)
    print(responseData.cookies)
    print(responseData.json())
    assert responseData.status_code == 200

