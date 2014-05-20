import os
import suds_marketo
import urllib3
from flask import Flask, request, json


#from flask.ext import restful
#from flask.ext.jsonpify import jsonify

app = Flask(__name__)
#api = restful.Api(app)
app.debug = True

#class merge(restful.Resource):
@app.route('/<ID>', methods=['POST'])
def merge(self):
    #Establish Connection, create the client handler
    #This is the msc.com instance connection
    #You see I own this town, you best not come around if you
    #If you wanna mess around like that, that's just how it is.
    jsonRequest = request.get_json(force = True)
    ID = jsonRequest['ID']

    client = suds_marketo.Client(soap_endpoint='https://970-WBY-466.mktoapi.com/soap/mktows/2_3',
                                 user_id='opentable1_62824687530E8A604131D1',
                                 encryption_key='5335137655137532553300EE88AA661244113492BE69')

    NewContactFromSFDC = str(ID)
    
    #get the leads from Marketo
    lead = client.get_lead_IDNUM(NewContactFromSFDC)
    for i in range(0,len(lead.leadRecordList.leadRecord[0].leadAttributeList[0])):
        if 'mKTOLeadID' == lead.leadRecordList.leadRecord[0].leadAttributeList[0][i].attrName:
            originalmarketoid = lead.leadRecordList.leadRecord[0].leadAttributeList[0][i].attrValue
    client.merge_leads(NewContactFromSFDC,originalmarketoid)

    return json.jsonify(Message = "",ResultCode = 0)

#api.add_resource(merge, '/<int:ID>')

if __name__ == '__main__':
    #app.run(debug=True)
    client = suds_marketo.Client(soap_endpoint='https://970-WBY-466.mktoapi.com/soap/mktows/2_3',
                                     user_id='opentable1_62824687530E8A604131D1',
                                     encryption_key='5335137655137532553300EE88AA661244113492BE69')
    lead = client.get_lead_IDNUM('543145')
    for i in range(0,len(lead.leadRecordList.leadRecord[0].leadAttributeList[0])):
        if 'mKTOLeadID' == lead.leadRecordList.leadRecord[0].leadAttributeList[0][i].attrName:
            originalmarketoid = lead.leadRecordList.leadRecord[0].leadAttributeList[0][i].attrValue
    client.merge_leads('543145',originalmarketoid)
    '''
    try:
        originalmarketoid = lead.originalmarketoid
        #make sure the original lead exists
        leadtomerge = client.get_lead(originalmarketoid)
        client.merge_leads(ID, orignalmarketoid)
    except:
        return
    '''
