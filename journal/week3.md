# Week 3 — Decentralized Authentication
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-3/week3.png)

## Required Homework

- Setup Cognito User Pool	
- Implement Custom Signin Page	
- Implement Custom Signup Page	
- Implement Custom Confirmation Page	
- Implement Custom Recovery Page	
- Verify JWT token server side	
- Decenteralized Authentication	
- Spending Considerations
- Watch about different approaches to verifying JWTs

***NB: DUE TO THE AMOUNT OF CODE CHANGES THAT WERE DONE TO IMPLEMENT A LOT OF THINGS IN OUR APP, I WILL NOT BE ABLE TO SHOW ALL THE CODE CHANGES. HOWEVER ALL CHANGES CAN BE VIEWED IN MY COMMITS FOR EACH WEEK.**


### Setup Cognito User Pool	
I was able to set up a cognito user pool via the AWS console. I went through all the steps and configured the user pool to fit my application's parameters. Cognito user pool sign-in options can't be changed after the user pool has been created.
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-3/Cognito%201.png)
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-3/Cognito%203.png)
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-3/Cognito%2014.png)



### Implement Custom Signup Page	

**Configure Amplify**
Inorder to interact with AWS Cognito I had to configure AWs Amplify. From the frontend-react-js directory run the following code `npm i aws-amplify –save`.

I could see `aws-amplify` installed as a dependency in your `package.json` file. Dependencies are libraries that are required to make the application work. Dev-dependencies are libraries that you only want installed when you are using them for development, they aren’t shipped with the code when we get to production.

I then navigated to the `App.js` file and installed amplify by running this code
`import { Amplify } from 'aws-amplify';`

Next I configured Amplify in my `app.js` file .

I proceeded to add env vars to my frontend in my docker file. To do this I followed the following steps:
- Proceeded to my AWS console and from my created user pool in Cognito, copy the User Pool ID.
- From your user pool page, navigate to the App Intergration tab.
- Scroll all the way down to app clients and analytics, from there copy the USER ID.


Next I to change some of our code so that it is Conditional. This basically means that the code will show certain things if a user is authenticated and logged in and will not show certain things if a user is logged out. Navigate to the HomeFeedPage.js file and add the following import: ```import { Auth } from 'aws-amplify'; ```

Update the `ProfilePage.js` file with this code:

```const signOut = async () => {
  try {
      await Auth.signOut({ global: true });
      window.location.href = "/"
  } catch (error) {
      console.log('error signing out: ', error);
  }
} 
```


Our application had been been set up to implement authentication using Cookies. Code above forces all sessions to close if you logged in from multiple sources.

At this point the app should be working and intergrated the changes we made we will run a docker compose up command .


### Implement Custom Signin Page
Inorder to implement the Signin page Ineed to play around and the code in some of the pages. I was able to get the Signin pages working properly.

Navigate top SigninPage.js. Replace:
``` import Cookies from ‘js-cookie’  ```

with

``` import { Auth } from 'aws-amplify';```
More changes to code were made.


Now try and sign in, If everything was configure correctly you should get error similar to the one shown below.

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-3/Cognito%2017d%20signin%20page%20working.png)


### Implement Custom Confirmation Page
	
From the  `ConfirmationPage.js` add this import statement:
`import { Auth } from 'aws-amplify';`


```
const resend_code = async (event) => {
  setErrors('')
  try {
    await Auth.resendSignUp(email);
    console.log('code resent successfully');
    setCodeSent(true)
  } catch (err) {
    // does not return a code
    // does cognito always return english
    // for this to be an okay match?
    console.log(err)
    if (err.message == 'Username cannot be empty'){
      setErrors("You need to provide an email in order to send Resend Activiation Code")   
    } else if (err.message == "Username/client id combination not found."){
      setErrors("Email is invalid or cannot be found.")   
    }
  }
}
```

Now replace `onsubmit` with code below;

```
const onsubmit = async (event) => {
    event.preventDefault();
    setErrors('')
    try {
      await Auth.confirmSignUp(email, code);
      window.location.href = "/"
    } catch (error) {
      setErrors(error.message)
    }
    return false
  }
```
Proceed to the Cruudur Home Page and Click `Join Now` and fill the signup form. You should be able to proceed to the `Confirm your email` page if the confirgurations where implemented correctly.

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-3/Cognito%2022%20Signup%20page%20went%20to%20next%20page.png)


### Implement Custom Recovery Page	
Inorder to implement our rcovery age we will need to make some changes to our currntly code. From the `RecoverPage.js` replace existing code with the one below:

```
import { Auth } from 'aws-amplify';

const onsubmit_send_code = async (event) => {
  event.preventDefault();
  setErrors('')
  Auth.forgotPassword(username)
  .then((data) => setFormState('confirm_code') )
  .catch((err) => setErrors(err.message) );
  return false
}

const onsubmit_confirm_code = async (event) => {
  event.preventDefault();
  setErrors('')
  if (password == passwordAgain){
    Auth.forgotPasswordSubmit(username, code, password)
    .then((data) => setFormState('success'))
    .catch((err) => setErrors(err.message) );
  } else {
    setErrors('Passwords do not match')
  }
  return false
}
```

