#!/usr/bin/env python
import time
import bluetooth
import re
import serial
import random
import pylcdlib
import MySQLdb
import RPi.GPIO as GPIO
from MindwaveDataPoints import RawDataPoint
from MindwaveDataPoints import AttentionDataPoint
from MindwaveDataPoints import MeditationDataPoint
from MindwaveDataPoints import EEGPowersDataPoint
from MindwaveDataPointReader import MindwaveDataPointReader



if __name__ == '__main__':
        # mincap 1 mac address
        #mac1 = '20:FA:BB:01:2A:F8'
        mac1 = '74:E5:43:D5:6D:C8'

        
db = MySQLdb.connect("localhost","root","root","PerformanceDataTable" )

cursor = db.cursor()


session_id = input("please enter session id:.....")
print "PS: Memorise or document session id... session id is:"
print session_id
print "===================="
print "===================="
print "initialization and headset connection.........."
while(True):
        
        time.sleep(2)

        
        mindwaveDataPointReader1 = MindwaveDataPointReader()
        mindwaveDataPointReader1.start(mac1)
                
        att_value=0
        med_value=0
        delta_value=0
        theta_value=0
        low_gamma_value=0
        mid_gamma_value=0
        low_beta_value=0
        high_beta_value=0
        low_alpha_value=0
        high_alpha_value=0
       
        while(True):
                dataPoint1 = mindwaveDataPointReader1.readNextDataPoint()
                if (dataPoint1.__class__ is AttentionDataPoint):
                                att_value = dataPoint1.attentionValue
                                print att_value
                   
                if (dataPoint1.__class__ is MeditationDataPoint):
                                med_value = dataPoint1.meditationValue
                                print med_value
                
                if (dataPoint1.__class__ is EEGPowersDataPoint):
                                delta_value = dataPoint1.delta
                                print delta_value
        
                if (dataPoint1.__class__ is EEGPowersDataPoint):
                                theta_value = dataPoint1.theta
                                print theta_value                                
   
                if (dataPoint1.__class__ is EEGPowersDataPoint):
                                low_alpha_value = dataPoint1.lowAlpha
                                print low_alpha_value
                        
                if (dataPoint1.__class__ is EEGPowersDataPoint):
                                high_alpha_value = dataPoint1.highAlpha
                                print high_alpha_value
                                
                if (dataPoint1.__class__ is EEGPowersDataPoint):
                                low_beta_value = dataPoint1.lowBeta
                                print low_beta_value
                                
                if (dataPoint1.__class__ is EEGPowersDataPoint):
                                high_beta_value = dataPoint1.highBeta
                                print high_beta_value
                                
                if (dataPoint1.__class__ is EEGPowersDataPoint):
                                low_gamma_value = dataPoint1.lowGamma
                                print low_gamma_value
                                
                if (dataPoint1.__class__ is EEGPowersDataPoint):
                                mid_gamma_value = dataPoint1.midGamma
                                print mid_gamma_value

                                sql = """INSERT INTO table_main(Attention, Meditation, Delta, Theta, LowAlpha, HighAlpha, LowBeta, HighBeta, LowGamma, MidGamma, SessionId) VALUES(%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d)"""%(att_value, med_value, delta_value, theta_value, low_alpha_value, high_alpha_value, low_beta_value, high_beta_value, low_gamma_value, mid_gamma_value, session_id)

                                #sql = "INSERT INTO table_main(Attention, Meditation, Delta, Theta, LowAlpha, HighAlpha, LowBeta, HighBeta, LowGamma, MidGamma, SessionId)
                                #VALUES ('att_value', 'med_value', 'delta_value', 'theta_value', 'low_alpha_value', 'high_alpha_value', 'low_beta_value', 'high_beta_value', 'low_gamma_value', 'mid_gamma_value', 'session_id')"
                                #cursor.execute(sql)
                                try:
                                        cursor.execute(sql)
                                        db.commit()
                                        print "entry accepted"
                                        print "===================="
                                except:
                                        db.rollback()
                                        print "entry declined"
                                        print "===================="
                                       
                                     #   sql = """INSERT INTO table_main(Attention, Meditation, Delta, Theta, LowAlpha, HighAlpha, LowBeta, HighBeta, LowGamma, MidGamma, SessionId)
                                     #VALUES(%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d )"""
                                     #(att_value, med_value, delta_value, theta_value, low_alpha_value, high_alpha_value, low_beta_value, high_beta_value, low_gamma_value, mid_gamma_value, session_id)

        mindwaveDataPointReader1.close()
        time.sleep(2)
