# from selenium import webdriver
# import time
# import pytest
#
#
# @pytest.fixture(scope='module')
# def krisha_kz():
#     global name
#     name = webdriver.Chrome()
#     name.implicitly_wait(10)
#     name.delete_all_cookies()
#     name.get('https://krisha.kz/')
#     name.implicitly_wait(5)
#     name.quit()
#
#
# @pytest.mark.usefixtures('krisha_kz')
# def test_py(krisha_kz):
#     assert "Крыша" in name.title
#
#
# @pytest.mark.usefixtures('krisha_kz')
# def url_test(krisha_kz):
#     assert name.url == "https://krisha.kz/"


from selenium import webdriver
import time
import pytest

driver = None

@pytest.fixture(scope='module')
def krisha_kz():
    global name
    name = webdriver.Chrome()
    name.implicitly_wait(10)
    name.delete_all_cookies()
    name.get('https://krisha.kz/')
    yield
    name.implicitly_wait(5)
    name.quit()

@pytest.mark.usefixtures('krisha_kz')
def test_url_zero(krisha_kz):
    assert "Крыша" in name.title

@pytest.mark.usefixtures('krisha_kz')
def test_url_one(krisha_kz):
    assert "Недвижимость" in name.title


@pytest.mark.usefixtures('krisha_kz')
def test_url_two(krisha_kz):
    assert name.url == "https://krisha.kz/"
