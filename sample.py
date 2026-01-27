# Sample of my First Project
# Importing Librarys
import numpy as np
import pandas as pd
import matplotlib.pyplot as mlt
import seaborn as sns
# Using While Loop for Enter Class
valid_class=[9,10,11,12]
print('Hello Students...Please Enter Your Class')
classes=int(input("class:"))
while classes not in valid_class:
     print('Enter Only 9 to 12') 
     classes=int(input("class:"))
# 9 or 10 class Students enter Name and Subject     
print('Your Class is :',classes)
if classes == 9 or classes== 10:
    print('Now Please Enter Your Details')
    Name=str(input("Name:"))
    subject_1=str(input('Enter Subject 1:'))
    subject_2=str(input("Enter Subject 2:"))
    subject_3=str(input("Enter Subject 3:"))
    subject_4=str(input("Enter Subject 4:"))
    subject_5=str(input("Enter Subject 5:"))
    subject_1_marks=int(input(f'Enter {subject_1} Marks:'))
    subject_2_marks=int(input(f'Enter {subject_2} Marks:'))
    subject_3_marks=int(input(f'Enter {subject_3} Marks:'))
    subject_4_marks=int(input(f'Enter {subject_4} Marks:'))
    subject_5_marks=int(input(f'Enter {subject_5} Marks:'))
    # Convert input to Dataframe
    subjects={'Name':[Name],
              subject_1:[subject_1_marks],
              subject_2:[subject_2_marks],
              subject_3:[subject_3_marks],
              subject_4:[subject_4_marks],      
              subject_5:[subject_5_marks]}
    df=pd.DataFrame(subjects)
    print(df)
    # Create a Plot by Using SeaBorn or Matplotlib
    sns.catplot(df,kind='bar')
    mlt.title(f'{Name}-Subjects Progress Comparison')
    mlt.show()
    # Taking Input from Student of Interesting Subject
    interest=input('Enter Your Interested Subjects:').lower()
    # Suggest Career Option to Student Basis on Interested Subject
    valid_subject=['maths','science','social science','accounts']
    while interest not in valid_subject:
        print('Enter Valid Subject')
        interest=input('Enter Your Interested Subjects:').lower()
    if interest == 'science':
        print("Science  Stream is Best Decision For you in 12th Class")
    elif interest == 'social science':
        print("Arts Stream is Best for you in 12th Class")
    elif interest == 'maths' or interest == 'accounts' :
        print('Commerce Stream is Best For You in 12th Class')
    # Adding Grade of Student Marks                 
    grade=(subject_1_marks+subject_2_marks+subject_3_marks+subject_4_marks+subject_5_marks)/5    
    if grade>=90:
        print("A Grade:",grade,'%')
    elif grade>=70 and grade<90:
        print("B Grade",grade,'%')
    elif grade>=50 and grade<70:
        print('C Grade ',grade,'%')
    elif grade>=35 and grade<50:
        print('D Grade',grade,'%')    
    else:
        print("FAIL")            
