import helpers as h
import building as b
import antenna as a

class Grid:
    width = 0
    height = 0
    no_buildings = 0
    buildings = []
    no_antennas_available = 0
    antennas = []
    reward_assigned = 0
        
    def __init__(self, file):
        get_data_from_file(self,file)
        
    def set_width(self, width):
        self.width = int(width)

    def set_height(self, height):
        self.height = int(height)
        
    def set_no_buildings(self, no_buildings):
        self.no_buildings = int(no_buildings)
        
    def set_building(self, building):
        self.buildings.append(building)
        
    def set_no_antennas_available(self, no_antennas_available):
        self.no_antennas_available = int(no_antennas_available)
        
    def set_antenna(self, antenna):
        self.antennas.append(antenna)
        
    def set_reward_assigned(self, reward_assigned):
        self.reward_assigned = int(reward_assigned)
        
def get_data_from_file(self, input_path_file):
    row_no = 0
    building_ctr = 0
    antennas_ctr = 0
    with open(input_path_file) as input_file:
        for line in input_file:
            line_without_comments = line.split('#', 1)[0]
            values = line_without_comments.split()
            if len(values) == 0:
                continue
            
            if(row_no == 0):
                [width, height] = values
                self.set_width(width)
                self.set_height(height)
                
            elif(row_no == 1):
                [no_of_buildings, available_antennas, reward] = values
                self.set_no_antennas_available(available_antennas)
                self.set_reward_assigned(reward)
                self.set_no_buildings(no_of_buildings)
                
            elif(row_no > 1 and building_ctr < self.no_buildings):
                [x, y, latency_weight, connection_speed_weight] = values
                self.set_building(b.Building(x, y, latency_weight, connection_speed_weight))
                building_ctr += 1
                
            elif(antennas_ctr < self.no_antennas_available):
                [range, connection_speed] = values
                self.set_antenna(a.Antenna(range, connection_speed))
                antennas_ctr += 1
                
            row_no += 1 