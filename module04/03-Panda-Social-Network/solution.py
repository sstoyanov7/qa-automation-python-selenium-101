class Panda:
    def __init__(self, name, email, gender):
        self._name = name
        self._email = email
        self._gender = gender
        return

    def name(self):
        return self._name

    def email(self):
        return self._email

    def gender(self):
        return self._gender

    def isMale(self):
        return self._gender == "male"

    def isFemale(self):
        return not self.isMale()

    def __eq__(self, other):
        result = self._name == other.name() and \
                 self._email == other.email() and \
                 self._gender == other.gender()

        return result

    def __hash__(self):
        s = self.__str__()
        h = hash(s)
        h2 = hash((self.name(), self.email(), self.gender()))
        return h

    def __str__(self):
        return f'Panda: ({self.name()}, {self.email()}, {self.gender()})'


class PandaSocialNetwork:
    def __init__(self):
        self.network = {}
        self.friends = {}
        return

    def add_panda(self, panda):
        if self.has_panda(panda):
            raise ValueError(f'I\'s already added {str(panda)} to the network.')

        key = panda.__hash__()
        self.network[key] = {key: panda}

        return

    def has_panda(self, panda):
        key = panda.__hash__()
        b = key in self.network

        return b

    def make_friends(self, panda1, panda2):
        if (not self.has_panda(panda1)):
            self.add_panda(panda1)

        if (not self.has_panda(panda2)):
            self.add_panda(panda2)

        key1 = panda1.__hash__()
        key2 = panda2.__hash__()
        self.network[key1][key2] = panda2
        self.network[key2][key1] = panda1

        return

    def are_friends(self, panda1, panda2):
        key1 = panda1.__hash__()
        key2 = panda2.__hash__()
        b = (key1 in self.network) and (key2 in self.network[key1])

        return b

    def friends_of(self, panda):
        if (not self.has_panda(panda)):
            return False

        friends_list = []
        friends_dict = self.network[panda.__hash__()]
        for friend_key in friends_dict:
            # exclude panda from the friends list
            if (friend_key == panda.__hash__()):
                continue

            friends_list.append(friends_dict[friend_key])

        return friends_list
