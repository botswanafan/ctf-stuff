# login
- Open up the website and notice that when one submits a given input, no network requests are made -> the user+pass are stored locally.
- The index.js contains the base64 user + pass, but only the pass is needed for the flag, as the flag is simply the pass stored