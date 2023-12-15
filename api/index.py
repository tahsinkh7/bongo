from flask import Flask, request, Response
import requests
import re

app = Flask(__name__)

@app.route('/<string:channel_id>.m3u8')
def generate_link(channel_id):
    url = channel_id
    headers = {
        "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJjZjllYTlmNC1iYTg2LTQxYTktYTg0Ny0xOGYxNjY0MWMzN2QiLCJpc3MiOiJIRUlNREFMTCIsInJvbGVzIjpbIlJPTEVfVVNFUiIsIlJPTEVfVVNFUl9BTk9OWU1PVVMiXSwidXNlcm5hbWUiOiJhbm9ueW1vdXMiLCJjbGllbnRfbG9naW5faWQiOjM0NzU1MzExMzUwLCJjbGllbnRfaWQiOiI0YzExZjUzNTg0ODE0ODRlOWI0NGExNDY3NmRlY2NlNSIsInBsYXRmb3JtX2lkIjoiYWJmZWE0NjItZjY0ZC00OTFlLTljZDktNzVlZTAwMWY0NWIwIiwiYm9uZ29faWQiOiJjZjllYTlmNC1iYTg2LTQxYTktYTg0Ny0xOGYxNjY0MWMzN2QiLCJ1c2VyX3R5cGUiOiJhbm9ueW1vdXMiLCJpYXQiOjE3MDI1NDk0MTYsImV4cCI6MTcxMDMyNTQyNi4wLCJjb3VudHJ5Q29kZSI6IkJEIiwicHJlZmVycmVkX3VzZXJuYW1lIjpudWxsfQ.XNJwChCnNn79cut4_E7gYwn_cAGlAvRENH8EgZAeXWtM2unNiHB8GfJ2UQvZgDvK3CfH5pEiEFRR3SYF-Vflkh81-Lp9CqH-OGrubs8u-zl9x4kKHocp3jfqXIDi_uq5O9zitIkoAFP5J8X2C1gktozFUcluW5hRDsG2qT-6U72A63FtF0DwtOB37fFRjK1j8ricjvOjB733PSq7eJtY7DRlhDKFK8F_kmvL4xoutScd1dXdyKAIfoh_aS9iLN9yny14Q8_h4-Yiwhjd9eyPpFydEMmBsDhtE_6F77ymsTtCfF3d1VXP63B1-K_L1j6b1fRZANMKcYGO6ZuUv-6qejT0l7qvbhsU4b0lwDpfODlv_vDS69GY9qhLAgaSAyMtd5bgjXWG6mUA-2zohF9b5v4C-e2RiH3xmAd-1zr_uT16lVndZBoBY4wQQaIOC5ajQGJ2mv7WChp2PCHkzsNM1WOlnBt2I0WVFuwFOgC1HP6LKaPOgIa8fXshneXlUTORrTGmKeRNxwk67FxRzEyCmCU6yu4pDAZiaeTFyes1kXUNRTISVTg6rS2bBs-fug0UKhvUWBgqewvpRSzmZQskEg1FoP_Q6U3YYOwlTDuhv3sGRoKPyYWqB1dGf0JKuWv5uvQI8dH4Ue45y8vNXxLGqPgAk8EGrHULu022HOqTrCI",
        "referer": "https://bongobd.com",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
        "country-code": "QkQ%3D"
    }

    response = requests.get(f"https://api.bongo-solutions.com/ironman/api/v1/content/detail/{url}", headers=headers)

    data = response.json()
    link = data["feed"]["source"]["feedLink"]

    amit = "https://live.bongobd.com/hls/"
    flink = link
    match = re.search(r'\/([^\/]+)\.m3u8$', link)

    if match:
        extracted_part = match.group(1)
        new_url = re.sub(r'\/[^\/]+\.m3u8$', '/' + extracted_part + '.m3u8', link)
        
        # Combine the headers with the new_url
        headers_combined = {
            "authorization": headers["authorization"],
            "referer": headers["referer"],
            "user-agent": headers["user-agent"],
            "Content-Type": headers["Content-Type"],
            "country-code": headers["country-code"]
        }

        # Create a response with a redirect and include headers
        resp = Response("", status=302)
        resp.headers["Location"] = new_url
        resp.headers.update(headers_combined)

        return resp
    else:
        pass

    return ""

@app.route("/ts")
def handle_ts():
    headers = {
        "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJjZjllYTlmNC1iYTg2LTQxYTktYTg0Ny0xOGYxNjY0MWMzN2QiLCJpc3MiOiJIRUlNREFMTCIsInJvbGVzIjpbIlJPTEVfVVNFUiIsIlJPTEVfVVNFUl9BTk9OWU1PVVMiXSwidXNlcm5hbWUiOiJhbm9ueW1vdXMiLCJjbGllbnRfbG9naW5faWQiOjM0NzU1MzExMzUwLCJjbGllbnRfaWQiOiI0YzExZjUzNTg0ODE0ODRlOWI0NGExNDY3NmRlY2NlNSIsInBsYXRmb3JtX2lkIjoiYWJmZWE0NjItZjY0ZC00OTFlLTljZDktNzVlZTAwMWY0NWIwIiwiYm9uZ29faWQiOiJjZjllYTlmNC1iYTg2LTQxYTktYTg0Ny0xOGYxNjY0MWMzN2QiLCJ1c2VyX3R5cGUiOiJhbm9ueW1vdXMiLCJpYXQiOjE3MDI1NDk0MTYsImV4cCI6MTcxMDMyNTQyNi4wLCJjb3VudHJ5Q29kZSI6IkJEIiwicHJlZmVycmVkX3VzZXJuYW1lIjpudWxsfQ.XNJwChCnNn79cut4_E7gYwn_cAGlAvRENH8EgZAeXWtM2unNiHB8GfJ2UQvZgDvK3CfH5pEiEFRR3SYF-Vflkh81-Lp9CqH-OGrubs8u-zl9x4kKHocp3jfqXIDi_uq5O9zitIkoAFP5J8X2C1gktozFUcluW5hRDsG2qT-6U72A63FtF0DwtOB37fFRjK1j8ricjvOjB733PSq7eJtY7DRlhDKFK8F_kmvL4xoutScd1dXdyKAIfoh_aS9iLN9yny14Q8_h4-Yiwhjd9eyPpFydEMmBsDhtE_6F77ymsTtCfF3d1VXP63B1-K_L1j6b1fRZANMKcYGO6ZuUv-6qejT0l7qvbhsU4b0lwDpfODlv_vDS69GY9qhLAgaSAyMtd5bgjXWG6mUA-2zohF9b5v4C-e2RiH3xmAd-1zr_uT16lVndZBoBY4wQQaIOC5ajQGJ2mv7WChp2PCHkzsNM1WOlnBt2I0WVFuwFOgC1HP6LKaPOgIa8fXshneXlUTORrTGmKeRNxwk67FxRzEyCmCU6yu4pDAZiaeTFyes1kXUNRTISVTg6rS2bBs-fug0UKhvUWBgqewvpRSzmZQskEg1FoP_Q6U3YYOwlTDuhv3sGRoKPyYWqB1dGf0JKuWv5uvQI8dH4Ue45y8vNXxLGqPgAk8EGrHULu022HOqTrCI",
        "referer": "https://bongobd.com",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
        "country-code": "QkQ%3D"
    }

    ts_id = request.args.get("id")
    base = request.args.get("base")
    response = requests.get(base + ts_id, headers=headers)

    return response.content

if __name__ == '__main__':
    app.run(debug=True)
