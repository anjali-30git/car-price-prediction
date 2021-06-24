 #import libraries
from types import MethodDescriptorType
import numpy as np
from flask import Flask, render_template,request,redirect
import pickle
#Initialize the flask App
app = Flask(__name__)
model = pickle.load(open('XGBoostDeploy.pkl', 'rb'))

@app.route('/', methods=['GET','POST'])
def index():
   return render_template("index.html")
#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    # For rendering results on HTML GUI
    manufacturer = request.form['manufacturer']
    condition = request.form['condition']
    fuel = request.form['fuel']
    size = request.form['size']
    type = request.form['type']
    transmission = request.form['transmission']
    paint_color = request.form['paint_color']
    type = request.form['type']
    drive = request.form['drive']
    cylinders = request.form['cylinders']
    year = request.form['year']
    odometer = request.form['odometer']

    manufacturer =1
    condition = 1
    fuel = 1
    size = 1
    type = 1
    transmission = 1
    paint_color = 1
    type  = 1
    drive = 1
    cylinders = 1
    year = int(year)
    odometer =int(odometer)


    car = ["jeep","bmw","dodge","chevrolet","ford","honda","toyota","nissan","subaru","gmc","volkswagen","kia","acura","ram","chrysel","volvo","mercedes-benz", "audi", "infiniti","mazda","mini","buick","mitsubishi","rover","pontiac","lincoln","lexus","flat","jaguar","mercury","saturn", "tesla", "harley-davidson", "ferrari", "land rover", "porche", "alfa-romeo", "morgan", "aston martin"]
    for x in car:
        if(x==manufacturer):
            m = car.index(x)
            
    con = ["like new","good","excellent","fair","new","salvage"]
    for x in con:
        if(x==condition):
            c = con.index(x)
    
    ful = ["gas", "diesel", "electric", "hybrid","other"]
    for x in ful:
        if(x==fuel):
            f = ful.index(x)

    siz = ["full-size", "mid-size", "sub-compact", "compact"]
    for x in siz:
        if(x==size):
            s = siz.index(x)  

    typ = ["offroad","sedan", "pickup", "convertable", "van", "truck", "SUV", "coupe", "hatchback", "mini-van", "other", "bus"]
    for x in typ:
        if(x==type):
            t = typ.index(x)

    trans = ["automatic", "manual", "other"]
    for x in trans:
        if(x==transmission):
            tr = trans.index(x)

    paint = ["silver", "grey", "red", "white", "black", "blue", "brown", "yellow", "orange", "custom", "purple"]
    for x in paint:
        if(x==paint_color):
            p = paint.index(x)

    driv = ["4wd","rwd","fwd"]
    for x in driv:
        if(x==drive):
            d = driv.index(x)
        

    cyl = ["4 cylinders", "5 cylinders", "6 cylinders", "8 cylinders", "10 cylinders", "other", "12 cylinders", "3 cylinders"]
    for x in cyl:
        if(x==cylinders):
            cy = paint.index(x)




#    int_features = [x for x in request.form.values()]
#    size1 = np.array([(size, type)])

#    arr = [year, odometer]

#    final_features = [ arr[0], m, c, f, s, t,  tr, p, t, d, cy,arr[1]]
    final_features = np.array([([year,odometer], manufacturer, condition,fuel, size, type,  transmission, paint_color, drive, cylinders)])
    
    sc=pickle.load(open('StandardScaler.sav','rb'))
    final_features=sc.transform(final_features)

    prediction = model.predict(final_features)

    return render_template("index.html", prediction_text='The Car price is : '.format(prediction))

if __name__ == "__main__":
    app.run(debug=True)