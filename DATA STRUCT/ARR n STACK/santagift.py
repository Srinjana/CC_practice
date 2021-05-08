# Christmas is here! Santa has already prepared the gifts for all children all around the world, however, he hasn’t picked them yet. Santa has N gifts, their sizes are given in an array, A, and he also has N boxes, their sizes are given in an array, B.
# Santa packs the gifts in the boxes in the following way:
# He tries to put the gifts inside boxes from left to right.
# He goes through the boxes from left to right until he finds the first empty box that fits the current gift(the box’s size should be larger or equal to the current gift’s size), and Santa puts the current gift in that box. Santa moves to the next gift to the right.
# You need to find the number of gifts which won’t be packed following Santa’s algorithms in packing the gifts.
# Author @Srinjana

N= int(input())
gifts = []
boxes = []
count = 0

for i in range (N):
    gifts.append(int(input()))
for i in range(N):
    boxes.append(int(input()))

for i in range(N):
    for j in range(N):
        if(gifts[i]<boxes[j]):
            count += 1
            boxes[j] = -1
            break
print(N-count)
