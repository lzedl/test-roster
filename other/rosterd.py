# -*- coding: utf8 -*-
from __future__ import unicode_literals


class Roster(object):
    data = {
        "contacts": [
            {
                "id": 1,
                "display_name": "Наполеон",
                "last_name": "Бонапард",
                "real_name": "Наполеон",
                "second_name": "",
                "records": [
                    {
                        "type": "email",
                        "description": "Основная почта",
                        "id": "napoleon@bonapard.com"
                    },
                    {
                        "type": "jabber",
                        "description": "main jabber",
                        "id": "napoleon@bonapard.com"
                    },
                    {
                        "type": "mobile",
                        "description": "So call me may be",
                        "id": "+71234567890"
                    }
                ]
            },
            {
                "id": 12,
                "display_name": "Адик",
                "last_name": "Гитлер",
                "real_name": "Адольф",
                "second_name": "",
                "records": [

                ]
            }
        ]
    }

    def getFullList(self):
        return [(c["id"], c["display_name"]) for c in self.data["contacts"]]

    def getContactData(self, contactID):
        for element in self.data["contacts"]:
            if element["id"] == contactID:
                return element
        return {}


roster = Roster()
