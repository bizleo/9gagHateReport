from dataclasses import dataclass

import requests

PRODUCTION_API_HOST = 'http://9gag.com'

@dataclass
class NineGagAPIClient:
    """Basic client for 9gag."""
    user: None = None
    host: str = PRODUCTION_API_HOST

    def _get_json(
        self,
        url: str,
        timeout: float = 4.0,
    ) -> dict:
        full_url = str(self.host) + url
        headers = None
        params_json = {} 
        response = requests.get(
            url=full_url,
            headers=headers,
            params=params_json,
            timeout=timeout,
        )

        if response.status_code == requests.codes.get("ok"):
            return response.json()
        else:
            return {"Error text": response.text}
