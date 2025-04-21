from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(3.0, 10.5)

    @task
    def my_task(self):#
        self.client.get("/")
        class MyUser2(HttpUser):
            wait_time = between(1, 3)

# @task
# def send_post_request(self):
#         payload = {
#             "username": "test_user",
#             "password": "123456"
#         }
#
#         headers = {
#             "Content-Type": "application/json",
#             "Authorization": "Bearer token123"
#         }
#
#         self.client.post(
#             "/login",
#             json=payload,
#             headers=headers,
#             name="POST /login"
#         )