import time
import random
from os import system
import os
import copy

class snakeLadder():

#   ------------------------------------INITIALIZE BOARD AND PLAYERS----------------------------------------------
    def __init__(self):
        self.player_names=[]
        self.No_of_player=0
        self.player_pos={}

        title="SNAKE AND LADDER"

        print("\n")
        for i in range(70):
            print(" "*i,end="")
            print("/\/\/\/\/\/\/\/\/\/\/*~",end="")
            time.sleep(0.01)
            print("\r",end="")

        print("\n\n\n")
        print("\t\t\t\t\t\t\t\t\t",end="")
        for i in title:
            print(i,end="",flush=True)
            time.sleep(0.05)

        input("\n\n\t\t\t\t\t\t\t\t   READY TO PLAY PRESS ENTER!!!")

        while self.No_of_player<2 or self.No_of_player>5:
            self.No_of_player=int(input("Enter Number of Players (max:5): "))
            if(self.No_of_player>5 or self.No_of_player<2):
                print("---------------Please Enter value Between 2 to 5 ------------------")

        for i in range(self.No_of_player):
            p_name=input(f"Enter Player {i+1} Name: ")
            while p_name in self.player_names:
                print("Player Names Must Different!!!!")
                p_name=input(f"Enter Player {i+1} Name: ")
            self.player_names.append(p_name)

        for i in self.player_names:
            self.player_pos[i[0]+i[-1]]=0



# -----------------------------Default Board---------------------------------------------
    def default_board(self):
        self.No_of_snakes=12
        self.No_of_ladder=8
        self.snake_position=[15,22,36,48,52,57,64,68,84,90,94,98]
        self.ladder_position=[8,19,23,35,40,52,73,77]



# -----------------------------CUSTOMIZE BOARD--------------------------------------------
    def custom_board(self):
        self.No_of_snakes=0
        self.No_of_ladder=0
        self.ladder_position=[]
        self.snake_position=[]

        #---------------------------------Custom Snakes----------------------------------------

        while self.No_of_snakes<1 or self.No_of_snakes>20:
            self.No_of_snakes=int(input("Enter Number of Snakes you want: "))
            if self.No_of_snakes<1 or self.No_of_snakes>20:
                print("---------------Please Enter value Between 1 to 20 ------------------")
                
        for i in range(self.No_of_snakes):
            pos=int(input(f"Enter Snake {i+1} Position: "))
            while pos>99 or pos<10 or (pos in self.snake_position):
                print("---------------Please Enter value Between 10 to 99 and different One!!------------------")
                pos=int(input(f"Enter Snake {i+1} Position: "))
            self.snake_position.append(pos)


        #  -------------------------------Custom Ladders--------------------------------------

        while self.No_of_ladder<1 or self.No_of_ladder>20:
            self.No_of_ladder=int(input("Enter Number of Ladders You Want: "))
            if self.No_of_ladder<1 or self.No_of_ladder>20:
                print("---------------Please Enter value Between 1 to 20 ------------------")

        for i in range(self.No_of_ladder):
            pos_l=int(input(f"Enter Ladder {i+1} Position: "))
            while pos_l>80 or pos_l<5 or (pos_l in self.ladder_position):
                print("---------------Please Enter value Between 5 to 80 and different One!!------------------")
                pos_l=int(input(f"Enter Ladder {i+1} Position: "))
            
            while pos_l in self.snake_position:
                print("Snake and Ladder Cannot Be On same Position!!!!!")
                pos_l=int(input(f"Enter Ladder {i+1} Position: "))

            self.ladder_position.append(pos_l)




