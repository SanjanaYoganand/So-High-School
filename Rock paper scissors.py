R='Game going'
print('\t\t\t\tRock, paper, scissors!')
print('\t\t\t\t----------------------')
import random
max_pts=int(input('Points to win:'))
pts=0
p_pts=0
print('\t\t\t\t\t\t\tScores:')
print('\t\t\t\t\t\t\t-------')
print('\t\t\t\t  Python:','\t\t\t\tYou:')
while R=='Game going':
     u=input('Yours:')
     r=random.randint(0,2)
     if r==0:
          p='Rock'
     elif r==1:
          p='Paper'
     elif r==2:
          p='Scissors'
     print('Python:',p)
     if u.lower()==p.lower():
          print('\t\t\t\t  0','\t\t\t\t\t0')
          continue
     elif u.lower()=='rock':
          if p.lower()=='scissors':
               pts+=1
               print('\t\t\t\t  0','\t\t\t\t\t1')
          elif p.lower()=='paper':
               p_pts+=1
               print('\t\t\t\t  1','\t\t\t\t\t0')
     elif u.lower()=='scissors':
          if p.lower()=='rock':
               p_pts+=1
               print('\t\t\t\t  1','\t\t\t\t\t0')
          elif p.lower()=='paper':
               pts+=1
               print('\t\t\t\t  0','\t\t\t\t\t1')
     elif u.lower()=='paper':
          if p.lower()=='rock':
               pts+=1
               print('\t\t\t\t  0','\t\t\t\t\t1')
          elif p.lower()=='scissors':
               p_pts+=1
               print('\t\t\t\t  1','\t\t\t\t\t0')
     if pts==max_pts or p_pts==max_pts:
          R='Game over'
          print('\t\t\t\t  Sum=',p_pts,'\t\t\t\tSum=',pts)
print()
print('Result:')
if pts==max_pts:
     print('You won!:)')
else:
     print('Python won!;)')
