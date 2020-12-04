import random
import time
import pygame
import copy 
from PIL import Image
import copy 
import os
from random import randint


#  初始化
pic_size = 600  # 图片大小
# 图片路径
path = "G:/Desktopsnew/小编/国庆拼图/pic_bg"
# 请输入阶数
num = input("请输入阶数")
while(pic_size % (int(num) )!= 0):
    num = input("输入阶数不符合，请重新输入")


## 获取图片片目录
def file_name(file_dir):
    roots = []
    dirses = []
    fileses = []
    for root, dirs, files in os.walk(file_dir):
        roots.append(root)
        dirses.append(dirs)
        fileses.append(files)
    return roots,dirses,fileses
roots,dirses,fileses = file_name(path)

#   序列长度  print(fileses[0])
# 获取图像序列长度list 进行随机选择

ran = randint(0,len(fileses[0])-1)

# 图片路径
pic_path = os.path.join(path,fileses[0][ran])

# 对图片进行 resize
img = Image.open(pic_path)
# img.show()

image_size = img.resize((600, 600),Image.ANTIALIAS)
image_size.save("temp.jpg")


# 初始化
pygame.init()
# 窗口标题screen
pygame.display.set_caption('中秋国庆系列拼图游戏')
# 窗口大小
screen = pygame.display.set_mode((1200, 600))





# 参数初始化

pic_fenge = int(num)   # 阶数
pix_fenge = pic_size /pic_fenge   # 像素
pic_huidu = pic_fenge * pic_fenge - 1  # 空白图像位置


#   绘制地图
#  其中  init_Map  表示初始化的地图 之后会被打乱
#   end_map 是
init_Map = []

for i in range(pic_fenge):
    b = []
    for j in range(pic_fenge):
        b.append(i*pic_fenge+j)
    init_Map.append(b)

end_Map = copy.deepcopy(init_Map) 






#游戏的单击事件
# y行   x 列
def click(x, y, map):
    # 如果点击了空白  下面的图片 上下图片互换
    if y - 1 >= 0 and map[y - 1][x] == pic_huidu:
        map[y][x], map[y - 1][x] = map[y - 1][x], map[y][x]
    # 如果点击了空白  上面的图片 上下图片互换    
    elif y + 1 <= pic_fenge-1 and map[y + 1][x] == pic_huidu:
        map[y][x], map[y + 1][x] = map[y + 1][x], map[y][x]
    # 如果点击了空白  右面的图片 左右图片互换      
    elif x - 1 >= 0 and map[y][x - 1] == pic_huidu:
        map[y][x], map[y][x - 1] = map[y][x - 1], map[y][x]
    # 如果点击了空白  左面的图片 左右图片互换   
    elif x + 1 <= pic_fenge-1 and map[y][x + 1] == pic_huidu:
        map[y][x], map[y][x + 1] = map[y][x + 1], map[y][x]
 

#  采用 点击的方式打乱地图
def randMap(map):
    for i in range(1000):
        x = random.randint(0, pic_fenge-1 )
        y = random.randint(0, pic_fenge-1 )
        click(x, y, map)
 

# 加载图片
img = pygame.image.load("temp.jpg")

#随机地图
randMap(init_Map)

#游戏主循环
while True:
    #延时32毫秒,相当于FPS=30
    pygame.time.delay(32)
    # pygame.event.get() 从队列中获取事件
    for event in pygame.event.get():
        # 窗口的关闭事件
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:      #鼠标单击事件
            if pygame.mouse.get_pressed() == (1, 0, 0):     #鼠标左键按下
                mx, my = pygame.mouse.get_pos()     #获得当前鼠标坐标
                if mx<pic_size and my <pic_size:      #判断鼠标是否在操作范围内
                    x=int(mx/pix_fenge)       #计算鼠标点到了哪个图块
                    y=int(my/pix_fenge)
                    click(x,y,init_Map)   #调用单击事件
                    if init_Map==end_Map:  #如果当前地图情况和胜利情况相同,就print胜利
                        print("恭喜您完成了拼图")
                        break
    
    
    #背景色填充成 朱红色
    screen.fill((240,65,85))
    #绘图
    for y in range(pic_fenge):
        for x in range(pic_fenge):
            i = init_Map[y][x]
            if i == pic_huidu:      #空白号图块不用绘制
                continue
            dx = (i % pic_fenge) * pix_fenge      #计算绘图偏移量
            dy = (int(i / pic_fenge)) * pix_fenge
            screen.blit(img, (x * pix_fenge, y * pix_fenge), (dx, dy, pix_fenge, pix_fenge))
    # 画参考图片
    screen.blit(img, (600, 0))
    # 刷新界面
    pygame.display.flip()


pygame.quit ()