'''
Step.1 - Import the Module
'''
import cv2
import os
import random
from PIL import Image

'''
Step.2 - Construct the Data Structure
'''
class DINO: 
    # Constructor
    def __init__(self, img, number, clothes, hat, nostril, eyebrow, eye, mouth, teeth, jaw, armor, body, hand, bg):
        self.img = img # 圖片
        self.resize_img = self.resize() # 修改大小之後的圖片，以方便在電腦上顯示
        self.number = number # 圖片編號
        self.clothes = clothes
        self.hat = hat
        self.nostril= nostril
        self.eyebrow = eyebrow
        self.eye = eye
        self.mouth = mouth
        self.teeth = teeth
        self.jaw = jaw
        self.armor = armor
        self.body = body
        self.hand = hand
        self.bg = bg

    # Method
    def print_dinoDATA(self):
        print(f"The Dino {self.number} Data is  1. Clothes: {self.clothes}\n \
                                                2. hat: {self.hat}\n \
                                                3. nostril: {self.nostril}\n \
                                                4. eyebrow: {self.eyebrow}\n \
                                                5. eye: {self.eye}\n \
                                                6. mouth: {self.mouth}\n \
                                                7. teeth: {self.teeth}\n \
                                                8. jaw: {self.jaw}\n \
                                                9. armor: {self.armor}\n \
                                                10. body: {self.body}\n \
                                                11. hand: {self.hand}\n \
                                                12. bg: {self.bg}")

    def resize(self):
        showing_img = cv2.resize(self.img, (720, 720)) # 修改大小之後的圖片，以方便在電腦上顯示
        return showing_img

    def show_dinoIMG(self):
        # cv2.imshow("Dino Image", self.img)
        cv2.imshow("Dino Image", self.resize_img)
        cv2.waitKey()


class PART:
    def __init__(self, part, filename, img):
        self.part = part
        self.filename = filename
        self.img = img
        self.shape = self.shape_init()
        self.color = self.color_init()

    def shape_init(self):
        if "open" in self.filename:
            return "open"
        elif "closed" in self.filename:
            return "closed"
        else:
            return "None"
            
    
    def color_init(self):
        if "green" in self.filename:
            return "green"
        elif "blue" in self.filename:
            return "blue"
        elif "aqua" in self.filename:
            return "aqua"
        else:
            return "None"


class DATA:
    def __init__(self, name, numbers, quantities):
        self.name = name
        
        self.numbers = numbers # 部位編號
        self.quantities = quantities # 部位數量
        self.location = self.location_init() # 部位資料夾相對位置，string
        self.ImgBase = self.load_ImgBase() # list

    
    def location_init(self):
        location = "./part_image/" + str(self.numbers) + ". " + str(self.name) + "/"
        return location
    
    def load_ImgBase(self):
        self.ImgBase = []
        if self.name == "bg":
            folder = "./part_image/" + str(self.numbers) + ". " + str(self.name) + " (background)"
        else:
            folder = "./part_image/" + str(self.numbers) + ". " + str(self.name)

        for filename in os.listdir(folder):
            img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_UNCHANGED)
            img = cv2.resize(img, (1000, 1000))
            if img is not None:
                self.ImgBase.append(PART(self.name, filename, img))

        # for i in range(self.quantities):
        #     print(self.ImgBase[i].shape)
    
        return self.ImgBase

    def show_ImgBase(self):
        for i in range(self.quantities):
            showing_img = cv2.resize(self.ImgBase[i].img, (720, 720)) # 修改大小之後的圖片，以方便在電腦上顯示
            cv2.imshow("Dino Image", showing_img)
            cv2.waitKey()

class DataBase:
    def __init__(self, Quantities):
        self.Base = []
        self.Quantities = Quantities
    
    def show_DataBase(self):
        for i in range(self.Quantities):
            self.Base[i].print_dinoDATA()
            cv2.imshow("Dino Image", self.Base[i].resize_img)
            cv2.waitKey()

    def save_DataBase(self):
        for i in range(self.Quantities):
            cv2.imwrite("./Final/#" + str(self.Base[i].number) + ".jpg", self.Base[i].img, [cv2.IMWRITE_JPEG_QUALITY, 100])


'''
Step.3 - Declaration
'''
clothes = DATA("clothes", 1, 3)
hat = DATA("head", 2, 2)
nostril = DATA("nostril", 3, 2)
eyebrow = DATA("eyebrow", 4, 6)
eye = DATA("eye" , 5, 4)
mouth = DATA("mouth", 6, 1)
teeth = DATA("teeth", 7, 4)
jaw = DATA("jaw", 8, 6)
armor = DATA("armor", 9, 4)
body = DATA("body", 10, 3)
hand = DATA("hand", 11, 5)
bg = DATA("bg", 12, 2)


'''
Step.4 - Random Blending the Parts
''' 
Dino_DataBase = DataBase(10)
Dino_HashTable = {}

