import cv2
import numpy as np

import classification.red_colour as red_colour,classification.green_colour as green_colour,classification.blue_colour as blue_colour
import classification.pink_colour as pink_colour,classification.violet_colour as violet_colour,classification.cyan_colour as cyan_colour
import classification.orange_colour as orange_colour,classification.yellow_colour as yellow_colour
import segment
import result
from fastapi import FastAPI,Body
class node:
    def __init__(self,frame,attr):
        self.frame=frame
        self.attr=attr

cap=cv2.VideoCapture(0)
app=FastAPI()
@app.get("/")
def fun():
    while True:
        ret,frame=cap.read()
        frame=cv2.resize(frame,(640,480))
        obs=[]
        obs.append(node(red_colour.red(frame),'r'))
        obs.append(node(green_colour.green(frame),'g'))
        obs.append(node(blue_colour.blue(frame),'b'))
        obs.append(node(pink_colour.pink(frame),'p'))
        obs.append(node(orange_colour.orange(frame),'o'))
        obs.append(node(yellow_colour.yellow(frame),'y'))
        obs.append(node(violet_colour.violet(frame),'v'))
        obs.append(node(cyan_colour.cyan(frame),'c'))

        upper,lower=segment.detect_upper_lower(obs)
        ans=result.get_value(upper,lower)
        print(round(ans,2))
        
        cv2.imshow("FRAME",frame)
        if cv2.waitKey(0)&0xFF==27:
            break
    cap.release()
    cv2.destroyAllWindows()