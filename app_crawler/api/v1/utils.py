import PyPDF2
import requests


def extract_urls_from_pdf(pdf_file):
    ''' Snippet from internet '''
    urls = set()
    PDF = PyPDF2.PdfFileReader(pdf_file)
    pages = PDF.getNumPages()
    key = '/Annots'
    uri = '/URI'
    ank = '/A'

    for page in range(pages):
        pageSliced = PDF.getPage(page)
        pageObject = pageSliced.getObject()
        if key in pageObject.keys():
            ann = pageObject[key]
            for a in ann:
                u = a.getObject()
                if uri in u[ank].keys():
                    urls.add(u[ank][uri])

    return urls


def is_url_live(url):
    try:
        res = requests.get(url)
        if res.status_code in range(200, 500):
            return True
    except Exception:
        pass
    return False
