# the is the template of CSV reader, the reading flow based on the sequence of rows,

# import numpy as np
# import pandas as pd
def __init__(self):
    """ YOUR CODE HERE. """
    self.plant_type = ""
    self.group_number = 0
    self.x_coordinate = 0.0
    self.y_coordinate = 0.0
    self.z_coordinate = 0.0
    self.init_plant_date = (0, 0, 0)

# df_test = pd.read_csv('test.csv')

def read_csv(self, path_file):
    """ YOUR CODE HERE. """
    file = open(path_file, "r")
    content = file.read()
    # Parse content by lines
    lines_list = content.splitlines()
    # Parse lines by whitespace delimiter
    for line in lines_list:
        line.split()

    # Parse lines by the headings of lines
    for line in lines_list:
        if line != lines_list[0]:
            plant_type = line[0]
            group_number = line[1]
            x_coordinate = line[2]
            y_coordinate = line[3]
            z_coordinate = line[4]
            init_plant_date = line[5]
    # save variables in current instance of class
    self.plant_type = plant_type
    self.group_number = group_number
    self.x_coordinate = x_coordinate
    self.y_coordinate = y_coordinate
    self.z_coordinate = z_coordinate
    self.init_plant_date = init_plant_date
    # print(df_test)