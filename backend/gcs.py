from . import settings
from google.cloud.storage import Client
from google.cloud.storage.blob import Blob

class Content:
    """
    TODO luigiの処理を参考に書き直す
    https://luigi.readthedocs.io/en/stable/_modules/luigi/contrib/gcs.html#GCSClient.exists
    """
    def __init__(self, name):
        self._bucket = None
        self._blob = None

        self.name = name

    def bucket(self):
        if self._bucket is None:
            client = Client()
            self._bucket = client.get_bucket(settings.BUCKET_NAME)
        return self._bucket

    def blob(self):
        if self._blob is None:
            self._blob = Blob(self.name, self.bucket())
        return self._blob

    def get(self):
        # TODO ファイルでもディレクトリでも同じクラスを返すような感じにリファクタ
        if self.isdir():
            return [dict(name=x.lstrip(self.name).lstrip("/"), path=x) for x in self._get_files()]
        else:
            return self.blob().download_as_string().decode()

    def _get_files(self):
        """
        このリンクを参考
        https://github.com/googleapis/google-cloud-python/issues/920#issuecomment-326125992
        """
        path = self.name if self.name.endswith("/") else self.name + "/"
        items = self.bucket().list_blobs(prefix=path, delimiter="/")._get_next_page_response().get("items")
        if items:
            return [x["name"] for x in items]
        else:
            return []

    def exists(self):
        if self.isdir():
            return True
        return self.blob().exists()

    def isdir(self):
        return len(self._get_files()) > 1

if __name__ == "__main__":
    con = Content("job-career")
    blob = con.blob()
    import pdb;pdb.set_trace()
