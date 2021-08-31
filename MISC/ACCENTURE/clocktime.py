# Mayur bought a watch in which time is displayed in 12 hour format. He wants to convert that in a 24 hour format to fill in the timesheet. Help him out to write a program for this time conversion.

# Example,

# Input – 12: 01: 11PM
# Output-12: 01: 11

# Input – 12: 01: 11AM
# Output-00: 01: 11

itime = input()

if 'AM' in itime:
    i_split = itime.replace('AM', '').split(":")
    if (i_split[0] == 12):
        i_split[0] = '00'
    res = i_split[0]+" : "+ i_split[1]+" : "+ i_split[2]
    print (res)

elif 'PM' in itime:
    i_split = itime.replace('PM', '').split(":")
    if i_split[0] != '12':
        i_split[0] = str(int(i_split[0])+12)
    res = i_split[0] +" : "+ i_split[1] +" : "+ i_split[2]
    print (res)


