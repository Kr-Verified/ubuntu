from random import choice as c
import sys
word_dict={}
correct=[]
wrong=[]
master=[]
dangerous=[]
first=[]
win=[0,0,0]

def check_answer(user_input, answers):
    user_answers = sorted(set(a for a in user_input.replace(' ', '').split(',')))
    nanswers = sorted(set(a for a in answers.replace(' ', '').replace('.', '').replace('~', '').replace('\'', '').split(',')))
    win[1]+=1
    return user_answers == nanswers

def up_pos(k):
    win[0]+=1
    win[2]+=1
    if k in first:
        master.append(k)
        first.remove(k)
        del word_dict[k]
    if k in correct:
        correct.remove(k)
        master.append(k)
        del word_dict[k]
    elif k in wrong:
        wrong.remove(k)
    elif k in dangerous:
        dangerous.remove(k)
        wrong.append(k)
    elif k not in master:
        correct.append(k)

def down_pos(k):
    win[0]=0
    if k in first:
        first.remove(k)
        return 0
    if k in correct:
        correct.remove(k)
    elif k in wrong:
        wrong.remove(k)
        dangerous.append(k)
    elif k not in dangerous:
        wrong.append(k)

def pick(word):
    if not word:
        print("단어 숙지 완료!")
        return None, None
    else:
        k, v = c(list(word.items()))
        if k in master:
            del word[k]
            pick(word)
        elif k in correct:
            if c([False, True]):
                return k, v
            else:
                pick(word)
        elif k in wrong:
            if c([True, False]):
                return k, v
            else:
                pick(word)
        elif k in dangerous:
            return k, v
        return k, v

def makeQuestion():
    #문제 종류 무작위 (영어, 뜻)
    key=''
    is_english = c([True, False, True])
    if is_english:
        question, answer = pick(word_dict)
        key = question
    else:
        answer, question = pick(word_dict)
        key = answer
    
    if question==None:
        sys.exit()

    print("---------------------------------------------------------------------------------------------------\n\n")
    
    if (win[0]==0): print("연속으로 문제 맞추기 도전!")
    elif (win[0]<3): print(f"무난하게 연속 {win[0]} 문제 맞춤")
    elif (win[0]<6): print(f"좀 어려운 연속 {win[0]} 문제 맞춤")
    elif (win[0]<10): print(f"생각보다 어려운 연속 {win[0]} 문제 맞춤")
    elif (win[0]<15): print(f"대단하게 연속 {win[0]} 문제 맞춤")
    elif (win[0]<20): print(f"어렵고 대단한 연속 {win[0]} 문제 맞춤")
    elif (win[0]<25): print(f"어떡해? 연속 {win[0]} 문제 맞춤")
    elif (win[0]<30): print(f"엄청 놀랍게 연속 {win[0]} 문제 맞춤!")
    elif (win[0]<35): print(f"와우! 연속 {win[0]} 문제 맞춤!")
    elif (win[0]<45): print(f"하루치 이상의 단어를 이렇게 대단하게 연속 {win[0]} 문제 맞춤!")
    elif (win[0]<60): print(f"이렇게 많은 단어를 연속 {win[0]} 문제 맞추다니!")
    elif (win[0]<75): print(f"?! 연속 {win[0]} 문제 맞춤!")
    elif (win[0]<90): print(f"믿을 수 없다! 연속 {win[0]} 문제 맞춤!")
    elif (win[0]<120): print(f"연속 [{win[0]}] 문제 맞춤!!")
    else: print(f"이럴수가! 연속 {win[0]} 문제 맞춤! 당신은 혹시 단어 천제?!")

    if (win[1]!=0):print(f"정답률 : {(win[2]/win[1])*100}%")
    print(f"\n\n문제 ( {len(word_dict)} ): \t {question}\n\n\n")

    # 사용자 입력 받기
    user_answer = input("답을 입력하세요  ( 여러 뜻은 쉼표로 구분 ) : \t").strip().replace(' ', '').replace('.', '').replace('~', '').replace('*', '').replace('\'', '')

    # 정답 확인
    correctA = check_answer(user_answer, answer)

    print('\n\n')

    # 결과 출력
    if correctA:
        up_pos(key)
        print("정답입니다!")
    else:
        down_pos(key)
        print(f'틀렸습니다.정답은 " {answer} " 입니다.')
    print("\n\n\n")
    print("---------------------------------------------------------------------------------------------------")

file = input("단어장 이름을 작성하시오: ")
try:
    with open(f"{file}.txt", 'r', encoding='utf-8') as file:
        for line in file:
            # 줄바꿈 문자 제거 및 '/'로 분리
            parts = line.strip().split('/')
            
            # 정확히 두 부분으로 나뉘었는지 확인
            if len(parts) == 2:
                english_word = parts[0].strip()
                meaning = parts[1].strip()
                word_dict[english_word] = meaning
                first.append(english_word)
            else:
                print(f"Warning: Skipping invalid line: {line}")

except FileNotFoundError:
        print(f"Error: File '{file}.txt' not found.")
except IOError:
        print(f"Error: Could not read file '{file}.txt'.")

while True:
     makeQuestion()
