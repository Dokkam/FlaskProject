from app import myapp_obj, db
from app.forms import TopCities
from app.models import Cities
from flask import render_template, flash, redirect

@myapp_obj.route("/", methods=['GET', 'POST'])
def base():
    title = 'Top Cities'
    name = 'Thomas'
    form = TopCities()

    city = db.session.query(Cities).order_by(Cities.cityRank.desc())

    if form.validate_on_submit():
        record = Cities(cityName = form.city_name.data, cityRank = form.city_rank.data)
        db.session.add(record)
        db.session.commit()
        flash (f'City of {form.city_name.data} has been added as rank {form.city_rank.data}!')
        return redirect('/')

    return render_template ('home.html', title = title, name = name, form = form, city = city)






    