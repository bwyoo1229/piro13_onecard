import random

class CardPlayer:
     def __init__(self):
         self.cardList = []  # 플레이어의 카드 덱 리스트
         self.player_card = ()  # 플레이어가 최근에 뽑은 카드 정보

     def choose_card(self, index):
         # 사용자의 덱에서 내고 싶은 카드를 선택한다.(튜플 형태)
         self.player_card = self.cardList[index - 1]

     def put_card(self, table_card):
         # choose_card의 return 값을 가져와서 카드를 낸다.
         # check_card()로 낼 수 있는 카드의 조건에 부합하지 않을시 경고문 출력 및 Boolean 값 리턴
         checking = check_card(self.player_card, table_card)
         if checking == False:
             print('낼 수 없는 카드입니다!')
             return False
         elif checking[1] == '7':
             table_card = checking  # table_card()를 그 모양이 바뀐 튜플, 즉 check_card의 return값으로 바꿈
             self.cardList.remove(self.player_card)  # 현재 플레이어 손에 있는 덱에서 사용자가 낸 카드를 remove
             print('카드모양이 바뀌었어요!')
             return table_card
         else:
             table_card = self.player_card  # 현재 타겟 카드를 사용자가 낸 카드로 업데이트
             self.cardList.remove(self.player_card)  # 사용자의 덱에서 사용자가 낸 카드를 삭제
             return table_card

     def draw_card(self):
         # 전체 카드리스트(entireCardList)에서 카드를 1장 드로우 한다.
         popped_card = entireCardList.pop()
         self.cardList.append(popped_card)

     def show_hand(self):
         # 현재 내 손에 있는 카드 리스트를 출력한다.
         for card in self.cardList:
             print(card, end=' ')

     # 내 덱에서 타겟 카드에 부합하는 카드가 있는지 알려주는 함수(가능한 카드가 있으면 True 반환, 없으면 False 반환)
     def check_draw(self, table_card):
         result = False
         for card in self.cardList:
             if table_card[0] == card[0] or table_card[1] == card[1]:
                 result = True
         return result

     # 컴퓨터가 조건에 부합하는 카드를 덱에서 뽑음
     def computer_choose(self, table_card):
         for card in self.cardList:
             if table_card[0] == card[0] or table_card[1] == card[1]:
                 self.player_card = card
                 return card


 entireCardList = [('♠', 'A'), ('♠', '2'), ('♠', '3'), ('♠', '4'), ('♠', '5'), ('♠', '6'), ('♠', '7'), ('♠', '8'),
                   ('♠', '9'), ('♠', '10'), ('♠', 'J'), ('♠', 'Q'), ('♠', 'K'), ('♥', 'A'), ('♥', '2'), ('♥', '3'),
                   ('♥', '4'), ('♥', '5'), ('♥', '6'), ('♥', '7'), ('♥', '8'), ('♥', '9'), ('♥', '10'), ('♥', 'J'),
                   ('♥', 'Q'), ('♥', 'K'), ('◆', 'A'), ('◆', '2'), ('◆', '3'), ('◆', '4'), ('◆', '5'), ('◆', '6'),
                   ('◆', '7'), ('◆', '8'), ('◆', '9'), ('◆', '10'), ('◆', 'J'), ('◆', 'Q'), ('◆', 'K'), ('♣', 'A'),
                   ('♣', '2'), ('♣', '3'), ('♣', '4'), ('♣', '5'), ('♣', '6'), ('♣', '7'), ('♣', '8'), ('♣', '9'),
                   ('♣', '10'), ('♣', 'J'), ('♣', 'Q'), ('♣', 'K')]


 # entireCardList의 덱을 무작위로 섞는다
 # def shuffle_deck():
 #     shuffled_entireCardList = random.suffle(entireCardList)
 #     return shuffled_entireCardList

 # 7장씩 카드를 플레이어(사용자,컴퓨터)에게 나눠준다.(pop()으로 7번 하면 될듯?)
 # player(인스턴스).cardList에 pop()한 카드를 넣는다.

 def give_card(player):
     i = 0
     while i < 7:
         player.cardList.append(entireCardList.pop())
         i += 1

 #카드가 A일 경우 attack_list에 팝한 카드 저장
 def card_A():
     for i in range(3):
         attack_list.append(entireCardList.pop())
     return attack_list

 #카드가 2일 경우 attack_list에 팝한 카드 저장
 def card_2():
     for i in range(2):
         attack_list.append(entireCardList.pop())
     return attack_list

 def card_7(player_card):
     current_shape=player_card[0]
     current_number=player_card[1]
     global player_turn
     while True: #무한루프, 사용자가 입력한 입력값이 1이거나 2이거나 3이면 break
         shape_list = ['♠', '♥', '◆', '♣']
         shape_list.remove(current_shape)  # player_card의 [0], 즉 모양을 가져와서 shape_list에서 제거
         if player_turn == 1:
             shape_input=input('바꿀 모양을 골라주세요: 1. {} 2. {} 3. {}'.format(shape_list[0],shape_list[1],shape_list[2])) #사용자로부터 어떤모양으로 바꿀지 1/2/3으로 받음
             if shape_input=='1':
                 shape_change = shape_list[0]
                 break #사용자가 선택한 수가 1이면 해당하는 모양을 shape_change 변수에 저장후 무한루프 break
             elif shape_input=='2':
                 shape_change = shape_list[1]
                 break #사용자가 선택한 수가 2이면 해당하는 모양을 shape_change 변수에 저장후 무한루프 break
             elif shape_input=='3':
                 shape_change = shape_list[2]
                 break #사용자가 선택한 수가 3이면 해당하는 모양을 shape_change 변수에 저장후 무한루프 break
             else:
                 print('입력값이 잘못되었습니다. 1,2,3 중 하나를 입력해주세요.') #사용자의 입력값이 1,2,3이 아니면 경고문 프린트 후 무한루프 회귀
         else:
             shape_list = ['♠', '♥', '◆', '♣']
             shape_list.remove(current_shape)
             shape_change = random.choice(shape_list)
             print("컴퓨터가 모양을 {}로 바꾸었습니다.".format(shape_change))
             break
     card_7_change=(shape_change,current_number) #7카드로 인해 변하게 되는 카드(변한모양,그대로의 수) 튜플을 card_7_change 변수에 저장
     return card_7_change #card_7_change 변수를 return

 def check_card(player_card, table_card):
     # table_card의 모양,숫자(table_card(0),table_card(1))와 player_card의 모양,숫자(player_card(0),player_card(1)) 중
     # 하나라도 일치할 시 True반환, 조건에 하나라도 부합하지 않으면 False 반환
     # 만약 True일시 현재 테이블에 놓여져 있는 카드(table_card)의 정보를 사용자가 낸 player_card로 업데이트
     result = True if table_card[0] == player_card[0] or table_card[1] == player_card[1] else False

     if result == True:
         global attack_card
         global attack_list
         global player_turn

         table_card = player_card
         result = table_card
         if player_card[1] == 'A':
             attack_list = card_A()
             attack_card = 'A'
             print("플레이어가 'A' 카드로 공격했습니다.")
         elif player_card[1] == '2':
             if attack_card != 'A':
                 attack_list = card_2()
                 attack_card = '2'
                 print("플레이어가 '2' 카드로 공격했습니다.")
             else:
                 if player_turn == 1:
                     player.cardList = player.cardList + attack_list
                     print("'A' 카드를 방어하지 못했습니다.")
                 else:
                     computer.cardList = computer.cardList + attack_list
                     print("'A' 카드를 방어하지 못했습니다.")

                 attack_list = []
                 attack_card = ''

         elif player_card[1] == '7':
             result = card_7(player_card)

         else:
             if player_turn == 1:

                 player.cardList = player.cardList + attack_list
             else:

                 computer.cardList = computer.cardList + attack_list
             attack_list = []
             attack_card = ''
     else:
         if attack_list != []:
             if player_turn == 1:
                 player.cardList = player.cardList + attack_list
             else:
                 computer.cardList = computer.cardList + attack_list
             print("상대방의 공격 카드를 방어하지 못했습니다.")
             attack_list = []
             attack_card = ''

     return result


 # 게임 시작 !
 count = 1  # 라운드 숫자
 attack_list = [] #공격시 임시로 먹어야할 카드 저장
 attack_card = '' #공격시 임시로 저장되는 공격 카드 종류

 while True:
     player_turn = 1
     if count == 1:  # 1라운드 일 때만 table_card를 처음으로 설정
         print("원 카드 게임을 시작합니다 !")
         player = CardPlayer()
         computer = CardPlayer()

         table_card = entireCardList.pop()  # 현재 테이블에 놓여져 있는 카드
         random.shuffle(entireCardList)  # 카드를 섞는다

         give_card(player)  # 카드를 플레이어에게 7장씩 분배한다.
         give_card(computer)  # 카드를 컴퓨터에게 7장씩 분배한다.

     print('====================================================================')
     print(f'현재 {count}라운드 이며, 현재 타겟 카드는 {table_card} 입니다.')

     # 조건에 부합하는 카드가 사용자 덱에 없을시 카드 1장을 드로우 하고 턴을 컴퓨터에게 넘김
     if player.check_draw(table_card) == False:
         if attack_list != []:
             print("상대방의 공격 카드를 방어하지 못했습니다.")
             player.cardList = player.cardList + attack_list
             attack_list = []
             attack_card = ''
         print('현재 타겟 카드에 부합하는 카드가 나의 덱에 존재하지 않습니다. 카드를 1장 뽑고 턴을 컴퓨터에게 넘깁니다.')
         print('카드를 뽑고 나서 나의 덱 구성은 다음과 같습니다.')
         player.draw_card()
         player.show_hand()
         print('')

     else:
         print('사용자의 턴! 뽑을 카드를 인덱스로 선택해주세요(1부터 시작) ! 현재 당신의 덱은 다음과 같습니다.')
         player.show_hand()
         print('')
         print('====================================================================')

         player_choose = int(input())  # 사용자가 현재 덱에서 뽑을 카드를 인덱스로 선택
         player.choose_card(player_choose)  # 사용자가 입력한 카드의 인덱스를 통해 뽑는다.
         player_put_card_result = player.put_card(table_card)  # 사용자가 고른 카드를 낼 수 있는지 여부(True : 가능, False : 불가능)

         while True:
             if player_put_card_result == False:
                 if len(player.cardList) == 0:
                     break

                 print('================================================================')
                 print('다시 사용자의 턴! 뽑을 카드를 인덱스로 선택해주세요(1부터 시작) ! 현재 당신의 덱은 다음과 같습니다.')
                 player.show_hand()
                 print('')
                 print('====================================================================')
                 player_choose = int(input())  # 사용자가 현재 덱에서 뽑을 카드를 인덱스로 선택
                 player.choose_card(player_choose)  # 사용자가 입력한 카드의 인덱스를 통해 뽑는다.
                 player_put_card_result = player.put_card(table_card)  # 사용자가 고른 카드를 낼 수 있는지 여부(True : 가능, False : 불가능)


             elif player_put_card_result[1] == 'J' or player_put_card_result[1] == 'K':
                 table_card = player_put_card_result

                 # 조건에 부합하는 카드가 사용자 덱에 없을시 카드 1장을 드로우 하고 턴을 컴퓨터에게 넘김
                 if player.check_draw(table_card) == False:
                     if len(player.cardList) == 0:
                         break

                     print('현재 타겟 카드에 부합하는 카드가 나의 덱에 존재하지 않습니다. 카드를 1장 뽑고 턴을 컴퓨터에게 넘깁니다.')
                     print('카드를 뽑고 나서 나의 덱 구성은 다음과 같습니다.')
                     player.draw_card()
                     player.show_hand()
                     print('')
                     break

                 print('================================================================')
                 print('J와 K를 골랐으니 다시 사용자의 턴! 뽑을 카드를 인덱스로 선택해주세요(1부터 시작) ! 현재 당신의 덱은 다음과 같습니다.')
                 player.show_hand()
                 print('')
                 print(f'현재 타겟 카드는 {table_card} 입니다.')
                 print('====================================================================')
                 player_choose = int(input())  # 사용자가 현재 덱에서 뽑을 카드를 인덱스로 선택
                 player.choose_card(player_choose)  # 사용자가 입력한 카드의 인덱스를 통해 뽑는다.
                 player_put_card_result = player.put_card(table_card)  # 사용자가 고른 카드를 낼 수 있는지 여부(True : 가능, False : 불가능)
                 continue

             else:
                 table_card = player_put_card_result
                 break

     if (len(entireCardList) == 0):
         print('무승부입니다! 게임을 종료합니다 !!')
         break

     if (len(player.cardList) == 0):
         print('사용자의 승리 ! 게임을 종료합니다 !!')
         break

     print('==========================================================')
     print(f'현재 {count}라운드 이며, 현재 타겟 카드는 {table_card} 입니다.')
     print('컴퓨터의 턴! 현재 컴퓨터의 덱은 다음과 같습니다.')
     computer.show_hand()
     print('')
     print('==========================================================')

     player_turn = 0

     # 조건에 부합하는 카드가 컴퓨터 덱에 없을시 카드 1장을 드로우 하고 턴을 사용자에게 넘김
     if computer.check_draw(table_card) == False:
         computer.cardList = computer.cardList + attack_list
         attack_list = []
         attack_card = ''
         print('현재 타겟 카드에 부합하는 카드가 컴퓨터의 덱에 존재하지 않습니다. 카드를 1장 뽑고 턴을 사용자에게 넘깁니다.')
         print('카드를 뽑고 나서 컴퓨터의 덱 구성은 다음과 같습니다.')
         computer.draw_card()
         computer.show_hand()
         print('')

     else:
         if computer.check_draw(table_card) == False:
             if len(computer.cardList) == 0:
                 break

             print('현재 타겟 카드에 부합하는 카드가 컴퓨터의 덱에 존재하지 않습니다. 카드를 1장 뽑고 턴을 사용자에게 넘깁니다.')
             print('카드를 뽑고 나서 컴퓨터의 덱 구성은 다음과 같습니다.')
             computer.draw_card()
             computer.show_hand()
             print('')
             break

         computer_choosed_card = computer.computer_choose(table_card)
         print(f'컴퓨터가 뽑은 카드는 {computer_choosed_card} 입니다.')
         computer_choosed_card_index = computer.cardList.index(computer_choosed_card)
         computer.choose_card(computer_choosed_card_index+1)
         table_card = computer.put_card(table_card)

         if (len(computer.cardList) == 0):
             print('컴퓨터의 승리 ! 게임을 종료합니다 !!')
             break

         if computer_choosed_card[1] == 'J' or computer_choosed_card[1] == 'K':
             print('====================================================================')
             print('J와 K를 골랐으니 다시 컴퓨터의 턴! 컴퓨터가 자동으로 카드를 뽑습니다!!! 현재 컴퓨터의 덱은 다음과 같습니다.')
             print(computer.show_hand())
             print('')
             print(f'현재 타겟 카드는 {table_card} 입니다.')
             print('====================================================================')
             continue

         if (len(entireCardList) == 0):
             print('무승부입니다! 게임을 종료합니다 !!')
             break

     count += 1  # 라운드가 끝날때 마다 라운드 숫자 증가가 
