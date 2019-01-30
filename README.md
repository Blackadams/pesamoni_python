# Pesamoni Python library

The Pesamoni Pesaway python Library provides integration access to Pesamoni services. You can view API features by clicking the link https://pesamoni.com/developers#features-intro.

## Requirements.

Python 2.7 and 3.4+

## Installation

### pip install

You can install the package directly from Github using [this link](https://github.com/Pesamoni/pesamoni_python) or using pip

```sh
pip install https://github.com/Pesamoni/pesamoni_python.git
```
(you may need to run `pip` with root permission: `sudo pip install https://github.com/Pesamoni/pesamoni_python.git`)

Then import the package:
```python
import pesamoni_python 
```
## Quick Start Example

The SDK needs to be instantiated using your API username and API password, which you can get from your [Pesamoni business account](https://pesamoni.com/business/dash).

You can register a new Pesamoni business account [Here](https://pesamoni.com/businesses/sign_up) or Sign in [Here](https://pesamoni.com/businesses/sign_in)


```python
from __future__ import print_function
import time
import pesamoni_python
from pesamoni_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: apipassword
configuration = pesamoni_python.Configuration()
configuration.api_key['apipassword'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apipassword'] = 'Bearer'
# Configure API key authorization: apiusername
configuration = pesamoni_python.Configuration()
configuration.api_key['apiusername'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiusername'] = 'Bearer'

# create an instance of the API class
api_instance = pesamoni_python.DefaultApi(pesamoni_python.ApiClient(configuration))
```

### Accepting funds from mobile subscriber
```python
# you can either use method acreceive or acreceivekeac as explained below
# method acreceive
# This method enables you receive funds from a mobile subscriber in your registered native currency on the Pesamoni platform. If for instance your account is registered in currency UGX and you request money from a Kenyan number e.g 254712346789, a Pesamoni exchange rate will automatically be applied and money deposited into your Pesamoni wallet in your default currency
# method acreceivekeac
# You can have two native currencies on your Pesamoni account on request. If you would like to deposit funds from a mobile subscriber to your Kenyan Pesamoni wallet account then this is the method you use.
# example
method = 'method_example' # str | Enter a request method. To check for request methods <a href=''>click here</a>
amount = 'amount_example' # str | Enter the amount you would like to request for. <p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, acsendbank, pesab2c, sendairtime, cardaccept</b></p>
mobile = 'mobile_example' # str | Enter the mobile number you would like to execute the above method in format 256.... or 254...<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, senderid, sendsms, sendairtime</b></p> (optional)
reference = 'reference_example' # str | Enter your user generated transaction reference<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, transactionstatus, sendairtime, pesab2c, sendsms, cardaccept</b></p> (optional)
genericmsg = 'genericmsg_example' # str | Enter your user generated generic message for the requested transaction<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept</b></p> (optional)
token = 'token_example' # str | Enter your user generated token for the above mentioned method<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept</b></p> (optional)
try:
    api_response = api_instance.transactions_post(method, amount, mobile=mobile, holdername=holdername, cardnumber=cardnumber, cvv=cvv, exp=exp, currency=currency, account=account, reference=reference, genericmsg=genericmsg, token=token, bouquet=bouquet, payoption=payoption, meternumber=meternumber)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transactions_post: %s\n" % e)
```
### Sending funds to a mobile subscriber

```python
method = 'acsend'
# you can either use method acsend or acsendkeac as explained below
# acsend
# This method enables you send funds to a mobile subscriber in your registered native currency on the Pesamoni platform. If for instance your account is registered in currency UGX and you send money to a kenyan number e.g 254712346789, a Pesamoni exchange rate will automatically be applied and the equivalent exchange amount deducted from your Pesamoni wallet in your default currency
# acsendkeac
# You can have two native currencies on your Pesamoni account on request. If you would like to send funds from your Pesamoni wallet to a mobile subscriber from your Kenyan Pesamoni wallet account then this is the method you use.
amount = 'amount_example' # str | Enter the amount you would like to send funds to. <p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, acsendbank, pesab2c, sendairtime, cardaccept</b></p>
mobile = 'mobile_example' # str | Enter the mobile number you would like to execute the above method in format 256.... or 254...<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, senderid, sendsms, sendairtime</b></p> (optional)
reference = 'reference_example' # str | Enter your user generated transaction reference<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, transactionstatus, sendairtime, pesab2c, sendsms, cardaccept</b></p> (optional)
genericmsg = 'genericmsg_example' # str | Enter your user generated generic message for the requested transaction<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept</b></p> (optional)
token = 'token_example' # str | Enter your user generated token for the above mentioned method<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept</b></p> (optional)
try:
    api_response = api_instance.transactions_post(method, amount, mobile=mobile, holdername=holdername, cardnumber=cardnumber, cvv=cvv, exp=exp, currency=currency, account=account, reference=reference, genericmsg=genericmsg, token=token, bouquet=bouquet, payoption=payoption, meternumber=meternumber)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transactions_post: %s\n" % e)

```

### Accepting Card Payments e.g VISA/MASTERCARD

```python

method = 'cardaccept'

amount = 'amount_example', # String | Enter the amount you would like to request for. <p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, acsendbank, pesab2c, sendairtime, cardaccept</b></p>
holdername ='holdername_example', # String | Enter name of payer for Visa/MasterCard transactions<p style=\"color:red\">This method applies for request method <b>cardaccept</b></p>
cardnumber = 'cardnumber_example', # String | Enter the Visa/MasterCard cardnumber<p style=\"color:red\">This method applies for request method <b>cardaccept</b></p>
cvv = 'cvv_example', # String | Enter the Visa/MasterCard cvv<p style=\"color:red\">This method applies for request method <b>cardaccept</b></p>
exp = 'exp_example', # String | Enter the Visa/MasterCard expiry date in the format MM/YYYY e.g 07/2030<p style=\"color:red\">This method applies for request method <b>cardaccept</b></p>
currency = 'currency_example', # String | Enter the currency you intend to make the transaction for Visa/MasterCard based transactions<p style=\"color:red\">This method applies for request method <b>cardaccept</b></p>
genericmsg = 'genericmsg_example', # String | Enter your user generated generic message for the requested transaction<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept</b></p>
token = 'token_example', # String | Enter your user generated token for the above mentioned method<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept</b></p>

try:
	    api_response = api_instance.transactions_post(method, amount, mobile=mobile, holdername=holdername, cardnumber=cardnumber, cvv=cvv, exp=exp, currency=currency, account=account, reference=reference, genericmsg=genericmsg, token=token, bouquet=bouquet, payoption=payoption, meternumber=meternumber)
	    pprint(api_response)
except ApiException as e:
	    print("Exception when calling DefaultApi->transactions_post: %s\n" % e)


```

### Bank transfers

```python
# you can either use method acsendbank or acsendbankeac as explained below
# acsendbank
# This method enables you send funds to a users bank account. A Pesamoni exchange rate will automatically be applied and the equivalent exchange amount deposited to your bank account dependent on your default currency.
# acsendbankeac
# You can have two native currencies on your Pesamoni account on request. If you would like to send funds from your Pesamoni wallet to a mobile subscriber from your Kenyan Pesamoni wallet account then this is the method you use.

method = 'acsendbank'

amount = 'amount_example', # String | Enter the amount you would like to request for. <p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, acsendbank, pesab2c, sendairtime, cardaccept</b></p>
currency = 'currency_example', # String | Enter the currency you intend to make the transaction for Visa/MasterCard based transactions<p style=\"color:red\">This method applies for request method <b>cardaccept</b></p>
account = 'account_example', # String | Enter the Pesamoni account you would like to use for this transaction<p style=\"color:red\">This method applies for request method <b>paybills</b></p>
reference = 'reference_example', # String | Enter your user generated transaction reference<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, transactionstatus, sendairtime, pesab2c, sendsms, cardaccept</b></p>
genericmsg = 'genericmsg_example', # String | Enter your user generated generic message for the requested transaction<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept</b></p>
token = 'token_example', # String | Enter your user generated token for the above mentioned method<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept</b></p>

try:
	    api_response = api_instance.transactions_post(method, amount, mobile=mobile, holdername=holdername, cardnumber=cardnumber, cvv=cvv, exp=exp, currency=currency, account=account, reference=reference, genericmsg=genericmsg, token=token, bouquet=bouquet, payoption=payoption, meternumber=meternumber)
	    pprint(api_response)
except ApiException as e:
	    print("Exception when calling DefaultApi->transactions_post: %s\n" % e)
```

### Sending Airtime to a mobile subsriber

```python
method = 'sendairtime'

amount = 'amount_example', # String | Enter the amount you would like to request for. <p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, acsendbank, pesab2c, sendairtime, cardaccept</b></p>
mobile = 'mobile_example', # String | Enter the mobile number you would like to execute the above method in format 256.... or 254...<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, senderid, sendsms, sendairtime</b></p>
reference = 'reference_example', # String | Enter your user generated transaction reference<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, transactionstatus, sendairtime, pesab2c, sendsms, cardaccept</b></p>
genericmsg = 'genericmsg_example', # String | Enter your user generated generic message for the requested transaction<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept</b></p>
token = 'token_example', # String | Enter your user generated token for the above mentioned method<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept</b></p>

try:
    api_response = api_instance.transactions_post(method, amount, mobile=mobile, holdername=holdername, cardnumber=cardnumber, cvv=cvv, exp=exp, currency=currency, account=account, reference=reference, genericmsg=genericmsg, token=token, bouquet=bouquet, payoption=payoption, meternumber=meternumber)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transactions_post: %s\n" % e)
```
### Sending to a Pesamoni users wallet

```python
method = 'pesab2c'

amount = 'amount_example', # String | Enter the amount you would like to request for. <p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, acsendbank, pesab2c, sendairtime, cardaccept</b></p>
account = 'account_example', # String | Enter the Pesamoni account you would like to use for this transaction<p style=\"color:red\">This method applies for request method <b>paybills</b></p>
reference = 'reference_example', # String | Enter your user generated transaction reference<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, transactionstatus, sendairtime, pesab2c, sendsms, cardaccept</b></p>
genericmsg = 'genericmsg_example', # String | Enter your user generated generic message for the requested transaction<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept</b></p>
token = 'token_example', # String | Enter your user generated token for the above mentioned method<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept</b></p>

try:
    api_response = api_instance.transactions_post(method, amount, mobile=mobile, holdername=holdername, cardnumber=cardnumber, cvv=cvv, exp=exp, currency=currency, account=account, reference=reference, genericmsg=genericmsg, token=token, bouquet=bouquet, payoption=payoption, meternumber=meternumber)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transactions_post: %s\n" % e)

```

### Accepting funds from a Pesamoni user

```python
method = 'pesac2b'

amount = 'amount_example', # String | Enter the amount you would like to request for. <p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, acsendbank, pesab2c, sendairtime, cardaccept</b></p>
account = 'account_example', # String | Enter the Pesamoni account you would like to use for this transaction<p style=\"color:red\">This method applies for request method <b>paybills</b></p>
reference = 'reference_example', # String | Enter your user generated transaction reference<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, transactionstatus, sendairtime, pesab2c, sendsms, cardaccept</b></p>
genericmsg = 'genericmsg_example', # String | Enter your user generated generic message for the requested transaction<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept</b></p>
token = 'token_example', # String | Enter your user generated token for the above mentioned method<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept</b></p>

try:
    api_response = api_instance.transactions_post(method, amount, mobile=mobile, holdername=holdername, cardnumber=cardnumber, cvv=cvv, exp=exp, currency=currency, account=account, reference=reference, genericmsg=genericmsg, token=token, bouquet=bouquet, payoption=payoption, meternumber=meternumber)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transactions_post: %s\n" % e)

```

### Paying Utility Bills

```python
method = 'paybills'
amount = 'amount_example', # String | Enter the amount you would like to request for. <p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, acsendbank, pesab2c, sendairtime, cardaccept</b></p>
mobile = 'mobile_example', # String | Enter the mobile number you would like to execute the above method in format 256.... or 254...<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, senderid, sendsms, sendairtime</b></p>
currency = 'currency_example', # String | Enter the currency you intend to make the transaction for Visa/MasterCard based transactions<p style=\"color:red\">This method applies for request method <b>cardaccept</b></p>
reference = 'reference_example', # String | Enter your user generated transaction reference<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, transactionstatus, sendairtime, pesab2c, sendsms, cardaccept</b></p>
genericmsg = 'genericmsg_example', # String | Enter your user generated generic message for the requested transaction<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept</b></p>
token = 'token_example', # String | Enter your user generated token for the above mentioned method<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept</b></p>
bouquet = 'bouquet_example', # String | Enter the bouquet or package you would like to pay for<p style=\"color:red\">This method applies for request methods <b>paybills</b></p>
payoption = 'payoption_example', # String | Enter your prefered payment option<p style=\"color:red\">This method applies for request methods <b>paybills</b></p>
meternumber = 'meternumber_example' # String | Enter the meter number for the intended payment<p style=\"color:red\">This method applies for request methods <b>paybills</b></p>

try:
    api_response = api_instance.transactions_post(method, amount, mobile=mobile, holdername=holdername, cardnumber=cardnumber, cvv=cvv, exp=exp, currency=currency, account=account, reference=reference, genericmsg=genericmsg, token=token, bouquet=bouquet, payoption=payoption, meternumber=meternumber)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transactions_post: %s\n" % e)
```

### Checking transaction status

```python
method = 'transactionstatus'

reference = 'reference_example', # String | Enter your user generated transaction reference<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, transactionstatus, sendairtime, pesab2c, sendsms, cardaccept</b></p>

try:
    api_response = api_instance.transactions_post(method, amount, mobile=mobile, holdername=holdername, cardnumber=cardnumber, cvv=cvv, exp=exp, currency=currency, account=account, reference=reference, genericmsg=genericmsg, token=token, bouquet=bouquet, payoption=payoption, meternumber=meternumber)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transactions_post: %s\n" % e)
```

### Checking your Pesamoni Business Wallet Balance

```python
method = 'acbalance'

try:
    api_response = api_instance.transactions_post(method, amount, mobile=mobile, holdername=holdername, cardnumber=cardnumber, cvv=cvv, exp=exp, currency=currency, account=account, reference=reference, genericmsg=genericmsg, token=token, bouquet=bouquet, payoption=payoption, meternumber=meternumber)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transactions_post: %s\n" % e)

```
### Sending SMS to a mobile subscriber

```python
method = 'sendsms'

mobile = 'mobile_example', # String | Enter the mobile number you would like to execute the above method in format 256.... or 254...<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, senderid, sendsms, sendairtime</b></p>
reference = 'reference_example', # String | Enter your user generated transaction reference<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, transactionstatus, sendairtime, pesab2c, sendsms, cardaccept</b></p>
genericmsg = 'genericmsg_example', # String | Enter your user generated generic message for the requested transaction<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept</b></p>
token = 'token_example', # String | Enter your user generated token for the above mentioned method<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept</b></p>
message = 'message_example'
# String | Enter your message <p style=\"color:red\">This method applies for request methods <b>sendsms</b></p>

try:
    api_response = api_instance.transactions_post(method, amount, mobile=mobile, holdername=holdername, cardnumber=cardnumber, cvv=cvv, exp=exp, currency=currency, account=account, reference=reference, genericmsg=genericmsg, token=token, bouquet=bouquet, payoption=payoption, meternumber=meternumber)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transactions_post: %s\n" % e)
```

# Documentation for API Endpoints

All Endpoint URIs are relative to https://pesamoni.com/api/live/v1/transactions


## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/Pesamoni.

## License

The Library is available as open source under the terms of the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).



