 # -*- coding:utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import *
import PIL
from PIL import ImageTk, Image


mouse_person = "个性柔和，为个坦诚，单纯，具有敏悦的直观，以感觉来判断事物的能力强，属性急、急功型、虚荣心强，常因异性之事而失败，经济、财运佳。重视感情、有很大的志向、善理财、聪明、 精力充沛、一丝不苟、善于社交、幽默。富幻想力，很会利用机会，爽朗活泼，讨人喜爱， 女性特別喜爱干净，会将家务整理得有条不紊。"
mouse_peoty = "被视为机警应变，善处逆境，子孙繁衍，家业兴旺的象征。有生生不息，繁盛不衰之吉祥寓意"

Cattle_person = "沉默寡言，为人正直、纯朴、不愿伪装表面，富于耐性，勤劳，努力坚毅的习惯，思考力强，常坚持已见，易失去益友，富于同情心，有老大气概，做事很精细，脚踏实地、行动缓慢、体格强壮、毅力强、自我牺牲、晚年将鸿图大展。女性较缺乏娇柔，如果能意认到自己的不足，改变一下拘谨冷漠的态度表现自已则在感情上亦能称心如意。"
Cattle_peoty = "被视为勤奋朴实，诚挚忠厚，忍辱负重，勇武倔强的象征。有勤劳致富，风调雨顺之吉祥寓意。"

tiger_person = "讲义理，男性外刚而内柔，女性则外柔而内刚，具有组织的才能，富于发明，革命性的开拓精神，热心公益，就女性而言，是个不让须眉型。喜冒险逞强，越挫越猛，雄心万丈，对自己充满信心。肖虎者外表不怒而威，深具自信，属领导型人物，性格刚毅顽强永不低头，凡事不完成绝不甘休，凡领导之职务皆可适任。一言九鼎说到做到，绝不反悔。"
tiger_peoty = "被视为威武勇猛，豪爽正义，文彩华美，气宇轩昂的象征。有辟邪降魅，四方安康之吉祥寓意。"

rabbit_person = "为人乐观、快活、不愿过拘束的生活，追求理想而前进，但因实践能力薄弱，故事多不成，凡有新流行，就是走在尖端，防卫观念非常敏锐。有语言天才与犀利的口才，颇受人欢迎。善交际为人和气，话题丰富谈笑风生，风度翩翩，处事谨慎。厌恶与人争执，带有能化敵为友的柔和气质。  Ｏ型血的兔豪放有胆，作风一但显露出来就变得勇敢果决。"
rabbit_peoty = "被视为温柔文静，纯洁高雅，机智灵敏，忠厚善良的象征。有自然超脱，长生不老之吉祥寓意。"

long_person = "人品高尚，刚毅，有强烈的向上心，属聪明才智型，富于热情，缺乏思考，耐心，事常半途而废，表面虽冷，其实内心有极强的仁侠骨气，亲切而处处为人着想。有强壮的体魄，精力充沛活力， 朝气勃勃，有高尚的理想，富罗曼蒂克气氛，是爱面子派头的人。女性豪爽热情慷慨，善解人意，是一般男性喜爱的对象。 属龙者象征权势，天之骄子得天独厚，他的智慧过人胆识夠，才气足，慷慨大方，神气活现气轩昂。"
long_peoty = "被视为尊贵神圣，志趣高远，能屈能伸，通达旷放的象征。有惩邪镇恶，国泰民安之吉祥寓意。"

snake_person = "具有周蜜的思考力，立定志愿后必勇往迈进，表面虽坦诚，其实是神经质，猜疑心强的人，智能高，研究心强，热心探索未知的世界，具有审美感，是个艺术天才。爱得深且专一，无法容忍对方的负心。 有神秘浪漫斯文外表与熟练处世态度，风度翩翩善于辞令很会钻营。天生感受性及知性很强，对別人卻有善意关怀的应变力强。"
snake_peoty = "被视为美丽多姿，痴情重义，豁达大度，灵活应变的象征。有以柔克刚，百折不挠之吉祥寓意。"

