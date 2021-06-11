import io
import random
from random import randint
from tempfile import NamedTemporaryFile

from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
from wand.color import Color
from wand.image import Image


class MakeAsScan(object):
    def __init__(self, input_file, output_file, pages_with_signatures=None,
                 signatures=None):
        if signatures:
            self.signatures = [Image(filename=s) for s in signatures]
        else:
            self.signatures = []
        self.input_file = input_file
        self.output_file = output_file
        if pages_with_signatures:
            self.pages_with_signatures = [int(p) for p in
                                          pages_with_signatures.split(',')]
        else:
            self.pages_with_signatures = []

    def process_file(self):
        merger = PdfFileMerger()
        for i, page in enumerate(self.split_pdf()):
            merger.append(self.process_page(page, i + 1))
        merger = self.add_meta(merger)
        merger.write(self.output_file)
        merger.close()

    def process_page(self, f, page_number):
        page = Image(file=f, resolution=130)
        f.close()
        if self.signatures and page_number in self.pages_with_signatures:
            page = self.add_signature(page)
        page.noise("multiplicative_gaussian", attenuate=-0.15)
        page.despeckle()
        page.sharpen(radius=8, sigma=4)
        page.gamma(1.3)
        page.rotate(randint(-100, 100) / 200, background=Color('rgb(255, 255, 255)'))
        page.convert('RGB')
        file_like = io.BytesIO(page.make_blob())
        return file_like

    def add_meta(self, pdf):
        pdf.addMetadata({
            '/Creator': 'HP Scan',
            '/Producer': 'HP Scan Extended Application'
        })
        return pdf

    def add_signature(self, page):
        white = Color('#ffffff')
        empty_lines_count = i = 0
        not_white_seen = False
        signature = random.choice(self.signatures)
        for i, row in enumerate(page[20:-20]):
            if i % 10 != 0:
                continue
            not_white_count = 0
            for col in row:
                if col != white:
                    if not not_white_seen:
                        not_white_seen = True
                    not_white_count += 1
                if not_white_count > 200:
                    empty_lines_count = 0
                    break
            else:
                empty_lines_count += 1
            if empty_lines_count > 10 and not_white_seen:
                break
        else:
            i = page.height - signature.height - 50
        print(i)
        page.composite(signature, left=page.width - signature.width - 100, top=i)
        return page

    def split_pdf(self):
        input_pdf = PdfFileReader(open(self.input_file, "rb"))
        for i in range(input_pdf.numPages):
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(input_pdf.getPage(i))
            f = NamedTemporaryFile(suffix='.pdf')
            pdf_writer.write(f)
            f.seek(0)
            yield f
