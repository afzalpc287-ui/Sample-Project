# Sample of my First Project
# Importing Librarys
import numpy as np
import pandas as pd
import matplotlib.pyplot as mlt
import seaborn as sns
# Create Function For Marks Validation
def get_marks(Subject):
    marks=int(input(f'Enter {Subject} Marks:'))
    while marks <0 or marks >100:
        print ('❌ Marks must be between 0 and 100')
        marks=int(input(f'Enter {Subject} Marks:'))
    return marks
def plot_marks(df,name):
     df_melt = df.melt(id_vars='Name', var_name='Subject', value_name='Marks')
     sns.catplot(data=df_melt, x='Subject', y='Marks', kind='bar')
     mlt.title(f'{name}-Subjects Progress Comparison')
     mlt.show()
def get_stream():
    valid_stream=('science','arts','commerce')
    while True:
        stream=input('Stream( Science / Arts / commerce):').strip().lower()
        if stream in valid_stream:
            return stream
        else:
            print("❌ Enter valid stream: science, arts, or commerce")     
# Using While Loop for Enter Class
print('Hello Students...Please Enter Your Class')
valid_class = [9, 10, 11, 12]
while True:
    try:
        classes = int(input("class: "))
        if classes in valid_class:
            break
        else:
            print("❌ Enter only 9 to 12")
    except ValueError:
        print("❌ Please enter numbers only")
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
    subject_1_marks=get_marks(subject_1)
    subject_2_marks=get_marks(subject_2)
    subject_3_marks=get_marks(subject_3)
    subject_4_marks=get_marks(subject_4)
    subject_5_marks=get_marks(subject_5)
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
    plot_marks(df, Name)
    # Taking Input from Student of Interesting Subject
    interest=input('Enter Your Interested Subjects:').lower()
    # Suggest Career Option to Student Basis on Interested Subject
    valid_subject=['maths','science','social science','accounts']
    while interest not in valid_subject:
        print('❌Enter Valid Subject')
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
    # Taking input sream for better Analyse
    stream = get_stream()
    # Science Stream Start
    if stream== 'science':
        stream_subject=str(input('Enter Your Subject is PCB or PCM:')).lower()
        valid_streamsubject=['pcb','pcm']
        while stream_subject not in valid_streamsubject:
            print('Enter Valid Subject:')
            stream_subject=str(input('Enter Your Subject is PCB or PCM:')).lower()
        #  11 or 12 class Science Stream Students enter Name and Subject
        print('Now Please Enter Your Details')
        Name=str(input("Name:"))
        subject_1=str(input('Enter Subject 1:'))
        subject_2=str(input("Enter Subject 2:"))
        subject_3=str(input("Enter Subject 3:"))
        subject_4=str(input("Enter Subject 4:"))
        subject_5=str(input("Enter Subject 5:"))
        subject_1_marks=get_marks(subject_1)
        subject_2_marks=get_marks(subject_2)
        subject_3_marks=get_marks(subject_3)
        subject_4_marks=get_marks(subject_4)
        subject_5_marks=get_marks(subject_5)
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
        plot_marks(df, Name)
        # Taking Input from Student of Interesting Subject
        interest=input('Enter Your Interested Subjects:').lower()
        valid_subject=['maths','physics','chemistry','biology','hindi','english']
        # Suggest Career Option to Student Basis on Interested Subject
        while interest not in valid_subject:
          print('❌Enter Valid Subject')
          interest=input('Enter Your Interested Subjects:').lower()
        if interest in ['physics','maths','chemistry']:
            print("Just Do JEE MAINS and Get Admission in B.Tech Engineering")
        elif interest in ['biology']:
            print("Just Do NEET and Get Admission in MBBS or Pharmacy"
                  '\n','You Also Have More Options like:D.Pharma,B.Phharma, and for more info search on internet')
        elif interest in  ['hindi','english']:
            print('Just Do CUET and Get Admission in', interest,'hounors and Become Lecturare',
                  '\n','You Also Have More Options like:D.Pharma,B.Phharma, and for more info search on internet' )
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
    # Arts Stream Start                     
    elif stream== 'arts':     
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
        subject_1_marks=get_marks(subject_1)
        subject_2_marks=get_marks(subject_2)
        subject_3_marks=get_marks(subject_3)
        subject_4_marks=get_marks(subject_4)
        subject_5_marks=get_marks(subject_5)
        subject_6_marks=get_marks(subject_6)
        subject_7_marks=get_marks(subject_7)
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
        plot_marks(df, Name)
        # Taking Input from Student of Interesting Subject
        interest=input('Enter Your Interested Subjects:').lower()
        valid_subject=['geography','history','political science','sociology','economics','hindi','english']
        # Suggest Career Option to Student Basis on Interested Subject
        while interest not in valid_subject:
            print('❌Enter Valid Subject')
            interest=input('Enter Your Interested Subjects:').lower()
        if interest in ['geography','history','political science']:
            print("Just Do UPSC or SSC and Become an IAS or IPS Officer",
                  '\n','You Also Have More Options like:BCA,BBA,IT Feild and for more info search on internet')
        elif interest in ['sociology','economics','hindi','english']:
            print('Just Do CUET and Get Admission in', interest,'hounors and Become Lecturare'
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
    # Commerce Stream Start                       
    elif stream=="commerce":     
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
        subject_1_marks=get_marks(subject_1)
        subject_2_marks=get_marks(subject_2)
        subject_3_marks=get_marks(subject_3)
        subject_4_marks=get_marks(subject_4)
        subject_5_marks=get_marks(subject_5)
        subject_6_marks=get_marks(subject_6)
        subject_7_marks=get_marks(subject_7)
        subject_8_marks=get_marks(subject_8)
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
        plot_marks(df, Name)
        # Taking Input from Student of Interesting Subject
        interest=input('Enter Your Interested Subjects:').lower()
        valid_subject=['maths','accounts','business','economics','hindi','english','enterpreneur','legal study']
        # Suggest Career Option to Student Basis on Interested Subject
        while interest not in valid_subject:
            print('❌Enter Valid Subject')
            interest=input('Enter Your Interested Subjects:').lower()
        if interest in ['maths','accounts','economics','business','legal study']:
            print("You have two best options CA(Chartered Accountant) and CS(Company Secretary)"
                  '\n','You Also Have More Options like:B.Com,BBA, and for more info search on internet')
        elif interest in ['enterpreneur']:
            print("Just Do Enterpreneur Course and Become an Enterprenuer"
                  '\n','You Also Have More Options like:B.Com,BBA, and for more info s# Adding Grade of Student Marks earch on internet')
        elif interest in  ['hindi','english']:
            print('Just Do CUET and Get Admission in', interest,'hounors and Become Lecturare'
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
        print("Enter Stream only science,arts and commerce ")