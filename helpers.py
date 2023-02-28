import grid

def get_data_from_file(input_path_file):
    row_no = 0
    with open(input_path_file) as input_file:
        for line in input_file:
            line_without_comments = line.split('#', 1)[0]
            values = line_without_comments.split()
            
            if(row_no == 0):
                [width, height] = values
                
            elif(row_no == 1):
                [no_of_buildings, available_antennas, reward] = values
            row_no += 1
            
    return []