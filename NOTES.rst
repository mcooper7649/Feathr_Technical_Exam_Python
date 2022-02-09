Implementation
======

Please describe your plan for how to implement secure authentication for whoami.

How are you going to receive and store sensitive user information? 
  - I am going to use mongoDB cloud services to host their user data. I will encrypt and verify using bcrypt, a hash that is notably strong against brute force style hacks. 
  - I will also delete the password from the user session prior to use so it isn't exposed to the user/client. 

How are you going to maintain their authenticated session? Etc.
  - I will utilize the session method of Flask4 to store the user data and logged in status.
  - When we use sessions the data is stored in the browser as a cookie. The cookie used to store session data is known session cookie. However, unlike an ordinary cookie, 
  Flask Cryptographically signs the session cookie. It means that anyone can view the contents of the cookie, but can't modify the cookie unless he has the secret key used to sign the cookie. 
  - If Flask fails to unsign the cookie then its content is discarded and a new session cookie is sent to the browser.


Limitations, Future Work
========================

Here, describe what shortcomings or flaws exist in the version you are submitting.
Nothing is ever perfect and we expect some things to be left unfinished - it's
important to be able to recognize those issues so we can come back and fix them
later.

- Complete Form Validation UI, I have response codes setup but ran out of time before I was able to
figure out how to inject the response codes into the headers of the correct template.
- Complete Testing Suite
    - Need to deepdive into PYTEST/FLASK documentation
- Additional Features
    - Avatar or Profile Photo
    - login tracker (how many visits, most recent session info, like location with ability to clear.)
    - favorite quote and ability to change/delete.
    - ability to search for and add other whoami users as a friends List
        - Display friends list on me page
    - Create feed page display friends and your shared media
      - comments below each video with username and like/flag feature



