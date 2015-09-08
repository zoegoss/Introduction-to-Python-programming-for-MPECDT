import pylab
import numpy as np

tide_file = open("../data/2012AVO.txt", "r")

# We know from inspecting the file that the first 11 lines are just
# header information so lets just skip those lines.
for i in range(11):
    line = tide_file.readline()

# Initialise an empty list to store the elevation
elevation = []
days = []

# Now we start reading the interesting data
n = 0
while True:  # This will keep looping until we break out.
    # Here we use a try/except block to try to read the data as normal
    # and to break out if unsuccessful - ie when we reach the end of the file.
    try:
        # Read the next line
        line = tide_file.readline()

        # Split this line into words.
        words = line.split()

        # If we do not have 5 words then it must be blank lines at the end of the file.
        if len(words) != 5:
            break
    except:
        # If we failed to read a line then we must have got to the end.
        break

    n += 1  # Count number of data points

    try:
        # The elevation data is on the 4th column. However, the BODC
        # appends a "M" when a value is improbable and an "N" when
        # data is missing (maybe a ship dumped into it during rough weather!)
        # Therefore, we put this conversion from a string into a float in a
        # try/except block.
        level = float(words[3])
        elevation.append(level)

        # There is a measurement every quarter hour.
        days.append(n*0.25/24)
    except:
        continue

# For plotting lets convert the list to a NumPy array.
elevation = np.array(elevation)
days = np.array(days)

pylab.plot(days, elevation)
pylab.xlabel("Days")
pylab.ylabel("Elevation (meters)")
pylab.show()
