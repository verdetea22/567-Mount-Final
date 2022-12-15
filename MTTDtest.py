import unittest

from MRTD import *
from unittest.mock import patch


class TestMRTD(unittest.TestCase):
      
      """
      Write test cases to test each function you implemented
      Please provide comments to each test case you create to explain what the test case is testing. Please report the coverage of your test cases.
      Output screenshot for coverage should indicate >80% coverage.
      """

      """
      Testing Function 1: Get the information in MRZ as two strings 
      Input: Scanned MRZ lines (string) 
      Output: Validation (boolean)    
      """
      @patch('MRTD.scan')
      
      def testScanMRZ(self,mock_scan):
            
            data = "P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<\nL898902C36UTO7408122F1204159ZE184226B<<<<<<1"
            mock_scan.return_value = data

            self.assertEqual("P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<\nL898902C36UTO7408122F1204159ZE184226B<<<<<<1", scanMRZ())

      
      
      """
      Testing Function 2: Decode the MRZ's two strings and cacluate check digits   
      Input: Scanned MRZ lines (string) 
      Output: Validation (boolean) 
      """
      def testDecodeMRZ():
            testString = "P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<;L898902C36UTO7408122F1204159ZE184226B<<<<<<1"
            self.assertEqual(decodeMRZ(testString).get("document_type"), "P")
            self.assertEqual(decodeMRZ(testString).get("issuing_country"), "UTO")
            self.assertEqual(decodeMRZ(testString).get("first_name"), "ANNA")
            self.assertEqual(decodeMRZ(testString).get("last_name"), "ERIKSSON")
            self.assertEqual(decodeMRZ(testString).get("middle_name"), "MARIA")
            self.assertEqual(decodeMRZ(testString).get("birth_date"), "740812")
            self.assertEqual(decodeMRZ(testString).get("sex"), "F")
            self.assertEqual(decodeMRZ(testString).get("expiration_date"), "120415")
            self.assertEqual(decodeMRZ(testString).get(
            "passport_number"), "L898902C3")
            self.assertEqual(decodeMRZ(testString).get(
            "personal_number"), "ZE184226B")
            self.assertEqual(decodeMRZ(testString).get("checkdigit1"), "6")
            self.assertEqual(decodeMRZ(testString).get("checkdigit2"), "2")
            self.assertEqual(decodeMRZ(testString).get("checkdigit3"), "9")
            self.assertEqual(decodeMRZ(testString).get("checkdigit4"), "1")

      
      """
      Testing Function 3: Encode travel information fields queried from a database into the two strings for the MRZ
      Input: Decoded info (string), Encoded info (string) 
      Output: Validation (boolean) 
      """
      def testEncodeMRZ():
            
            return()
      
      """
      Function 4: report a mismatch between certain information fields and the check digit. The system shall report where error occured relative to check digit
      Input: Scanned MRZ lines (string), Mismatched info (string) 
      Output:  Validation (boolean) 
      """
      def testErrorMRZ():
            
            return()  

if __name__ == '__main__':
    print('Running unit tests...')
    unittest.main()