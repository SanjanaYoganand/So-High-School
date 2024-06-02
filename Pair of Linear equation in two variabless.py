a=int(input('Enter co-eff of x in eqn1:'))
b=int(input('Enter co-eff of y in eqn1:'))
c=int(input('Enter constant of eqn1:'))
print()
A=int(input('Enter co-eff of x in eqn2:'))
B=int(input('Enter co-eff of y in eqn2:'))
C=int(input('Enter constant of eqn2:'))
print('Given eqns are:')
print(a,'x','+',b,'y','=',c)
print(A,'x','+',B,'y','=',C)
if abs(A)>abs(a):
     a1=A
     A1=a
else:
     a1=a
     A1=A
if abs(B)>abs(b):
     b1=B
     B1=b
else:
     b1=b
     B1=B
if a1/A1<b1/B1:
     K=a
     a=a*A
     b=b*A
     c=c*A
     A=A*K
     B=B*K
     C=C*K
     Sa=a-A;Sb=b-B;Sc=c-C
     y=Sc/Sb
     x=(C-(y*B))/A
     print('--------------')
     print(Sb,'y=',Sc)
     print('--------------')
     print('x=',x,'y=',y)
else:
     k=b
     a=a*B
     b=b*B
     c=c*B
     A=A*k
     B=B*k
     C=C*k
     Sa=a-A;Sb=b-B;Sc=c-C
     x=Sc/Sa
     y=(C-(x*A))/B
     print('--------------')
     print(Sa,'x=',Sc)
     print('--------------')
     print('x=',x,'y=',y)






