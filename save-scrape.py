import json
mydict ={"https://www.nvcc.edu/parking/faq.html": {'Where can I park on campus?': "Campus parking designations are determined by the type of permit you have. Student parking is in 'B' lots and Faculty/Staff parking is in 'A' lots. Non-permit holders and visitors must use NOVA hourly parking options.  These include:  Passport Mobile Pay or payments via Pay Stations in hourly lots.  Parking in 'B' lots and hourly lots/garages is free after 3:45 p.m. Monday through Friday and all day on the weekends.", 'How much does parking cost at NOVA?': 'Parking permits cost $80. Visitor parking is $2 an hour with a maximum of $10 per day.', 'How can I purchase a NOVA parking permit?': 'Students may purchase their parking permits online at www.nvcc.edu/parking or at any campus Parking Services office.', 'I have a disabled parking placard. Where can I park on campus?': "Vehicles with valid DMV-issued plates or placards may park in any permit space located in an 'A', 'B', or hourly lot in addition to any designated handicap parking space on campus.", 'What are my parking options at NOVA as a visitor/non-permit holder?': "Visitors/non-permit holders may park in any hourly space for an hourly rate of $2. Visitors/non-permit holders may also utilize NOVA's hourly mobile pay option through Passport Mobile Pay to park in any 'B' Lot prior to 3:45 p.m. on weekdays.", 'How can I appeal or pay for a parking citation?': 'Customers may appeal and/or pay for a parking citation either online at www.nvcc.edu/parking or in person at any campus Parking Services office. Appeals must be submitted within 15 calendar days after issuance of the citation. Please be aware that all denied appeals are subject to a $10 processing fee.', 'Why do I have to pay to park at NOVA?': 'NOVA must generate revenue through parking permits and fees to create, maintain and manage parking lots and facilities. Virginia policy requires that parking services operate as an auxiliary enterprise; therefore, State funds cannot be used to construct, maintain or operate parking lots or garages.', 'Where can I get more information about Parking Services at NOVA?': 'You may contact NOVA Parking Customer Support at 703.323.3123 or parking@nvcc.edu. Additional information for Parking Services can be found on our website www.nvcc.edu/parking. All six campuses also have a Parking Services office with knowledgeable staff who can assist you.', 'What do I need to do if I drive a different vehicle to campus?': 'You may add and remove vehicles to your parking permit online. If you are using a new vehicle temporarily, please ensure the vehicle is linked to the permit through your parking account by visiting the Parking Portal.  You may also email parking@nvcc.edu from your NOVA email address with the vehicleaTMs license plate number and state, make, model, and color and we are able to link the vehicle to your permit for you.', 'I dropped my class/my class was canceled by the College. How do I get a refund for my parking permit?': 'Requests for student permit refunds must be received by a NOVA Campus Parking Services office within the published add/drop (census) date as listed in the Schedule of Classes.  If you are taking classes in multiple sessions, the deadline for submitting permit refund requests is the earliest census date. If a class was canceled, refund requests must be submitted to a Campus Parking Services office within three business days from the date the class was canceled.', 'I am a new faculty/staff/P-14 employee. How do I order my permit?': 'All employees are required to order their Faculty/Staff permit online at www.nvcc.edu/parking.  Once the permit order is completed, your virtual permit is effective immediately.', 'When are parking permits sold and how long are they valid?': 'Permits are available for purchase by semester as follows: Fall - August 1; Spring - December 1; Summer - May 1. Student parking permits are valid through the semester they were purchased.', 'Can I leave my vehicle overnight at a campus?': 'NOVA does not permit overnight parking at any of its campuses. If your vehicle needs to be left overnight for College business or due to an emergency please complete the Overnight Parking form. If you donaTMt have a valid NOVA Parking Permit, you can send an email to parking@nvcc.edu to request an Overnight Parking Pass.', 'I drive more than one vehicle to campus regularly. What are my parking options?': 'Student and Faculty/Staff permits may be linked to up to three vehicles. Vehicles must be properly linked to your permit prior to parking on campus. Only one vehicle linked to your permit may be parked at any NOVA campus at one time.', 'When do you enforce parking?': "Vehicles parked in student 'B' permit lots must have a valid permit until 3:45 p.m. Monday through Friday. All other lots ('A' lots, reserved spaces, etc.) are enforced at all times.", 'Is there free parking on campus?': "At the beginning of every semester, the College has a grace period for parking. Students may park in the 'B' lots for free until enforcement begins. See campus signage or the Important Dates section on the Parking website home page for exact enforcement dates. Once enforcement begins, vehicles may park without a student permit after 3:45 p.m. Monday through Friday and anytime on weekends in student 'B' lots only.", 'I am a senior citizen. Do I have to pay for parking?': 'Senior citizens who have enrolled through the Senior Citizen Tuition Waiver process may order a student parking permit online or at any Campus Parking Services office at no charge 48 hours after enrolling.', 'Do I have to be a student to purchase a parking permit?': 'Only currently-enrolled students are eligible to purchase student parking permits.', 'I have a valid parking permit for this semester. Can I park at an hourly space?': 'Since there are a limited number of hourly parking spaces, individuals with a valid permit may not park in hourly parking lots. Vehicles with valid permits are subject to receiving a citation in hourly spaces.', 'What is the Parking Infrastructure Fee? Does it pay for my parking?': 'The Parking Infrastructure fee supports the continuing maintenance, repair and improvements to the collegeaTMs infrastructure. The fee is charged to all students as part of their tuition and helps pay for many resources used by students even if they do not drive to campus, such as walkways, exterior lights, and safety improvements. If you have any further questions, please contact us.', 'Do I need to purchase a parking permit if I am riding a motorcycle to campus?': 'Motorcycles do not require a parking permit to park on campus. Each campus also has designated motorcycle parking spaces.'}}
with open("faqs.json", "r+") as fp:
    a = json.load(fp)
    a.update(mydict)
    json.dump(a,fp)