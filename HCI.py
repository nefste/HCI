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
if 'ueq' not in st.session_state:
    st.session_state['ueq'] = False



# Now add a submit button to the form:
demo = demoform.form_submit_button("Submit")
if demo is True or st.session_state['demo']:
    st.balloons()
    st.session_state['demo'] = True 
    st.success(f"Thank you {surname} {name} for your information, we saved them successfully. You can now proceed.")
    
    st.subheader("Figma Prototype Testing")
    st.markdown("**Please read follwing instructions very carefully and click on the button below when you are ready to perform the task in your figma prototype.**")
    st.markdown("""
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
                st.balloons()
                st.session_state['sus'] = True
                result_sus = (((one + three + five + seven + nine)-5) + (25-(two+four+six+eight+ten)))*2.5
                st.success(f"Your SUS Score is {result_sus}")
                st.info("Based on research, a SUS score above a 68 would be considered above average and anything below 68 is below average, however the best way to interpret your results involves “normalizing” the scores to produce a percentile ranking.")
                
                st.write("")
                ueqform = st.form("UEQ Survey:")
                ueqform.subheader("UEQ Survey:")
                ueqform.write("For the assessment of the product, please fill out the following questionnaire. The questionnaire consists of pairs of contrasting attributes that may apply to the product. The circles between the attributes represent gradations between the opposites. You can express your agreement with the attributes by ticking the circle that most closely reflects your impression.")
                ueqform.write("Example:")
                
                exleft, exanswer, exright = ueqform.columns([3,7,3])
                
                #Example
                exleft.write("attractive")
                exright.write("unattractive")
                exleft.write("---")
                exright.write("---")
                example = exanswer.slider("",1,7,key='example', value=2)
                
                ueqform.write("This response would mean that you rate the application as more attractive than unattractive.")
                ueqform.write("---")
                ueqform.subheader("Lets start with the survey:")
                
                left, answer, right = ueqform.columns([3,7,3])
                #1
                left.write("annoying")
                right.write("enjoyable")
                left.write("---")
                right.write("---")
                q1 = answer.slider("",1,7,key='q1')
                
                
                #2
                left.write("not understandable")
                right.write("understandable")
                left.write("---")
                right.write("---")
                q2 = answer.slider('',1,7,key='q2')
                
                #3
                left.write("creative")
                right.write("dull")
                left.write("---")
                right.write("---")
                q3 = answer.slider('',1,7,key='q3')
                
                #4
                left.write("easy to learn")
                right.write("difficult to learn")
                left.write("---")
                right.write("---")
                q4 = answer.slider('',1,7,key='q4')
                
                #5
                left.write("valuable")
                right.write("inferior")
                left.write("---")
                right.write("---")
                q5 = answer.slider('',1,7,key='q5')
                
                #6
                left.write("boring")
                right.write("exciting")
                left.write("---")
                right.write("---")
                q6 = answer.slider('',1,7,key='q6')
                
                #7
                left.write("not interesting")
                right.write("interesting")
                left.write("---")
                right.write("---")
                q7 = answer.slider('',1,7,key='q7')
                
                #8
                left.write("unpredictable")
                right.write("predictable")
                left.write("---")
                right.write("---")
                q8 = answer.slider('',1,7,key='q8')
                
                #9
                left.write("fast")
                right.write("slow")
                left.write("---")
                right.write("---")
                q9 = answer.slider('',1,7,key='q9')
                
                #10
                left.write("inventive")
                right.write("conventional")
                left.write("---")
                right.write("---")
                q10 = answer.slider('',1,7,key='q10')
                
                #11
                left.write("obstructive")
                right.write("inventive")
                left.write("---")
                right.write("---")
                q11 = answer.slider('',1,7,key='q11')
                
                #12
                left.write("good")
                right.write("bad")
                left.write("---")
                right.write("---")
                q12 = answer.slider('',1,7,key='q12')
                
                #13
                left.write("complicated")
                right.write("easy")
                left.write("---")
                right.write("---")
                q13 = answer.slider('',1,7,key='q13')
                
                #14
                left.write("unlikable")
                right.write("pleasing")
                left.write("---")
                right.write("---")
                answer.write("")
                q14 = answer.slider('',1,7,key='q14')
                
                #15
                left.write("usuable")
                right.write("leading edge")
                left.write("---")
                right.write("---")
                answer.write("")
                q15 = answer.slider('',1,7,key='q15')
                
                #16
                left.write("unpleasant")
                right.write("pleasant")
                left.write("---")
                right.write("---")
                q16 = answer.slider('',1,7,key='q16')
                
                #17
                left.write("secure")
                right.write("not secure")
                left.write("---")
                right.write("---")
                q17 = answer.slider('',1,7,key='q17')
                
                #18
                left.write("motivating")
                right.write("demotivating")
                left.write("---")
                right.write("---")
                q18 = answer.slider('',1,7,key='q18')
                
                #19
                left.write("meets expectations")
                right.write("doesnt m' expect.")
                left.write("---")
                right.write("---")
                q19 = answer.slider('',1,7,key='q19')
                
                #20
                left.write("inefficient")
                right.write("efficient")
                left.write("---")
                right.write("---")
                q20 = answer.slider('',1,7,key='q20')
                
                #21
                left.write("clear")
                right.write("confusing")
                left.write("---")
                right.write("---")
                q21 = answer.slider('',1,7,key='q21')
                
                #22
                left.write("impractical")
                right.write("practical")
                left.write("---")
                right.write("---")
                answer.write("")
                q22 = answer.slider('',1,7,key='q22')
                
                #23
                left.write("organised")
                right.write("cluttered")
                left.write("---")
                right.write("---")
                answer.write("")
                q23 = answer.slider('',1,7,key='q23')
                
                #24
                left.write("attractive")
                right.write("unatractive")
                left.write("---")
                right.write("---")
                q24 = answer.slider('',1,7,key='q24')
                
                #25
                left.write("friendly")
                right.write("unfriendly")
                left.write("---")
                right.write("---")
                q25 = answer.slider('',1,7,key='q25')
                
                #26
                left.write("conservative")
                right.write("inovative")
                left.write("---")
                right.write("---")
                q26 = answer.slider('',1,7,key='q26')
                
                
                
                
                
                ueq = ueqform.form_submit_button("Submit UEQ Survey")
                if ueq is True or st.session_state['ueq']:
                    st.balloons()
                    st.session_state['ueq'] = True
                    st.success(f"Thanks {name}. Your UEQ Results will be calculated by us.")
                    st.write("---")
                    st.info("Please don't forget to download and send your results.")
                    
                
                
                
                    with open(f"{name}_{surname}_results.txt", "a") as results:
                        results.write(f"\n{60*'-'}\n{dt} - NEW ENTRY:\n{name}\n{surname}\n{age}\n{skills}\n{location}\n{60*'-'}\n")
                    
                    with open(f"{name}_{surname}_results.txt", "a") as results:
                        results.write(f"\n{60*'-'}\nTask Completed from {name} {surname}: {(st.session_state['dt_end'] - st.session_state['dt_start']).total_seconds()} seconds\n{60*'-'}\n")
                    
                    with open(f"{name}_{surname}_results.txt", "a") as results:
                        results.write(f"\n{60*'-'}\nSUS-Survey from {surname} {name}:\n{one};{two};{three};{four};{five};{six};{seven};{eight};{nine};{ten}\n{60*'-'}\nResult Score: {result_sus}\n{60*'-'}\n")
                    
                    with open(f"{name}_{surname}_results.txt", "a") as results:
                        results.write(f"{q1};{q2};{q3};{q4};{q5};{q6};{q7};{q8};{q9};{q10};{q12};{q13};{q14};{q15};{q16};{q17};{q18};{q19};{q20};{q21};{q22};{q23};{q24};{q25};{q26}")
                    
                    
                    with open(f"{name}_{surname}_results.txt", "rb") as file:
                        btn = st.download_button(
                            label="Download Data & Results",
                            data=file,
                            file_name=f'data_{name}_{surname}.txt',
                            mime='text/txt')
    
    





    
    
    
    
   