horse_person = "为人豪爽、活泼、直感力，推断力强，头脑灵活、机警迅速，对任何事都很坦率，正直，善于口才，好辩、对事物的好恶差距大，英雄主义很重，常替人打抱不平。很容易走极端，是个性急、任性的人。演讲很动听且有领导群众能力，由于领悟力强，往往別人还没发言他就知导对方的思想和动向。肖马颇讲究衣着服饰的华丽，老爱在镜子前反覆整容。最不善于理财，往往只知开源而不懂节流。"
horse_peoty = "被视为矫健雄伟，忠实诚信，傲岸不羁，勇敢坚定的象征。有勇往直前，生命不息之吉祥寓意。"

sheep_person = "柔和而稳重，有深重的人情味，重仁义的好人，具有细腻的思考力，有毅力，可得一技之长，表面柔和而内心却是坚持已见，反抗精神强的人，防卫本能极优。凡事考虑周到，对四周事务处理妥当，有进取心， 善于交际，个性温柔具捨已成仁胸怀。 跪乳羔羊，一生孝顺，做事忍耐力强，前进不懈。 懂得节俭，待人亲切，热爱大自然，有高贵大方的仪态。 羊年生的女性心地善良喜欢照顾別人，通常是位身材勻称五官端正的美人。"
sheep_peoty = "被视为温文善良，仁慈和睦，顺天随人，纯洁高尚的象征。有丰年富庶，和气生财之吉祥寓意。"

monkey_person = "幽默、机智、活泼、所以多方面的才能常超越人群、人缘好、但重名利，独占欲强，处事敏捷，自尊心强，手灵活，善于摹仿，开放性而宽厚。社交手腕高明善解人意，很快与人打成一片，但不喜欢被人控制，喜爱追求新鲜事务。求知欲很强，记忆力超人，头脑灵活很有创造力。猴年生的男性精力充沛身体健壮，常表现达观机智勇敢，对环境变化有很强的适应能力生性顽强不服输，拥有多项才能而能居主导地位。"
monkey_peoty = "被视为自由敏捷，聪明灵巧，智勇双全，重情好义的象征。有驱魔降妖，快乐怡年之吉祥寓意。"

chik_person = "表现力强，能注意到事务的细节为人温和、谦虚而谨慎、有强烈的经济观念，但虚荣心强、爱享受、喜派头，走流行、对异性的诱惑常无法克制。坦白活跃，勇敢风趣，机智多谋，善于辩论又具说服力，有现代新潮派的大志向，脑筋转动很快。 性急，喜欢打扮自己，善于交际，有贵人相助，有恒心和毅力如鸡司晨一样有信心。 对色彩感觉有独到之处。"
chik_peoty = "被视为勇武好斗，锐意进取，化解百毒，平安祥瑞的象征。有家园安定，夫妇和谐之吉祥寓意。"

dog_person = "为人正直、守规矩、有责任感，对上司、长辈敬重，服从，工作认真，自我观念极浓，缺乏通融性，发表力，所以常失去许多美好的事物，防卫意识强。重人情道义，做事全力以赴。生性纯朴正直，诚实友善，为人忠实可靠。直觉锐利，为人忠诚，颇爱主持公道，很受人严敬。感情上，爱上对方不会轻易变心，宁可自己吃亏也不愿给人添麻烦，不会为自己利益做出违背道义的事。"
dog_peoty = "被视为机智聪慧，赤诚勇敢，尽职守信，舍身重义的象征。有四季康泰，和平安宁之吉祥寓意。"

pig_person = "崇尚义理，人情，纯情，好睡重眠心地善良，对人没有猜疑而常受骗上当。Ｏ型猪年生的人思想单纯天真，不会与人斤斤计较，肖猪的人绝对不是詐欺和出賣朋友的人， 坦诚真意很能容忍。乐天主义，不需要过份操劳便可维持生计。 智力丰富求知欲强，慷慨大方，直接了当。 女性非常着重家庭，有计划地安排家务。"
pig_peoty = "被视为豪放谦和，朴拙憨厚，随遇而安，与世无争的象征。有安居乐业，丰衣足食之吉祥寓意"

