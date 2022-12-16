"""
567 A/AU Final
Mikayla Mount
Dr Bondi

I pledge my Honor that I have abided by the Stevens Honor System. 

USING Python 3.7.15
Implement the functions for the four requirement specifications. 
      1 The system shall be able to scan the MRZ of a travel document using a hardware device scanner and get the information in MRZ as two strings (line 1 and line 2 from the above Figure). Note that you do not need to worry about the implementation of the hardware device. But you need to define this method for the software part. This means that you define an empty method for this function. 
      2 The system shall be able to decode the two strings from specification #1 into their respective fields and identify the respective check digits for the fields, following the same format in the above example.
      3 The system shall be able to encode travel document information fields queried from a database into the two strings for the MRZ in a travel document. This is the opposite process compared to specification #2. Assume that the database function is not ready. But for testing purposes, you need to define a method for database interaction and leave it empty.
      4 The system shall be able to report a mismatch between certain information fields and the check digit. The system shall report where the miss match happened, i.e. which information field does not match its respective check digit.
"""

"""
Function 1: Get the information in MRZ as one string     
Input: No input
Return: string of both lines (string)
"""
def scanMRZ():
      
      #first_line = ""
      #second_line = ""
      #return ( first_line + "+" + second_line )
      
      #reads the document, scans the two lines of information
      
      return scan(MRZ=any)

def scan(MRZ):
      return "travel information"

"""
Function 2: Decode the MRTD's two strings and format    
Input: Scanned MRZ lines (string) 
Output: dictionary of data types 
"""
def decodeMRZ(MRZ_s):
      
      #dictionary of all fields on travel document
      info_fields = {
            
      #line one
            "document_type": "",
            "issuing_country": "",
            "first_name": "",
            "middle_name": "",
            "last_name": "",
            
      #line two
            "passport_number": "",
            "country_code": "",
            #YYMMDD
            "birth_date": "",
            "sex": "",
            #YYMMDD
            "expiration_date": "",
            "personal_number": "",
            
      #check digits
            "checkdigit1": "",
            "checkdigit2": "",
            "checkdigit3": "",
            "checkdigit4": "",  
      }
      
      # seperate travel info into two seperate variables
      first_line = list(MRZ_s.split(";"))[0]
      second_line = list(MRZ_s.split(";"))[1]
      
      # create lists, filter out "<" characters 
      first_line_list = list(filter(None, list(first_line.split("<"))))
      second_line_list = list(filter(None, list(second_line.split("<"))))
      
      #populate first string list with information 
      info_fields["document_type"] = first_line_list[0]
      info_fields["last_name"]= first_line_list[1][3::]
      info_fields["first_name"] = first_line_list[2]
      info_fields["middle_name"] = first_line_list[3]
      
      #populate second list with information // checkdigits appear between every few fields
      info_fields["passport_number"] = second_line_list[0:9]
      info_fields["checkdigit1"] = second_line_list[9]
      info_fields["issuing_country"]= second_line_list[10:13]
      info_fields["birth_date"]= second_line_list[13:19]
      info_fields["checkdigit2"] = second_line_list[19]
      info_fields["sex"] = second_line_list[20]
      info_fields["expiration_date"] = second_line_list[21:27]
      info_fields["checkdigit3"] = second_line_list[27]
      info_fields["personal_number"] = second_line_list[28:37]
      info_fields["checkdigit4"] = second_line_list[43]
      
      return info_fields
      

"""
Function 3: Encode travel information fields queried from a database into the two strings for the MRTD, calculate check digits based on format
Input: Identifier (string) 
Output: Two encoded lines (string) """

string_len = 44

def encode(passport_number):
      
      #calling method to retrive travel info
      issuing_country, first_name, last_name, middle_name,birth_date, sex, expiration_date, personal_number = getMRTDInfo(passport_number) 
      return encodeData(issuing_country, first_name, last_name, middle_name,birth_date, sex, expiration_date, personal_number)


