import sqlite3
from django.shortcuts import render
from bangazonapi.models import Product
from bangazonreports.views import Connection


def expensive_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    p.id,
                    p.name,
                    p.description,
                    p.price
                from bangazonapi_product p
                where p.price >= 1000
            """)

            dataset = db_cursor.fetchall()
            products = {}
            for row in dataset:
                pid = row["id"]
                
                products[pid] = {}
                products[pid]['name'] = row["name"]
                products[pid]['description'] = row["description"]
                products[pid]['price'] = row["price"]

        template = 'products/expensive.html'
        context = {
            'expensive_list': products.values
        }

        return render(request, template, context)
