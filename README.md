# DNAC to Teams Webhook Notifications
Cisco DNA Center has a compatibility issue sending webhook notifications to Microsoft Teams,  attempting to do a test will cause the test to error with a generic "Failure" message which doesn't really help in the investigation.  After further debugging/packet capturing you'll see that MS Teams replies with an error 400 stating 'Summary or Text is required'

Microsoft Teams Webhooks use a particular JSON structure before it'll accept a webhook which can be found here: https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/connectors-using?tabs=cURL one that Cisco DNA Center doesn't know about and at time of writing doesn't have any plans to intergrate it into the platform.

This is a simple script that utilises python flask to receive a Cisco DNA Centre webhook, convert it into something Microsoft Teams will accept for it to appear in your webhook alerts channel.  Basically a middleware server/webhook proxy

This script will only send the notification as plain text to Teams, if I get any spare time I'll try looking into implementing formatting so it looks pretty with colour and fonts, etc, etc. 

Hope this helps fellow engineers from pulling their hair out trying to get better visiblity from their DNA Center.  I'm not a programmer at all, I stumble my way through python so if there's something that could improved reach out :)
