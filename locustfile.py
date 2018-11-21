from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):
    @task
    def req_1(self):
        self.client.post("/anonAccountInfoGet", json={"type": "anonAccountInfoGet", "bodyId":"int:0500012C0067F4EC"})

    @task
    def req_050001F2E1AB12E1(self):
        self.client.post("/anonAccountInfoGet", json={"type": "anonAccountInfoGet", "bodyId":"int:05000137B41D9EC6"})

    @task
    def req_050001D58A983AE6(self):
        self.client.post("/anonAccountInfoGet", json={"type": "anonAccountInfoGet", "bodyId":"int:050001F8CAA3C487"})

    @task
    def req_050001724C8EACD9(self):
        self.client.post("/anonAccountInfoGet", json={"type": "anonAccountInfoGet", "bodyId":"int:05000163AA20FA3D"})
    
    @task
    def req_050001552F5A5E8E(self):
        self.client.post("/anonAccountInfoGet", json={"type": "anonAccountInfoGet", "bodyId":"int:050001A6E1DE4438"})

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 10
    max_wait = 20
