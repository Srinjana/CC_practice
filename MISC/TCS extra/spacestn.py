# Space Station
# India is a country with a number of cities, some of which have space stations. Cities are numbered consecutively and each has a road of 1km length connecting it to the next city. It is not a circular route, so the first city doesn’t connect with the last city. Determine the maximum distance from any city to its nearest space station.

# Function Description
# It should return an integer that represents the maximum distance any city is from a space station.
# SpaceStations has the following parameter(s):

# n: the number of cities
# c: an integer array that contains the indices of cities with a space station, 1-based indexing
# Input Format
# The first line consists of two space-separated integers, n and m.
# The second line contains m space-separated integers, the indices of each city having a space-station. These values are unordered and unique.
# Output Format
# Print an integer denoting the maximum distance that an astronaut in a India city would need to travel to reach the nearest space station.

# Sample Input
# 5 2
# 0 4
# Sample Output
# 2

def findStations(n, stations):
    max_dist = max(stations[0], n-1 - stations[-1])

    for i in range(len(stations)-1):
        max_dist = max((stations[i+1]-stations[i])//2, max_dist)

    return max_dist


# Driver code
n, m = map(int, input().split())
spacestn = [int(i) for i in input().split()][:m]
spacestn.sort()
result = findStations(n, spacestn)
print(result)
