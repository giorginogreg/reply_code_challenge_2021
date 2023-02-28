class Building:
    x = 0
    y = 0
    latency_weight = 0
    connection_speed_weight = 0
    
    def __init__(self, x, y, latency_weight, connection_speed_weight):
        self.x = x
        self.y = y
        self.latency_weight = latency_weight
        self.connection_speed_weight = connection_speed_weight