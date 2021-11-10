import datetime
import docxtpl
from docxtpl import DocxTemplate,InlineImage
from docx.shared import Cm
import pandas as pd

data = pd.read_csv('data.csv',sep=';')
brand = data.brand.values[0]
model = data.model.values[0]
consumption = data.consumption.values[0]
price = data.price.values[0]
picture = 'ext-front_tcm-3020-1767644.png'
template = 'template.docx'




def to_template(brand, model, consumption, price, picture, template):
    context = {'brand': brand, 'model': model, 'price': price, 'consumption': consumption}

    template = DocxTemplate(template)
    img_size = Cm(15)
    picture  = InlineImage(template,picture,img_size)
    context['picture'] = picture

    template.render(context)

    template.save(brand+'_'+model+'_'+str(datetime.datetime.now().date())+'_report.docx')

to_template(brand, model, consumption, price, picture, template)
