""" 효율적인 풀이도 기억해두자!
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)"""



def solution(s):
    n = len(s)
    num = []
    answer = []
    for i in range(10):
          num.append(str(i))
    A = 0
    while( A <= n ):
        if( A == n):
          answer = int(''.join(answer))
          break
        if( s[A] in num ):
          answer.append(s[A])
          A += 1
          continue
        elif(s[A] == 'z'):
          answer.append('0')
          A += 4
          continue
        elif(s[A] == 'o'):
          answer.append('1')
          A += 3
          continue
        elif(s[A] == 'n'):
          answer.append('9')
          A += 4
          continue
        elif(s[A] == 'e'):
          answer.append('8')
          A += 5
        elif(s[A] == 't'):
            if(s[A+1] == 'w'):
              answer.append('2')
              A += 3
              continue
            else:
              answer.append('3')
              A += 5
              continue
        elif(s[A] == 'f'):
            if(s[A+1] == 'o'):
              answer.append('4')
              A += 4
              continue
            else:
              answer.append('5')
              A += 4
              continue
        elif(s[A] == 's'):
            if(s[A+1] == 'e'):
              answer.append('7')
              A += 5
              continue
            else:
              answer.append('6')
              A += 3
              continue

    return answer