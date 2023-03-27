from abc import abstractmethod


class Environment(object):

    @abstractmethod
    def __init__(self, n):
        self.n = n
        self.rooms = [Room("Room " + str(i), 'dirty') for i in range(1, n+1)]

    def executeStep(self, n=1):
        raise NotImplementedError('action must be defined!')

    def executeAll(self):
        raise NotImplementedError('action must be defined!')

    def delay(self, n=100):
        self.delay = n


class NRoomVaccumCleanerEnvironment(Environment):
    def __init__(self, agent, nRooms=2):
        super().__init__(nRooms)
        self.agent = agent
        self.currentRoom = self.rooms[0]
        self.delay = 1000
        self.step = 1
        self.action = ""
        self.score = 0

    def executeStep(self, n=1):
        for _ in range(0, n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res
            if res == 'clean':
                self.currentRoom.status = 'clean'
                self.score += 25
            elif res == 'right':
                idx = (self.rooms.index(self.currentRoom) + 1) % self.n
                self.currentRoom = self.rooms[idx]
                self.score -= 1
            else:
                idx = (self.rooms.index(self.currentRoom) - 1 + self.n) % self.n
                self.currentRoom = self.rooms[idx]
                self.score -= 1

            if self.currentRoom.status == 'dirty':
                self.score -= 10
            self.displayScore()
            self.displayAction()
            self.step += 1

    def executeAll(self):
        raise NotImplementedError('action must be defined!')

    def displayPerception(self):
        print("Perception at step %d is [%s,%s]" % (
            self.step, self.currentRoom.status, self.currentRoom.location))

    def displayAction(self):
        print(
            "------- Action taken at step %d is [%s]" % (self.step, self.action))

    def displayScore(self):
        print(
            "------- Score taken at step %d is %d" % (self.step, self.score))


class Room:
    def __init__(self, location, status="dirty"):
        self.location = location
        self.status = status


class Agent(object):
    @abstractmethod
    def __init__(self): pass

    @abstractmethod
    def sense(self, environment):
        pass

    @abstractmethod
    def act(self):
        pass


class VaccumAgent(Agent):

    def __init__(self):
        pass

    def sense(self, env):
        self.environment = env

    def act(self):
        if self.environment.currentRoom.status == 'dirty':
            return 'clean'
        if self.environment.currentRoom.location == str(self.environment.n):
            return 'left'
        return 'right'


if __name__ == '__main__':
    vcagent = VaccumAgent()
    env = NRoomVaccumCleanerEnvironment(vcagent, 10)
    env.executeStep(50)
