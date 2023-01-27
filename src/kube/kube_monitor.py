



class SystemMonitor():

    def __init__(self):
        pass
        print("System Monitor constrcutor")
        self.a="sys"


class PodMonitor():

    def __init__(self):
        print("PodMonitor constrcutor")
        self.b="pod"
    



if __name__=="__main__":
    sm = SystemMonitor()
    print (sm.a)
