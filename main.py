import json,os,urllib.request as u
U=os.environ["MAKEFUN_ENV_URL"]
V=(0,100,320,330,500,900,0)
N=(31,33,14,18,-31,-33,-14,-18)
G=(1,15,16,17,-1,-15,-16,-17)
I=(15,17,-15,-17);R=(1,16,-1,-16)
D=(0,0,N,I,R,I+R,G)
S=(0,0,1,9,9,9,1)
K={0:13,7:14,4:12,112:7,119:11,116:3}
B=[0]*128;T=1;C=0;E=-1;W=4;Y=116;O=0;L=150000
def f(n):
 global B,T,C,E,W,Y
 B=[0]*128;T=1;C=0;E=-1;W=4;Y=116;q=112
 a=n.split()
 for c in a[0]:
  if c=="/":q-=24
  elif c.isdigit():q+=int(c)
  else:
   v="PNBRQK".index(c.upper())+1
   if c.islower():v=-v
   B[q]=v
   if v==6:W=q
   if v==-6:Y=q
   q+=1
 T=1 if a[1]=="w" else -1
 C=sum(1<<i for i,ch in enumerate("KQkq") if ch in a[2])
 E=ord(a[3][0])-97+(int(a[3][1])-1)*16 if a[3]!="-" else -1
def A(q,y):
 for o in (-1,1):
  t=q-16*y+o
  if not t&136 and B[t]==y:return 1
 for X,k in ((N,2),(G,6)):
  for o in X:
   t=q+o
   if not t&136 and B[t]==y*k:return 1
 for o in I+R:
  t=q+o
  while not t&136:
   v=B[t]
   if v:
    if v==y*5 or (o in I and v==y*3) or (o in R and v==y*4):return 1
    break
   t+=o
 return 0
def g(z=0):
 o=[];Z=o.append
 for s in range(128):
  if s&136:continue
  v=B[s]
  if not v or (v>0)!=(T>0):continue
  a=abs(v);d=16*T
  if a==1:
   for x in (d,d-1,d+1):
    t=s+x
    if t&136:continue
    w=B[t]
    if x==d:
     if w or z:continue
    elif not ((w and (w>0)!=(T>0)) or t==E):continue
    Q=(5,2,3,4) if t>>4==7*(T>0) else (0,)
    for q in Q:Z(s|(t<<7)|(q<<14))
    if x==d and not Q[0] and s>>4==1+5*(T<0) and not B[s+2*d]:Z(s|((s+2*d)<<7))
  else:
   for x in D[a]:
    t=s+x;n=S[a]
    while n and not t&136:
     w=B[t]
     if w:
      if (w>0)!=(T>0):Z(s|(t<<7))
      break
     if not z:Z(s|(t<<7))
     t+=x;n-=1
   if a==6 and not z:
    k=4 if T>0 else 116
    for d in (1,-1):
     r=1<<(2*(T<0)+(d<0));t=k+2*d;rk=k+3*d if d>0 else k-4
     if C&r and not B[k+d] and not B[t] and B[rk]==4*T and not A(k,-T) and not A(k+d,-T) and not A(t,-T) and (d>0 or not B[k-3]):
      Z(k|(t<<7))
 return o
def m(n):
 global T,C,E,W,Y
 a=n&127;b=(n>>7)&127;c=(n>>14)&7;v=B[a];p=B[b];e=-1
 if abs(v)<2 and b==E:e=b-16*T;p=B[e];B[e]=0
 u=(n,p,e,C,E,W,Y)
 B[b]=(c or abs(v))*((v>0)*2-1);B[a]=0
 if abs(v)==6 and abs(b-a)==2:
  q,w=(b+1,b-1) if b&7==6 else (b-2,b+1);B[w]=B[q];B[q]=0
 E=a+16*T if abs(v)<2 and abs(b-a)==32 else -1
 C&=K.get(a,15)&K.get(b,15)
 if v==6:W=b
 if v==-6:Y=b
 T=-T
 return u
def j(u):
 global T,C,E,W,Y
 n,p,e,c,q,w,y=u
 a=n&127;b=(n>>7)&127;d=(n>>14)&7;v=B[b]
 T=-T;C=c;E=q;W=w;Y=y
 if abs(v)>5 and abs(b-a)==2:
  r,w=(b+1,b-1) if b&7==6 else (b-2,b+1);B[r]=B[w];B[w]=0
 B[a]=(1 if d else abs(v))*((v>0)*2-1);B[b]=p if e<0 else 0
 if e>=0:B[e]=p
def l(z=0):
 o=[]
 for n in g(z):
  u=m(n)
  if not A(W if T<0 else Y,T):o.append(n)
  j(u)
 return o
def e():
 s=0
 for v in B:
  if v:s+=V[abs(v)]*((v>0)*2-1)
 return s*T
def q(a,b,d=10):
 global O
 O+=1
 if O>L:raise StopIteration
 k=W if T>0 else Y
 c=A(k,-T)
 if not c:
  s=e()
  if s>=b:return b
  if s>a:a=s
 if d<=0:return a
 for n in l(not c):
  u=m(n)
  try:r=-q(-b,-a,d-1)
  except StopIteration:j(u);raise
  j(u)
  if r>=b:return b
  if r>a:a=r
 return a
def s(d,a,b):
 global O
 O+=1
 if O>L:raise StopIteration
 if d==0:return q(a,b)
 z=l()
 if not z:
  return -99999 if A(W if T>0 else Y,-T) else 0
 z.sort(key=lambda n:-V[abs(B[(n>>7)&127])])
 c=a
 for n in z:
  u=m(n)
  try:r=-s(d-1,-b,-c)
  except StopIteration:j(u);raise
  j(u)
  if r>c:c=r
  if c>=b:break
 return c
def y(z):
 global O
 O=0;d=1;h=z[0]
 while d<=12:
  try:
   a=-99999;g=z[0]
   for n in sorted(z,key=lambda n:-V[abs(B[(n>>7)&127])]):
    u=m(n)
    try:r=-s(d-1,-99999,-a)
    except StopIteration:j(u);raise
    j(u)
    if r>a:a=r;g=n
   h=g;d+=1
  except StopIteration:break
 return h
def w(n):
 return "".join(chr(97+(x&7))+str((x>>4)+1) for x in (n&127,(n>>7)&127))+("","","n","b","r","q")[n>>14]
def p(t,b):
 with u.urlopen(U+t,json.dumps(b).encode()) as x:return json.load(x)
while 1:
 H=p("/game",{})
 if H["status"][0]=="d":break
 while H["status"][0]=="y":
  f(H["fen"]);z=l();H=p("/move",{"game":H["game"],"move":w(y(z))})
