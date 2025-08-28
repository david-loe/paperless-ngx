def get_parser(*args, **kwargs):
    from paperless_mail.parsers import MailDocumentParser

    return MailDocumentParser(*args, **kwargs)


def emlfix_consumer_declaration(sender, **kwargs):
    return {
        "parser": get_parser,
        "weight": 0,
        "mime_types": {
            "text/html": ".eml",
        },
    }
