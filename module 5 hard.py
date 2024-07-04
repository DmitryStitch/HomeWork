import time

class User:
    def __init__(self,nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    def __init__(self,title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

    def __contains__(self, item):
        return item in self.items


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname: str, password: str, age: int):
        password = hash(password)
        for user in self.users:
                if user.nickname == nickname:
                    print(f"Пользователь {nickname} уже существует")
                    return

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} зарегистрирован и вошел в систему.")

    def log_out(self):
        self.current_user = None

    def log_in(self, login: str, password: str):
        for user in self.users:
            if login == user.nickname and password == user.password:
                self.current_user = user

    def add(self, *args):
        for movie in args:
            if movie not in self.videos:
                self.videos.append(movie)



time_now = 0
        for i in range(duration):
            sleep(1)
            time_now += 1
            print('Конец видео')




