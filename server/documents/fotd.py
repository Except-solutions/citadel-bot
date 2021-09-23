from datetime import datetime

from odmantic import Model, Reference

from server.documents.users import UserDoc


class FodtDoc(Model):
    datetime: datetime
    user_doc: UserDoc = Reference()