#getting info from database
def getMRTDInfo(passport_number):
      # first_line = [passport_number.type_of_passport, passport_number.issuing_country, passport_number.name]
      # second_line = [passport_number.country_code, passport_number.birthdate, passport_number.gender, passport_number.expiration, passport_number]
      # MRTD = [string_one, string_two]
      print("Information regarding " + passport_number)
      
      
# Formatting of document feild       
def padString(string, intended_length):
    while (len(string) < intended_length):
        string = string + "<"
    return string

# Method to associate numeric values to letters and numbers   
def calcAlphaNum(character):
    if type(character) == int or character.isnumeric():
        return int(character)
    elif character.isalpha():
        return ord(character.upper()) - 55
    else:
        return 0


# Check Digit = sum of products, divison by modulus 
def calcCheckDigit(name):
    arr = list(str(name))
    weights = digitWeight(len(arr))
    products = []
    for i in range(len(arr)):
        products.append(weights[i] * calcAlphaNum(arr[i]))

    return str(sum(products) % 10)

# Weighting sequence (use 7,3,1)
def digitWeight(length):
    amt = (length // 3) + 1
    arr = amt * [7, 3, 1]
    return arr[:length]


def encodeData(issuing_country, first_name, last_name, middle_name, birthdate, gender, expiration, passport_number, personal_number):

    # compiles first string 
    first_string = "P<" + issuing_country + last_name + \
        "<<" + first_name + "<" + middle_name
    if (len(first_string) < string_len):
        first_string = padString(first_string, string_len)

    if (len(passport_number) < 9):
        passport_number = padString(passport_number, 9)

    checkdigit1 = calcCheckDigit(passport_number)
    checkdigit2 = calcCheckDigit(birthdate)
    checkdigit3 = calcCheckDigit(expiration)
    checkdigit4 = calcCheckDigit(personal_number)

    # compiles second string 
    second_string = passport_number + checkdigit1 + issuing_country + birthdate + \
        checkdigit2 + gender + expiration + checkdigit3 + personal_number
    if (len(second_string) < string_len - 1):
        second_string = padString(second_string, string_len - 1)
    second_string = second_string + checkdigit4

    # returns both strings
    return first_string + "\n" + second_string
"""
Function 4: report a mismatch between certain information fields and the check digit. The system shall report where error occured relative to check digit
Input: Scanned MRZ lines (string),  
Output: Mismatched info (string)
Author:
"""
def errorMRZ(MRZ_string, issuing_country, first_name, last_name, middle_name, birth_date, sex, expiration_date, passport_number, personal_number):
      
      #encode info to get expected result
      encode_result = encodeData(issuing_country, first_name, last_name, middle_name, birth_date, sex, expiration_date, passport_number, personal_number)
      
      #return message if no error
      error_message = "Passed: No mismatches"
      
      #checks if there is any error, if not return no mismatch
      if MRZ_string == encode_result:
            return error_message
      
      #checks if there is any error, if there return mismatch
      else:
            error_message = "Error found: "
            
            #checks if general passport is formatted correctly
            if len(MRZ_string) != len(encode_result):
                  error_message  = "Passport ID length invalid"
            
            #checks for errors intermittenly at each checkdigit 
            if MRZ_string[54] != encode_result[54]:
                  error_message = error_message + "\nPassport number " + encode_result[54] + " != " + MRZ_string[54]
            
            if MRZ_string[64] != encode_result[64]:
                  error_message = error_message + "\nBirth date " + encode_result[64] + " != " + MRZ_string[64]
            
            if MRZ_string[72] != encode_result[72]:
                  error_message = error_message + "\nExpiration date " + encode_result[72] + " != " + MRZ_string[72]
            
            if MRZ_string[88] != encode_result[88]:
                  error_message = error_message + "\nPersonal number " + encode_result[88] + " != " + MRZ_string[88]

      return error_message