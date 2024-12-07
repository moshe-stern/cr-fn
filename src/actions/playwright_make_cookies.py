from playwright.async_api import APIRequestContext


async def playwright_make_cookies(context: APIRequestContext, access_token: str):
    url = "https://members.centralreach.com/api/?framework.authtoken"
    payload = {"token": access_token}
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    response = await context.post(url, headers=headers, data=payload)
    if response.status_text != "OK":
        raise Exception(response.text)
