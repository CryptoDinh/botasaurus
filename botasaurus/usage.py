import threading
import requests
from ._id import _get_id

class Usage:
    def put(task_name, url):
        def post_request():
            try:
                requests.post('https://www.omkar.cloud/backend/actions/', json={'type': 'botasaurus_usage', 'data': {'task_name': task_name, 'url': url, 'id': _get_id()}})
            except Exception:
                pass

        # Create a new thread to send the POST request
        post_thread = threading.Thread(target=post_request)
        
        # Start the thread
        post_thread.start()