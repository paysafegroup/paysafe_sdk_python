------------------------------------------------------------------------------------
Synopsis:
------------------------------------------------------------------------------------

        
------------------------------------------------------------------------------------
Installation:
------------------------------------------------------------------------------------
I) Following steps are mentioned with respect to Linux/Macintosh Operating Systems:


1.If Ubuntu/Macintosh machine does not have python 3x version installed then we 
have to upgrade the python version.

	sudo apt-get upgrade python

	Python upgraded version can be confirmed using following command:
	sudo python3 -V
	Sample Output: Python 3.4.0

2.Install/ Upgrade required python packages before starting Paysafe setup.
	
	Urllib3 and certifi are two necessary packages need to be installed before 
    starting PaysafeSDK setup.

	Python may have a pre-installed packages for urllib3 which may not be the 
    latest version.
	To install/upgrade use following commands:
	sudo python3 �m pip install urllib3==1.10.2
	sudo python3 �m pip install certifi

3.Install PaysafeSDK using following command:

	Goto this directory: PythonSDK/src
	Command: sudo python3 setup.py install

	In case if a tar file is provided, execute following command:
	sudo python3 �m pip install <tar ball file>

	Example: sudo python3 �m pip install paysafe==1.0

4.To execute automation  test scripts, execute following steps:

	Goto this directory: PythonSDK/TestCases
	Command: sudo python3 StartExecution.py

	Upon successful execution of StartExecution.py an html file will be 
    generated in the same directory named Report.html.
	This file will provide a detailed report of all test cases for 3 API�s:
		I.   Customer Vault Service
	    II.  Card Payment Service
		III. Direct Debit Service
		IV.  Three D Secure Service

	Note:
	Green mark indicates API has a success response, whereas
	Red mark indicates failure response.


II) Following steps are mentioned with respect to Windows Operating System:


1.If Windows machine does not have python 3x version installed then we have to 
install it from https://www.python.org/downloads/:

	python -V
	Sample Output: Python 3.4.0

2.Install/ Upgrade required python packages before starting PaysafeSDK setup.
	
	Urllib3 and certifi are two necessary packages need to be installed before 
    starting PaysafeSDK setup.

	Python may have a pre-installed packages for urllib3 which may not be the 
    latest version.
	To install/upgrade use following commands:
	python �m pip install urllib3
	python �m pip install certifi

3.Install PaysafeSDK using following command:

	Goto this directory: PythonSDK/src
	Command: python -m pip setup.py install

	In case if a tar file is provided, execute following command:
	python �m pip install <tar ball file>

	Example: python �m pip install paysafe==1.0

4.To execute automation  test scripts, execute following steps:

	Goto this directory: PythonSDK/TestCases
	Command: python StartExecution.py

	Upon successful execution of StartExecution.py an html file will be 
    generated in the same directory named Report.html.
	This file will provide a detailed report of all test cases for 3 API�s:
		I.   Customer Vault Service
	    II.  Card Payment Service
		III. Direct Debit Service
		IV.  Three D Secure Service

	Note:
	Green mark indicates API has a success response, whereas
	Red mark indicates failure response.

------------------------------------------------------------------------------------
API Reference:
------------------------------------------------------------------------------------
https://developer.optimalpayments.com/en/documentation/


------------------------------------------------------------------------------------
Code Example:
------------------------------------------------------------------------------------
Verify That the Service Is Accessible for Direct Debit:

'''
Monitoring Direct Debit Services
'''
response_object = self.paysafe_obj_ACH.direct_debit_service_handler().monitor()
print ("\nResponse Values ==========> ")
Utils.print_response(response_object)


------------------------------------------------------------------------------------
Tests:
------------------------------------------------------------------------------------
Firstly, set confirgurations in samples/Config.py

To run sample applications, start server and execute following command:
python ExecuteScriptServer.py

Example for Direct Debit Purchase request for ACH Bank Account:

To run sample open below URL in browser after server starts successfully,
http://localhost:3000/DirectDebitACHpurchase.py