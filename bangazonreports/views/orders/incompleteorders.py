import sqlite3
from django.shortcuts import render
from bangazonapi.models import Order
from bangazonreports.views import Connection


def incomplete_order_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    o.id,
                    o.created_date,
                    u.first_name || " " || u.last_name as fullname,
                    sum(p.price) as TotalCost
                from bangazonapi_order o, bangazonapi_customer c, auth_user as u, bangazonapi_product p, bangazonapi_orderproduct op
                where o.customer_id = c.id and
                c.user_id = u.id and
                p.id = op.product_id and
                o.id = op.order_id and
                o.payment_type_id is null
                GROUP BY o.id
            """)

            dataset = db_cursor.fetchall()
            orders = {}
            for row in dataset:
                oid = row["id"]
                
                orders[oid] = {}
                orders[oid]['id'] = row["id"]
                orders[oid]['fullname'] = row["fullname"]
                orders[oid]['totalcost'] = row["TotalCost"]
                
        template = 'orders/incomplete.html'
        context = {
            'incomplete_list': orders.values
        }

        return render(request, template, context)
