import sqlite3
from django.shortcuts import render
from bangazonreports.views import Connection


def favorites_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
              select  distinct customer.id as id, customer.fullname as customer, seller.fullname as seller   from 
              (select
                f.customer_id as id,
                u.first_name || " " || u.last_name as fullname,
                f.customer_id as customerid
                from bangazonapi_customer c, auth_user as u, bangazonapi_favorite f
                where f.customer_id = c.id and
                c.user_id = u.id) as customer,
                (select
                    u.first_name || " " || u.last_name as fullname,
                    f.customer_id as customerid
                from bangazonapi_customer c, auth_user as u, bangazonapi_favorite f
                where f.seller_id = c.id and
                c.user_id = u.id) as seller
                where customer.customerid = seller.customerid
                
            """)

            dataset = db_cursor.fetchall()
            favorites = {}
            for row in dataset:
                fid = row["id"]
                
                if fid in favorites:
                    favorites[fid]['sellers'].append(row["seller"])
                else:
                    # Otherwise, create the key and dictionary value
                    favorites[fid] = {}
                    favorites[fid]["id"] = fid
                    favorites[fid]["customername"] = row["customer"]
                    favorites[fid]["sellers"] = [row['seller']]
        
        template = 'favorites/favoritesellers.html'
        context = {
            'favorite_list': favorites.values
        }

        return render(request, template, context)
