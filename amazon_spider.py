import scrapy
import xlsxwriter

# Verificar se existe iPhone e Apple no titulo
def verify_iphone_is_in(s):
    result = str(s).lower().split(' ')

    if ('iphone' in result) and ('apple' in result):
        return True
    return False

class AmazonSpider(scrapy.Spider):
    name = "Amazon Spider"
    start_urls = ['https://www.amazon.com.br/s?k=iphone']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.workbook = xlsxwriter.Workbook('amazon_iphones.xlsx')
        self.worksheet = self.workbook.add_worksheet()

        # TableHeader
        self.title = self.workbook.add_format(
            {'bold': True, 'font_size': 16, 'align': 'center', 'valign': 'vcenter', 'border': 2})
        self.title.set_bg_color('#c2c2c6')
        self.worksheet.set_row(0, 70)
        self.worksheet.set_column('A:A', 115)
        self.worksheet.set_column('B:B', 30)

        self.worksheet.write('A1', 'PRODUTO', self.title)
        self.worksheet.write('B1', 'VALOR', self.title)

        # style Normal
        self.normal = self.workbook.add_format({'bold': True})
        self.normal.set_bg_color('#c6c6c0')

        # style Aviso
        self.warning = self.workbook.add_format({'bold': True, 'font_color': 'gray'})
        self.warning.set_bg_color('#c0c0c0')

    def parse(self, response, **kwargs):
        # Resultados na primira página
        produt_list = response.css('.a-section.a-spacing-medium')

        for index, product in enumerate(produt_list, 2):

            product_title = product.css("span.a-size-base-plus.a-color-base.a-text-normal").css(
                "::text").extract_first()
            product_price = product.css("span.a-offscreen").css("::text").extract_first()

            # Filtragem
            if verify_iphone_is_in(product_title):
                if product_title is not None and product_price is not None:
                    self.worksheet.write(f'A{index}', product_title, self.normal)
                    self.worksheet.write(f'B{index}', product_price, self.normal)
                else:
                    self.worksheet.write(f'A{index}', 'ITEM FORA DO ESCOPO DA PESQUISA', self.warning)
                    self.worksheet.write(f'B{index}', '---', self.warning)
            else:
                self.worksheet.write(f'A{index}', 'ITEM FORA DO ESCOPO DA PESQUISA', self.warning)
                self.worksheet.write(f'B{index}', '---', self.warning)

        self.workbook.close()
