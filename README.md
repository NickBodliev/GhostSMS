# GhostSMS
App that interrogates [TextBelt SMS API](https://textbelt.com/) to send ghost SMS messages to phone number you specify. The phone number must contain the country code. TextBelt API permits to send only 1 message every 24 hours in the free version.

You can buy also more SMS texts if you want. The version in this repository is the free one

![TextBelt SMS API Costs](https://user-images.githubusercontent.com/62834545/116057618-44303700-a67f-11eb-8574-359d7a63e60a.png)


To use the app, you have open the path of the directory with the CLI and write 'python GhostSMS'. It will ask you for the destination and the message you want to send.
After that you will get the object of response from TextBelt API, if the 'success' alue is 'True', it means that the message was sent with success.
In the contrary case, the 'success' value will be 'False'.

E.G.

![response](https://user-images.githubusercontent.com/62834545/116058694-61b1d080-a680-11eb-80b5-d98c8ba61af7.png)

 In the future updates the will be able to handle the response and show a custom message.

