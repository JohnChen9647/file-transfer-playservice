
import os

from locust import HttpUser, between, task


FILE_NAME = os.environ.get("FILE_NAME", "32k.txt")


class DownloadUser(HttpUser):
    """Repeatedly retrieve and optionally verify one file through the gateway."""

    wait_time = between(0, 0.2)

    @task
    def download_file(self):
        with self.client.get(
            "/files",
            params={"name": FILE_NAME},
            name="/files",
            catch_response=True,
        ) as response:
            if response.status_code != 200:
                response.failure(f"HTTP {response.status_code}: {response.text[:200]}")
                return

            response.success()
            return