def hash_unique(HashTable):

    # now_... 是指 index，所以需要減 1
    now_clothes = random.randint(1, clothes.quantities) - 1
    now_hat = random.randint(1, hat.quantities) - 1
    now_nostril = random.randint(1, nostril.quantities) - 1
    now_jaw = random.randint(1, jaw.quantities) - 1 # 必須先固定 jaw
    now_eyebrow = random.randint(1, eyebrow.quantities) - 1
    while jaw.ImgBase[now_jaw].color != eyebrow.ImgBase[now_eyebrow].color:
        now_eyebrow = random.randint(1, eyebrow.quantities) - 1
    now_eye = random.randint(1, eye.quantities) - 1
    now_mouth = random.randint(1, mouth.quantities) - 1 # 目前嘴巴只有一種所以下面先註解掉
    # while mouth.ImgBase[now_mouth].shape != jaw.ImgBase[now_jaw].shape:
    #     now_mouth = random.randint(1, mouth.quantities) - 1
    now_teeth = random.randint(1, teeth.quantities) - 1
    while jaw.ImgBase[now_jaw].shape != teeth.ImgBase[now_teeth].shape:
        now_teeth = random.randint(1, teeth.quantities) - 1
    now_armor = random.randint(1, armor.quantities) - 1
    now_body = random.randint(1, body.quantities) - 1
    while jaw.ImgBase[now_jaw].color != body.ImgBase[now_body].color:
        now_body = random.randint(1, body.quantities) - 1
    now_hand = random.randint(1, hand.quantities) - 1
    while jaw.ImgBase[now_jaw].color != hand.ImgBase[now_hand].color:
        now_hand = random.randint(1, hand.quantities) - 1
    now_bg = random.randint(1, bg.quantities) - 1


    # hash function
    now_hash = pow(clothes.numbers, now_clothes % 11) + \
               pow(hat.numbers, now_hat % 11) + \
               pow(nostril.numbers, now_nostril % 11) + \
               pow(eyebrow.numbers, now_eyebrow % 11) + \
               pow(eye.numbers, now_eye % 11) + \
               pow(mouth.numbers, now_mouth % 11) + \
               pow(teeth.numbers, now_teeth % 7) + \
               pow(jaw.numbers, now_jaw % 7) + \
               pow(armor.numbers, now_armor % 7) + \
               pow(body.numbers, now_body % 7) + \
               pow(hand.numbers, now_hand % 7) + \
               pow(bg.numbers, now_bg % 7)

    print(now_hash)

    if HashTable.get(str(now_hash)) != None:
        now_clothes, now_hat, now_nostril, now_jaw, now_eyebrow, now_eye, now_mouth, now_teeth, now_armor, now_body, now_hand, now_bg = hash_unique(HashTable)
    else:
        HashTable[str(now_hash)] = now_hash

    return now_clothes, now_hat, now_nostril, now_jaw, now_eyebrow, now_eye, now_mouth, now_teeth, now_armor, now_body, now_hand, now_bg


def Blending(img_1, img_2):

    img1 = img_1.copy()
    img2 = img_2.copy()

    x_offset = y_offset = 0
    y1, y2 = y_offset, y_offset + img2.shape[0]
    x1, x2 = x_offset, x_offset + img2.shape[1]
    alpha_s = img2[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        img1[y1:y2, x1:x2, c] = alpha_s * img2[:, :, c] + alpha_l * img1[y1:y2, x1:x2, c]

    return img1


for i in range(Dino_DataBase.Quantities):
    # Hash
    now_clothes, now_hat, now_nostril, now_jaw, now_eyebrow, now_eye, now_mouth, now_teeth, now_armor, now_body, now_hand, now_bg = hash_unique(Dino_HashTable)

    # blending
    new_picture = []
    new_picture = Blending(bg.ImgBase[now_bg].img, hand.ImgBase[now_hand].img)
    new_picture = Blending(new_picture, body.ImgBase[now_body].img)
    new_picture = Blending(new_picture, armor.ImgBase[now_armor].img)
    new_picture = Blending(new_picture, jaw.ImgBase[now_jaw].img)
    new_picture = Blending(new_picture, teeth.ImgBase[now_teeth].img)
    new_picture = Blending(new_picture, mouth.ImgBase[now_mouth].img)
    new_picture = Blending(new_picture, eye.ImgBase[now_eye].img)
    new_picture = Blending(new_picture, eyebrow.ImgBase[now_eyebrow].img)
    new_picture = Blending(new_picture, nostril.ImgBase[now_nostril].img) 
    new_picture = Blending(new_picture, hat.ImgBase[now_hat].img)
    new_picture = Blending(new_picture, clothes.ImgBase[now_clothes].img)

    Dino_DataBase.Base.append(DINO(new_picture, i, now_clothes, now_hat, now_nostril, now_eyebrow, now_eye, now_mouth, now_teeth, now_jaw, now_armor, now_body, now_hand, now_bg))
    print(len(Dino_DataBase.Base))


'''
Step.5 - Save Image
'''
Dino_DataBase.show_DataBase()
Dino_DataBase.save_DataBase()
