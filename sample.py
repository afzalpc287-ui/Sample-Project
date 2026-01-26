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
    Maths_Marks=int(input("Maths Marks:"))
    science=int(input("Science marks:"))
    social_science=int(input('Social Science marks:'))
    hindi=int(input('Hindi marks:'))
    english=int(input('English marks:'))
    # Convert input to Dataframe
    subjects={'Name':[Name],
              'Maths':[Maths_Marks],
              'Science':[science],
              'Social Science':[ social_science],
              'Hindi':[hindi],
              'English':[english]}
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
    grade=(Maths_Marks+science+social_science+hindi+english)/5    
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
    print('Now PLease Enter your Stream')
    # Taking input sream for better Analyse
    stream=str(input('stream:'))
    # Science Stream Start
    if stream =="Science" or stream== 'science':
        #  11 or 12 class Science Stream Students enter Name and Subject
        print('Now Please Enter Your Details')
        Name=str(input("Name:"))
        Maths_Marks=int(input("Maths Marks:"))
        physics=int(input("Physics Marks:"))
        chemistry=int(input('Chemistry Marks:'))
        biology=int(input('Biology Mraks:'))
        hindi=int(input('Hindi Marks:'))
        english=int(input('English Marks:'))
         # Convert input to Dataframe
        subjects={'Name':[Name],
              'Maths':[Maths_Marks],
              'Physics':[physics],
              'Chemistry':[chemistry],
              'Biology':[biology],
              'Hindi':[hindi],
              'English':[english]}
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
        grade=(Maths_Marks+physics+chemistry+biology+hindi+english)/6    
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
    elif stream == "Arts" or stream== 'arts':     
        print('Now Please Enter Your Details')
        # 11 or 12 class Arts Stream Students enter Name and Subject
        Name=str(input("Name:"))
        Geography=int(input("Geography Marks:"))
        history=int(input("History Marks:"))
        political_science=int(input('Political Science Marks:'))
        sociology=int(input('Sociology Marks:'))
        economics=int(input('Economics Marks:'))
        hindi=int(input('Hindi Marks:'))
        english=int(input('English Marks:'))
        # Convert input to Dataframe
        subjects={'Name':[Name],
              'Geography':[Geography],
              'History':[history],
              'Political Science':[political_science],
              'Sociology':[sociology],
              'Economics':[economics],
              'Hindi':[hindi],
              'English':[english]}
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
        grade=(Geography+history+political_science+sociology+economics+hindi+english)/7   
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
        Accounts=int(input("Accounts Marks:"))
        Maths_Marks=int(input("Maths Marks:"))
        business=int(input('Business Marks:'))
        economics=int(input('Economics Marks:'))
        enterpre=int(input('Enterprenuership Marks:'))
        legal_study=int(input('Legal Studies Marks:'))
        hindi=int(input('Hindi Marks:'))
        english=int(input('English Marks:')) 
        # Convert input to Dataframe
        subjects={'Name':[Name],
              'Maths':[Maths_Marks],
              'Accounts':[Accounts],
              'Business':[business],
              'Economics':[economics],
              'Enterpreneur':[enterpre],
              'Legal Study':[legal_study],
              'Hindi':[hindi],
              'English':[english]}
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
        grade=(Accounts+Maths_Marks+business+economics+enterpre+legal_study+hindi+english)/8   
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
        print("Enter Stream only science and arts")