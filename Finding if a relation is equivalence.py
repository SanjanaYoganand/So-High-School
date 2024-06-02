s1=eval(input('Enter a set A:'))
s2=s1
S=set()
for i in s1:
     for j in s2:
          S.add((i,j))
print('AxA=',S)
R=eval(input('Enter relation over the set:'))
rr='Reflexive'
ss='Symmetric'
tt='Transitive'
Result='Not Equivalence'
for r in s1:
     if (r,r) not in R:
          rr='Not Reflexive'
for (K,J) in R:
     if (J,K) not in R:
          ss='Not Symmetric'
     for l in s1:
          if (K,l) in R:
               if (J,l) not in R:
                    tt='Not Transitive'
if rr=='Reflexive' and ss=='Symmetric' and tt=='Transitive':
     Result='Equivalence'
print(rr,ss,tt,Result,sep='\n')
