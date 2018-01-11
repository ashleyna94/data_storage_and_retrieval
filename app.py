# Dependencies 
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Set up the database
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into a new model then reflect the tables 
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save the references to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Start the session
session = Session(engine)

# Set up Flask
app = Flask(__name__)


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Query for dates and temperature observation from the last year.
    Convert the query results to a dictionary using date as the key
    and the tobs as the value. Return the json representation of your
    dictionary."""
    prcp_results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > "2016-08-22").order_by(Measurement.date).all()
    
    date = [result[0] for result in prcp_results]
    precipitation = [result[1] for result in prcp_results]
    
    date_prcp_dict = dict([result[0] for result[1] in prcp_results])
        
    
    return jsonify(date_prcp_dict)


@app.route("/api/v1.0/stations")
def stations():
    """Returns a JSON list of stations from the dataset."""
    station_results = session.query(Station.station).all()
    
    all_stations = list(np.ravel(station_results))
    
    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def temperature_observation():
    """Return a json list of Temperature Observations (tobs) for 
    the previous year."""
    tobs_results = session.query(Measurement.tobs).filter(Measurement.date > "2016-08-22").order_by(Measurement.date).all()
    
    all_tobs = list(np.ravel(tobs_results))
    
    return jsonify(all_tobs)


@app.route("/api/v1.0/<start>")
def hi():
    """Return a json list of the minimum temperature, the average 
    temperature, and the max temperature for a given start. 
    Then calculate TMIN, TAVG, and TMAX for all dates greater than 
    and equal to the start date."""


@app.route("/api/v1.0/<start>/<end>")
def hihi():
    """Return a json list of the minimum temperature, the average
    temperature, and the max temperature for a given start-end range.
    Then calculate the TMIN, TAVG, and TMAX for dates between the 
    start and end date inclusive."""
    
    

if __name__ == "__main__":
    app.run()

