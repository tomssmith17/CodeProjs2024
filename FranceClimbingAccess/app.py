from flask import Flask,request,render_template
import pandas as pd
import ipyleaflet as leaf
#geopandas


#googlemapsapi with token in textfile, read in to keep secret

#add flask stuff so that they interact properly
#result will be text output of best climb destination and map showing route. 
#top 3 results???


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/analyze",methods=['POST'])

def analyze():
    cType = request.form['ClimbType']
    Days = request.form['Days']
    Region = request.form['Region']

    #cAreas = GDF
    #get data from french climb website and throw into gdf
    #use osm for public transit info
    data = {
        'Crags': ['Fountainbleau', 'Les Calanques', 'Verdon Gorge', 'Ceuse', 'Gorge du Tarn'],
        'Region': ['Paris', 'South East', 'South East', 'South East', 'South Central'],
        'Size': ['Grande', 'Large', 'Grande', 'Grande', 'Medium'],
        'Style': ['Bouldering', 'Ropes', 'Ropes', 'Ropes', 'Ropes'],
        'GPS': [(1,2), (3,4), (5,6), (7,8), (9,10)]
    }
    user_input = [cType, int(Days), Region]

    '''
    def questions(user_input, climb_all):
        print('here are your results: ')
        print(user_input) #strings

        subData_df = climb_all[(climb_all['Style'] == user_input[0]) & (climb_all['Region'] == user_input[2])] 
        
        if int(user_input[1]) <= 3:
            subData_df2 = subData_df[(subData_df['Size'] == 'Small') or (subData_df['Size'] == 'Medium')]
        elif int(user_input[1]) > 3 and int(user_input[1]) <= 5:
            subData_df2 = subData_df[subData_df['Size'] == 'Large']
        else:
            subData_df2 = subData_df[subData_df['Size'] == 'Grande']

        print('here is your subset: ')
        print(subData_df2)
        #subset data table to desired destinations w/ if else statement
        #output queried table to use later for mapping > look up how again




    df = pd.DataFrame(data)
    print(df)

    questions(answers, df)
    '''
    result = [type(cType), type(Days), type(Region)]

    return render_template('index.html',result = result)

if __name__ == "__main__":
    app.run(debug=True)



"""
what type of climbing do you want to do? bouldering or sport or other
how many days climbing > used to assess if multiple areas are PT accessible
what region you want to go to?
here are your results. 
juniper notebook of results with map and results table or something

1. Data needed:
    -climbing area locations (worth a visit haha so set lower limit to ignore) - webscrapping?
    -bus networks + train network + walking + bike rental things haha???
    -uber / ride share???
2. starting point paris
3. shape file or just gps coords would be easier - projections and such???
4. 
5. ranking of variety of climbing grades??? or something like this

most accessible climbing areas via public transport in france, order/rank with overall score, map routes, 
 from nearest metro area, directions, depends on crag
 good web map opportunity here
table of all climbing areas in france:
name, region, nearest city/town, access from paris, gps location(s), type climbing, etc.
public data: train routes, bus routes, walking in google maps api
websites with climbing area locations (webscrape / manual pull / shapefile of area and pick center)
"""






