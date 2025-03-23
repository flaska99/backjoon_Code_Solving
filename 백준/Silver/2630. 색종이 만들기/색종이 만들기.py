import sys

def paper_cut(x, y, size) :
    global white_paper, blue_paper

    if check_paper(x, y, size):
        if paper_list[x][y] == 0 :
            white_paper += 1
        else : 
            blue_paper += 1
        return

    half = size // 2
    paper_cut(x, y, half)
    paper_cut(x + half, y, half)
    paper_cut(x, y + half, half)
    paper_cut(x + half, y + half, half)

def check_paper(x, y, size) : # 색종이를 자를수있는지 검사
    color = paper_list[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper_list[i][j] != color :
                return False
    
    return True


n = int(sys.stdin.readline())
paper_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
white_paper = 0
blue_paper = 0

paper_cut(0,0,n)
print(white_paper)
print(blue_paper)



