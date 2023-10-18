# JWT_

### main.py

- mainly trying to implement the jwt as on the official site jwt.io, so that can try to play with forged tokens

## Trying the none alg attack

- referenced article : https://auth0.com/blog/critical-vulnerabilities-in-json-web-token-libraries/
- doesn't work now

## Algo Confusion Attack

- it doesn't seem plausible that I could try this if server already uses HMAC
- so, as i understand, if i can get the RSA public key, then I could forge a token (alg=HS256) and get server to accept that
