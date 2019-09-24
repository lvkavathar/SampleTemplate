import requests
import json
import sys
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
import datetime
from scipy import linalg
from scipy.stats import f
from scipy.optimize import least_squares

with open('configuration.json') as json_configuration_file:
    configuration = json.load(json_configuration_file)
    predictionSettingsEndPoint = configuration["predictionSettingsEndPoint"]
    assetHealthValuesEndPoint = configuration["predictionSettingsEndPoint"]
    predictionEndPoint = configuration["predictionSettingsEndPoint"]


class prediction:
    def __init__(self, access_key, asset_id, url):
        self.access_key = access_key
        self.asset_id = asset_id
        self.url = url

    def get_predict_settings(self):
        headers = {'content-type': 'application/json',
                   'access-key': self.access_key, 'assetID': self.asset_id}
        r = requests.get(
            self.url + predictionSettingsEndPoint, headers=headers)
        return r.json()

    def post_predict_settings(self, payload):
        headers = {'content-type': 'application/json',
                   'access-key': self.access_key, 'assetID': self.asset_id}
        r = requests.post(self.url + predictionSettingsEndPoint,
                          data=json.dumps(payload), headers=headers)
        return r.json()

    def post_predict_vals(self, payload):
        headers = {'content-type': 'application/json',
                   'access-key': self.access_key, 'assetID': self.asset_id}
        r = requests.post(self.url + predictionEndPoint,
                          data=json.dumps(payload, default=str), headers=headers)
        return r.json()

    def get_asset_health_vals(self):
        headers = {'content-type': 'application/json',
                   'access-key': self.access_key, 'assetID': self.asset_id}
        r = requests.get(self.url + assetHealthValuesEndPoint, headers=headers)
        return r.json()

    def get_API_endpoint_names(self):
        return "predictionEndPoint: " + predictionEndPoint + ", assetHealthValuesEndPoint: " + assetHealthValuesEndPoint + ", predictionEndPoint: " + predictionEndPoint