#  11 or 12 class Start         
elif classes == 11 or classes== 12:
    print('Enter Valid Stream')
    # Taking input sream for better Analyse
    stream=str(input('stream:')).lower()
    # Adding Loop for Stream
    valid_stream=['science','arts','commerce']
    while stream not in valid_stream:
        print('Enter Valid Stream')
        stream=str(input('stream:'))
    # Science Stream Start
    if stream== 'science'.lower():
        #  11 or 12 class Science Stream Students enter Name and Subject
        print('Now Please Enter Your Details')
        Name=str(input("Name:"))
        subject_1=str(input('Enter Subject 1:'))
        subject_2=str(input("Enter Subject 2:"))
        subject_3=str(input("Enter Subject 3:"))
        subject_4=str(input("Enter Subject 4:"))
        subject_5=str(input("Enter Subject 5:"))
        subject_6=str(input("Enter Subject 6:"))
        subject_1_marks=int(input(f'Enter {subject_1} Marks:'))
        subject_2_marks=int(input(f'Enter {subject_2} Marks:'))
        subject_3_marks=int(input(f'Enter {subject_3} Marks:'))
        subject_4_marks=int(input(f'Enter {subject_4} Marks:'))
        subject_5_marks=int(input(f'Enter {subject_5} Marks:'))
        subject_6_marks=int(input(f'Enter {subject_5} Marks:'))
        # Convert input to Dataframe
        subjects={'Name':[Name],
                  subject_1:[subject_1_marks],
                  subject_2:[subject_2_marks],
                  subject_3:[subject_3_marks],
                  subject_4:[subject_4_marks],      
                  subject_5:[subject_5_marks],
                  subject_6:[subject_6_marks]}
        df=pd.DataFrame(subjects)
        print(df)
        # Create a Plot by Using SeaBorn or Matplotlib
        sns.catplot(df,kind='bar')
        mlt.title(f'{Name}-Subjects Progress Comparison')
        mlt.show()
        # Taking Input from Student of Interesting Subject
        interest=input('Enter Your Interested Subjects:').lower()
        valid_subject=['maths','physics','chemistry','biology','hindi','english']
        # Suggest Career Option to Student Basis on Interested Subject
        while interest not in valid_subject:
            print('Enter Valid Subject')
            interest=input('Enter Your Interested Subjects:').lower()
        if interest in ['physics','maths','chemistry']:
            print("Just Do JEE MAINS and Get Addmission in B.Tech Engineering")
        elif interest in ['biology']:
            print("Just Do NEET and Get Addmission in MBBS or Pharmacy"
                  '\n','You Also Have More Options like:D.Pharma,B.Phharma, and for more info search on internet')
        elif interest in  ['hindi','english']:
            print('Just Do CUET and Get Addmission in', interest,'hounors and Become Lecturare',
                  '\n','You Also Have More Options like:D.Pharma,B.Phharma, and for more info search on internet' )
        # Adding Grade of Student Marks                  
        grade=(subject_1_marks+subject_2_marks+subject_3_marks+subject_4_marks+subject_5_marks+subject_6_marks)/6    
        if grade>=90:
            print("A Grade:",grade,'%')
        elif grade>=70 and grade<90:
            print("B Grade",grade,'%')
        elif grade>=50 and grade<70:
            print('C Grade ',grade,'%')
        elif grade>=35 and grade<50:
            print('D Grade',grade,'%')    
        else:
            print("FAIL") 
    # Arts Stream Start                     
    elif stream== 'arts'.lower():     
        print('Now Please Enter Your Details')
        # 11 or 12 class Arts Stream Students enter Name and Subject
        Name=str(input("Name:"))
        subject_1=str(input('Enter Subject 1:'))
        subject_2=str(input("Enter Subject 2:"))
        subject_3=str(input("Enter Subject 3:"))
        subject_4=str(input("Enter Subject 4:"))
        subject_5=str(input("Enter Subject 5:"))
        subject_6=str(input("Enter Subject 6:"))
        subject_7=str(input("Enter Subject 7:"))
        subject_1_marks=int(input(f'Enter {subject_1} Marks:'))
        subject_2_marks=int(input(f'Enter {subject_2} Marks:'))
        subject_3_marks=int(input(f'Enter {subject_3} Marks:'))
        subject_4_marks=int(input(f'Enter {subject_4} Marks:'))
        subject_5_marks=int(input(f'Enter {subject_5} Marks:'))
        subject_6_marks=int(input(f'Enter {subject_5} Marks:'))
        subject_7_marks=int(input(f'Enter {subject_7} Marks:'))
        # Convert input to Dataframe
        subjects={'Name':[Name],
                  subject_1:[subject_1_marks],
                  subject_2:[subject_2_marks],
                  subject_3:[subject_3_marks],
                  subject_4:[subject_4_marks],      
                  subject_5:[subject_5_marks],
                  subject_6:[subject_6_marks],
                  subject_7:[subject_7_marks]}
        df=pd.DataFrame(subjects)
        print(df)
        # Create a Plot by Using SeaBorn or Matplotlib
        sns.catplot(df,kind='bar')
        mlt.title(f'{Name}-Subjects Progress Comparison')
        mlt.show()
        # Taking Input from Student of Interesting Subject
        interest=input('Enter Your Interested Subjects:').lower()
        valid_subject=['geography','history','political science','sociology','economics','hindi','english']
        # Suggest Career Option to Student Basis on Interested Subject
        while interest not in valid_subject:
            print('Enter Valid Subject')
            interest=input('Enter Your Interested Subjects:').lower()
        if interest in ['geography','history','political science']:
            print("Just Do UPSC or SSC and Become an IAS or IPS Officer",
                  '\n','You Also Have More Options like:BCA,BBA,IT Feild and for more info search on internet')
        elif interest in ['sociology','economics','hindi','english']:
            print('Just Do CUET and Get Addmission in', interest,'hounors and Become Lecturare'
                   '\n','You Also Have More Options like:BCA,BBA,IT Feild and for more info search on internet')
        # Adding Grade of Student Marks   
        grade=(subject_1_marks+subject_2_marks+subject_3_marks+subject_4_marks+subject_5_marks+subject_6_marks+subject_7_marks)/7   
        if grade>=90:
            print("A Grade:",grade,'%')
        elif grade>=70 and grade<90:
            print("B Grade",grade,'%')
        elif grade>=50 and grade<70:
            print('C Grade ',grade,'%')
        elif grade>=35 and grade<50:
            print('D Grade',grade,'%')    
        else:
            print("FAIL")
    # Arts Stream Start                       
    elif stream=="Commerce" or stream=='commerce':     
        print('Now Please Enter Your Details')
        # 11 or 12 class Commerce Stream Students enter Name and Subject
        Name=str(input("Name:"))
        subject_1=str(input('Enter Subject 1:'))
        subject_2=str(input("Enter Subject 2:"))
        subject_3=str(input("Enter Subject 3:"))
        subject_4=str(input("Enter Subject 4:"))
        subject_5=str(input("Enter Subject 5:"))
        subject_6=str(input("Enter Subject 6:"))
        subject_7=str(input("Enter Subject 7:"))
        subject_8=str(input("Enter Subject 8:"))
        subject_1_marks=int(input(f'Enter {subject_1} Marks:'))
        subject_2_marks=int(input(f'Enter {subject_2} Marks:'))
        subject_3_marks=int(input(f'Enter {subject_3} Marks:'))
        subject_4_marks=int(input(f'Enter {subject_4} Marks:'))
        subject_5_marks=int(input(f'Enter {subject_5} Marks:'))
        subject_6_marks=int(input(f'Enter {subject_5} Marks:'))
        subject_7_marks=int(input(f'Enter {subject_7} Marks:'))
        subject_8_marks=int(input(f'Enter {subject_8} Marks:'))
        # Convert input to Dataframe
        subjects={'Name':[Name],
                  subject_1:[subject_1_marks],
                  subject_2:[subject_2_marks],
                  subject_3:[subject_3_marks],
                  subject_4:[subject_4_marks],      
                  subject_5:[subject_5_marks],
                  subject_6:[subject_6_marks],
                  subject_7:[subject_7_marks],
                  subject_8:[subject_8_marks]}
        df=pd.DataFrame(subjects)
        print(df)
        # Create a Plot by Using SeaBorn or Matplotlib 
        sns.catplot(df,kind='bar')
        mlt.title(f'{Name}-Subjects Progress Comparison')
        mlt.show()
        # Taking Input from Student of Interesting Subject
        interest=input('Enter Your Interested Subjects:').lower()
        valid_subject=['maths','accounts','business','economics','hindi','english','enterpreneur','legal study']
        # Suggest Career Option to Student Basis on Interested Subject
        while interest not in valid_subject:
            print('Enter Valid Subject')
            interest=input('Enter Your Interested Subjects:').lower()
        if interest in ['maths','accounts','economics','business','legal study']:
            print("You have two best options CA(Chartered Accountant) and CS(Company Secretary)"
                  '\n','You Also Have More Options like:B.Com,BBA, and for more info search on internet')
        elif interest in ['enterpreneur']:
            print("Just Do Enterpreneur Course and Become an Enterprenuer"
                  '\n','You Also Have More Options like:B.Com,BBA, and for more info s# Adding Grade of Student Marks earch on internet')
        elif interest in  ['hindi','english']:
            print('Just Do CUET and Get Addmission in', interest,'hounors and Become Lecturare'
                  '\n','You Also Have More Options like:B.Com,BBA, and for more info search on internet') 
        # Adding Grade of Student Marks                 
        grade=(subject_1_marks+subject_2_marks+subject_3_marks+subject_4_marks+subject_5_marks+subject_6_marks+subject_7_marks+subject_8_marks)/8   
        if grade>=90:
            print("A Grade:",grade,'%')
        elif grade>=70 and grade<90:
            print("B Grade",grade,'%')
        elif grade>=50 and grade<70:
            print('C Grade ',grade,'%')
        elif grade>=35 and grade<50:
            print('D Grade',grade,'%')    
        else:
            print("FAIL")                        
    else:
        print("Enter Stream only science and arts and commerce ")