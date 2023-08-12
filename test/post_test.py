import pytest
from assertpy import assert_that
from faker import Faker

from api_client.posts import PostAPI


@pytest.fixture(scope="session")
def post_api():
    return PostAPI()


def test_get_all_posts(post_api):
    response = post_api.get_all()
    assert_that(response.status_code).is_equal_to(200)
    total_posts = len(response.json())
    assert_that(total_posts).is_greater_than_or_equal_to(1)


def test_get_post_by_id(post_api):
    post_id = 100
    response = post_api.get_by_id(post_id)
    assert_that(response.status_code).is_equal_to(200)
    data = response.json()
    data_post = data['id']
    assert_that(data_post).is_equal_to(post_id)


def test_create_post(post_api):
    fake = Faker()
    request_body = {
        'title': fake.word(),
        'body': fake.sentence(),
        'userID': 1
    }
    response = post_api.create_post(request_body)
    assert_that(response.status_code).is_equal_to(201)
    assert_that(response.text).contains(request_body['title'])
    assert_that(response.text).contains(request_body['body'])
    assert_that(response.json().get('userID')).is_equal_to('1')


def test_update_post(post_api):
    fake = Faker()
    post_id = 1
    request_body = {
        'id': 1,
        'title': fake.word(),
        'body': fake.sentence(),
        'userID': 1
    }
    response = post_api.update_post(request_body, post_id)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json().get('id')).is_equal_to(post_id)


def test_update_post_title(post_api):
    fake = Faker()
    post_id = 1
    request_body = {
        'title': fake.word()
    }
    response = post_api.update_post_patch(request_body, post_id)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.text).contains(request_body['title'])


def test_delete_post(post_api):
    post_id = 1
    response = post_api.delete_post(post_id)
    assert_that(response.status_code).is_equal_to(200)
