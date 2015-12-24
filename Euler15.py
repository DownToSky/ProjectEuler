#Author DownToSky
#Euler Problem 15

#The lattice is a n by n grid
n=20
#Finds the number of paths in i and j position from the previous i and j positions
grid=[[0]*(n+1)]*(n+1)

for i in range(n,-1,-1):
        for j in range(n,-1,-1):
            if i==n and j==n:
                grid[i][j]=1
            else:
                if i==n:
                    grid[i][j]=grid[i][j+1]
                else:
                    if j==n:
                        grid[i][j]=grid[i+1][j]
                    else:
                        grid[i][j]=grid[i+1][j]+grid[i][j+1]
print(grid[0][0])
