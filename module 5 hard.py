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
        print('Выход из аккаунта')

    def log_in(self, login: str, password: str):
        for user in self.users:
            if login == user.nickname and password == user.password:
                self.current_user = user
                print(f"Вход выполнен как {nickname}")

    def add(self, *args):
        for movie in args:
            if movie not in self.videos:
                self.videos.append(movie)

    def get_videos(self, search_word):
        result = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, video_title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == video_title:  
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                print(f"Воспроизведение видео: {video.title}")
                for i in range(1, video.duration + 1):
                    print(f"Просмотр: {i} секунд")
                    time.sleep(1)
                    video.time_now = i
                print("Конец видео")
                return
        print(f"Видео с названием '{video_title}' не найдено.")



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')




