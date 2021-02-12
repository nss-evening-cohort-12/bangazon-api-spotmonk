import sqlite3
from django.shortcuts import render
from bangazonapi.models import Order
from bangazonreports.views import Connection


def completed_order_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    o.id,
                    o.created_date,
                    u.first_name || " " || u.last_name as fullname
                from bangazonapi_order o, bangazonapi_customer c, auth_user as u
                where o.customer_id = c.id and
                c.user_id = u.id and
                o.payment_type_id is not null
            """)

            dataset = db_cursor.fetchall()
            orders = {}
            for row in dataset:
                pid = row["id"]
                
                orders[pid] = {}
                orders[pid]['fullname'] = row["fullname"]
                orders[pid]['created_date'] = row["created_date"]
                
        template = 'orders/completed.html'
        context = {
            'completed_list': orders.values
        }

        return render(request, template, context)
