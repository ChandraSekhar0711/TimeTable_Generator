import random
m=6
n=8
Periods=m*n
print("Enter no.of Subjects,no.of default_periods,no.of labs,no.of free_periods::")
sub,dp,l,fp=map(int,input().split())


emp=""
p=[[emp for i in range(n+5)]for j in range(m+5)]
q=[[emp for i in range(n+5)]for j in range(m+5)]
freq=[]
freq1=[]

default=[]
print("Enter",dp,"default_periods...")
for i in range(0,dp):
    default.append(input())
print()

fperiods=[]
print("Enter",fp,"free_periods...")
for i in range(0,fp):
    fperiods.append(input())
print()

labs=[]
labs_faculty=[]
lab_details={}
print("Enter",l,"lab_periods...")
for i in range(0,l):
    print("enter lab",i,":",end=" ")
    labs.append(input())
    #print("enter faculty for ",labs[i],"lab:",end=" ")
    #labs_faculty.append(input())
    #lab_details[labs_faculty[i]]=labs[i]
print()

main_subjects=[]
sub_faculty=[]
subject_faculty={}
print("Enter",sub,"Subjects...")
for i in range(0,sub):
    print("enter subject", i,":",end=" ")
    main_subjects.append(input())
    #print("enter faculty for ",main_subjects[i],":",end=" ")
    #sub_faculty.append(input())
    #subject_faculty[sub_faculty[i]]=main_subjects[i]
print()


def sec1():
    def default_periods():
        def exams():
                i=2
                for j in range(0,i):
                        p[i][j]=default[0]
                        q[i][j]=default[0]
        exams()

        def rev():
                i=1
                for j in range(4,n):
                        p[i][j]=default[1]
                        q[i][j]=default[1]
        rev()

        def elec():
            i=2
            count=0
            while count<5:
                k=random.randint(0,5)
                s=random.randint(0,6)
                if p[k][s]!=emp or q[k][s]!=emp :
                  continue
                else:
                  p[k][s]=default[i]
                  q[k][s]=default[i]
                  count=count+1
        elec()

    default_periods()

    def free_periods():
        def crt():
          i=0
          count=0
          while count<3:
              k=random.randint(0,5)
              s=random.randint(0,6)
              if p[k][s]!=emp:
                continue
              else:
                p[k][s]=fperiods[i]
                count=count+1
        crt()

        def free():
          count=0
          while count<5:
              k=random.randint(0,5)
              s=7
              if p[k][s]!=emp and q[k][s]!=emp:
                continue
              else:
                p[k][s]=fperiods[1]
                q[k][s]=fperiods[1]
                count=count+1
        free()
    free_periods()

    def lab_periods():
        def lab():
                i=0
                count =0
                while count<9:
                    k=random.randint(0,5)
                    s=random.randint(0,4)
                    if (p[k][s]!=emp or p[k][s+1]!=emp or p[k][s+2]!=emp):
                        continue
                    else:
                        for j in range(0,3):
                            p[k][s+j]=labs[i]
                            count=count+i
                        i+=1
        lab()
    lab_periods()

    def subj():
        def subjects():
          i=0
          count=0
          while count<20:
            while freq.count(main_subjects[i])<5:
              k=random.randint(0,5)
              s=random.randint(0,6)
              if p[k][s]!=emp:
                continue
              else:
                p[k][s]=main_subjects[i]
                count=count+1
                freq.append(main_subjects[i])
            i=i+1
        subjects()
    subj()
sec1()
#Section allocation starts from here.....
def sec2():
    def crt1():
      i=0
      count=0
      while count<3:
          k=random.randint(0,5)
          s=random.randint(0,7)
          if q[k][s]!=emp or p[k][s]==fperiods[i]:
            continue
          else:
            q[k][s]=fperiods[i]
            count=count+1
    crt1()

    def labs1():
            i=0
            count=0
            while count<9:
                    k=random.randint(0,5)
                    s=random.randint(0,4)
                    if (q[k][s]!=emp or q[k][s+1]!=emp or q[k][s+2]!=emp or p[k][s]==labs[i] or p[k][s+1]==labs[i] or p[k][s+2]==labs[i]):
                            continue
                    else:
                            for j in range(0,3):
                                    q[k][s+j]=labs[i]
                                    count=count+1
                            i+=1
    labs1()



    def subjects1():
      i=0
      count=0
      while count<20:
        while freq1.count(main_subjects[i])<5:
          k=random.randint(0,5)
          s=random.randint(0,6)
          if q[k][s]!=emp or p[k][s]==main_subjects[i]:
            continue
          else:
            q[k][s]=main_subjects[i]
            count=count+1
            freq1.append(main_subjects[i])
        i=i+1
    subjects1()
sec2()


for i in range(0,m):
    for j in range(0,n):
        print(p[i][j],end=" | ")
    print()
print()
print()
for i in range(0,m):
    for j in range(0,n):
        print(q[i][j],end=" | ")
    print()
print()
print()



print("subjects:",subject_faculty)
print("labs:",lab_details)
