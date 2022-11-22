# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 19:18:50 2022

@author: steph
"""

import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

st.title("HCI Test Study - Figma Prototype")
st.write("""Participants can take part in our study directly here on this webpage. 
This page include all the information plus guidance that the participant needs to walk through the experiment on their own.""")

dt = datetime.now()

st.write("PREPARATION")


demoform = st.form("Demographic Questionaire:")
demoform.subheader("Demographic Questionaire:")
surname = demoform.text_input("surname:")
name = demoform.text_input("last name:")
age = demoform.slider("age:",0,100)
skills = demoform.select_slider("how often do you use smartphone apps?:",["never","weekly","daily","~5 times/day","> 10 times/day"])
location = demoform.text_input("Where are you currently at:", placeholder="in class, at home")


if 'demo' not in st.session_state:
    st.session_state['demo'] = False
if 'start' not in st.session_state:
    st.session_state['start'] = False
if 'end' not in st.session_state:
    st.session_state['end'] = False
if 'sus' not in st.session_state:
    st.session_state['sus'] = False



# Now add a submit button to the form:
demo = demoform.form_submit_button("Submit")
if demo is True or st.session_state['demo']:
    st.session_state['demo'] = True 
    st.success(f"Thank you {surname} {name} for your information, we saved them successfully. You can now proceed.")
    
    st.subheader("Figma Prototype Testing")
    st.markdown("**Please read follwing instructions very carefully and click on the button below when you are ready to perform the task in your figma prototype.**")
    st.markdown("""
            ** Please be aware:: you cannot do anything wrong here. This experiment is to test our tool and not you.**
            
             **Precondition:** Before you start make sure you are on the Home Screen, for that do a "Restart" on Figma iFrame (bottom right) or press key "R". When you press the Start Button the time will be recorded automatically. No worries, you do not have a given time to complete the task.
            
             **Step 1:** The user will start at the Home Screen where he has an quick overview of his devices and settings. Then he needs to click on the menu item Setting to jump to the Setting Screen.

             **Step 2:** The user should test the carousel effect by scrolling trough the devices and get an overview of all setup/installed/connected devices. Once he did that he clicks on the Challenges menu item on the bottom of the screen to jump to the Challenges Screen.

             **Step 3:** The user sees that no challenge is setup, therefore he clicks now on the Add-Icon (Plus Icon) to add a new challenge. The user will be forwarded to the Enemy Screen.

             **Step 4:** The user needs to choose an enemy, in our scenario he need to specifically select “Geralt of Rivia”. The selection is in a scrollable list. If the user selects another enemy he will be forwarded to the Enemy-Fallback Screen where he will be informed that he need to choose “Geralt of Rivia” for this test scenario. When user selected given enemy he will be forwarded to the Device Screen.

             **Step 5:** The user needs to choose a device, in our scenario he needs to specifically select “Lights”. The selection is here again in a scrollable list. If the user selects another device he will be forwarded to the Device-Fallback Screen where he will be informed that he need to choose “Lights” for this test scenario. When user selected given device he will be forwarded to the Start Screen.
                
             **Step 6**: The user needs to start/add the challenge by clicking the button Start on the Start Screen.
                
             **Step 7:** The user sees a success message, on this Success Screen he needs to click on the button “See all my Challenges”, he will be forwarded to the Challenges (new) screen with the newly added challenge. Here the user will be informed as well that he finished his task/scenario. **Since you completed the task, press on the button "Finished Task" bellow and continue according given instructions.**
             """)
    start = st.button("[START] I understood the task, lets start")

    if start is True or st.session_state['start']:
        st.session_state['start'] = True
        dt_start = datetime.now()
        if 'dt_start' not in st.session_state:
            st.session_state['dt_start'] = dt_start
        components.iframe(src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Fproto%2FsMM0nRH0fXmQVG3uWSlfen%2FPrototype%3Fnode-id%3D61%253A965%26scaling%3Dscale-down%26page-id%3D0%253A1%26starting-point-node-id%3D1%253A288", width=800, height=600)
        end = st.button("[FINISHED TASK] I finished the task according given instructions")
    
    
    
        if end is True or st.session_state['end']:
            st.session_state['end'] = True
            dt_end = datetime.now()
            if 'dt_end' not in st.session_state:
                st.session_state['dt_end'] = dt_end
            st.success(f"Thank you {surname} {name}, please continue with survey...")
            
            susform = st.form("SUS Survey:")
            susform.subheader("SUS Survey:")
            one = susform.slider("I think that I would like to use this system frequently.",1,5)
            two = susform.slider("I found the system unnecessarily complex.",1,5)
            three = susform.slider("I thought the system was easy to use.",1,5)
            four = susform.slider("I think that I would need the support of a technical person to be able to use this system.",1,5)
            five = susform.slider("I found the various functions in this system were well integrated.",1,5)
            six = susform.slider("I thought there was too much inconsistency in this system.",1,5)
            seven = susform.slider("I would imagine that most people would learn to use this system very quickly.",1,5)
            eight = susform.slider("I found the system very cumbersome to use.",1,5)
            nine = susform.slider("I felt very confident using the system.",1,5)
            ten = susform.slider("I needed to learn a lot of things before I could get going with this system.",1,5)
            # Now add a submit button to the form:
            sus = susform.form_submit_button("Submit SUS Survey")

            
            if sus is True or st.session_state['sus']:
                st.session_state['sus'] = True
                result_sus = (((one + three + five + seven + nine)-5) + (25-(two+four+six+eight+ten)))*2.5
                st.success(f"Your SUS Score is {result_sus}")
                st.info("Based on research, a SUS score above a 68 would be considered above average and anything below 68 is below average, however the best way to interpret your results involves “normalizing” the scores to produce a percentile ranking.")
                
                
                with open(f"{name}_{surname}_results.txt", "a") as results:
                    results.write(f"\n{60*'-'}\n{dt} - NEW ENTRY:\n{name}\n{surname}\n{age}\n{skills}\n{location}\n{60*'-'}\n")
                
                with open(f"{name}_{surname}_results.txt", "a") as results:
                    results.write(f"\n{60*'-'}\nTask Completed from {name} {surname}: {(st.session_state['dt_end'] - st.session_state['dt_start']).total_seconds()} seconds\n{60*'-'}\n")
                
                with open(f"{name}_{surname}_results.txt", "a") as results:
                    results.write(f"\n{60*'-'}\nSUS-Survey from {surname} {name}:\n1.={one}\n2.={two}\n3.={three}\n4.={four}\n5.={five}\n6.={six}\n7.={seven}\n8.={eight}\n9.={nine}\n10.={ten}\n{60*'-'}\nResult Score: {result_sus}\n{60*'-'}\n")
                
                
                
                with open(f"{name}_{surname}_results.txt", "rb") as file:
                    btn = st.download_button(
                        label="Download Data & Results",
                        data=file,
                        file_name=f'data_{name}_{surname}.txt',
                        mime='text/txt')







    
    
    
    
    
    