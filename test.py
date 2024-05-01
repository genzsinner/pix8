from veeva_connector.veeva_sdk import VeevaSDK

veeva_obj = VeevaSDK("Un", "Known")

print(veeva_obj.fetch_user_data())