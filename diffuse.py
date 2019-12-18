import random

maxstep=10000
npart=500
perc=0
steps=[(1,0),(-1,0),(0,1),(0,-1)]
x,y=0,0
side=21 #Can be 21,31,41,51 long as its an odd number

density=float(input("Enter a value for density between 0.0-1.0:"))
grid=[[0 for x in range(side)]for y in range(side)]

#Loop over all cells in grid and set to 1 with a probability given by density
while x<len(grid):
    while y<len(grid[x]):
        grid[x][y]=random.choices([0,1],[1.0-density,density],k=1)[0]
        y+=1
    x+=1
    y=0
for ipart in range(npart): #particle will start at the center
    x,y=side//2,side//2 #random walk/convert while loop and loops over max steps

for isteps in range(maxstep):#moves the particle randomly
    sx,sy=random.choice(steps) #if value is checked ==1 it skips iteration

    if grid[x+sx][y+sy]==1:
        continue
    else:
        x+=sx
        y+=sy
#goes to the next particle if the particle reaches the edge of the system increment of perc +1

    if x<=0 or y<=0 or x==side-1 or y==side-1:
        perc+=1
        break

print("The Probability of the Particle Percolating out of the system is {}".format(perc/npart))
