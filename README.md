### Restful-Booker API Testing

To create this automated API test cases for the page [Restful-booker](https://restful-booker.herokuapp.com/apidoc/index.html) we use Python and PyTest, here you can check the following steps:

1. **Set Up Your Environment**:

   Ensure you have Python and PyTest installed on your system. Otherwise, you can install PyTest using the following command line:

   ```
   pip install pytest requests
   ```


2. **Run the Tests**:

   Open your terminal and navigate to the directory containing the test file (`test_create_token.py`) and run the tests using the following command:

   ```
   pytest -v test_create_token.py
   ```

   PyTest will discover and execute the test cases, and you'll see the test results in the terminal.

3. **Review the Test Results**:

   Check the test results to ensure that your API endpoints are working as expected.

