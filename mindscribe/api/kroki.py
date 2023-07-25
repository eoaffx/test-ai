```python
import requests

def generate_mindmap(data):
    KROKI_API_URL = "https://kroki.io"
    KROKI_DIAGRAM_TYPE = "mindmap"
    
    response = requests.post(
        f"{KROKI_API_URL}/{KROKI_DIAGRAM_TYPE}/svg",
        data=data.encode("utf-8"),
        headers={"Content-Type": "text/plain"}
    )
    
    if response.status_code == 200:
        return response.content.decode("utf-8")
    else:
        raise Exception("Failed to generate mindmap with Kroki API")
```