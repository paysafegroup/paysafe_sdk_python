from PythonPaysafeSDK.ThreeDSecureV2.Card import Card
from PythonPaysafeSDK.ThreeDSecureV2.ElectronicDelivery import ElectronicDelivery
from PythonPaysafeSDK.ThreeDSecureV2.OrderItemDetails import OrderItemDetails
from PythonPaysafeSDK.ThreeDSecureV2.BillingCycle import BillingCycle
from PythonPaysafeSDK.ThreeDSecureV2.PurchasedGiftCardDetails import PurchasedGiftCardDetails
from PythonPaysafeSDK.ThreeDSecureV2.BrowserDetails import BrowserDetails
from PythonPaysafeSDK.ThreeDSecureV2.BillingDetails import BillingDetails
from PythonPaysafeSDK.ThreeDSecureV2.ShippingDetails import ShippingDetails
from PythonPaysafeSDK.ThreeDSecureV2.UserAccountDetails import UserAccountDetails
from PythonPaysafeSDK.ThreeDSecureV2.Profile import Profile
from PythonPaysafeSDK.ThreeDSecureV2.PaymentAccountDetails import PaymentAccountDetails
from PythonPaysafeSDK.ThreeDSecureV2.PriorThreeDSAuthentication import PriorThreeDSAuthentication
from PythonPaysafeSDK.ThreeDSecureV2.ShippingDetailsUsage import ShippingDetailsUsage
from PythonPaysafeSDK.ThreeDSecureV2.TravelDetails import TravelDetails
from PythonPaysafeSDK.ThreeDSecureV2.UserLogin import UserLogin
from PythonPaysafeSDK.common.CardExpiry import CardExpiry
from PythonPaysafeSDK.PaysafeApiClient import PaysafeApiClient
from PythonPaysafeSDK.ThreeDSecureV2.Authentications import Authentications
from utils.Utils import Utils

from Config import Config
from RandomTokenGenerator import RandomTokenGenerator


optimal_obj = PaysafeApiClient(Config.api_key, Config.api_password, Config.environment, Config.account_number)
# Submit Authentication with card details
authentications_obj = Authentications(None)
card_obj = Card(None)
card_expiry_obj = CardExpiry(None)
billingDetails_obj=BillingDetails(None)
shippingDetails_obj=ShippingDetails(None)
profile_obj=Profile(None)
billingCycle_obj=BillingCycle(None)
orderItemDetails_obj=OrderItemDetails(None)
purchasedGiftCardDetails_obj=PurchasedGiftCardDetails(None)
userAccountDetails_obj=UserAccountDetails(None)
paymentAccountDetails_obj=PaymentAccountDetails(None)
priorThreeDSAuthentication_obj=PriorThreeDSAuthentication(None)
shippingDetailsUsage_obj=ShippingDetailsUsage(None)
travelDetails_obj=TravelDetails(None)
userLogin_obj=UserLogin(None)
browserDetails_obj=BrowserDetails(None)

authentications_obj.amount(99999999999)
authentications_obj.currency("EUR")
authentications_obj.mcc("0742")
authentications_obj.merchantName("Merchant Name Inc")
authentications_obj.merchantRefNum(RandomTokenGenerator().generateToken())    
authentications_obj.merchantUrl("https://mysite.com")

card_obj.cardNum("4111111111111111")
card_obj.holderName("John Smith")
        
card_expiry_obj.month(10)
card_expiry_obj.year(2020)
        
card_obj.cardExpiry(card_expiry_obj)
authentications_obj.card(card_obj)
        
billingDetails_obj.city("New York")
billingDetails_obj.country("US")
billingDetails_obj.state("AL")
billingDetails_obj.street("My street1")
billingDetails_obj.street2("My street2")
billingDetails_obj.zip("CHY987")
authentications_obj.billingDetails(billingDetails_obj)
        
shippingDetails_obj.city("New York")
shippingDetails_obj.country("US")
shippingDetails_obj.state("AL")
shippingDetails_obj.street("My street 1")
shippingDetails_obj.street2("My street 2")
shippingDetails_obj.zip("CHY987")
shippingDetails_obj.shipMethod("S")
authentications_obj.shippingDetails(shippingDetails_obj)

profile_obj.cellphone("+154657854697")
profile_obj.email("example@example.com")
profile_obj.phone("+154657854697")
authentications_obj.profile(profile_obj)

authentications_obj.deviceFingerprintingId("bf3d194c-c413-4205-bb25-4a5e14301c68")
authentications_obj.deviceChannel("BROWSER")
authentications_obj.requestorChallengePreference("NO_PREFERENCE")
authentications_obj.messageCategory("PAYMENT")
authentications_obj.transactionIntent("GOODS_OR_SERVICE_PURCHASE")
authentications_obj.authenticationPurpose("PAYMENT_TRANSACTION")
authentications_obj.maxAuthorizationsForInstalmentPayment(2)
authentications_obj.initialPurchaseTime("2019-01-21T14:47:31.540Z")
        
