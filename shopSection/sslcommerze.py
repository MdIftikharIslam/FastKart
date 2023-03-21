# from sslcommerz_lib import SSLCOMMERZ
# from sslcommerz_lib import sslcommerz

# def sslcommerz_payment_gateway(request, name, amount):
#
#     # sslcommez = SSLCOMMERZ(settings)
#     post_body = {}
#     post_body['store_id'] = 'niyam6412dc52e1e89'
#     post_body['store_id'] = 'niyam6412dc52e1e89@ssl'
#     post_body["total_amount"] = amount
#     post_body["currency"] = "BDT"
#     # post_body["tran_id"] = unique_trangection_id_generator()
#     post_body["success_url"] = "http://donatehub.herokuapp.com/payment/success/"
#     post_body["fail_url"] = "http://donatehub.herokuapp.com/payment/faild/"
#     post_body["cancel_url"] = "http://donatehub.herokuapp.com/"
#     post_body["emi_option"] = 0
#     post_body["cus_name"] = name
#     post_body["cus_email"] = 'request.data["email"]'
#     post_body["cus_phone"] = 'request.data["phone"]'
#     post_body["cus_add1"] = 'request.data["address"]'
#     post_body["cus_city"] = 'request.data["address"]'
#     post_body["cus_country"] = "Bangladesh"
#     post_body["shipping_method"] = "NO"
#     post_body["multi_card_name"] = ""
#     post_body["num_of_item"] = 1
#     post_body["product_name"] = "Test"
#     post_body["product_category"] = "Test Category"
#     post_body["product_profile"] = "general"
#
#     # OPTIONAL PARAMETERS
#     post_body["value_a"] = name
#
#     response = sslcommez.createSession(post_body)
#     return (
#             "https://sandbox.sslcommerz.com/gwprocess/v4/gw.php?Q=pay&SESSIONKEY="
#             + response["sessionkey"]
#     )
#

