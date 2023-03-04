{'name': 'Product Grade',
 'version': '16.0.1.0.0',
 'sequence': -1,
 'website': 'https://www.odoo.com/page/most_sold',
 'category': 'all',
 'installable': True,
 'application': True,
 'auto_install': False,
 'depends': ['base','point_of_sale'],
 'data': [
     'views/product_template_inherit.xml'
 ],
 'assets':{
  'point_of_sale.assets':[
       'pos_grade/static/scr/xml/pos_session_grade.xml',
       'pos_grade/static/scr/xml/pos_receipt.xml',
       'pos_grade/static/scr/js/pos_receipt.js'
 ]
     }
 }