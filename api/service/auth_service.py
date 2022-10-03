"module"
import datetime
import uuid

import requests
from api.config import JWTKEY
from app import globalvars
from app.config import JWTKEY_CURRENT, SPA_TOKEN_HOURS
from app.err import err_obj
from app.utils.helpers import get_token_from_headers
from jose import jwt


def get_token_info(headers):
    "function"
    try:
        token = get_token_from_headers(headers)
        data, status = get_token_details(token)
        if status != 200:
            return data, status
        return {"message": "your current token details", "data": data}, 200

    except Exception as error:
        return err_obj("get_token_info", __name__, error), 500


def get_token_details(token):
    "function"
    try:
        unv_header = jwt.get_unverified_header(token)
        unv_claims = jwt.get_unverified_claims(token)
        issued = datetime.datetime.utcfromtimestamp(unv_claims["iat"])
        expires = datetime.datetime.utcfromtimestamp(unv_claims["exp"])
        return {
            "token": token,
            "issued": str(issued) + " UTC",
            "expires": str(expires) + " UTC",
            "decoded": {"header": unv_header, "claims": unv_claims},
        }, 200

    except Exception as error:
        return err_obj("get_token_details", __name__, error), 500


def get_token(headers):
    """
    Get SPA token (short duration token).
    Important - the Authorization token passed in the headers is an MS Graph token.
    """
    try:
        token = get_token_from_headers(headers)
        res = requests.get(
            "https://graph.microsoft.com/v1.0/me",
            headers={"Authorization": f"Bearer {token}"},
        )

        if res.status_code != 200:
            return {"error": res.text}, res.status_code
        me_data = res.json()
        upn = me_data["userPrincipalName"]
        name = me_data["displayName"]

        # If the token successfully got graph data, it can be trusted.
        unv_claims = jwt.get_unverified_claims(token)
        email = unv_claims["email"]

        iat = datetime.datetime.utcnow()
        exp = datetime.datetime.utcnow() + datetime.timedelta(hours=int(SPA_TOKEN_HOURS))
        expires_utc = int(exp.timestamp())
        auth_token = encode_auth_token(iat, exp, upn, name, email)

        return {
            "username": upn,
            "name": name,
            "email": email,
            "api_token": auth_token,
            "expires_utc": expires_utc,
        }, 200

    except Exception as error:
        return err_obj("get_token", __name__, error), 500


def validate_token(headers):
    "function"
    try:
        token = get_token_from_headers(headers)
        unv_header = jwt.get_unverified_header(token)
        kid = unv_header.get("kid")
        if kid is None:
            kid = "BLANK"
        key = JWTKEY.get(kid)
        if key is None:
            return {"error": "auth token has obsolete key id: " + kid}, 401
        payload = jwt.decode(token, key)
        if payload["jti"] in globalvars.BLACKLIST:
            return {"error": "auth token has been blacklisted"}, 401
        return {"success": True}, 200

    except jwt.ExpiredSignatureError:
        return {"error": "Auth token expired"}, 403

    except Exception as error:
        print(error)
        return {"error": "Invalid auth token"}, 403


def encode_auth_token(iat, exp, user_id, name, email):
    "function"
    try:
        jti = str(uuid.uuid4())
        headers = {"kid": JWTKEY_CURRENT}
        payload = {
            "exp": exp,
            "iat": iat,
            "username": user_id,
            "name": name,
            "email": email,
            "jti": jti,
        }
        return jwt.encode(payload, JWTKEY[JWTKEY_CURRENT], headers=headers, algorithm="HS256")
    except Exception as error:
        return error
