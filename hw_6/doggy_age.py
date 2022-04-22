"""Task 2
Doggy age
Create a class Dog with class attribute age_factor equals to 7. Make _init_() which takes values for a dog’s age.
Then create a method human_age which returns the dog’s age in human equivalent.
(Собачий возраст
Создайте класс Dog с атрибутом age_factor, равным 7. Сделайте __init __(), который принимает значения для возраста
собаки. Затем создайте метод human_age, который возвращает возраст собаки в человеческом эквиваленте (то есть работает
формула: "возраст в человеческом эквиваленте" = "возраст собаки" * 7)
Третье задание сложное и требует вдумчивого подхода.

"""


class DogAge:
    def __init__(self, dog_age):
        self.dog_age = dog_age
        self.age_factor = 7

        try:
            self.dog_age = int(self.dog_age)
        except ValueError:
            return 'age must contain digits only!'
        else:
            pass

    def human_age(self):
        return f"Human age of your dog is: {self.dog_age * self.age_factor}"


d_a = input("Input age of your dog: ")
d = DogAge(d_a)
print(d.human_age())
