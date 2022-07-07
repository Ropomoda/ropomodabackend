import requests
sms_panel_address = "https://restfulsms.com/api/" 
sms_panel_user_api_key = '98047a5e6869a834c01a7a5e'
sms_panel_user_secret_key = 'C!@6#te6)*it%B&'

def verification_sms(*args, **kwargs):
    phone_number = str(args[0])
    activation_code = str(args[1])
    send_template_sms([
            { "Parameter":"code" , "ParameterValue":activation_code }
        ], 
        phone_number,
        '67586')
    return True
def send_template_sms(parameters , to , template):
    """
        parameters is a list of { Parameter , ParameterValue } 
    """
    c = requests.post(f"{sms_panel_address}UltraFastSend/UserApiKey" , json={
    "ParameterArray": parameters,
    "Mobile":to,
    "TemplateId": template,
    "UserApiKey":sms_panel_user_api_key,
    "SecretKey":sms_panel_user_secret_key
},headers={
        'Content-Type':'application/json'
    })
    return True