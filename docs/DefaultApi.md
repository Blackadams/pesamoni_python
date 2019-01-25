# pesamoni_python.DefaultApi

All URIs are relative to *https://pesamoni.com/api/live/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transactions_post**](DefaultApi.md#transactions_post) | **POST** /transactions | 


# **transactions_post**
> InlineResponse200 transactions_post(method, amount, mobile=mobile, holdername=holdername, cardnumber=cardnumber, cvv=cvv, exp=exp, currency=currency, account=account, reference=reference, genericmsg=genericmsg, token=token, bouquet=bouquet, payoption=payoption, meternumber=meternumber)



Below are parameters and their respective expected responses. In order to try out the service, simply click Try it out.

### Example
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
method = 'method_example' # str | Enter a request method. To check for request methods <a href=''>click here</a>
amount = 'amount_example' # str | Enter the amount you would like to request for. <p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, acsendbank, pesab2c, sendairtime, cardaccept</b></p>
mobile = 'mobile_example' # str | Enter the mobile number you would like to execute the above method in format 256.... or 254...<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, senderid, sendsms, sendairtime</b></p> (optional)
holdername = 'holdername_example' # str | Enter name of payer for Visa/MasterCard transactions<p style=\"color:red\">This method applies for request method <b>cardaccept</b></p> (optional)
cardnumber = 'cardnumber_example' # str | Enter the Visa/MasterCard cardnumber<p style=\"color:red\">This method applies for request method <b>cardaccept</b></p> (optional)
cvv = 'cvv_example' # str | Enter the Visa/MasterCard cvv<p style=\"color:red\">This method applies for request method <b>cardaccept</b></p> (optional)
exp = 'exp_example' # str | Enter the Visa/MasterCard expiry date in the format MM/YYYY e.g 07/2030<p style=\"color:red\">This method applies for request method <b>cardaccept</b></p> (optional)
currency = 'currency_example' # str | Enter the currency you intend to make the transaction for Visa/MasterCard based transactions<p style=\"color:red\">This method applies for request method <b>cardaccept</b></p> (optional)
account = 'account_example' # str | Enter the Pesamoni account you would like to use for this transaction<p style=\"color:red\">This method applies for request method <b>paybills</b></p> (optional)
reference = 'reference_example' # str | Enter your user generated transaction reference<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, transactionstatus, sendairtime, pesab2c, sendsms, cardaccept</b></p> (optional)
genericmsg = 'genericmsg_example' # str | Enter your user generated generic message for the requested transaction<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept</b></p> (optional)
token = 'token_example' # str | Enter your user generated token for the above mentioned method<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept</b></p> (optional)
bouquet = 'bouquet_example' # str | Enter the bouquet or package you would like to pay for<p style=\"color:red\">This method applies for request methods <b>paybills</b></p> (optional)
payoption = 'payoption_example' # str | Enter your prefered payment option<p style=\"color:red\">This method applies for request methods <b>paybills</b></p> (optional)
meternumber = 'meternumber_example' # str | Enter the meter number for the intended payment<p style=\"color:red\">This method applies for request methods <b>paybills</b></p> (optional)

try:
    api_response = api_instance.transactions_post(method, amount, mobile=mobile, holdername=holdername, cardnumber=cardnumber, cvv=cvv, exp=exp, currency=currency, account=account, reference=reference, genericmsg=genericmsg, token=token, bouquet=bouquet, payoption=payoption, meternumber=meternumber)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transactions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method** | **str**| Enter a request method. To check for request methods &lt;a href&#x3D;&#39;&#39;&gt;click here&lt;/a&gt; | 
 **amount** | **str**| Enter the amount you would like to request for. &lt;p style&#x3D;\&quot;color:red\&quot;&gt;This method applies for request methods &lt;b&gt;acreceive, acreceivekeac, acsend, acsendkeac, acsendbank, pesab2c, sendairtime, cardaccept&lt;/b&gt;&lt;/p&gt; | 
 **mobile** | **str**| Enter the mobile number you would like to execute the above method in format 256.... or 254...&lt;p style&#x3D;\&quot;color:red\&quot;&gt;This method applies for request methods &lt;b&gt;acreceive, acreceivekeac, acsend, acsendkeac, senderid, sendsms, sendairtime&lt;/b&gt;&lt;/p&gt; | [optional] 
 **holdername** | **str**| Enter name of payer for Visa/MasterCard transactions&lt;p style&#x3D;\&quot;color:red\&quot;&gt;This method applies for request method &lt;b&gt;cardaccept&lt;/b&gt;&lt;/p&gt; | [optional] 
 **cardnumber** | **str**| Enter the Visa/MasterCard cardnumber&lt;p style&#x3D;\&quot;color:red\&quot;&gt;This method applies for request method &lt;b&gt;cardaccept&lt;/b&gt;&lt;/p&gt; | [optional] 
 **cvv** | **str**| Enter the Visa/MasterCard cvv&lt;p style&#x3D;\&quot;color:red\&quot;&gt;This method applies for request method &lt;b&gt;cardaccept&lt;/b&gt;&lt;/p&gt; | [optional] 
 **exp** | **str**| Enter the Visa/MasterCard expiry date in the format MM/YYYY e.g 07/2030&lt;p style&#x3D;\&quot;color:red\&quot;&gt;This method applies for request method &lt;b&gt;cardaccept&lt;/b&gt;&lt;/p&gt; | [optional] 
 **currency** | **str**| Enter the currency you intend to make the transaction for Visa/MasterCard based transactions&lt;p style&#x3D;\&quot;color:red\&quot;&gt;This method applies for request method &lt;b&gt;cardaccept&lt;/b&gt;&lt;/p&gt; | [optional] 
 **account** | **str**| Enter the Pesamoni account you would like to use for this transaction&lt;p style&#x3D;\&quot;color:red\&quot;&gt;This method applies for request method &lt;b&gt;paybills&lt;/b&gt;&lt;/p&gt; | [optional] 
 **reference** | **str**| Enter your user generated transaction reference&lt;p style&#x3D;\&quot;color:red\&quot;&gt;This method applies for request methods &lt;b&gt;acreceive, acreceivekeac, acsend, acsendkeac, sendsms, transactionstatus, sendairtime, pesab2c, sendsms, cardaccept&lt;/b&gt;&lt;/p&gt; | [optional] 
 **genericmsg** | **str**| Enter your user generated generic message for the requested transaction&lt;p style&#x3D;\&quot;color:red\&quot;&gt;This method applies for request methods &lt;b&gt;acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept&lt;/b&gt;&lt;/p&gt; | [optional] 
 **token** | **str**| Enter your user generated token for the above mentioned method&lt;p style&#x3D;\&quot;color:red\&quot;&gt;This method applies for request methods &lt;b&gt;acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept&lt;/b&gt;&lt;/p&gt; | [optional] 
 **bouquet** | **str**| Enter the bouquet or package you would like to pay for&lt;p style&#x3D;\&quot;color:red\&quot;&gt;This method applies for request methods &lt;b&gt;paybills&lt;/b&gt;&lt;/p&gt; | [optional] 
 **payoption** | **str**| Enter your prefered payment option&lt;p style&#x3D;\&quot;color:red\&quot;&gt;This method applies for request methods &lt;b&gt;paybills&lt;/b&gt;&lt;/p&gt; | [optional] 
 **meternumber** | **str**| Enter the meter number for the intended payment&lt;p style&#x3D;\&quot;color:red\&quot;&gt;This method applies for request methods &lt;b&gt;paybills&lt;/b&gt;&lt;/p&gt; | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[apipassword](../README.md#apipassword), [apiusername](../README.md#apiusername)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

