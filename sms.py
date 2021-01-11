from kavenegar import *
import pandas as pd
cells= pd.read_excel ('sms.xlsx')
sms_number=(cells['number'])
payamak=(cells['message'])
customer=(cells['name'])
for i in (payamak.index):
    api = KavenegarAPI('7666717061636236495746553246436532654E6B364B46647238374B7679466F4175534D2F7476663737733D')
    params = {    'sender': '1000596446',    'receptor': sms_number[i],    'message': " سلام "+customer[i]+" خوبی "}
#    print(sms_number[i], payamak[i])
    response = api.sms_send(params)