billingCycle_obj.endDate("2014-01-26")
billingCycle_obj.frequency(1)
authentications_obj.billingCycle(billingCycle_obj)
        
orderItemDetails_obj.preOrderItemAvailabilityDate("2014-01-26")
orderItemDetails_obj.preOrderPurchaseIndicator("MERCHANDISE_AVAILABLE")
orderItemDetails_obj.reorderItemsIndicator("FIRST_TIME_ORDER")
orderItemDetails_obj.shippingIndicator("SHIP_TO_BILLING_ADDRESS")
authentications_obj.orderItemDetails(orderItemDetails_obj)
        
purchasedGiftCardDetails_obj.amount(99999999999)
purchasedGiftCardDetails_obj.count(2)
purchasedGiftCardDetails_obj.currency("USD")
authentications_obj.purchasedGiftCardDetails(purchasedGiftCardDetails_obj)
        
userAccountDetails_obj.addCardAttemptsForLastDay(1)
userAccountDetails_obj.changedDate("2014-01-26")
userAccountDetails_obj.changedRange("DURING_TRANSACTION")
userAccountDetails_obj.createdDate("2014-01-26")
userAccountDetails_obj.createdRange("NO_ACCOUNT")
userAccountDetails_obj.passwordChangedDate("2014-01-26")
userAccountDetails_obj.passwordChangedRange("NO_CHANGE")
					
paymentAccountDetails_obj.createdRange("NO_ACCOUNT")
paymentAccountDetails_obj.createdDate("2014-01-26")
userAccountDetails_obj.paymentAccountDetails(paymentAccountDetails_obj)
        
priorThreeDSAuthentication_obj.data("Some up to 2048 bytes undefined data")
priorThreeDSAuthentication_obj.method("FRICTIONLESS_AUTHENTICATION")
priorThreeDSAuthentication_obj.id("123e4567-e89b-12d3-a456-426655440000")
priorThreeDSAuthentication_obj.time("2014-01-26T10:32:28Z")
userAccountDetails_obj.priorThreeDSAuthentication(priorThreeDSAuthentication_obj)
        
shippingDetailsUsage_obj.cardHolderNameMatch(True)
shippingDetailsUsage_obj.initialUsageDate("2014-01-26")
shippingDetailsUsage_obj.initialUsageRange("CURRENT_TRANSACTION")
userAccountDetails_obj.shippingDetailsUsage(shippingDetailsUsage_obj)

userAccountDetails_obj.suspiciousAccountActivity(True)
userAccountDetails_obj.totalPurchasesSixMonthCount(1)
userAccountDetails_obj.transactionCountForPreviousDay(1)
userAccountDetails_obj.transactionCountForPreviousYear(3)

travelDetails_obj.isAirTravel(True)
travelDetails_obj.airlineCarrier("Wizz air")
travelDetails_obj.departureDate("2014-01-26")
travelDetails_obj.destination("SOF")
travelDetails_obj.origin("BCN")
travelDetails_obj.passengerFirstName("John")
travelDetails_obj.passengerLastName("Smith")
userAccountDetails_obj.travelDetails(travelDetails_obj)
					
userLogin_obj.authenticationMethod("NO_LOGIN")
userLogin_obj.data("Some up to 2048 bytes undefined data")
userLogin_obj.time("2014-01-26T10:32:28Z")
userAccountDetails_obj.userLogin(userLogin_obj)
authentications_obj.userAccountDetails(userAccountDetails_obj)
					
browserDetails_obj.acceptHeader("*/*")
browserDetails_obj.colorDepthBits("24")
browserDetails_obj.customerIp("207.48.141.20")
browserDetails_obj.javascriptEnabled(True)
browserDetails_obj.javaEnabled(True)
browserDetails_obj.language("en-US")
browserDetails_obj.screenHeight(768)
browserDetails_obj.screenWidth(1024)
browserDetails_obj.timezoneOffset(240)
browserDetails_obj.userAgent("Mozilla/4.0 (compatible; Win32; WinHttp.WinHttpRequest.5)")
authentications_obj.browserDetails(browserDetails_obj)	

        
response_object=optimal_obj.three_d_secure_v2_service_handler().submit_authentications_withCardDetails(authentications_obj)
response_object2=optimal_obj.three_d_secure_v2_service_handler().lookup_authentications(response_object)

print ("\nResponse Values ==========> ")
Utils.print_response(response_object2)
