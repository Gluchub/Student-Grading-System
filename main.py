from abc import ABC, abstractmethod
import re
class students:
    proffesion="i am instructor"
    def _init_(self, name):
        self.character=name
    @abstractmethod
    def marks_of_student(self,name,marks):
        #intializing marks
        self.marks=marks
        #intializing name
        self.name=name
        #opening the file with student name and editing its marks
        with open(f"{name}.txt", "r")as reads:
            file_info=reads.read()
        reads.close()
        #finding all subjects in the text file
        subs=re.compile(r'Science|English|Maths|History|Avg_marks').findall(file_info)
        #A list with all subjects
        subjects=[sub for sub in subs if len(sub)>1]
        #finding all numbers importantly marks of each subject in the text file
        nums=re.compile(r'[1-9]*.[1-9]*|[1-9][1-9]').findall(file_info)
        #A list with all respective numbers
        score=[num for num in nums if len(num)>1]
        #Marking dictionary with a particular subject and marks scored in it
        subject_with_marks={}
        for keys,values in zip(subjects,score):
            subject_with_marks.update({keys:values})
        #Asking user in which subject he or she want to commit change in their marks
        subject=input("Enter subject name here\n").capitalize()
        #checking wheather the given input exists in the given list or not
        if subject in subjects:
            #intializing original_marks and Avg_marks with there existed values
            original_marks=subject_with_marks.get(subject)
            Avg_marks=f"{score[-1]}"
            #Opeaning the respective student file
            with open(f"{name}.txt", "r+")as reads:
                file_info1=reads.read()
                #Replacing original marks by updated marks
                file_info2=file_info1.replace(original_marks, f" {str(marks)}")
                #Matching original marks each respective item in list inorder to obtain its number useful for slicing
                #by using enumerate function 
                for iter_num,item in enumerate(score):
                    if original_marks==item:
                        #replacing marks at the place of original marks
                        score.insert(iter_num, marks)
                        #removing its original value
                        score.remove(item)
                #intializing new_score
                new_score=0
                #this for loop function is made for changing value of average number
                for inte in score[0:-1]:
                    new_score+=int(inte)/len(score[0:-1])
                new_Avg_score=f" {new_score}"
                #replacing average marks by new average marks
                file_info3=file_info2.replace(Avg_marks, new_Avg_score)
            reads.close()
        #overwriting the previous value by obtained value
        with open(f"{name}.txt", "w")as writes:
            writes.write(file_info3)
        writes.close()
    #function which shows students info
    @abstractmethod
    def student_info(self, name):
        with open(f"{name}.txt", "r")as reads:
            file_txt=reads.read()
            print(file_txt)
    #function that shows class info
    @abstractmethod
    def classes_info(self):
        class_info=open("class_info.txt", "r").read()
        print(class_info)
#intializing user as class object
user=students()
if __name__=="__main__":
    #printing details
    print("You have three options\n1)Edit the marks of the student. type 1 to proceed\n2)Display students info. type 2 to proceed\n3)Display class info. type 3 to proceed")
    #taking user request
    try:
        command=int(input("Type here\n"))
    except:
        print("Expecting the integer")
    else:
        if command==1:
            user.marks_of_student(input("Enter Student Name here\n"),int(input("Enter Student Marks here (note marks should be an integer)\n")))
        if command==2:
            user.student_info(input("Enter student name stored with txt file\n"))
        if command==3:
            user.classes_info()