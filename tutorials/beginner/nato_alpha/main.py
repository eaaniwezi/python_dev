import pandas

student_data = pandas.read_csv("nato_phonetic_alphabet.csv")

student_dict = {row.letter:row.code for index,row in student_data.iterrows()}

 

def generate_phonetics():
    user_input = input("Enter a word").upper()
    try:
        result = [student_dict[char] for char in user_input]
    except KeyError:
        generate_phonetics()
        print("Please enter characters in the English Alphabet only")
    else:    

        print(result)
        
 
generate_phonetics()