This should enable you to recover your email and create a new password.


### Verify JWT token server side and cors update

Add cors to your `app.py`

```
cors = CORS(
  app, 
  resources={r"/api/*": {"origins": origins}},
  headers=['Content-Type', 'Authorization'], 
  expose_headers='Authorization',
  methods="OPTIONS,GET,HEAD,POST"
)
```

In your `app.py` add the following statement in `data_home()` route.
``` app.logger.debug("AUTH HEADER", request.headers.get("Authorization"))```
You can view your logs for your backend.You should be able to see a printout of your auth headers. You can delete once youconfirm they are working fine.


***JWT Verification***
From your`lib` folder create a new file `cognito_jwt_token.py` with the following code

```
import time
import requests
from jose import jwk, jwt
from jose.exceptions import JOSEError
from jose.utils import base64url_decode

class FlaskAWSCognitoError(Exception):
  pass

class TokenVerifyError(Exception):
  pass

def extract_access_token(request_headers):
    access_token = None
    auth_header = request_headers.get("Authorization")
    if auth_header and " " in auth_header:
        _, access_token = auth_header.split()
    return access_token

class CognitoJwtToken:
    def __init__(self, user_pool_id, user_pool_client_id, region, request_client=None):
        self.region = region
        if not self.region:
            raise FlaskAWSCognitoError("No AWS region provided")
        self.user_pool_id = user_pool_id
        self.user_pool_client_id = user_pool_client_id
        self.claims = None
        if not request_client:
            self.request_client = requests.get
        else:
            self.request_client = request_client
        self._load_jwk_keys()

    def _load_jwk_keys(self):
        keys_url = f"https://cognito-idp.{self.region}.amazonaws.com/{self.user_pool_id}/.well-known/jwks.json"
        try:
            response = self.request_client(keys_url)
            self.jwk_keys = response.json()["keys"]
        except requests.exceptions.RequestException as e:
            raise FlaskAWSCognitoError(str(e)) from e

    @staticmethod
    def _extract_headers(token):
        try:
            headers = jwt.get_unverified_headers(token)
            return headers
        except JOSEError as e:
            raise TokenVerifyError(str(e)) from e

    def _find_pkey(self, headers):
        kid = headers["kid"]
        # search for the kid in the downloaded public keys
        key_index = -1
        for i in range(len(self.jwk_keys)):
            if kid == self.jwk_keys[i]["kid"]:
                key_index = i
                break
        if key_index == -1:
            raise TokenVerifyError("Public key not found in jwks.json")
        return self.jwk_keys[key_index]

    @staticmethod
    def _verify_signature(token, pkey_data):
        try:
            # construct the public key
            public_key = jwk.construct(pkey_data)
        except JOSEError as e:
            raise TokenVerifyError(str(e)) from e
        # get the last two sections of the token,
        # message and signature (encoded in base64)
        message, encoded_signature = str(token).rsplit(".", 1)
        # decode the signature
        decoded_signature = base64url_decode(encoded_signature.encode("utf-8"))
        # verify the signature
        if not public_key.verify(message.encode("utf8"), decoded_signature):
            raise TokenVerifyError("Signature verification failed")

    @staticmethod
    def _extract_claims(token):
        try:
            claims = jwt.get_unverified_claims(token)
            return claims
        except JOSEError as e:
            raise TokenVerifyError(str(e)) from e

    @staticmethod
    def _check_expiration(claims, current_time):
        if not current_time:
            current_time = time.time()
        if current_time > claims["exp"]:
            raise TokenVerifyError("Token is expired")  # probably another exception

    def _check_audience(self, claims):
        # and the Audience  (use claims['client_id'] if verifying an access token)
        audience = claims["aud"] if "aud" in claims else claims["client_id"]
        if audience != self.user_pool_client_id:
            raise TokenVerifyError("Token was not issued for this audience")

    def verify(self, token, current_time=None):
        """ https://github.com/awslabs/aws-support-tools/blob/master/Cognito/decode-verify-jwt/decode-verify-jwt.py """
        if not token:
            raise TokenVerifyError("No token provided")

        headers = self._extract_headers(token)
        pkey_data = self._find_pkey(headers)
        self._verify_signature(token, pkey_data)

        claims = self._extract_claims(token)
        self._check_expiration(claims, current_time)
        self._check_audience(claims)

        self.claims = claims 
        return claims
```

After adding all the code as per the [video instructions](https://www.youtube.com/watch?v=d079jccoG-M&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=39) 

I ran into a error. My logs showed the error below;

![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-3/JWT%20logs%20error%20.png)

To mitigate this, add this dependency to your `requirements.txt` file: `social-auth-core` and rAn pip install


Restarted the workspace and got everything working
![](https://github.com/CloudRiRi15/aws-bootcamp-cruddur-2023/blob/main/journal/assets/week-3/JWT%20logs%20errors%20fixed%20.png)









