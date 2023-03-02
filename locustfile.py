from locust import HttpUser, task,between

class AppUser(HttpUser):
    wait_time = between(2, 5)

    @task
    def test_index(self):
        self.client.get("/")

    @task
    def test_showSummary(self):
        from_data = {'email':'admin@irontemple.com'}
        self.client.post("/showSummary", data = from_data)

    @task
    def test_book(self):
        self.client.get("/book/Spring Festival/She Lifts")

    @task
    def test_purchasePlaces(self):
        from_data = {'competition': 'atam competiton',
                'club': 'Simply Lift',
                'date': '2023-03-30 13:30:00',
                'places':'10'}
        self.client.post("/purchasePlaces", data = from_data)

    
    @task
    def test_logout(self):
        self.client.get("/logout")

# from locust import HttpUser, TaskSet, task, between

# class UserBehaviour(TaskSet):

#     def on_start(self):
#         self.client.get('/login')

#     def on_stop(self):
#         self.client.get('/logout')

#     @task(10)
#     def index(self):
#         self.client.get("/showSummary",methods=['POST'])

#     @task(5)
#     def book(self):
#         self.client.get("/book/<competition>/<club>")

#     @task(1)
#     def purchase(self):
#         self.client.get("/purchasePlaces",methods=['POST'])

# class WebsiteUser(HttpUser):
#     tasks = [UserBehaviour] # task_set = UserBehaviour
#     wait_time = between(5, 9)