#   --------------------------------------Create Board--------------------------------------------


    def create_board(self):
        system("cls")
        for i in range(10,0,-1):
            loc=0
            raw_line=[]
            for j in range(0,10):
                if(i%2==0):
                    loc=(i*10)-j
                    if loc in self.snake_position:
                        print(f"-{(i*10)-j}-$-{int(loc/2)}--".center(13),end="")
                    elif loc in self.ladder_position:
                        print(f"-{(i*10)-j}-#-{loc+10}--".center(13),end="")
                    else:
                        print(f"----{(i*10)-j}----".center(13),end="")
                    raw_line.append(loc)
                    
                else:
                    loc=((i-1)*10)+j+1
                    if loc in self.snake_position:
                        print(f"-{((i-1)*10)+j+1}-$-{int(loc/2)}--".center(13),end="")
                    elif loc in self.ladder_position:
                        print(f"-{((i-1)*10)+j+1}-#-{loc+10}--".center(13),end="")
                    else:
                        print(f"----{((i-1)*10)+j+1}----".center(13),end="")

                    raw_line.append(loc)
            print(end="\n")

            for i in range(len(raw_line)):
                pla_combine=""
                for k,v in self.player_pos.items():
                    if raw_line[i]==v:
                        pla_combine=pla_combine+"^"+k

                if pla_combine=="":
                    print("         ".center(13),end="")
                else:
                    print(f"**[{pla_combine}]**".center(13),end="")
                    
            print("\n")



#   -------------------------------------------ROLL DICE------------------------------------------------

    def roll_dice(self):
        input("!!!!! Press Enter To Roll Dice !!!!!")
        
        dice_val=random.randint(1,6)
        if(dice_val==1):
            print((" ________\n|        |\n|   *    |\n|________|"))
        elif(dice_val==2):
            print((" ________\n|        |\n|  *  *  |\n|________|"))
        elif(dice_val==3):
            print((" ________\n|        |\n| * * *  |\n|________|"))
        elif(dice_val==4):
            print((" ________\n|  *  *  |\n|        |\n|__*__*__|"))
        elif(dice_val==5):
            print((" ________\n|  *  *  |\n|   *    |\n|__*__*__|"))
        elif(dice_val==6):
            print((" ________\n|  *  *  |\n|  *  *  |\n|__*__*__|"))
        return dice_val



# -----------------------------------------------BOARD Refresh-------------------------------------------
    def refresh_board(self):
        input("\nPress Enter To Move Pieces!!!")
        self.create_board()
        


#  -----------------------------------------------Main Play Function--------------------------------------
    def play(self):
        ack=0
        turn_open_dict=copy.deepcopy(self.player_pos)
        while ack==0:
            for i in self.player_names:
                print(f"{i}'s turn:")
                num=self.roll_dice()
                if self.player_pos[i[0]+i[-1]]==0:
                    if num==6:
                        print("Wow Piece Opened!!!")
                        turn_open_dict[i[0]+i[-1]]=1
                    else:
                        print("\nBring 6 to Open Piece!!!")

                    self.refresh_board()


                if turn_open_dict[i[0]+i[-1]]==1:
                    test_pos=self.player_pos[i[0]+i[-1]]+num

                    if test_pos>100:
                        self.refresh_board()
                        continue
                        
                    if test_pos==100:
                        self.player_pos[i[0]+i[-1]]=test_pos
                        self.refresh_board()
                        print(f"\n\n________________________________________________________________________________________________")
                        print(f"_____________________________________Hurrey!!! {i} Wins_____________________________________")
                        input()
                        os._exit(1)
                        
                    if test_pos in self.snake_position:
                        print("\nOhh No! You Got A Snake Bite!!! ")
                        test_pos=int(test_pos/2)
                        self.player_pos[i[0]+i[-1]]=test_pos
                    elif test_pos in self.ladder_position:
                        print("\nNice! You Found A Ladder!!! ")
                        test_pos=test_pos+10
                        self.player_pos[i[0]+i[-1]]=test_pos
                    else:
                        self.player_pos[i[0]+i[-1]]=test_pos
                    self.refresh_board()



# ------------------------------------------Program Starts From Here----------------------------------------------------


if __name__=="__main__":
    obj=snakeLadder()
    
    while True:
        ack=int(input(("\n\nChoose:\n1) Play Default Board \n2) Customize Board \n:  ")))

        if(ack==1):
            obj.default_board()
            break
        elif(ack==2):
            obj.custom_board()
            break
        else:
            print("Please Choose Valid Option!!")


    input(("\n\n\t\t\t\t\t\t\t\t   Let's Begin Press Enter!!!"))

    obj.create_board()
    obj.play()