option_en = ['mouse','Cattle','tiger','rabbit','long','snake','horse','sheep','monkey','chik','dog','pig'] 



def annimal_process(event):
    annimal_type = clicked.get()
    # print(planet_type)
    kkey = option.index(annimal_type)
    # print(option_en[kkey])

    pic_path = option_en[kkey]+".jpg"
    print(pic_path)
                                          
    image = Image.open(pic_path)
    basewidth = 400

    canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717',bd=0, highlightthickness=0, relief='ridge')
    wpercent = (basewidth / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(wpercent)))
    image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    item4 = canvas2.create_image(225, 210, image=photo)

    canvas2.place(relx=0.05, rely=0.1, relheight=0.6, relwidth=0.5)

    for widget in desc_frame.winfo_children():
        widget.destroy()

    for widget in fact_frame.winfo_children():
        widget.destroy()
    text_temp = '%s_person'%option_en[kkey]
    text_temp1 = '%s_peoty'%option_en[kkey]
    text3 = eval(text_temp)
    text4 = eval(text_temp1)

    earth_label = tk.Label(desc_frame, text=text3,justify="left",wraplength = 300, font=('Gadugi', 14), bg='#121212', fg='white')
    earth_label.pack()

    earth_fact = tk.Label(fact_frame, text=text4,justify="center",wraplength = 800, font=('Monotype Corsiva', 16), bg='#121212', fg='white')
    earth_fact.pack(side='left')

    item4.pack()




#  主程序

HEIGHT = 700
WIDTH = 900

root = tk.Tk()
root.title('属相分析仪')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#171717')
canvas.pack()

desc_frame_name = tk.Frame(root, bg='#F8F8FF')             
# relx/y  表示偏移量    relheight/relwidth表示大小
desc_frame_name.place(relx=0.6, rely=0.05, relheight=0.05, relwidth=0.35)



desc_frame = tk.Frame(root, bg='#121212')             
# relx/y  表示偏移量    relheight/relwidth表示大小
desc_frame.place(relx=0.6, rely=0.1, relheight=0.6, relwidth=0.35)

fact_frame_name = tk.Frame(root, bg='#F8F8FF')
fact_frame_name.place(relx=0.05, rely=0.74, relheight=0.05, relwidth=0.9)


fact_frame = tk.Frame(root, bg='#121212')
fact_frame.place(relx=0.05, rely=0.79, relheight=0.2, relwidth=0.9)

option = ['鼠','牛','虎','兔','龙','蛇','马','羊','猴','鸡','狗','猪'] 
clicked = StringVar()
clicked.set(option[0])  # 设置默认值
drop = OptionMenu(root, clicked, *option)
drop.place(relx=0.3, rely=0.01, relheight=0.05, relwidth=0.1)


planet_type = clicked.get()  #获取枚举
button = tk.Button(canvas, text='进行分析')
button.bind('<Button-1>', annimal_process) # 案件函数的绑定
button.place(relx=0.4, rely=0.01, relheight=0.05, relwidth=0.1)


text2 = '关于属相的寓意将在这里展示'

text = """
欢迎来到属相性格分析仪


请输入您的属相进行分析

"""

initial_label3 = tk.Label(desc_frame_name, text="性格分析",justify="center" ,font=('Gadugi', 20), bg='#F8F8FF', fg='red')
initial_label3.pack(side='top')


initial_label2 = tk.Label(fact_frame, text=text2, font=('Monotype Corsiva', 18), bg='#121212', fg='white')
initial_label2.pack(side='left')

initial_label4 = tk.Label(fact_frame_name, text="寓意", justify="center",wraplength = 300,font=('Gadugi', 20), bg='#F8F8FF', fg='red')
initial_label4.pack()

initial_label = tk.Label(desc_frame, text=text, justify="center",wraplength = 300,font=('Gadugi', 16), bg='#121212', fg='white')
initial_label.pack()

root.mainloop() 