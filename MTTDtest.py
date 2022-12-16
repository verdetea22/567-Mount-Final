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
      """
      @patch('MRTD.scan')
      
      def testScanMRZ(self,mock_scan):
            
            data = "P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<\nL898902C36UTO7408122F1204159ZE184226B<<<<<<1"
            mock_scan.return_value = data

            self.assertEqual("P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<\nL898902C36UTO7408122F1204159ZE184226B<<<<<<1", scanMRZ())

      
      
      """
      Testing Function 2: Decode the MRZ's two strings and cacluate check digits   
      """
      def testDecodeMRZ(self):
            testString = "P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<;L898902C36UTO7408122F1204159ZE184226B<<<<<<1"
            self.assertEqual(decodeMRZ(testString).get("document_type"), "P")
            self.assertEqual(decodeMRZ(testString).get("issuing_country"), "UTO")
            
            self.assertEqual(decodeMRZ(testString).get("first_name"), "ANNA")
            self.assertEqual(decodeMRZ(testString).get("last_name"), "ERIKSSON")
            self.assertEqual(decodeMRZ(testString).get("middle_name"), "MARIA")
            self.assertEqual(decodeMRZ(testString).get("birth_date"), "740812")
            self.assertEqual(decodeMRZ(testString).get("sex"), "F")
            
            self.assertEqual(decodeMRZ(testString).get("expiration_date"), "120415")
            self.assertEqual(decodeMRZ(testString).get("passport_number"), "L898902C3")
            self.assertEqual(decodeMRZ(testString).get("personal_number"), "ZE184226B")
            
            self.assertEqual(decodeMRZ(testString).get("checkdigit1"), "6")
            self.assertEqual(decodeMRZ(testString).get("checkdigit2"), "2")
            self.assertEqual(decodeMRZ(testString).get("checkdigit3"), "9")
            self.assertEqual(decodeMRZ(testString).get("checkdigit4"), "1")

      
      """
      Testing Function 3: Encode travel information fields queried from a database into the two strings for the MRZ
      """
      #Test find check digit based on typical value
      def testsFindCheckDigit(self):
            st = "L898902C3"
            self.assertEqual(calcCheckDigit(st), "6")

      #Test find check digit of a string of length 0
      def testFindCheckDigitOfEmptryString(self):
            st = ""
            self.assertEqual(calcCheckDigit(st), "0")

      # Test adding < to the end of a string
      def testPadString(self):
            st = padString("A", 10)
            self.assertEqual(st, "A<<<<<<<<<")

      #Test getting weight array for given length
      def testDigitWeight(self):
            arr = digitWeight(7)
            self.assertEqual(arr, [7, 3, 1, 7, 3, 1, 7])

      #Test getting value of a letter
      def testAlphaNum(self):
            self.assertEqual(calcAlphaNum("B"), 11)

      #Test getting value of a number
      def testAlphaNumOfNumber(self):
            self.assertEqual(calcAlphaNum("3"), 3)

      #Test getting value of a symbol
      def testAlphaNumOfSymbol(self):
            self.assertEqual(calcAlphaNum("<"), 0)

      #Test encode functionality with given passport number
      @patch('MRTD.getMRTDInfo')
      def testEncode(self, mock_get_MRTDInfo):
            # issuing_country, first_name, last_name, middle_name,birth_date, sex, expiration_date, personal_number
            data = "UTO", "ANNA", "ERIKSSON", "MARIA", "740812", "F", "120415", "ZE184226B"
            mock_get_MRTDInfo.return_value = data

            self.assertEqual(
                  "P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<\nL898902C36UTO7408122F1204159ZE184226B<<<<<<1", encode("L898902C3"))
            
            return()
      
      """
      Function 4: Report a mismatch between certain information fields and the check digit. The system shall report where error occured relative to check digit
      """
      def nonError(self):
            
            # Testing with accurate credentials 
            self.assertEqual(errorMRZ("P<NICLOUGHLIN<<PERCY<ANDREW<<<<<<<<<<<<<<<<<\n5986721677NIC0108168M2401014TR913125H<<<<<<6",
            "NIC", "PERCY", "LOUGHLIN", "ANDREW", "010816", "M", "240101", "598672167", "TR913125H"), "No mismatches found")
        
      
      def testErrorMRZ(self):
            
            #Testing with incorrect final check digit
            self.assertEqual(errorMRZ("P<NICLsOUGHLIN<<PERCY<ANDREW<<<<<<<<<<<<<<<<<\n5986721677NIC0108168M2401014TR913125H<<<<<<8",
            "NIC", "PERCY", "LOUGHLIN", "ANDREW", "010816", "M", "240101", "598672167", "TR913125H"),
             "Errors found in: " + "\nPersonal number " + "6" + " != " + "8")
            
             #Testing with incorrect expiration date check digit
            self.assertEqual(errorMRZ("P<NICLOUGHLIN<<PERCY<ANDREW<<<<<<<<<<<<<<<<<\n5986721677NIC0108168M2401015TR913125H<<<<<<6",
            "NIC", "PERCY", "LOUGHLIN", "ANDREW", "010816", "M", "240101", "598672167", "TR913125H"),
            "Errors found in: " + "\nExpiration date " + "4" + " != " + "5")
            
            return()  

if __name__ == '__main__':
    print('Running unit tests...')
    unittest.main()