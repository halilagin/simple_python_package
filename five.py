from kube.kube_monitor import PodMonitor, SystemMonitor






if __name__=="__main__":   
    pod_monitor = PodMonitor()
    system_monitor = SystemMonitor()
    print (pod_monitor.b, system_monitor.a)
