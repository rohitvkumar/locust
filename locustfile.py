from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):
    @task
    def req_050001F359206076(self):
        self.client.post("/anonAccountInfoGet", json={"type": "anonAccountInfoGet", "bodyId":"int:050001F359206076"})

    @task
    def req_050001F2E1AB12E1(self):
        self.client.post("/anonAccountInfoGet", json={"type": "anonAccountInfoGet", "bodyId":"int:050001F2E1AB12E1"})

    @task
    def req_050001D58A983AE6(self):
        self.client.post("/anonAccountInfoGet", json={"type": "anonAccountInfoGet", "bodyId":"int:050001D58A983AE6"})

    @task
    def req_050001724C8EACD9(self):
        self.client.post("/anonAccountInfoGet", json={"type": "anonAccountInfoGet", "bodyId":"int:050001724C8EACD9"})
    
    @task
    def req_050001552F5A5E8E(self):
        self.client.post("/anonAccountInfoGet", json={"type": "anonAccountInfoGet", "bodyId":"int:050001552F5A5E8E"})

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 100
    max_wait = 200
