import requests

def introspection_info(obj):


  info = {
    "Тип": type(obj),
    "Атрибуты": dir(obj),
    "Методы": [attr for attr in dir(obj) if callable(getattr(obj, attr))],
    "Модуль": getattr(obj, "__module__", None),
  }

  return info

number_info = introspection_info('Готовимся писать диплом')
print(number_info)