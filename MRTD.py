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
Function 1: Get the information in MRZ as two strings     
Input: Scanned MRZ lines (string)
"""
def scanMRZ():
      
      #first_line = ""
      #second_line = ""
      #return ( first_line + "+" + second_line )
      
      #reads the document, scans the two lines of information
      def scan(MRZ):
            return "travel information"
      
      return scan(MRZ=any)


"""
Function 2: Decode the MRZ's two strings and cacluate check digits   
Input: Scanned MRZ lines (string) 
Output: Decoded info (list), Check Digit (int)

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
            "passport_num": "",
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
      first_line = list(MRZ_s.split("+"))[0]
      second_line = list(MRZ_s.split("+"))[1]
      
      # create lists, filter out "<" characters 
      first_line_list = list(filter(None, list(first_line.split("<"))))
      second_line_list = list(filter(None, list(second_line.split("<"))))
      
      #populate lists with information // first string
      info_fields["document_type"] = first_line_list[0]
      info_fields["last_name"]= first_line_list[1][3::]
      info_fields["first_name"] = first_line_list[2]
      info_fields["middle_name"] = first_line_list[3]
      
      #populate lists with information // second string
      info_fields["passport_number"] = second_line_list[0:9]

"""
Function 3: Encode travel information fields queried from a database into the two strings for the MRZ
Input: Decoded info (string) 
Output: Encoded info (list) """

def encodeMRZ():
      
      return()

"""
Function 4: report a mismatch between certain information fields and the check digit. The system shall report where error occured relative to check digit
Input: Scanned MRZ lines (string),  
Output: Mismatched info (string)
Author:
"""
def errorMRZ():
      
      return()
