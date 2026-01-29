# Sample of my First Project
# Importing Librarys
import pandas as pd
import matplotlib.pyplot as mlt
import seaborn as sns
# Create Function to make code short
#input Function 1
def get_marks(Subject):
    marks=int(input(f'Enter {Subject} Marks:'))
    while marks <0 or marks >100:
        print ('❌ Marks must be between 0 and 100')
        marks=int(input(f'Enter {Subject} Marks:'))
    return marks
# 2
def get_stream():
    valid_stream=['science','arts','commerce']
    while True:
        stream=input('Stream( Science / Arts / commerce):').strip().lower()
        if stream in valid_stream:
            return stream
        else:
            print("❌ Enter valid stream: science, arts, or commerce")
#Plotting Function
def plot_marks(df,name):
     df_melt = df.melt(id_vars='Name', var_name='Subject', value_name='Marks')
     sns.catplot(data=df_melt, x='Subject', y='Marks', kind='bar',hue='Subject',palette='pastel',legend=False)
     mlt.title(f'{name}-Subjects Progress Comparison')
     mlt.show()
#Calculating function     
def grade_calculate(marks):
     avg= sum(marks) / len(marks)
     if avg>=90:
         return "A ",avg
     elif avg>=70 and avg<90:
         return "B ",avg
     elif avg>=50 and avg<70:
         return 'C ',avg
     elif avg>=35 and avg<50:
         return 'D ',avg    
     else:
         return "FAIL❌ Need Improvement",avg               
def collect_and_analyze(name, total_subjects):
    subjects = []
    marks = []
    for i in range(total_subjects):
        sub = input(f"Enter Subject {i+1}: ")
        subjects.append(sub)
    for sub in subjects:
        marks.append(get_marks(sub))
    data = {'Name': [name]}
    for i in range(len(subjects)):
        data[subjects[i]] = [marks[i]]
    df = pd.DataFrame(data)
    print(df)
    plot_marks(df, name)
    grade, avg = grade_calculate(marks)
    print(f"{grade} Grade: {avg:.2f}%")
    return marks                        
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
if classes in (9,10):
    print('Now Please Enter Your Details')
    Name=str(input("Name:"))
    marks = collect_and_analyze(Name, 5)
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
#  11 or 12 class Start
elif classes in (11 , 12):
    # Input stream 
    stream=get_stream()
    if stream == 'science':
         print('Now Please Enter Your Details')
         Name=str(input("Name:"))
         marks = collect_and_analyze(Name, 5)
    elif stream == 'arts':
         print('Now Please Enter Your Details')
         Name=str(input("Name:"))
         marks = collect_and_analyze(Name, 7)
    elif stream == 'commerce':
         print('Now Please Enter Your Details')
         Name=str(input("Name:"))
         marks = collect_and_analyze(Name, 8)     
    # Science Stream
    if stream== 'science':
        stream_subject=str(input('Enter Your Subject is PCB or PCM:')).lower()
        valid_streamsubject=['pcb','pcm']
        while stream_subject not in valid_streamsubject:
            print('Enter Valid Subject:')
            stream_subject=str(input('Enter Your Subject is PCB or PCM:')).lower()
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
    # Arts Stream Start                     
    elif stream== 'arts':
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
    # Commerce Stream Start                       
    elif stream=="commerce":
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
    else:
        print("Enter Stream only science,arts and commerce ")