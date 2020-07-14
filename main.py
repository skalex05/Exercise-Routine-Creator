import pickle
import time
import random

class Ex:
    def __init__(self,name,reps = 0,time_ = 0,rest = 0):
        self.name = name
        self.baseReps = reps
        self.reps = reps
        self.baseTime = time_
        self.time = time_
        self.baseRest = rest
        self.rest = rest
    def changeScale(self,scale):
        self.reps = self.baseReps * scale
        self.time = self.baseTime * scale
        self.rest = int(self.baseRest / scale)


exercises = [
    Ex("situps",10,0,60),
    Ex("pressups",5,0,60),
    Ex("running on the spot",0,10,30),
    Ex("squats",5,0,60)
    ]

def CountDown(secs):
    for i in range(int(secs)):
        print(f"{secs-i}!")
        time.sleep(1)
    print("GO!")

class Session:
    def __init__(self):
        self.difficulty = 3
        self.scale = 3
        self.routine = []
    def createRoutine(self,prev = None):
        if prev:
            length = len(prev.routine)
            if prev.difficulty == 5:
                length -= 3
                scale - 1
                if length < 5:length = 5
            elif prev.difficulty <= 3:
                self.scale += 4 - prev.difficulty
                length += 2 * (3 - prev.difficulty)
            for i in range(length):
                self.routine.append(random.choice(exercises))
        else:
            for i in range(4):
                self.routine.append(random.choice(exercises))
    def run(self):
        print(f"Welcome to session #{len(pastSessions)+1}!")
        for exercise in self.routine:
            exercise.changeScale(self.scale)
            if exercise.reps == 0 and exercise.time != 0:
                print(f"You have to do {exercise.name} for {exercise.time} seconds!")
                CountDown(5)
                time.sleep(exercise.time)
                print("Times up!")
                print(f"You've now got a {exercise.rest} second rest!")
                time.sleep(exercise.rest)
            else:
                print(f"You have to do {exercise.reps} reps of {exercise.name}")
                input("Press enter when you are complete!\n")
                print(f"You've now got a {exercise.rest} second rest!")
                time.sleep(exercise.rest)
        dif = -1
        while not dif >= 1 or not dif <= 5:
            try:
                dif = int(input("On a scale of 1-5, 1 being very easy and 5 being very hard, how dificult was that session?\n"))
            except:
                pass
        self.dificulty = dif
        pastSessions.append(self)

try:
    pastSessions = pickle.load(open("Sessions.dat","rb"))
except Exception as e:
    pass

while True:
    session = Session()
    if pastSessions == []:
        session.createRoutine()
    else:
        session.createRoutine(pastSessions[-1])
    session.run()
    pickle.dump(pastSessions,open("Sessions.dat","wb"))
    if "n" in input("Continue? "):
        break
