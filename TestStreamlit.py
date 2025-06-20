import streamlit as st
import urllib.request
import json

st.title("Kokonut Chat Bot")

question = st.text_input("Enter your question", "")
st.write(f"Your question is : {question}")


# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data = {"question": question}

body = str.encode(json.dumps(data))

url = 'https://kokonutbot19062025.swedencentral.inference.ml.azure.com/score'
# Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
api_key = '2xynqh6qAV7bNy9gbeJvUu7HPGR2NamSynV9cEvpDnXTphbEgJcWJQQJ99BFAAAAAAAAAAAAINFRAZML2Ksm'
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {'Content-Type':'application/json', 'Accept': 'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    text = result.decode('utf-8')
    parsed = json.loads(text)
    finalResult = parsed['joke']
    #resultJson = response.json()
    #result1 = resultJson["joke"]

    st.write(f"result is : {finalResult}")
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    st.write(error.info())
    st.write(error.read().decode("utf8", 'ignore'))
