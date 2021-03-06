### DATING APP

class DatingApp:
    def __init__(self, name):
        self.name = name
        self.registered_profiles = []

    def register(self, *profiles): #separate the tasks of checking and adding to registered_profiles
        for profile in profiles:
            if isinstance([profile for profile in profiles], Profile):
                raise TypeError(f"{profile} is not an object of class Profile.")

        self.registered_profiles = [profile for profile in profiles]

    def new_day(self):
        for profile in self.registered_profiles:
            profile.reset_likes_count()

    def check_recommend_criteria(self,target, profile):

    def recommend_profiles(self, target):
        return f"{[profile.id for profile in self.registered_profiles if profile.id not in target.likes_list and target.gender_pref == profile.gender and target.gender == profile.gender_pref]}"

    def who_liked_profile(self, target):
        return f"{[profile.id for profile in self.registered_profiles if target.id in profile.likes_list]}"

    def advanced_recommend_profiles(self, target):
        recommendations = [profile.id for profile in self.registered_profiles if
                           profile.id not in target.likes_list and target.gender_pref == profile.gender and target.gender == profile.gender_pref and target.id in profile.likes_list]
        recommendations += [profile.id for profile in self.registered_profiles if
                            profile.id not in target.likes_list and target.gender_pref == profile.gender and target.gender == profile.gender_pref and target.id not in profile.likes_list]
        return recommendations


class Profile:
    id = 1

    def __init__(self, gender, age, gender_pref):
        self.id = Profile.id
        self.age = age
        self.gender = gender
        self.gender_pref = gender_pref
        Profile.id += 1
        self.likes_per_day = 1
        self.likes_list = []

    def reset_likes_count(self):
        self.likes_per_day = 1

    def __repr__(self):
        return f"{self.age} year old {self.gender}, looking for a {self.gender_pref}. (id: {self.id})"

    def likes(self, target):
        if self.likes_per_day < 1:
            print("You can't like more, you've reached your like limit.")
        elif target.id == self.id:
            print("You can't like your own profile.")
        elif target.id in self.likes_list:
            print("You already liked this profile.")
        else:
            self.likes_list.append(target.id)
            self.likes_per_day -= 1
            if self.id in target.likes_list:
                print("It's a match!")

    def send_message(self, target, message):
        print("Unable to send message, upgrade your profile to Pro.")


class FreeProfile(Profile):

    def __init__(self, gender, age, gender_pref):
        super().__init__(gender, age, gender_pref)


class ProProfile(Profile):

    def __init__(self, name, gender, age, gender_pref):
        super().__init__(gender, age, gender_pref)
        self.name = name
        self.likes_per_day = 1000

    def reset_likes_count(self):
        self.likes_per_day = 1000

    def __repr__(self):
        return f"{self.name.capitalize()} is a {self.age} year old {self.gender}, looking for a {self.gender_pref}. (id: {self.id})"

    def send_message(self, target, message):
        print(f"Message is sent to profile #{target.id}.")


### SAMPLE CODE Using your solution, the following code should run without errors and print the expected results
ibsnder = DatingApp('IBSnder')
john = ProProfile('John', 'male', 30, 'female')  # should have profile id 1
jane = FreeProfile('female', 28, 'male')  # should have profile id 2
kate = ProProfile('Kate', 'female', 34, 'female')  # should have profile id 3
jack = FreeProfile('male', 23, 'male')  # should have profile id 4
jill = ProProfile('Jill', 'female', 28, 'male')  # should have profile id 5
bob = ProProfile('Bob', 'male', 42, 'female')  # should have profile id 6
david = FreeProfile('male', 37, 'female')  # should have profile id 7
ibsnder.register(john, jane, kate, jack, jill, bob, david)
print(john)  # should print: John is a 30 year old male, looking for a female. (id: 1)
print(jane)  # should print: 28 year old female, looking for a male. (id: 2)
john.likes(jane)
jane.likes(john)  # should print: It's a match!
jane.likes(bob)  # should print: You can't like more, you've reached your like limit.
john.likes(john)  # should print: You can't like your own profile.
john.likes(kate)
jill.likes(john)
david.likes(jill)
print(ibsnder.recommend_profiles(jill))  # since Jill already liked John, it should print only: [6, 7]
print(ibsnder.advanced_recommend_profiles(jill))  # since David liked Jill, it should print only: [7, 6]
print(ibsnder.who_liked_profile(john))  # should print [2, 5]
ibsnder.new_day()
jane.likes(john)  # should print: You already liked this profile.
jane.likes(bob)  # no error, because Jane again has a free like
john.send_message(jane, 'hello')  # should print: Message is sent to profile #2.
jane.send_message(john, 'hi')  # Unable to send message, upgrade your profile to Pro.
