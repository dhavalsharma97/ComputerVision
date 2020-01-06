# Author : Dhaval Harish Sharma
# Red ID : 824654344
# Assignment 5, Question 1
# Finding area from a chain code

# Function for finding the area of the region enclosed by the chain code
def Area(ChainCode):
    # Initializing the attributes
    x, y = 0, 0
    area = 0
    coord = []
    
    # Loop for finding the coordinates from the chain code
    for direction in ChainCode:
        if direction == 0:
            y += 1
        elif direction == 1:
            x -= 1
        elif direction == 3:
            x += 1
        else:
            y -= 1
        
        if [x, y] not in coord:
            coord.append([x, y])
    
    # Finding the area of the region from the coordinates
    for i in range(len(coord) - 1):
        area += coord[i + 1][0] * coord[i][1] - coord[i][0] * coord[i + 1][1]
    area = area // 2
    
    return area

print(Area([0, 0, 3, 0, 3, 2, 3, 2, 1, 1, 2, 1]))
print(Area([0, 0, 3, 2, 2, 1]))
print(Area([0, 0, 0, 3, 3, 0, 3, 0, 3, 2, 2, 2, 1, 1, 2, 1, 2, 1]))