# 🎼Voice-to-Note🤖

### How it works

This is a Whatsapp bot that, given audio, will use Google's Cloud Speech-to-Text to extract the text and send it back to the user. 
When a message comes in, the file containing the audio is fetched through twilio from an s3 bucket and sent to the Google Speech Recognition API. The result is returned to the flask server and the flask server then sends it back to the user.

## How to use it

Connect to the sandbox bot and start sending it audio or voice notes, its as easy as that!

## Demo

Feel free to connect to my sandbox by sending a WhatsApp message from your device to +1 415 523 8886 with code join terrible-shop.

[Whatsapp Bot Screenshot](https://dev-to-uploads.s3.amazonaws.com/i/1oz5llwkgg8sa3nwruys.png)


## Set up

### Requirements

- [Python 3](https://www.python.org/downloads/)
- A Google Cloud account - [sign up](https://cloud.google.com)
- A Twilio account - [sign up](https://www.twilio.com/try-twilio)

### Local development

After the above requirements have been met:

1. Clone this repository and `cd` into it

```bash
git clone git@github.com:twilio-labs/sample-template-nodejs.git
cd sample-template-nodejs
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Set your environment variables

You need to have your Google Cloud API Key in a file stored locally. Replace \[PATH\] with the path of the JSON file that contains your service account key. 

```bash
export GOOGLE_APPLICATION_CREDENTIALS="[PATH TO API]"
```

See [Twilio Account Settings](#twilio-account-settings) to locate the necessary environment variables.

4. Run the application

```bash
python lambda_function.py
```

5. Expose locally running server

Use a tool such as [ngrok]('https://ngrok.com/') to expose the server running locally to the web.

6. Pass the public-facing url to the Twilio whatsapp webhooks

You'll find this on the [Sandbox Configuration]() page.
If your public url is https://notarealurl.com then your settings will be as follows:

|WHEN A MESSAGE COMES IN |  https://notarealurl.com/bot-receiver | HTTP Post|
--- | --- | ---
|STATUS CALLBACK URL |  https://notarealurl.com/bot-status | HTTP Post|


7. Connect to the sandbox

You should now be able to send it voice notes or audio files!


### Tests

No tests are present as yet.

### Cloud deployment

Additionally to trying out this application locally, you can deploy it to a variety of host services. 

This was the route I followed, see this [guide](https://dev.to/apcelent/deploying-flask-on-aws-lambda-4k42)

If you follow the guide, using this repository as the root folder, it should allow you to deploy to the cloud.

Once the flask server is running, select the lambda running the server and set the environment variables as shown in the steps above in the [AWS console](https://console.aws.amazon.com/lambda). Proceed to follow the local development steps from step 6 onward.

Please be aware that some of these might charge you for the usage or might make the source code for this application visible to the public. When in doubt research the respective hosting service first.

## License

[MIT](http://www.opensource.org/licenses/mit-license.html)

## Disclaimer

No warranty expressed or implied. Software is as is.
